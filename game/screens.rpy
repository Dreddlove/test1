init offset = -1










style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        if who is not None:
            window:
                style "namebox"
                text who id "who"

        text what id "what"
        button:
            style "dialogue_button_map_style"
            if phase == "event":
                null
            elif "item_map" in inventory or "item_celia_map" in inventory or event_derek_map_activation == 1:
                if gamepath == "mason":
                    action If(renpy.get_screen("map_mason"), Hide("map_mason"), ShowTransient("map_mason"))
                if gamepath == "celia":
                    action If(renpy.get_screen("map_celia"), Hide("map_celia"), ShowTransient("map_celia"))
                if gamepath == "derek":
                    action If(renpy.get_screen("map_derek"), Hide("map_derek"), ShowTransient("map_derek"))
            else:
                null
            text "Map":
                style "dialogue_button_text"

        $ chance = renpy.random.randint(1,100)
        if gamepath == "mason" and chance <= 10 and sanity < 40 and event_mason_sanity_1 == 0:
            button:
                style "dialogue_button_inventory_style"
                if phase == "event":
                    null
                else:
                    if renpy.get_screen("inventory"):
                        action (Hide("inventory"), Hide("inventory_item"))
                    else:
                        action (If(renpy.get_screen("fakeinventory"), Hide("fakeinventory"), ShowTransient("fakeinventory")), Hide("inventory_item"))
                text "Inventory":
                    style "dialogue_button_text"
        else:
            button:
                style "dialogue_button_inventory_style"
                if phase == "event":
                    null
                else:
                    if renpy.get_screen("fakeinventory"):
                        action (Hide("fakeinventory"), Hide("inventory_item"))
                    else:
                        action (If(renpy.get_screen("inventory"), Hide("inventory"), ShowTransient("inventory")), Hide("inventory_item"))
                text "Inventory":
                    style "dialogue_button_text"
        $ chance2 = renpy.random.randint(1,100)
        if gamepath == "mason" and chance2 <= 10 and sanity < 40 and event_mason_sanity_2 == 0:
            button:
                style "dialogue_button_actions_style"
                if phase == "event":
                    null
                else:
                    if renpy.get_screen("actions"):
                        action Hide("actions")
                    else:
                        action If(renpy.get_screen("fakeactions"), Hide("fakeactions"), ShowTransient("fakeactions"))
                text "Actions":
                    style "dialogue_button_text"
        else:
            button:
                style "dialogue_button_actions_style"
                if phase == "event":
                    null
                else:
                    if renpy.get_screen("fakeactions"):
                        action Hide("fakeactions")
                    else:
                        action If(renpy.get_screen("actions"), Hide("actions"), ShowTransient("actions"))
                text "Actions":
                    style "dialogue_button_text"
        button:
            style "dialogue_button_status_style"
            if gamepath != "start":
                action If(renpy.get_screen("status"), Hide("status"), ShowTransient("status"))
            else:
                null
            text "Status":
                style "dialogue_button_text"





    add SideImage() xalign 0.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("images/dialogue.png", xalign=0.5, yalign=1.0)
style window:
    variant "small"
    background Image("images/dialogue_phone.png", xalign=0.5, yalign=1.0)

style dialogue_button_map_style:
    xsize 160
    ysize 47
    right_padding 10
    top_padding 3
    ypos 55
    xpos 910
    background "images/dialogue_button_map.png"
    hover_background "images/dialogue_button_map_hover.png"
    insensitive_background "images/dialogue_button_map_insensitive.png"
style dialogue_button_map_style:
    variant "small"
    xsize 176
    ysize 58
    ypos 48
    background "images/dialogue_button_map_large.png"
    hover_background "images/dialogue_button_map_hover_large.png"
    insensitive_background "images/dialogue_button_map_insensitive_large.png"
style dialogue_button_inventory_style:
    xsize 163
    ysize 45
    right_padding 10
    top_padding 3
    ypos 55
    xpos 1090
    background "images/dialogue_button_inventory.png"
    hover_background "images/dialogue_button_inventory_hover.png"
    insensitive_background "images/dialogue_button_inventory_insensitive.png"
style dialogue_button_inventory_style:
    variant "small"
    xsize 179
    ysize 58
    ypos 48
    background "images/dialogue_button_inventory_large.png"
    hover_background "images/dialogue_button_inventory_hover_large.png"
    insensitive_background "images/dialogue_button_inventory_insensitive_large.png"
style dialogue_button_actions_style:
    xsize 164
    ysize 42
    right_padding 10
    top_padding 3
    ypos 115
    xpos 906
    background "images/dialogue_button_actions.png"
    hover_background "images/dialogue_button_actions_hover.png"
    insensitive_background "images/dialogue_button_actions_insensitive.png"
style dialogue_button_actions_style:
    variant "small"
    xsize 180
    ysize 58
    background "images/dialogue_button_actions_large.png"
    hover_background "images/dialogue_button_actions_hover_large.png"
    insensitive_background "images/dialogue_button_actions_insensitive_large.png"
style dialogue_button_status_style:
    xsize 163
    ysize 42
    right_padding 10
    top_padding 3
    ypos 115
    xpos 1090
    background "images/dialogue_button_status.png"
    hover_background "images/dialogue_button_status_hover.png"
    insensitive_background "images/dialogue_button_status_insensitive.png"
style dialogue_button_status_style:
    variant "small"
    xsize 179
    ysize 58
    background "images/dialogue_button_status_large.png"
    hover_background "images/dialogue_button_status_hover_large.png"
    insensitive_background "images/dialogue_button_status_insensitive_large.png"
style dialogue_button_text:
    xalign 1.0
    size 20
    font "images/libel-suit.regular.ttf"
    color "fff"
    hover_color "cc0000"
    insensitive_color "444"
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]

style dialogue_button_text:
    variant "small"
    size 36

style dialogue_button_status_text is dialogue_button_text
style dialogue_button_inventory_text is dialogue_button_text
style dialogue_button_map_text is dialogue_button_text
style dialogue_button_actions_text is dialogue_button_text

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("images/dialogue_name.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    xpos 70
    size 25
    yalign 0.3
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]












screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action







style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")



screen timer_choice(items):
    style_prefix "timer_choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define config.narrator_menu = True


style timer_choice_vbox is vbox
style timer_choice_button is button
style timer_choice_button_text is button_text

style timer_choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style timer_choice_button is default:
    properties gui.button_properties("choice_button")
    background None


style timer_choice_button_text is default:
    properties gui.button_text_properties("choice_button")







screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            xanchor 0.5
            if not renpy.variant("small"):
                ypos 684
                xpos 973
            else:
                ypos 657
                xpos 597

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            if not renpy.variant("small"):
                textbutton _("Save") action ShowMenu('save')
            if not renpy.variant("small"):
                textbutton _("Menu") action ShowMenu('preferences')
            else:
                textbutton _("Menu") action ShowMenu('save')
            if not renpy.variant("small"):
                textbutton _("Help") action ShowMenu('help')
                text _("{noalt}H - toggle overlay{/noalt}") style ("menu_tiny")




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    yoffset -2

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    font "images/libel-suit.regular.ttf"
    hover_color "FFF"
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]
style menu_tiny is quick_button_text:
    color "666"
    size 14










screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        if main_menu:

            textbutton _("Start") action Start()

        else:



            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")





        textbutton _("Collections") action ShowMenu("collections")

        textbutton _("Credits") action ShowMenu("credits")

        textbutton _("Warnings") action ShowMenu("warnings")

        if renpy.variant("pc"):


            textbutton _("Help") action ShowMenu("help")


            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text:
    color "fff"
    hover_color "cc0000"
    size 35
    font "images/libel-suit.regular.ttf"

style navigation_button:
    background None
    hover_background "images/textarrow.png"
    hover_left_padding 16
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")








transform menu_logo:
    "images/logo.png"
    xalign 0.5
    yalign 0.5
transform mm_sway_back:
    xalign 0.5
    yalign 0.5
    easein 2.2 xoffset 25 yoffset 25
    easein 2.2 xoffset -20 yoffset 50
    easein 2.2 xoffset -40 yoffset 20
    easein 2.2 xoffset 35 yoffset -40
    easein 2.2 xoffset 15 yoffset 10
    easein 2.2 xoffset -50 yoffset -50
    easein 2.2 xoffset -25 yoffset -40
    easein 2.2 xoffset -15 yoffset 30
    easein 2.2 xoffset 30 yoffset -20
    easein 2.2 xoffset 40 yoffset 35
    easein 2.2 xoffset -30 yoffset -15
    easein 2.2 xoffset 10 yoffset -10
    easein 2.2 xoffset 0 yoffset 0
    repeat
transform mm_sway_fore:
    xalign 0.5
    yalign 0.5
    easein_expo 2.2 xoffset 50 yoffset 50
    easein_expo 2.2 xoffset -40 yoffset 100
    easein_expo 2.2 xoffset -80 yoffset 40
    easein_expo 2.2 xoffset 70 yoffset -80
    easein_expo 2.2 xoffset 30 yoffset 20
    easein_expo 2.2 xoffset -100 yoffset -100
    easein_expo 2.2 xoffset -50 yoffset -80
    easein_expo 2.2 xoffset -30 yoffset 60
    easein_expo 2.2 xoffset 60 yoffset -40
    easein_expo 2.2 xoffset 80 yoffset 70
    easein_expo 2.2 xoffset -60 yoffset -30
    easein_expo 2.2 xoffset 20 yoffset -20
    easein_expo 2.2 xoffset 0 yoffset 0
    repeat

screen main_menu():

    $ derek_endings_complete = len(persistent.endings_derek)
    $ mason_endings_complete = len(persistent.endings_mason)
    $ celia_endings_complete = len(persistent.endings_celia)




    style_prefix "main_menu" tag menu

    add "images/main_menu_background.jpg" at mm_sway_back
    if derek_endings_complete >= 21:
        add "images/main_menu_background_red.png" at mm_sway_back
    if mason_endings_complete >= 15:
        add "images/main_menu_background_green.png" at mm_sway_back
    if celia_endings_complete >= 14:
        add "images/main_menu_background_blue.png" at mm_sway_back
    add "mm_foregound" at mm_sway_fore


    frame




    use navigation

    add Text("Version [config.version!t]",style="versionstyle")
    if "cg_fox_keep" in persistent.cgs_fox:
        add "badge_foxlogo" xpos 1055 ypos 25

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True
    background "images/titlecard_menubg.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=False)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style thehuntstyle:
    xpos 910
    ypos 630
    color "aa0000"
    size 60
    font "images/feral.regular.ttf"
    outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]
style versionstyle:
    xpos 10
    ypos 682
    color "#555"
    size 20
    font "images/expressway-free.regular.ttf"
    outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]











screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        if renpy.get_screen("load"):
            style "game_menu_outer_frame_green"
        elif renpy.get_screen("save"):
            style "game_menu_outer_frame_red"
        elif renpy.get_screen("collections"):
            style "game_menu_outer_frame_blue"
        elif renpy.get_screen("preferences"):
            style "game_menu_outer_frame_yellow"
        elif renpy.get_screen("credits"):
            style "game_menu_outer_frame_pink"
            vbox:
                add 'gyg_gore' xpos 1190 ypos -45
            vbox:
                xalign 0.5
                text "GORE by Graveyardguy" style "gore_title"
                null height 3
                hbox:
                    xalign 0.5
                    imagebutton auto "button_play_%s.png" action Play("music", "music/Graveyardguy_Gore.mp3", selected=True)
                    imagebutton auto "button_pause_%s.png" action Stop("music")
                null height 3
                hbox:
                    xalign 0.5
                    textbutton "< Download >" action OpenURL("https://music.apple.com/us/album/gore-single/1588494669") style "gore_buttons"
                    null width 5
                    textbutton "< Stream >" action OpenURL("https://open.spotify.com/track/6yoEOFr35rkI7VnuoCvGno?autoplay=true") style "gore_buttons"
                xpos 1015 ypos -100

        else:
            style "game_menu_outer_frame"

        hbox:


            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        has vbox
                        transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _(u"Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text:
    color "#ffffff"

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"
style game_menu_outer_frame_red is game_menu_outer_frame:
    background "gui/overlay/game_menu_red.png"
style game_menu_outer_frame_blue is game_menu_outer_frame:
    background "gui/overlay/game_menu_blue.png"
style game_menu_outer_frame_yellow is game_menu_outer_frame:
    background "gui/overlay/game_menu_yellow.png"
style game_menu_outer_frame_green is game_menu_outer_frame:
    background "gui/overlay/game_menu_green.png"
style game_menu_outer_frame_pink is game_menu_outer_frame:
    background "gui/overlay/game_menu_pink.png"
style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color "#ffffff"
    yalign 0.5
    font "images/feral.regular.ttf"
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

style gore_title:
    size 18
    color "#cc0000"
style gore_buttons:
    size 12
style gore_buttons_text:
    size 12
    color "#cc0000"
    hover_color "#ffffff"









screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size




screen credits():
    tag menu






    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        vbox:
            xalign 0.5
            text _("Music/Sound") style "credits_title" at center
            text _("Main Menu - Adaptive Behaviors by BARBATUS") style "credits_1" at center
            text _("Credits - GORE by Graveyardguy") style "credits_1" at center
            text _("Desert Wandering - Achtung by BARBATUS") style "credits_1" at center
            text _("Desert Wandering - Warnung by BARBATUS") style "credits_1" at center
            text _("Celia's Basement - Women Beat Their Men by BARBATUS") style "credits_1" at center
            text _("??? - Going Up by BARBATUS") style "credits_1" at center
            text _("All music/consultation for DLC \"The Show Must Go On\" by BARBATUS") style "credits_1" at center
            text _("Additional music purchased from Envato.com") style "credits_1" at center
            text _("Sound effects purchased from Zapsplat.com") style "credits_1" at center
            null height 20
            text _("Check out BARBATUS at Bandcamp to hear his work!") style "credits_1" at center
            text _("He also works on brutal gore comics and art at barbatus.neocities.org ;)") style "credits_1" at center
            null height 20
            text _("Engine") style "credits_title" at center
            text _("Ren'Py") style "credits_1" at center
            null height 20
            text _("Animated Secret Chibi Art") style "credits_title" at center
            text _("Darqx") style "credits_1" at center
            null height 20
            text _("Special Character Designs") style "credits_title" at center
            text _("Tom - Josie Smith") style "credits_1" at center
            text _("Jaqueline - Vivian") style "credits_1" at center
            null height 20
            text _("Alpha Testers") style "credits_title" at center
            text _("Josie Smith {image=images/credits_separator.png} Slashesotron {image=images/credits_separator.png} Stanley Cosmos {image=images/credits_separator.png} Clover {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Rini {image=images/credits_separator.png} Tweakerwolf") style "credits_1" at center
            null height 20
            text _("Special Thanks") style "credits_title" at center
            text _("Mr Fishess - for helping set up the Android version") style "credits_1" at center
            null height 20
            text _("Financial Supporters") style "credits_title" at center
            text _("These people put food on my table and clothes on my back. If it weren't for them, this game wouldn't exist.") style "credits_1" at center
            null height 20
            text _("Month 1 - Framework Programming") style "credits_2" at left
            frame style "credits_month":
                text _("KuramiKami {image=images/credits_separator.png} Mori {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Ryan Rae {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Felix M {image=images/credits_separator.png} Mogshade {image=images/credits_separator.png} Lara Yee {image=images/credits_separator.png} alyxtried") style "credits_1" at center
            text _("Month 2 - Programming and Writing") style "credits_2" at left
            frame style "credits_month":
                text _("Lance Lyons {image=images/credits_separator.png} Elway {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} Rogue M. {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Felix M {image=images/credits_separator.png} Mogshade {image=images/credits_separator.png} Lara Yee {image=images/credits_separator.png} KuramiKami {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Ryan Rae {image=images/credits_separator.png} Yarre {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} pin3appl3dtogo") style "credits_1" at center
            text _("Month 3 - Programming and Writing") style "credits_2" at left
            frame style "credits_month":
                text _("Lance Lyons {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Mogshade {image=images/credits_separator.png} Lara Yee {image=images/credits_separator.png} KuramiKami {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Ryan Rae {image=images/credits_separator.png} Yarre {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} pin3appl3dtogo {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Dorian Richter") style "credits_1" at center
            text _("Month 4 - Programming and Writing") style "credits_2" at left
            frame style "credits_month":
                text _("Lance Lyons {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Mogshade {image=images/credits_separator.png} Lara Yee {image=images/credits_separator.png} KuramiKami {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ryan Rae {image=images/credits_separator.png} Yarre {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} pin3appl3dtogo {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Selly {image=images/credits_separator.png} ZizanieDreams {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} Alyssa {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Cyglyce {image=images/credits_separator.png} Mininjake") style "credits_1" at center
            text _("Month 5 - Programming and Writing") style "credits_2" at left
            frame style "credits_month":
                text _("Malpertuis {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Lara Yee {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ryan Rae {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} pin3appl3dtogo {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} Alyssa {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Baphomet-tan {image=images/credits_separator.png} Fini") style "credits_1" at center
            text _("Month 6 - Programming and Writing") style "credits_2" at left
            frame style "credits_month":
                text _("Malpertuis {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Lara Yee {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ryan Rae {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} pin3appl3dtogo {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} Alyssa {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Fini {image=images/credits_separator.png} Stanley Cosmos {image=images/credits_separator.png} Onyx-Menhera") style "credits_1" at center
            text _("Month 7 - UI and Placeholder Sketch Art") style "credits_2" at left
            frame style "credits_month":
                text _("Malpertuis {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ryan Rae {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} pin3appl3dtogo {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} Alyssa {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Fini {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} BestBi {image=images/credits_separator.png} Rinipanini {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Antenora") style "credits_1" at center
            text _("Month 8 - UI and Placeholder Sketch Art") style "credits_2" at left
            frame style "credits_month":
                text _("Malpertuis {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ryan Rae {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} pin3appl3dtogo {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} Alyssa {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Fini {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Yuki Cosplay {image=images/credits_separator.png} Rinipanini {image=images/credits_separator.png} ZizanieDreams {image=images/credits_separator.png} dustin e.w.") style "credits_1" at center
            text _("Month 9 - UI and Placeholder Sketch Art") style "credits_2" at left
            frame style "credits_month":
                text _("Malpertuis {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ryan Rae {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} Alyssa {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Fini {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} ZizanieDreams {image=images/credits_separator.png} dustin e.w. {image=images/credits_separator.png} Cyglyce") style "credits_1" at center
            text _("Month 10 - Alpha Testing and Bug Fixes") style "credits_2" at left
            frame style "credits_month":
                text _("Malpertuis {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ryan Rae {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} Alyssa {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Fini {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} ZizanieDreams {image=images/credits_separator.png} dustin e.w. {image=images/credits_separator.png} Cheyenne Applegate {image=images/credits_separator.png} Adek Fukumoto") style "credits_1" at center
            text _("Month 11 - Background Art") style "credits_2" at left
            frame style "credits_month":
                text _("Malpertuis {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ryan Rae {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} Alyssa {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Fini {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} ZizanieDreams {image=images/credits_separator.png} dustin e.w. {image=images/credits_separator.png} Cheyenne Applegate {image=images/credits_separator.png} Adek Fukumoto {image=images/credits_separator.png} Gin {image=images/credits_separator.png} Sir Captain Rainbow {image=images/credits_separator.png} SilkMilkSpiderDrankSomeCider {image=images/credits_separator.png} Alex Prince") style "credits_1" at center
            text _("Month 12 - Background Art") style "credits_2" at left
            frame style "credits_month":
                text _("Malpertuis {image=images/credits_separator.png} Clover {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} Alyssa {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Fini {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} dustin e.w. {image=images/credits_separator.png} Cheyenne Applegate {image=images/credits_separator.png} Adek Fukumoto {image=images/credits_separator.png} Gin {image=images/credits_separator.png} Sir Captain Rainbow {image=images/credits_separator.png} SilkMilkSpiderDrankSomeCider {image=images/credits_separator.png} Tunic {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Gizellie {image=images/credits_separator.png} S.Q. {image=images/credits_separator.png} Raenoke Fukumoto {image=images/credits_separator.png} Intranocent") style "credits_1" at center
            text _("Month 13 - Sprite Art") style "credits_2" at left
            frame style "credits_month":
                text _("Adek Fukumoto {image=images/credits_separator.png} Alyssa {image=images/credits_separator.png} Aipe {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Clover {image=images/credits_separator.png} card captor nero {image=images/credits_separator.png} Chaoticgouda {image=images/credits_separator.png} Cheyenne Applegate {image=images/credits_separator.png} Clever Sailor {image=images/credits_separator.png} Selly {image=images/credits_separator.png} dustin e.w. {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Gin {image=images/credits_separator.png} Gizellie {image=images/credits_separator.png} Fini {image=images/credits_separator.png} Intranocent {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} HSZRLeo {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Redd the Mighty {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Sarah Rose {image=images/credits_separator.png} SilkMilkSpiderDrankSomeCider {image=images/credits_separator.png} Sir Captain Rainbow {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} Tunic {image=images/credits_separator.png} Vin Céleste") style "credits_1" at center
            text _("Month 14 - Sprite Art") style "credits_2" at left
            frame style "credits_month":
                text _("Adek Fukumoto {image=images/credits_separator.png} Aipe {image=images/credits_separator.png} Ren the blood fox {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} BaphometBabe  {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Card Captor Nero {image=images/credits_separator.png} Chaoticgouda {image=images/credits_separator.png} Selly {image=images/credits_separator.png} dustin e.w. {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Gin {image=images/credits_separator.png} Gizellie {image=images/credits_separator.png} Intranocent {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Jay K. {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} HSZRLeo {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} BestBi {image=images/credits_separator.png} Lyric {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Prince {image=images/credits_separator.png} Redd the Mighty {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} Sage {image=images/credits_separator.png} Sarah Rose {image=images/credits_separator.png} SilkMilkSpiderDrankSomeCider {image=images/credits_separator.png} Sir Captain Rainbow {image=images/credits_separator.png} Lea {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} Tunic {image=images/credits_separator.png} Vin Céleste") style "credits_1" at center
            text _("Month 15 - Sprite Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Adek Fukumoto {image=images/credits_separator.png} Aipe {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Card Captor Nero {image=images/credits_separator.png} Chaoticgouda {image=images/credits_separator.png} Clever Sailor {image=images/credits_separator.png} Clever Sailor {image=images/credits_separator.png} Clover {image=images/credits_separator.png} dustin e.w. {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Filthy Fruit {image=images/credits_separator.png} Gin {image=images/credits_separator.png} Gizellie {image=images/credits_separator.png} Intranocent {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Jay K. {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} HSZRLeo {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Kevin Munro {image=images/credits_separator.png} Lea {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Michaela {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Felix {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Prince {image=images/credits_separator.png} Redd the Mighty {image=images/credits_separator.png} Ren the blood fox {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Sage {image=images/credits_separator.png} Sarah Rose {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Sir Captain Rainbow {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Vin Céleste") style "credits_1" at center
            text _("Month 16 - Sprite Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Adek Fukumoto {image=images/credits_separator.png} Aipe {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Card Captor Nero {image=images/credits_separator.png} Chaoticgouda {image=images/credits_separator.png} Clover {image=images/credits_separator.png} dustin e.w. {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Filthy Fruit {image=images/credits_separator.png} Gin {image=images/credits_separator.png} Gizellie {image=images/credits_separator.png} Intranocent {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Jay K. {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Lea {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Michaela {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} NiwiNoodle {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Redd the Mighty {image=images/credits_separator.png} Ren the blood fox {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Sage {image=images/credits_separator.png} Sarah Rose {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Sir Captain Rainbow {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Vin Céleste {image=images/credits_separator.png} WHY WE GOIN SO FUCKING FAST") style "credits_1" at center
            text _("Month 17 - Art Fixes and UI/Programming Touchups") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Aipe {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} Ren the blood fox {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Card Captor Nero {image=images/credits_separator.png} Chaoticgouda {image=images/credits_separator.png} Selly {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Filthy Fruit {image=images/credits_separator.png} Gin {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Redd the Mighty {image=images/credits_separator.png} Sage {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} Vin Céleste {image=images/credits_separator.png} WHY WE GOIN SO FUCKING FAST") style "credits_1" at center
            text _("Month 18 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} Ren the blood fox {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Card Captor Nero {image=images/credits_separator.png} Selly {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Filthy Fruit {image=images/credits_separator.png} Gin {image=images/credits_separator.png} Gizellie {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Redd the Mighty {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Sage {image=images/credits_separator.png} Sarah Rose {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} WHY WE GOIN SO FUCKING FAST {image=images/credits_separator.png} Windy") style "credits_1" at center
            text _("Month 19 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Card Captor Nero {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Filthy Fruit {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Raenoke Fukumoto {image=images/credits_separator.png} Redd the Mighty {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Sage {image=images/credits_separator.png} Sarah Rose {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Mori {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} WHY WE GOIN SO FUCKING FAST {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} Zombiegutz") style "credits_1" at center
            text _("Month 20 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Card Captor Nero {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Dragon {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Filthy Fruit {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Kait Patrone {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} Onyx-Menhera {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Raenoke Fukumoto {image=images/credits_separator.png} Redd the Mighty {image=images/credits_separator.png} Ren the blood fox {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Sage {image=images/credits_separator.png} Sarah Rose {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} TheVampireRose {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} WHY WE GOIN SO FUCKING FAST {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle") style "credits_1" at center
            text _("Month 21 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} BestBi {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Dorian Richter {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Filthy Fruit {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} Gizellie {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Kait Patrone {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} ola'papi {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Redd the Mighty {image=images/credits_separator.png} Ren the blood fox {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Sage {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} WHY WE GOIN SO FUCKING FAST {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle") style "credits_1" at center
            text _("Month 22 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Dorian Richter {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} FaustusFalk {image=images/credits_separator.png} Filthy Fruit {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} Gizellie {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} ola'papi {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Redd the Mighty {image=images/credits_separator.png} Ren the blood fox {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Sage {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Supurreme {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} WHY WE GOIN SO FUCKING FAST {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle") style "credits_1" at center
            text _("Month 23 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} AwkwardArin {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} Bean {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Dorian Richter {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} FaustusFalk {image=images/credits_separator.png} Filthy Fruit {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Georgina Jaime {image=images/credits_separator.png} Gin {image=images/credits_separator.png} Gizellie {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} ola'papi {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Peasant {image=images/credits_separator.png} Ren the blood fox {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Supurreme {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} Temprince Addams {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} WHY WE GOIN SO FUCKING FAST {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} Zae n Weez") style "credits_1" at center
            text _("Month 24 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Allen {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Ashley J {image=images/credits_separator.png} Aswhy {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} Bean {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} FaustusFalk {image=images/credits_separator.png} Filthy Fruit {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} Gizellie {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} Nuka Big Tits and Fizzy Fuck {image=images/credits_separator.png} ola'papi {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Peasant {image=images/credits_separator.png} Ren the blood fox {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Supurreme {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} Temprince Addams {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Vin Céleste {image=images/credits_separator.png} WHY WE GOIN SO FUCKING FAST {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} Zae n Weez") style "credits_1" at center
            text _("Month 25 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Allen {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Aswhy {image=images/credits_separator.png} AwkwardArin {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} Bean {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} blueboibitch {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} FaustusFalk {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} slug {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} Nuka Big Tits and Fizzy Fuck {image=images/credits_separator.png} ola'papi {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Peasant {image=images/credits_separator.png} RabidRot {image=images/credits_separator.png} Ren the blood fox {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Supurreme {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} Temprince Addams {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Vin Céleste  {image=images/credits_separator.png} WHY WE GOIN SO FUCKING FAST {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} yxnalesca") style "credits_1" at center
            text _("Month 26 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Allen {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Aswhy {image=images/credits_separator.png} AwkwardArin {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} blueboibitch {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Elliot Valentine {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} FaustusFalk {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} slug {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} majorspacebirb {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} Nuka Big Tits and Fizzy Fuck {image=images/credits_separator.png} ola'papi {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Peasant {image=images/credits_separator.png} RabidRot {image=images/credits_separator.png} Ren the blood fox {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} Temprince Addams {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Vin Céleste {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} yxnalesca") style "credits_1" at center
            text _("Month 27 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Allen {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Aswhy {image=images/credits_separator.png} AwkwardArin {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} blueboibitch {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Elliot Valentine {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} LadyMorgue {image=images/credits_separator.png} slug {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} majorspacebirb {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Peasant {image=images/credits_separator.png} RabidRot {image=images/credits_separator.png} Rainey {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} Temprince Addams {image=images/credits_separator.png} TrashFaun {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Vin Céleste  {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} yxnalesca") style "credits_1" at center
            text _("Month 28 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Allen {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Antenora {image=images/credits_separator.png} Aswhy {image=images/credits_separator.png} AwkwardArin {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} BestBi {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} blueboibitch {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Elliot Valentine {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} FaustusFalk {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} LadyMorgue {image=images/credits_separator.png} slug {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} majorspacebirb {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Peasant {image=images/credits_separator.png} RabidRot {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} SylvieLucrece {image=images/credits_separator.png} Temprince Addams {image=images/credits_separator.png} TrashFaun {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} yxnalesca") style "credits_1" at center
            text _("Month 29 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Allen {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Aswhy {image=images/credits_separator.png} AwkwardArin {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} blueboibitch {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Elliot Valentine {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} FaustusFalk {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} happy cow {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} slug {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Peasant {image=images/credits_separator.png} RabidRot {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} SylvieLucrece {image=images/credits_separator.png} TaiTai {image=images/credits_separator.png} Temprince Addams {image=images/credits_separator.png} Beezlebabe 669 {image=images/credits_separator.png} TrashFaun {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} yxnalesca {image=images/credits_separator.png} Zoe") style "credits_1" at center
            text _("Month 30 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Allen {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Aswhy {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} Beezlebabe 669 {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} blueboibitch {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Emily Houser {image=images/credits_separator.png} FaustusFalk {image=images/credits_separator.png} Finnigan {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} happy cow {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} slug {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Peasant {image=images/credits_separator.png} RabidRot {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} SylvieLucrece {image=images/credits_separator.png} TaiTai {image=images/credits_separator.png} TrashFaun {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} yxnalesca {image=images/credits_separator.png} Zoe") style "credits_1" at center
            text _("Month 31 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Allen {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Aswhy {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} Beezlebabe 669 {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} blueboibitch {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Devilsflair {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Emily Houser {image=images/credits_separator.png} FaustusFalk {image=images/credits_separator.png} Finnigan {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} happy cow {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} slug {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mori {image=images/credits_separator.png} MrFishess {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Peasant {image=images/credits_separator.png} RabidRot {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Selly {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} TaiTai {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} yxnalesca {image=images/credits_separator.png} Zoe") style "credits_1" at center
            text _("Month 32 - CG Art") style "credits_2" at left
            frame style "credits_month":
                text _("A S {image=images/credits_separator.png} Alexa & los testigos de Gatobob {image=images/credits_separator.png} Allen {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Aswhy {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} Bandaid Club {image=images/credits_separator.png} Beezlebabe 669 {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} blueboibitch {image=images/credits_separator.png} cadaverkitten {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Devilsflair {image=images/credits_separator.png} doktor corvid {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Falk {image=images/credits_separator.png} Finnigan {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} happy cow {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} sweets-and-horror {image=images/credits_separator.png} Lena Ross & los Testigos de Gatobob {image=images/credits_separator.png} slug {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mori {image=images/credits_separator.png} MrFishess {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Peasant {image=images/credits_separator.png} Phenix Rose {image=images/credits_separator.png} RabidRot {image=images/credits_separator.png} Rare Wind {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} TaiTai {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} yxnalesca") style "credits_1" at center
            text _("Month 33 - CG Art and Audio Design") style "credits_2" at left
            frame style "credits_month":
                text _("1800B10H4Z4RD {image=images/credits_separator.png} A S {image=images/credits_separator.png} Allen {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Aswhy {image=images/credits_separator.png} AwkwardArin {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} Bandaid Club {image=images/credits_separator.png} Beezlebabe 669 {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} blueboibitch {image=images/credits_separator.png} Clover {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Devilsflair {image=images/credits_separator.png} doktor corvid {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} Falk {image=images/credits_separator.png} Finnigan {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} happy cow {image=images/credits_separator.png} JasperDap {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} slug {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mori {image=images/credits_separator.png} M07H_M4N {image=images/credits_separator.png} MrFishess {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} mutedlight {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} NMRspindoc {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Peasant {image=images/credits_separator.png} Phenix Rose {image=images/credits_separator.png} RabidRot {image=images/credits_separator.png} Rare Wind {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} savannah allison {image=images/credits_separator.png} sqort {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Westinghouse {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} yxnalesca") style "credits_1" at center
            text _("Month 34 - Beta Testing and Bonus Content") style "credits_2" at left
            frame style "credits_month":
                text _("1800B10H4Z4RD {image=images/credits_separator.png} A S {image=images/credits_separator.png} Allen {image=images/credits_separator.png} alyxtried {image=images/credits_separator.png} Angel Boy {image=images/credits_separator.png} Aswhy {image=images/credits_separator.png} AwkwardArin {image=images/credits_separator.png} AzzyDoesntExist {image=images/credits_separator.png} Bandaid Club {image=images/credits_separator.png} Beezlebabe 669 {image=images/credits_separator.png} Bellamy {image=images/credits_separator.png} BloodstainsandHeartache {image=images/credits_separator.png} blueboibitch {image=images/credits_separator.png} Car {image=images/credits_separator.png} Clover {image=images/credits_separator.png} cypress {image=images/credits_separator.png} Daddy Turnip {image=images/credits_separator.png} Devilsflair {image=images/credits_separator.png} doktor corvid {image=images/credits_separator.png} earthwornn {image=images/credits_separator.png} Elliot Valentine {image=images/credits_separator.png} Em {image=images/credits_separator.png} Emily Astrom {image=images/credits_separator.png} entsutcliff {image=images/credits_separator.png} Falk {image=images/credits_separator.png} Finnigan {image=images/credits_separator.png} GeminiNeedle {image=images/credits_separator.png} Gin {image=images/credits_separator.png} happy cow {image=images/credits_separator.png} Josie Smith {image=images/credits_separator.png} Taylor Kaine {image=images/credits_separator.png} Kontrabanned {image=images/credits_separator.png} Kris X {image=images/credits_separator.png} Lauren Red {image=images/credits_separator.png} Lypa {image=images/credits_separator.png} Malpertuis {image=images/credits_separator.png} Meghan Strickler {image=images/credits_separator.png} MilkLuca {image=images/credits_separator.png} Mininjake {image=images/credits_separator.png} Mori {image=images/credits_separator.png} Moth {image=images/credits_separator.png} MrFishess {image=images/credits_separator.png} Mushroom Cabin {image=images/credits_separator.png} mutedlight {image=images/credits_separator.png} NebuCosmo {image=images/credits_separator.png} NewWoldPhoenix {image=images/credits_separator.png} NMRspindoc {image=images/credits_separator.png} Nuka Big Tits and Fizzy Fuck {image=images/credits_separator.png} PanicDracoFelidae {image=images/credits_separator.png} Peasant {image=images/credits_separator.png} RabidRot {image=images/credits_separator.png} Rare Wind {image=images/credits_separator.png} Rhianna {image=images/credits_separator.png} Ricochet Kreibich {image=images/credits_separator.png} slug {image=images/credits_separator.png} sqort {image=images/credits_separator.png} Swaggeroonie {image=images/credits_separator.png} Tully {image=images/credits_separator.png} UnamusedDetective {image=images/credits_separator.png} Vivianne Starlight {image=images/credits_separator.png} Westinghouse {image=images/credits_separator.png} WhatIsSleep {image=images/credits_separator.png} Windy {image=images/credits_separator.png} xxoobattle {image=images/credits_separator.png} yxnalesca {image=images/credits_separator.png} Zoe {image=images/credits_separator.png} Zombiegutz") style "credits_1" at center
            null height 20
            text _("Everything Else (Coding, Writing, Art, etc)") style "credits_title" at center
            text _("Gatobob") style "credits_1" at center

    on "replace" action Play("music", "music/Graveyardguy_Gore.mp3", selected=True)
    on "replaced" action Play("music", "music/main_menu.mp3")

style credits_month:
    background Frame("images/bg_darkbox_whiteborder.png", 10, 10)
    top_padding 10
    bottom_padding 10
    left_padding 30
    right_padding 30
    bottom_margin 10
    xfill True
style credits_title:
    size 30
    color "c00"
    font "images/libel-suit.regular.ttf"
    text_align 0.5
    outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]
style credits_1:
    text_align 0.5
    size 20
    layout "subtitle"
style credits_2:
    text_align 0
    size 20




screen warnings():
    tag menu





    use game_menu(_("Warnings"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "Content and Trigger Warnings"

            text _("This chart contains detailed content/trigger warnings for the game, based on the three general game paths.") style "small_text"
            text _("If you find yourself feeling overwhelmed at any time, please take care to close the game.") style "small_text"
            text _("This game is built to entertain people, not to harm them.") style "small_text"
            null height 20

            label "{color=#9fff8f}Mason{/color}" at center
            null height 20

            hbox:
                xfill True

                grid 2 12:
                    spacing 5

                    frame:
                        background "#430000"
                        xsize 700
                        text _("Warning") at center
                    frame:
                        background "#430000"
                        xsize 150
                        text _("Severity") at center

                    text _("Animal Harm - Fish, Deer, Bear")
                    text _("High")

                    text _("Animal Death - Fish, Deer")
                    text _("High")

                    text _("Images of Animal Remains")
                    text _("Medium")

                    text _("Noose Mention/Imagery")
                    text _("High")

                    text _("Suicide Themes")
                    text _("Medium")

                    text _("Drowning")
                    text _("Medium")

                    text _("Violence - Knife, Burns, Crossbow, Axe, Gore") xsize 700
                    text _("High")

                    text _("Violence / Death of Non-Player Character")
                    text _("Medium")

                    text _("Gun Mention and Sound")
                    text _("Medium")

                    text _("Audio and Visual Hallucinations")
                    text _("Medium")

                    text _("Sexual Assault and Rape*") style "red_text"
                    text _("High") style "red_text"
            text _("*Only with Sexual Content enabled at the beginning of the game") style "red_small_text"
            null height 50

            label "{color=#7cb3d2}Celia{/color}" at center
            null height 20

            hbox:
                xfill True
                grid 2 13:
                    spacing 5

                    frame:
                        background "#430000"
                        xsize 700
                        text _("Warning") at center
                    frame:
                        background "#430000"
                        xsize 150
                        text _("Severity") at center

                    text _("Force Feeding")
                    text _("High")

                    text _("Gun Imagery and Sound")
                    text _("High")

                    text _("Forced Nudity")
                    text _("Mild")

                    text _("Noose / Hanging Mention")
                    text _("Medium")

                    text _("Alcohol Consumption")
                    text _("Medium")

                    text _("Violence - Knife, Gun, Whip, Garotte, Taser") xsize 700
                    text _("High")

                    text _("Violence / Death of Non-Player Character")
                    text _("High")

                    text _("Audio and Visual Hallucinations")
                    text _("Mild")

                    text _("Extreme Torture / Mindbreak Themes")
                    text _("High")

                    text _("Oral Mutilation")
                    text _("High")

                    text _("Amputation")
                    text _("Medium")

                    text _("Sexual Assault and Rape*") style "red_text"
                    text _("Medium") style "red_text"
            text _("*Only with Sexual Content enabled at the beginning of the game") style "red_small_text"
            null height 50

            label "{color=#ff3451}Derek{/color}" at center
            null height 20
            hbox:
                xfill True
                grid 2 12:
                    spacing 5

                    frame:
                        background "#430000"
                        xsize 700
                        text _("Warning") at center
                    frame:
                        background "#430000"
                        xsize 150
                        text _("Severity") at center

                    text _("Religious Cult Themes")
                    text _("High")

                    text _("Poison / Paralysis")
                    text _("High")

                    text _("Violence - Knife, Machete, Brass Knuckles, Explosives") xsize 700
                    text _("High")

                    text _("Violence / Death of Non-Player Character")
                    text _("Very High")

                    text _("Audio and Visual Hallucinations")
                    text _("Mild")

                    text _("Oral Mutilation")
                    text _("High")

                    text _("Eye Mutilation")
                    text _("High")

                    text _("Genital Mutilation*") style "red_text"
                    text _("Medium") style "red_text"

                    text _("Necrophilia Mention*") style "red_text"
                    text _("Mild") style "red_text"

                    text _("Sexual Assault and Rape*") style "red_text"
                    text _("High") style "red_text"

                    text _("Sexual Assault and Rape of Non-Player Character*") style "red_text"
                    text _("High") style "red_text"
            text _("*Only with Sexual Content enabled at the beginning of the game") style "red_small_text"
            null height 50

            label "{color=#000}Fox{/color}" style "fox_label" at center
            null height 20
            hbox:
                xfill True
                grid 2 20:
                    spacing 5

                    frame:
                        background "#430000"
                        xsize 700
                        text _("Warning") at center
                    frame:
                        background "#430000"
                        xsize 150
                        text _("Severity") at center

                    text _("Non-Consensual Filming and Live Streaming")
                    text _("High")

                    text _("Forced and Unconscious Undressing")
                    text _("High")

                    text _("Violence - Beating, Knives, Burning, Various Weapons") xsize 700
                    text _("High")

                    text _("Forced Feminization")
                    text _("Mild")

                    text _("Joint Dislocation")
                    text _("High")

                    text _("Foot Mutilation")
                    text _("High")

                    text _("Eye Mutilation")
                    text _("Extremely High")

                    text _("Asphyxiation / Hanging")
                    text _("High")

                    text _("Gun Imagery and Sound")
                    text _("High")

                    text _("Imprisonment")
                    text _("Mild")

                    text _("Torture / Drugging / Mindbreak Themes")
                    text _("Extremely High")

                    text _("Unreality / Mind Control Themes")
                    text _("High")

                    text _("Described Hallucinations")
                    text _("Medium")

                    text _("Non-Consensual Autocannibalism")
                    text _("Medium")

                    text _("Gutting / Gore Imagery")
                    text _("High")

                    text _("Self Harm / Cutting Self")
                    text _("High")

                    text _("Implied Necrophilia*") style "red_text"
                    text _("Medium") style "red_text"

                    text _("Forced Sexual Performance for an Audience*") style "red_text"
                    text _("High") style "red_text"

                    text _("Sexual Assault and Rape*") style "red_text"
                    text _("Extremely High") style "red_text"


            text _("*Only with Sexual Content enabled at the beginning of the game") style "red_small_text"

style fox_label_text:
    outlines [ (absolute(2), "#ffffff", absolute(0), absolute(0)) ]










screen save():
    tag menu


    use file_slots(_("Save to which file?"))
    text "Save" style "bigboytext"
    if persistent.redcounter == True:
        add "demonfire" xpos 0 ypos 300 zoom 2.0
        add "chibi_demon" xpos 90 ypos 405

screen load():
    tag menu


    use file_slots(_("Load which save?"))
    text "Load" style "bigboytext"
    if persistent.greencounter == True:
        add "bluefire" xpos 135 ypos 365 zoom 0.3 alpha 0.3
        add "bluefire" xpos -145 ypos 465 zoom 0.4 alpha 0.3
        add "bluefire" xpos 0 ypos 565 zoom 0.5 alpha 0.3
        add "chibi_lich" xpos 135 ypos 365 zoom 0.9


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"




                        textbutton _("delete") action FileDelete(slot):
                            style "slot_delete_button"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 16):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style bigboytext:
    xpos 705
    ypos 50
    color "#FFF"
    size 70

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    color "#FFF"


style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

style slot_delete_button:
    idle_child "images/button_delete_idle.png"
    hover_child "images/button_delete_hover.png"
    insensitive_child "images/empty.png"
    xalign 1.0
    yoffset -190
    xoffset 7


style slot_delete_button_text:
    size 12








screen preferences():
    tag menu


    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")


















            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True











                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_music:

                        label _("Ambient Noise Volume")

                        hbox:
                            bar value Preference("ambient volume")

                    if config.has_sound:

                        label _("Sound Effects Volume")

                        hbox:
                            bar value Preference("sound volume")

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450








screen collections():
    tag menu





    use game_menu(_("Collections"), scroll="viewport"):

        style_prefix "about"
        $ game_endings_total = 50
        $ game_art_total = 115
        $ game_bgs_total = 21
        $ game_completion_total = game_endings_total + game_art_total + game_bgs_total
        $ game_completion_50 = int(math.ceil(game_completion_total*0.5))
        $ game_completion_75 = int(math.ceil(game_completion_total*.75))
        $ game_endings = (len(persistent.endings_derek)) + (len(persistent.endings_mason)) + (len(persistent.endings_celia))
        $ game_art = (len(persistent.cgs_derek)) + (len(persistent.cgs_mason)) + (len(persistent.cgs_celia))
        $ game_bgs = (len(persistent.bgs_seen))
        $ game_completion = game_art + game_endings + game_bgs
        hbox:
            vbox:
                if not renpy.variant("small"):
                    null height 20
                xsize 650
                textbutton _(" Death Collection") action ShowMenu("collections_death") style "lines_button" at center
                text _("This list contains every available ending you've collected- and those you haven't") style "collections_text" at center
                null height 20
                textbutton _(" Art Collection") action ShowMenu("collections_art_backgrounds") style "lines_button" at center
                text _("You can view any full screen art you've already seen here at your leisure") style "collections_text" at center
                null height 20
                textbutton _(" Music Collection") action ShowMenu("musicroom") style "lines_button" at center
                text _("You can listen to any music you've already heard") style "collections_text" at center
                null height 20
                if game_completion >= game_completion_50:
                    textbutton _(" Character Bios") action ShowMenu("character_bios") style "lines_button" at center
                    text _("This contains a list of characters and some trivia and tidbits about them") style "collections_text" at center
                else:
                    textbutton _(" Character Bios") style "lines_button" at center
                    text _("[game_completion]/[game_completion_50] unlocked items") style "collections_text" at center
                null height 20
                if game_completion >= game_completion_75:
                    textbutton _(" Concept Art") action ShowMenu("concept_art") style "lines_button" at center
                    text _("This contains art made before and during game production, as well as some cut concepts") style "collections_text" at center
                else:
                    textbutton _(" Concept Art") style "lines_button" at center
                    text _("[game_completion]/[game_completion_75] unlocked items") style "collections_text" at center
                if not renpy.variant("small"):
                    null height 120
                else:
                    null height 40
                textbutton _(" Wipe All Game Data") action Confirm("Are you sure? This will destroy all progress and save files.", yes=Confirm("Are you REALLY sure? This will {color=#cc0000}delete everything{/color} and make your game like brand new.", yes=Function(destroy_progress))) style "lines_button_red" at center

            vbox:
                hbox:
                    vbox:
                        if game_completion >= game_completion_total:
                            text _("Memelord Mode -") style "collections_text_3" at right
                        else:
                            text _("Memelord Mode -") style "collections_text" at right
                        null height 100
                        if game_completion >= game_completion_75:
                            text _("Concept Art -") style "collections_text_2" at right
                        else:
                            text _("Concept Art -") style "collections_text" at right
                        null height 100
                        if game_completion >= game_completion_50:
                            text _("Character Bios -") style "collections_text_2" at right
                        else:
                            text _("Character Bios -") style "collections_text" at right
                    frame:
                        vbar value game_completion range game_completion_total xalign 0.5 yalign 0.366 xmaximum 43 ymaximum 500 left_bar Frame("#000", 10, 0) right_bar Frame("images/bar_completion_bg.jpg", 10, 0) thumb "images/bar_completion_indicator.png" thumb_offset 172
    vbox:
        add 'embarassing_coverup' xpos 1077 ypos 629
    if persistent.bluecounter == True:
        add "chibi_announcer" xpos 960 ypos 400

screen collection_art_navigation():
    frame:
        top_margin 40
        left_margin 560
        has hbox
        textbutton " Backgrounds" action ShowMenu("collections_art_backgrounds") style "lines_button"
        textbutton " Mason" action ShowMenu("collections_art_mason") style "lines_button"
        textbutton " Celia" action ShowMenu("collections_art_celia") style "lines_button"
        textbutton " Derek" action ShowMenu("collections_art_derek") style "lines_button"
        if persistent.bluecounter:
            textbutton " Fox" action ShowMenu("collections_art_fox") style "lines_button"
        else:
            textbutton " ???" style "lines_button"
        textbutton " Sexual Content" action ShowMenu("collections_art_sex") style "lines_button"









screen collections_death():
    $ derek_endings_complete = len(persistent.endings_derek)
    $ mason_endings_complete = len(persistent.endings_mason)
    $ celia_endings_complete = len(persistent.endings_celia)
    default deathtab = "Mason"
    tag menu




    use game_menu(_("Collections {size=50}{font=images/expressway-free.regular.ttf}-{/font}{/size} Deaths"), scroll="viewport"):

        style_prefix "about"

        vbox:
            $ all_mason_endings = [("You visited the cabin", 0), ("Your hunt is over", 0), ("Your flame is out", 0), ("You lost your head", 0), ("Your smoke gave you away", 0), ("The cold took you", 0), ("You were caught in his trap", 0), ("You were caught and cleaned", 0), ("You smelled delicious", 0), ("You bled out", 0), ("The water is still", 0), ("You denied him the pleasure", 0), ("Now you are the hunter", 1), ("You made a friend", 1), ("You changed", 2)]
            $ all_celia_endings = [("You were shot down", 0), ("You ate your mistake", 0), ("You fought and lost", 0), ("You were caught in the elevator", 0), ("You were stripped", 0), ("You were strung up", 0), ("You got a taste of your own medicine", 0), ("You became her broken toy", 1), ("You left her behind", 1), ("You killed for your freedom", 1),("You were cleaned up", 0), ("You ran out of time", 0), ("You were released", 1), ("You ran away together", 1)]
            $ all_derek_endings = [("You volunteered for first blood", 0), ("You refused to cry", 0), ("He didn't let you run", 0), ("You played with fireworks", 0), ("You wandered into the camp", 0), ("You gave your life in exchange", 0), ("You were caught by Jack", 0), ("You tried to be a hero", 0), ("You paved the way for sacrifice", 0), ("The heat got to you", 0), ("You were sacrificed", 0), ("You drank the water", 0), ("You wandered the desert", 0), ("You went down in the escape", 0), ("Your fight is over", 0), ("You were betrayed", 0), ("You bled out", 0), ("You succumbed to thirst", 0), ("You escaped with friends", 1), ("He took you home", 1), ("The machete was laid to rest", 1)]
            hbox:
                xalign 0.5
                textbutton "Mason" action SetScreenVariable("deathtab", "Mason") style "masondeathtabtitle"
                textbutton "Celia" action SetScreenVariable("deathtab", "Celia") style "celiadeathtabtitle"
                textbutton "Derek" action SetScreenVariable("deathtab", "Derek") style "derekdeathtabtitle"
            frame:
                style "deathholder"
                has hbox
                showif deathtab == "Mason":
                    vpgrid:
                        cols 2
                        spacing 19
                        allow_underfull True
                        transclude
                        for ending in all_mason_endings:
                            $ ending_name = ending[0]
                            $ ending_type = ending[1]
                            if ending_type == 0:
                                if ending_name in persistent.endings_mason:
                                    frame style "collections_death":
                                        text ("{font=images/circlethings.ttf}A{/font} " + ending_name) style "collections_death_text"
                                else:
                                    frame style "collections_death_null":
                                        text ("{font=images/circlethings.ttf}A{/font} " + ending_name) style "collections_death_null_text"
                            if ending_type == 1:
                                if ending_name in persistent.endings_mason:
                                    frame style "collections_death":
                                        text ("{font=images/circlethings.ttf}B{/font} " + ending_name) style "collections_death_text"
                                else:
                                    frame style "collections_death_null":
                                        text ("{font=images/circlethings.ttf}B{/font} " + ending_name) style "collections_death_null_text"
                            if ending_type == 2:
                                if ending_name in persistent.endings_mason:
                                    frame style "collections_death":
                                        text ("{font=images/circlethings.ttf}a{/font} " + ending_name) style "collections_death_text"
                                else:
                                    frame style "collections_death_null":
                                        text ("{font=images/circlethings.ttf}a{/font} " + ending_name) style "collections_death_null_text"
                elif deathtab == "Celia":
                    vpgrid:
                        cols 2
                        spacing 19
                        allow_underfull True
                        transclude
                        for ending in all_celia_endings:
                            $ ending_name = ending[0]
                            $ ending_type = ending[1]
                            if ending_type == 0:
                                if ending_name in persistent.endings_celia:
                                    frame style "collections_death":
                                        text ("{font=images/circlethings.ttf}A{/font} " + ending_name) style "collections_death_text"
                                else:
                                    frame style "collections_death_null":
                                        text ("{font=images/circlethings.ttf}A{/font} " + ending_name) style "collections_death_null_text"
                            if ending_type == 1:
                                if ending_name in persistent.endings_celia:
                                    frame style "collections_death":
                                        text ("{font=images/circlethings.ttf}B{/font} " + ending_name) style "collections_death_text"
                                else:
                                    frame style "collections_death_null":
                                        text ("{font=images/circlethings.ttf}B{/font} " + ending_name) style "collections_death_null_text"
                elif deathtab == "Derek":
                    vpgrid:
                        cols 2
                        spacing 19
                        allow_underfull True
                        transclude
                        for ending in all_derek_endings:
                            $ ending_name = ending[0]
                            $ ending_type = ending[1]
                            if ending_type == 0:
                                if ending_name in persistent.endings_derek:
                                    frame style "collections_death":
                                        text ("{font=images/circlethings.ttf}A{/font} " + ending_name) style "collections_death_text"
                                else:
                                    frame style "collections_death_null":
                                        text ("{font=images/circlethings.ttf}A{/font} " + ending_name) style "collections_death_null_text"
                            if ending_type == 1:
                                if ending_name in persistent.endings_derek:
                                    frame style "collections_death":
                                        text ("{font=images/circlethings.ttf}B{/font} " + ending_name) style "collections_death_text"
                                else:
                                    frame style "collections_death_null":
                                        text ("{font=images/circlethings.ttf}B{/font} " + ending_name) style "collections_death_null_text"
                    if derek_endings_complete >= 21:
                        add "chibi_derek" xoffset -170 yoffset 300
    if deathtab == "Mason":
        add "gui/tab_line.jpg" xpos 370 ypos 179
        if mason_endings_complete >= 15:
            add "chibi_mason" xpos 1022 ypos 355
    if deathtab == "Celia":
        add "gui/tab_line.jpg" xpos 650 ypos 179
        if celia_endings_complete >= 14:
            add "chibi_celia" xpos 1020 ypos 355
    if deathtab == "Derek":
        add "gui/tab_line.jpg" xpos 930 ypos 179
style deathholder:
    background Frame("gui/frame2.png", Borders(8, 8, 8, 8), tile=gui.frame_tile)
    xfill True
    xpadding 20
    ypadding 20
    xmargin 30
style deathtabtitle:
    xsize 280
    background Frame("gui/tab_frame.png", Borders(8, 8, 8, 8), tile=gui.frame_tile)
    hover_background Frame("gui/tab_frame_hover.png", Borders(8, 8, 8, 8), tile=gui.frame_tile)
    xmargin 10
style deathtabtitle_text:
    xalign 0.5 yalign 0.5
    size 40
    font "images/still-time.regular.ttf"
style masondeathtabtitle is deathtabtitle
style celiadeathtabtitle is deathtabtitle
style derekdeathtabtitle is deathtabtitle
style masondeathtabtitle_text is deathtabtitle_text:
    color "#9fff8f"
    hover_color "#ffffff"
style celiadeathtabtitle_text is deathtabtitle_text:
    color "#7cb3d2"
    hover_color "#ffffff"
style derekdeathtabtitle_text is deathtabtitle_text:
    color "#cc0000"
    hover_color "#ffffff"
style collections_label_text:
    color "#fff"
    size 40
    font "images/still-time.regular.ttf"
style collections_text:
    color "#888"
    size 15
    italic True
style collections_text_2 is collections_text:
    color "#fff"
style collections_text_3 is collections_text:
    color "#cc0000"
style collections_death:
    xsize 400
    background "gui/death_collection_item_bg_active.png"
    top_padding 4
    bottom_padding 7
    xpadding 7
style collections_death_text:
    color "#fff"
    size 20
style collections_death_null is collections_death:
    background "gui/death_collection_item_bg.png"
    foreground "gui/death_collection_item_fg.png"
style collections_death_null_text is collections_death_text:
    color "#444"




init python:
    g = Gallery()



    g.transition = dissolve
    g.locked_button = "images/gallery_locked.png"

    g.button("bg_derek_camp")
    g.image("images/bg_derek_camp.jpg")
    g.condition("'bg_derek_camp' in persistent.bgs_seen")
    g.image("images/bg_derek_camp_morning.jpg")
    g.condition("'bg_derek_camp' in persistent.bgs_seen")
    g.image("images/bg_derek_camp_twilight.jpg")
    g.condition("'bg_derek_camp' in persistent.bgs_seen")
    g.image("images/bg_derek_camp_night.jpg")
    g.condition("'bg_derek_camp' in persistent.bgs_seen")

    g.button("bg_derek_hill")
    g.image("images/bg_derek_hill.jpg")
    g.condition("'bg_derek_hill' in persistent.bgs_seen")
    g.image("images/bg_derek_hill_morning.jpg")
    g.condition("'bg_derek_hill' in persistent.bgs_seen")
    g.image("images/bg_derek_hill_twilight.jpg")
    g.condition("'bg_derek_hill' in persistent.bgs_seen")
    g.image("images/bg_derek_hill_night.jpg")
    g.condition("'bg_derek_hill' in persistent.bgs_seen")

    g.button("bg_derek_fissure")
    g.image("images/bg_derek_fissure.jpg")
    g.condition("'bg_derek_fissure' in persistent.bgs_seen")
    g.image("images/bg_derek_fissure_morning.jpg")
    g.condition("'bg_derek_fissure' in persistent.bgs_seen")
    g.image("images/bg_derek_fissure_twilight.jpg")
    g.condition("'bg_derek_fissure' in persistent.bgs_seen")
    g.image("images/bg_derek_fissure_night.jpg")
    g.condition("'bg_derek_fissure' in persistent.bgs_seen")

    g.button("bg_derek_desert")
    g.image("images/bg_derek_desert.jpg")
    g.condition("'bg_derek_desert' in persistent.bgs_seen")
    g.image("images/bg_derek_desert_morning.jpg")
    g.condition("'bg_derek_desert' in persistent.bgs_seen")
    g.image("images/bg_derek_desert_twilight.jpg")
    g.condition("'bg_derek_desert' in persistent.bgs_seen")
    g.image("images/bg_derek_desert_night.jpg")
    g.condition("'bg_derek_desert' in persistent.bgs_seen")

    g.button("bg_derek_deepdesert")
    g.image("images/bg_derek_deepdesert.jpg")
    g.condition("'bg_derek_deepdesert' in persistent.bgs_seen")
    g.image("images/bg_derek_deepdesert_morning.jpg")
    g.condition("'bg_derek_deepdesert' in persistent.bgs_seen")
    g.image("images/bg_derek_deepdesert_twilight.jpg")
    g.condition("'bg_derek_deepdesert' in persistent.bgs_seen")
    g.image("images/bg_derek_deepdesert_night.jpg")
    g.condition("'bg_derek_deepdesert' in persistent.bgs_seen")

    g.button("bg_derek_cave")
    g.image("images/bg_derek_cave.jpg")
    g.condition("'bg_derek_cave' in persistent.bgs_seen")

    g.button("bg_derek_theritz")
    g.image("images/bg_derek_theritz.jpg")
    g.condition("'bg_derek_theritz' in persistent.bgs_seen")

    g.button("bg_mason_meadow")
    g.image("images/bg_mason_meadow.jpg")
    g.condition("'bg_mason_meadow' in persistent.bgs_seen")
    g.image("images/bg_mason_meadow_morning.jpg")
    g.condition("'bg_mason_meadow' in persistent.bgs_seen")
    g.image("images/bg_mason_meadow_twilight.jpg")
    g.condition("'bg_mason_meadow' in persistent.bgs_seen")
    g.image("images/bg_mason_meadow_night.jpg")
    g.condition("'bg_mason_meadow' in persistent.bgs_seen")

    g.button("bg_mason_thicket")
    g.image("images/bg_mason_thicket.jpg")
    g.condition("'bg_mason_thicket' in persistent.bgs_seen")
    g.image("images/bg_mason_thicket_morning.jpg")
    g.condition("'bg_mason_thicket' in persistent.bgs_seen")
    g.image("images/bg_mason_thicket_twilight.jpg")
    g.condition("'bg_mason_thicket' in persistent.bgs_seen")
    g.image("images/bg_mason_thicket_night.jpg")
    g.condition("'bg_mason_thicket' in persistent.bgs_seen")

    g.button("bg_mason_waterfall")
    g.image("images/bg_mason_waterfall.jpg")
    g.condition("'bg_mason_waterfall' in persistent.bgs_seen")
    g.image("images/bg_mason_waterfall_morning.jpg")
    g.condition("'bg_mason_waterfall' in persistent.bgs_seen")
    g.image("images/bg_mason_waterfall_twilight.jpg")
    g.condition("'bg_mason_waterfall' in persistent.bgs_seen")
    g.image("images/bg_mason_waterfall_night.jpg")
    g.condition("'bg_mason_waterfall' in persistent.bgs_seen")

    g.button("bg_mason_talltree")
    g.image("images/bg_mason_talltree.jpg")
    g.condition("'bg_mason_talltree' in persistent.bgs_seen")
    g.image("images/bg_mason_talltree_morning.jpg")
    g.condition("'bg_mason_talltree' in persistent.bgs_seen")
    g.image("images/bg_mason_talltree_twilight.jpg")
    g.condition("'bg_mason_talltree' in persistent.bgs_seen")
    g.image("images/bg_mason_talltree_night.jpg")
    g.condition("'bg_mason_talltree' in persistent.bgs_seen")

    g.button("bg_mason_cabin")
    g.image("images/bg_mason_cabin.jpg")
    g.condition("'bg_mason_cabin' in persistent.bgs_seen")
    g.image("images/bg_mason_cabin_morning.jpg")
    g.condition("'bg_mason_cabin' in persistent.bgs_seen")
    g.image("images/bg_mason_cabin_twilight.jpg")
    g.condition("'bg_mason_cabin' in persistent.bgs_seen")
    g.image("images/bg_mason_cabin_night.jpg")
    g.condition("'bg_mason_cabin' in persistent.bgs_seen")

    g.button("bg_mason_incabin")
    g.image("images/bg_mason_incabin.jpg")
    g.condition("'bg_mason_incabin' in persistent.bgs_seen")
    g.image("images/bg_mason_incabin_morning.jpg")
    g.condition("'bg_mason_incabin' in persistent.bgs_seen")
    g.image("images/bg_mason_incabin_twilight.jpg")
    g.condition("'bg_mason_incabin' in persistent.bgs_seen")
    g.image("images/bg_mason_incabin_night.jpg")
    g.condition("'bg_mason_incabin' in persistent.bgs_seen")

    g.button("bg_mason_swamp")
    g.image("images/bg_mason_swamp.jpg")
    g.condition("'bg_mason_swamp' in persistent.bgs_seen")
    g.image("images/bg_mason_swamp_morning.jpg")
    g.condition("'bg_mason_swamp' in persistent.bgs_seen")
    g.image("images/bg_mason_swamp_twilight.jpg")
    g.condition("'bg_mason_swamp' in persistent.bgs_seen")
    g.image("images/bg_mason_swamp_night.jpg")
    g.condition("'bg_mason_swamp' in persistent.bgs_seen")

    g.button("bg_celia_room")
    g.image("black","bg_celia_room_smaller")
    g.condition("'bg_celia_room' in persistent.bgs_seen")

    g.button("bg_celia_lounge")
    g.image("images/bg_celia_lounge.jpg")
    g.condition("'bg_celia_lounge' in persistent.bgs_seen")

    g.button("bg_celia_elevator")
    g.image("images/bg_celia_elevator.jpg")
    g.condition("'bg_celia_elevator' in persistent.bgs_seen")

    g.button("bg_celia_office")
    g.image("images/bg_celia_office.jpg")
    g.condition("'bg_celia_office' in persistent.bgs_seen")

    g.button("bg_celia_breakroom")
    g.image("images/bg_celia_breakroom.jpg")
    g.condition("'bg_celia_breakroom' in persistent.bgs_seen")

    g.button("bg_celia_stairs")
    g.image("images/bg_celia_stairs.jpg")
    g.condition("'bg_celia_stairs' in persistent.bgs_seen")

    g.button("bg_celia_basement")
    g.image("images/bg_celia_basement.jpg")
    g.condition("'bg_celia_basement' in persistent.bgs_seen")

    g.button("cg_foxbg_dark")
    g.image("images/cg_foxbg_dark.png")
    g.condition("'cg_foxbg_dark' in persistent.cgs_fox")
    g.image("images/cg_foxbg_dark_full.png")
    g.condition("'cg_foxbg_dark' in persistent.cgs_fox")

    g.button("cg_foxbg_light")
    g.image("images/cg_foxbg_light.png")
    g.condition("'cg_foxbg_light' in persistent.cgs_fox")
    g.image("images/cg_foxbg_light_full.png")
    g.condition("'cg_foxbg_light' in persistent.cgs_fox")




    g.button("cg_derek_angrystab")
    g.image("cg_derek_angrystab.jpg")
    g.condition("'cg_derek_angrystab' in persistent.cgs_derek")

    g.button("cg_derek_bat")
    g.image("cg_derek_bat.jpg")
    g.condition("'cg_derek_bat' in persistent.cgs_derek")

    g.button("cg_derek_cave")
    g.image("cg_derek_cave.jpg")
    g.condition("'cg_derek_cave' in persistent.cgs_derek")
    g.image("cg_derek_cave_d.jpg")
    g.condition("'cg_derek_cave' in persistent.cgs_derek")
    g.image("cg_derek_cave_k.jpg")
    g.condition("'cg_derek_cave' in persistent.cgs_derek")
    g.image("cg_derek_cave_kd_dknife.jpg")
    g.condition("'cg_derek_cave' in persistent.cgs_derek")
    g.image("cg_derek_cave_kd_kknife.jpg")
    g.condition("'cg_derek_cave' in persistent.cgs_derek")
    g.image("cg_derek_cave_kd_salt.jpg")
    g.condition("'cg_derek_cave' in persistent.cgs_derek")

    g.button("cg_derek_cave_sacrifice")
    g.image("cg_derek_cave_sacrifice.jpg")
    g.condition("'cg_derek_cave_sacrifice' in persistent.cgs_derek")
    g.image("cg_derek_cave_sacrifice2.jpg")
    g.condition("'cg_derek_cave_sacrifice' in persistent.cgs_derek")

    g.button("cg_derek_cave_guts")
    g.image("cg_derek_cave_guts.jpg")
    g.condition("'cg_derek_cave_guts' in persistent.cgs_derek")

    g.button("cg_derek_cham")
    g.image("cg_derek_cham.jpg")
    g.condition("'cg_derek_cham' in persistent.cgs_derek")

    g.button("cg_derek_crouchknife")
    g.image("cg_derek_crouchknife_angry.jpg")
    g.condition("'cg_derek_crouchknife' in persistent.cgs_derek")
    g.image("cg_derek_crouchknife.jpg")
    g.condition("'cg_derek_crouchknife' in persistent.cgs_derek")

    g.button("cg_derek_deadtom")
    g.image("cg_derek_deadtom.jpg")
    g.condition("'cg_derek_deadtom' in persistent.cgs_derek")

    g.button("cg_derek_demon")
    g.image("cg_derek_demon.jpg")
    g.condition("'cg_derek_demon' in persistent.cgs_derek")

    g.button("cg_derek_dragonstab")
    g.image("cg_derek_dragonstab.jpg")
    g.condition("'cg_derek_dragonstab' in persistent.cgs_derek")

    g.button("cg_derek_favour")
    g.image("cg_derek_favour1.jpg")
    g.condition("'cg_derek_favour' in persistent.cgs_derek")
    g.image("cg_derek_favour2.jpg")
    g.condition("'cg_derek_favour' in persistent.cgs_derek")

    g.button("cg_derek_fireworks_crouch")
    g.image("cg_derek_fireworks_crouch.jpg")
    g.condition("'cg_derek_fireworks_crouch' in persistent.cgs_derek")

    g.button("cg_derek_fireworks_drop")
    g.image("cg_derek_fireworks_drop.jpg")
    g.condition("'cg_derek_fireworks_drop' in persistent.cgs_derek")
    g.image("cg_derek_fireworks_empty.jpg")
    g.condition("'cg_derek_fireworks_drop' in persistent.cgs_derek")

    g.button("cg_derek_fireworks_gag1")
    g.image("cg_derek_fireworks_gag1.jpg")
    g.condition("'cg_derek_fireworks_gag1' in persistent.cgs_derek")

    g.button("cg_derek_fireworks_gerb")
    g.image("cg_derek_fireworks_gerb.jpg")
    g.condition("'cg_derek_fireworks_gerb' in persistent.cgs_derek")

    g.button("cg_derek_firstblood_1")
    g.image("cg_derek_firstblood_1.jpg")
    g.condition("'cg_derek_firstblood_1' in persistent.cgs_derek")

    g.button("cg_derek_firstblood_2")
    g.image("cg_derek_firstblood_2.jpg")
    g.condition("'cg_derek_firstblood_2' in persistent.cgs_derek")

    g.button("cg_derek_helptom")
    g.image("cg_derek_helptom.jpg")
    g.condition("'cg_derek_helptom' in persistent.cgs_derek")

    g.button("cg_derek_jack_choke")
    g.image("cg_derek_jack_choke1.jpg")
    g.condition("'cg_derek_jack_choke' in persistent.cgs_derek")
    g.image("cg_derek_jack_choke2.jpg")
    g.condition("'cg_derek_jack_choke' in persistent.cgs_derek")

    g.button("cg_derek_jack_knuckles")
    g.image("cg_derek_jack_knuckles.jpg")
    g.condition("'cg_derek_jack_knuckles' in persistent.cgs_derek")

    g.button("cg_derek_jackknife_close")
    g.image("cg_derek_jackknife_close.jpg")
    g.condition("'cg_derek_jackknife_close' in persistent.cgs_derek")

    g.button("cg_derek_jackknife_pin")
    g.image("cg_derek_jackknife_pin.jpg")
    g.condition("'cg_derek_jackknife_pin' in persistent.cgs_derek")

    g.button("cg_derek_jackknife")
    g.image("cg_derek_jackknife.jpg")
    g.condition("'cg_derek_jackknife' in persistent.cgs_derek")

    g.button("cg_derek_jackmask")
    g.image("cg_derek_jackmask.jpg")
    g.condition("'cg_derek_jackmask' in persistent.cgs_derek")

    g.button("cg_derek_kdgut1")
    g.image("cg_derek_kdgut1.jpg")
    g.condition("'cg_derek_kdgut1' in persistent.cgs_derek")

    g.button("cg_derek_kdgut2")
    g.image("cg_derek_kdgut2.jpg")
    g.condition("'cg_derek_kdgut2' in persistent.cgs_derek")

    g.button("cg_derek_kdloom")
    g.image("cg_derek_kdloom.jpg")
    g.condition("'cg_derek_kdloom' in persistent.cgs_derek")

    g.button("cg_derek_loveanddeath")
    g.image("cg_derek_loveanddeath.jpg")
    g.condition("'cg_derek_loveanddeath' in persistent.cgs_derek")

    g.button("cg_derek_loveanddeath2")
    g.image("cg_derek_loveanddeath2.jpg")
    g.condition("'cg_derek_loveanddeath2' in persistent.cgs_derek")

    g.button("cg_derek_machete_sister")
    g.image("cg_derek_machete_sister.jpg")
    g.condition("'cg_derek_machete_sister' in persistent.cgs_derek")

    g.button("cg_derek_machete")
    g.image("cg_derek_machete.jpg")
    g.condition("'cg_derek_machete' in persistent.cgs_derek")

    g.button("cg_derek_nightsky_machete1")
    g.image("cg_derek_nightsky_machete1.jpg")
    g.condition("'cg_derek_nightsky_machete1' in persistent.cgs_derek")

    g.button("cg_derek_nightsky_machete2")
    g.image("cg_derek_nightsky_machete2.jpg")
    g.condition("'cg_derek_nightsky_machete2' in persistent.cgs_derek")

    g.button("cg_derek_nightsky")
    g.image("cg_derek_nightsky.jpg")
    g.condition("'cg_derek_nightsky' in persistent.cgs_derek")

    g.button("cg_derek_quadbat")
    g.image("cg_derek_quadbat.jpg")
    g.condition("'cg_derek_quadbat' in persistent.cgs_derek")

    g.button("cg_derek_throat")
    g.image("cg_derek_throat.jpg")
    g.condition("'cg_derek_throat' in persistent.cgs_derek")

    g.button("cg_derek_sand")
    g.image("cg_derek_sand.jpg")
    g.condition("'cg_derek_sand' in persistent.cgs_derek")
    g.image("cg_derek_sand_night.jpg")
    g.condition("'cg_derek_sand' in persistent.cgs_derek")

    g.button("cg_derek_showdown_attempted")
    g.image("cg_derek_showdown_attempted.jpg")
    g.condition("'cg_derek_showdown_attempted' in persistent.cgs_derek")

    g.button("cg_derek_showdown_backstab")
    g.image("cg_derek_showdown_backstab.jpg")
    g.condition("'cg_derek_showdown_backstab' in persistent.cgs_derek")

    g.button("cg_derek_showdown_baddog")
    g.image("cg_derek_showdown_baddog.jpg")
    g.condition("'cg_derek_showdown_baddog' in persistent.cgs_derek")

    g.button("cg_derek_showdown_standover")
    g.image("cg_derek_showdown_standover.jpg")
    g.condition("'cg_derek_showdown_standover' in persistent.cgs_derek")

    g.button("cg_derek_showdown_close")
    g.image("cg_derek_showdown_close.jpg")
    g.condition("'cg_derek_showdown_close' in persistent.cgs_derek")

    g.button("cg_derek_showdown_closeup")
    g.image("cg_derek_showdown_closeup.jpg")
    g.condition("'cg_derek_showdown_closeup' in persistent.cgs_derek")

    g.button("cg_derek_showdown_far")
    g.image("cg_derek_showdown_far.jpg")
    g.condition("'cg_derek_showdown_far' in persistent.cgs_derek")

    g.button("cg_derek_showdown_jackstab1")
    g.image("cg_derek_showdown_jackstab1.jpg")
    g.condition("'cg_derek_showdown_jackstab1' in persistent.cgs_derek")

    g.button("cg_derek_showdown_jackstab2")
    g.image("cg_derek_showdown_jackstab2.jpg")
    g.condition("'cg_derek_showdown_jackstab2' in persistent.cgs_derek")

    g.button("cg_derek_showdown_jackstomp")
    g.image("cg_derek_showdown_jackstomp.jpg")
    g.condition("'cg_derek_showdown_jackstomp' in persistent.cgs_derek")

    g.button("cg_derek_showdown_jaqdown")
    g.image("cg_derek_showdown_jaqdown.jpg")
    g.condition("'cg_derek_showdown_jaqdown' in persistent.cgs_derek")

    g.button("cg_derek_showdown_machetejack")
    g.image("cg_derek_showdown_machetejack.jpg")
    g.condition("'cg_derek_showdown_machetejack' in persistent.cgs_derek")

    g.button("cg_derek_showdown_neck")
    g.image("cg_derek_showdown_neck.jpg")
    g.condition("'cg_derek_showdown_neck' in persistent.cgs_derek")
    g.image("cg_derek_showdown_bleedout.jpg")
    g.condition("'cg_derek_showdown_neck' in persistent.cgs_derek")

    g.button("cg_derek_stabbed")
    g.image("black","cg_derek_stabbed_smaller")
    g.condition("'cg_derek_stabbed' in persistent.cgs_derek")

    g.button("cg_derek_straddle")
    g.image("cg_derek_straddle1.jpg")
    g.condition("'cg_derek_straddle' in persistent.cgs_derek")
    g.image("cg_derek_straddle2.jpg")
    g.condition("'cg_derek_straddle' in persistent.cgs_derek")
    g.image("cg_derek_straddle3.jpg")
    g.condition("'cg_derek_straddle' in persistent.cgs_derek")

    g.button("cg_derek_theritz")
    g.image("cg_derek_theritz.jpg")
    g.condition("'cg_derek_theritz' in persistent.cgs_derek")

    g.button("cg_derek_victims")
    g.image("cg_derek_victims.jpg")
    g.condition("'cg_derek_victims' in persistent.cgs_derek")

    g.button("cg_derek_vsmachete1")
    g.image("cg_derek_vsmachete0.jpg")
    g.condition("'cg_derek_vsmachete' in persistent.cgs_derek")
    g.image("cg_derek_vsmachete1.jpg")
    g.condition("'cg_derek_vsmachete' in persistent.cgs_derek")
    g.image("cg_derek_vsmachete2.jpg")
    g.condition("'cg_derek_vsmachete' in persistent.cgs_derek")

    g.button("cg_derek_vsmachete_hush")
    g.image("cg_derek_vsmachete4.jpg")
    g.condition("'cg_derek_vsmachete_hush' in persistent.cgs_derek")
    g.image("cg_derek_vsmachete3.jpg")
    g.condition("'cg_derek_vsmachete_hush' in persistent.cgs_derek")

    g.button("cg_derek_vsmachete5")
    g.image("cg_derek_vsmachete5.jpg")
    g.condition("'cg_derek_vsmachete5' in persistent.cgs_derek")

    g.button("cg_derek_watermachete1")
    g.image("cg_derek_watermachete1.jpg")
    g.condition("'cg_derek_watermachete1' in persistent.cgs_derek")

    g.button("cg_derek_watermachete2")
    g.image("cg_derek_watermachete2.jpg")
    g.condition("'cg_derek_watermachete2' in persistent.cgs_derek")



    g.button("cg_celia_basement_cage")
    g.image("cg_celia_basement_cage.jpg")
    g.condition("'cg_celia_basement_cage' in persistent.cgs_celia")
    g.image("cg_celia_basement_cage_alone.jpg")
    g.condition("'cg_celia_basement_cage' in persistent.cgs_celia")

    g.button("cg_celia_ceiling_gun")
    g.image("cg_celia_ceiling_gun.jpg")
    g.condition("'cg_celia_ceiling_gun' in persistent.cgs_celia")
    g.image("cg_celia_ceiling.jpg")
    g.condition("'cg_celia_ceiling_gun' in persistent.cgs_celia")

    g.button("cg_celia_donuts")
    g.image("cg_celia_donuts.jpg")
    g.condition("'cg_celia_donuts' in persistent.cgs_celia")

    g.button("cg_celia_elevator_1")
    g.image("cg_celia_elevator_1.jpg")
    g.condition("'cg_celia_elevator_1' in persistent.cgs_celia")

    g.button("cg_celia_elevator_2")
    g.image("cg_celia_elevator_2.jpg")
    g.condition("'cg_celia_elevator_2' in persistent.cgs_celia")

    g.button("cg_celia_elevator_3")
    g.image("cg_celia_elevator_3.jpg")
    g.condition("'cg_celia_elevator_3' in persistent.cgs_celia")

    g.button("cg_celia_escape")
    g.image("cg_celia_escape_1.jpg")
    g.condition("'cg_celia_escape' in persistent.cgs_celia")
    g.image("cg_celia_escape_2.jpg")
    g.condition("'cg_celia_escape' in persistent.cgs_celia")
    g.image("cg_celia_escape_3.jpg")
    g.condition("'cg_celia_escape' in persistent.cgs_celia")

    g.button("cg_celia_fallen")
    g.image("cg_celia_fallen.jpg")
    g.condition("'cg_celia_fallen' in persistent.cgs_celia")

    g.button("cg_celia_glass")
    g.image("cg_celia_glass_1.jpg")
    g.condition("'cg_celia_glass' in persistent.cgs_celia")
    g.image("cg_celia_glass_2.jpg")
    g.condition("'cg_celia_glass' in persistent.cgs_celia")

    g.button("cg_celia_harold_choked")
    g.image("cg_celia_harold_choked_2.jpg")
    g.condition("'cg_celia_harold_choked' in persistent.cgs_celia")
    g.image("cg_celia_harold_choked.jpg")
    g.condition("'cg_celia_harold_choked' in persistent.cgs_celia")

    g.button("cg_celia_harold_kill_1")
    g.image("cg_celia_harold_kill_1.jpg")
    g.condition("'cg_celia_harold_kill_1' in persistent.cgs_celia")

    g.button("cg_celia_harold_kill_2")
    g.image("cg_celia_harold_kill_2.jpg")
    g.condition("'cg_celia_harold_kill_2' in persistent.cgs_celia")

    g.button("cg_celia_harold_shot")
    g.image("cg_celia_harold_shot.jpg")
    g.condition("'cg_celia_harold_shot' in persistent.cgs_celia")

    g.button("cg_celia_harold_tripped")
    g.image("cg_celia_harold_tripped.jpg")
    g.condition("'cg_celia_harold_tripped' in persistent.cgs_celia")

    g.button("cg_celia_leave")
    g.image("cg_celia_leave_1.jpg")
    g.condition("'cg_celia_leave' in persistent.cgs_celia")
    g.image("cg_celia_leave_2.jpg")
    g.condition("'cg_celia_leave' in persistent.cgs_celia")
    g.image("cg_celia_leave_3.jpg")
    g.condition("'cg_celia_leave' in persistent.cgs_celia")
    g.image("cg_celia_leave_4.jpg")
    g.condition("'cg_celia_leave' in persistent.cgs_celia")

    g.button("cg_celia_lounge")
    g.image("cg_celia_lounge_angry.jpg")
    g.condition("'cg_celia_lounge' in persistent.cgs_celia")
    g.image("cg_celia_lounge_happy.jpg")
    g.condition("'cg_celia_lounge' in persistent.cgs_celia")
    g.image("cg_celia_lounge_phone.jpg")
    g.condition("'cg_celia_lounge' in persistent.cgs_celia")
    g.image("cg_celia_lounge.jpg")
    g.condition("'cg_celia_lounge' in persistent.cgs_celia")

    g.button("cg_celia_poisoned")
    g.image("cg_celia_poisoned.jpg")
    g.condition("'cg_celia_poisoned' in persistent.cgs_celia")

    g.button("cg_celia_poisoned2")
    g.image("cg_celia_poisoned2.jpg")
    g.condition("'cg_celia_poisoned2' in persistent.cgs_celia")

    g.button("cg_celia_roomcorner")
    g.image("cg_celia_roomcorner.jpg")
    g.condition("'cg_celia_roomcorner' in persistent.cgs_celia")

    g.button("cg_celia_slitharold")
    g.image("cg_celia_slitharold_1.jpg")
    g.condition("'cg_celia_slitharold' in persistent.cgs_celia")
    g.image("cg_celia_slitharold_2.jpg")
    g.condition("'cg_celia_slitharold' in persistent.cgs_celia")

    g.button("cg_celia_straddle_bag")
    g.image("cg_celia_straddle_bag.jpg")
    g.condition("'cg_celia_straddle_bag' in persistent.cgs_celia")

    g.button("cg_celia_straddle_knife")
    g.image("cg_celia_straddle_knife.jpg")
    g.condition("'cg_celia_straddle_knife' in persistent.cgs_celia")
    g.image("cg_celia_straddle_knife2.jpg")
    g.condition("'cg_celia_straddle_knife' in persistent.cgs_celia")

    g.button("cg_celia_straddle")
    g.image("cg_celia_straddle.jpg")
    g.condition("'cg_celia_straddle' in persistent.cgs_celia")

    g.button("cg_celia_strip_gun")
    g.image("cg_celia_strip_gun.jpg")
    g.condition("'cg_celia_strip_gun' in persistent.cgs_celia")

    g.button("cg_celia_taserbattle_1")
    g.image("cg_celia_taserbattle_1.jpg")
    g.condition("'cg_celia_taserbattle_1' in persistent.cgs_celia")

    g.button("cg_celia_taserbattle_2")
    g.image("cg_celia_taserbattle_2.jpg")
    g.condition("'cg_celia_taserbattle_2' in persistent.cgs_celia")
    g.image("cg_celia_taserbattle_3.jpg")
    g.condition("'cg_celia_taserbattle_2' in persistent.cgs_celia")

    g.button("cg_celia_whip1")
    g.image("cg_celia_whip1.jpg")
    g.condition("'cg_celia_whip1' in persistent.cgs_celia")

    g.button("cg_celia_whip2")
    g.image("cg_celia_whip2.jpg")
    g.condition("'cg_celia_whip2' in persistent.cgs_celia")

    g.button("cg_celia_wirekill_1")
    g.image("cg_celia_wirekill_1.jpg")
    g.condition("'cg_celia_wirekill_1' in persistent.cgs_celia")

    g.button("cg_celia_wirekill_2")
    g.image("cg_celia_wirekill_2.jpg")
    g.condition("'cg_celia_wirekill_2' in persistent.cgs_celia")



    g.button("cg_mason_armbolt")
    g.image("cg_mason_armbolt1.jpg")
    g.condition("'cg_mason_armbolt' in persistent.cgs_mason")
    g.image("cg_mason_armbolt2.jpg")
    g.condition("'cg_mason_armbolt' in persistent.cgs_mason")

    g.button("cg_mason_bear")
    g.image("cg_mason_bear1.jpg")
    g.condition("'cg_mason_bear' in persistent.cgs_mason")
    g.image("cg_mason_bear2.jpg")
    g.condition("'cg_mason_bear' in persistent.cgs_mason")

    g.button("cg_mason_beartrapped_gore")
    g.image("cg_mason_beartrapped_gore.jpg")
    g.condition("'cg_mason_beartrapped_gore' in persistent.cgs_mason")
    g.image("cg_mason_beartrapped_gore2.jpg")
    g.condition("'cg_mason_beartrapped_gore' in persistent.cgs_mason")

    g.button("cg_mason_beartrapped_looming")
    g.image("cg_mason_beartrapped_looming.jpg")
    g.condition("'cg_mason_beartrapped_looming' in persistent.cgs_mason")
    g.image("cg_mason_beartrapped_loomingknife.jpg")
    g.condition("'cg_mason_beartrapped_looming' in persistent.cgs_mason")

    g.button("cg_mason_beartrapped_crouch")
    g.image("cg_mason_beartrapped_crouch.jpg")
    g.condition("'cg_mason_beartrapped_crouch' in persistent.cgs_mason")

    g.button("cg_mason_beartrapped")
    g.image("cg_mason_beartrapped_day.jpg")
    g.condition("'cg_mason_beartrapped' in persistent.cgs_mason")
    g.image("cg_mason_beartrapped_night.jpg")
    g.condition("'cg_mason_beartrapped' in persistent.cgs_mason")
    g.image("cg_mason_beartrapped_twilight.jpg")
    g.condition("'cg_mason_beartrapped' in persistent.cgs_mason")

    g.button("cg_mason_bleedout")
    g.image("cg_mason_bleedout.jpg")
    g.condition("'cg_mason_bleedout' in persistent.cgs_mason")

    g.button("cg_mason_cabindoor")
    g.image("cg_mason_cabindoor.jpg")
    g.condition("'cg_mason_cabindoor' in persistent.cgs_mason")

    g.button("cg_mason_clouds")
    g.image("cg_mason_clouds.jpg")
    g.condition("'cg_mason_clouds' in persistent.cgs_mason")

    g.button("cg_mason_cabinfire")
    g.image("cg_mason_cabinfire.jpg")
    g.condition("'cg_mason_cabinfire' in persistent.cgs_mason")

    g.button("cg_mason_campfire")
    g.image("cg_mason_campfire.jpg")
    g.condition("'cg_mason_campfire' in persistent.cgs_mason")

    g.button("cg_mason_carry")
    g.image("cg_mason_carry.jpg")
    g.condition("'cg_mason_carry' in persistent.cgs_mason")

    g.button("cg_mason_dead")
    g.image("cg_mason_dead.jpg")
    g.condition("'cg_mason_dead' in persistent.cgs_mason")

    g.button("cg_mason_deer")
    g.image("cg_mason_deer1.jpg")
    g.condition("'cg_mason_deer' in persistent.cgs_mason")
    g.image("cg_mason_deer2.jpg")
    g.condition("'cg_mason_deer' in persistent.cgs_mason")
    g.image("cg_mason_deer2_blood.jpg")
    g.condition("'cg_mason_deer' in persistent.cgs_mason")

    g.button("cg_mason_gutting1")
    g.image("cg_mason_gutting1.jpg")
    g.condition("'cg_mason_gutting1' in persistent.cgs_mason")

    g.button("cg_mason_gutting2")
    g.image("cg_mason_gutting2.jpg")
    g.condition("'cg_mason_gutting2' in persistent.cgs_mason")

    g.button("cg_mason_kill")
    g.image("cg_mason_kill1.jpg")
    g.condition("'cg_mason_kill' in persistent.cgs_mason")
    g.image("cg_mason_kill2.jpg")
    g.condition("'cg_mason_kill' in persistent.cgs_mason")
    g.image("cg_mason_kill3.jpg")
    g.condition("'cg_mason_kill' in persistent.cgs_mason")

    g.button("cg_mason_log")
    g.image("cg_mason_log.jpg")
    g.condition("'cg_mason_log' in persistent.cgs_mason")

    g.button("cg_mason_snare")
    g.image("cg_mason_snare_blood.jpg")
    g.condition("'cg_mason_snare' in persistent.cgs_mason")
    g.image("cg_mason_snare_day.jpg")
    g.condition("'cg_mason_snare' in persistent.cgs_mason")
    g.image("cg_mason_snare_night.jpg")
    g.condition("'cg_mason_snare' in persistent.cgs_mason")
    g.image("cg_mason_snare_twilight.jpg")
    g.condition("'cg_mason_snare' in persistent.cgs_mason")

    g.button("cg_mason_snow")
    g.image("cg_mason_snow.jpg")
    g.condition("'cg_mason_snow' in persistent.cgs_mason")

    g.button("cg_mason_stump")
    g.image("cg_mason_stump.jpg")
    g.condition("'cg_mason_stump' in persistent.cgs_mason")

    g.button("cg_mason_trapped")
    g.image("cg_mason_trapped.jpg")
    g.condition("'cg_mason_trapped' in persistent.cgs_mason")

    g.button("cg_mason_treeview")
    g.image("cg_mason_treeview_day.jpg")
    g.condition("'cg_mason_treeview' in persistent.cgs_mason")
    g.image("cg_mason_treeview_evening.jpg")
    g.condition("'cg_mason_treeview' in persistent.cgs_mason")
    g.image("cg_mason_treeview_morning.jpg")
    g.condition("'cg_mason_treeview' in persistent.cgs_mason")
    g.image("cg_mason_treeview_night.jpg")
    g.condition("'cg_mason_treeview' in persistent.cgs_mason")

    g.button("cg_mason_upsidedown")
    g.image("cg_mason_upsidedown.jpg")
    g.condition("'cg_mason_upsidedown' in persistent.cgs_mason")
    g.image("cg_mason_upsidedown2.jpg")
    g.condition("'cg_mason_upsidedown' in persistent.cgs_mason")

    g.button("cg_mason_wall")
    g.image("cg_mason_wall.jpg")
    g.transform(left)
    g.condition("'cg_mason_wall' in persistent.cgs_mason")

    g.button("cg_mason_baneberry_drown")
    g.image("cg_mason_baneberry_drown.jpg")
    g.condition("'cg_mason_baneberry_drown' in persistent.cgs_mason")



    g.button("cg_fox_ultraclose")
    g.image("cg_fox_ultraclose2.jpg")
    g.condition("'cg_fox_ultraclose2' in persistent.cgs_fox")
    g.image("cg_fox_ultraclose_cocked.jpg")
    g.condition("'cg_fox_ultraclose_cocked' in persistent.cgs_fox")
    g.image("cg_fox_ultraclose3.jpg")
    g.condition("'cg_fox_ultraclose3' in persistent.cgs_fox")

    g.button("cg_fox_camera")
    g.image("cg_fox_camera1.jpg")
    g.condition("'cg_fox_camera' in persistent.cgs_fox")
    g.image("cg_fox_camera2.jpg")
    g.condition("'cg_fox_camera' in persistent.cgs_fox")
    g.image("cg_fox_camera3.jpg")
    g.condition("'cg_fox_camera' in persistent.cgs_fox")

    g.button("cg_fox_close_knife")
    g.image("cg_fox_close_knife.jpg")
    g.condition("'cg_fox_close_knife' in persistent.cgs_fox")

    g.button("cg_fox_gunjob_far")
    g.image("cg_fox_gunjob_far.jpg")
    g.condition("'cg_fox_gunjob_far' in persistent.cgs_fox")

    g.button("cg_fox_standover")
    g.image("cg_fox_standover.jpg")
    g.condition("'cg_fox_standover' in persistent.cgs_fox")

    g.button("cg_fox_nomask")
    g.image("cg_fox_nomask.jpg")
    g.condition("'cg_fox_nomask' in persistent.cgs_fox")

    g.button("cg_fox_holdingcam")
    g.image("cg_fox_holdingcam.jpg")
    g.condition("'cg_fox_holdingcam' in persistent.cgs_fox")

    g.button("cg_fox_ultraclose_gag")
    g.image("cg_fox_ultraclose_gag.jpg")
    g.condition("'cg_fox_ultraclose_gag' in persistent.cgs_fox")

    g.button("cg_fox_chokechain")
    g.image("cg_fox_chokechain.jpg")
    g.condition("'cg_fox_chokechain' in persistent.cgs_fox")

    g.button("cg_fox_ultraclose_speculum")
    g.image("cg_fox_ultraclose_speculum.jpg")
    g.condition("'cg_fox_ultraclose_speculum' in persistent.cgs_fox")

    g.button("cg_fox_light_sitting")
    g.image("cg_fox_light_sitting1.jpg")
    g.condition("'cg_fox_light_sitting' in persistent.cgs_fox")
    g.image("cg_fox_light_sitting2.jpg")
    g.condition("'cg_fox_light_sitting' in persistent.cgs_fox")
    g.image("cg_fox_light_sitting3.jpg")
    g.condition("'cg_fox_light_sitting' in persistent.cgs_fox")
    g.image("cg_fox_light_sitting4.jpg")
    g.condition("'cg_fox_light_sitting' in persistent.cgs_fox")

    g.button("cg_fox_nailgun_look")
    g.image("cg_fox_nailgun_look.jpg")
    g.condition("'cg_fox_nailgun_look' in persistent.cgs_fox")
    g.image("cg_fox_nailgun_look2.jpg")
    g.condition("'cg_fox_nailgun_look' in persistent.cgs_fox")

    g.button("cg_fox_torch_close_on")
    g.image("cg_fox_torch_close_on.jpg")
    g.condition("'cg_fox_torch_close_on' in persistent.cgs_fox")

    g.button("cg_MC_guts2")
    g.image("cg_MC_guts2.jpg")
    g.condition("'cg_MC_guts2' in persistent.cgs_fox")

    g.button("cg_fox_keep")
    g.image("cg_fox_keep1.jpg")
    g.condition("'cg_fox_keep' in persistent.cgs_fox")
    g.image("cg_fox_keep2.jpg")
    g.condition("'cg_fox_keep' in persistent.cgs_fox")
    g.image("cg_fox_keep3.jpg")
    g.condition("'cg_fox_keep' in persistent.cgs_fox")



    g.button("cg_mason_x_upsidedown")
    g.image("cg_mason_x_upsidedown.jpg")
    g.condition("'cg_mason_x_upsidedown' in persistent.cgs_mason_sex")

    g.button("cg_celia_straddle_sex")
    g.image("cg_celia_straddle_sex.jpg")
    g.condition("'cg_celia_straddle_sex' in persistent.cgs_celia_sex")

    g.button("cg_celia_straddle_sex2")
    g.image("cg_celia_straddle_sex2.jpg")
    g.condition("'cg_celia_straddle_sex2' in persistent.cgs_celia_sex")

    g.button("cg_derek_favoursex")
    g.image("cg_derek_favoursex.jpg")
    g.condition("'cg_derek_favoursex' in persistent.cgs_derek_sex")

    g.button("cg_derek_fireworks_gag2")
    g.image("cg_derek_fireworks_gag2.jpg")
    g.condition("'cg_derek_fireworks_gag2' in persistent.cgs_derek_sex")

    g.button("cg_derek_missionary")
    g.image("cg_derek_missionary.jpg")
    g.condition("'cg_derek_missionary' in persistent.cgs_derek_sex")

    g.button("cg_fox_nsfw1")
    g.image("cg_fox_nsfw1.jpg")
    g.condition("'cg_fox_nsfw1' in persistent.cgs_fox_sex")

    g.button("cg_fox_nsfw2")
    g.image("cg_fox_nsfw2.jpg")
    g.condition("'cg_fox_nsfw2' in persistent.cgs_fox_sex")

screen collections_art():
    tag menu





    use game_menu(_("Collections {size=50}{font=images/expressway-free.regular.ttf}-{/font}{/size} Art"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "Art Collection" style "collections_label" at center
            text _("Unlocking artwork will contribute to your overall completion.") style "collections_text" at center
            text _("Sexual content is not counted towards completion.") style "collections_text" at center
            null height 20

            xfill True

    use collection_art_navigation
screen collections_art_backgrounds():
    tag menu





    use game_menu(_("Collections {size=50}{font=images/expressway-free.regular.ttf}-{/font}{/size} Art"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "Art Collection {font=images/expressway-free.regular.ttf}-{/font} Backgrounds" style "collections_label" at center
            null height 20

            text _("Mountain") at center
            grid 3 3:

                spacing 0
                xfill True

                add g.make_button("bg_mason_meadow", "bg_mason_meadow_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("bg_mason_talltree", "bg_mason_talltree_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("bg_mason_thicket", "bg_mason_thicket_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("bg_mason_waterfall", "bg_mason_waterfall_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("bg_mason_cabin", "bg_mason_cabin_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("bg_mason_incabin", "bg_mason_incabin_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("bg_mason_swamp", "bg_mason_swamp_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                null
                null


            text _("City") at center
            grid 3 3:

                spacing 0
                xfill True

                add g.make_button("bg_celia_room", "bg_celia_room_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("bg_celia_lounge", "bg_celia_lounge_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("bg_celia_elevator", "bg_celia_elevator_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("bg_celia_office", "bg_celia_office_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("bg_celia_breakroom", "bg_celia_breakroom_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("bg_celia_stairs", "bg_celia_stairs_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("bg_celia_basement", "bg_celia_basement_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                null
                null

            text _("Desert") at center
            grid 3 3:

                spacing 0
                xfill True

                add g.make_button("bg_derek_camp", "bg_derek_camp_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("bg_derek_hill", "bg_derek_hill_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("bg_derek_fissure", "bg_derek_fissure_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("bg_derek_desert", "bg_derek_desert_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("bg_derek_deepdesert", "bg_derek_deepdesert_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("bg_derek_cave", "bg_derek_cave_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("bg_derek_theritz", "bg_derek_theritz_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                null
                null

            text _("Bunker") at center
            grid 3 1:

                spacing 0
                xfill True

                add g.make_button("cg_foxbg_dark", "cg_foxbg_dark_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_foxbg_light", "cg_foxbg_light_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                null

    use collection_art_navigation

screen collections_art_mason():
    tag menu





    use game_menu(_("Collections {size=50}{font=images/expressway-free.regular.ttf}-{/font}{/size} Art"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "Art Collection {font=images/expressway-free.regular.ttf}-{/font} {color=#9fff8f}Mason{/color}" style "collections_label" at center
            text _("Unlocking artwork will contribute to your overall completion.") style "collections_text" at center
            text _("Sexual content is not counted towards completion.") style "collections_text" at center
            null height 20

            grid 3 9:
                spacing 0

                xfill True

                add g.make_button("cg_mason_armbolt", "cg_mason_armbolt_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_bear", "cg_mason_bear_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_beartrapped_gore", "cg_mason_beartrapped_gore_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_mason_beartrapped_looming", "cg_mason_beartrapped_looming_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_beartrapped_crouch", "cg_mason_beartrapped_crouch_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_beartrapped", "cg_mason_beartrapped_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_mason_bleedout", "cg_mason_bleedout_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_cabindoor", "cg_mason_cabindoor_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_cabinfire", "cg_mason_cabinfire_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_mason_clouds", "cg_mason_clouds_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_campfire", "cg_mason_campfire_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_carry", "cg_mason_carry_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_mason_dead", "cg_mason_dead_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_deer", "cg_mason_deer_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_gutting1", "cg_mason_gutting1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_mason_gutting2", "cg_mason_gutting2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_kill", "cg_mason_kill_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_log", "cg_mason_log_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_mason_snare", "cg_mason_snare_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_snow", "cg_mason_snow_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_stump", "cg_mason_stump_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_mason_trapped", "cg_mason_trapped_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_treeview", "cg_mason_treeview_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_upsidedown", "cg_mason_upsidedown_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_mason_wall", "cg_mason_wall_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_mason_baneberry_drown", "cg_mason_baneberry_drown_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                null

    use collection_art_navigation

screen collections_art_celia():
    tag menu





    use game_menu(_("Collections {size=50}{font=images/expressway-free.regular.ttf}-{/font}{/size} Art"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "Art Collection {font=images/expressway-free.regular.ttf}-{/font} {color=#7cb3d2}Celia{/color}" style "collections_label" at center
            text _("Unlocking artwork will contribute to your overall completion.") style "collections_text" at center
            text _("Sexual content is not counted towards completion.") style "collections_text" at center
            null height 20

            grid 3 10:
                spacing 0

                xfill True

                add g.make_button("cg_celia_basement_cage", "cg_celia_basement_cage_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_ceiling_gun", "cg_celia_ceiling_gun_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_donuts", "cg_celia_donuts_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_celia_elevator_1", "cg_celia_elevator_1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_elevator_2", "cg_celia_elevator_2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_elevator_3", "cg_celia_elevator_3_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_celia_escape", "cg_celia_escape_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_fallen", "cg_celia_fallen_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_glass", "cg_celia_glass_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_celia_harold_choked", "cg_celia_harold_choked_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_harold_kill_1", "cg_celia_harold_kill_1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_harold_kill_2", "cg_celia_harold_kill_2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_celia_harold_shot", "cg_celia_harold_shot_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_harold_tripped", "cg_celia_harold_tripped_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_leave", "cg_celia_leave_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_celia_lounge", "cg_celia_lounge_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_poisoned", "cg_celia_poisoned_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_poisoned2", "cg_celia_poisoned2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_celia_roomcorner", "cg_celia_roomcorner_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_slitharold", "cg_celia_slitharold_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_straddle_bag", "cg_celia_straddle_bag_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_celia_straddle_knife", "cg_celia_straddle_knife_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_straddle", "cg_celia_straddle_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_strip_gun", "cg_celia_strip_gun_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_celia_taserbattle_1", "cg_celia_taserbattle_1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_taserbattle_2", "cg_celia_taserbattle_2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_whip1", "cg_celia_whip1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_celia_whip2", "cg_celia_whip2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_wirekill_1", "cg_celia_wirekill_1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_wirekill_2", "cg_celia_wirekill_2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

    use collection_art_navigation

screen collections_art_derek():
    tag menu





    use game_menu(_("Collections {size=50}{font=images/expressway-free.regular.ttf}-{/font}{/size} Art"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "Art Collection {font=images/expressway-free.regular.ttf}-{/font} {color=#ff3451}Derek{/color}" style "collections_label" at center
            text _("Unlocking artwork will contribute to your overall completion.") style "collections_text" at center
            text _("Sexual content is not counted towards completion.") style "collections_text" at center
            null height 20

            grid 3 20:
                spacing 0

                xfill True

                add g.make_button("cg_derek_angrystab", "cg_derek_angrystab_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_bat", "cg_derek_bat_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_cave", "cg_derek_cave_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_cave_sacrifice", "cg_derek_cave_sacrifice_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_cave_guts", "cg_derek_cave_guts_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_cham", "cg_derek_cham_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_crouchknife", "cg_derek_crouchknife_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_deadtom", "cg_derek_deadtom_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_demon", "cg_derek_demon_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_dragonstab", "cg_derek_dragonstab_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_favour", "cg_derek_favour_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_fireworks_crouch", "cg_derek_fireworks_crouch_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_fireworks_drop", "cg_derek_fireworks_drop_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_fireworks_gag1", "cg_derek_fireworks_gag1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_fireworks_gerb", "cg_derek_fireworks_gerb_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_firstblood_1", "cg_derek_firstblood_1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_firstblood_2", "cg_derek_firstblood_2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_helptom", "cg_derek_helptom_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_jack_choke", "cg_derek_jack_choke_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_jack_knuckles", "cg_derek_jack_knuckles_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_jackknife_close", "cg_derek_jackknife_close_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_jackknife_pin", "cg_derek_jackknife_pin_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_jackknife", "cg_derek_jackknife_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_jackmask", "cg_derek_jackmask_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_kdgut1", "cg_derek_kdgut1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_kdgut2", "cg_derek_kdgut2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_kdloom", "cg_derek_kdloom_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_loveanddeath", "cg_derek_loveanddeath_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_loveanddeath2", "cg_derek_loveanddeath2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_machete_sister", "cg_derek_machete_sister_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_machete", "cg_derek_machete_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_nightsky_machete1", "cg_derek_nightsky_machete1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_nightsky_machete2", "cg_derek_nightsky_machete2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_nightsky", "cg_derek_nightsky_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_quadbat", "cg_derek_quadbat_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_throat", "cg_derek_throat_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_sand", "cg_derek_sand_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_showdown_attempted", "cg_derek_showdown_attempted_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_showdown_backstab", "cg_derek_showdown_backstab_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_showdown_baddog", "cg_derek_showdown_baddog_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_showdown_standover", "cg_derek_showdown_standover_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_showdown_close", "cg_derek_showdown_close_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_showdown_closeup", "cg_derek_showdown_closeup_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_showdown_far", "cg_derek_showdown_far_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_showdown_jackstab1", "cg_derek_showdown_jackstab1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_showdown_jackstab2", "cg_derek_showdown_jackstab2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_showdown_jackstomp", "cg_derek_showdown_jackstomp_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_showdown_jaqdown", "cg_derek_showdown_jaqdown_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_showdown_machetejack", "cg_derek_showdown_machetejack_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_showdown_neck", "cg_derek_showdown_neck_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_stabbed", "cg_derek_stabbed_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_straddle", "cg_derek_straddle_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_theritz", "cg_derek_theritz_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_victims", "cg_derek_victims_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_vsmachete1", "cg_derek_vsmachete1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_vsmachete_hush", "cg_derek_vsmachete_hush_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_vsmachete5", "cg_derek_vsmachete5_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_watermachete1", "cg_derek_watermachete1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_watermachete2", "cg_derek_watermachete2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                null

    use collection_art_navigation

screen collections_art_fox():
    tag menu





    use game_menu(_("Collections {size=50}{font=images/expressway-free.regular.ttf}-{/font}{/size} Art"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "Art Collection {font=images/expressway-free.regular.ttf}-{/font} {color=#ffffff}Fox{/color}" style "collections_label" at center
            text _("Art from 'The Show Must Go On' DLC does not count towards completion.") style "collections_text" at center
            null height 20

            grid 3 5:
                spacing 0

                xfill True

                add g.make_button("cg_fox_ultraclose", "cg_fox_ultraclose2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_fox_camera", "cg_fox_camera1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_fox_close_knife", "cg_fox_close_knife_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_fox_gunjob_far", "cg_fox_gunjob_far_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_fox_standover", "cg_fox_standover_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_fox_nomask", "cg_fox_nomask_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_fox_holdingcam", "cg_fox_holdingcam_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_fox_ultraclose_gag", "cg_fox_ultraclose_gag_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_fox_chokechain", "cg_fox_chokechain_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_fox_ultraclose_speculum", "cg_fox_ultraclose_speculum_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_fox_light_sitting", "cg_fox_light_sitting1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_fox_nailgun_look", "cg_fox_nailgun_look_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_fox_torch_close_on", "cg_fox_torch_close_on_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_MC_guts2", "cg_MC_guts2_thumbnail.jpg", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_fox_keep", "cg_fox_keep1_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

    use collection_art_navigation

screen collections_art_sex():
    tag menu





    use game_menu(_("Collections {size=50}{font=images/expressway-free.regular.ttf}-{/font}{/size} Art"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "Art Collection {font=images/expressway-free.regular.ttf}-{/font} Sexual Content" style "collections_label" at center
            text _("Sexual content is not counted towards completion.") style "collections_text" at center
            null height 20

            grid 3 3:
                spacing 0

                xfill True

                add g.make_button("cg_mason_x_upsidedown", "cg_mason_x_upsidedown_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_straddle_sex", "cg_celia_straddle_sex_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_celia_straddle_sex2", "cg_celia_straddle_sex2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_derek_favoursex", "cg_derek_favoursex_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_fireworks_gag2", "cg_derek_fireworks_gag2_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_derek_missionary", "cg_derek_missionary_thumbnail", style="slot_button", xalign=0.5, yalign=0.5)

                add g.make_button("cg_fox_nsfw1", "images/cg_fox_nsfw1_thumbnail.jpg", style="slot_button", xalign=0.5, yalign=0.5)
                add g.make_button("cg_fox_nsfw2", "images/cg_fox_nsfw2_thumbnail.jpg", style="slot_button", xalign=0.5, yalign=0.5)
                null

    use collection_art_navigation


init python:
    g2 = Gallery()



    g2.transition = dissolve
    g2.locked_button = "images/gallery_locked.png"
    g2.idle_border = Frame("gui/frame_white_line.png",2,2)
    g2.hover_border = Frame("gui/frame_red_line.png",2,2)
    g2.navigation = False
    g2.span_buttons = False

    g2.button("concept_proto")
    g2.image("images/black.jpg","images/concept_proto.jpg")

    g2.button("concept_first")
    g2.image("images/black.jpg","images/concept_first.jpg")

    g2.button("concept_placeholders")
    g2.image("images/black.jpg","images/concept_placeholders.jpg")

    g2.button("concept_celia_sketches")
    g2.image("images/black.jpg","images/concept_celia_sketches.jpg")

    g2.button("concept_celia_success")
    g2.image("images/black.jpg","images/concept_celia_success.jpg")

    g2.button("concept_celia_blue")
    g2.image("images/black.jpg","images/concept_celia_blue.jpg")

    g2.button("concept_celia_chain")
    g2.image("images/black.jpg","images/concept_celia_chain.jpg")

    g2.button("concept_celia_lounge")
    g2.image("images/black.jpg","images/concept_celia_lounge.jpg")

    g2.button("concept_machete")
    g2.image("images/black.jpg","images/concept_machete.jpg")

    g2.button("concept_cham")
    g2.image("images/black.jpg","images/concept_cham.jpg")

    g2.button("concept_chibiheads")
    g2.image("images/black.jpg","images/concept_chibiheads.jpg")

    g2.button("concept_derek_bat")
    g2.image("images/black.jpg","images/concept_derek_bat.jpg")

    g2.button("concept_derek_sketches")
    g2.image("images/black.jpg","images/concept_derek_sketches.jpg")

    g2.button("concept_derek_ringgag")
    g2.image("images/black.jpg","images/concept_derek_ringgag.jpg")

    g2.button("concept_bonfire")
    g2.image("images/black.jpg","images/concept_bonfire.jpg")

    g2.button("concept_celia_splash")
    g2.image("images/black.jpg","images/concept_celia_splash.jpg")

    g2.button("concept_red")
    g2.image("images/black.jpg","images/concept_red.jpg")

    g2.button("concept_trio")
    g2.image("images/black.jpg","images/concept_trio.jpg")

    g2.button("concept_jack_sketches")
    g2.image("images/black.jpg","images/concept_jack_sketches.jpg")

    g2.button("concept_lizard_sketches")
    g2.image("images/black.jpg","images/concept_lizard_sketches.jpg")

    g2.button("concept_machete_sketches")
    g2.image("images/black.jpg","images/concept_machete_sketches.jpg")

    g2.button("concept_mason_blood")
    g2.image("images/black.jpg","images/concept_mason_blood.jpg")

    g2.button("concept_crack")
    g2.image("images/black.jpg","images/concept_crack.jpg")

    g2.button("concept_victims")
    g2.image("images/black.jpg","images/concept_victims.jpg")

    g2.button("concept_mason_sketches")
    g2.image("images/black.jpg","images/concept_mason_sketches.jpg")

    g2.button("concept_mason_splash")
    g2.image("images/black.jpg","images/concept_mason_splash.jpg")

    g2.button("concept_derek_back")
    g2.image("images/black.jpg","images/concept_derek_back.jpg")

    g2.button("concept_celia_drunk")
    g2.image("images/black.jpg","images/concept_celia_drunk.jpg")

    g2.button("concept_mason_pinup")
    g2.image("images/black.jpg","images/concept_mason_pinup.jpg")

    g2.button("concept_kd_chillin")
    g2.image("images/black.jpg","images/concept_kd_chillin.jpg")

    g2.button("concept_derek_unhinged")
    g2.image("images/black.jpg","images/concept_derek_unhinged.jpg")

    g2.button("concept_fox_1")
    g2.image("images/black.jpg","images/concept_fox_1.jpg")

    g2.button("concept_fox_2")
    g2.image("images/black.jpg","images/concept_fox_2.jpg")

    g2.button("concept_beg")
    g2.image("images/black.jpg","images/concept_beg.jpg")

    g2.button("concept_oldhabits")
    g2.image("images/black.jpg","images/concept_oldhabits.jpg")

    g2.button("concept_ren_bluemonday")
    g2.image("images/black.jpg","images/concept_ren_bluemonday.jpg")

    g2.button("concept_uglychibis")
    g2.image("images/black.jpg","images/concept_uglychibis.jpg")

    g2.button("concept_locked_1")
    g2.image("images/black.jpg","images/concept_sacrifice.jpg")

    g2.button("concept_locked_2")
    g2.image("images/black.jpg","images/concept_control.jpg")

    g2.button("concept_locked_3")
    g2.image("images/black.jpg","images/concept_blood.jpg")

    g2.button("concept_locked_4")
    g2.image("images/black.jpg","images/concept_DLC.jpg")

    g2.button("concept_silver")
    g2.image("images/black.jpg","gui/phone/overlay/silver.jpg")

    g2.button("concept_water")
    g2.image("images/black.jpg","gui/phone/overlay/water.jpg")

    g2.button("concept_birth")
    g2.image("images/black.jpg","gui/phone/overlay/birth.jpg")

screen concept_art():
    tag menu




    use game_menu(_("Concept Art"), scroll="viewport"):

        style_prefix "about"

        vbox:
            null height 10
            vpgrid:
                allow_underfull True
                cols 5
                xspacing 10
                yspacing 10
                xmaximum 950
                transclude

                add g2.make_button("concept_proto", "images/concept_proto_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_first", "images/concept_first_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_placeholders", "images/concept_placeholders_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_celia_sketches", "images/concept_celia_sketches_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_celia_success", "images/concept_celia_success_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_celia_blue", "images/concept_celia_blue_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_celia_chain", "images/concept_celia_chain_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_celia_lounge", "images/concept_celia_lounge_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_machete", "images/concept_machete_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_cham", "images/concept_cham_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_chibiheads", "images/concept_chibiheads_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_victims", "images/concept_victims_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_derek_sketches", "images/concept_derek_sketches_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_derek_bat", "images/concept_derek_bat_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_derek_ringgag", "images/concept_derek_ringgag_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_bonfire", "images/concept_bonfire_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_celia_splash", "images/concept_celia_splash_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_red", "images/concept_red_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_trio", "images/concept_trio_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_jack_sketches", "images/concept_jack_sketches_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_lizard_sketches", "images/concept_lizard_sketches_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_machete_sketches", "images/concept_machete_sketches_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_mason_blood", "images/concept_mason_blood_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_crack", "images/concept_crack_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_mason_sketches", "images/concept_mason_sketches_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_mason_splash", "images/concept_mason_splash_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_derek_back", "images/concept_derek_back_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_celia_drunk", "images/concept_celia_drunk_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_mason_pinup", "images/concept_mason_pinup_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_kd_chillin", "images/concept_kd_chillin_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_derek_unhinged", "images/concept_derek_unhinged_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                add g2.make_button("concept_uglychibis", "images/concept_uglychibis_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                if persistent.bluecounter == True:
                    add g2.make_button("concept_fox_1", "images/concept_fox_1_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                    add g2.make_button("concept_fox_2", "images/concept_fox_2_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                    add g2.make_button("concept_ren_bluemonday", "images/concept_ren_bluemonday_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                    add g2.make_button("concept_oldhabits", "images/concept_oldhabits_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                    add g2.make_button("concept_beg", "images/concept_beg_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                else:
                    add g2.make_button("concept_locked_4", "images/concept_locked_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                    add g2.make_button("concept_locked_4", "images/concept_locked_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                    add g2.make_button("concept_locked_4", "images/concept_locked_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                    add g2.make_button("concept_locked_4", "images/concept_locked_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                    add g2.make_button("concept_locked_4", "images/concept_locked_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                if persistent.greencounter == True:
                    add g2.make_button("concept_water", "gui/phone/overlay/water_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                else:
                    add g2.make_button("concept_locked_1", "images/concept_locked_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                if persistent.bluecounter == True:
                    add g2.make_button("concept_silver", "gui/phone/overlay/silver_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                else:
                    add g2.make_button("concept_locked_2", "images/concept_locked_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                if persistent.redcounter == True:
                    add g2.make_button("concept_birth", "gui/phone/overlay/birth_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)
                else:
                    add g2.make_button("concept_locked_3", "images/concept_locked_thumb.jpg", xalign=0.5, yalign=0.5, yminimum=150)



init python:
    mr = MusicRoom(channel=u'music', fadeout=0.0, fadein=0.0, loop=True, single_track=False, shuffle=False, stop_action=None)
    mr.add("music/celias_theme.ogg")
    mr.add("music/dereks_theme.ogg")
    mr.add("music/masons_theme.ogg")
    mr.add("music/lizards_theme.ogg")
    mr.add("music/jacks_theme.ogg")
    mr.add("music/machetes_theme.ogg")
    mr.add("music/game_show.ogg")
    mr.add("music/you_died.ogg")
    mr.add("music/music_but_at_what_cost.ogg")
    mr.add("music/music_killer.ogg")
    mr.add("music/music_city_lights.ogg")
    mr.add("music/music_desert_escape.ogg")
    mr.add("music/music_changed.ogg")
    mr.add("music/music_machete_ending.ogg")
    mr.add("music/music_achtung.ogg")
    mr.add("music/music_achtung_2.ogg")
    mr.add("music/ambient_dire_situation.ogg")
    mr.add("music/music_nightmare.ogg")
    mr.add("music/music_snow.ogg")
    mr.add("music/music_175oz.ogg")
    mr.add("music/ambient_fox_01.ogg")
    mr.add("music/ambient_fox_02.ogg")
    mr.add("music/ambient_fox_03.ogg")
    mr.add("music/ambient_fox_04.ogg")
    mr.add("music/ambient_fox_06.ogg")
    mr.add("music/ambient_fox_extra_02.ogg")
    mr.add("music/ambient_fox_08.ogg")
    mr.add("music/ambient_fox_09.ogg")
    mr.add("music/music_emptylove.ogg")
    mr.add("music/main_menu.mp3")
    mr.add("music/Graveyardguy_Gore.mp3")
    mr.add("music/music_elevator_muzak.ogg")
    mr.add("music/ambient_fox_buddy.ogg")

screen musicroom():
    tag menu





    use game_menu(_("Music"), scroll="viewport"):

        style_prefix "about"

        vbox:
            hbox:
                xsize 770
                spacing 5
            $ music_list = [("Celia's Theme", "music/celias_theme.ogg", "4:15", "Envato.com"), ("Derek's Theme", "music/dereks_theme.ogg", "1:33", "Envato.com"), ("Mason's Theme", "music/masons_theme.ogg", "1:33", "Envato.com"), ("Komodo and Dragon", "music/lizards_theme.ogg", "3:13", "Envato.com"), ("Jack's Theme", "music/jacks_theme.ogg", "2:16", "Envato.com"), ("Machete's Theme", "music/machetes_theme.ogg", "2:16", "Envato.com"), ("Let the Game Begin", "music/game_show.ogg", "2:27", "AudioBlocks.com"), ("You Died", "music/you_died.ogg", "1:55", "Envato.com"), ("But At What Cost", "music/music_but_at_what_cost.ogg", "1:30", "Envato.com"), ("Killer", "music/music_killer.ogg", "2:49", "Envato.com"), ("City Lights", "music/music_city_lights.ogg", "2:46", "Envato.com"), ("Desert Escape", "music/music_desert_escape.ogg", "3:24", "Envato.com"), ("You Changed", "music/music_changed.ogg", "1:55", "Envato.com"), ("His Revenge", "music/music_machete_ending.ogg", "2:19", "Envato.com"), ("Achtung", "music/music_achtung.ogg", "2:19", "BARBATUS"), ("Warnung", "music/music_achtung_2.ogg", "1:09", "BARBATUS"), ("A Dire Situation", "music/ambient_dire_situation.ogg", "2:17", "Envato.com"), ("Nightmare", "music/music_nightmare.ogg", "1:21", "Envato.com"), ("Snow", "music/music_snow.ogg", "2:00", "Envato.com"), ("175oz", "music/music_175oz.ogg", "1:24", "BARBATUS"), ("Archaeopteris", "music/ambient_fox_01.ogg", "4:43", "BARBATUS"), ("Host Pathogen Interface", "music/ambient_fox_02.ogg", "5:59", "BARBATUS"), ("Eunuch Phenomenon", "music/ambient_fox_03.ogg", "1:10", "BARBATUS"), ("Hindbrain Self", "music/ambient_fox_04.ogg", "8:09", "BARBATUS"), ("Autolytic Cell Destruction", "music/ambient_fox_06.ogg", "3:12", "BARBATUS"), ("So Much For The Tolerant Left", "music/ambient_fox_extra_02.ogg", "3:15", "BARBATUS"), ("Achtung Perpetual", "music/ambient_fox_08.ogg", "2:22", "BARBATUS"), ("I've Been Good Sir", "music/ambient_fox_09.ogg", "6:03", "BARBATUS"), ("Empty Love", "music/music_emptylove.ogg", "5:28", "BARBATUS"), ("Adaptive Behaviors", "music/main_menu.mp3", "2:23", "BARBATUS"), ("GORE", "music/Graveyardguy_Gore.mp3", "3:08", "Graveyardguy"), ("Going Up", "music/music_elevator_muzak.ogg", "1:38", "BARBATUS"), ("Buddy I Been Great", "music/ambient_fox_buddy.ogg", "8:50", "BARBATUS")]
            for song in music_list:
                $ music_name = song[0]
                $ music_file = song[1]
                $ music_time = song[2]
                $ music_source = song[3]
                hbox:
                    xsize 900
                    spacing 5
                    vbox:
                        xsize 550
                        if renpy.variant("small"):
                            xsize 500
                        textbutton "[music_name]" action mr.Play(music_file) style "mr_song"
                    vbox:
                        xsize 60
                        text _("[music_time]") style "mr_time"
                    vbox:
                        xsize 250
                        if renpy.variant("small"):
                            xsize 300
                        text _("[music_source]") style "mr_src"

    hbox:
        xpos 0.5
        xoffset -100
        ypos 70
        imagebutton auto "images/music_previous_%s.png" action mr.Previous()
        null width 20
        imagebutton auto "images/music_playpause_%s.png" action mr.TogglePause()
        null width 20
        imagebutton auto "images/music_next_%s.png" action mr.Next()
        null width 50
        imagebutton auto "images/music_loop_%s.png" action mr.ToggleLoop()
        null width 10
        imagebutton auto "images/music_shuffle_%s.png" action mr.ToggleShuffle()
        null width 10
        imagebutton auto "images/music_single_%s.png" action mr.ToggleSingleTrack()

    on "replace" action [Stop("music"),Stop("music2"),Stop("ambient")]
    on "replaced" action Play("music", "music/main_menu.mp3")

style mr_song:
    left_padding 25
    background None
    selected_background "images/now_playing.png"
style mr_song_text:
    size 22
    color "#FFFFFF"
    insensitive_color "#666666"
    selected_color "#cc0000"
style mr_song_text:
    variant "small"
    size 35
style mr_time:
    size 22
    color "#666666"
style mr_time:
    variant "small"
    size 35
style mr_src:
    size 22
    color "#666666"
style mr_src:
    variant "small"
    size 35



screen character_bios():
    $ derek_endings_complete = len(persistent.endings_derek)
    $ mason_endings_complete = len(persistent.endings_mason)
    $ celia_endings_complete = len(persistent.endings_celia)
    tag menu




    use game_menu(_("Character Bios")):

        style_prefix "about"

        vbox:
            null height 10
            vpgrid:
                allow_underfull True
                cols 3
                xspacing 10
                yspacing 10
                xsize 950
                ysize 550
                transclude

                if mason_endings_complete >= 15:
                    imagebutton auto "character_bio_mason_bloody_%s.png" action ShowMenu("character_bios_mason") style "character_bio_button"
                else:
                    imagebutton auto "character_bio_mason_%s.png" action ShowMenu("character_bios_mason") style "character_bio_button"
                if celia_endings_complete >= 14:
                    imagebutton auto "character_bio_celia_bloody_%s.png" action ShowMenu("character_bios_celia") style "character_bio_button"
                else:
                    imagebutton auto "character_bio_celia_%s.png" action ShowMenu("character_bios_celia") style "character_bio_button"
                if derek_endings_complete >= 21:
                    imagebutton auto "character_bio_derek_bloody_%s.png" action ShowMenu("character_bios_derek") style "character_bio_button"
                else:
                    imagebutton auto "character_bio_derek_%s.png" action ShowMenu("character_bios_derek") style "character_bio_button"
                imagebutton auto "character_bio_harold_%s.png" action ShowMenu("character_bios_harold") style "character_bio_button"
                imagebutton auto "character_bio_jack_%s.png" action ShowMenu("character_bios_jack") style "character_bio_button"
                imagebutton auto "character_bio_dragon_%s.png" action ShowMenu("character_bios_dragon") style "character_bio_button"
                imagebutton auto "character_bio_komodo_%s.png" action ShowMenu("character_bios_komodo") style "character_bio_button"
                imagebutton auto "character_bio_machete_%s.png" action ShowMenu("character_bios_machete") style "character_bio_button"
                imagebutton auto "character_bio_cham_%s.png" action ShowMenu("character_bios_cham") style "character_bio_button"
                imagebutton auto "character_bio_tom_%s.png" action ShowMenu("character_bios_tom") style "character_bio_button"
                imagebutton auto "character_bio_jaq_%s.png" action ShowMenu("character_bios_jaq") style "character_bio_button"
                imagebutton auto "character_bio_richard_%s.png" action ShowMenu("character_bios_richard") style "character_bio_button"
                imagebutton auto "character_bio_lich_%s.png" action If(renpy.seen_image("cg_mason_snow"), ShowMenu("character_bios_lich")) style "character_bio_button"
                imagebutton auto "character_bio_announcer_%s.png" action If(persistent.bluecounter, ShowMenu("character_bios_announcer")) style "character_bio_button"
                imagebutton auto "character_bio_demon_%s.png" action If(renpy.seen_image("cg_derek_demon"), ShowMenu("character_bios_demon")) style "character_bio_button"

style character_bio_button:
    xsize 280
    ysize 90



screen character_bios_mason():
    $ mason_endings_complete = len(persistent.endings_mason)
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_mason.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Full Name: Mason Heiral")
                    vbox:
                        xminimum 200
                        text _("Age: 38")
                    vbox:
                        xminimum 200
                        text _("Height: 6'5\"")
                null height 10
                text ("Mason lives alone in a cabin, deep in the Canadian wilderness.") size 17
                null height 10
                text ("When he was a teenager, he killed his girlfriend 'Sandy' and fashioned a knife, using her bone for the handle. Ever since that incident, his passion for hunting has expanded to include his fellow humans.") size 17
                null height 10
                text ("He began by hunting the odd hiker and camper who came through his area, but eventually people stopped coming. After some thought, he decided to visit an auction to 'stock' his mountain with new prey.") size 17
                if mason_endings_complete >= 15:
                    null height 10
                    text ("Mason was born and raised in a religious cult who originally settled a few kilometers from his current location.") size 17
                    null height 10
                    text ("Mason was well loved and respected in his little off-the-grid community, as he became revered for his hunting skills. After he killed his girlfriend, he went back to the cult and hunted every other member down with a smile on his face. He murdered his entire family and community.") size 17
                    null height 10
                    text ("In the empty houses of his dead family, he found all the money he would ever need. Over the next several years, he used the internet in the leader's building to learn about the outside world. He discovered ways of travelling, ways of hunting, and eventually- how to buy people.") size 17
                    null height 20
        textbutton "< Back to Characters" action ShowMenu("character_bios")

screen character_bios_celia():
    $ celia_endings_complete = len(persistent.endings_celia)
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_celia.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Full Name: Celia Lede")
                    vbox:
                        xminimum 200
                        text _("Age: 32")
                    vbox:
                        xminimum 200
                        text _("Height: 5'9\"")
                null height 10
                text ("Celia is an inside director for a very succesful advertising firm.") size 17
                null height 10
                text ("Her entire life revolves around her career and climbing the corporate ladder. She married her husband Harold when she was 24 exclusively to further her own career.") size 17
                null height 10
                text ("The stress of her single-minded lifestyle has manifested into functional alcoholism and several violent tendencies.") size 17
                if celia_endings_complete >= 14:
                    null height 10
                    text ("At first, Celia satisfied her violent thoughts by watching illegal torture and murder streams online.") size 17
                    null height 10
                    text ("However, she soon found it wasn't enough. When she was 29, she tricked an intern into following her to an abandoned office complex before brutally murdering him.") size 17
                    null height 10
                    text ("After two more interns dissappeared in quick succession, police began to ask questions around her company. Celia managed to control her urges to avoid being found out- until a link to an auction appeared after one of her favourite streams.") size 17
                    null height 20
        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_derek():
    $ derek_endings_complete = len(persistent.endings_derek)
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_derek.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Full Name: Derek Goffard")
                    vbox:
                        xminimum 200
                        text _("Age: 27")
                    vbox:
                        xminimum 200
                        text _("Height: 5'10\"")
                null height 10
                text ("Derek is the eldest son and heir of an insanely wealthy investor/luxury goods mogul.") size 17
                null height 10
                text ("Throughout most of the year, Derek does whatever his father tells him to do to prepare for his eventual takeover of his father's company. He attends parties and rubs shoulders with other wealthy and powerful people to further his dad's networking opportunities.") size 17
                null height 10
                text ("Derek hasn't been the perfect heir, however. His abysmal performance in university coupled with multiple illegal/violent incidents have caused severe friction between himself and his father- who has had to pay to cover everything up.") size 17
                if derek_endings_complete >= 21:
                    null height 10
                    text ("Eventually, Derek's father had enough. He offered a deal to Derek.") size 17
                    null height 10
                    text ("His father told him about a group that meets once a year out in the desert. A place where he could do absolutely anything he wanted, to 'get it all out of his system'. Derek was accepted into the group after a sizable 'donation' was made. He even pointed Derek to an auction to obtain his own mandatory victim.") size 17
                    null height 10
                    text ("Derek made the mistake of asking how his father had all these connections once. His punishment was so intense, he never asked his father another question again.") size 17
                    null height 20
        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_jack():
    tag menu

    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_jack.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Name: \"Jack\"")
                    vbox:
                        xminimum 200
                        text _("Age: 46")
                    vbox:
                        xminimum 200
                        text _("Height: 5'11\"")
                null height 10
                text ("\"Jack\" (real name: Dean) is the oldest and currently longest standing member of the desert group.") size 17
                null height 10
                text ("During the rest of the year he works as a corrupt police officer- covering up misconduct and accepting bribes to pay for his expensive habits.") size 17
                null height 10
                text ("He looks forward to the yearly 'vacation', and enjoys the thrill of kidnapping his own victim himself. He feels that 'the chase is the best part'.") size 17

        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_dragon():
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_dragon.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Name: \"Dragon\"")
                    vbox:
                        xminimum 200
                        text _("Age: 25")
                    vbox:
                        xminimum 200
                        text _("Height: 5'8\"")
                null height 10
                text ("\"Dragon\" (real name: Jason, goes by Jace) is a college dropout who works at a distribution facility with his 'best friend' Mike.") size 17
                null height 10
                text ("He and Mike have been in the desert group the longest, aside from Jack. At first they joined for the simple thrill of murder, but they eventually became obsessed with the occult.") size 17
                null height 10
                text ("Jace enthusiastically follows along with Mike's ideas. He's generally quite happy to take on the physically demanding tasks, especially when kidnapping or working on their 'rituals'.") size 17

        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_komodo():
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_komodo.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Name: \"Komodo\"")
                    vbox:
                        xminimum 200
                        text _("Age: 26")
                    vbox:
                        xminimum 200
                        text _("Height: 5'7\"")
                null height 10
                text ("\"Komodo\" (real name: Micheal, goes by Mike) is a worker at a distribution facility with his 'best friend' Jace.") size 17
                null height 10
                text ("Mike and Jace have been attending the desert group for years. They usually bring victims from Jace's old college campus.") size 17
                null height 10
                text ("Recently however, Mike had stumbled upon some very strange websites centered around the occult. He learned about a different way of seeing the world, and a Demon.") size 17
                null height 10
                text ("Jace was, of course, only too happy to help.") size 17

        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_machete():
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_machete.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Name: \"Machete\"")
                    vbox:
                        xminimum 200
                        text _("Age: 23")
                    vbox:
                        xminimum 200
                        text _("Height: 6'0\"")
                null height 10
                text ("\"Machete\" (real name unknown) is the newest member of the desert group.") size 17
                null height 10
                text ("He had to prove himself worthy by performing various criminal tasks to be allowed in.") size 17
                null height 10
                text ("Despite his recent acceptance, the rest of the group remain wary of him. His quiet demeanor and decisive actions tend to unsettle the other members.") size 17
                if renpy.seen_image("cg_derek_machete_sister"):
                    null height 10
                    text ("He regrets everything he's done to be admitted into the group, but he chose to stop at nothing to get revenge for his sister.") size 17
                    null height 10
                    text ("He feels as though he's completely lost his identity and humanity to his 'purpose'.") size 17

        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_cham():
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_cham.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Name: Chamomile")
                    vbox:
                        xminimum 200
                        text _("Age: 23")
                    vbox:
                        xminimum 200
                        text _("Height: 5'4\"")
                null height 10
                text ("A very unfortunate college student, who seems to be plagued with bad luck.") size 17
                null height 10
                text ("She majored in biology, hoping to get into a research field. When she was walking home after studying far into the night, she was knocked out and kidnapped by Komodo and Dragon.") size 17

        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_tom():
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_tom.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Name: Thomas")
                    vbox:
                        xminimum 200
                        text _("Age: 26")
                    vbox:
                        xminimum 200
                        text _("Height: 5'6\"")
                null height 10
                text ("Tom is a college student, taking a media development course centered around sound design.") size 17
                null height 10
                text ("He took a few years off after high school, kind of meandering through life without an aim for a while. However, he eventually found a passion for making music.") size 17
                null height 10
                text ("Despite tons of research and hard work, he was never really able to get his brand off the ground, so he decided to head to college to get some formal education on the subject. Late one night, as he was about to head home, he was abducted by Komodo and Dragon.") size 17

        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_jaq():
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_jaq.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Name: Jaqueline")
                    vbox:
                        xminimum 200
                        text _("Age: 24")
                    vbox:
                        xminimum 200
                        text _("Height: 5'8\"")
                null height 10
                text ("Jaqueline is a young trades worker learning to paint houses.") size 17
                null height 10
                text ("She takes pride in her work and also frequently goes to the gym. Her mom pesters her to get a higher education, but she loves her current career path. Due to the friction with her family over her career, she tends to choose to spend time with friends instead.") size 17
                null height 10
                text ("She was violently abducted by Jack in broad daylight, unlucky to have no witnesses.") size 17

        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_richard():
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_richard.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Name: Richard")
                    vbox:
                        xminimum 200
                        text _("Age: 30")
                    vbox:
                        xminimum 200
                        text _("Height: 5'11\"")
                null height 10
                text ("Richard is unemployed.") size 17
                null height 10
                text ("Richard met Machete online, as Machete was posing as someone else. Eventually, Richard agreed to meet in person- in private. Once Richard arrived, Machete easily overpowered and abducted him.") size 17
                null height 10
                text ("He got his black eye from Machete shortly after arriving at the desert.") size 17

        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_harold():
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_harold.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Name: Harold")
                    vbox:
                        xminimum 200
                        text _("Age: 51")
                    vbox:
                        xminimum 200
                        text _("Height: 5'9\"")
                null height 10
                text ("Harold is Celia's husband and the chief operations officer of the advertising firm they both work for.") size 17
                null height 10
                text ("He knows that she's been up to shady business after hours, and that she bought an abandoned office building, but he doesn't know the extent of her crimes.") size 17
                null height 10
                text ("However, he simply doesn't care. She turns a blind eye to his constant infidelity and he turns a blind eye to her violent tendencies.") size 17
                null height 10
                text ("Their relationship is more of an uneasy truce than a proper marriage.") size 17

        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_lich():
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_lich.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Name: ???")
                    vbox:
                        xminimum 200
                        text _("Age: ???")
                    vbox:
                        xminimum 200
                        text _("Height: 6'11\"")
                null height 10
                text ("A monster in a pond; a lich of sorts. He used to be a human once, a long time ago.") size 17
                null height 10
                text ("He never fully found his way to death, so he came to the mountain to lie in a pond.") size 17
                null height 10
                text ("His intention was to stay in the River between life and death, but curiosity roused him. He kept getting visitors, so he wandered back to see where the deaths were coming from.") size 17
                null height 10
                text ("He didn't realize his body would be so different. So much was gone.") size 17
                null height 10
                text ("He was lonely. And he was hungry.") size 17
        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_demon():
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_demon.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Name: ???")
                    vbox:
                        xminimum 200
                        text _("Age: ???")
                    vbox:
                        xminimum 200
                        text _("Height: 8'5\"")
                null height 10
                text ("An awful Demon with a gaping hole in his chest.") size 17
                null height 10
                text ("He is a creature of pure sadism and agony, given his demonic state by a usurper king.") size 17
                null height 10
                text ("He is new and voracious, and eternally empty.") size 17

        textbutton "< Back to Characters" action ShowMenu("character_bios")
screen character_bios_announcer():
    tag menu
    use game_menu(_("Character Bios"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yminimum 520
            vbox:
                add "images/character_bio_header_announcer.jpg"
                null height 10
                hbox:
                    vbox:
                        xminimum 500
                        text _("Name: ???")
                    vbox:
                        xminimum 200
                        text _("Age: 47")
                    vbox:
                        xminimum 200
                        text _("Height: 5'1\"")
                null height 10
                text ("A mysterious, inhuman figure who leads an illegal auction.") size 17
                null height 10
                text ("Rumors say he's incredibly experienced in the art of kidnapping. He rose up from humble beginnings, a captive himself.") size 17
                null height 10
                text ("After he gained his freedom, he dabbled in live-stream murder. His knack for showmanship won him instant popularity.") size 17
                null height 10
                text ("Now, with decades of experience, he guards his identity perfectly. He controls an entire auction system- although, from time to time, he will still put on a show of his own.") size 17

        textbutton "< Back to Characters" action ShowMenu("character_bios")







screen choosename():
    tag menu

    window:
        style "nvl_window"
        has vbox:
            xalign 0.5
            yalign 0.5
        text "{font=images/still-time.regular.ttf}{color=#c00}{size=50}What's your name?{/size}{/color}{/font}\n" xalign 0.5 yalign 0.4
        input value VariableInputValue('player_name') length 10 xalign 0.5 yalign 0.5 color "#FFFFFF"
        null height 20
        textbutton "{font=images/still-time.regular.ttf}Next >{/font}" action Return(value=_return) xalign 0.5
        key "K_RETURN" action Return(value=_return)

screen startgame():
    $ game_endings_total = 50
    $ game_art_total = 115
    $ game_bgs_total = 21
    $ game_completion_total = game_endings_total + game_art_total + game_bgs_total
    $ game_endings = (len(persistent.endings_derek)) + (len(persistent.endings_mason)) + (len(persistent.endings_celia))
    $ game_art = (len(persistent.cgs_derek)) + (len(persistent.cgs_mason)) + (len(persistent.cgs_celia))
    $ game_bgs = (len(persistent.bgs_seen))
    $ game_completion = game_art + game_endings + game_bgs
    if game_completion >= game_completion_total:
        $ meme_mode_available = True
    else:
        $ meme_mode_available = False
    tag menu
    text _("This game may use pronouns for the player in some dialogue. Your choice will not affect any body descriptions or gameplay- only the use of pronouns and some dialogue.") style "pref_tooltip1"
    text _("This game contains optional sexual content: including nudity, non consensual sex acts, detailed descriptions of sex acts, and sexually explicit art. Turning sexual content off will remove all of these scenes and art from gameplay. Sexual content is not included in completion rewards or percentages.") style "pref_tooltip2"
    add _("images/arrow_small_right.png"):
        xpos 380
        ypos 263
        if renpy.variant("small"):
            xpos 280
    add _("images/arrow_small_left.png"):
        xpos 815
        ypos 263
        if renpy.variant("small"):
            xpos 965
    vbox:
        xalign 0.5
        yalign 0.5

        hbox:
            box_wrap True

            if not renpy.variant("small"):
                null width 50
            vbox:
                xminimum 200
                style_prefix "radio"
                label _("Pronoun")
                textbutton _("They/Them") action SetVariable("pronoun", "they")
                textbutton _("She/Her") action SetVariable("pronoun", "she")
                textbutton _("He/Him") action SetVariable("pronoun", "he")
            if renpy.variant("small"):
                null width 20
            vbox:
                xminimum 240
                style_prefix "radio"
                label _("Sexual")
                textbutton _("Art and Text") action SetVariable("sexcontent", "yes")
                textbutton _("Text Only") action SetVariable("sexcontent", "yestext")
                textbutton _("No") action SetVariable("sexcontent", "no")



        null height (4 * gui.pref_spacing)
        hbox:
            xalign 0.5
            yalign 0.5
            textbutton _("I'm Ready.") action Return(value=_return) style "confirmbutton"
            null width 50
    if meme_mode_available:
        vbox:
            xpos 450
            ypos 100
            hbox:
                style_prefix "radio"
                label _("{color=#ffffff}Memelord Mode{/color}")
                null width 30
                vbox:
                    textbutton _("Yes") action SetVariable("meme_mode", True)
                    textbutton _("No") action SetVariable("meme_mode", False)


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style sexcontent_label_text is pref_label_text
style sexcontent_label_text:
    size 30
style sexcontent_choice is radio_button
style sexcontent_choice_text:
    size 20

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin gui.pref_spacing

style pref_label_text:
    yalign 1.0
    font "images/feral.regular.ttf"
    size 40

style confirmbutton:
    xalign 0.5
style confirmbutton_text:
    hover_color "#c00"
style confirmbutton_text:
    variant "small"
    size 36
style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450
style preftooltip:
    color "#888"
    size 14
    xsize 250
style preftooltip:
    variant "small"
    size 20
style pref_tooltip1 is preftooltip:
    xpos 120
    ypos 250
    text_align 1.0
style pref_tooltip1 is preftooltip:
    variant "small"
    xpos 20
    ypos 250
style pref_tooltip2 is preftooltip:
    xpos 855
    ypos 250
style pref_tooltip2 is preftooltip:
    variant "small"
    xpos 1000
    ypos 250








screen history():




    predict False tag menu

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5







screen help_navigation():
    frame:
        top_margin 40
        left_margin 560
        has hbox
        textbutton " How To Play" action ShowMenu("help") style "lines_button"
        textbutton " Controls" action ShowMenu("controls") style "lines_button"



screen help():
    tag menu

    use game_menu(_("Help"), scroll="viewport"):

        vbox:
            spacing 15

            label _("How To Play:")
            text _("This game revolves around the passage of time. Every major action you take (like searching an area or travelling) will advance time by one hour. As time passes, your stats will change (you may become hotter or colder, you will lose energy and food, and if you're gravely injured you will lose health).")
            text _("The passage of time also affects your environment and the actions of dangerous characters. Certain events will happen at certain times, in certain places. It's up to you to find or avoid these events.")
            hbox:
                spacing 15
                xmaximum 600
                vbox:
                    label _("The Map:")
                    text _("On all three game paths, you'll have the opportunity to obtain a map. You may get it by reaching a high up place, finding it, or you may have to draw it yourself. The map can be accessed any time you can travel.")
                frame:
                    add "images/screens_help_map.jpg" zoom 0.5
            hbox:
                spacing 15
                xmaximum 600
                frame:
                    add "images/screens_help_inventory.jpg" zoom 0.5
                vbox:
                    xminimum 600
                    label _("Your Inventory:")
                    text _("During your game, you may pick up items. You may get them from events or by searching your surroundings. Each item in your inventory can be clicked on to check it. Sometimes, if conditions are right, you may be able to use an item in a special way.")
            hbox:
                spacing 15
                xmaximum 600
                vbox:
                    label _("Actions:")
                    text _("When your game is not in the middle of an event, your 'Actions' button will light up. From this button, you can choose to sleep to restore energy, search for information/items, or sometimes perform a special action. Performing a search will typically use up an hour of time, so use it wisely!")
                frame:
                    add "images/screens_help_actions.jpg" zoom 0.5
            hbox:
                spacing 15
                xmaximum 600
                frame:
                    add "images/screens_help_status.jpg" zoom 0.5
                vbox:
                    xminimum 600
                    label _("Status:")
                    text _("When your 'Status' button is lit up, you can check on your player status. Everything on the status screen can affect your gameplay.")
                    text _("{color=#cc0000}Health{/color}: If you run out of health, you will die.")
                    text _("{color=#cc0000}Sanity{/color}: If you run low on sanity, your character may experience problems. Running out of sanity is also likely to kill you.")
                    text _("{color=#cc0000}Food{/color}: Running out of food will not kill your character, but it will affect the rate at which you lose energy. Running around on an empty stomach will result in passing out a lot.")
                    text _("{color=#cc0000}Energy{/color}: Running out of energy will cause your character to pass out for 12 hours. Choosing to sleep by using the 'Actions' button will save you a lot of time comparitavely. Passing out for 12 hours is extremely dangerous in most cases.")
                    text _("{color=#cc0000}Temperature{/color}: On the lower left of your status screen is an icon indicating your character's temperature. On Mason's path, you will have to make sure not to freeze to death. Likewise, on Derek's path you'll have to make sure you don't pass out from the heat during the day. Keep an eye on your temperature and take actions to keep it in the middle (it will appear green when you're a comfortable temperature).")
                    text _("{color=#cc0000}Time{/color}: On the lower right of your status screen, you'll see a clock. You can use it to tell what time of day it is, and to keep track of when certain events happen- However, on Celia's path, your character will not be able to see the sky or find a clock to be able to tell the time.")

    use help_navigation
screen controls():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help
    use help_navigation

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0







transform status_swiper:
    on show:
        xpos 1550
        easein 0.2 xpos 1270
    on replace:
        xpos 1550
        pause 0.2
        easein 0.2 xpos 1270
    on hide:
        xpos 1270
        easeout 0.2 xpos 1550
    on replaced:
        xpos 1270
        easeout 0.2 xpos 1550
transform inventory_swiper:
    on show:
        xpos 1850
        easein 0.2 xpos 1340
    on replace:
        xpos 1850
        pause 0.2
        easein 0.2 xpos 1340
    on hide:
        xpos 1340
        easeout 0.2 xpos 1850
    on replaced:
        xpos 1340
        easeout 0.2 xpos 1850
transform map_swiper:
    on show:
        xpos 1850
        easein 0.2 xpos 1270
    on replace:
        xpos 1850
        pause 0.2
        easein 0.2 xpos 1270
    on hide:
        xpos 1270
        easeout 0.2 xpos 1850
    on replaced:
        xpos 1270
        easeout 0.2 xpos 1850
transform actions_swiper:
    on show:
        xpos 1850
        easein 0.2 xpos 1270
    on replace:
        xpos 1850
        pause 0.2
        easein 0.2 xpos 1270
    on hide:
        xpos 1270
        easeout 0.2 xpos 1850
    on replaced:
        xpos 1270
        easeout 0.2 xpos 1850
transform inventory_item_swiper:
    on show:
        alpha 0
        easein 0.1 alpha 1
    on replace:
        alpha 0
        pause 0.2
        easein 0.1 alpha 1
    on hide:
        alpha 1
        easeout 0.1 alpha 0
    on replaced:
        alpha 1
        easeout 0.1 alpha 0
screen actions_base():
    zorder 200
    frame at actions_swiper:
        background "images/actions_bg.png"
        xsize 570
        ysize 132
        xanchor 1.0
        yanchor 1.0
        xpos 1270
        ypos 510
        top_padding 45
        if renpy.variant("small"):
            top_padding 40
        hbox:
            spacing 10
            xalign 0.5
            transclude
    key "game_menu" action Hide("actions")
screen actions():
    modal False tag mini_screen
    use actions_base:
        if gamepath == "mason":
            if map_location == "House":
                if energy >= 18:
                    textbutton " Go to Sleep" action [Hide("actions"), Jump("event_mason_sleepfail")] style "lines_button"
                else:
                    textbutton " Go to Sleep" action [Hide("actions"), Jump("event_mason_cabin_sleep")] style "lines_button"
            else:
                if energy >= 18:
                    textbutton " Go to Sleep" action [Hide("actions"), Jump("event_mason_sleepfail")] style "lines_button"
                else:
                    textbutton " Go to Sleep" action [SetVariable("sleep",8), SetVariable("arrivedby","sleep"),  Hide("actions"), Jump("mason_turn_order")] style "lines_button"
            textbutton " Search Area" action [Hide("actions"), Jump("mason_search_subroutine")] style "lines_button"
            if fire > 0:
                textbutton " Put Out Fire" action [Hide("actions"), Jump("event_mason_put_out_fire")] style "lines_button"
            if map_location == "Tall Tree":
                textbutton " Climb the Tree" action [Hide("actions"), Jump("mason_talltree_climbtree")] style "lines_button"
        if gamepath == "celia":
            if energy >= 18:
                textbutton " Go to Sleep" action [Hide("actions"), Jump("event_celia_sleepfail")] style "lines_button"
            else:
                textbutton " Go to Sleep" action [SetVariable("sleep",8), SetVariable("arrivedby","sleep"),  Hide("actions"), Jump("celia_turn_order")] style "lines_button"
            textbutton " Search Area" action [Hide("actions"), Jump("celia_search_subroutine")] style "lines_button"
            if celia_bound == 1:
                textbutton " Struggle" action [Hide("actions"), Jump("celia_desk_struggle")] style "lines_button"
        if gamepath == "derek":
            if map_location == "Deep Desert":
                textbutton " Panic" action [Hide("actions"), Function(renpy.call, label="event_derek_panic")] style "lines_button_glitch"
            else:
                if energy >= 18:
                    textbutton " Go to Sleep" action [Hide("actions"), Jump("event_derek_sleepfail")] style "lines_button"
                else:
                    textbutton " Go to Sleep" action [SetVariable("sleep",8), SetVariable("arrivedby","sleep"),  Hide("actions"), Jump("derek_turn_order")] style "lines_button"
                textbutton " Search Area" action [Hide("actions"), Jump("derek_search_subroutine")] style "lines_button"
screen fakeactions():
    modal False tag mini_screen
    use actions_base:
        textbutton " The beast will tear your flesh from your body" action [Hide("fakeactions"), SetVariable("event_mason_sanity_2","1")] style "lines_button"
screen status():
    modal False
    zorder 200 tag mini_screen
    frame at status_swiper:
        background "images/status_bg.png"
        xsize 235
        ysize 466
        xanchor 1.0
        yanchor 1.0
        xpos 1270
        ypos 492
        top_padding 0
        left_padding 45
        has vbox
        vbox:
            spacing 5
            xsize 235
            use wound_indicator
            null ysize 10
            use health_bar
            use sanity_bar
            use stomach_bar
            use energy_bar
            hbox:
                yoffset -115
                spacing 25
                use temp_bar
                null
                vbox:
                    null height 10
                    use time_bar
    key "game_menu" action Hide("status")
style status_text:
    xalign 1.0
    yoffset -10
    size 20
    font "images/libel-suit.regular.ttf"
    color "fff"
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]
screen health_bar():
    vbox:
        hbox:
            spacing 5
            xoffset -25
            add "images/status_icons_health.png"
            bar value AnimatedValue(health, range=100.0):
                ypos 7
                xsize 173
                ysize 18
                if health <= 25:
                    left_bar Frame("images/status_bar_danger.png", 10, 0)
                elif health <= 50:
                    left_bar Frame("images/status_bar_half.png", 10, 0)
                else:
                    left_bar Frame("images/status_bar_full.png", 10, 0)
                right_bar Frame("images/status_bar_empty.png", 10, 0)
                thumb None
                bar_vertical False
        text "Health" style "status_text":
            ypos 5
        text "[health]/100" style "status_text":
            xanchor 1.0
            xpos 182
            ypos -25
screen sanity_bar():
    vbox:
        yoffset -30
        hbox:
            spacing 5
            xoffset -25
            add "images/status_icons_sanity.png"
            bar value AnimatedValue(sanity, range=100.0):
                ypos 7
                xsize 173
                ysize 18
                if sanity <= 25:
                    left_bar Frame("images/status_bar_danger.png", 10, 0)
                elif sanity <= 50:
                    left_bar Frame("images/status_bar_half.png", 10, 0)
                else:
                    left_bar Frame("images/status_bar_full.png", 10, 0)
                right_bar Frame("images/status_bar_empty.png", 10, 0)
                thumb None
                bar_vertical False
        text "Sanity" style "status_text":
            ypos 5
        text "[sanity]/100" style "status_text":
            xanchor 1.0
            xpos 182
            ypos -25
screen stomach_bar():
    vbox:
        yoffset -60
        hbox:
            spacing 5
            xoffset -25
            add "images/status_icons_stomach.png"
            bar value AnimatedValue(food, range=24.0):
                ypos 7
                xsize 173
                ysize 18
                if food <= 6:
                    left_bar Frame("images/status_bar_danger.png", 10, 0)
                elif food <= 12:
                    left_bar Frame("images/status_bar_half.png", 10, 0)
                else:
                    left_bar Frame("images/status_bar_full.png", 10, 0)
                right_bar Frame("images/status_bar_empty.png", 10, 0)
                thumb None
                bar_vertical False
        text "Food" style "status_text":
            ypos 5
        text "[food]/24" style "status_text":
            xanchor 1.0
            xpos 182
            ypos -25
screen energy_bar():
    vbox:
        yoffset -90
        hbox:
            spacing 5
            xoffset -25
            add "images/status_icons_energy.png"
            bar value AnimatedValue(energy, range=24.0):
                ypos 7
                xsize 173
                ysize 18
                if energy <= 6:
                    left_bar Frame("images/status_bar_danger.png", 10, 0)
                elif energy <= 12:
                    left_bar Frame("images/status_bar_half.png", 10, 0)
                else:
                    left_bar Frame("images/status_bar_full.png", 10, 0)
                right_bar Frame("images/status_bar_empty.png", 10, 0)
                thumb None
                bar_vertical False
        text "Energy" style "status_text":
            ypos 5
        text "[energy]/24" style "status_text":
            xanchor 1.0
            xpos 182
            ypos -25
screen temp_bar():
    bar value AnimatedValue(temp, range=100.0):
        xsize 37
        ysize 120
        left_bar Frame("images/status_temp_empty.png", 10, 0)
        right_bar Frame(ConditionSwitch("temp >= 80","images/status_temp_red.png","temp >= 60","images/status_temp_orange.png","temp <= 20","images/status_temp_blue.png","temp <= 40","images/status_temp_cyan.png","temp <= 59","images/status_temp_green.png",), 10, 0)
        thumb None
        bar_vertical True
        xoffset 10
screen wound_indicator():
    hbox:
        spacing 3
        yoffset -4
        xoffset -15
        if wound == 1:
            frame:
                xpadding 0
                xmargin 0
                left_padding 23
                right_padding 0
                ymargin 0
                ypadding 1
                ysize 26
                background Frame("images/status_wound_bg.png",23,23,23,23)
                text "Wounded" style "wound_text"
        elif wound == 2:
            frame:
                xpadding 0
                xmargin 0
                left_padding 23
                right_padding 0
                ymargin 0
                ypadding 1
                ysize 26
                background Frame("images/status_wound_bg.png",23,23,23,23)
                text "Gravely Wounded" style "wound_text"
        else:
            frame:
                xpadding 0
                xmargin 0
                left_padding 23
                right_padding 0
                ymargin 0
                ypadding 1
                ysize 26
                background None
                text " " style "wound_text"
        if encumbered == 1:
            frame:
                xpadding 0
                xmargin 0
                left_padding 23
                right_padding 0
                ymargin 0
                ypadding 1
                ysize 26
                background Frame("images/status_encumbered_bg.png",23,23,23,23)
                text "Encumbered" style "wound_text"
        else:
            frame:
                xpadding 0
                xmargin 0
                left_padding 23
                right_padding 0
                ymargin 0
                ypadding 1
                ysize 26
                background None
                text " " style "wound_text"
image time_under = ConditionSwitch(
    "gamepath == 'celia'", "images/status_time_under_static.png",
    "gamepath == 'fox'", "images/status_time_under_static.png",
    "gamepath == 'mason'", "images/status_time_under.png",
    "gamepath == 'derek'", "images/status_time_under.png",)
screen time_bar():
    add "time_under" xanchor 0.5 yanchor 0.5 xpos 45 ypos 45 rotate hour_rotation
    add "images/status_time_over.png" xanchor 0.5 yanchor 0.5 xpos 45 yoffset -98
    if gamepath == "celia" or gamepath == "fox":
        text "--:--" style "status_text" xoffset 26 yoffset -190
    else:
        text "[hours]:00" style "status_text" xoffset 26 yoffset -190
screen status_update_health(amount):
    zorder 100
    hbox at status_update_animation:
        if amount > 0:
            text "+[amount]" style "status_text":
                yoffset 10
                xoffset 10
        else:
            text "[amount]" style "status_text":
                yoffset 10
                xoffset 10
        add "images/status_update_bg.png":
            xoffset 15
        add "images/status_icons_health.png":
            xoffset -32
            yoffset 5
        xsize 100
        ysize 43
        xalign 1.0
        ypos 60
    timer 2 action Hide('status_update_health') repeat True
screen status_update_sanity(amount):
    zorder 100
    hbox at status_update_animation:
        if amount > 0:
            text "+[amount]" style "status_text":
                yoffset 10
                xoffset 10
        else:
            text "[amount]" style "status_text":
                yoffset 10
                xoffset 10
        add "images/status_update_bg.png":
            xoffset 15
        add "images/status_icons_sanity.png":
            xoffset -32
            yoffset 5
        xsize 100
        ysize 43
        xalign 1.0
        ypos 140
    timer 2 action Hide('status_update_sanity') repeat True
screen status_update_food(amount):
    zorder 100
    hbox at status_update_animation:
        if amount > 0:
            text "+[amount]" style "status_text":
                yoffset 10
                xoffset 10
        else:
            text "[amount]" style "status_text":
                yoffset 10
                xoffset 10
        add "images/status_update_bg.png":
            xoffset 15
        add "images/status_icons_stomach.png":
            xoffset -32
            yoffset 5
        xsize 100
        ysize 43
        xalign 1.0
        ypos 220
    timer 2 action Hide('status_update_food') repeat True
screen status_update_energy(amount):
    zorder 100
    hbox at status_update_animation:
        if amount > 0:
            text "+[amount]" style "status_text":
                yoffset 10
                xoffset 10
        else:
            text "[amount]" style "status_text":
                yoffset 10
                xoffset 10
        add "images/status_update_bg.png":
            xoffset 15
        add "images/status_icons_energy.png":
            xoffset -32
            yoffset 5
        xsize 100
        ysize 43
        xalign 1.0
        ypos 300
    timer 2 action Hide('status_update_energy') repeat True
screen status_update_temp_increase(amount):
    zorder 100
    hbox at status_update_animation:
        text "+" style "status_text":
            yoffset 10
            xoffset 10
        add "images/status_update_bg.png":
            xoffset 15
        add "images/status_icons_heat.png":
            xoffset -32
            yoffset 5
        xsize 100
        ysize 43
        xalign 1.0
        xoffset 5
        ypos 380
    timer 2 action Hide('status_update_temp_increase') repeat True
screen status_update_temp_decrease(amount):
    zorder 100
    hbox at status_update_animation:
        text "-" style "status_text":
            yoffset 10
            xoffset 10
        add "images/status_update_bg.png":
            xoffset 15
        add "images/status_icons_cold.png":
            xoffset -32
            yoffset 5
        xsize 100
        ysize 43
        xalign 1.0
        xoffset 5
        ypos 380
    timer 2 action Hide('status_update_temp_decrease') repeat True

transform status_update_animation:
    xalign 0.96
    zoom 1.0
    anchor (0.5,0.5)
    on show:
        alpha 0
        easein 0.25 alpha 1.0 zoom 1.2
        easein 0.1 zoom 1.0
    on hide:
        linear 0.5 alpha 0.0

screen inventory_base():
    zorder 200

    frame at inventory_swiper:
        background "images/inventory_background.png"
        xsize 406
        ysize 511
        xanchor 1.0
        yanchor 1.0
        xpos 1340
        ypos 515
        top_padding 22
        left_padding 20
        has vpgrid:
            cols 3
            spacing 5
            allow_underfull True
        transclude

    key "game_menu" action Hide("inventory")

screen inventory():
    modal False tag mini_screen

    use inventory_base:
        for x in inventory:
            $ pic = "images/" + x + "_%s.png"
            imagebutton auto pic action [If(renpy.get_screen(x), Hide(x), ShowTransient(x)), Hide("inventory")]
screen fakeinventory():
    modal False tag mini_screen

    use inventory_base:
        imagebutton auto "images/item_noose_%s.png" action [If(renpy.get_screen("item_noose"), Hide("item_noose"), ShowTransient("item_noose")), Hide("fakeinventory")]
style status_text:
    xalign 0.0
    yoffset -15
    xoffset 10
    size 20
    font "images/libel-suit.regular.ttf"
    color "fff"
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]
style popup_text:
    size 40
    xfill True
style popup_description:
    size 16
    text_align 0.5
style popup_description:
    variant "small"
    size 25
style popup_title:
    variant "small"
    size 36
style wound_text:
    font "images/libel-suit.regular.ttf"
    color "fff"
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]
    xalign 0.5
    size 15
style lines_button:
    background Frame("images/lines_bg.png",1,1)
    hover_background Frame("images/lines_bg_hover.png",1,1)
    insensitive_background Frame("images/lines_bg_insensitive.png",1,1)
    xminimum 100
style lines_button:
    variant "small"
    ysize 50
    xpadding 6
style lines_button_red is lines_button:
    background Frame("images/lines_bg_red.png",1,1)
    hover_background Frame("images/lines_bg_red_hover.png",1,1)
style timer_button:
    background None
    hover_background None
    xminimum 500
style lines_button_glitch is lines_button:

    background Animation("images/button_glitch_1.jpg", .05, "images/button_glitch_4.jpg", .05, "images/button_glitch_2.jpg", .05, "images/button_glitch_3.jpg", .05, "images/button_glitch_4.jpg", .05)
    hover_background Frame("images/lines_bg_hover.png",1,1)
    xminimum 100
style lines_button_text:
    size 20
    font "images/libel-suit.regular.ttf"
    color "fff"
    hover_color "cc0000"
    insensitive_color "777"
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]
    xalign 0.5
style lines_button_text:
    variant "small"
    size 25
style lines_button_red_text is lines_button_text
style timer_button_text:
    size 20
    font "images/libel-suit.regular.ttf"
    color "fff"
    hover_color "cc0000"
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]
    xalign 0.5
style lines_button_glitch_text:
    size 20
    font "images/libel-suit.regular.ttf"
    color "cc0000"
    hover_color "cc0000"
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]
    xalign 0.5
style small_text:
    size 17
style red_text:
    color "cc0000"
style red_small_text:
    size 15
    color "cc0000"

screen item_base():
    frame at inventory_item_swiper:
        xsize 745
        ysize 263
        background "images/popup_background.png"
        xalign 0.5
        yalign 0.5
        xpadding 50
        has vbox:
            yalign 0.5
            xfill True
            spacing 10
        transclude

screen item_knife():
    modal True tag inventory_item

    use item_base:
        text "Pocket Knife" style "popup_title" xalign 0.5
        text "A small knife. It doesn't look like it would make a very good weapon." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put away" action Hide("item_knife") style "lines_button"
            if sanity <= 0:
                textbutton " End this" action Hide("item_knife"), Jump("event_mason_knife_suicide") style "lines_button_glitch"
            if wound == 2:
                textbutton " Make a Tourniquet" action Hide("item_knife"), Jump("event_mason_tourniquet") style "lines_button"
screen item_flint():
    modal True tag inventory_item

    use item_base:
        text "Flint and Steel" style "popup_title" xalign 0.5
        if fire == 0:
            text "I think I can start a fire with this." style "popup_description" xalign 0.5
        else:
            text "Thanks to this, I already have a pretty good fire going!" style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_flint") style "lines_button" xalign 0.5
            if fire == 0:
                if (map_location == "Meadow" or map_location == "Thicket" or map_location == "Tall Tree" or map_location == "Waterfall"):
                    textbutton " Make a Fire" action Hide("item_flint"), Jump("event_mason_buildfire") style "lines_button"
                if map_location == "House":
                    textbutton " Make a Fire" action Hide("item_flint"), Jump("event_mason_housefire") style "lines_button"
                if map_location == "Swamp":
                    textbutton " Make a Fire" action Hide("item_flint"), Jump("event_mason_swampfire") style "lines_button"
screen item_paper():
    modal True tag inventory_item

    use item_base:
        text "Paper and Pencil" style "popup_title" xalign 0.5
        text "Some paper and a small pencil. I can try and make a map and keep track of where I am..." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Draw my Location" action [Hide("item_paper"), Function(Use_Item_Paper)] style "lines_button"
            textbutton " Put Away" action Hide("item_paper") style "lines_button"
screen item_trail_mix():
    modal True tag inventory_item

    use item_base:
        text "Trail Mix" style "popup_title" xalign 0.5
        text "A bag of trail mix. I got it from Mason. I don't know if it's safe but it smells okay." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Eat" action [Hide("item_trail_mix"), Function(Use_Item_Trailmix)] style "lines_button"
            textbutton " Put Away" action Hide("item_trail_mix") style "lines_button"
screen item_map():
    modal True tag inventory_item

    use item_base:
        text "Map" style "popup_title" xalign 0.5
        if (map_location == "Meadow" and map_discovery_meadow == False) or (map_location == "Swamp" and map_discovery_swamp == False) or (map_location == "Tall Tree" and map_discovery_talltree == False) or (map_location == "Thicket" and map_discovery_thicket == False) or (map_location == "Waterfall" and map_discovery_waterfall == False) or (map_location == "House" and map_discovery_house == False):
            text "A map of my surroundings. I haven't added this place yet." style "popup_description" xalign 0.5
        else:
            text "A map of my surroundings. Filling this in might help me out." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            if (map_location == "Meadow" and map_discovery_meadow == False) or (map_location == "Swamp" and map_discovery_swamp == False) or (map_location == "Tall Tree" and map_discovery_talltree == False) or (map_location == "Thicket" and map_discovery_thicket == False) or (map_location == "Waterfall" and map_discovery_waterfall == False) or (map_location == "House" and map_discovery_house == False):
                textbutton " Draw my Location" action [Function(Use_Item_Map), Hide("item_map"), Notify("Location Drawn!")] style "lines_button"
            textbutton " Put Away" action Hide("item_map") style "lines_button"
screen item_bones():
    modal True tag inventory_item

    use item_base:
        text "Bones" style "popup_title" xalign 0.5
        text "A couple of bones I found in the meadow... I think they belonged to a deer." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_bones") style "lines_button"
            if map_location == "Swamp":
                textbutton " Offer" action [Function(Use_Item_Bones), Hide("item_bones"), Jump("event_mason_offerbones")] style "lines_button"
screen item_saskatoons():
    modal True tag inventory_item

    use item_base:
        text "Blue Berries" style "popup_title" xalign 0.5
        text "A pile of blueish purple berries. They seem safe..." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Eat" action [Hide("item_saskatoons"), Function(Use_Item_Saskatoons)] style "lines_button"
            textbutton " Put Away" action Hide("item_saskatoons") style "lines_button"
screen item_baneberries():
    modal True tag inventory_item

    use item_base:
        text "Red Berries" style "popup_title" xalign 0.5
        text "A pile of red berries. They seem safe..." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Eat" action [Function(Use_Item_Baneberries), Hide("item_baneberries"), Jump("event_mason_baneberry_freakout")] style "lines_button"
            textbutton " Put Away" action Hide("item_baneberries") style "lines_button"
screen item_fish():
    modal True tag inventory_item

    use item_base:
        text "Fish" style "popup_title" xalign 0.5
        text "A fish I managed to catch in the river." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Eat" action [Hide("item_fish"), Function(Use_Item_Fish)] style "lines_button"
            if fire > 0:
                textbutton " Cook" action [Hide("item_fish"), Jump("event_mason_fish_cook")] style "lines_button"
            textbutton " Put Away" action Hide("item_fish") style "lines_button"
screen item_cookedfish():
    modal True tag inventory_item

    use item_base:
        text "Fish" style "popup_title" xalign 0.5
        text "A fish I caught and cooked. It looks and smells delicious!" style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Eat" action [Hide("item_cookedfish"), Function(Use_Item_Cookedfish)] style "lines_button"
            textbutton " Put Away" action Hide("item_cookedfish") style "lines_button"
screen item_fish_cute():
    modal True tag inventory_item

    use item_base:
        text "Fish" style "popup_title" xalign 0.5
        text "A fish I managed to catch in the river. It almost looks like it's begging me not to eat it." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Eat" action [Hide("item_fish_cute"), Function(Use_Item_Fish)] style "lines_button"
            if fire > 0:
                textbutton " Cook" action [Hide("item_fish_cute"), Jump("event_mason_fish_cook")] style "lines_button"
            textbutton " Put Away" action Hide("item_fish_cute") style "lines_button"
screen item_cookedfish_cute():
    modal True tag inventory_item

    use item_base:
        text "Fish" style "popup_title" xalign 0.5
        text "A fish I caught and cooked. It looks and smells delicious!" style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Eat" action [Hide("item_cookedfish_cute"), Function(Use_Item_Cookedfish)] style "lines_button"
            textbutton " Put Away" action Hide("item_cookedfish_cute") style "lines_button"
screen item_beartrap():
    modal True tag inventory_item

    use item_base:
        text "Bear Trap" style "popup_title" xalign 0.5
        text "A heavy steel bear trap. It looks extremely dangerous." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Drop" action [Hide("item_beartrap"), Jump("event_mason_beartrap_drop")] style "lines_button"
            if map_location == "House" and map_location_cabin == "inside":
                textbutton " Set" action [Hide("item_beartrap"), Jump("event_mason_beartrap_set")] style "lines_button"
            else:
                textbutton " Set" action [Hide("item_beartrap"), Jump("event_mason_beartrap_failset")] style "lines_button"
            textbutton " Put Away" action Hide("item_beartrap") style "lines_button"
screen item_noose():
    modal True tag inventory_item

    use item_base:
        text "You're never leaving this mountain." style "popup_title" xalign 0.5
    timer 3.0 action [Hide("item_noose"), SetVariable("event_mason_sanity_1", "1")]
screen item_celia_map():
    modal True tag inventory_item

    use item_base:
        text "Map" style "popup_title" xalign 0.5
        text "A crusty old floorplan. I can use it to tell where I am down here." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_celia_map") style "lines_button"
screen item_office_key():
    modal True tag inventory_item

    use item_base:
        text "Office Key" style "popup_title" xalign 0.5
        text "A slightly rusty room key." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_office_key") style "lines_button"
            if map_location == "Room" and event_celia_room_key_attempt == 0:
                textbutton " Unlock Door" action [Hide("item_office_key"), Jump("event_celia_room_key_attempt")] style "lines_button"
            if map_location == "Lounge" and celia_office_locked == 1:
                textbutton " Unlock Door" action [Hide("item_office_key"), Jump("event_celia_unlock_office")] style "lines_button"
            if map_location == "Lounge" and celia_office_locked == 0:
                textbutton " Lock Door" action [Hide("item_office_key"), Jump("event_celia_lock_office")] style "lines_button"
screen item_basement_key():
    modal True tag inventory_item

    use item_base:
        text "Small Key" style "popup_title" xalign 0.5
        text "A small metal key." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_basement_key") style "lines_button"
            if map_location == "Office" and celia_basement_locked == 1 and event_celia_discover_basement == 1:
                textbutton " Unlock Door" action [Hide("item_basement_key"), Jump("event_celia_unlock_basement")] style "lines_button"
            if map_location == "Office" and celia_basement_locked == 0 and event_celia_discover_basement == 1:
                textbutton " Lock Door" action [Hide("item_basement_key"), Jump("event_celia_lock_basement")] style "lines_button"
screen item_taser():
    modal True tag inventory_item

    use item_base:
        text "Taser" style "popup_title" xalign 0.5
        text "A handheld taser. Unfortunately, without batteries, it isn't going to be any use." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_taser") style "lines_button"
screen item_battery_taser():
    modal True tag inventory_item

    use item_base:
        text "Taser" style "popup_title" xalign 0.5
        text "A handheld taser. Now fully charged and ready to use!" style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_battery_taser") style "lines_button"
screen item_wire():
    modal True tag inventory_item

    use item_base:
        text "Wire" style "popup_title" xalign 0.5
        text "Some strong, sharp wire." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_wire") style "lines_button"
            if map_location == "Room" and event_celia_set_trap == 0:
                textbutton " Set Trap" action [Hide("item_wire"), Jump("event_celia_set_trap")] style "lines_button"
screen item_pin():
    modal True tag inventory_item

    use item_base:
        text "Pin" style "popup_title" xalign 0.5
        text "Half of a hair pin. I can use it to open the door." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_pin") style "lines_button"
            if map_location == "Room" and event_celia_room_door_locked == 1:
                textbutton " Unlock Door" action [Hide("item_pin"), Jump("event_celia_unlock_room")] style "lines_button"
screen item_shackles():
    modal True tag inventory_item

    use item_base:
        text "Handcuffs" style "popup_title" xalign 0.5
        if celia_bound == 1:
            text "Shackles with a long chain connected to the desk. I can't get them off my wrists." style "popup_description" xalign 0.5
        else:
            text "Cuffs with long chains attached to my wrists. I can't get them off." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Okay" action Hide("item_shackles") style "lines_button"
screen item_soda():
    modal True tag inventory_item

    use item_base:
        text "Ginger Ale" style "popup_title" xalign 0.5
        text "A can of diet soda." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Drink" action [Hide("item_soda"), Jump("event_celia_drink_soda")] style "lines_button"
            textbutton " Put Away" action Hide("item_soda") style "lines_button"
screen item_rat_poison():
    modal True tag inventory_item

    use item_base:
        text "Rat Poison" style "popup_title" xalign 0.5
        text "A small packet of powder. It claims to kill rats very effectively." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_rat_poison") style "lines_button"
screen item_note():
    modal True tag inventory_item

    use item_base:
        text "Bloody Note" style "popup_title" xalign 0.5
        text "A note scrawled in blood. It says '0247'." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_note") style "lines_button"
screen item_canteen_full():
    modal True tag inventory_item

    use item_base:
        text "Canteen" style "popup_title" xalign 0.5
        if meme_mode:
            text "A canteen dropped by Derek... It's full of warm milk." style "popup_description" xalign 0.5
        else:
            text "A canteen dropped by Derek... It's full of water." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Drink" action [Hide("item_canteen_full"), Jump("event_derek_drink_water")] style "lines_button"
            textbutton " Put Away" action Hide("item_canteen_full") style "lines_button"
screen item_canteen_empty():
    modal True tag inventory_item

    use item_base:
        text "Canteen" style "popup_title" xalign 0.5
        text "A completely empty canteen." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_canteen_empty") style "lines_button"
screen item_canteen_poison():
    modal True tag inventory_item

    use item_base:
        text "Canteen" style "popup_title" xalign 0.5
        text "A canteen that you refilled with water from the fissure." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Drink" action [Hide("item_canteen_poison"), Jump("event_derek_drink_poison")] style "lines_button"
            textbutton " Put Away" action Hide("item_canteen_poison") style "lines_button"
            if map_location == "Camp":
                textbutton " Plant" action [Hide("item_canteen_poison"), Jump("event_derek_plant_poison")] style "lines_button"
screen item_sacrificial_knife():
    modal True tag inventory_item

    use item_base:
        text "Sacrificial Knife" style "popup_title" xalign 0.5
        text "An ornamental knife taken from Komodo and Dragon. It's still very sharp." style "popup_description" xalign 0.5
        null height 15
        hbox:
            xalign 0.5
            textbutton " Put Away" action Hide("item_sacrificial_knife") style "lines_button"

init python:
    def Use_Item_Trailmix():
        renpy.jump("event_mason_eat_trailmix")
        return
    def Use_Item_Saskatoons():
        renpy.jump("event_mason_eat_saskatoons")
        return
    def Use_Item_Fish():
        renpy.jump("event_mason_eat_fish")
        return
    def Use_Item_Cookedfish():
        renpy.jump("event_mason_eat_cookedfish")
        return
    def Use_Item_Baneberries():
        inventory.remove("item_baneberries")
        return
    def Use_Item_Bones():
        inventory.remove("item_bones")
        return
    def Use_Item_Paper():
        global map_discovery_meadow
        global map_discovery_thicket
        global map_discovery_waterfall
        global map_discovery_talltree
        global map_discovery_house
        global map_discovery_swamp
        global map_location
        if map_location == "Meadow":
            map_discovery_meadow = True
        elif map_location == "Thicket":
            map_discovery_thicket = True
        elif map_location == "Tall Tree":
            map_discovery_talltree = True
        elif map_location == "Waterfall":
            map_discovery_waterfall = True
        elif map_location == "House":
            map_discovery_house = True
        elif map_location == "Swamp":
            map_discovery_swamp = True
        inventory.remove("item_paper")
        inventory.append("item_map")
        renpy.jump("event_mason_drawmap")
        return
    def Use_Item_Map():
        global map_discovery_meadow
        global map_discovery_thicket
        global map_discovery_waterfall
        global map_discovery_talltree
        global map_discovery_house
        global map_discovery_swamp
        global map_location
        if map_location == "Meadow":
            map_discovery_meadow = True
        elif map_location == "Thicket":
            map_discovery_thicket = True
        elif map_location == "Tall Tree":
            map_discovery_talltree = True
        elif map_location == "Waterfall":
            map_discovery_waterfall = True
        elif map_location == "House":
            map_discovery_house = True
        elif map_location == "Swamp":
            map_discovery_swamp = True
        return

screen map_mason():


    modal False


    zorder 200 tag mini_screen
    frame at map_swiper:
        background "images/mason_map_base.png"
        xsize 520
        ysize 355
        xanchor 1.0
        yanchor 1.0
        xpos 1276
        ypos 510
        if map_discovery_house == True:
            add "images/mason_map_house.png":
                xpos 95
                ypos 168
        if map_discovery_meadow == True:
            add "images/mason_map_meadow.png":
                xpos 140
                ypos 235
        if map_discovery_thicket == True:
            add "images/mason_map_thicket.png":
                xpos 358
                ypos 202
        if map_discovery_talltree == True:
            add "images/mason_map_talltree.png":
                xpos 463
                ypos 169
        if map_discovery_waterfall == True:
            add "images/mason_map_waterfall.png":
                xpos 25
                ypos 180
        if map_discovery_swamp == True:
            add "images/mason_map_swamp.png":
                xpos 270
                ypos 174
        if (map_location == "Meadow" and map_discovery_meadow == True) or (map_location == "Swamp" and map_discovery_swamp == True) or (map_location == "Tall Tree" and map_discovery_talltree == True) or (map_location == "Thicket" and map_discovery_thicket == True) or (map_location == "Waterfall" and map_discovery_waterfall == True) or (map_location == "House" and map_discovery_house == True):
            add "map_pointer":
                if map_location == "House":
                    xpos 185
                    ypos 140
                if map_location == "Waterfall":
                    xpos 65
                    ypos 200
                if map_location == "Meadow":
                    xpos 240
                    ypos 235
                if map_location == "Thicket":
                    xpos 400
                    ypos 190
                if map_location == "Tall Tree":
                    xpos 470
                    ypos 155
                if map_location == "Swamp":
                    xpos 325
                    ypos 155
        if map_discovery_swamp == True and map_location != "Swamp" and sanity > 40 and event_mason_sanity_3 == 0:
            timer 6.0 action SetVariable("event_mason_sanity_3","1")
            add "mapscare":
                xpos 67
                ypos 168


    key "game_menu" action Hide("map_mason")

screen map_celia():


    modal False


    zorder 200 tag mini_screen
    frame at map_swiper:
        background "images/celia_map_base.png"
        xsize 520
        ysize 355
        xanchor 1.0
        yanchor 1.0
        xpos 1276
        ypos 510
        if map_location == "Room":
            add "images/celia_map_room.png":
                xpos 238
                ypos 225
        if map_location == "Lounge":
            add "images/celia_map_lounge.png":
                xpos 199
                ypos 118
        if map_location == "Elevator":
            add "images/celia_map_elevator.png":
                xpos 150
                ypos 177
        if map_location == "Office":
            add "images/celia_map_office.png":
                xpos 352
                ypos 45
        if map_location == "Basement":
            add "images/celia_map_basement.png":
                xpos 316
                ypos 55
        if map_location == "Break Room":
            add "images/celia_map_breakroom.png":
                xpos 152
                ypos 42
        add "images/celia_map_room_label.png":
            xpos 248
            ypos 245
        if event_celia_enter_lounge == 1:
            add "images/celia_map_lounge_label.png":
                xpos 367
                ypos 160
        if event_celia_try_elevator == 1:
            add "images/celia_map_elevator_label.png":
                xpos 153
                ypos 182
        if event_celia_enter_office == 1:
            add "images/celia_map_office_label.png":
                xpos 370
                ypos 65
        if event_celia_enter_basement == 1:
            add "images/celia_map_basement_label.png":
                xpos 319
                ypos 62
        if event_celia_enter_breakroom == 1:
            add "images/celia_map_breakroom_label.png":
                xpos 180
                ypos 85
        if event_celia_try_office == 1:
            if celia_office_locked == 1:
                add "images/celia_map_locked.png":
                    xpos 397
                    ypos 107
            else:
                add "images/celia_map_unlocked.png":
                    xpos 397
                    ypos 107
        if event_celia_discover_basement == 1:
            if celia_basement_locked == 1:
                add "images/celia_map_locked.png":
                    xpos 337
                    ypos 66
            else:
                add "images/celia_map_unlocked.png":
                    xpos 337
                    ypos 66
        if map_location == "Room":
            add "map_pointer":
                xpos 265
                ypos 238
        if map_location == "Lounge":
            add "map_pointer":
                xpos 393
                ypos 145
        if map_location == "Elevator":
            add "map_pointer":
                xpos 160
                ypos 160
        if map_location == "Office":
            add "map_pointer":
                xpos 395
                ypos 40
        if map_location == "Basement":
            add "map_pointer":
                xpos 320
                ypos 100
        if map_location == "Break Room":
            add "map_pointer":
                xpos 220
                ypos 70



    key "game_menu" action Hide("map_celia")

screen map_derek():


    modal False


    zorder 200 tag mini_screen
    if map_location == "Deep Desert":
        frame at map_swiper:
            background "images/derek_map_sand.png"
            xsize 520
            ysize 355
            xanchor 1.0
            yanchor 1.0
            xpos 1276
            ypos 510
            add "mapsand":
                xpos 10
                ypos 9
            add "map_pointer_glitch":
                ypos 155
                xpos 250
    else:
        frame at map_swiper:
            background "images/derek_map_base.png"
            xsize 520
            ysize 355
            xanchor 1.0
            yanchor 1.0
            xpos 1276
            ypos 510
            if map_location == "Camp":
                add "images/derek_map_camp.png":
                    xpos 38
                    ypos 266
                add "map_pointer":
                    xpos 140
                    ypos 250
            if map_location == "Desert":
                add "images/derek_map_desert.png":
                    xpos 182
                    ypos 168
                add "map_pointer":
                    xpos 360
                    ypos 250
            if map_location == "Hill":
                add "images/derek_map_hill.png":
                    xpos 10
                    ypos 10
                add "map_pointer":
                    xpos 100
                    ypos 60
            if map_location == "Fissure":
                add "images/derek_map_fissure.png":
                    xpos 288
                    ypos 10
                add "map_pointer":
                    xpos 395
                    ypos 40
            if event_derek_cave_discovery != 0:
                if map_location == "Cave":
                    add "images/derek_map_cave2.png":
                        xpos 30
                        ypos 100
                    add "map_pointer":
                        xpos 40
                        ypos 80
                else:
                    add "images/derek_map_cave.png":
                        xpos 30
                        ypos 100


    key "game_menu" action Hide("map_derek")


transform timerbutton_transform:
    xalign 0.5
    yalign 0.37
    yoffset 0
    xoffset 0
    zoom 1.0
    alpha 0
    easein 0.1 zoom 1.2 alpha 1
    easein 0.1 zoom 1.0
screen timer_button():
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('timer_button'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.366 xmaximum 500 ymaximum 43 left_bar Frame("timebar_empty.jpg", 10, 0) right_bar Frame("timebar_full.jpg", 10, 0) thumb None bar_vertical False at timerbutton_transform
    textbutton timer_button_text action Jump(timer_button_jump) style "timer_button" at timerbutton_transform



transform splatter_1:
    anchor (0,1)
    xalign 0.0
    yalign 1.0
    zoom 1.05
    alpha 0
    pause 0.2
    easein 0.03 zoom 1.0 alpha 1
transform splatter_2:
    anchor (1,0)
    xalign 1.0
    yalign 0.0
    zoom 1.05
    alpha 0
    pause 0.4
    easein 0.03 zoom 1.0 alpha 1
transform death_text_intro:
    xalign 0.5
    yalign 0.5
    zoom 1.3
    alpha 0
    ypos 250
    pause 0.6
    easein 0.1 zoom 1.0 alpha 1
transform death_text_fade:
    xalign 0.5
    yalign 0.5
    zoom 1.3
    alpha 0
    pause 0.6
    easein 0.1 zoom 1.0 alpha 1
transform death_text_fade_change:
    xalign 0.5
    yalign 0.5
    zoom 1.3
    alpha 0
    pause 0.6
    easein 1.0 zoom 1.0 alpha 1
transform deathbutton_1:
    xalign 0.5
    yalign 0.5
    yoffset 80
    xoffset -120
    zoom 1.3
    alpha 0
    pause 0.6
    easein 0.3 zoom 1.0 alpha 1
transform deathbutton_2:
    xalign 0.5
    yalign 0.5
    yoffset 80
    xoffset 0
    zoom 1.3
    alpha 0
    pause 0.7
    easein 0.3 zoom 1.0 alpha 1
transform deathbutton_3:
    xalign 0.5
    yalign 0.5
    yoffset 80
    xoffset 120
    zoom 1.3
    alpha 0
    pause 0.8
    easein 0.3 zoom 1.0 alpha 1
transform deathbutton_4:
    xalign 0.5
    yalign 0.5
    yoffset 200
    xoffset -60
    zoom 1.3
    alpha 0
    pause 0.7
    easein 0.3 zoom 1.0 alpha 1
transform deathbutton_5:
    xalign 0.5
    yalign 0.5
    yoffset 200
    xoffset 60
    zoom 1.3
    alpha 0
    pause 0.8
    easein 0.3 zoom 1.0 alpha 1
transform deathbutton_6:
    xalign 0.5
    yalign 0.5
    yoffset 200
    xoffset -90
    zoom 1.3
    alpha 0
    pause 0.7
    easein 0.3 zoom 1.0 alpha 1
transform deathbutton_7:
    xalign 0.5
    yalign 0.5
    yoffset 200
    xoffset 90
    zoom 1.3
    alpha 0
    pause 0.8
    easein 0.3 zoom 1.0 alpha 1
screen disableclick(time):
    timer time action Hide("disableclick")
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "K_SELECT" action NullAction()
screen bg_splash():
    add "images/bloodsplatter_1.png" at splatter_1
    add "images/bloodsplatter_2.png" at splatter_2
    text "THIS GAME IS {size=150}{font=images/expressway-free.regular.ttf}18+{/font}{/size}" style "endslate_title" outlines [(2, "000000", 0, 0)] at truecenter, death_text_intro
    text "This game includes many triggering themes ranging from\nmurder, gore, and suicide to sexual assault.\n\n{size=30}It is NOT for minors.{/size}\n\nIf you are under 18 and someone is showing you this game, get away from that person.\nFor more information about triggers, please visit the Warnings page." style "endslate_subtitle" outlines [(2, "000000", 0, 0)] at truecenter, death_text_fade
    if renpy.variant("small"):
        textbutton " I Understand" action Jump("keepgoing") style "lines_button" at deathbutton_6
        textbutton " Warnings" action ShowMenu("warnings") style "lines_button" at deathbutton_7
    else:
        textbutton " I Understand" action Jump("keepgoing") style "lines_button" at deathbutton_4
        textbutton " Warnings" action ShowMenu("warnings") style "lines_button" at deathbutton_5
screen bg_endslate_text(main, sub):
    $ sillydeath = renpy.random.choice(['F', 'WASTED', 'You Ded', 'OOPS', 'Oof', 'Yikes', 'Riperoni','RIP in Pieces', 'You Died uwu', 'Nice Job, Dingus', 'You Nailed It'])
    modal True
    zorder 200
    add "images/bloodsplatter_1.png" at splatter_1
    add "images/bloodsplatter_2.png" at splatter_2
    if meme_mode and main == "You Died":
        text sillydeath style "endslate_title" outlines [(2, "000000", 0, 0)] at truecenter, death_text_fade
    else:
        text main style "endslate_title" outlines [(2, "000000", 0, 0)] at truecenter, death_text_fade
    text sub style "endslate_subtitle" outlines [(2, "000000", 0, 0)] at truecenter, death_text_fade
    textbutton " Load" action [ShowMenu("load"), Stop("music")] style "lines_button" at deathbutton_1
    textbutton " Start Over" action [MainMenu(confirm=False), Stop("music")] style "lines_button" at deathbutton_2
    textbutton " Credits" action [ShowMenu("credits"), Stop("music")] style "lines_button" at deathbutton_3
screen bg_endslate_survival_text(main, sub):
    modal True
    zorder 200
    text main style "endslate_title_surv" outlines [(2, "000000", 0, 0)] at truecenter, death_text_fade
    text sub style "endslate_subtitle_surv" outlines [(2, "000000", 0, 0)] at truecenter, death_text_fade
    textbutton " Load" action [ShowMenu("load"), Stop("music")] style "lines_button" at deathbutton_1
    textbutton " Start Over" action [MainMenu(confirm=False), Stop("music")] style "lines_button" at deathbutton_2
    textbutton " Credits" action [ShowMenu("credits"), Stop("music")] style "lines_button" at deathbutton_3
screen bg_endslate_survival_text_white(main, sub):
    modal True
    zorder 200
    text main style "endslate_title" outlines [(2, "000000", 0, 0)] at truecenter, death_text_fade
    text sub style "endslate_subtitle" outlines [(2, "000000", 0, 0)] at truecenter, death_text_fade
    textbutton " Load" action [ShowMenu("load"), Stop("music")] style "lines_button" at deathbutton_1
    textbutton " Start Over" action [MainMenu(confirm=False), Stop("music")] style "lines_button" at deathbutton_2
    textbutton " Credits" action [ShowMenu("credits"), Stop("music")] style "lines_button" at deathbutton_3
screen bg_endslate_change_text(main, sub):
    modal True
    zorder 200
    text main style "endslate_title" outlines [(2, "000000", 0, 0)] at truecenter, death_text_fade_change
    text sub style "endslate_subtitle" outlines [(2, "000000", 0, 0)] at truecenter, death_text_fade
    textbutton " Load" action [ShowMenu("load"), Stop("music")] style "lines_button" at deathbutton_1
    textbutton " Start Over" action [MainMenu(confirm=False), Stop("music")] style "lines_button" at deathbutton_2
    textbutton " Credits" action [ShowMenu("credits"), Stop("music")] style "lines_button" at deathbutton_3








screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action style "lines_button"
            textbutton _("No") action no_action style "lines_button"


    key "game_menu" action no_action

screen showconfirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _(" I understand") action yes_action style "lines_button"
            textbutton _(" Warnings") action no_action style "lines_button"


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 6

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        xoffset -250
        easein .25 alpha 1.0 xoffset 0
        easein .05 xoffset -5
    on hide:
        easein .05 xoffset 0
        easeout .25 xoffset -400


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
    yminimum 43

style notify_text:
    properties gui.text_properties("notify")
    yalign 0.5



transform numpad_input_show:
    on show:
        alpha 0
        linear 1.0 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.25 alpha 0.0

screen numpad_input(prompt):
    modal True
    frame at numpad_input_show:
        style "numpad_input_frame"
        add "gui/overlay/confirm.png"
        if renpy.variant("small"):
            add "numpad_bg_small"
        else:
            add "numpad_bg"
        window:
            style "nvl_window"
            if renpy.variant("small"):
                input id "input" xalign 0.5 yalign 0.2 color "#ffffff" style "numpad_input_style"
            else:
                input id "input" xalign 0.5 yalign 0.5 color "#ffffff" style "numpad_input_style"


style numpad_input_frame is empty
style numpad_input_frame:
    background None
style numpad_input_style:
    size 40
    caret None







screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background None
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



screen showDLC_vote():


    modal False

    zorder 200 tag mini_screen
    frame at numpad_input_show:
        style "poll_frame"
        add "images/bar_votebg.png"
        xpos 25
        ypos 25
        bar value AnimatedValue(show_votepos, range=10.0, delay=0.5):
            xsize 370
            ysize 5
            left_bar "images/bar_vote_green.png"
            right_bar "#333333"
            thumb None
            xpos 25
            ypos 25
        bar value AnimatedValue(show_voteneg, range=10.0, delay=0.5):
            xsize 370
            ysize 5
            left_bar "images/bar_vote_red.png"
            right_bar "#333333"
            thumb None
            xpos 25
            ypos 40
    if meme_mode:
        add "images/bar_vote_green_label_meme.png":
            xpos 190
            ypos 7
    else:
        add "images/bar_vote_green_label.png":
            xpos 215
            ypos 11
    if meme_mode:
        add "images/bar_vote_red_label_meme.png":
            xpos 190
            ypos 80
    else:
        add "images/bar_vote_red_label.png":
            xpos 220
            ypos 82
style poll_frame is empty
style poll_frame:
    background None



































style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
