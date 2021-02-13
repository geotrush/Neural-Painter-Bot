import os
import gc
import asyncio
import logging
import threading
from io import BytesIO

from config import *
from painting_mode.test import *
from stylization_mode.test import *
from stylization_mode.style_menu import *

from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentType
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, ChatActions, CallbackQuery, InputMediaPhoto


####################################
##   Neural Painter Bot 🧠👨‍🎨🤖   ##
####################################

'''
Greetings, Earthling 🖖

I'm the Neural Painter, and it'll be my great pleasure to
stylize and paint any picture your heart desires! 😍

Take into account that:

— Both stylization and painting take a minute to complete ⏳

— Right now I only have square 350×350 canvases left ◻️

— At this point I'm only able to paint like Van Gogh 🖼

I can't promise to capture every detail, but
I'll do my best to complete your picture in due time
and with finesse worthy of the Great Masters! 👨‍🎨
'''

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Configure logging
logging.basicConfig(format='%(asctime)s - %(message)s',
                    level=logging.INFO)


##############################
##   Groups of Bot States   ##
##############################

class FNSTStates(StatesGroup):
    '''
    Fast Neural Style Transfer States
    '''
    style_menu = State()
    upload_content = State()
    run_fnst = State()


class GNSTStates(StatesGroup):
    '''
    Generative Neural Style Transfer States
    '''
    upload_content = State()
    run_gnst = State()


###############################
##   Core Message Handlers   ##
###############################

@dp.message_handler(commands=['start', 'help'], state='*')
async def help(message: Message):
    '''
    Shows the list of available commands
    '''
    logging.info('Helping...')
    await message.answer('/help — View the list of available options ❓\n'
                         '/reset — Reset, if you\'ve uploaded the wrong images 🔄\n'
                         '/stylization — Select a style to transfer onto your image 🌈\n'
                         '/painting — Upload your image to turn it into a painting 🎨\n'
                         '/about — Check out the source code, if you\'re curious 🤓\n')


@dp.message_handler(commands=['reset'], state='*')
async def reset(message: Message, state: FSMContext):
    '''
    Allows to reset bot state
    '''
    logging.info('Resetting...')
    await state.finish()
    for image_file in os.listdir():
        if (image_file.endswith('.jpg')):
            os.remove(image_file)
    await message.answer('Changed your mind? Alright, let\'s start over 🙄')


@dp.message_handler(commands=['stylization'], state=None)
async def stylization(message: Message, state: FSMContext):
    '''
    Enables stylization mode
    '''
    await message.answer('You\'ve chosen stylization 🌈')
    logging.info('Stylization — selecting style...')
    await FNSTStates.style_menu.set()
    async with state.proxy() as data:
        data['style_path'] = 'stylization_mode/style_images/oil_painting.jpg'
        await message.answer_photo(open(data['style_path'], 'rb'),
                                        caption='1️⃣ Select one of 21 styles...',
                                        reply_markup=select_style_1)


@dp.message_handler(commands=['painting'], state=None)
async def painting(message: Message):
    '''
    Enables painting mode
    '''
    await message.answer('You\'ve chosen painting 🎨')
    logging.info('Painting — uploading content...')
    await GNSTStates.upload_content.set()
    await message.answer('1️⃣ Upload a content image...')


@dp.message_handler(commands=['about'], state='*')
async def about(message: Message):
    '''
    Shows bot info
    '''
    await message.answer('Author: @tensorush 👨‍💻\n'
                         'GitHub: https://github.com/geotrush/Neural-Painter-Bot')


@dp.message_handler(state=None, content_types=ContentType.ANY)
async def other(message: Message):
    '''
    Handles unknown commands
    '''
    await message.answer('Sorry, I don\'t get what you\'re saying 🤨')


####################################
##   Fast Neural Style Transfer   ##
####################################

@dp.callback_query_handler(select_style_callback.filter(), state=FNSTStates.style_menu)
async def select_style(call: CallbackQuery, callback_data: dict, state: FSMContext):
    '''
    Navigates the 21 style options
    '''
    name = callback_data.get('name')
    await call.message.edit_media(InputMediaPhoto(open(f'stylization_mode/style_images/{name}.jpg', 'rb')),
                                  reply_markup=style_menu[name])
    async with state.proxy() as data:
        data['style_path'] = f'stylization_mode/style_images/{name}.jpg'


@dp.callback_query_handler(text='ignore_style', state=FNSTStates.style_menu)
async def ignore_style(call: CallbackQuery):
    '''
    Ignores button input for the selected style
    '''
    await call.answer()


@dp.callback_query_handler(text='accept_style', state=FNSTStates.style_menu)
async def accept_style(call: CallbackQuery):
    '''
    Accepts the chosen style
    '''
    await call.answer()
    await call.message.answer('Splendid! 🎇')
    logging.info('Stylization — uploading content...')
    await FNSTStates.upload_content.set()
    await call.message.answer('2️⃣ Upload a content image...')


@dp.message_handler(state=FNSTStates.upload_content, content_types=ContentType.ANY)
async def upload_content(message: Message, state: FSMContext):
    '''
    Downloads content image and executes FNST in another thread
    '''
    # Check if the message contains a photo
    if not message.photo:
        return await message.reply('Please try again - just send a compressed JPEG or PNG 🖼')
    # Get content path
    content_path = str(message.from_user.id) + '_content.jpg'
    # Download content image
    await message.photo[-1].download(content_path)
    await message.answer('Brilliant! 💎\n')
    # Prepare to run FNST
    logging.info('Stylization — running FNST...')
    await FNSTStates.run_fnst.set()
    await message.answer('3️⃣ Be patient — it\'ll take half a minute at most ⏳')
    # Signal typing
    await ChatActions.typing()
    # Get style path
    input_data = await state.get_data()
    style_path = input_data['style_path']
    # Run FNST in a separate thread
    thread = threading.Thread(target=lambda message, state, content_path, style_path:
                              asyncio.run(run_fnst(message, state, content_path, style_path)),
                              args=(message, state, content_path, style_path))
    thread.start()


async def run_fnst(message: Message, state: FSMContext, content_path, style_path):
    '''
    Runs Fast Neural Style Transfer with MSG-Net
    '''
    # Instantiate FNST class
    fnst = FNST(content_path, style_path)
    # Run FNST
    stylized_image, time_passed = fnst.transfer_style()
    # Send stylized image
    bytes = BytesIO()
    bytes.name = 'stylized_image.jpg'
    stylized_image.save(bytes, 'JPEG')
    bytes.seek(0)
    bot_fnst = Bot(token=BOT_TOKEN)
    await bot_fnst.send_photo(message.chat.id,
                              photo=bytes,
                              caption=f'Stylization took only {time_passed} seconds ⏰')
    await bot_fnst.close()
    # Clear memory storage
    os.remove(content_path)
    del fnst
    gc.collect()
    # End FNST state
    logging.info('Stylization — FNST completed!')
    await state.finish()


##########################################
##   Generative Neural Style Transfer   ##
##########################################

@dp.message_handler(state=GNSTStates.upload_content, content_types=ContentType.ANY)
async def upload_content(message: Message, state: FSMContext):
    '''
    Downloads content image and executes GNST in another thread
    '''
    # Check if the message contains a photo
    if not message.photo:
        return await message.reply('Please try again - just send a compressed JPEG or PNG 🖼')
    # Get content path
    content_path = str(message.from_user.id) + '_content.jpg'
    # Download content image
    await message.photo[-1].download(content_path)
    await message.answer('Brilliant! 💎\n')
    # Prepare to run GNST
    logging.info('Painting — running GNST...')
    await GNSTStates.run_gnst.set()
    await message.answer('2️⃣ Be patient — it\'ll take half a minute at most ⏳')
    # Signal typing
    await ChatActions.typing()
    # Run GNST in a separate thread
    thread = threading.Thread(target=lambda message, state, content_path:
                              asyncio.run(run_gnst(message, state, content_path)),
                              args=(message, state, content_path))
    thread.start()


async def run_gnst(message: Message, state: FSMContext, content_path):
    '''
    Runs Generative Neural Style Transfer with CycleGAN
    '''
    # Instantiate GNST class
    gnst = GNST(content_path)
    # Run GNST
    painted_image, time_passed = gnst.transfer_style()
    # Send stylized image
    bytes = BytesIO()
    bytes.name = 'painted_image.jpg'
    painted_image.save(bytes, 'JPEG')
    bytes.seek(0)
    bot_gnst = Bot(token=BOT_TOKEN)
    await bot_gnst.send_photo(message.chat.id,
                              photo=bytes,
                              caption=f'Stylization took only {time_passed} seconds ⏰')
    await bot_gnst.close()
    # Clear memory storage
    os.remove(content_path)
    del gnst
    gc.collect()
    # End GNST state
    logging.info('Stylization — GNST completed!')
    await state.finish()


##############################
##   Bot Control Settings   ##
##############################

async def on_startup(dp: Dispatcher):
    logging.warning('Starting up...')
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp: Dispatcher):
    logging.warning('Shutting down...')
    for image_file in os.listdir():
        if (image_file.endswith('.jpg')):
            os.remove(image_file)
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=False,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )
