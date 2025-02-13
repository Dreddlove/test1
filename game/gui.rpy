init offset = -2









init python:
    gui.init(1280, 720)













define gui.accent_color = '#cc0000'


define gui.idle_color = '#555555'



define gui.idle_small_color = '#aaaaaa'


define gui.hover_color = '#cc0000'



define gui.selected_color = '#ffffff'


define gui.insensitive_color = '#5555557f'



define gui.muted_color = '#510000'
define gui.hover_muted_color = '#7a0000'


define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'





define gui.text_font = "images/expressway-free.regular.ttf"


define gui.name_text_font = "images/expressway-free.regular.ttf"


define gui.interface_text_font = "images/expressway-free.regular.ttf"


define gui.text_size = 22


define gui.name_text_size = 30


define gui.interface_text_size = 24


define gui.label_text_size = 28


define gui.notify_text_size = 16


define gui.title_text_size = 60





define gui.main_menu_background = "images/emblem_bg.jpg"
define gui.game_menu_background = "gui/overlay/game_menu.png"


define gui.show_name = False








define gui.textbox_height = 219



define gui.textbox_yalign = 1.0




define gui.name_xpos = 184
define gui.name_ypos = 1



define gui.name_xalign = 0.0



define gui.namebox_width = 331
define gui.namebox_height = 46



define gui.namebox_borders = Borders(5, 5, 5, 5)



define gui.namebox_tile = False





define gui.dialogue_xpos = 300
define gui.dialogue_ypos = 70


define gui.dialogue_width = 600



define gui.dialogue_text_xalign = 0.0








define gui.button_width = None
define gui.button_height = 36


define gui.button_borders = Borders(4, 4, 4, 4)



define gui.button_tile = False


define gui.button_text_font = gui.interface_text_font


define gui.button_text_size = gui.interface_text_size


define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color



define gui.button_text_xalign = 0.0








define gui.radio_button_borders = Borders(25, 4, 4, 4)

define gui.check_button_borders = Borders(25, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 16
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = "FFF"












define gui.choice_button_width = 500
define gui.choice_button_height = 42
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(50, 5, 50, 5)

define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#ffffff"
define gui.choice_button_text_hover_color = "#cc0000"
define gui.choice_button_text_outlines = [ (absolute(3), "#000000", absolute(0), absolute(0)) ]
define gui.choice_button_text_font = "images/libel-suit.regular.ttf"









define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color


define config.thumbnail_width = 256
define config.thumbnail_height = 144


define gui.file_slot_cols = 3
define gui.file_slot_rows = 2









define gui.navigation_xpos = 40


define gui.skip_ypos = 10


define gui.notify_ypos = 20


define gui.choice_spacing = 22


define gui.navigation_spacing = 4


define gui.pref_spacing = 10


define gui.pref_button_spacing = 0


define gui.page_spacing = 0


define gui.slot_spacing = 10


define gui.main_menu_text_xalign = 1.0








define gui.frame_borders = Borders(4, 4, 4, 4)


define gui.confirm_frame_borders = Borders(40, 40, 40, 40)


define gui.skip_frame_borders = Borders(16, 5, 50, 5)


define gui.notify_frame_borders = Borders(30, 0, 86, 0)


define gui.frame_tile = False











define gui.bar_size = 36
define gui.scrollbar_size = 12
define gui.slider_size = 30


define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False


define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)


define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)



define gui.unscrollable = "hide"







define config.history_length = 250



define gui.history_height = 140



define gui.history_name_xpos = 150
define gui.history_name_ypos = 0
define gui.history_name_width = 150
define gui.history_name_xalign = 1.0


define gui.history_text_xpos = 170
define gui.history_text_ypos = 5
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0







define gui.nvl_borders = Borders(0, 10, 0, 20)



define gui.nvl_height = 115



define gui.nvl_spacing = 10



define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0


define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0



define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0


define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0







define gui.language = "unicode"






init python:



    if renpy.variant("touch"):
        
        gui.quick_button_borders = Borders(40, 14, 40, 0)



    if renpy.variant("small"):
        
        
        gui.text_size = 25
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 45
        gui.label_text_size = 36
        
        
        
        
        
        
        
        
        gui.choice_button_width = 800
        gui.choice_button_height = 65
        gui.choice_button_tile = True
        gui.choice_button_text_size = 36
        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10
        
        gui.history_height = 190
        gui.history_text_width = 690
        
        
        gui.file_slot_cols = 3
        gui.file_slot_rows = 2
        
        
        gui.nvl_height = 170
        
        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325
        
        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5
        
        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20
        
        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
        
        
        gui.quick_button_text_size = 35
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
