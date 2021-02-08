from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


select_style_callback = CallbackData('select', 'name')


##########################
##   21 Style Options   ##
##########################

select_style_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅ Oil Paint', callback_data='ignore_style'),
            InlineKeyboardButton(text='Oil Paint 2', callback_data=select_style_callback.new(name='oil_painting_2')),
            InlineKeyboardButton(text='Watercolor >', callback_data=select_style_callback.new(name='watercolor_painting'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Oil Paint', callback_data=select_style_callback.new(name='oil_painting')),
            InlineKeyboardButton(text='✅ Oil Paint 2', callback_data='ignore_style'),
            InlineKeyboardButton(text='Watercolor >', callback_data=select_style_callback.new(name='watercolor_painting')),
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Oil Paint 2', callback_data=select_style_callback.new(name='oil_painting_2')),
            InlineKeyboardButton(text='✅ Watercolor', callback_data='ignore_style'),
            InlineKeyboardButton(text='Pencil >', callback_data=select_style_callback.new(name='pencil_sketch'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Watercolor', callback_data=select_style_callback.new(name='watercolor_painting')),
            InlineKeyboardButton(text='✅ Pencil', callback_data='ignore_style'),
            InlineKeyboardButton(text='Digital >', callback_data=select_style_callback.new(name='digital_art'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Pencil', callback_data=select_style_callback.new(name='pencil_sketch')),
            InlineKeyboardButton(text='✅ Digital', callback_data='ignore_style'),
            InlineKeyboardButton(text='Stained-glass >', callback_data=select_style_callback.new(name='stained-glass_window'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Digital', callback_data=select_style_callback.new(name='digital_art')),
            InlineKeyboardButton(text='✅ Stained-glass', callback_data='ignore_style'),
            InlineKeyboardButton(text='Pollock >', callback_data=select_style_callback.new(name='pollock_number_23'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Stained-glass', callback_data=select_style_callback.new(name='stained-glass_window')),
            InlineKeyboardButton(text='✅ Pollock', callback_data='ignore_style'),
            InlineKeyboardButton(text='Kahlo >', callback_data=select_style_callback.new(name='kahlo_self-portrait_with_necklace_of_thorns'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_8 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Pollock', callback_data=select_style_callback.new(name='pollock_number_23')),
            InlineKeyboardButton(text='✅ Kahlo', callback_data='ignore_style'),
            InlineKeyboardButton(text='Escher >', callback_data=select_style_callback.new(name='escher_hand_with_reflecting_sphere'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Kahlo', callback_data=select_style_callback.new(name='kahlo_self-portrait_with_necklace_of_thorns')),
            InlineKeyboardButton(text='✅ Escher', callback_data='ignore_style'),
            InlineKeyboardButton(text='Picasso >', callback_data=select_style_callback.new(name='picasso_muse'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Escher', callback_data=select_style_callback.new(name='escher_hand_with_reflecting_sphere')),
            InlineKeyboardButton(text='✅ Picasso', callback_data='ignore_style'),
            InlineKeyboardButton(text='Picabia >', callback_data=select_style_callback.new(name='picabia_udnie'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_11 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Picasso', callback_data=select_style_callback.new(name='picasso_muse')),
            InlineKeyboardButton(text='✅ Picabia', callback_data='ignore_style'),
            InlineKeyboardButton(text='Kandinsky >', callback_data=select_style_callback.new(name='kandinsky_composition_vii'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_12 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Picabia', callback_data=select_style_callback.new(name='picabia_udnie')),
            InlineKeyboardButton(text='✅ Kandinsky', callback_data='ignore_style'),
            InlineKeyboardButton(text='Picasso 2 >', callback_data=select_style_callback.new(name='picasso_seated_nude'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_13 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Kandinsky', callback_data=select_style_callback.new(name='kandinsky_composition_vii')),
            InlineKeyboardButton(text='✅ Picasso 2', callback_data='ignore_style'),
            InlineKeyboardButton(text='Picasso 3 >', callback_data=select_style_callback.new(name='picasso_self-portrait'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_14 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Picasso 2', callback_data=select_style_callback.new(name='picasso_seated_nude')),
            InlineKeyboardButton(text='✅ Picasso 3', callback_data='ignore_style'),
            InlineKeyboardButton(text='Delaunay >', callback_data=select_style_callback.new(name='delaunay_portrait_of_jean_metzinger'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_15 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Picasso 3', callback_data=select_style_callback.new(name='picasso_self-portrait')),
            InlineKeyboardButton(text='✅ Delaunay', callback_data='ignore_style'),
            InlineKeyboardButton(text='Matisse >', callback_data=select_style_callback.new(name='matisse_woman_with_hat'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_16 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Delaunay', callback_data=select_style_callback.new(name='delaunay_portrait_of_jean_metzinger')),
            InlineKeyboardButton(text='✅ Matisse', callback_data='ignore_style'),
            InlineKeyboardButton(text='Munch >', callback_data=select_style_callback.new(name='munch_scream'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_17 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Matisse', callback_data=select_style_callback.new(name='matisse_woman_with_hat')),
            InlineKeyboardButton(text='✅ Munch', callback_data='ignore_style'),
            InlineKeyboardButton(text='Van Gogh >', callback_data=select_style_callback.new(name='van_gogh_starry_night'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_18 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Munch', callback_data=select_style_callback.new(name='munch_scream')),
            InlineKeyboardButton(text='✅ Van Gogh', callback_data='ignore_style'),
            InlineKeyboardButton(text='Hokusai >', callback_data=select_style_callback.new(name='hokusai_great_wave_off_kanagawa'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_19 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Van Gogh', callback_data=select_style_callback.new(name='van_gogh_starry_night')),
            InlineKeyboardButton(text='✅ Hokusai', callback_data='ignore_style'),
            InlineKeyboardButton(text='Turner >', callback_data=select_style_callback.new(name='turner_shipwreck'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_20 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Hokusai', callback_data=select_style_callback.new(name='hokusai_great_wave_off_kanagawa')),
            InlineKeyboardButton(text='✅ Turner', callback_data='ignore_style'),
            InlineKeyboardButton(text='Mosaic', callback_data=select_style_callback.new(name='roman_mosaic'))
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)

select_style_21 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='< Hokusai', callback_data=select_style_callback.new(name='hokusai_great_wave_off_kanagawa')),
            InlineKeyboardButton(text='Turner', callback_data=select_style_callback.new(name='turner_shipwreck')),
            InlineKeyboardButton(text='✅ Mosaic', callback_data='ignore_style')
        ],
        [
            InlineKeyboardButton(text='Select style', callback_data='accept_style')
        ]
    ]
)


####################
##   Style Menu   ##
####################

style_menu = {
    'oil_painting': select_style_1,
    'oil_painting_2': select_style_2,
    'watercolor_painting': select_style_3,
    'pencil_sketch': select_style_4,
    'digital_art': select_style_5,
    'stained-glass_window': select_style_6,
    'pollock_number_23': select_style_7, # 1948
    'kahlo_self-portrait_with_necklace_of_thorns': select_style_8, # 1940
    'escher_hand_with_reflecting_sphere': select_style_9, # 1935
    'picasso_muse': select_style_10, # 1935
    'picabia_udnie': select_style_11, # 1913
    'kandinsky_composition_vii': select_style_12, # 1913
    'picasso_seated_nude': select_style_13, # 1910
    'picasso_self-portrait': select_style_14, # 1907
    'delaunay_portrait_of_jean_metzinger': select_style_15, # 1906
    'matisse_woman_with_hat': select_style_16, # 1905
    'munch_scream': select_style_17, # 1893
    'van_gogh_starry_night': select_style_18, # 1889
    'hokusai_great_wave_off_kanagawa': select_style_19, # 1833
    'turner_shipwreck': select_style_20, # 1805
    'roman_mosaic': select_style_21 # 300 CE
}
