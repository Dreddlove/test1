













define config.name = _("The Price Of Flesh")
define config.steam_appid = 1940040










define config.version = "1.2.8"




define gui.about = _("")






define build.name = "ThePriceOfFlesh"
define build.directory_name = "ThePriceOfFlesh"

define config.rollback_length = 20
define config.hard_rollback_limit = 20






define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = "music/main_menu.mp3"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.after_load_transition = dissolve




define config.end_game_transition = dissolve
define config.end_splash_transition = dissolve














define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "TheHunt-1500591670"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.rpy', None)
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')









    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
