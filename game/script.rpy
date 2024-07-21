




define p = DynamicCharacter("player_name",color="FFF")
define unknown = Character ("???",color="FFF")
define announcer = Character ("Cheerful Voice",color="FFF",image="announcer",what_xpos=350,what_xsize=550,who_xpos=90)
define redwindow = DynamicCharacter ("red_voice",color="ff3451",image="derek_sil")
define bluewindow = DynamicCharacter ("blue_voice",color="7cb3d2",image="celia_sil")
define greenwindow = DynamicCharacter ("green_voice",color="9fff8f",image="mason_sil")
define m = DynamicCharacter ("mason_name",color="9fff8f",image="mason")
define d = DynamicCharacter ("derek_name",color="ff3451",image="derek")
define c = DynamicCharacter ("celia_name",color="7cb3d2",image="celia")
define lich = DynamicCharacter ("lich_name",color="57ffe1",image="lich")
define h = DynamicCharacter ("harold_name",color="7cb3d2",image="harold")
define jack = DynamicCharacter ("jack_name",color="7a3535",image="jack")
define komodo = DynamicCharacter ("komodo_name",color="bdc65e",image="komodo")
define dragon = DynamicCharacter ("dragon_name",color="d4833b",image="dragon")
define machete = DynamicCharacter ("machete_name",color="605a54",image="machete")
define cham = DynamicCharacter ("cham_name",color="f0eeb6",image="cham")
define jaq = DynamicCharacter ("jaq_name",color="b6c7f0",image="jaq")
define tom = DynamicCharacter ("tom_name",color="b6f0e3",image="tom")
define rich = DynamicCharacter ("rich_name",color="f0cab6",image="rich")
define demon = DynamicCharacter ("demon_name",color="66FD17",image="demon")
define fox = DynamicCharacter ("fox_name",color="000000", who_outlines=[(2, "#FFFFFF", absolute(0), absolute(0))],image="fox")
define goon = Character ("Fox's Employee",color="616161",image="fox")

define dis = { "polllayer" : Dissolve(2.0) }
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

define eyedissolve = ImageDissolve("images/effect_iris.jpg", 0.2, ramplen=256)
define eyedissolve_reverse = ImageDissolve("images/effect_iris.jpg", 0.2, reverse=True, ramplen=256)
define blooddissolve = ImageDissolve("images/effect_dripspread.jpg", 2.0, ramplen=0)
define firedissolve = ImageDissolve("images/effect_flamespread.jpg", 1.5, ramplen=64)
define zoomdissolve = ImageDissolve("images/effect_starzoom.jpg", 1.5, ramplen=64)
define shotbase = ImageDissolve("images/effect_gunshotwound.jpg", 3, ramplen=0)
define shot = { "master" : shotbase }


define glitchdissolve = MultipleTransition([
    False, Dissolve(0.5),
    "images/black.jpg", Pause(0.1),
    "images/glitch1.jpg", Pause(0.05),
    "images/glitch2.jpg", Pause(0.05),
    "images/glitch3.jpg", Pause(0.05),
    "images/glitch4.jpg", Pause(0.05),
    "images/glitch5.jpg", Pause(0.05),
    "images/black.jpg", Dissolve(0.5),
    True])
image mm_foregound:
    "images/main_menu_foreground.png"
    block:
        easeout 2.5 zoom 0.9
        easein 2.5 zoom 0.8
        easeout 2.5 zoom 0.9
        easein 5.0 zoom 1.0
        repeat
image badge_foxlogo_glow:
    block:
        "images/badge_foxlogo_glow1.png" with Dissolve(0.2, alpha=True)
        pause 0.2
        "images/badge_foxlogo_glow2.png" with Dissolve(0.2, alpha=True)
        pause 0.2
        "images/badge_foxlogo_glow3.png" with Dissolve(0.2, alpha=True)
        pause 0.2
        "images/badge_foxlogo_glow4.png" with Dissolve(0.2, alpha=True)
        pause 0.2
        "images/badge_foxlogo_glow5.png" with Dissolve(0.2, alpha=True)
        pause 0.2
        repeat
image badge_foxlogo = Composite(
    (200, 200),
    (0, 0), "badge_foxlogo_glow",
    (25, 25), "images/badge_foxlogo.png")
image dialogue_button_actions_large:
    "images/dialogue_button_actions.png"
    zoom 1.5
image dialogue_button_actions_large_hover:
    "images/dialogue_button_actions_hover.png"
    zoom 1.5
image dialogue_button_actions_large_insensitive:
    "images/dialogue_button_actions_insensitive.png"
    zoom 1.5
image chibi_celia:
    "gui/frames/1/1/1.png"
    pause 1.0
    "gui/frames/1/1/2.png"
    pause 0.2
    "gui/frames/1/1/3.png"
    pause 0.2
    "gui/frames/1/1/4.png"
    pause 1.0
    "gui/frames/1/1/5.png"
    pause 0.2
    repeat
image chibi_derek:
    "gui/frames/1/2/1.png"
    pause 0.5
    "gui/frames/1/2/2.png"
    pause 0.2
    "gui/frames/1/2/3.png"
    pause 0.2
    "gui/frames/1/2/4.png"
    pause 0.5
    "gui/frames/1/2/5.png"
    pause 0.2
    repeat
image chibi_mason:
    "gui/frames/1/3/1.png"
    pause 2.0
    "gui/frames/1/3/2.png"
    pause 0.2
    "gui/frames/1/3/3.png"
    pause 0.2
    "gui/frames/1/3/4.png"
    pause 1.0
    "gui/frames/1/3/5.png"
    pause 0.2
    repeat
image chibi_lich:
    parallel:
        alpha 1.0
        pause 10.0
        linear 5.0 alpha 0.0
        linear 0.2 alpha 1.0
        pause 0.2
        alpha 0.5
        pause 0.05
        alpha 1.0
        pause 0.05
        alpha 0.5
        pause 0.05
        alpha 1.0
        pause 0.05
        repeat
    parallel:
        block:
            block:
                "music/license/bog/1.png"
                pause 0.1
                "music/license/bog/2.png"
                pause 0.1
                "music/license/bog/3.png"
                pause 0.1
                "music/license/bog/4.png"
                pause 0.1
                repeat 15
            "music/license/bog/5.png"
            pause 0.2
            "music/license/bog/6.png"
            pause 0.2
            repeat 3
        "music/license/bog/4.png"
        zoom 1.8 xoffset -85 yoffset -150
        pause 0.1
        zoom 1.0 xoffset 0 yoffset 0
        repeat
image chibi_demon:
    "music/license/sinner/1.png"
    pause 0.2
    "music/license/sinner/2.png"
    pause 0.2
    "music/license/sinner/3.png"
    pause 0.2
    "music/license/sinner/4.png"
    pause 0.2
    "music/license/sinner/5.png"
    pause 0.2
    "music/license/sinner/6.png"
    pause 0.2
    repeat
image chibi_announcer:
    "music/license/newjob/1.png"
    pause 3.0
    "music/license/newjob/2.png"
    pause 0.1
    "music/license/newjob/3.png"
    pause 0.1
    "music/license/newjob/4.png"
    pause 1.0
    "music/license/newjob/5.png"
    pause 0.1
    "music/license/newjob/6.png"
    pause 0.1
    repeat

screen countdown():
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.366 xmaximum 500 ymaximum 43 left_bar Frame("timebar_empty.jpg", 10, 0) right_bar Frame("timebar_full.jpg", 10, 0) thumb None bar_vertical False

init:
    python:
        import math
        class Shaker(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                
                self.start = [ self.anchors.get(i, i) for i in start ]  
                self.dist = dist    
                self.child = child
            
            def __call__(self, t, sizes):
                
                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                return (int(nx), int(ny), 0, 0)
        def _Shake(start, time, child=None, dist=100.0, **properties):
            move = Shaker(start, child, dist=dist)
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)
        Shake = renpy.curry(_Shake)
init:
    $ smallshake = Shake((0, 0, 0, 0), 100.0, dist=2)
    $ largeshake = Shake((0, 0, 0, 0), 100.0, dist=4)
    $ vpunchhard = Move((0, 25), (0, -25), .10, bounce=True, repeat=True, delay=.275)
    $ hpunchhard = Move((25, 0), (-25, 0), .10, bounce=True, repeat=True, delay=.275)
    $ vpunchtiny = Move((0, 5), (0, -5), .2, repeat=True, delay=.3)
    $ hpunchtiny = Move((5, 0), (-5, 0), .2, repeat=True, delay=.3)
init:
    python:
        def silhouette_matrix (r,g,b,a=1.0):
            return im.matrix((0, 0, 0, 0, r,
                               0, 0, 0, 0, g,
                               0, 0, 0, 0, b,
                               0, 0, 0, a, 0,))
        def silhouetted (filename, r,g,b, a = 1.0):
            return im.MatrixColor (Image (filename), silhouette_matrix (r,g,b,a))
init python:
    renpy.music.register_channel("ambient", mixer="ambient", loop=True, stop_on_mute=True, tight=True)
    renpy.music.register_channel("music2", mixer="music", loop=True, stop_on_mute=True, tight=True)
    renpy.add_layer("polllayer", above="master", below=None, menu_clear=False)

init python:
    if persistent.endings_derek is None:
        persistent.endings_derek = set()
    if persistent.endings_mason is None:
        persistent.endings_mason = set()
    if persistent.endings_celia is None:
        persistent.endings_celia = set()
    if persistent.bgs_seen is None:
        persistent.bgs_seen = set()
    if persistent.cgs_celia is None:
        persistent.cgs_celia = set()
    if persistent.cgs_derek is None:
        persistent.cgs_derek = set()
    if persistent.cgs_mason is None:
        persistent.cgs_mason = set()
    if persistent.cgs_fox is None:
        persistent.cgs_fox = set()
    if persistent.cgs_celia_sex is None:
        persistent.cgs_celia_sex = set()
    if persistent.cgs_derek_sex is None:
        persistent.cgs_derek_sex = set()
    if persistent.cgs_mason_sex is None:
        persistent.cgs_mason_sex = set()
    if persistent.cgs_fox_sex is None:
        persistent.cgs_fox_sex = set()
    if persistent.deathcounter is None:
        persistent.deathcounter = 0
    if persistent.bluecounter is None:
        persistent.bluecounter = False
    if persistent.redcounter is None:
        persistent.redcounter = False
    if persistent.greencounter is None:
        persistent.greencounter = False
    if persistent.derek_killed is None:
        persistent.derek_killed = False

    def destroy_progress():
        for attr in dir(persistent):
            if not callable(attr) and not attr.startswith("_"):
                setattr(persistent, attr, None)
        for slot in renpy.list_saved_games(fast=True):
            renpy.unlink_save(slot)
        persistent._clear(progress=True)
        persistent.endings_derek = set()
        persistent.endings_mason = set()
        persistent.endings_celia = set()
        persistent.bgs_seen = set()
        persistent.cgs_celia = set()
        persistent.cgs_derek = set()
        persistent.cgs_mason = set()
        persistent.cgs_fox = set()
        persistent.cgs_celia_sex = set()
        persistent.cgs_derek_sex = set()
        persistent.cgs_mason_sex = set()
        persistent.cgs_fox_sex = set()
        persistent.deathcounter = 0
        persistent.bluecounter = False
        persistent.redcounter = False
        persistent.greencounter = False
        persistent.derek_killed = False
        renpy.notify("All data and saves cleared.")
        return



image side announcer = "images/char_announcer.png"
image side mason_sil = "images/char_sil_mason.png"
image side mason = "images/char_side_mason.png"
image side mason alert = "images/char_side_mason_alert.png"
image side mason smile = "images/char_side_mason_smile.png"
image side mason question = "images/char_side_mason_question.png"
image side mason wistful = "images/char_side_mason_wistful.png"
image side mason wistful2 = "images/char_side_mason_wistful2.png"
image side mason wistful3 = "images/char_side_mason_wistful3.png"
image side mason smirk = "images/char_side_mason_smirk.png"
image side mason surprised = "images/char_side_mason_surprised.png"
image side mason serious = "images/char_side_mason_serious.png"
image side mason angry = "images/char_side_mason_angry.png"
image side mason predatory = "images/char_side_mason_predatory.png"

image side lich = "images/char_side_lich.png"
image side lich normal = "images/char_side_lich.png"

image side demon = "demonfire"

image side jack = "images/char_side_jack.png"
image side jack normal = "images/char_side_jack.png"
image side jack serious = "images/char_side_jack_serious.png"
image side jack intense = "images/char_side_jack_intense.png"
image side jack naked = "images/char_side_jack_naked.png"

image side komodo = "images/char_side_komodo.png"
image side komodo normal = "images/char_side_komodo.png"
image side komodo surprised = "images/char_side_komodo_surprised.png"

image side dragon = "images/char_side_dragon.png"
image side dragon scared = "images/char_side_dragon_scared.png"
image side dragon angry = "images/char_side_dragon_angry.png"

image side machete = "images/char_side_machete.png"
image side cham = "images/char_side_cham.png"

image side jaq = "images/char_side_jaq.png"
image side jaq angry = "images/char_side_jaq_angry.png"
image side jaq hurt = "images/char_side_jaq_hurt.png"
image side jaq sad = "images/char_side_jaq_sad.png"
image side jaq surprised = "images/char_side_jaq_surprised.png"
image side jaq serious = "images/char_side_jaq_serious.png"
image side jaq happy = "images/char_side_jaq_happy.png"

image side tom = "images/char_side_tom.png"
image side tom surprised = "images/char_side_tom_surprised.png"
image side tom worried = "images/char_side_tom_worried.png"
image side tom happy = "images/char_side_tom_happy.png"

image side rich = ConditionSwitch(
    "meme_mode == True", "images/char_side_richard_m.png",
    "True", "images/char_side_richard.png")
image side rich scared = ConditionSwitch(
    "meme_mode == True", "images/char_side_richard_scared_m.png",
    "True", "images/char_side_richard_scared.png")

image side celia_sil = "images/char_sil_celia.png"
image side celia = "images/char_side_celia.png"
image side celia annoyed = "images/char_side_celia_annoyed.png"
image side celia angry = "images/char_side_celia_angry.png"
image side celia smile = "images/char_side_celia_smile.png"
image side celia sadistic = "images/char_side_celia_sadistic.png"
image side celia bored = "images/char_side_celia_bored.png"
image side celia horny = "images/char_side_celia_horny.png"
image side celia surprised = "images/char_side_celia_surprised.png"
image side celia surpangry = "images/char_side_celia_surpangry.png"
image side celia poisoned = "images/char_side_celia_poisoned.png"
image side celia sad = "images/char_side_celia_sad.png"
image side celia nosebleed = "images/char_side_celia_nosebleed.png"

image side derek = "images/char_side_derek.png"
image side derek normal = "images/char_side_derek.png"
image side derek_sil = "images/char_sil_derek.png"
image side derek grumpy = "images/char_side_derek_grumpy.png"
image side derek angry = "images/char_side_derek_angry.png"
image side derek mocking = "images/char_side_derek_mocking.png"
image side derek high = "images/char_side_derek_high.png"
image side derek surprise = "images/char_side_derek_surprise.png"
image side derek incredulous1 = "images/char_side_derek_incredulous_1.png"
image side derek incredulous2 = "images/char_side_derek_incredulous_2.png"
image side derek laughing = "images/char_side_derek_laughing.png"
image side derek horny = "images/char_side_derek_horny.png"
image side derek hornyblush = "images/char_side_derek_horny_blush.png"
image side derek ragged = "images/char_side_derek_ragged.png"

image mason = "images/sprite_mason.png"
image mason normal = "images/sprite_mason.png"
image mason calm = "images/sprite_mason_calm.png"
image mason question = "images/sprite_mason_question.png"
image mason serious = "images/sprite_mason_serious.png"
image mason smug = "images/sprite_mason_smug.png"
image mason excited = "images/sprite_mason_excited.png"
image mason crossbow = "images/sprite_mason_crossbow.png"
image mason knife = "images/sprite_mason_knife.png"
image mason trapped = "images/sprite_mason_trapped.png"
image mason2 shot1 = "images/sprite_mason_shot1.png"
image mason shot2 = "images/sprite_mason_shot2.png"
image mason knees = "images/sprite_mason_knees.png"

image celia = "images/sprite_celia.png"
image celia normal = "images/sprite_celia.png"
image celia relaxed = "images/sprite_celia_relaxed.png"
image celia bored = "images/sprite_celia_bored.png"
image celia disgusted = "images/sprite_celia_disgusted.png"
image celia question = "images/sprite_celia_question.png"
image celia semiserious = "images/sprite_celia_semiserious.png"
image celia serious = "images/sprite_celia_serious.png"
image celia sadistic = "images/sprite_celia_sadistic.png"
image celia surprised = "images/sprite_celia_surprised.png"
image celia mocking = "images/sprite_celia_mocking.png"
image celia angry = "images/sprite_celia_angry.png"
image celia hungry = "images/sprite_celia_hungry.png"
image celia annoyed = "images/sprite_celia_annoyed.png"
image celia sympathy = "images/sprite_celia_sympathy.png"
image celia shocked = "images/sprite_celia_shocked.png"
image celia worried = "images/sprite_celia_worried.png"
image celia laughing = "images/sprite_celia_laughing.png"
image celia phone = "images/sprite_celia_phone.png"
image celia drunk = "images/sprite_celia_drunk.png"
image celia gun = ConditionSwitch(
    "meme_mode == True", "images/sprite_celia_gun_googly.png",
    "True", "images/sprite_celia_gun.png")
image celia gunangry = ConditionSwitch(
    "meme_mode == True", "images/sprite_celia_gunangry_googly.png",
    "True", "images/sprite_celia_gunangry.png")

image harold = "images/sprite_harold.png"
image harold angry = "images/sprite_harold_angry.png"
image harold surprised = "images/sprite_harold_surprised.png"

image derek = "images/sprite_derek.png"
image derek smug = "images/sprite_derek_smug.png"
image derek fancy = "images/sprite_derek_fancy.png"
image derek fancymad = "images/sprite_derek_fancymad.png"
image derek stabbed = "images/sprite_derek_stabbed.png"
image derek deranged = "images/sprite_derek_deranged.png"
image derek fancynude = "images/sprite_derek_fancy_nude.png"
image derek fancynudecensor = "images/sprite_derek_fancy_nude_censored.png"
image derek fancymadnude = "images/sprite_derek_fancymad_nude.png"
image derek fancymadnudecensor = "images/sprite_derek_fancymad_nude_censored.png"

image machete = "images/sprite_machete.png"
image machete done = "images/sprite_machete_done.png"
image komodo = "images/sprite_komodo.png"
image dragon = "images/sprite_dragon.png"
image jack = "images/sprite_jack.png"

image jaq = "images/sprite_jaq.png"
image jaq normal = "images/sprite_jaq.png"
image jaq worried = "images/sprite_jaq_worried.png"
image jaq question = "images/sprite_jaq_question.png"
image jaq angry = "images/sprite_jaq_angry.png"
image jaq serious = "images/sprite_jaq_serious.png"
image jaq semiserious = "images/sprite_jaq_semiserious.png"
image jaq surprised = "images/sprite_jaq_surprised.png"
image jaq smile = "images/sprite_jaq_smile.png"
image tom = "images/sprite_tom.png"
image tom normal = "images/sprite_tom.png"
image tom worried = "images/sprite_tom_worried.png"
image tom wistful = "images/sprite_tom_wistful.png"
image tom happy = "images/sprite_tom_happy.png"
image tom surprised = "images/sprite_tom_surprised.png"
image rich = ConditionSwitch(
    "meme_mode == True", "images/sprite_richard_m.png",
    "True", "images/sprite_richard.png")
image rich normal = ConditionSwitch(
    "meme_mode == True", "images/sprite_richard_m.png",
    "True", "images/sprite_richard.png")
image rich worried = ConditionSwitch(
    "meme_mode == True", "images/sprite_richard_worried_m.png",
    "True", "images/sprite_richard_worried.png")
image rich angry = ConditionSwitch(
    "meme_mode == True", "images/sprite_richard_angry_m.png",
    "True", "images/sprite_richard_angry.png")
image rich turned = "images/sprite_richard_turned.png"
image rich surprised = ConditionSwitch(
    "meme_mode == True", "images/sprite_richard_surprised_m.png",
    "True", "images/sprite_richard_surprised.png")

image side mason empty = "images/empty.png"
image side celia empty = "images/empty.png"
image side derek empty = "images/empty.png"
image side lich empty = "images/empty.png"
image side harold empty = "images/empty.png"
image side machete empty = "images/empty.png"
image side komodo empty = "images/empty.png"
image side dragon empty = "images/empty.png"
image side jack empty = "images/empty.png"
image side demon empty = "images/empty.png"
image side cham empty = "images/empty.png"
image side jaq empty = "images/empty.png"
image side tom empty = "images/empty.png"
image side rich empty = "images/empty.png"
image side fox empty = "images/empty.png"

image side fox = "images/char_side_fox.png"
image side fox eyeswide = "images/char_side_fox_eyeswide.png"
image side fox angry = "images/char_side_fox_angry.png"
image side fox happy = "images/char_side_fox_happy.png"
image side fox horny = "images/char_side_fox_horny.png"
image side fox teeth = "images/char_side_fox_teeth.png"
image side fox teeth open = "images/char_side_fox_teeth_open.png"
image side fox light = "images/char_side_fox_light.png"
image camera1 = "images/sprite_camera1.png"
image camera2 = "images/sprite_camera2.png"
image camera3 = "images/sprite_camera3.png"
image camera1 tripod = "images/sprite_camera1_tripod.png"
image wedge = "images/sprite_wedge.png"
image tray = "images/sprite_tray.png"
image cam = "images/sprite_cam_empty.png"
image cam wide = "images/sprite_cam_wide.png"
image cam close = "images/sprite_cam_close_underwear.png"
image cam close claws = "images/sprite_cam_close_claws.png"
image cam close nude = "images/sprite_cam_close_nude.png"
image cam close dangle = "images/sprite_cam_close_dangle.png"
image cam close done = "images/sprite_cam_close_done.png"
image cam close done2 = "images/sprite_cam_close_done2.png"
image fox = "images/sprite_fox.png"
image fox oncomputer = "images/sprite_fox_oncomputer.png"
image fox eyeswide = "images/sprite_fox_eyeswide.png"
image fox eyeswide nomask = "images/sprite_fox_eyeswide_nomask.png"
image fox cocked = "images/sprite_fox_cocked.png"
image fox cocked nomask = "images/sprite_fox_cocked_nomask.png"
image fox angry = "images/sprite_fox_angry.png"
image fox behindmc = "images/sprite_fox_behind.png"
image fox close = "images/sprite_fox_close_long.png"
image fox close long = "images/sprite_fox_close_long.png"
image fox close long happy = "images/sprite_fox_close_long_happy.png"
image fox close long lust = "images/sprite_fox_close_long_lust.png"
image fox close long eyeswide = "images/sprite_fox_close_long_eyeswide.png"
image fox close happy = "images/sprite_fox_close_long_happy.png"
image fox close touch = "images/sprite_fox_close_touch.png"
image fox close touch happy = "images/sprite_fox_close_touch_happy.png"
image fox close touch horny = "images/sprite_fox_close_touch_horny.png"
image fox close touch cocked = "images/sprite_fox_close_touch_cocked.png"
image fox close touch eyeswide = "images/sprite_fox_close_touch_eyeswide.png"
image fox close knife = "images/sprite_fox_close_knife.png"
image fox close whisper = "images/sprite_fox_close_whisper.png"
image fox close serious = "images/sprite_fox_close_serious.png"
image fox close soldering = "images/sprite_fox_close_soldering.png"
image fox close soldering eyeswide = "images/sprite_fox_close_soldering_eyeswide.png"
image fox holdingcam = "images/sprite_fox_holdingcam.png"
image fox ultraclose = "images/sprite_fox_ultraclose.png"
image fox ultraclose eyeswide = "images/sprite_fox_ultraclose_eyeswide.png"
image fox ultraclose eyeswide nomask = "images/sprite_fox_ultraclose_eyeswide_nomask.png"
image fox ultraclose happy = "images/sprite_fox_ultraclose_happy.png"
image fox ultraclose cocked = "images/sprite_fox_ultraclose_cocked.png"
image fox ultraclose gag = "images/sprite_fox_ultraclose_gag.png"
image fox ultraclose kabedon = "images/sprite_fox_ultraclose_kabedon.png"
image fox ultraclose kabedon angry = "images/sprite_fox_ultraclose_kabedon_angry.png"
image fox ultraclose speculum = "images/sprite_fox_ultraclose_speculum.png"
image fox ultraclose grab = "images/sprite_fox_ultraclose_grab.png"
image fox torch = "images/sprite_fox_torch.png"
image fox torch fire = "images/sprite_fox_torch_on.png"
image fox torch close = "images/sprite_fox_torch_close.png"
image fox torch close happy = "images/sprite_fox_torch_close_happy.png"
image fox torch close angry = "images/sprite_fox_torch_close_angry.png"
image fox torch close fire = "images/sprite_fox_torch_close_on.png"
image afterburn = "images/sprite_fox_afterburn.png"
image fox hand knife = "images/sprite_fox_hand_knife.png"
image fox comp = "images/sprite_fox_comp.png"
image fox comp presenting = "images/sprite_fox_comp_presenting.png"
image fox comp lookback = "images/sprite_fox_comp_lookback.png"
image fox comp lookback laugh = "images/sprite_fox_comp_lookback_laugh.png"
image fox comp cocked = "images/sprite_fox_comp_cocked.png"
image fox comp shrug = "images/sprite_fox_comp_shrug.png"
image fox comp angry = "images/sprite_fox_comp_angry.png"
image fox comp over = "images/sprite_fox_comp_over.png"
image fox comp maskon = "images/sprite_fox_comp_mask.png"
image fox comp gun = "images/sprite_fox_comp_gun.png"
image fox comp gunback = "images/sprite_fox_comp_gunback.png"
image fox comp gunup = "images/sprite_fox_comp_gunup.png"
image fox comp soldering = "images/sprite_fox_comp_soldering.png"
image fox comp soldering cocked = "images/sprite_fox_comp_soldering_cocked.png"
image fox comp soldering shrug = "images/sprite_fox_comp_soldering_shrug.png"
image fox comp gag = "images/sprite_fox_comp_gag.png"
image fox comp toys = "images/sprite_fox_comp_toys.png"
image fox comp toys cocked = "images/sprite_fox_comp_toys_cocked.png"
image fox comp nailgun = "images/sprite_fox_comp_nailgun.png"
image fox comp nailgun lookback = "images/sprite_fox_comp_nailgun_lookback.png"
image fox chokechain = "images/sprite_fox_chokechain.png"
image fox nailgun = "images/sprite_fox_nailgun.png"
image fox nailgun look = "images/sprite_fox_nailgun_look.png"
image fox nailgun cocked = "images/sprite_fox_nailgun_cocked.png"
image fox gunjob = "images/sprite_fox_gunjob.png"
image fox gunjob narrow = "images/sprite_fox_gunjob_narrow.png"
image fox gunjob far = "images/sprite_fox_gunjob_far.png"
image fox gunjob lookback = "images/sprite_fox_gunjob_lookback.png"
image fox gunjob far eyeswide = "images/sprite_fox_gunjob_far_eyeswide.png"
image fox gunjob far serious = "images/sprite_fox_gunjob_far_serious.png"
image fox cock = "images/sprite_fox_cock.png"
image fox standover = "images/sprite_fox_standover.png"
image fox standover cock = "images/sprite_fox_standover_cock.png"
image fox light = "images/sprite_fox_light.png"
image fox light smile = "images/sprite_fox_light_smile.png"
image fox light laugh = "images/sprite_fox_light_laugh.png"
image fox light cocked = "images/sprite_fox_light_cocked.png"
image fox light serious = "images/sprite_fox_light_serious.png"
image fox light angry = "images/sprite_fox_light_angry.png"
image fox light sitting = ConditionSwitch(
    "meme_mode == True", "images/sprite_fox_light_sitting_meme.png",
    "True", "images/sprite_fox_light_sitting.png")
image fox light sitting smile = ConditionSwitch(
    "meme_mode == True", "images/sprite_fox_light_sitting_smile_meme.png",
    "True", "images/sprite_fox_light_sitting_smile.png")
image fox light sitting smile2 = ConditionSwitch(
    "meme_mode == True", "images/sprite_fox_light_sitting_smile2_meme.png",
    "True", "images/sprite_fox_light_sitting_smile2.png")
image fox light sitting talk = ConditionSwitch(
    "meme_mode == True", "images/sprite_fox_light_sitting_talk_meme.png",
    "True", "images/sprite_fox_light_sitting_talk.png")
image fox light sitting bored = ConditionSwitch(
    "meme_mode == True", "images/sprite_fox_light_sitting_bored_meme.png",
    "True", "images/sprite_fox_light_sitting_bored.png")
image fox light sitting thinking = ConditionSwitch(
    "meme_mode == True", "images/sprite_fox_light_sitting_thinking_meme.png",
    "True", "images/sprite_fox_light_sitting_thinking.png")
image fox light sitting laugh = ConditionSwitch(
    "meme_mode == True", "images/sprite_fox_light_sitting_laugh_meme.png",
    "True", "images/sprite_fox_light_sitting_laugh.png")
image fox light sitting question = ConditionSwitch(
    "meme_mode == True", "images/sprite_fox_light_sitting_question_meme.png",
    "True", "images/sprite_fox_light_sitting_question.png")
image fox keep1 = "images/sprite_fox_keep1.png"
image fox keep2 = "images/sprite_fox_keep2.png"
image fox keep3 = "images/sprite_fox_keep3.png"
image fox light tail:
    "images/sprite_fox_light.png"
    pause 0.1
    "images/sprite_fox_light_2.png"
    pause 0.1
    "images/sprite_fox_light_3.png"
    pause 0.1
    "images/sprite_fox_light_4.png"
    pause 0.1
    "images/sprite_fox_light.png"
image fox torch flicker:
    "fox torch"
    pause 0.25
    "fox torch fire"
    pause 0.05
    "fox torch"
    pause 0.10
    "fox torch fire"
    pause 0.25
    "fox torch"
image fox torch flicker close:
    "fox torch close"
    pause 0.25
    "fox torch close fire"
    pause 0.05
    "fox torch close"
    pause 0.10
    "fox torch close fire"

image goonk = ConditionSwitch(
    "meme_mode == True", "images/sprite_goon_kangaroo_meme.png",
    "True", "images/sprite_goon_kangaroo.png")
image goonr = ConditionSwitch(
    "meme_mode == True", "images/sprite_goon_rhino_meme.png",
    "True", "images/sprite_goon_rhino.png")
image goonk smile = ConditionSwitch(
    "meme_mode == True", "images/sprite_goon_kangaroo_smile_meme.png",
    "True", "images/sprite_goon_kangaroo_smile.png")
image goonr smile = ConditionSwitch(
    "meme_mode == True", "images/sprite_goon_rhino_smile_meme.png",
    "True", "images/sprite_goon_rhino_smile.png")
image showguts1 = "images/sprite_MC_guts1.png"
image showguts2 = "images/sprite_MC_guts2.png"

image darkroom = ConditionSwitch(
    "meme_mode == True", "images/show_darkroom_meme.png",
    "True", "images/show_darkroom.png")
image darkroom red = ConditionSwitch(
    "meme_mode == True", "images/show_darkroom_red_meme.png",
    "True", "images/show_darkroom_red.png")
image darkroom bright = ConditionSwitch(
    "meme_mode == True", "images/show_darkroom_bright_meme.png",
    "True", "images/show_darkroom_bright.png")
image lightroom = ConditionSwitch(
    "meme_mode == True", "images/show_lightroom_meme.png",
    "True", "images/show_lightroom.png")
image darkwipe = "images/effect_blackwipe.png"

image icon_heart:
    "images/icon_heart.png"
image menu_pin_large:
    "images/item_pin_idle.png"
    zoom 1.0
    yoffset -45
image menu_pin:
    "images/item_pin_idle.png"
    zoom 0.85
    yoffset -55
image menu_rat_poison_large:
    "images/item_rat_poison_idle.png"
    zoom 1.0
    yoffset -50
image menu_rat_poison:
    "images/item_rat_poison_idle.png"
    zoom 0.85
    yoffset -60
image menu_office_key_large:
    "images/item_office_key_idle.png"
    zoom 1.0
    yoffset -45
image menu_office_key:
    "images/item_office_key_idle.png"
    zoom 0.85
    yoffset -55
image menu_battery_taser_large:
    "images/item_battery_taser_idle.png"
    zoom 1.0
    yoffset -45
image menu_battery_taser:
    "images/item_battery_taser_idle.png"
    zoom 0.85
    yoffset -55
image menu_sanity_large:
    "images/icon_half_sanity.png"
    zoom 1.2
    yoffset -13
image menu_sanity:
    "images/icon_half_sanity.png"
    yoffset -23
image numpad_bg:
    "images/numpad_bg.png"
    yzoom 0
    xalign 0.5
    yalign 0.49
    pause 0.5
    easeout_expo 0.5 yzoom 1.0
image numpad_bg_small:
    "images/numpad_bg.png"
    yzoom 0
    xalign 0.5
    yalign 0.19
    pause 0.5
    easeout_expo 0.5 yzoom 1.0
image window_red_flash:
    "images/window_red.png"
    xanchor 0.0
    yanchor 0.0
    xpos 0
    ypos -13
    alpha 0.0
    easein_expo 0.5 alpha 1.0
    easeout 1.0 alpha 0.0
image window_blue_flash:
    "images/window_blue.png"
    xanchor 0.0
    yanchor 0.0
    xpos -3
    ypos -4
    alpha 0.0
    easein_expo 0.5 alpha 1.0
    easeout 1.0 alpha 0.0
image window_green_flash:
    "images/window_green.png"
    xanchor 0.0
    yanchor 0.0
    xpos -1
    ypos -19
    alpha 0.0
    easein_expo 0.5 alpha 1.0
    easeout 1.0 alpha 0.0

image map_pointer:
    "images/map_indicator.png"
    yoffset 0
    ease_bounce 0.5 yoffset 5
    repeat
image map_pointer_glitch:
    "images/map_indicator.png"
    block:
        yoffset 0
        ease_bounce 0.5 yoffset 5
        repeat 7
    yoffset 50
    xoffset 50
    pause 0.1
    yoffset 0
    ease_bounce 0.5 yoffset 5
    pause 0.3
    yoffset 0
    xoffset 0
    pause 1.0
    yoffset -80
    xoffset -120
    pause 0.5
    yoffset 0
    ease_bounce 0.5 yoffset 5
    pause 0.3
    yoffset 0
    xoffset 0
    repeat
image effect_injury:
    "images/effect_injury.png"
    zoom 1.0
    alpha 0.7
    easeout_expo 0.05 alpha 1.0 zoom 1.1
    pause 0.4
    easeout 0.5 alpha 0.0

transform side_changer(old, new):
    contains:
        old
        yalign 1.0
        xoffset 0
        alpha 1.0
        easein 0.1 xoffset -20 alpha 0.0
    contains:
        new
        yalign 1.0
        xoffset -20
        alpha 0.0
        easein 0.3 xoffset 0 alpha 1.0
transform bounce:
    yoffset 15
    easein .05 yoffset 0
    easeout .05 yoffset 15
    easein .05 yoffset 12
    easeout .05 yoffset 15
    yoffset 15
transform laugh:
    yoffset 0
    easein .05 yoffset 15
    easeout .1 yoffset 0
    easein .05 yoffset 10
    easeout .1 yoffset 5
    yoffset 0
transform swing:
    zoom 1.1
    xoffset 0
    easein 0.75 xoffset 20
    easeout 0.75 xoffset 0
    easein 0.75 xoffset -20
    easeout 0.75 xoffset 0
    easein 0.75 xoffset 15
    easeout 0.75 xoffset 0
    easein 0.75 xoffset -15
    easeout 0.75 xoffset 0
    easein 0.75 xoffset 10
    easeout 0.75 xoffset 0
    easein 0.75 xoffset -10
    easeout 0.75 xoffset 0
    easein 0.75 xoffset 5
    easeout 0.75 xoffset 0
    easein 0.75 xoffset 5
    easeout 0.75 xoffset 0
transform pulse:
    xalign 0.5
    yalign 0.5
    xanchor 0.5
    yanchor 0.5
    zoom 1.0
    easeout 0.5 zoom 1.05
    easein 0.5 zoom 1.1
    easeout 0.5 zoom 1.05
    easein 0.5 zoom 1.0
    repeat
transform heartbeat:
    xalign 0.5
    yalign 0.0
    xanchor 0.5
    yanchor 0.5
    zoom 1.0
    easeout 0.3 zoom 1.005
    easein 0.3 zoom 1.0
    pause 1.0
    easeout 0.2 zoom 1.01
    easein 0.2 zoom 1.0
    pause 1.0
    easeout 0.1 zoom 1.02
    easein 0.1 zoom 1.0
    pause 1.0
    block:
        easeout 0.1 zoom 1.02
        ease 0.05 zoom 1.1
        ease 0.05 zoom 1.02
        easein 0.1 zoom 1.0
        pause 1.0
        repeat
transform tension_vibrate:
    xalign 0.5
    yalign 0.5
    xanchor 0.5
    yanchor 0.5
    zoom 1.0
    parallel:
        easein 1.0 zoom 1.05
    parallel:
        ease_bounce 0.05 yoffset 3
        ease_bounce 0.05 yoffset -3
        repeat
    parallel:
        ease_bounce 0.05 xoffset 3
        ease_bounce 0.05 xoffset -3
        repeat
transform flicker:
    alpha 0.0
    xoffset 0
    easein 1.0 alpha 1.0
    block:
        alpha 0.0
        pause 0.01
        alpha 1
        xoffset -5
        pause 0.02
        xoffset 2
        pause 0.01
        xoffset 0
        alpha 0.5
        easein 0.1 alpha 1
        pause 0.5
        easein 0.1 alpha 0.5
        pause 0.1
        alpha 1.0
        pause 0.1
        alpha 0.0
        pause 0.3
        alpha 1.0
        pause 3.0
        repeat
transform confused_bobbing:
    xoffset 0
    xalign 0.5
    easein 0.75 xoffset 100
    easeout 0.75 xoffset 0
    easein 0.75 xoffset -100
    easeout 0.75 xoffset 0
    easein 0.75 xoffset 50
    easeout 0.75 xoffset 0
    easein 0.75 xoffset -50
    easeout 0.75 xoffset 0
    repeat
image mapscare:
    "images/mapscare_1.png"
    pause 2.0
    "images/mapscare_2.png"
    pause 1.0
    "images/mapscare_3.png"
    pause 2.0
    "images/mapscare_5.png"
    pause 0.03
    "images/mapscare_4.png"
    pause 0.03
    "images/mapscare_5.png"
image mapsand:
    "images/derek_map_glitch1.png"
    pause 0.03
    "images/derek_map_glitch2.png"
    pause 0.03
    "images/derek_map_glitch3.png"
    pause 0.03
    "images/derek_map_glitch4.png"
    pause 3.0
    repeat
image cg_derek_shadowdemon:
    "images/cg_derek_shadowdemon_0.jpg"
    pause 2.0
    "images/cg_derek_shadowdemon_1.jpg"
    pause 0.1
    "images/cg_derek_shadowdemon_2.jpg"
    pause 0.1
    "images/cg_derek_shadowdemon_3.jpg"
    pause 0.1
    "images/cg_derek_shadowdemon_4.jpg"
    pause 0.1
    "images/cg_derek_shadowdemon_5.jpg"
    pause 0.1
    "images/cg_derek_shadowdemon_6.jpg"
    pause 0.1
    "images/cg_derek_shadowdemon_7.jpg"
    pause 0.1
    "images/black.jpg"
image cg_derek_shadowdemon_1:
    "images/cg_derek_shadowdemon_0.jpg"
image cg_derek_shadowdemon_2:
    "images/cg_derek_shadowdemon_1.jpg"
    pause 0.1
    "images/cg_derek_shadowdemon_2.jpg"
    pause 0.1
    "images/cg_derek_shadowdemon_3.jpg"
    pause 0.1
    "images/cg_derek_shadowdemon_4.jpg"
    pause 0.1
    "images/cg_derek_shadowdemon_5.jpg"
    pause 0.1
    "images/cg_derek_shadowdemon_6.jpg"
    pause 0.1
    "images/cg_derek_shadowdemon_7.jpg"
    pause 0.1
    "images/black.jpg"
define config.side_image_change_transform = side_changer
define config.side_image_only_not_showing = True

image campfire_base_1:
    "images/fire_glow.png"
    easeout 0.5 zoom 1.05
    easein 0.5 zoom 1.1
    easeout 0.5 zoom 1.05
    easein 0.5 zoom 1.0
    repeat
image campfire_base_2:
    "images/fire_1.png"
    easeout 1.0 alpha 0.0
    easeout 1.0 alpha 1.0
    repeat
image campfire_base_3:
    "images/fire_2.png"
    alpha 0.0
    easeout 1.0 alpha 1.0
    easeout 1.0 alpha 0.0
    repeat
image campfire = Composite(
    (1280, 720),
    (0, 0), "campfire_base_1",
    (0, 0), "campfire_base_2",
    (0, 0), "campfire_base_3")
image mason_scare_1_1:
    "images/asset_visitor_1.png"
    alpha 0.0
    easeout 0.1 alpha 1.0
    pause 5.0
    easein 0.3 alpha 0.0
image mason_scare_1_2:
    "images/asset_visitor_2.png"
    alpha 0.0
    pause 3.0
    easein 1.0 alpha 1.0
    pause 0.3
    easeout 0.1 alpha 0.0
image mason_scare_1 = Composite(
    (1280, 720),
    (300, 280), "mason_scare_1_1",
    (300, 280), "mason_scare_1_2")
image mason_scare_2:
    "images/bg_mason_thicket_eyes.png"
    alpha 0.0
    easein 1.0 alpha 1.0
    pause 3.0
    easein 0.5 alpha 0.0
image demonfire_base_1:
    "images/char_side_strade_1.png"
    easeout 1.0 alpha 0.0
    pause 1.0
    easeout 1.0 alpha 1.0
    repeat
image demonfire_base_2:
    "images/char_side_strade_2.png"
    alpha 0.0
    easeout 1.0 alpha 1.0
    easeout 1.0 alpha 0.0
    pause 1.0
    repeat
image demonfire_base_3:
    "images/char_side_strade_3.png"
    alpha 0.0
    pause 1.0
    easeout 1.0 alpha 1.0
    easeout 1.0 alpha 0.0
    repeat
image demonfire_base_4:
    "images/char_side_strade_4.png"
image demonfire = Composite(
    (333, 333),
    (0, 0), "demonfire_base_4",
    (0, 0), "demonfire_base_1",
    (0, 0), "demonfire_base_2",
    (0, 0), "demonfire_base_3")
image bluefire:
    "images/asset_bluefire_1.png"
    pause 0.1
    "images/asset_bluefire_2.png"
    pause 0.1
    "images/asset_bluefire_3.png"
    pause 0.1
    "images/asset_bluefire_4.png"
    pause 0.1
    "images/asset_bluefire_5.png"
    pause 0.1
    "images/asset_bluefire_6.png"
    pause 0.1
    "images/asset_bluefire_7.png"
    pause 0.1
    repeat
image embarassing_coverup:
    "images/embarassing_coverup.png"
image bg_mason_meadow = ConditionSwitch(
    "8 <= hours <= 18", "images/bg_mason_meadow.jpg",
    "hours == 7", "images/bg_mason_meadow_morning.jpg",
    "hours == 19", "images/bg_mason_meadow_twilight.jpg",
    "True", "images/bg_mason_meadow_night.jpg")
image bg_mason_thicket = ConditionSwitch(
    "8 <= hours <= 18", "images/bg_mason_thicket.jpg",
    "hours == 7", "images/bg_mason_thicket_morning.jpg",
    "hours == 19", "images/bg_mason_thicket_twilight.jpg",
    "True", "images/bg_mason_thicket_night.jpg")
image bg_mason_talltree = ConditionSwitch(
    "8 <= hours <= 18", "images/bg_mason_talltree.jpg",
    "hours == 7", "images/bg_mason_talltree_morning.jpg",
    "hours == 19", "images/bg_mason_talltree_twilight.jpg",
    "True", "images/bg_mason_talltree_night.jpg")
image bg_mason_waterfall = ConditionSwitch(
    "8 <= hours <= 18", "images/bg_mason_waterfall.jpg",
    "hours == 7", "images/bg_mason_waterfall_morning.jpg",
    "hours == 19", "images/bg_mason_waterfall_twilight.jpg",
    "True", "images/bg_mason_waterfall_night.jpg")
image bg_mason_cabin = ConditionSwitch(
    "8 <= hours <= 18", "images/bg_mason_cabin.jpg",
    "hours == 7", "images/bg_mason_cabin_morning.jpg",
    "hours == 19", "images/bg_mason_cabin_twilight.jpg",
    "True", "images/bg_mason_cabin_night.jpg")
image bg_mason_incabin = ConditionSwitch(
    "8 <= hours <= 18 and meme_mode == True", "images/bg_mason_incabin_wd.jpg",
    "8 <= hours <= 18", "images/bg_mason_incabin.jpg",
    "hours == 7 and meme_mode == True", "images/bg_mason_incabin_morning_wd.jpg",
    "hours == 7", "images/bg_mason_incabin_morning.jpg",
    "hours == 19 and meme_mode == True", "images/bg_mason_incabin_twilight_wd.jpg",
    "hours == 19", "images/bg_mason_incabin_twilight.jpg",
    "meme_mode == True", "images/bg_mason_incabin_night_wd.jpg",
    "True", "images/bg_mason_incabin_night.jpg")
image bg_mason_swamp = ConditionSwitch(
    "8 <= hours <= 18", "images/bg_mason_swamp.jpg",
    "hours == 7", "images/bg_mason_swamp_morning.jpg",
    "hours == 19", "images/bg_mason_swamp_twilight.jpg",
    "True", "images/bg_mason_swamp_night.jpg")
image bg_derek_camp = ConditionSwitch(
    "8 <= hours <= 18", "images/bg_derek_camp.jpg",
    "hours == 7", "images/bg_derek_camp_morning.jpg",
    "hours == 19", "images/bg_derek_camp_twilight.jpg",
    "True", "images/bg_derek_camp_night.jpg")
image bg_derek_desert = ConditionSwitch(
    "8 <= hours <= 18", "images/bg_derek_desert.jpg",
    "hours == 7", "images/bg_derek_desert_morning.jpg",
    "hours == 19", "images/bg_derek_desert_twilight.jpg",
    "True", "images/bg_derek_desert_night.jpg")
image bg_derek_hill = ConditionSwitch(
    "8 <= hours <= 18", "images/bg_derek_hill.jpg",
    "hours == 7", "images/bg_derek_hill_morning.jpg",
    "hours == 19", "images/bg_derek_hill_twilight.jpg",
    "True", "images/bg_derek_hill_night.jpg")
image bg_derek_fissure = ConditionSwitch(
    "8 <= hours <= 18", "images/bg_derek_fissure.jpg",
    "hours == 7", "images/bg_derek_fissure_morning.jpg",
    "hours == 19", "images/bg_derek_fissure_twilight.jpg",
    "True", "images/bg_derek_fissure_night.jpg")
image bg_derek_deepdesert = ConditionSwitch(
    "8 <= hours <= 18", "images/bg_derek_deepdesert.jpg",
    "hours == 7", "images/bg_derek_deepdesert_morning.jpg",
    "hours == 19", "images/bg_derek_deepdesert_twilight.jpg",
    "True", "images/bg_derek_deepdesert_night.jpg")
image bg_derek_cave = "images/bg_derek_cave.jpg"

image bg_celia_room_10:
    "images/bg_celia_room.jpg"
image bg_celia_room_alpha_90:
    "images/bg_celia_room_strain.jpg"
    alpha 0.9
image bg_celia_room_alpha_80:
    "images/bg_celia_room_strain.jpg"
    alpha 0.8
image bg_celia_room_alpha_70:
    "images/bg_celia_room_strain.jpg"
    alpha 0.7
image bg_celia_room_alpha_60:
    "images/bg_celia_room_strain.jpg"
    alpha 0.6
image bg_celia_room_alpha_50:
    "images/bg_celia_room_strain.jpg"
    alpha 0.5
image bg_celia_room_alpha_40:
    "images/bg_celia_room_strain.jpg"
    alpha 0.4
image bg_celia_room_alpha_30:
    "images/bg_celia_room_strain.jpg"
    alpha 0.3
image bg_celia_room_alpha_20:
    "images/bg_celia_room_strain.jpg"
    alpha 0.2
image bg_celia_room_alpha_10:
    "images/bg_celia_room_strain.jpg"
    alpha 0.1
image bg_celia_room_9 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_room.jpg",
(0, 0), "bg_celia_room_alpha_90")
image bg_celia_room_8 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_room.jpg",
(0, 0), "bg_celia_room_alpha_80")
image bg_celia_room_7 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_room.jpg",
(0, 0), "bg_celia_room_alpha_70")
image bg_celia_room_6 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_room.jpg",
(0, 0), "bg_celia_room_alpha_60")
image bg_celia_room_5 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_room.jpg",
(0, 0), "bg_celia_room_alpha_50")
image bg_celia_room_4 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_room.jpg",
(0, 0), "bg_celia_room_alpha_40")
image bg_celia_room_3 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_room.jpg",
(0, 0), "bg_celia_room_alpha_30")
image bg_celia_room_2 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_room.jpg",
(0, 0), "bg_celia_room_alpha_20")
image bg_celia_room_1 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_room.jpg",
(0, 0), "bg_celia_room_alpha_10")

image bg_celia_office_10:
    "images/bg_celia_office.jpg"
image bg_celia_office_alpha_90:
    "images/bg_celia_office_strain.jpg"
    alpha 0.9
image bg_celia_office_alpha_80:
    "images/bg_celia_office_strain.jpg"
    alpha 0.8
image bg_celia_office_alpha_70:
    "images/bg_celia_office_strain.jpg"
    alpha 0.7
image bg_celia_office_alpha_60:
    "images/bg_celia_office_strain.jpg"
    alpha 0.6
image bg_celia_office_alpha_50:
    "images/bg_celia_office_strain.jpg"
    alpha 0.5
image bg_celia_office_alpha_40:
    "images/bg_celia_office_strain.jpg"
    alpha 0.4
image bg_celia_office_alpha_30:
    "images/bg_celia_office_strain.jpg"
    alpha 0.3
image bg_celia_office_alpha_20:
    "images/bg_celia_office_strain.jpg"
    alpha 0.2
image bg_celia_office_alpha_10:
    "images/bg_celia_office_strain.jpg"
    alpha 0.1
image bg_celia_office_9 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_office.jpg",
(0, 0), "bg_celia_office_alpha_90")
image bg_celia_office_8 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_office.jpg",
(0, 0), "bg_celia_office_alpha_80")
image bg_celia_office_7 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_office.jpg",
(0, 0), "bg_celia_office_alpha_70")
image bg_celia_office_6 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_office.jpg",
(0, 0), "bg_celia_office_alpha_60")
image bg_celia_office_5 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_office.jpg",
(0, 0), "bg_celia_office_alpha_50")
image bg_celia_office_4 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_office.jpg",
(0, 0), "bg_celia_office_alpha_40")
image bg_celia_office_3 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_office.jpg",
(0, 0), "bg_celia_office_alpha_30")
image bg_celia_office_2 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_office.jpg",
(0, 0), "bg_celia_office_alpha_20")
image bg_celia_office_1 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_office.jpg",
(0, 0), "bg_celia_office_alpha_10")


image bg_celia_lounge_10:
    "images/bg_celia_lounge.jpg"
image bg_celia_lounge_alpha_90:
    "images/bg_celia_lounge_strain.jpg"
    alpha 0.9
image bg_celia_lounge_alpha_80:
    "images/bg_celia_lounge_strain.jpg"
    alpha 0.8
image bg_celia_lounge_alpha_70:
    "images/bg_celia_lounge_strain.jpg"
    alpha 0.7
image bg_celia_lounge_alpha_60:
    "images/bg_celia_lounge_strain.jpg"
    alpha 0.6
image bg_celia_lounge_alpha_50:
    "images/bg_celia_lounge_strain.jpg"
    alpha 0.5
image bg_celia_lounge_alpha_40:
    "images/bg_celia_lounge_strain.jpg"
    alpha 0.4
image bg_celia_lounge_alpha_30:
    "images/bg_celia_lounge_strain.jpg"
    alpha 0.3
image bg_celia_lounge_alpha_20:
    "images/bg_celia_lounge_strain.jpg"
    alpha 0.2
image bg_celia_lounge_alpha_10:
    "images/bg_celia_lounge_strain.jpg"
    alpha 0.1
image bg_celia_lounge_9 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_lounge.jpg",
(0, 0), "bg_celia_lounge_alpha_90")
image bg_celia_lounge_8 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_lounge.jpg",
(0, 0), "bg_celia_lounge_alpha_80")
image bg_celia_lounge_7 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_lounge.jpg",
(0, 0), "bg_celia_lounge_alpha_70")
image bg_celia_lounge_6 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_lounge.jpg",
(0, 0), "bg_celia_lounge_alpha_60")
image bg_celia_lounge_5 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_lounge.jpg",
(0, 0), "bg_celia_lounge_alpha_50")
image bg_celia_lounge_4 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_lounge.jpg",
(0, 0), "bg_celia_lounge_alpha_40")
image bg_celia_lounge_3 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_lounge.jpg",
(0, 0), "bg_celia_lounge_alpha_30")
image bg_celia_lounge_2 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_lounge.jpg",
(0, 0), "bg_celia_lounge_alpha_20")
image bg_celia_lounge_1 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_lounge.jpg",
(0, 0), "bg_celia_lounge_alpha_10")

image bg_celia_breakroom_10:
    "images/bg_celia_breakroom.jpg"
image bg_celia_breakroom_alpha_90:
    "images/bg_celia_breakroom_strain.jpg"
    alpha 0.9
image bg_celia_breakroom_alpha_80:
    "images/bg_celia_breakroom_strain.jpg"
    alpha 0.8
image bg_celia_breakroom_alpha_70:
    "images/bg_celia_breakroom_strain.jpg"
    alpha 0.7
image bg_celia_breakroom_alpha_60:
    "images/bg_celia_breakroom_strain.jpg"
    alpha 0.6
image bg_celia_breakroom_alpha_50:
    "images/bg_celia_breakroom_strain.jpg"
    alpha 0.5
image bg_celia_breakroom_alpha_40:
    "images/bg_celia_breakroom_strain.jpg"
    alpha 0.4
image bg_celia_breakroom_alpha_30:
    "images/bg_celia_breakroom_strain.jpg"
    alpha 0.3
image bg_celia_breakroom_alpha_20:
    "images/bg_celia_breakroom_strain.jpg"
    alpha 0.2
image bg_celia_breakroom_alpha_10:
    "images/bg_celia_breakroom_strain.jpg"
    alpha 0.1
image bg_celia_breakroom_9 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_breakroom.jpg",
(0, 0), "bg_celia_breakroom_alpha_90")
image bg_celia_breakroom_8 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_breakroom.jpg",
(0, 0), "bg_celia_breakroom_alpha_80")
image bg_celia_breakroom_7 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_breakroom.jpg",
(0, 0), "bg_celia_breakroom_alpha_70")
image bg_celia_breakroom_6 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_breakroom.jpg",
(0, 0), "bg_celia_breakroom_alpha_60")
image bg_celia_breakroom_5 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_breakroom.jpg",
(0, 0), "bg_celia_breakroom_alpha_50")
image bg_celia_breakroom_4 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_breakroom.jpg",
(0, 0), "bg_celia_breakroom_alpha_40")
image bg_celia_breakroom_3 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_breakroom.jpg",
(0, 0), "bg_celia_breakroom_alpha_30")
image bg_celia_breakroom_2 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_breakroom.jpg",
(0, 0), "bg_celia_breakroom_alpha_20")
image bg_celia_breakroom_1 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_breakroom.jpg",
(0, 0), "bg_celia_breakroom_alpha_10")

image bg_celia_basement_10:
    "images/bg_celia_basement.jpg"
image bg_celia_basement_alpha_90:
    "images/bg_celia_basement_strain.jpg"
    alpha 0.9
image bg_celia_basement_alpha_80:
    "images/bg_celia_basement_strain.jpg"
    alpha 0.8
image bg_celia_basement_alpha_70:
    "images/bg_celia_basement_strain.jpg"
    alpha 0.7
image bg_celia_basement_alpha_60:
    "images/bg_celia_basement_strain.jpg"
    alpha 0.6
image bg_celia_basement_alpha_50:
    "images/bg_celia_basement_strain.jpg"
    alpha 0.5
image bg_celia_basement_alpha_40:
    "images/bg_celia_basement_strain.jpg"
    alpha 0.4
image bg_celia_basement_alpha_30:
    "images/bg_celia_basement_strain.jpg"
    alpha 0.3
image bg_celia_basement_alpha_20:
    "images/bg_celia_basement_strain.jpg"
    alpha 0.2
image bg_celia_basement_alpha_10:
    "images/bg_celia_basement_strain.jpg"
    alpha 0.1
image bg_celia_basement_9 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_basement.jpg",
(0, 0), "bg_celia_basement_alpha_90")
image bg_celia_basement_8 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_basement.jpg",
(0, 0), "bg_celia_basement_alpha_80")
image bg_celia_basement_7 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_basement.jpg",
(0, 0), "bg_celia_basement_alpha_70")
image bg_celia_basement_6 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_basement.jpg",
(0, 0), "bg_celia_basement_alpha_60")
image bg_celia_basement_5 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_basement.jpg",
(0, 0), "bg_celia_basement_alpha_50")
image bg_celia_basement_4 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_basement.jpg",
(0, 0), "bg_celia_basement_alpha_40")
image bg_celia_basement_3 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_basement.jpg",
(0, 0), "bg_celia_basement_alpha_30")
image bg_celia_basement_2 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_basement.jpg",
(0, 0), "bg_celia_basement_alpha_20")
image bg_celia_basement_1 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_basement.jpg",
(0, 0), "bg_celia_basement_alpha_10")

image bg_celia_elevator_10:
    "images/bg_celia_elevator.jpg"
image bg_celia_elevator_alpha_90:
    "images/bg_celia_elevator_strain.jpg"
    alpha 0.9
image bg_celia_elevator_alpha_80:
    "images/bg_celia_elevator_strain.jpg"
    alpha 0.8
image bg_celia_elevator_alpha_70:
    "images/bg_celia_elevator_strain.jpg"
    alpha 0.7
image bg_celia_elevator_alpha_60:
    "images/bg_celia_elevator_strain.jpg"
    alpha 0.6
image bg_celia_elevator_alpha_50:
    "images/bg_celia_elevator_strain.jpg"
    alpha 0.5
image bg_celia_elevator_alpha_40:
    "images/bg_celia_elevator_strain.jpg"
    alpha 0.4
image bg_celia_elevator_alpha_30:
    "images/bg_celia_elevator_strain.jpg"
    alpha 0.3
image bg_celia_elevator_alpha_20:
    "images/bg_celia_elevator_strain.jpg"
    alpha 0.2
image bg_celia_elevator_alpha_10:
    "images/bg_celia_elevator_strain.jpg"
    alpha 0.1
image bg_celia_elevator_9 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_elevator.jpg",
(0, 0), "bg_celia_elevator_alpha_90")
image bg_celia_elevator_8 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_elevator.jpg",
(0, 0), "bg_celia_elevator_alpha_80")
image bg_celia_elevator_7 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_elevator.jpg",
(0, 0), "bg_celia_elevator_alpha_70")
image bg_celia_elevator_6 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_elevator.jpg",
(0, 0), "bg_celia_elevator_alpha_60")
image bg_celia_elevator_5 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_elevator.jpg",
(0, 0), "bg_celia_elevator_alpha_50")
image bg_celia_elevator_4 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_elevator.jpg",
(0, 0), "bg_celia_elevator_alpha_40")
image bg_celia_elevator_3 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_elevator.jpg",
(0, 0), "bg_celia_elevator_alpha_30")
image bg_celia_elevator_2 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_elevator.jpg",
(0, 0), "bg_celia_elevator_alpha_20")
image bg_celia_elevator_1 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_elevator.jpg",
(0, 0), "bg_celia_elevator_alpha_10")

image bg_celia_stairs_10:
    "images/bg_celia_stairs.jpg"
image bg_celia_stairs_alpha_90:
    "images/bg_celia_stairs_strain.jpg"
    alpha 0.9
image bg_celia_stairs_alpha_80:
    "images/bg_celia_stairs_strain.jpg"
    alpha 0.8
image bg_celia_stairs_alpha_70:
    "images/bg_celia_stairs_strain.jpg"
    alpha 0.7
image bg_celia_stairs_alpha_60:
    "images/bg_celia_stairs_strain.jpg"
    alpha 0.6
image bg_celia_stairs_alpha_50:
    "images/bg_celia_stairs_strain.jpg"
    alpha 0.5
image bg_celia_stairs_alpha_40:
    "images/bg_celia_stairs_strain.jpg"
    alpha 0.4
image bg_celia_stairs_alpha_30:
    "images/bg_celia_stairs_strain.jpg"
    alpha 0.3
image bg_celia_stairs_alpha_20:
    "images/bg_celia_stairs_strain.jpg"
    alpha 0.2
image bg_celia_stairs_alpha_10:
    "images/bg_celia_stairs_strain.jpg"
    alpha 0.1
image bg_celia_stairs_9 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_stairs.jpg",
(0, 0), "bg_celia_stairs_alpha_90")
image bg_celia_stairs_8 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_stairs.jpg",
(0, 0), "bg_celia_stairs_alpha_80")
image bg_celia_stairs_7 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_stairs.jpg",
(0, 0), "bg_celia_stairs_alpha_70")
image bg_celia_stairs_6 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_stairs.jpg",
(0, 0), "bg_celia_stairs_alpha_60")
image bg_celia_stairs_5 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_stairs.jpg",
(0, 0), "bg_celia_stairs_alpha_50")
image bg_celia_stairs_4 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_stairs.jpg",
(0, 0), "bg_celia_stairs_alpha_40")
image bg_celia_stairs_3 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_stairs.jpg",
(0, 0), "bg_celia_stairs_alpha_30")
image bg_celia_stairs_2 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_stairs.jpg",
(0, 0), "bg_celia_stairs_alpha_20")
image bg_celia_stairs_1 = Composite(
(1280, 720),
(0, 0), "images/bg_celia_stairs.jpg",
(0, 0), "bg_celia_stairs_alpha_10")

image bg_celia_room = ConditionSwitch(
    "sanity >= 100", "images/bg_celia_room.jpg",
    "sanity >= 90", "bg_celia_room_1",
    "sanity >= 80", "bg_celia_room_2",
    "sanity >= 70", "bg_celia_room_3",
    "sanity >= 60", "bg_celia_room_4",
    "sanity >= 50", "bg_celia_room_5",
    "sanity >= 40", "bg_celia_room_6",
    "sanity >= 30", "bg_celia_room_7",
    "sanity >= 20", "bg_celia_room_8",
    "sanity >= 10", "bg_celia_room_9",
    "True", "images/bg_celia_room_strain.jpg")
image bg_celia_office = ConditionSwitch(
    "sanity >= 100", "images/bg_celia_office.jpg",
    "sanity >= 90", "bg_celia_office_1",
    "sanity >= 80", "bg_celia_office_2",
    "sanity >= 70", "bg_celia_office_3",
    "sanity >= 60", "bg_celia_office_4",
    "sanity >= 50", "bg_celia_office_5",
    "sanity >= 40", "bg_celia_office_6",
    "sanity >= 30", "bg_celia_office_7",
    "sanity >= 20", "bg_celia_office_8",
    "sanity >= 10", "bg_celia_office_9",
    "True", "images/bg_celia_office_strain.jpg")
image bg_celia_basement = ConditionSwitch(
    "sanity >= 100", "images/bg_celia_basement.jpg",
    "sanity >= 90", "bg_celia_basement_1",
    "sanity >= 80", "bg_celia_basement_2",
    "sanity >= 70", "bg_celia_basement_3",
    "sanity >= 60", "bg_celia_basement_4",
    "sanity >= 50", "bg_celia_basement_5",
    "sanity >= 40", "bg_celia_basement_6",
    "sanity >= 30", "bg_celia_basement_7",
    "sanity >= 20", "bg_celia_basement_8",
    "sanity >= 10", "bg_celia_basement_9",
    "True", "images/bg_celia_basement_strain.jpg")
image bg_celia_breakroom = ConditionSwitch(
    "sanity >= 100", "images/bg_celia_breakroom.jpg",
    "sanity >= 90", "bg_celia_breakroom_1",
    "sanity >= 80", "bg_celia_breakroom_2",
    "sanity >= 70", "bg_celia_breakroom_3",
    "sanity >= 60", "bg_celia_breakroom_4",
    "sanity >= 50", "bg_celia_breakroom_5",
    "sanity >= 40", "bg_celia_breakroom_6",
    "sanity >= 30", "bg_celia_breakroom_7",
    "sanity >= 20", "bg_celia_breakroom_8",
    "sanity >= 10", "bg_celia_breakroom_9",
    "True", "images/bg_celia_breakroom_strain.jpg")
image bg_celia_elevator = ConditionSwitch(
    "sanity >= 100", "images/bg_celia_elevator.jpg",
    "sanity >= 90", "bg_celia_elevator_1",
    "sanity >= 80", "bg_celia_elevator_2",
    "sanity >= 70", "bg_celia_elevator_3",
    "sanity >= 60", "bg_celia_elevator_4",
    "sanity >= 50", "bg_celia_elevator_5",
    "sanity >= 40", "bg_celia_elevator_6",
    "sanity >= 30", "bg_celia_elevator_7",
    "sanity >= 20", "bg_celia_elevator_8",
    "sanity >= 10", "bg_celia_elevator_9",
    "True", "images/bg_celia_elevator_strain.jpg")
image bg_celia_lounge = ConditionSwitch(
    "sanity >= 100", "images/bg_celia_lounge.jpg",
    "sanity >= 90", "bg_celia_lounge_1",
    "sanity >= 80", "bg_celia_lounge_2",
    "sanity >= 70", "bg_celia_lounge_3",
    "sanity >= 60", "bg_celia_lounge_4",
    "sanity >= 50", "bg_celia_lounge_5",
    "sanity >= 40", "bg_celia_lounge_6",
    "sanity >= 30", "bg_celia_lounge_7",
    "sanity >= 20", "bg_celia_lounge_8",
    "sanity >= 10", "bg_celia_lounge_9",
    "True", "images/bg_celia_lounge_strain.jpg")
image bg_celia_stairs = ConditionSwitch(
    "sanity >= 100", "images/bg_celia_stairs.jpg",
    "sanity >= 90", "bg_celia_stairs_1",
    "sanity >= 80", "bg_celia_stairs_2",
    "sanity >= 70", "bg_celia_stairs_3",
    "sanity >= 60", "bg_celia_stairs_4",
    "sanity >= 50", "bg_celia_stairs_5",
    "sanity >= 40", "bg_celia_stairs_6",
    "sanity >= 30", "bg_celia_stairs_7",
    "sanity >= 20", "bg_celia_stairs_8",
    "sanity >= 10", "bg_celia_stairs_9",
    "True", "images/bg_celia_stairs_strain.jpg")

image bg_endslate:
    "images/bg_redhaze.jpg"
    xalign 0.5
    yalign 0.5
    xanchor 0.5
    yanchor 0.5
    zoom 1.0
    block:
        easeout 0.5 zoom 1.05
        easein 0.5 zoom 1.1
        easeout 0.5 zoom 1.05
        easein 0.5 zoom 1.0
        repeat
image bg_endslate_survival:
    "images/bg_greyhaze.jpg"
    xalign 0.5
    yalign 0.5
    xanchor 0.5
    yanchor 0.5
    zoom 1.0
    block:
        easeout 1 zoom 1.05
        easein 1 zoom 1.1
        easeout 1 zoom 1.05
        easein 1 zoom 1.0
        repeat
image bg_endslate_change:
    "images/bg_river1.jpg" with Dissolve(1, alpha=True)
    pause 1
    "images/bg_river2.jpg" with Dissolve(1, alpha=True)
    pause 1
    "images/bg_river3.jpg" with Dissolve(1, alpha=True)
    pause 1
    repeat
style endslate_title:
    size 130
    color "#FFFFFF"
    font "feral.regular.ttf"
    yoffset -70
style endslate_subtitle:
    color "#fff"
    text_align 0.5
    yoffset 20
style endslate_title_surv is endslate_title:
    color "#800000"
style endslate_subtitle_surv is endslate_subtitle:
    color "#800000"

image effect_health_0:
    "images/effect_health.png"
    alpha 0.0
image effect_health_1:
    "images/effect_health.png"
    alpha 0.2
    ease 2.0 alpha 0.1
    ease 2.0 alpha 0.2
    repeat
image effect_health_2:
    "images/effect_health.png"
    alpha 0.4
    ease 2.0 alpha 0.3
    ease 2.0 alpha 0.4
    repeat
image effect_health_3:
    "images/effect_health.png"
    alpha 0.6
    ease 2.0 alpha 0.5
    ease 2.0 alpha 0.6
    repeat
image effect_health_4:
    "images/effect_health.png"
    alpha 0.8
    ease 2.0 alpha 0.7
    ease 2.0 alpha 0.8
    repeat
image effect_health_5:
    "images/effect_health.png"
    alpha 1.0
    ease 2.0 alpha 0.9
    ease 2.0 alpha 1.0
    repeat

image effect_ice_0:
    "images/effect_ice.png"
    alpha 0.0
image effect_ice_1:
    "images/effect_ice.png"
    alpha 0.2
image effect_ice_2:
    "images/effect_ice.png"
    alpha 0.4
image effect_ice_3:
    "images/effect_ice.png"
    alpha 0.6
image effect_ice_4:
    "images/effect_ice.png"
    alpha 0.8
image effect_ice_5:
    "images/effect_ice.png"
    alpha 1.0

image effect_health = ConditionSwitch(
    "health >= 50", "effect_health_0",
    "health >= 40", "effect_health_1",
    "health >= 30", "effect_health_2",
    "health >= 20", "effect_health_3",
    "health >= 10", "effect_health_4",
    "True", "effect_health_5")
image effect_ice = ConditionSwitch(
    "temp >= 25", "effect_ice_0",
    "temp >= 20", "effect_ice_1",
    "temp >= 15", "effect_ice_2",
    "temp >= 10", "effect_ice_3",
    "temp >= 5", "effect_ice_4",
    "True", "effect_ice_5")

screen effect_health():
    add "effect_health"
screen effect_ice():
    add "effect_ice"

image gyg_gore:
    "images/gyg_gore.png"
    xanchor 0.5
    yanchor 0.5
    easeout 0.5 zoom 1.00
    easein 0.5 zoom 1.05
    repeat


image cg_derek_demon = "images/cg_derek_demon.jpg"
image cg_mason_snow = "images/cg_mason_snow.jpg"
image cg_celia_stream = "gui/overlay/game_menu_black.png"
image cg_derek_machete_sister = "images/cg_derek_machete_sister.jpg"

image bg_derek_camp_thumbnail:
    "images/bg_derek_camp.jpg"
    zoom 0.2
image bg_derek_hill_thumbnail:
    "images/bg_derek_hill.jpg"
    zoom 0.2
image bg_derek_fissure_thumbnail:
    "images/bg_derek_fissure.jpg"
    zoom 0.2
image bg_derek_desert_thumbnail:
    "images/bg_derek_desert.jpg"
    zoom 0.2
image bg_derek_deepdesert_thumbnail:
    "images/bg_derek_deepdesert.jpg"
    zoom 0.2
image bg_derek_cave_thumbnail:
    "images/bg_derek_cave.jpg"
    zoom 0.2
image bg_derek_theritz_thumbnail:
    "images/bg_derek_theritz.jpg"
    zoom 0.2
image bg_mason_meadow_thumbnail:
    "images/bg_mason_meadow.jpg"
    zoom 0.2
image bg_mason_thicket_thumbnail:
    "images/bg_mason_thicket.jpg"
    zoom 0.2
image bg_mason_waterfall_thumbnail:
    "images/bg_mason_waterfall.jpg"
    zoom 0.2
image bg_mason_talltree_thumbnail:
    "images/bg_mason_talltree.jpg"
    zoom 0.2
image bg_mason_cabin_thumbnail:
    "images/bg_mason_cabin.jpg"
    zoom 0.2
image bg_mason_incabin_thumbnail:
    "images/bg_mason_incabin.jpg"
    zoom 0.2
image bg_mason_swamp_thumbnail:
    "images/bg_mason_swamp.jpg"
    zoom 0.2
image bg_celia_room_thumbnail:
    "images/bg_celia_room.jpg"
    zoom 0.2
    crop (0,0,1280,720)
image bg_celia_room_smaller:
    "images/bg_celia_room.jpg"
    zoom 0.67
image bg_celia_lounge_thumbnail:
    "images/bg_celia_lounge.jpg"
    zoom 0.2
image bg_celia_elevator_thumbnail:
    "images/bg_celia_elevator.jpg"
    zoom 0.2
image bg_celia_office_thumbnail:
    "images/bg_celia_office.jpg"
    zoom 0.2
image bg_celia_breakroom_thumbnail:
    "images/bg_celia_breakroom.jpg"
    zoom 0.2
image bg_celia_stairs_thumbnail:
    "images/bg_celia_stairs.jpg"
    zoom 0.2
image bg_celia_basement_thumbnail:
    "images/bg_celia_basement.jpg"
    zoom 0.2


image cg_celia_basement_cage_thumbnail:
    "images/cg_celia_basement_cage.jpg"
    zoom 0.2
image cg_celia_ceiling_gun_thumbnail:
    "images/cg_celia_ceiling_gun.jpg"
    zoom 0.2
image cg_celia_donuts_thumbnail:
    "images/cg_celia_donuts.jpg"
    zoom 0.2
image cg_celia_elevator_1_thumbnail:
    "images/cg_celia_elevator_1.jpg"
    zoom 0.2
image cg_celia_elevator_2_thumbnail:
    "images/cg_celia_elevator_2.jpg"
    zoom 0.2
image cg_celia_elevator_3_thumbnail:
    "images/cg_celia_elevator_3.jpg"
    zoom 0.2
image cg_celia_escape_thumbnail:
    "images/cg_celia_escape_2.jpg"
    zoom 0.2
image cg_celia_fallen_thumbnail:
    "images/cg_celia_fallen.jpg"
    zoom 0.2
image cg_celia_glass_thumbnail:
    "images/cg_celia_glass_2.jpg"
    zoom 0.2
image cg_celia_harold_choked_thumbnail:
    "images/cg_celia_harold_choked_2.jpg"
    zoom 0.2
image cg_celia_harold_kill_1_thumbnail:
    "images/cg_celia_harold_kill_1.jpg"
    zoom 0.2
image cg_celia_harold_kill_2_thumbnail:
    "images/cg_celia_harold_kill_2.jpg"
    zoom 0.2
image cg_celia_harold_shot_thumbnail:
    "images/cg_celia_harold_shot.jpg"
    zoom 0.2
image cg_celia_harold_tripped_thumbnail:
    "images/cg_celia_harold_tripped.jpg"
    zoom 0.2
image cg_celia_leave_thumbnail:
    "images/cg_celia_leave_1.jpg"
    zoom 0.2
image cg_celia_lounge_thumbnail:
    "images/cg_celia_lounge.jpg"
    zoom 0.2
image cg_celia_poisoned_thumbnail:
    "images/cg_celia_poisoned.jpg"
    zoom 0.2
image cg_celia_poisoned2_thumbnail:
    "images/cg_celia_poisoned2.jpg"
    zoom 0.2
image cg_celia_roomcorner_thumbnail:
    "images/cg_celia_roomcorner.jpg"
    zoom 0.2
image cg_celia_slitharold_thumbnail:
    "images/cg_celia_slitharold_1.jpg"
    zoom 0.2
image cg_celia_straddle_bag_thumbnail:
    "images/cg_celia_straddle_bag.jpg"
    zoom 0.2
image cg_celia_straddle_knife_thumbnail:
    "images/cg_celia_straddle_knife2.jpg"
    zoom 0.2
image cg_celia_straddle_thumbnail:
    "images/cg_celia_straddle.jpg"
    zoom 0.2
image cg_celia_strip_gun_thumbnail:
    "images/cg_celia_strip_gun.jpg"
    zoom 0.2
image cg_celia_taserbattle_1_thumbnail:
    "images/cg_celia_taserbattle_1.jpg"
    zoom 0.2
image cg_celia_taserbattle_2_thumbnail:
    "images/cg_celia_taserbattle_3.jpg"
    zoom 0.2
image cg_celia_whip1_thumbnail:
    "images/cg_celia_whip1.jpg"
    zoom 0.2
image cg_celia_whip2_thumbnail:
    "images/cg_celia_whip2.jpg"
    zoom 0.2
image cg_celia_wirekill_1_thumbnail:
    "images/cg_celia_wirekill_1.jpg"
    zoom 0.2
image cg_celia_wirekill_2_thumbnail:
    "images/cg_celia_wirekill_2.jpg"
    zoom 0.2

image cg_derek_angrystab_thumbnail:
    "images/cg_derek_angrystab.jpg"
    zoom 0.2
image cg_derek_bat_thumbnail:
    "images/cg_derek_bat.jpg"
    zoom 0.2
image cg_derek_cave_thumbnail:
    "images/cg_derek_cave_kd_dknife.jpg"
    zoom 0.2
image cg_derek_cave_sacrifice_thumbnail:
    "images/cg_derek_cave_sacrifice.jpg"
    zoom 0.2
image cg_derek_cave_guts_thumbnail:
    "images/cg_derek_cave_guts.jpg"
    zoom 0.2
image cg_derek_cham_thumbnail:
    "images/cg_derek_cham.jpg"
    zoom 0.2
image cg_derek_crouchknife_thumbnail:
    "images/cg_derek_crouchknife_angry.jpg"
    zoom 0.2
image cg_derek_deadtom_thumbnail:
    "images/cg_derek_deadtom.jpg"
    zoom 0.2
image cg_derek_demon_thumbnail:
    "images/cg_derek_demon.jpg"
    zoom 0.2
image cg_derek_dragonstab_thumbnail:
    "images/cg_derek_dragonstab.jpg"
    zoom 0.2
image cg_derek_favour_thumbnail:
    "images/cg_derek_favour2.jpg"
    zoom 0.2
image cg_derek_fireworks_crouch_thumbnail:
    "images/cg_derek_fireworks_crouch.jpg"
    zoom 0.2
image cg_derek_fireworks_drop_thumbnail:
    "images/cg_derek_fireworks_drop.jpg"
    zoom 0.2
image cg_derek_fireworks_gag1_thumbnail:
    "images/cg_derek_fireworks_gag1.jpg"
    zoom 0.2
image cg_derek_fireworks_gerb_thumbnail:
    "images/cg_derek_fireworks_gerb.jpg"
    zoom 0.2
image cg_derek_firstblood_1_thumbnail:
    "images/cg_derek_firstblood_1.jpg"
    zoom 0.2
image cg_derek_firstblood_2_thumbnail:
    "images/cg_derek_firstblood_2.jpg"
    zoom 0.2
image cg_derek_helptom_thumbnail:
    "images/cg_derek_helptom.jpg"
    zoom 0.2
image cg_derek_jack_choke_thumbnail:
    "images/cg_derek_jack_choke1.jpg"
    zoom 0.2
image cg_derek_jack_knuckles_thumbnail:
    "images/cg_derek_jack_knuckles.jpg"
    zoom 0.2
image cg_derek_jackknife_close_thumbnail:
    "images/cg_derek_jackknife_close.jpg"
    zoom 0.2
image cg_derek_jackknife_pin_thumbnail:
    "images/cg_derek_jackknife_pin.jpg"
    zoom 0.2
image cg_derek_jackknife_thumbnail:
    "images/cg_derek_jackknife.jpg"
    zoom 0.2
image cg_derek_jackmask_thumbnail:
    "images/cg_derek_jackmask.jpg"
    zoom 0.2
image cg_derek_kdgut1_thumbnail:
    "images/cg_derek_kdgut1.jpg"
    zoom 0.2
image cg_derek_kdgut2_thumbnail:
    "images/cg_derek_kdgut2.jpg"
    zoom 0.2
image cg_derek_kdloom_thumbnail:
    "images/cg_derek_kdloom.jpg"
    zoom 0.2
image cg_derek_loveanddeath_thumbnail:
    "images/cg_derek_loveanddeath.jpg"
    zoom 0.2
image cg_derek_loveanddeath2_thumbnail:
    "images/cg_derek_loveanddeath2.jpg"
    zoom 0.2
image cg_derek_machete_sister_thumbnail:
    "images/cg_derek_machete_sister.jpg"
    zoom 0.2
image cg_derek_machete_thumbnail:
    "images/cg_derek_machete.jpg"
    zoom 0.2
image cg_derek_nightsky_machete1_thumbnail:
    "images/cg_derek_nightsky_machete1.jpg"
    zoom 0.2
image cg_derek_nightsky_machete2_thumbnail:
    "images/cg_derek_nightsky_machete2.jpg"
    zoom 0.2
image cg_derek_nightsky_thumbnail:
    "images/cg_derek_nightsky.jpg"
    zoom 0.2
image cg_derek_quadbat_thumbnail:
    "images/cg_derek_quadbat.jpg"
    zoom 0.2
image cg_derek_sand_thumbnail:
    "images/cg_derek_sand.jpg"
    zoom 0.2
image cg_derek_showdown_attempted_thumbnail:
    "cg_derek_showdown_attempted.jpg"
    zoom 0.2
image cg_derek_showdown_backstab_thumbnail:
    "cg_derek_showdown_backstab.jpg"
    zoom 0.2
image cg_derek_showdown_baddog_thumbnail:
    "cg_derek_showdown_baddog.jpg"
    zoom 0.2
image cg_derek_showdown_standover_thumbnail:
    "cg_derek_showdown_standover.jpg"
    zoom 0.2
image cg_derek_showdown_close_thumbnail:
    "cg_derek_showdown_close.jpg"
    zoom 0.2
image cg_derek_showdown_closeup_thumbnail:
    "cg_derek_showdown_closeup.jpg"
    zoom 0.2
image cg_derek_showdown_far_thumbnail:
    "cg_derek_showdown_far.jpg"
    zoom 0.2
image cg_derek_showdown_jackstab1_thumbnail:
    "cg_derek_showdown_jackstab1.jpg"
    zoom 0.2
image cg_derek_showdown_jackstab2_thumbnail:
    "cg_derek_showdown_jackstab2.jpg"
    zoom 0.2
image cg_derek_showdown_jackstomp_thumbnail:
    "cg_derek_showdown_jackstomp.jpg"
    zoom 0.2
image cg_derek_showdown_jaqdown_thumbnail:
    "cg_derek_showdown_jaqdown.jpg"
    zoom 0.2
image cg_derek_showdown_machetejack_thumbnail:
    "cg_derek_showdown_machetejack.jpg"
    zoom 0.2
image cg_derek_showdown_neck_thumbnail:
    "cg_derek_showdown_neck.jpg"
    zoom 0.2
image cg_derek_stabbed_thumbnail:
    "cg_derek_stabbed.jpg"
    zoom 0.2
    crop (0,0,1280,720)
image cg_derek_stabbed_smaller:
    "cg_derek_stabbed.jpg"
    yalign 0.0
    zoom 0.72
image cg_derek_straddle_thumbnail:
    "cg_derek_straddle1.jpg"
    zoom 0.2
image cg_derek_theritz_thumbnail:
    "cg_derek_theritz.jpg"
    zoom 0.2
image cg_derek_victims_thumbnail:
    "cg_derek_victims.jpg"
    zoom 0.2
image cg_derek_vsmachete1_thumbnail:
    "cg_derek_vsmachete1.jpg"
    zoom 0.2
image cg_derek_vsmachete_hush_thumbnail:
    "cg_derek_vsmachete4.jpg"
    zoom 0.2
image cg_derek_vsmachete5_thumbnail:
    "cg_derek_vsmachete5.jpg"
    zoom 0.2
image cg_derek_watermachete1_thumbnail:
    "cg_derek_watermachete1.jpg"
    zoom 0.2
image cg_derek_watermachete2_thumbnail:
    "cg_derek_watermachete2.jpg"
    zoom 0.2
image cg_derek_throat_thumbnail:
    "cg_derek_throat.jpg"
    zoom 0.2

image cg_mason_armbolt_thumbnail:
    "images/cg_mason_armbolt2.jpg"
    zoom 0.2
image cg_mason_clouds_thumbnail:
    "images/cg_mason_clouds.jpg"
    zoom 0.2
image cg_mason_bear_thumbnail:
    "images/cg_mason_bear2.jpg"
    zoom 0.2
image cg_mason_beartrapped_gore_thumbnail:
    "images/cg_mason_beartrapped_gore.jpg"
    zoom 0.2
image cg_mason_beartrapped_looming_thumbnail:
    "images/cg_mason_beartrapped_loomingknife.jpg"
    zoom 0.2
image cg_mason_beartrapped_crouch_thumbnail:
    "images/cg_mason_beartrapped_crouch.jpg"
    zoom 0.2
image cg_mason_beartrapped_thumbnail:
    "images/cg_mason_beartrapped_day.jpg"
    zoom 0.2
image cg_mason_bleedout_thumbnail:
    "images/cg_mason_bleedout.jpg"
    zoom 0.2
image cg_mason_cabindoor_thumbnail:
    "images/cg_mason_cabindoor.jpg"
    zoom 0.2
image cg_mason_cabinfire_thumbnail:
    "images/cg_mason_cabinfire.jpg"
    zoom 0.2
image cg_mason_campfire_thumbnail:
    "images/cg_mason_campfire.jpg"
    zoom 0.2
image cg_mason_carry_thumbnail:
    "images/cg_mason_carry.jpg"
    zoom 0.2
image cg_mason_dead_thumbnail:
    "images/cg_mason_dead.jpg"
    zoom 0.2
image cg_mason_deer_thumbnail:
    "images/cg_mason_deer2.jpg"
    zoom 0.2
image cg_mason_gutting1_thumbnail:
    "images/cg_mason_gutting1.jpg"
    zoom 0.2
image cg_mason_gutting2_thumbnail:
    "images/cg_mason_gutting2.jpg"
    zoom 0.2
image cg_mason_kill_thumbnail:
    "images/cg_mason_kill1.jpg"
    zoom 0.2
image cg_mason_log_thumbnail:
    "images/cg_mason_log.jpg"
    zoom 0.2
image cg_mason_snare_thumbnail:
    "images/cg_mason_snare_blood.jpg"
    zoom 0.2
image cg_mason_snow_thumbnail:
    "images/cg_mason_snow.jpg"
    zoom 0.2
image cg_mason_stump_thumbnail:
    "images/cg_mason_stump.jpg"
    zoom 0.2
image cg_mason_trapped_thumbnail:
    "images/cg_mason_trapped.jpg"
    zoom 0.2
image cg_mason_treeview_thumbnail:
    "images/cg_mason_treeview_day.jpg"
    zoom 0.2
image cg_mason_upsidedown_thumbnail:
    "images/cg_mason_upsidedown2.jpg"
    zoom 0.2
image cg_mason_wall_thumbnail:
    "images/cg_mason_wall.jpg"
    zoom 0.2
    crop (0,0,1280,720)
image cg_mason_baneberry_drown_thumbnail:
    "images/cg_mason_baneberry_drown.jpg"
    zoom 0.2

image cg_celia_straddle_sex_thumbnail:
    "images/cg_celia_straddle_sex.jpg"
    zoom 0.2
image cg_celia_straddle_sex2_thumbnail:
    "images/cg_celia_straddle_sex2.jpg"
    zoom 0.2
image cg_derek_favoursex_thumbnail:
    "images/cg_derek_favoursex.jpg"
    zoom 0.2
image cg_derek_fireworks_gag2_thumbnail:
    "images/cg_derek_fireworks_gag2.jpg"
    zoom 0.2
image cg_derek_missionary_thumbnail:
    "images/cg_derek_missionary.jpg"
    zoom 0.2
image cg_mason_x_upsidedown_thumbnail:
    "images/cg_mason_x_upsidedown.jpg"
    zoom 0.2

label splashscreen:
    call screen bg_splash
    $ renpy.pause(hard=True)
    label keepgoing:
    return

label start:
    default phase = "event"
    default gamepath = "start"
    default meme_mode = False
    default player_name = ""
    default event_derek_map_activation = 0
    default health = 100
    default stat_health = 0
    default sanity = 100
    default stat_sanity = 0
    default temp = 50
    default stat_temp = 0
    default energy = 24
    default stat_energy = 0
    default food = 24
    default stat_food = 0
    default thirst = 72
    default inventory = list(())
    default mason_name = "???"
    default derek_name = "???"
    default celia_name = "???"
    default lich_name = "???"
    default harold_name = "???"
    default jack_name = "???"
    default komodo_name = "???"
    default dragon_name = "???"
    default machete_name = "???"
    default jaq_name = "???"
    default tom_name = "???"
    default rich_name = "???"
    default cham_name = "???"
    default demon_name = "???"
    default fox_name = "???"
    default blue_voice = "Smooth Voice"
    default red_voice = "Sharp Voice"
    default green_voice = "Gravelly Voice"
    default map_location = "Unknown"
    default hours = 12
    default hour_rotation = 90
    default arrivedby = "idle"
    default total_hours = 12
    default sleep = 0
    default grace_period = 0
    default c_auction_love = 0
    default d_auction_love = 0
    default m_auction_love = 0
    default map_mason_house_discover = False
    default location_temp = "warm"
    default mason_location = "house"
    default map_location_cabin = "outside"
    default encumbered = 0
    default wound = 0
    default map_enabled = False
    default map_discovery_meadow = False
    default map_discovery_thicket = False
    default map_discovery_waterfall = False
    default map_discovery_talltree = False
    default map_discovery_house = False
    default map_discovery_swamp = False
    default event_mason_sanity_1 = 0
    default event_mason_sanity_2 = 0
    default event_mason_sanity_3 = 0
    default event_mason_sanity_4 = 0
    default event_mason_sanity_5 = 0
    default event_mason_sound_1 = 0
    default event_mason_sound_2 = 0
    default event_mason_sound_3 = 0
    default event_mason_1 = 0
    default event_mason_discoverhouse = 0
    default event_mason_discoverswamp = 0
    default event_mason_findcabin = 0
    default event_mason_findincabin = 0
    default event_mason_returnswamp = 0
    default event_mason_nightmare = 0
    default event_mason_findbones = 0
    default event_mason_mapswamp = 0
    default event_mason_findberries = 0
    default event_mason_findfish = 0
    default event_mason_offerbones = 0
    default event_mason_discover_snare = 0
    default event_mason_snare_dismantle = 0
    default event_mason_snare_deer = 0
    default event_mason_discover_beartrap = 0
    default event_mason_crossbow_1 = 0
    default event_mason_crossbow_2 = 0
    default event_mason_crossbow_3 = 0
    default event_mason_pepper_1 = 0
    default event_mason_pepper_2 = 0
    default event_mason_arrivetalltree = 0
    default event_mason_arrivewaterfall = 0
    default fire = 0
    default celia_love = 0
    default celia_bound = 1
    default event_celia_try_office = 0
    default event_celia_try_elevator = 0
    default event_celia_discover_basement = 0
    default event_celia_harrison = 0
    default event_celia_spacer = 0
    default event_celia_donuts = 0
    default event_celia_room_door_locked = 1
    default celia_desk_escape_attempt = 0
    default celia_room_idling = 0
    default celia_room_window_smashed = 0
    default event_celia_room_key_attempt = 0
    default item_basement_key_search = 0
    default event_office_search = 0
    default event_celia_enter_lounge = 0
    default event_celia_enter_office = 0
    default event_celia_enter_basement = 0
    default event_celia_unlock_basement = 0
    default event_celia_enter_breakroom = 0
    default event_celia_basement_caught = 0
    default event_celia_brandy_poisoned = 0
    default event_celia_soda_get = 0
    default celia_office_locked = 1
    default celia_basement_locked = 1
    default celia_brandy = 0
    default event_celia_headache = 0
    default event_celia_sanity_1 = 0
    default event_celia_sanity_2 = 0
    default event_celia_sound_1 = 0
    default event_celia_sound_2 = 0
    default event_celia_sound_3 = 0
    default event_celia_complain = 0
    default event_celia_endgame = 0
    default event_celia_set_trap = 0
    default event_celia_tased = 0
    default event_celia_starving = 0
    default event_celia_findpin = 0
    default event_derek_hot_1 = 0
    default event_derek_hot_2 = 0
    default event_derek_hot_3 = 0
    default event_derek_thirst_1 = 0
    default event_derek_thirst_2 = 0
    default event_derek_thirst_3 = 0
    default event_derek_sanity_1 = 0
    default event_derek_sanity_2 = 0
    default event_derek_sound_1 = 0
    default event_derek_sound_2 = 0
    default event_derek_sound_3 = 0
    default event_derek_encounter_1 = 0
    default event_derek_encounter_2 = 0
    default event_derek_cave_discovery = 0
    default event_derek_search_fissure = 0
    default event_derek_search_cave = 0
    default event_derek_searchcamp = 0
    default event_derek_jack_countdown = 0
    default event_derek_poison_planted = 0
    default event_derek_derekvsmachete = 0
    default event_derek_first_visit_is_free = 0
    default event_derek_get_map = 0
    default event_derek_talk_tom = 0
    default event_derek_talk_jaq = 0
    default event_derek_talk_rich = 0
    default event_derek_jaq_knife = 0
    default event_derek_save_rich = 0
    default event_derek_jack_jaq = 0
    default event_derek_endgame = 0
    default event_derek_endgame_missed = 0
    default event_derek_tomleave = 0
    default machete_unlock = 0
    default derek_status = "Fine"
    default derek_location = "Camp"
    default tom_location = "Peril"
    default jaq_location = "Peril"
    default rich_location = "Peril"
    default fox_love = 0
    default chat_love = 0
    default show_firstquestion = 0
    default show_pollstat_1 = 0
    default show_pollstat_2 = 0
    default show_pollstat_3 = 0
    default show_pollstat_4 = 0
    default show_votepos = 5
    default show_voteneg = 5
    default show_event_dressup = 0
    default show_virgin_question = 0
    default show_silence = 0
    default show_rensdecision = 0
    default show_design = "diamond"
    default sexcontent_cg = "yes"

    init python:
        def limit_hours():
            try:
                if store.hours > 24:
                    store.hours = store.hours - 24
            except:
                pass

        config.python_callbacks.append(limit_hours)
        def rotate_hours():
            try:
                if store.hours:
                    store.hour_rotation = store.hours*15
            except:
                pass
        config.python_callbacks.append(rotate_hours)
    init python:
        def check_stats():
            try:
                if store.stat_health != 0:
                    renpy.show_screen("status_update_health",store.stat_health)
                    if store.stat_health < 0:
                        renpy.show("effect_injury")
                    store.health = store.health + store.stat_health
                    store.stat_health = 0
                    if store.health > 100:
                        store.health = 100
                    if store.health < 0:
                        store.health = 0
                if store.stat_sanity != 0:
                    renpy.show_screen("status_update_sanity",store.stat_sanity)
                    store.sanity = store.sanity + store.stat_sanity
                    store.stat_sanity = 0
                    if store.sanity > 100:
                        store.sanity = 100
                    if store.sanity < 0:
                        store.sanity = 0
                if store.stat_energy != 0:
                    renpy.show_screen("status_update_energy",store.stat_energy)
                    store.energy = store.energy + store.stat_energy
                    store.stat_energy = 0
                    if store.energy > 24:
                        store.energy = 24
                    if store.energy < 0:
                        store.energy = 0
                if store.stat_food != 0:
                    renpy.show_screen("status_update_food",store.stat_food)
                    store.food = store.food + store.stat_food
                    store.stat_food = 0
                    if store.food > 24:
                        store.food = 24
                    if store.food < 0:
                        store.food = 0
                if store.stat_temp > 0:
                    renpy.show_screen("status_update_temp_increase",store.stat_temp)
                    store.temp = store.temp + store.stat_temp
                    store.stat_temp = 0
                    if store.temp > 100:
                        store.temp = 100
                if store.stat_temp < 0:
                    renpy.show_screen("status_update_temp_decrease",store.stat_temp)
                    store.temp = store.temp + store.stat_temp
                    store.stat_temp = 0
                    if store.temp < 0:
                        store.temp = 0
            except:
                pass
        config.python_callbacks.append(check_stats)
    scene black with glitchdissolve
    call screen choosename
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Anon"
label start_sexual:
    scene black with dissolve
    $ pronoun = "they"
    $ sexcontent = "no"
    call screen startgame

    if pronoun == "he":
        $ pp_sub= "he"
        $ pp_obj= "him"
        $ pp_sub_c= "He"
        $ pp_obj_c= "Him"
        $ pp_pos= "his"
        $ pp_pos_c= "His"
        $ pp_is= "he's"
        $ pp_is_c= "He's"
    if pronoun == "she":
        $ pp_sub= "she"
        $ pp_obj= "her"
        $ pp_sub_c= "She"
        $ pp_obj_c= "Her"
        $ pp_pos= "her"
        $ pp_pos_c= "Her"
        $ pp_is= "she's"
        $ pp_is_c= "She's"
    if pronoun == "they":
        $ pp_sub= "they"
        $ pp_obj= "them"
        $ pp_sub_c= "They"
        $ pp_obj_c= "Them"
        $ pp_pos= "their"
        $ pp_pos_c= "Their"
        $ pp_is= "they're"
        $ pp_is_c= "They're"

label start_intro:
    if meme_mode:
        $ red_voice = "Irritating Voice"
        if achievement.has("ach_lord_of_memes") != True:
            $ persistent.ach_lord_of_memes = True
            $ achievement.grant("ach_lord_of_memes")
            init:
                $ achievement.register("ach_lord_of_memes")
                $ achievement.sync()
                $ renpy.save_persistent()
                if persistent.ach_lord_of_memes == True and achievement.has("ach_lord_of_memes") != True:
                    $ achievement.grant("ach_lord_of_memes")
                    $ achievement.register("ach_lord_of_memes")
                    $ achievement.sync()
    show screen effect_health
    show screen effect_ice
    stop music fadeout 1.0
    play ambient "music/ambient_drone_intermittent.ogg" fadein 1.0
    scene black with glitchdissolve
    show cg_burlap_under at confused_bobbing
    show cg_burlap_over
    unknown "Hey."
    unknown "[pp_is_c] waking up."
    pause(1.0)
    unknown "Oh... just a sec."
    "Something was pressed against my face."
    "I barely had time to register the sound of a car's engine before I passed out again."
    scene black with eyedissolve
    pause(1.0)
    show bg_auction:
        yalign 1.0
        alpha 0.0
        easein_expo 1.5 yalign 0.0 alpha 1.0
    "Where..."
    p "Woah!"
    p "W-where am I?"
    "I looked down, horrified to see only shackles."
    "I couldn't see anyone else."
    p "Hello?"
    show window_red_flash
    show window_blue_flash
    show window_green_flash
    stop ambient fadeout 1.0
    play music "music/game_show.ogg"
    "Suddenly, a cheerful voice rang through speakers placed around the room."
    announcer "Good evening and welcome!"
    announcer "Ladies and Gentlemen, have I got a treat for you!"
    announcer "[pp_is_c] fresh, healthy, and alert. I'm sure [pp_sub]'ll be versatile enough to fulfill any of your... needs."
    "The voice chuckled softly."
    announcer "Now I'm sure you all know the drill; I'll start asking questions, and you lovely folks can begin bidding at any time!"
    show window_red_flash
    redwindow "Get on with it!"
    show window_blue_flash
    bluewindow "Shut up unless you're bidding!"
    show window_red_flash
    redwindow "Heh, you sound like a hag!"
    show window_blue_flash
    bluewindow "You little shit!! I bet you can't even afford anything here! Get back to-"
    announcer "Now, now..."
    announcer "Shouldn't we save our passion for the main event?"
    "For a moment, the voices went silent."
    announcer "Shall we ask our item some questions and begin the bidding?"
    show window_green_flash
    greenwindow "... Yes, please."
    announcer "Haha! Excellent!"
    announcer "Let's begin!"
    $ price = 100
    $ bidder = "green"
    if meme_mode:
        $ mememoney = "¢"
    elif True:
        $ mememoney = ""
    announcer "We'll start the bidding at 100."
    "I wondered briefly about what it was even a hundred of."
    "I decided I didn't want to know what I was 'worth'."
    announcer "Here's our first question!"
    announcer "What are you doing here?"
    menu:
        "I waited for a moment, realizing he was addressing me."
        "\"I don't know..?\"" if True:
            "Am I supposed to know what's going on?"
            $ price += 10
            show window_blue_flash
            bluewindow "[price][mememoney]."
            $ c_auction_love += 10
            $ bidder = "blue"
        "\"How the hell should I know!?\"" if True:

            $ price += 10
            show window_green_flash
            greenwindow "[price][mememoney]."
            $ m_auction_love += 10
            $ bidder = "green"

        "\"Getting my ass sold, what's it look like?\"" if meme_mode == True:
            $ price += 20
            show window_green_flash
            greenwindow "[price][mememoney]."
            $ d_auction_love += 10
            $ bidder = "green"
            announcer "Hahaha! The enthusiasm!"
        "-Refuse to answer-" if True:

            "I don't know who these people are..."
            "But I'm not playing along with this."
            $ price += 10
            show window_green_flash
            greenwindow "[price][mememoney]."
            $ m_auction_love += 10
            $ bidder = "green"
            "I grimaced."
            "Apparently even doing nothing seemed to appeal to them..."

    announcer "Wonderful!"
    announcer "Now... do you consider yourself to be athletic?"
    menu:
        " "
        "-Say yes-" if True:
            "I cleared my throat and tried to sound more confident."
            p "... Yes."
            $ m_auction_love += 30
            if bidder != "green":
                $ price += 20
                show window_green_flash
                greenwindow "[price][mememoney]."
                $ bidder = "green"
            elif True:
                "..."
        "-Say no-" if True:

            $ c_auction_love += 20
            $ d_auction_love += 10
            "There was no point in lying..."
            p "Not really..."
            if bidder != "blue":
                $ price += 20
                show window_blue_flash
                bluewindow "[price][mememoney]."
                $ bidder = "blue"
            elif True:
                "..."
        "-Say you're not sure-" if True:

            $ c_auction_love += 20
            $ d_auction_love += 20
            p "Kind of..? Uhh..."
            if bidder != "blue":
                $ price += 10
                show window_blue_flash
                bluewindow "[price][mememoney]."
                $ price += 10
                show window_red_flash
                redwindow "[price][mememoney]!"
                $ bidder = "red"
            elif True:
                "..."
        "-Refuse to answer-" if True:

            "I stayed silent."
            if bidder != "green":
                $ price += 10
                show window_green_flash
                greenwindow "...[price][mememoney]."
                $ bidder = "green"
            elif True:
                "..."
    announcer "Here's a fun one..."
    announcer "Are you scared?"
    menu:
        " "
        "-Say no-" if True:
            $ d_auction_love += 10
            $ m_auction_love += 30
            "What the hell kind of questions are these!?"
            "I made sure to speak clearly and keep my back straight."
            p "No. I'm not scared of you people."
            if bidder != "green":
                $ price += 30
                show window_green_flash
                greenwindow "[price][mememoney]."
                $ bidder = "green"
            elif True:
                "..."
        "-Say yes-" if True:
            $ c_auction_love += 10
            $ d_auction_love += 30
            "What the hell kind of questions are these!?"
            "I doubted that I could hide the shaking in my legs anyway."
            p "Fine... yeah..."
            if bidder != "blue":
                $ price += 10
                show window_blue_flash
                bluewindow "[price][mememoney]."
                $ price += 30
                show window_red_flash
                redwindow "[price][mememoney]!"
                show window_blue_flash
                bluewindow "Hmph."
                $ bidder = "red"
            elif bidder != "red":
                $ price += 20
                show window_red_flash
                redwindow "[price][mememoney]!"
                $ bidder = "red"
            elif True:
                "..."
        "-Refuse to answer-" if True:

            $ m_auction_love += 10
            "What the hell kind of questions are these!?"
            "I glowered at the windows and kept my mouth shut."
            if bidder != "green":
                $ price += 10
                show window_green_flash
                greenwindow "[price][mememoney]."
                $ bidder = "green"
            elif True:
                "..."
    announcer "Heh, okay, let's see..."
    announcer "How much money do you make?"
    menu:
        " "
        "\"I make plenty!\"" if True:
            $ c_auction_love += 10
            if bidder != "blue":
                $ price += 50
                show window_blue_flash
                bluewindow "[price][mememoney]."
                $ bidder = "blue"
            elif True:
                "..."
        "\"I get by...\"" if True:
            $ m_auction_love += 10
            $ d_auction_love += 10
            if bidder != "green":
                $ price += 10
                show window_green_flash
                greenwindow "[price][mememoney]."
                $ bidder = "green"
            elif True:
                "..."
        "\"I'm practically broke.\"" if True:

            $ d_auction_love += 30
            if bidder != "red":
                $ price += 10
                show window_red_flash
                redwindow "Ha! [price][mememoney]!"
                $ bidder = "red"
            elif True:
                "..."
        "-Refuse to answer-" if True:

            "As if I would answer that."
            "The room stayed silent as I gritted my teeth."
    announcer "Good, good!"
    announcer "Okay..."
    announcer "How well do you follow instructions?"
    menu:
        " "
        "\"I'm not answering any of YOUR 'instructions'!\"" if True:
            $ m_auction_love += 10
            if bidder != "green":
                $ price += 10
                show window_green_flash
                greenwindow "[price][mememoney]."
                $ bidder = "green"
            elif True:
                "..."
        "\"I... I don't know?\"" if True:
            $ d_auction_love += 10
            if bidder != "red":
                $ price += 10
                show window_red_flash
                redwindow "[price][mememoney]!"
                $ bidder = "red"
            elif True:
                "..."
        "\"I can follow instructions just fine...\"" if True:
            $ c_auction_love += 30
            if bidder != "blue":
                $ price += 10
                show window_blue_flash
                bluewindow "Oh~ [price][mememoney]."
                $ bidder = "blue"
            elif True:
                "..."
        "-Refuse to answer-" if True:
            if bidder != "green":
                $ price += 10
                show window_green_flash
                greenwindow "[price][mememoney]."
                $ bidder = "green"
            elif True:
                "..."
            announcer "So defiant~!"
            announcer "Haha! But I'm sure you all have a plan for dealing with that, don't you?"
    if sexcontent != "no":
        announcer "Oh... this one's interesting."
        announcer "Are you a virgin?"
        menu:
            " "
            "-Say yes-" if True:
                $ show_virgin_question = 1
                $ d_auction_love += 50
                $ c_auction_love += 10
                if bidder != "red":
                    $ price += 50
                    show window_red_flash
                    redwindow "..."
                    redwindow "[price][mememoney]."
                    show window_blue_flash
                    bluewindow "Ugh. You're disgusting."
                    show window_red_flash
                    redwindow "Shove a sock in it bitch!"
                    $ bidder = "red"
                elif True:
                    "..."
            "-Say no-" if True:

                if bidder != "blue":
                    $ price += 10
                    show window_blue_flash
                    bluewindow "... [price][mememoney]."
                    $ bidder = "blue"
                elif True:
                    "..."

            "\"None of your goddamned business!\"" if meme_mode:
                $ m_auction_love += 30
                $ d_auction_love += 10
                if bidder != "red":
                    $ price += 10
                    show window_red_flash
                    redwindow "[price][mememoney]!"
                    $ price += 10
                    show window_green_flash
                    greenwindow "Hm... [price][mememoney]."
                    $ bidder = "green"
                elif True:
                    "..."
                announcer "Oh my~"
                announcer "It seems my clients beg to differ..."
                "The announcer laughed."
            "-Refuse to answer-" if True:

                $ m_auction_love += 10
                $ d_auction_love += 20
                if bidder != "green":
                    $ price += 10
                    show window_green_flash
                    greenwindow "[price][mememoney]."
                    $ price += 10
                    show window_red_flash
                    redwindow "Hm... [price][mememoney]."
                    $ bidder = "red"
                elif True:
                    "..."

    announcer "Don't worry, just a couple left."
    announcer "Do you enjoy camping?"
    "I stood there stunned for a moment."
    "What does that have to do with any of this..?"
    menu:
        " "
        "\"I love camping.\"" if True:
            $ m_auction_love += 40
            "I scoffed quietly."
            "Was one of these weirdos wanting to take me camping?"
            if bidder != "green":
                $ price += 50
                show window_green_flash
                greenwindow "[price][mememoney]."
                $ bidder = "green"
            elif True:
                "..."
            announcer "Haha, alright, alright."
            announcer "You're doing wonderfully."
        "\"It's okay..?\"" if True:
            $ m_auction_love += 10
            if bidder != "green":
                $ price += 10
                show window_green_flash
                greenwindow "[price][mememoney]."
                $ bidder = "green"
            elif True:
                "..."
            announcer "Haha, alright, alright."
            announcer "You're doing wonderfully."
        "\"I hate camping...\"" if True:
            "I looked down."
            "I'd rather be camping than here though..."
            $ c_auction_love += 10
            if bidder != "blue":
                $ price += 10
                show window_blue_flash
                bluewindow "Hmmm~ [price][mememoney]."
                $ bidder = "blue"
            elif True:
                "..."
            announcer "Haha, alright, alright."
            announcer "You're doing wonderfully."
        "-Refuse to answer-" if True:

            "I remained stoic."
            "Everyone was quiet for a moment before the announcer continued."
            announcer "How mysterious!"
            announcer "Love the energy!"

    announcer "Last question:"
    announcer "Who would you like to go home with?"
    "... What?"
    "I looked at the windows across from me in the dark room."
    menu:
        " "
        "-Choose the red window-" if True:
            "It's not like I even knew who any of them were."
            "Maybe the youngest sounding one would be safer..."
            "I pointed at the red window."
            show window_red_flash
            redwindow "Ohhhh~?"
            redwindow "[pp_is_c] a smart one! Good taste!"
            if bidder != "red":
                $ price += 10
                redwindow "[price][mememoney]."
            show window_blue_flash
            $ price += 10
            bluewindow "[price][mememoney]."
            show window_red_flash
            $ price += 10
            redwindow "Fuck off!"
            redwindow "[price][mememoney]!!"
            show window_blue_flash
            $ price += 10
            bluewindow "[price][mememoney]. You wouldn't even know what to do with [pp_obj]."
            "I heard the announcer chuckling softly."
            "I guess he didn't care if they were fighting as long as the price went up..."
            show window_red_flash
            $ price += 10
            redwindow "Why don't I show you firsthand what I plan to do with [pp_obj]!?"
            redwindow "[price][mememoney]!"
            show window_blue_flash
            bluewindow "Funny. You couldn't even afford to lick my shoe."
            bluewindow "Enjoy your toy, little boy."
            $ bidder = "red"
        "-Choose the blue window-" if True:

            "I thought about the voices I'd heard."
            "The voice behind the blue window seemed...a little softer than the others."
            "I suppose if I had to choose a safer option..."
            "I pointed to the blue window."
            show window_blue_flash
            "I heard her light laugh."
            bluewindow "That's not too suprising, considering your options."
            if bidder != "blue":
                $ price += 10
                bluewindow "I'll take pity on you. [price][mememoney]."
            show window_red_flash
            "I heard an obnoxious snort."
            $ price += 10
            redwindow "You sound so full of yourself."
            if sexcontent != "no":
                redwindow "You should relax and let someone fill you with something else for once! Hahaha!"
            redwindow "[price][mememoney]!"
            show window_blue_flash
            bluewindow "..."
            $ price += 100
            bluewindow "[price][mememoney]."
            show window_red_flash
            redwindow "W..what the fuck..?"
            show window_blue_flash
            bluewindow "What's wrong?"
            bluewindow "Did daddy not give you a big enough allowance?"
            "Her laugh was quiet and cruel this time."
            bluewindow "That's what I thought."
            $ bidder = "blue"
        "-Choose the green window-" if True:

            "Whoever the two in the blue and red windows were..."
            "They both gave me a bad feeling."
            "If they were that rude to each other..."
            "I probably don't stand a chance."
            "Might as well go with the more polite one..."
            "I pointed to the green window."
            show window_red_flash
            redwindow "Heh! Can't take that stuck up blue window bitch either?"
            if bidder != "green":
                $ price += 10
                redwindow "Why don't you come with me instead?"
                redwindow "[price][mememoney]!"
            show window_blue_flash
            bluewindow "Jesus, you really can't keep that mouth shut can you?"
            show window_red_flash
            if sexcontent != "no":
                redwindow "Are you really one to talk?"
                redwindow "With all that money, I bet your mouth's open all the time..."
                show window_blue_flash
                bluewindow "You disgusting little prick!"
                show window_red_flash
                redwindow "Hahaha! You call me little one more time and I'm gonna have to show you!"
            elif True:
                redwindow "Why don't you come over here and say that to my face?"
                show window_blue_flash
                bluewindow "In your {i}dreams{/i}, boy."
            $ price += 500
            show window_green_flash
            greenwindow "[price][mememoney]."
            "The low voice growled through the room."
            "Both of the other windows went silent."
            "Even the announcer seemed to be stunned."
            greenwindow "No more bids then?"
            "The voice quieted down gruffly."
            greenwindow "Good."
            "The announcer took a moment to regain his composure."
            $ bidder = "green"

        "-Point at the Announcer-" if persistent.bluecounter:
            announcer "..."
            announcer "Oh?"
            "The announcer suddenly laughed with a strange bark."
            show window_red_flash
            redwindow "Stop messing around!"
            "The announcer cleared his throat."
            announcer "Yes, of course."
            announcer "I'm very flattered, and I would simply {i}love{/i} to take you home! But I'm afraid the show must go on~"
            announcer "These lovely and very patient patrons have paid good money to be here today."
            announcer "So, let's wrap up the bidding shall we?"
            menu:
                " "
                "Beg the announcer to take you home" if True:
                    $ bidder = "fox"
                    p "Wait! Please!"
                    "I fumbled for reasons. These people all sound insane."
                    "Surely I stand a better chance with whoever is doing the announcing here."
                    p "I want to go with you! Not them! Please!"
                    "I flushed at the sound of desperation in my voice."
                    "Please, just let this work..."
                    show window_blue_flash
                    bluewindow "That's kind of cute..."
                    bluewindow "You know, maybe you SHOULD take [pp_obj] home."
                    show window_red_flash
                    redwindow "What the fuck are you {i}talking{/i} about?"
                    redwindow "We've already bid!"
                    if bidder == "red":
                        redwindow "You're just saying this because I was winning!"
                    show window_blue_flash
                    bluewindow "Relax! There's other choices, aren't there?"
                    announcer "Oh, of course!"
                    announcer "We have a very diverse and exciting selection of products for you to peruse today~"
                    show window_blue_flash
                    bluewindow "See? You can just bid on another one."
                    show window_red_flash
                    redwindow "Tch..."
                    show window_blue_flash
                    bluewindow "And I'm sure his {i}fans{/i} would love to see another show..."
                    "I stood there, frozen, listening to the exchange."
                    "Something about the blue window's voice changed when she mentioned a 'show'."
                    announcer "I'm humbled and flattered!"
                    show window_green_flash
                    greenwindow "Whatever yer decidin', get it over with."
                    announcer "Oh! Yes! I'm terribly sorry for the interruption!"
                    announcer "Well, how about this?"
                    announcer "If you're willing to so graciously relinquish this delightful specimen to myself..."
                    announcer "I'll give you three a ten percent discount on your {i}next{/i} purchase."
                    show window_blue_flash
                    bluewindow "Oh! You're too kind!"
                    bluewindow "I happily accept."
                    bluewindow "And I'm sure the others do too."
                    show window_red_flash
                    redwindow "Don't talk for me, bitch!"
                    redwindow "..."
                    redwindow "But I guess it's fine. I didn't really want this one anyway."
                    "Silence overtook the room again as the others waited for the green window to speak."
                    show window_green_flash
                    greenwindow "It's fine. I can wait for another one."
                    announcer "So it's settled then!"
                    announcer "What an exciting turn of events!"
                    announcer "I suppose I'm the one who won this bid!"
                    "He let out another barking laugh."
                    announcer "Let's get [pp_obj] packed up and move on to our next product!"
                    "I felt a sharp jab in my ankle."
                    p "Wh... aa..."
                    "I tried to bend down to inspect the pain, but I just crumpled to the floor."
                    "There was pain in my leg and I couldn't move."
                    "I was seeing double and trying to speak."
                    stop music fadeout 1.0
                    scene black with eyedissolve
                    "But I passed out."
                    pause(1.0)
                    jump game_start_fox
                "Let the bidding continue" if True:
                    pass
            jump final_bids
        "\"I don't want to be sold, you asshole!\"" if True:


            "I lost my cool and shouted into the room."
            p "Fuck you people!"
            announcer "Oh my!"
            label final_bids:
            if c_auction_love >= d_auction_love and c_auction_love >= m_auction_love:

                if bidder != "red":
                    $ price += 10
                    show window_red_flash
                    redwindow "[price][mememoney]!"
                announcer "..."
                announcer "Anyone else?"
                $ price += 10
                show window_blue_flash
                bluewindow "Hmmm. I guess I could do [price][mememoney]."
                "Everyone seemed to suddenly slow down."
                $ bidder = "blue"

            elif d_auction_love >= c_auction_love and d_auction_love >= m_auction_love:

                if bidder != "blue":
                    $ price += 10
                    show window_blue_flash
                    bluewindow "[price][mememoney]."
                $ price += 10
                show window_red_flash
                redwindow "[price][mememoney]!"
                $ price += 10
                show window_blue_flash
                bluewindow "[price][mememoney]."
                $ price += 20
                show window_red_flash
                redwindow "[price][mememoney]!"
                $ price += 20
                show window_blue_flash
                bluewindow "... [price][mememoney]."
                $ price += 50
                show window_red_flash
                redwindow "[price][mememoney]!!!"
                $ price += 10
                show window_blue_flash
                bluewindow "[price][mememoney]~"
                show window_red_flash
                redwindow "Alright you damn bitch!"
                $ price += 100
                redwindow "[price][mememoney]! Choke on it!"
                show window_blue_flash
                $ bidder = "red"
                bluewindow "Hahaha!"
                bluewindow "... Enjoy~"
                announcer "We DO love some competition!"
                announcer "Now..."
            elif True:


                if bidder != "green":
                    $ price += 10
                    show window_green_flash
                    greenwindow "[price][mememoney]."
                $ price += 10
                show window_red_flash
                redwindow "[price][mememoney]!"
                $ price += 10
                show window_green_flash
                greenwindow "[price][mememoney]."
                $ price += 10
                show window_red_flash
                redwindow "Come on, old man! You wouldn't even know what to do with [pp_obj]!"
                redwindow "[price][mememoney]!"
                "I shifted my weight for a moment as the silence became awkward."
                $ price += 500
                show window_green_flash
                greenwindow "[price][mememoney]."
                show window_red_flash
                redwindow "Wha-!?"
                show window_blue_flash
                bluewindow "Haha~"
                "I could practically feel the angry energy coming from the red window."
                "I felt a little bit better knowing that he wouldn't be winning."
                $ bidder = "green"

    announcer "I hear [price][mememoney]!"
    announcer "Anyone else..?"
    if bidder == "green":
        announcer "Haha! Sold!"
        show window_green_flash
        announcer "To my robust friend in the green!"
    if bidder == "blue":
        announcer "Haha! Sold!"
        show window_blue_flash
        announcer "To the elegant lady in blue!"
    if bidder == "red":
        announcer "Haha! Sold!"
        show window_red_flash
        announcer "To the obstreperous gentleman in red!"
    if price >= 500:
        $ persistent.ach_luxury_product = True
        $ achievement.grant("ach_luxury_product")
        init:
            $ achievement.register("ach_luxury_product")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_luxury_product == True and achievement.has("ach_luxury_product") != True:
                $ achievement.grant("ach_luxury_product")
                $ achievement.register("ach_luxury_product")
                $ achievement.sync()
    announcer "We'll prepare the shipment to send out with you right away."
    announcer "Thank you very much for coming!!"
    "Shipment!?"
    "What did that mea-"
    "I felt a sharp jab in my ankle."
    p "Wh... aa..."
    "I tried to bend down to inspect the pain, but I just crumpled to the floor."
    "There was pain in my leg and I couldn't move."
    "I was seeing double and trying to speak."
    stop music fadeout 1.0
    scene black with eyedissolve
    "But I passed out."
    pause(1.0)
    if bidder == "green":
        jump game_start_mason
    if bidder == "blue":
        jump game_start_celia
    if bidder == "red":
        jump game_start_derek



label game_start_mason:
    $ gamepath = "mason"
    $ location_temp = "cold"
    $ map_location = "Meadow"
    $ food = 20
    $ energy = 24

    play ambient "music/ambient_forest.ogg" fadein 3.0
    "I woke up coughing."
    "It's cold..."
    show bg_mason_meadow at confused_bobbing
    show cg_burlap_over
    "H-huh!?"
    "I can't see!"
    "I took a moment to try and get my bearings."
    "I'm lying down... My hands are tied and I'm blindfolded."
    "I pushed down at the wave of panic rising in my chest."
    "I'm wearing something warm, but a cold wind is biting at my face and hands."
    "I'm definitely outside..."
    m empty "Oh!"
    "My panic exploded from my control as I heard the gruff voice and heavy footsteps approaching."
    m empty "Lookit you. Already awake."
    "I felt the nudge of a boot, and tried to get away from it."
    menu:
        " "
        "Stay still" if True:
            "I gulped and stayed still, trying to calm myself."
            "I can't panic now..."
        "Try to get up" if True:
            "I immediately twisted my body and tried to get my knees underneath myself."
            m "Hm. Settle down."
            "The boot pushed me back down to the ground." with vpunch
            "It wasn't particularly rough, but something about the force behind the motion sent a shiver down my body."
        "Talk" if True:
            p "Who are you!?"
            p "Where am I!?"
            "I tried to keep my panic out of my voice, but it bled through anyway."
            m "Heh."
    m empty "Looks like you're about ready, eh?"
    "I could hear the heavy footsteps slowly circle my body."
    m empty "Now, the suits gave me a name for you."
    if player_name.upper() == "SANDY":
        m empty "[player_name]..."
        "His voiced trailed off, and I could only hear the wind through leaves."
        m empty "World's a funny place, isn't it?"
    elif True:
        m empty "[player_name]. Is that right?"
    "Before I could answer, he continued."
    m empty "Anyway, s'pose we might as well have it even."
    $ mason_name = "Mason"
    m empty "You can call me Mason, if you're the talkin' sort."
    m empty "Now, I'm gonna be takin' the blindfold off."
    m empty "Stand up."
    menu:
        " "
        "Obey" if True:
            "I might as well comply. It's not like I have much of a choice."
            "I awkwardly scrambled before managing to get into a kneeling position."
            "I took a deep breath and shakily got onto one foot, then the other."
            "I half expected him to say something about how long I was taking, yet I only heard silence."
        "Refuse" if True:
            p "Fuck you!"
            "Why should I make anything easier for this asshole?"
            "I braced myself for his reply."
            m empty "Havin' trouble?"
            "I heard him close the gap in one step."
            "A large hand gripped the back of my clothing."
            p "Wait! No-"
            "I gasped as my body was pulled upwards, quickly and firmly." with vpunch
            "I forgot about my protests as I suddenly adjusted to standing on shaky legs."
    "The crunch of a twig told me he'd gotten very close."
    m empty "Mmhm. That's better."
    "A hand gripped my blindfold."
    play music "music/masons_theme.ogg" fadein 1.0
    scene white with Dissolve(0.2)
    scene bg_mason_thicket:
        zoom 1.1
        xalign 0.5
        yalign 1.0
        easeout 0.5 zoom 1.0
    show mason:
        zoom 1.2
        xalign 0.5
        yalign 1.0
        easeout 0.5 zoom 1.0
    with Dissolve(2.0)
    "I stepped back as my eyes adjusted."
    if meme_mode:
        p "God DAMN you're big!"
        m "Mmm."
        "Someone ate their wheaties..."
    elif True:
        "This guy is huge!"
    "My eyes darted everywhere, trying to get as much information as I could."
    "I looked down at myself and saw clothing I've never seen before."
    "I was wearing a warm outfit and coat..."
    "What the hell..."
    m calm "Hrm. Yup. It's a little late in the year."
    "My attention snapped back to him."
    m normal "Your job is to survive."
    m question "Mountain's a dangerous place, understand?"
    "To my surprise, he held out a small backpack."
    m calm "Supplies. For the mountain."
    menu:
        " "
        "-Take the backpack-" if True:
            label mason_take_backpack:
            $ inventory.append("item_knife")
            $ inventory.append("item_flint")
            $ inventory.append("item_paper")
            $ inventory.append("item_trail_mix")
            $ renpy.notify("Items Added!")
            show screen inventory
            pause(1.5)
            hide screen inventory
            "I cautiously grabbed the backpack."
            "I should probably take anything I can get at this point..."
            "I pulled the backpack over my arms and looked to him."
            "He nodded in approval."
        "-Refuse to move-" if True:
            m "..."
            m "Take it."
            menu:
                " "
                "-Take the backpack-" if True:
                    jump mason_take_backpack
                "-Stay still-" if True:
                    "I didn't move."
                    m serious "Mm."
                    m question "Frozen up, huh?"
                    show mason normal
                    "I flinched as he suddenly grasped the front of my coat and shirt." with vpunch
                    "He pulled me with such strength that I couldn't help but panic."
                    m calm "Shh. Shhh, I gotcha."
                    "My squirming was weak and useless from the cold and whatever they used to knock me out."
                    "He wrenched the backpack over one of my arms."
                    $ inventory.append("item_knife")
                    $ inventory.append("item_flint")
                    $ inventory.append("item_paper")
                    $ inventory.append("item_trail_mix")
                    $ renpy.notify("Items Added!")
                    show screen inventory
                    pause(1.5)
                    hide screen inventory
                    "Then he simply let me go."
    m normal "Alright."
    hide mason with dissolve
    "He grabbed something from behind him."
    show black:
        alpha 0.0
        easein 0.5 alpha 0.5
    show mason crossbow with dissolve
    play sound "music/sfx_scrape_fast.ogg"
    m "Run."
    scene black with dissolve
    "I turned around, screaming internally at my body to move faster."
    "I stumbled over roots, cursing my stiff legs."
    "What the fuck was that!?"
    "A crossbow!?"
    play sound "<from 0.0 to 1.0>music/sfx_bolt_wood.ogg"
    "Just as I began to manage my muscles and the pounding blood in my ears, I heard a crack in front of me."
    $ stat_sanity -= 10
    "I glanced to the side just in time to see a crossbow bolt lodged deep in a tree beside me."
    "I ran even faster than I knew I could."
    "He's trying to kill me!"
    "I don't know how long I ran for."
    "I ran until my lungs felt like they were full of glass shards."
    "I slowed, but I kept moving."
    "Sucking in the cold air and forcing my aching limbs to move."
    play sound "music/sfx_impact_forest.ogg"
    scene bg_mason_meadow with vpunch
    "Something caught my dragging feet and I fell to the ground."
    "I laid there, shaking, trying to process what was happening."
    stop music fadeout 3.0
    "I listened for him."
    "..."
    "Nothing... just wind through the trees."

label mason_turn_order:
    $ phase = "event"
    hide screen mini_screen
    hide screen inventory_item
    hide screen status_update_health
    hide screen status_update_sanity
    hide screen status_update_energy
    hide screen status_update_food
    hide screen status_update_temp_increase
    hide screen status_update_temp_decrease
    hide screen notify
    $ hours += 1
    $ total_hours += 1
    if location_temp == "cold":
        $ stat_temp -= 5
    if location_temp == "warm":
        if temp <= 40:
            $ stat_temp += 10
    if fire > 0 and arrivedby == "idle":
        $ fire += 1
    $ stat_food -= 1
    if wound == 1:
        $ stat_health -= 3
    if wound == 2:
        $ stat_health -= 5
    if sleep > 0:
        $ energy += 3
        if energy >= 24:
            $ energy = 24
            $ sleep = 0
            $ arrivedby = "wakeup"
    elif True:
        if food <= 0 or encumbered == 1:
            $ stat_energy -= 3
        elif True:
            $ stat_energy -= 1
    if grace_period > 0:
        $ grace_period -= 1
    call mason_display_subroutine from _call_mason_display_subroutine
    call mason_stat_subroutine from _call_mason_stat_subroutine
    label mason_turn_nostats:
        call mason_event_subroutine from _call_mason_event_subroutine
        $ phase = "adventure"
        $ renpy.pause(hard=True)


label mason_stat_subroutine:
    if health <= 0 and map_location != "House":
        jump event_mason_death_health
    if temp == 30 and location_temp == "cold" and sleep <= 0:
        jump event_mason_cold_1
    if temp == 20 and location_temp == "cold" and sleep <= 0:
        jump event_mason_cold_2
    if temp == 10 and location_temp == "cold" and sleep <= 0:
        jump event_mason_cold_3
    if temp <= 0:
        jump event_mason_colddeath
    return

label mason_display_subroutine:
    if sleep > 0:
        scene black with eyedissolve
    elif True:
        if map_location == "Meadow":
            window show
            $ persistent.bgs_seen.add("bg_mason_meadow")
            $ renpy.save_persistent()
            scene bg_mason_meadow with dissolve
            if fire > 0:
                show campfire
        elif map_location == "Thicket":
            window show
            $ persistent.bgs_seen.add("bg_mason_thicket")
            $ renpy.save_persistent()
            scene bg_mason_thicket with dissolve
            if fire > 0:
                show campfire
        elif map_location == "Tall Tree":
            window show
            $ persistent.bgs_seen.add("bg_mason_talltree")
            $ renpy.save_persistent()
            scene bg_mason_talltree with dissolve
            if fire > 0:
                show campfire
        elif map_location == "Waterfall":
            window show
            $ persistent.bgs_seen.add("bg_mason_waterfall")
            $ renpy.save_persistent()
            scene bg_mason_waterfall with dissolve
            if fire > 0:
                show campfire
        elif map_location == "House":
            window show
            $ persistent.bgs_seen.add("bg_mason_cabin")
            $ renpy.save_persistent()
            if map_location_cabin == "outside":
                scene bg_mason_cabin with dissolve
            elif True:
                scene bg_mason_incabin with dissolve
        elif map_location == "Swamp":
            $ persistent.bgs_seen.add("bg_mason_swamp")
            $ renpy.save_persistent()
            window show
            scene bg_mason_swamp with dissolve
    return




label mason_event_subroutine:
    if event_mason_1 == 0:
        label event_mason_1:
            $ event_mason_1 = 1
            "I took a few deep breaths and looked around myself."
            "Everything looked the same... just trees and mountains."
            "I held my arms close and tried to stay calm."
            "The autumn cold was biting."
            "It's colder than it looks out here..."
            "I have to find some way to get warm, or that crossbow will be the least of my problems."
            $ phase = "adventure"
            menu:
                "I could look through what I have... or keep moving."
                "Stay here" if True:
                    $ map_location = "Meadow"
                    $ arrivedby = "idle"
                    jump mason_turn_order
                "Keep Moving" if True:
                    $ map_location = "Thicket"
                    $ arrivedby = "new"
                    jump mason_turn_order

    if event_mason_nightmare == 0 and sleep > 0 and sanity <= 50:
        $ event_mason_nightmare = 1
        jump event_mason_nightmare

    if event_mason_arrivetalltree == 0 and map_location == "Tall Tree":
        jump event_mason_arrivetalltree

    if event_mason_arrivewaterfall == 0 and map_location == "Waterfall":
        jump event_mason_arrivewaterfall

    if total_hours == 13 or total_hours == 14:
        $ mason_location = "Meadow"
    if total_hours == 15 or total_hours == 16:
        $ mason_location = "Thicket"
    elif total_hours == 17 or total_hours == 18:
        $ mason_location = "Meadow"
    elif 19 <= total_hours <= 32:
        $ mason_location = "House"
    elif total_hours == 33 or total_hours == 34:
        $ mason_location = "Meadow"
    elif total_hours == 35 or total_hours == 36:
        $ mason_location = "Waterfall"
    elif total_hours == 37 or total_hours == 38:
        $ mason_location = "Meadow"
    elif total_hours == 39 or total_hours == 40:
        $ mason_location = "Thicket"
    elif total_hours == 41 or total_hours == 42:
        $ mason_location = "Tall Tree"
    elif 43 <= total_hours <= 58:
        $ mason_location = "House"
    elif total_hours == 59 or total_hours == 60:
        $ mason_location = "Tall Tree"
    elif total_hours == 61 or total_hours == 62:
        $ mason_location = "Thicket"
    elif total_hours == 63 or total_hours == 64:
        $ mason_location = "Waterfall"
    elif total_hours == 65 or total_hours == 66:
        $ mason_location = "Meadow"
    elif 67 <= total_hours <= 80:
        $ mason_location = "House"
    elif total_hours == 81 or total_hours == 82:
        $ mason_location = "Meadow"
    elif total_hours == 83 or total_hours == 84:
        $ mason_location = "Thicket"
    elif total_hours == 85 or total_hours == 86:
        $ mason_location = "Tall Tree"
    elif total_hours == 87 or total_hours == 88:
        $ mason_location = "Thicket"
    elif total_hours == 89 or total_hours == 90:
        $ mason_location = "Waterfall"
    elif 91 <= total_hours <= 102:
        $ mason_location = "House"

    if mason_location == map_location and grace_period == 0 and mason_location != "House":
        jump event_mason_crossbow_1

    if fire > 3 and 8 <= hours <= 18:
        jump event_mason_firedeath

    if energy <= 0:
        label mason_energy_passout:
            $ phase = "event"
            $ arrivedby = "sleep"
            if map_location_cabin == "inside":
                "My vision wavered."
                "I tried to move but I couldn't."
                jump event_mason_cabin_sleep
            elif True:
                "My vision wavered."
                "I tried to move but I couldn't."
                "I collapsed to the ground. I didn't have the energy to move on."
                "I struggled for a moment longer, then passed out."
            $ sleep = 12
            jump mason_turn_order

    if map_location == "Thicket" and map_discovery_meadow == True and map_discovery_thicket == True and map_discovery_talltree == True and map_discovery_waterfall == True and event_mason_mapswamp == 0 and sleep == 0:
        $ event_mason_mapswamp = 1
        jump event_mason_mapswamp

    if total_hours > 30 and 22 <= hours <= 24 and event_mason_pepper_1 == 0 and sleep <= 0 and map_location != "House":
        $ event_mason_pepper_1 = 1
        jump event_mason_pepper_1
    if total_hours > 40 and 11 <= hours <= 14 and event_mason_pepper_2 == 0 and sleep <= 0 and map_location != "House":
        $ event_mason_pepper_2 = 1
        jump event_mason_pepper_2

    if map_location == "Tall Tree" and 8 <= hours <= 18 and event_mason_snare_dismantle == 1 and event_mason_snare_deer == 0 and arrivedby == "new":
        $ event_mason_snare_deer = 1
        $ grace_period = 5
        jump event_mason_snare_deer

    if (20 <= hours <= 24 or 0 <= hours <= 6) and sleep != 0 and ("item_saskatoons" in inventory or "item_fish" in inventory or "item_cookedfish" in inventory or "item_fish_cute" in inventory or "item_cookedfish_cute" in inventory):
        jump event_mason_bear_death

    if total_hours >= 100:
        jump event_mason_timedeath

    if map_location == "Meadow" and hours == 3 and sanity <= 30 and event_mason_sanity_1 == 0:
        $ event_mason_sanity_1 = 1
        play sound [ "<silence 5.0>", "music/sfx_twig_snap_1.ogg" ]
        show mason_scare_1 behind effect_ice

    if map_location == "Thicket" and hours == 15 and sanity <= 40 and event_mason_sanity_2 == 0:
        $ event_mason_sanity_2 = 1
        play sound [ "<silence 15.0>", "music/sfx_twig_snap_2.ogg" ]
        show mason_scare_2 behind effect_ice



    if map_location == "Meadow":

        if sleep > 1:
            label mason_meadow_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump mason_turn_order
        if arrivedby == "wakeup":
            label mason_meadow_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                "I looked around myself and remembered where I was."
                if meme_mode:
                    "Ah shit. Here we go again."
                elif True:
                    "I groggily got back up."
                $ arrivedby = "special"
                jump mason_turn_nostats


        if arrivedby == "new" or arrivedby == "chased":
            $ arrivedby = "idle"
            "I've made it to the meadow. I sat down and rested in the clearing."
        elif arrivedby == "idle":
            $ arrivedby = "idle"
            if fire > 0:
                "I relaxed by the fire."
            elif True:
                "I stayed in the meadow."
        elif arrivedby == "wander":
            "Branches clawed at me as I walked."
            "Then, the trees opened up."
            "Huh?"
            "The clearing..? I must have gotten turned around..."
        label mason_meadow_travel:
            $ phase = "adventure"
            menu:
                " "
                "Stay here" if True:
                    $ map_location = "Meadow"
                    $ arrivedby = "idle"
                    jump mason_turn_order
                "Walk into the trees" if True:
                    $ chance = renpy.random.randint(1,100)
                    if chance <= 20 and sanity < 40:
                        stop ambient fadeout 1.0
                        play ambient "music/ambient_creek.ogg" fadein 1.0
                        $ map_location = "Waterfall"
                        $ arrivedby = "wander"
                    elif True:
                        $ map_location = "Thicket"
                        $ arrivedby = "new"
                    if fire != 0:
                        $ fire = 0
                        $ location_temp = "cold"
                        stop music fadeout 0.5
                        hide campfire with dissolve
                        "I quickly put out my fire."
                    jump mason_turn_order
                "Walk towards the rocks" if True:
                    $ chance = renpy.random.randint(1,100)
                    if chance <= 20 and sanity < 40:
                        $ map_location = "Thicket"
                        $ arrivedby = "wander"
                    elif True:
                        stop ambient fadeout 1.0
                        play ambient "music/ambient_creek.ogg" fadein 1.0
                        $ map_location = "Waterfall"
                        $ arrivedby = "new"
                    if fire != 0:
                        $ fire = 0
                        $ location_temp = "cold"
                        stop music fadeout 0.5
                        hide campfire with dissolve
                        "I quickly put out my fire."
                    jump mason_turn_order
                "Walk towards the cabin" if map_discovery_house == True:
                    $ chance = renpy.random.randint(1,100)
                    if chance <= 20 and sanity < 40:
                        $ map_location = "Thicket"
                        $ arrivedby = "wander"
                    elif True:
                        $ map_location = "House"
                        $ arrivedby = "new"
                    if fire != 0:
                        $ fire = 0
                        $ location_temp = "cold"
                        stop music fadeout 0.5
                        hide campfire with dissolve
                        "I quickly put out my fire."
                    jump mason_turn_order
        return


    if map_location == "Thicket":

        if sleep > 1:
            label mason_thicket_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump mason_turn_order
        if arrivedby == "wakeup":
            label mason_thicket_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                "I looked around myself and remembered where I was."
                if meme_mode:
                    "Well... Time to get back on my bullshit."
                elif True:
                    "I groggily got back up."
                $ arrivedby = "special"
                jump mason_turn_nostats

        if arrivedby == "new" or arrivedby == "chased":
            $ arrivedby = "idle"
            "I've made it to the trees. I sat down against a large tree."
        elif arrivedby == "idle":
            $ arrivedby = "idle"
            if fire > 0:
                "I relaxed by the fire."
            elif True:
                "I stayed in the thicket."
        elif arrivedby == "wander":
            "I trudged over the dirt and dead leaves."
            "I spotted a familiar set of tree trunks."
            "Wait... that's not right."
            "I must have gone the wrong way..."
        label mason_thicket_travel:
            $ phase = "adventure"
            menu:
                " "
                "Stay here" if True:
                    $ map_location = "Thicket"
                    $ arrivedby = "idle"
                    jump mason_turn_order
                "Walk back to the clearing" if True:
                    $ chance = renpy.random.randint(1,100)
                    if chance <= 20 and sanity < 40:
                        $ map_location = "Tall Tree"
                        $ arrivedby = "wander"
                    elif True:
                        $ map_location = "Meadow"
                        $ arrivedby = "new"
                    if fire != 0:
                        $ fire = 0
                        $ location_temp = "cold"
                        stop music fadeout 0.5
                        hide campfire with dissolve
                        "I quickly put out my fire."
                    jump mason_turn_order
                "Walk deeper into the woods" if True:
                    $ chance = renpy.random.randint(1,100)
                    if chance <= 20 and sanity < 40:
                        $ map_location = "Meadow"
                        $ arrivedby = "wander"
                    elif True:
                        $ map_location = "Tall Tree"
                        $ arrivedby = "new"
                    if fire != 0:
                        $ fire = 0
                        $ location_temp = "cold"
                        stop music fadeout 0.5
                        hide campfire with dissolve
                        "I quickly put out my fire."
                    jump mason_turn_order
                "Walk to the black swamp" if map_discovery_swamp == True:
                    $ chance = renpy.random.randint(1,100)
                    if chance <= 20 and sanity < 40:
                        $ map_location = "Tall Tree"
                        $ arrivedby = "wander"
                    elif True:
                        $ map_location = "Swamp"
                        $ arrivedby = "new"
                    if fire != 0:
                        $ fire = 0
                        $ location_temp = "cold"
                        stop music fadeout 0.5
                        hide campfire with dissolve
                        "I quickly put out my fire."
                    jump mason_turn_order


    if map_location == "Tall Tree":

        if sleep > 1:
            label mason_talltree_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump mason_turn_order
        if arrivedby == "wakeup":
            label mason_talltree_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                if meme_mode:
                    "Don't talk to me unless I've had my coffee..."
                    "I looked around."
                    "Oh, right."
                elif True:
                    "I looked around myself and remembered where I was."
                    "I groggily got back up."
                $ arrivedby = "special"
                jump mason_turn_nostats

        if arrivedby == "new" or arrivedby == "chased":
            $ arrivedby = "idle"
            "I've made it to the largest trees."
        elif arrivedby == "idle":
            $ arrivedby = "idle"
            if fire > 0:
                "I relaxed by the fire."
            elif True:
                "I stayed under the giant trees."
        elif arrivedby == "wander":
            "I slapped branches out of the way."
            "I looked around and noticed the trees getting thicker."
            "...What?"
            "Ugh... I went the wrong way..."
        label mason_talltree_travel:
            $ phase = "adventure"
            if event_mason_discover_snare == 0 and total_hours > 24:
                menu:
                    " "
                    "Stay here" if True:
                        $ map_location = "Tall Tree"
                        $ arrivedby = "idle"
                        jump mason_turn_order
                    "Walk back into the woods" if True:
                        if fire != 0:
                            $ fire = 0
                            $ location_temp = "cold"
                            stop music fadeout 0.5
                            hide campfire with dissolve
                            "I quickly put out my fire."
                        "I began walking into the thicker brush."
                        jump event_mason_snare_death
            elif True:
                menu:
                    " "
                    "Stay here" if True:
                        $ map_location = "Tall Tree"
                        $ arrivedby = "idle"
                        jump mason_turn_order
                    "Walk back into the woods" if True:
                        if sanity < 50 and event_mason_sound_1 == 0:
                            $ mason_sanity_sound = 1
                            play sound [ "<silence 4.0>", "music/sfx_pinecone_drop.ogg" ]
                        $ map_location = "Thicket"
                        $ arrivedby = "new"
                        if fire != 0:
                            $ fire = 0
                            $ location_temp = "cold"
                            stop music fadeout 0.5
                            hide campfire with dissolve
                            "I quickly put out my fire."
                        jump mason_turn_order


    if map_location == "Waterfall":

        if sleep > 1:
            label mason_waterfall_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump mason_turn_order
        if arrivedby == "wakeup":
            label mason_waterfall_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                "I looked around myself and remembered where I was."
                if meme_mode:
                    "Oh no."
                    "I woke up."
                elif True:
                    "I groggily got back up."
                $ arrivedby = "special"
                jump mason_turn_nostats

        if arrivedby == "new" or arrivedby == "chased":
            $ arrivedby = "idle"
            "I followed the sound of running water and found the creek."
        elif arrivedby == "idle":
            $ arrivedby = "idle"
            if fire > 0:
                "I relaxed by the fire."
            elif True:
                "I stayed by the water."
        elif arrivedby == "wander":
            "I pushed through bush and twigs."
            "I heard the sound of water."
            "Wait...this isn't right."
            "I must have gotten turned around..."
        label mason_waterfall_travel:
            $ phase = "adventure"
            if total_hours > 36 and event_mason_discover_beartrap == 0:
                menu:
                    " "
                    "Stay here" if True:
                        $ map_location = "Waterfall"
                        $ arrivedby = "idle"
                        jump mason_turn_order
                    "Walk back to the clearing" if True:
                        "I started walking towards the trees."
                        jump event_mason_beartrap_death
            elif True:
                menu:
                    " "
                    "Stay here" if True:
                        $ map_location = "Waterfall"
                        $ arrivedby = "idle"
                        jump mason_turn_order
                    "Walk back to the clearing" if True:
                        $ map_location = "Meadow"
                        $ arrivedby = "new"
                        if fire != 0:
                            $ fire = 0
                            $ location_temp = "cold"
                            stop music fadeout 0.5
                            hide campfire with dissolve
                            "I quickly put out my fire."
                        play ambient "music/ambient_forest.ogg" fadein 1.0
                        jump mason_turn_order


    if map_location == "House":

        if sleep > 1:
            label mason_house_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump mason_turn_order
        if arrivedby == "wakeup":
            label mason_house_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                p "Shit!"
                "I can't believe I fell asleep out here..."
                "I got up and dusted myself off, feeling rather lucky that I hadn't been caught."
                $ arrivedby = "special"
                jump mason_turn_nostats

        if arrivedby == "new":
            if event_mason_findcabin == 0:
                $ event_mason_findcabin = 1
                "I think I'm going in the right direction..."
                "I pushed past more trees."
                "There!"
                "Suddenly, a break in the trees led to the side of a wooden cabin."
                "To my frustration, there was no sign of any road."
                "Just thick forest on all sides."
                "How the hell does he get out of here?"
                p "Hm."
                "I could try looking inside..."
            elif True:
                "The small cabin was still hard to find."
                "I managed to recognize the surrounding trees and get to the familiar tiny clearing."
                "There it is..."
        elif True:
            "I'm not sure I should stay here long..."

        if map_location_cabin == "inside" and (0 <= hours <= 7 or 21 <= hours <= 24):
            "I jumped as I heard heavy footsteps outside."
            "Shit!"
            "I frantically looked around for somewhere to hide, but the cabin was so small..."
            "Before I could even step towards the wall, the door was thrown open."
            "For a split second, he just stared at me in surprise."
            jump event_mason_masonshome

        label mason_house_travel:
            $ phase = "adventure"
            menu:
                " "
                "Go inside the cabin" if map_location_cabin != "inside":
                    $ persistent.bgs_seen.add("bg_mason_incabin")
                    $ renpy.save_persistent()
                    $ phase = "event"
                    if 8 <= hours <= 20:
                        if event_mason_findincabin == 0:
                            scene black with dissolve
                            $ event_mason_findincabin = 1
                            stop ambient fadeout 1.0
                            "I slowly opened the door."
                            "I wasn't sure if I was shaking from the cold or from worry."
                            "I moved it so slowly, terrified of making a sound."
                            "Eventually, I was able to peek inside."
                            "Dark..."
                            "I opened the door and poked my head in."
                            scene bg_mason_incabin with dissolve
                            "Once my eyes adjusted, I could see bones and furs..."
                            "It smelled musty, but it was warm."
                            "And sort of cozy... in a way."
                        elif True:
                            scene bg_mason_incabin with dissolve
                            "I opened the door and slid inside."
                            "The skins and bones of animals in here put me on edge."
                            "But at least it was warm..."
                        $ map_location_cabin = "inside"
                        $ location_temp = "warm"
                        $ arrivedby = "idle"
                        jump mason_turn_order
                    elif True:
                        $ phase = "event"
                        scene black with dissolve
                        stop ambient fadeout 1.0
                        "I slowly opened the door."
                        "I wasn't sure if I was shaking from the cold or from worry."
                        "I moved it so slowly, terrified of making a sound."
                        "Eventually, I was able to peek inside."
                        "Dark..."
                        "I opened the door and poked my head in."
                        "A hand pulled me in." with vpunch
                        p "AHH!"
                        scene bg_mason_incabin with dissolve
                        label event_mason_masonshome:
                        play music "music/masons_theme.ogg"
                        show mason at center with Dissolve(0.3)
                        m question "Oh?"
                        m normal "I spend all day looking for you..."
                        m smug "And you're right here."
                        "I fumbled for my knife and tried to swipe at him."
                        hide mason with Dissolve(0.3)
                        "I yelped as he grabbed my weapon arm and twisted it behind my back."
                        scene cg_mason_wall at left
                        $ persistent.cgs_mason.add("cg_mason_wall")
                        $ renpy.save_persistent()
                        play sound "music/sfx_impact_thud.ogg"
                        "He slammed me face-first into the cabin wall" with vpunch
                        "I could feel him breathing behind me."
                        m wistful "Hrm. I really did want this to last longer."
                        m "Barely got any tracking in."
                        "He pressed me tighter and I wheezed."
                        m alert "But, can't have ya knowing where the cabin is."
                        "He let go of my arm and gripped both sides of my head."
                        "I felt a chill of recognition."
                        "No-"
                        scene cg_mason_wall:
                            easein_bounce 0.3 xalign 1.0
                        pause(0.3)
                        scene black
                        $ stat_health -= 100
                        play sound "music/sfx_bone_snap.ogg"
                        stop ambient
                        stop music
                        "With one practiced and brutally strong motion, he snapped my neck." with vpunch
                        "I was unable to move or speak."
                        "I could only lie there for the next few seconds as my senses faded."
                        $ quick_menu = False
                        window hide
                        hide screen effect_health
                        hide screen effect_ice
                        hide screen status
                        $ persistent.endings_mason.add("You visited the cabin")
                        $ persistent.deathcounter += 1
                        $ renpy.save_persistent()
                        call achievement_checker from _call_achievement_checker
                        play music "<from 0.3>music/you_died.ogg"
                        scene bg_endslate with blooddissolve
                        show screen bg_endslate_text("You Died","You visited the cabin")
                        $ renpy.pause(hard=True)
                "Get the hell out of here" if map_location_cabin != "inside":
                    $ map_location = "Meadow"
                    $ arrivedby = "new"
                    jump mason_turn_order

                "Leave the cabin" if map_location_cabin == "inside":
                    $ map_location = "House"
                    $ arrivedby = "idle"
                    $ location_temp = "cold"
                    $ map_location_cabin = "outside"
                    play ambient "music/ambient_forest.ogg" fadein 1.0
                    jump mason_turn_order


    if map_location == "Swamp":

        if sleep > 1:
            label mason_swamp_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump mason_turn_order
        if arrivedby == "wakeup":
            label mason_swamp_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                "I looked around myself and remembered where I was."
                if meme_mode:
                    "No..."
                    "My merman dream..."
                elif True:
                    "I groggily got back up."
                $ arrivedby = "special"
                jump mason_turn_nostats

        if event_mason_discoverswamp == 0:
            $ event_mason_discoverswamp = 1
            "After struggling through the thickest part of the brush, I came to a clearing."
            "... Not a clearing."
            "Some kind of pond... or swamp."
            "It seemed strange that the water wasn't frozen in this cold."
            "I looked back towards the trees before taking out my map."
            "I'd better mark this place down."
            $ map_discovery_swamp = True
            $ renpy.notify("Location Added!")
            "I put away my map and looked out at the still water."
            jump mason_swamp_travel

        if arrivedby == "new" or arrivedby == "chased":
            $ arrivedby = "idle"
            if event_mason_returnswamp == 0 and event_mason_nightmare == 1:
                $ event_mason_returnswamp = 1
                "I approached the dark water again."
                "The same sense of dread from my nightmare began to rise in me."
                "I gulped down my fear and stepped closer to the water."
                "Trying not to get wet, I peered into it."
                "Then I jumped back."
                "Bones."
                "It really is full of bones."
            elif True:
                "I've made it to the water."
        elif arrivedby == "idle":
            $ arrivedby = "idle"
            "I stayed at the swamp."
        label mason_swamp_travel:
            $ phase = "adventure"
            menu:
                "It's completely silent here..."
                "Stay here" if True:
                    $ map_location = "Swamp"
                    $ arrivedby = "idle"
                    jump mason_turn_order
                "Walk back into the woods" if True:
                    $ map_location = "Thicket"
                    $ arrivedby = "new"
                    jump mason_turn_order




label mason_search_subroutine:
    $ phase = "event"
    if map_location == "Meadow" and event_mason_nightmare == 1 and event_mason_findbones == 0:
        $ event_mason_findbones = 1
        "I looked carefully around the tall grasses of the meadow."
        "By the rotting remains of a tree trunk, I spotted something white."
        "I looked more closely, brushing away the dirt and decaying leaves."
        "Bones..."
        "It seemed like most of the skeleton was missing, but from what I could see it looked like it was a deer."
        if meme_mode:
            p "Finally, some good food."
        elif True:
            "I remembered the creature from my dream."
            "... Maybe these can help me."
        $ inventory.append("item_bones")
        $ renpy.notify("Bones Added!")
        show screen inventory
        pause(1.5)
        hide screen inventory
        if meme_mode:
            "I stuffed the bones into my backpack."
        elif True:
            "I gathered a couple of the most intact bones and put them in my backpack."
        $ arrivedby = "special"
        jump mason_turn_order

    if map_location == "Waterfall" and event_mason_discover_beartrap == 0 and total_hours > 36:
        $ event_mason_discover_beartrap = 1
        "I searched the rocky area near the water for something useful."
        "Nothing much has changed since I got here..."
        "A pile of leaves caught my eye."
        "Something about it bothered me."
        "I looked around it."
        "I don't think this was here before..."
        "I crouched near the leaves and lifted a few of them."
        "Fuck!"
        "It's a damn bear trap!"
        "I nearly fell backwards, glad I hadn't set it off."
        "I took a moment to calm down."
        "Okay. I have to disarm this."
        "I looked around and easily found a large branch."
        "I gulped and moved the branch over the trap."
        "Please don't be too loud..."
        "I squeezed my eyes shut and brought the branch down onto the trap's center plate."
        play sound "music/sfx_bear_trap_snap.ogg"
        "Instantly, the crack of splintering wood rang out and I felt the jerk of the wood in my hands."
        "My hands felt clammy."
        "It was hard not to imagine what that would have been like on my leg..."
        "I shook my head and dropped the branch."
        "Now that the trap wasn't a danger, I wondered if I could possibly use it."
        "Although... it looks really heavy."
        "Dragging it around would be difficult."
        menu:
            " "
            "Take the bear trap" if True:
                "This is just too good of an opportunity."
                "If I can figure out how to set this..."
                "I could really turn the tables."
                $ inventory.append("item_beartrap")
                $ renpy.notify("Bear Trap Added!")
                show screen inventory
                pause(1.5)
                hide screen inventory
                "I grabbed the large metal device and lifted it over my backpack."
                $ encumbered = 1
                $ renpy.notify("You are encumbered.")
                "I grunted. It must be at least 30 pounds."
                "This better be worth it..."
                $ arrivedby = "special"
                jump mason_turn_order
            "Leave it" if True:
                "I decided to leave the bear trap on the ground."
                "It's too heavy, and I doubt I'd be able to set it again anyway."
                "Better to just take this victory and not push my luck."
                "I kicked away the branch to make my interference less obvious."
                "Good enough!"
                $ arrivedby = "special"
                jump mason_turn_order

    if map_location == "Waterfall" and 7 <= hours <= 19 and event_mason_findfish == 0:
        $ event_mason_findfish = 1
        "I approached the water of the creek."
        "I could see movement under the water."
        "Fish!"
        "Fish were fighting the current, even in the shallow parts of the creek."
        "I saw some, barely moving, resting in the lee of rocks."
        menu:
            "Try to catch a fish" if True:
                "I quickly sprung into action."
                "I ran back into the bush and found a long stick."
                "I tried to move as quickly as possible... I didn't know how long the fish would be here."
                "I kept an eye on one fish in particular as I pulled out my small knife to whittle a point on to the stick."
                "Once I was satisfied with my 'spear' I approached the creek again."
                "My heart was pounding."
                "I'm probably only going to have one chance at this."
                "My target was practically still."
                "I readied my weapon..."
                play sound "music/sfx_water_splash.ogg"
                "Now!" with vpunch
                "With the furious splashing under my strike, I knew I had done it right."
                "The other fish vanished as I waited for my victim to stop moving."
                "I pulled it out carefully."
                "I did it!"
                if meme_mode:
                    $ inventory.append("item_fish_cute")
                elif True:
                    $ inventory.append("item_fish")
                $ renpy.notify("Fish Added!")
                show screen inventory
                pause(1.5)
                hide screen inventory
                if achievement.has("ach_a_reel_nice_catch") != True:
                    $ persistent.ach_a_reel_nice_catch = True
                    $ achievement.grant("ach_a_reel_nice_catch")
                    init:
                        $ achievement.register("ach_a_reel_nice_catch")
                        $ achievement.sync()
                        $ renpy.save_persistent()
                        if persistent.ach_a_reel_nice_catch == True and achievement.has("ach_a_reel_nice_catch") != True:
                            $ achievement.grant("ach_a_reel_nice_catch")
                            $ achievement.register("ach_a_reel_nice_catch")
                            $ achievement.sync()
                "I really caught a fish!"
                $ arrivedby = "special"
                jump mason_turn_order
            "Leave them alone" if True:
                "I looked at the fish and considered killing one to feed myself."
                "..."
                "I don't want to..."
                "I huffed and raised my chin."
                "There's gotta be other options out here."
                $ arrivedby = "special"
                jump mason_turn_order

    if map_location == "Thicket" and event_mason_findberries == 0 and 8 <= hours <= 18:
        $ event_mason_findberries = 1
        "I searched around me for something useful."
        "I wandered through the trees, trying to remember where I'd been."
        "After several minutes of wandering, I spotted some color."
        "Two bushes, not very far apart, seemed to have berries on them."
        "One had small, purplish blue berries."
        "They looked a bit like blueberries..."
        "The other had bright red, juicy looking berries."
        "These ones looked sort of like cranberries."
        menu:
            " "
            "Pick the blue berries" if True:
                "The blue berries seemed like the safe option."
                $ inventory.append("item_saskatoons")
                $ renpy.notify("Berries Added!")
                show screen inventory
                pause(1.5)
                hide screen inventory
                "I picked all the ones I could find."
                $ arrivedby = "special"
                jump mason_turn_order
            "Pick the red berries" if True:

                "The red berries seemed like the safe option."
                $ inventory.append("item_baneberries")
                $ renpy.notify("Berries Added!")
                show screen inventory
                pause(1.5)
                hide screen inventory
                "I picked all the ones I could find."
                $ arrivedby = "special"
                jump mason_turn_order
            "Pick both" if True:

                "Well... beggars can't be choosers."
                "I might as well take what I can get."
                $ inventory.append("item_baneberries")
                $ inventory.append("item_saskatoons")
                $ renpy.notify("Berries Added!")
                show screen inventory
                pause(1.5)
                hide screen inventory
                "I picked all the berries I could find."
                $ arrivedby = "special"
                jump mason_turn_order
            "Leave them alone" if True:

                $ event_mason_findberries = 0
                "I'm not quite desperate enough to be eating strange berries yet."
                "I decided to leave them all alone."
                $ arrivedby = "special"
                jump mason_turn_order

    if map_location == "Tall Tree" and event_mason_discover_snare == 0 and total_hours > 24:
        $ event_mason_discover_snare = 1
        "I searched around the dark forest floor for something useful."
        "A glint just barely caught my eye."
        "I looked closer and saw... wire?"
        "Around it was a strange display of raised sticks in a 'T' shape."
        "They were blending in before, but now they seemed obvious."
        "As I followed the wire to the tree with my eyes I supressed a shudder."
        "It's a snare."
        "A really big one..."
        "I gulped."
        "I'm really glad I spotted this before stepping in it."
        "I touched the wire."
        "It's sharp..."
        menu:
            " "
            "Dismantle the snare" if True:
                $ event_mason_snare_dismantle = 0
                "I'm not leaving this up."
                "I looked carefully for the ring of wire at the base of the trap."
                "Using a branch from the forest floor, I pushed the center stick of the contraption."
                play sound "music/sfx_cord.ogg"
                "The wire whipped up past me."
                "I let out a relieved sigh."
                "Not this time, asshole..."
            "Leave it up" if True:
                $ event_mason_snare_dismantle = 1
                "I decided to just leave it be and remember its location."
                "Maybe he'll wander into it himself."
                p "Heh..."
        $ arrivedby = "special"
        jump mason_turn_order

    if map_location == "Meadow":
        "I looked carefully around the tall grasses of the meadow."
        "I searched hard, but I couldn't find anything useful."
        $ arrivedby = "special"
        jump mason_turn_order
    if map_location == "Thicket":
        "I looked carefully through the bush among the trees."
        "I searched hard, but I couldn't find anything useful."
        $ arrivedby = "special"
        jump mason_turn_order
    if map_location == "Tall Tree":
        "I looked carefully through the bush among the base of the tall tree."
        "I searched hard, but I couldn't find anything useful."
        $ arrivedby = "special"
        jump mason_turn_order
    if map_location == "Waterfall":
        if 7 <= hours <= 19:
            "I looked carefully around the rocks and in the water."
            "There doesn't seem to be fish in the water or anything useful around here right now."
            "I searched hard, but I couldn't find anything useful."
        elif True:
            "I searched around the rocks and water."
            "... I can hardly see anything."
        $ arrivedby = "special"
        jump mason_turn_order
    if map_location == "Swamp":
        "I searched the area around the water."
        "The dying and dead foliage around the shore gave off an earthy smell."
        "The water is too still..."
        "Every time I looked toward the swamp, I got an urge to walk in."
        "There's something wrong with this place."
        $ arrivedby = "special"
        jump mason_turn_order
    if map_location == "House":
        if map_location_cabin == "inside":
            if event_mason_offerbones == 1:
                "I remembered what that voice from the swamp told me."
                "I looked around the room and spotted a thick bear hide hung on the wall behind me."
                "I tentatively grabbed it and looked behind it."
                "I gasped."
                "Carved in the wooden wall was a shelf just big enough to hold a winchester rifle."
                "A gun!"
                "I carefully grabbed it and checked-"
                play sound "music/sfx_gun_click.ogg"
                play music "music/ambient_drone_intermittent.ogg" fadein 3.0
                "... It's loaded."
                "My heart pounded in my ears."
                "This changes everything!"
                scene cg_mason_cabindoor with dissolve
                $ persistent.cgs_mason.add("cg_mason_cabindoor")
                $ renpy.save_persistent()
                "I looked towards the cabin door."
                "It looks like I'm the hunter now."
                "I decided my best bet would be to wait here, where it's warm."
                "He has to come back here sometime."
                "The minutes stretched into hours."
                "They seemed to last days, with how tense I was."
                "I almost jumped up when I heard those heavy footsteps approaching from outside."
                "This is it!"
                play sound "music/sfx_gun_click.ogg"
                "I aimed the rifle at the door and tried to breathe evenly."
                "The knob rattled."
                "Everything seemed to be moving in slow motion."
                play sound "<from 0.0 to 1.5>music/sfx_gunshot_rifle.ogg"
                stop music
                stop ambient
                show mason2 shot1
                show mason shot2 with shot
                show screen disableclick(3)
                "He swung the door open and I fired.{w=3.0}{nw}" with vpunch
                m "G... hrk..."
                "For what felt like a whole minute, we just stared at each other."
                hide mason2
                show mason knees
                "Then, the spell was broken and he fell to his knees."
                "For a moment, I saw something strange."
                "The smallest smile."
                "Almost like he was proud."
                "Or maybe I was just imagining things."
                scene cg_mason_dead with dissolve
                $ persistent.cgs_mason.add("cg_mason_dead")
                $ renpy.save_persistent()
                if achievement.has("ach_firepower") != True:
                    $ persistent.ach_firepower = True
                    $ achievement.grant("ach_firepower")
                    init:
                        $ achievement.register("ach_firepower")
                        $ achievement.sync()
                        $ renpy.save_persistent()
                        if persistent.ach_firepower == True and achievement.has("ach_firepower") != True:
                            $ achievement.grant("ach_firepower")
                            $ achievement.register("ach_firepower")
                            $ achievement.sync()
                "He slumped to the floor and I kept the rifle on him."
                play sound "<from 2.7 to 4.0>music/sfx_gunshot_rifle.ogg"
                "I fired again, just to be sure." with vpunch
                "And he didn't move."
                "It took several more minutes for me to gain the courage to step forward and move again."
                "He's... really dead."
                "I kicked his body." with vpunch
                "I began to breathe easily."
                call mason_display_subroutine from _call_mason_display_subroutine_1
                "Now I just have to get out of here."
                "As I tried to clear my head, I heard the faintest whisper."
                lich "You did well."
                play sound "music/sfx_scrape_fast.ogg"
                lich "Hunter."
                "Once again, I looked around in vain for the source of the voice."
                "Then I shook my head."
                "I won't be distracted."
                "I searched the cabin and the body."
                "It didn't take long to find keys and a way to get out of here."
                scene black with dissolve
                hide screen effect_health
                hide screen effect_ice
                "I made my way back to civilization."
                "I made my way back to my home."
                "I never talked about what happened to me."
                "... Or the man I killed."
                "And after some time, for the most part, I managed to rest easy."
                "Aside from the odd strange nightmare."
                "About an endless river."
                "And a voice."
                "That told me I'd come home soon."
                $ quick_menu = False
                window hide
                hide screen status
                $ persistent.endings_mason.add("You made a friend")
                $ renpy.save_persistent()
                call achievement_checker from _call_achievement_checker_1
                play music "<from 0.4>music/music_killer.ogg" fadein 1.0
                scene bg_endslate_survival with zoomdissolve
                show screen bg_endslate_survival_text("You Lived","You made a friend")
                $ renpy.pause(hard=True)
            elif True:

                "I got to work searching the inside of the cabin."
                "I checked the shelves and cupboards."
                "I tried to ignore the fake glass eyes and the open skull sockets watching me."
                "Tools for cooking and carving..."
                "Strange dark brown leather and furs..."
                "Everything seemed to be handmade..."
                "How could there be nothing useful?"
                "It was a small, albiet somewhat creepy, living area."
                "Not a single weapon, at least nothing bigger or more dangerous than the knife I already have."
                "I sighed in frustration."
                $ arrivedby = "special"
                jump mason_turn_order
        elif True:
            "I searched around the outside of the cabin."
            "There didn't seem to be any sign of anything useful."
            "No vehicle, no weapons..."
            "Nothing."
            $ arrivedby = "special"
            jump mason_turn_order


label event_mason_arrivetalltree:
    $ phase = "event"
    $ event_mason_arrivetalltree = 1
    "One of the trees stood out among the rest."
    "It's a lot bigger."
    "If I could get to the top..."
    "Maybe I could find a way out of here?"
    $ arrivedby = "special"
    jump mason_turn_nostats

label event_mason_arrivewaterfall:
    $ phase = "event"
    $ event_mason_arrivewaterfall = 1
    "After following the sound of water, I came to a creek."
    "The lazy stream was actually kind of pretty..."
    $ stat_sanity += 5
    "It made me feel a little better."
    $ arrivedby = "special"
    jump mason_turn_nostats

label event_mason_crossbow_1:
    $ phase = "event"
    if event_mason_crossbow_1 == 0:
        $ event_mason_crossbow_1 = 1
        $ grace_period = 3
        if arrivedby == "sleep" or arrivedby == "wakeup":
            $ stat_health -= 15
            $ sleep = 0
            call mason_display_subroutine from _call_mason_display_subroutine_2
            stop ambient
            play sound "music/sfx_knife_stab.ogg"
            $ wound = 1
            "I was woken up with a blinding pain in my leg." with vpunch
            "I sat up in fear and confusion."
        elif arrivedby == "idle":
            stop ambient fadeout 1.0
            "Something was wrong."
            "I looked around myself, trying to find the source of my unease."
            "The birds..."
            "The animals weren't making any sound."
            if meme_mode:
                "He's right behind me, isn't he."
            $ stat_health -= 15
            play sound "music/sfx_knife_stab.ogg"
            queue sound "music/sfx_impact_forest.ogg"
            $ wound = 1
            "I was knocked to my knees." with vpunch
            "Then I felt the pain."
        elif True:
            stop ambient fadeout 1.0
            "As I walked forward, I noticed my pace slowing."
            "Something was wrong."
            "I stopped and looked around myself."
            "The birds..."
            "The animals weren't making any sound."
            if meme_mode:
                "He's right behind me, isn't he."
            $ stat_health -= 15
            play sound "music/sfx_knife_stab.ogg"
            queue sound "music/sfx_impact_forest.ogg"
            $ wound = 1
            "I was knocked to my knees." with vpunch
            "Then I felt the pain."
        "I gripped the ground and half-stifled a scream."
        "I looked down and could see the tip of a crossbow bolt protruding from the front of my thigh."
        "I quickly whipped around, trying to see where it came from."
        "He's here..."
        menu:
            "I saw the slightest movement from behind a tree."
            "Run" if True:
                "I turned on my heel and ran as fast as I could."
                "The pain seemed to fade away with the fear and adrenaline."
                $ fire = 0
                $ location_temp = "cold"
                stop music fadeout 0.5
                hide campfire with dissolve
                scene black with dissolve
                "I ran for as long as I could."
                $ stat_energy -= 10
                "My foot began to drag."
                "My leg was no longer obeying me."
                "I heaved, unsure of how long I'd actually been running."
                "I slumped to the ground, my heart pounding."
                $ stat_health -= 10
                "My leg was covered in blood."
                "I think I got away."
                "I glanced down at my bloody leg while catching my breath."
                "I can't keep running with this..."
                "I gripped the tip poking out of my pant leg in the front."
                $ stat_sanity -= 10
                "All the pain came flooding back."
                "I clenched my teeth and pulled hard."
                $ stat_health -= 5
                "Thankfully the bolt came out fairly easily."
                "I held my leg with as much pressure as I could, hoping that it would stop bleeding."
                "Judging by the slow ooze of blood, it hadn't managed to hit any major artery."
                $ renpy.notify("You are wounded.")
                "I breathed slowly on the ground, clutching my leg."
                if map_location != "Meadow":
                    $ map_location = "Meadow"
                    play ambient "music/ambient_forest.ogg" fadein 1.0
                    call mason_display_subroutine from _call_mason_display_subroutine_3
                    $ arrivedby = "new"
                elif True:
                    $ map_location = "Thicket"
                    play ambient "music/ambient_forest.ogg" fadein 1.0
                    call mason_display_subroutine from _call_mason_display_subroutine_4
                    $ arrivedby = "new"
                jump mason_turn_nostats
            "Hide" if True:
                "I knew I couldn't run now."
                "I moved quickly and tried to stay low as I looked for cover."
                "The movement I saw was far away, I have enough time..."
                "I spotted a dip in the ground and the fallen trunk of a dead tree."
                $ fire = 0
                $ location_temp = "cold"
                stop music fadeout 0.5
                hide campfire with dissolve
                scene cg_mason_log with dissolve
                $ persistent.cgs_mason.add("cg_mason_log")
                $ renpy.save_persistent()
                "I slid in close to it and laid down against the ground."
                "I tried to steady my breathing and listen past my pounding heartbeat."
                "Soon, the slow and soft crunching of dead leaves hit me."
                "I bit my lip as the sound got closer."
                play sound "music/sfx_twig_snap_2.ogg"
                "Soon he was so close, I could swear I could hear him breathing."
                "No... no..."
                "A quiet low chuckle."
                "I squeezed my eyes shut, bracing myself."
                "..."
                "Then the footsteps walked away."
                "I dug my fingers into the earth below me."
                "He was really leaving!"
                "I stayed there long after I couldn't hear him."
                "Until I couldn't feel my hands and I was certain he was gone."
                "As I tentatively moved to sit up, I became more aware of the throbbing in my leg."
                "... I won't be able to walk with this."
                "I gripped the tip poking out of my pant leg in the front."
                $ stat_sanity -= 10
                "All the pain came flooding back."
                "I clenched my teeth and pulled hard."
                $ stat_health -= 5
                "Thankfully the bolt came out fairly easily."
                "I held my leg with as much pressure as I could, hoping that it would stop bleeding."
                "Judging by the slow ooze of blood, it hadn't managed to hit any major artery."
                $ renpy.notify("You are wounded.")
                "I breathed slowly on the ground, clutching my leg."
                play ambient "music/ambient_forest.ogg" fadein 1.0
                $ arrivedby = "special"
                call mason_display_subroutine from _call_mason_display_subroutine_5
                jump mason_turn_nostats
    elif True:
        jump event_mason_crossbow_2

label event_mason_crossbow_2:
    $ phase = "event"
    if event_mason_crossbow_2 == 0:
        $ event_mason_crossbow_2 = 1
        $ grace_period = 3
        $ wound = 2
        if arrivedby != "sleep":
            play sound "<from 0.0 to 1.0>music/sfx_bolt_wood.ogg"
            "I heard a loud crack."
            "I jumped at the loud sound and whipped around, looking for the source."
        elif True:
            $ sleep = 0
            call mason_display_subroutine from _call_mason_display_subroutine_6
            play sound "<from 0.0 to 1.0>music/sfx_bolt_wood.ogg"
            "I heard a loud crack."
            "The loud sound startled me awake."
            "I climbed to my feet and looked for the source of the sound."
        "I spotted it easily and stumbled backwards."
        "I stared in horror at the bolt protruding from the tree bark next to me."
        "I turned to where the end of the bolt was pointing and saw him."
        "Everything felt so slow, like I was trying to move during a nightmare."
        "I saw the second bolt in the air."
        $ stat_health -= 10
        scene black
        play sound "music/sfx_knife_stab.ogg"
        "I felt the punch and yank on my arm." with vpunch
        "I was knocked off balance and fell backwards with a soft thud."
        if health <= 0:
            jump bloodjumper
        "I was still a deer in headlights."
        "I wanted to scream but it felt like it was stuck inside my throat."
        "Finally, I began to gain control of my body again and began to scramble-"
        "As a boot landed on my chest." with vpunch
        if meme_mode:
            p "Aw, beans."
        elif True:
            p "No- Wait!"
        play music "music/masons_theme.ogg" fadein 1.0
        m smirk "You're not so hard to find, are ya?"
        $ fire = 0
        $ location_temp = "cold"
        hide campfire with dissolve
        scene cg_mason_armbolt1 with dissolve
        $ persistent.cgs_mason.add("cg_mason_armbolt")
        $ renpy.save_persistent()
        "I strained against his weight as he bent down."
        "My eyes widened as he grabbed the bolt currently through my arm."
        p "NO!"
        show cg_mason_armbolt1 at tension_vibrate
        pause(1.0)
        show cg_mason_armbolt2:
            xalign 0.5
            yalign 0.5
            xanchor 0.5
            yanchor 0.5
            zoom 1.05
            easeout 0.25 zoom 1.0
        $ stat_health -= 5
        $ stat_sanity -= 10
        "He yanked it from my flesh in one mercilessly rough motion." with vpunch
        "I screamed loudly and clearly."
        if health <= 0:
            jump bloodjumper
        "It seemed to ring through the cold air."
        "I realized he leaned closer as I gasped for air."
        m empty "You got an animal's scream."
        m empty "Gets the heart pumping..."
        menu:
            " "
            "'Why are you doing this!?'" if True:
                "I yelled at him and struggled."
                "He looked at me for a moment before letting out a small huff of a laugh."
                m empty "Aye, you think I'm crazy, then?"
                p "You are!"
                m empty "You know what happens to deer without wolves?"
                "What the hell is he talking about now?"
                "He seemed to pick up on my confusion."
                m empty "Deer."
                m empty "They multiply and eat everything."
                m empty "Then they get sick."
                m empty "They starve and die."
                "He paused for a moment, as if I was supposed to get some punchline."
                m empty "Everything needs to be hunted."
                m empty "People are getting mighty sick out there."
                $ sanity -= 10
                "I shivered."
                "He's completely insane."
            "'Get off me!'" if True:
                "I struggled as hard as I could."
                "He was massive and didn't budge."
                "Still, I needed to try everything."
                "I grunted as he pressed down a bit harder."
            "'Please don't hurt me...'" if True:
                "I spoke meekly."
                "I had no other options."
                m empty "Already gone soft, eh?"
                "He looked me right in the eyes and smiled fondly, like he was recounting a warm memory."
                m empty "There's something I really like about people."
                m empty "The critters around here never do any beggin'."
                m empty "But you're smarter than that."
                $ sanity -= 10
                "His voice and expression were so warm, but I was shivering."
                "I could tell this wasn't the kind of fondness that meant anything good for me."
            "-Say nothing-" if True:
                "I stayed still and silent."
                "I wasn't in a position to fight and there was nothing to say."
        "He flashed a small grin."
        scene cg_mason_armbolt1 with dissolve
        m empty "So... how's the leg holding up?"
        "His words made me look down."
        "Dark blood was caked all around my thigh, soaked through my pants."
        "I almost didn't notice him licking his thumb before he had it pressed to the wound on my leg."
        "I had no time to react."
        $ stat_health -= 5
        $ stat_sanity -= 15
        "I cried out hoarsely as he shoved his thumb deep into my thigh."
        "My cry ended in a wheezing sob as I tried to curl in on myself."
        "The pain was blinding."
        if health <= 0:
            jump bloodjumper
        call mason_display_subroutine from _call_mason_display_subroutine_7
        show mason with dissolve
        m normal "Careful, now."
        "I began to shake involuntarily as he stood up."
        m smug "A hole like that's gonna slow you down."
        $ renpy.notify("You are gravely wounded.")
        "I tried to hold my injured leg with my bleeding arm."
        "He stepped away from me, and to my surprise, began backing away."
        hide mason with dissolve
        stop music fadeout 1.0
        "I just watched in confusion as he nodded to me once and then turned around to walk away."
        p "W... what..?"
        "He disappeared into the trees."
        "Why was he leaving me?"
        "I squeezed my torn up arm and tried to avoid thinking what I knew was the answer."
        "{i}He was playing with me.{/i}"
        $ arrivedby = "special"
        jump mason_turn_nostats
    elif True:
        jump event_mason_crossbow_3
label event_mason_crossbow_3:
    $ phase = "event"
    if event_mason_crossbow_3 == 0:
        $ event_mason_crossbow_3 = 1
        $ grace_period = 3
        if arrivedby == "sleep" or arrivedby == "wakeup":
            $ stat_health -= 20
            $ sleep = 0
            call mason_display_subroutine from _call_mason_display_subroutine_8
            play sound "music/sfx_knife_stab.ogg"
            "I woke up screaming." with vpunch
            "I looked down to the source of the pain and saw the bolt sticking out of my gut."
            play music "music/masons_theme.ogg" fadein 1.0
            m surprised "Heh!"
            m smirk "Just lyin' around waitin for me, eh?"
        elif arrivedby == "idle":
            "I clutched at my leg, the ache kept coming in waves."
            "I was looking down at the ground in front of me when I heard the click."
            "I froze."
            play music "music/masons_theme.ogg" fadein 1.0
            show mason crossbow with dissolve
            "He was directly in front of me."
            "I stared down the loaded crossbow in his hands."
            m "Not paying much attention anymore, are ya?"
            $ stat_health -= 20
            play sound "music/sfx_impact_thud.ogg"
            "I opened my mouth to speak, but I was interrupted by the force of the bolt in my gut." with vpunch
            hide mason with dissolve
            "He closed the distance between us casually."
        elif True:
            "I clutched at my leg, walking with a limp."
            "I was looking down at the ground in front of me when I heard the click."
            "I froze."
            play music "music/masons_theme.ogg" fadein 1.0
            show mason crossbow with dissolve
            "He was directly in front of me."
            "I stared down the loaded crossbow in his hands."
            m "You just came right to me this time, eh?"
            $ stat_health -= 20
            play sound "music/sfx_impact_thud.ogg"
            "I opened my mouth to speak, but I was interrupted by the force of the bolt in my gut." with vpunch
            hide mason with dissolve
            "He closed the distance between us casually."
        "I couldn't breathe or cry out."
        if sanity <= 30:
            m wistful3 "Ahh. Look at ya.{p=0.5}{nw}"
        m wistful2 "Ahh. Look at ya."
        m "I think you've run your last."
        "He pulled out a small knife with a white handle."
        "I tried to talk again, but coughed from the effort."
        "It was wet."
        scene cg_mason_gutting1 with dissolve
        $ persistent.cgs_mason.add("cg_mason_gutting1")
        "He crouched down close to me."
        m empty "I want to thank ya."
        m empty "It's been a good hunt."
        "He let out a single gruff laugh."
        m empty "Even if ya did wander round right to me at the end!"
        $ stat_health -= 20
        scene cg_mason_gutting2 with dissolve
        $ persistent.cgs_mason.add("cg_mason_gutting2")
        $ renpy.save_persistent()
        play sound "music/sfx_knife_stab.ogg"
        "Without warning, he plunged the small knife into my gut." with vpunch
        play sound "music/sfx_blood_drip.ogg"
        "I coughed more wetness as he slid the knife upward."
        "It seemed surreal and wrong, how soft I was."
        "Somehow, the pain seemed to be taking a back seat to the absurdity of the view."
        m empty "Got really pretty skin."
        "He wiped his brow, smiling."
        $ stat_health -= 10
        "He shoved his fingers into the open gash on my abdomen and grabbed a handful of my bleeding skin."
        "I lurched, and only blood came up through my mouth."
        "I couldn't take in a breath."
        "I was drowning."
        "As I saw him begin to slice further down to my hips, I was briefly thankful that I couldn't breathe."
        stop music fadeout 1.0
        stop ambient fadeout 1.0
        scene black with dissolve
        $ stat_health -= 100
        if achievement.has("ach_the_perfect_hunt") != True:
            $ persistent.ach_the_perfect_hunt = True
            $ achievement.grant("ach_the_perfect_hunt")
            init:
                $ achievement.register("ach_the_perfect_hunt")
                $ achievement.sync()
                $ renpy.save_persistent()
                if persistent.ach_the_perfect_hunt == True and achievement.has("ach_the_perfect_hunt") != True:
                    $ achievement.grant("ach_the_perfect_hunt")
                    $ achievement.register("ach_the_perfect_hunt")
                    $ achievement.sync()
        "The last thing I heard was his whistling."
        $ quick_menu = False
        window hide
        hide screen effect_health
        hide screen effect_ice
        hide screen status
        $ persistent.endings_mason.add("Your hunt is over")
        $ persistent.deathcounter += 1
        $ renpy.save_persistent()
        call achievement_checker from _call_achievement_checker_2
        play music "<from 0.3>music/you_died.ogg"
        scene bg_endslate with blooddissolve
        show screen bg_endslate_text("You Died","Your hunt is over")
        $ renpy.pause(hard=True)

label mason_talltree_climbtree:
    $ phase = "event"
    if (event_mason_discoverhouse == 0) and (7 < hours < 19):
        label event_mason_discoverhouse:
            $ event_mason_discoverhouse = 1
            "I grabbed hold of the sturdier looking branches and began to climb the tallest tree."
            $ stat_energy -= 1
            $ stat_food -= 1
            if event_mason_crossbow_1 == 1:
                "I hissed in pain as the effort reawakened fresh pain in my injured leg."
                "I breathed deeply and kept moving."
            "After some progress, my limbs began to ache from the effort."
            $ stat_energy -= 1
            $ stat_food -= 1
            "I kept moving, trying not to look down."
            play music "music/ambient_wind.ogg" fadein 1.0
            scene cg_mason_treeview_day with dissolve
            $ persistent.cgs_mason.add("cg_mason_treeview")
            $ renpy.save_persistent()
            "Finally, I saw light."
            "I moved a bit higher up and saw the tops of the trees around me."
            "It might have been beautiful if I was in a different situation."
            "I took a deep breath and looked around for any kind of road or something that could help me."
            "I spotted the meadow I had been released in... and..."
            "Something dark. Something manmade!"
            "I squinted. It was definitely a cabin."
            "I took note of the sun's position and where the cabin was."
            "It looks like I can get to it from that meadow."
            "A gust of wind shook the top of the tree as I clung to the branches."
            "It's pretty cold and dangerous up here... I'd better go back down."
            stop music fadeout 2.0
            call mason_display_subroutine from _call_mason_display_subroutine_9
            "I carefully climbed back down the tree to safety."
            if "item_map" in inventory:
                "I pulled out the crumpled map."
                $ map_discovery_house = True
                $ map_discovery_talltree = True
                $ renpy.notify("Map Updated!")
                "I did my best to sketch its location."
                "I won't forget where it is now."
            elif True:
                "I pulled out the crumpled paper and pencil."
                "I need to remember where it was..."
                $ map_discovery_house = True
                $ map_discovery_talltree = True
                $ inventory.remove("item_paper")
                $ inventory.append("item_map")
                $ renpy.notify("Location Drawn!")
                "I did my best to sketch something."
                "This will probably be better if I draw some other locations too."
                "I put it away."
                "It'll have to do for now."
            $ arrivedby = "special"
            jump mason_turn_nostats
    if (7 <= hours <= 19):
        "I looked up at the tree and grabbed a branch to hoist myself up."
        $ stat_energy -= 1
        $ stat_food -= 1
        if event_mason_crossbow_1 == 1:
            "I hissed in pain as the effort reawakened fresh pain in my injured leg."
        "I breathed hard as I climbed the tree, using the limbs I knew were strong enough."
        $ stat_energy -= 1
        $ stat_food -= 1
        "I kept moving, trying not to look down."
        if hours == 7:
            scene cg_mason_treeview_morning
        elif hours == 19:
            scene cg_mason_treeview_evening
        elif True:
            scene cg_mason_treeview_day
        play music "music/ambient_wind.ogg" fadein 1.0
        $ persistent.cgs_mason.add("cg_mason_treeview")
        $ renpy.save_persistent()
        "As I broke above the canopy, I could see the mountains around me through the fog of my breath."
        $ stat_sanity += 20
        "For a moment I felt detached from my current reality."
        "It really was kind of beautiful up here."
        "..."
        "My hands were getting cold and I knew I'd better climb back down."
        stop music fadeout 1.0
        call mason_display_subroutine from _call_mason_display_subroutine_10
        "I carefully descended and returned to the bottom of the tree."
        $ arrivedby = "special"
        jump mason_turn_nostats
    if (7 > hours) or (hours > 19):
        "I looked up at the tree and grabbed a branch to hoist myself up."
        $ stat_energy -= 1
        $ stat_food -= 1
        if event_mason_crossbow_1 == 1:
            "I hissed in pain as the effort reawakened fresh pain in my injured leg."
            "I breathed deeply and kept moving."
        "It was hard to see which branch to pick in the darkness."
        $ stat_energy -= 1
        $ stat_food -= 1
        "I kept climbing slowly, trying not to look down."
        play music "music/ambient_wind.ogg" fadein 1.0
        scene cg_mason_treeview_night
        $ persistent.cgs_mason.add("cg_mason_treeview")
        $ renpy.save_persistent()
        "As I broke above the canopy, I could see starlight."
        "The forest around me was like a black sea, frozen in time."
        $ stat_sanity += 20
        "For a moment I felt detached from my current reality."
        "It really was kind of beautiful up here."
        "..."
        "My hands were getting cold and I knew I'd better climb back down."
        stop music fadeout 1.0
        call mason_display_subroutine from _call_mason_display_subroutine_11
        "I carefully descended and returned to the bottom of the tree."
        $ arrivedby = "special"
        jump mason_turn_nostats

label event_mason_buildfire:
    $ phase = "event"
    "I searched around for some small dry bits to start my fire with."
    "Luckily, there seemed to be plenty to work with."
    "I gathered some wood and started to work with the flint."
    $ fire = 1
    $ location_temp = "warm"
    play sound "<from 0.0 to 2.0>music/sfx_flint.ogg"
    play music [ "<silence 2.0>", "music/ambient_small_fire.ogg" ]
    show campfire
    "As the spark caught the tinder, I felt a sigh of relief."
    "The warmth from the flickering light reached my hands and filled me with comfort."
    $ arrivedby = "special"
    jump mason_turn_nostats


label event_mason_housefire:
    $ phase = "event"
    if sanity < 50:
        "I looked down at my flint."
        stop ambient fadeout 1.0
        "... Now there's an idea."
        "I'm going to die here."
        "But I don't have to go down alone..."
        if map_location_cabin == "inside":
            "I looked around the cabin and easily found a dry cloth."
            "This place is all wood."
            play sound "<from 0.0 to 2.0>music/sfx_flint.ogg"
            "I struck the flint."
            "It only took a couple tries."
            "My heart was pounding."
            "After watching the flame spread on the cloth to the wall, I left the cabin."
            $ map_location_cabin = "outside"
            call mason_display_subroutine from _call_mason_display_subroutine_12
        elif True:
            "There are dry twigs everywhere."
            "I got up close to the cabin."
            play sound "<from 0.0 to 2.0>music/sfx_flint.ogg"
            "I struck the flint."
            "It only took a couple tries."
            "My heart was pounding."
        play ambient "music/ambient_small_fire.ogg" fadein 1.0
        hide screen effect_ice with dissolve
        "It spread surprisingly quickly."
        play ambient "music/ambient_large_fire.ogg" fadein 1.0
        scene cg_mason_cabinfire with dissolve
        $ persistent.cgs_mason.add("cg_mason_cabinfire")
        $ renpy.save_persistent()
        "One minute it was a flickering flame, the next, a towering inferno engulfing the front of the cabin."
        "I could feel the heat, and I took a few steps back."
        "And froze."
        "Behind me..."
        "His thick arm was around my throat before I could turn around."
        "My feet left the ground briefly from the force of it." with vpunch
        "I grasped at his elbow and tried to yell."
        "I couldn't get much sound out."
        play music "music/masons_theme.ogg" fadein 1.0
        m angry "You..."
        "He was growling in my ear."
        if meme_mode:
            p "I set your DILF cabin on fire..."
            p "Heh..."
        m "Think you're clever, eh?"
        "The arm around my neck tightened."
        "A strange twinge of pain told me that if he chokes me any harder, my neck will snap."
        p "S... sto..."
        "My plea was ignored as he lifted my now limp body."
        play sound "music/sfx_fire_whoosh.ogg"
        "I heard the explosion of something inside the cabin and watched the flames tower higher."
        $ stat_health -= 100
        play sound "music/sfx_bone_snap.ogg"
        "I felt another pop, but this time it wasn't the fire." with vpunch
        "I could no longer feel anything."
        "Yet the fire danced, and I smiled."
        hide screen effect_health
        scene black with eyedissolve
        stop music fadeout 1.0
        stop ambient fadeout 1.0
        "As I blacked out, I could hear him roaring in anger."
        "The satisfied grin stayed on my face."
        $ quick_menu = False
        window hide
        hide screen status
        $ persistent.endings_mason.add("Your flame is out")
        $ persistent.deathcounter += 1
        $ renpy.save_persistent()
        call achievement_checker from _call_achievement_checker_3
        play music "<from 0.3>music/you_died.ogg"
        scene bg_endslate with blooddissolve
        show screen bg_endslate_text("You Died","Your flame is out")
        $ renpy.pause(hard=True)
    elif True:
        $ arrivedby = "special"
        "I really don't think it would be a good idea to build a fire here..."
        jump mason_turn_nostats

label event_mason_swampfire:
    $ phase = "event"
    "There doesn't seem to be anything dry around here that I can burn..."
    $ arrivedby = "special"
    jump mason_turn_nostats

label event_mason_cabin_sleep:
    $ phase = "event"
    if (sanity < 30 and map_location_cabin == "inside") or energy == 0:
        $ phase = "event"
        "It's nice and warm in here..."
        "I looked around the cabin and easily found a large bed."
        "A real bed..."
        "I crawled onto the soft surface."
        "Like the rest of the furniture, it was covered in furs."
        "Who cares anymore..."
        "It's just as dangerous anywhere else."
        "I might as well be comfortable."
        scene black with eyedissolve
        hide screen effect_ice
        "I curled up on the blankets and furs, and immediately dozed off."
        pause 3.0
        "As I felt my body gently swaying, for a moment I was lost in time."
        "Living in the memory of being almost entirely asleep as a parent carried me off to my own bed."
        "No... this isn't right."
        scene cg_mason_carry with eyedissolve_reverse
        $ persistent.cgs_mason.add("cg_mason_carry")
        $ renpy.save_persistent()
        play music "music/masons_theme.ogg" fadein 1.0
        "I jolted awake, going stiff at the face of the man holding me."
        m empty "G'morning, 'Goldilocks'."
        "He chuckled."
        m empty "Though I s'pose it's more evening than morning."
        "This can't be real."
        "I squirmed for a moment and his grip immediately went from gentle to crushing."
        m empty "Aye, not so fast."
        m empty "Yer all out of run anyway."
        "A calloused hand squeezed my arm."
        m empty "I can feel you've gone all soft."
        "How was he holding me so tightly?"
        "It felt like my bones were grinding together."
        "I wheezed in pain."
        "Then I realized he'd carried me outside."
        "Where..?"
        scene cg_mason_stump with dissolve
        $ persistent.cgs_mason.add("cg_mason_stump")
        $ renpy.save_persistent()
        play sound "music/sfx_impact_forest.ogg"
        "I yelped as his arms opened up and I was dropped to the hard ground." with vpunch
        scene cg_mason_stump:
            align (0.5,0.0)
            xanchor 0.5
            yanchor 0.0
            easein 0.1 zoom 1.5
            easeout 0.1 zoom 1.48
        "Before I could scramble to my feet, he grabbed the back of my coat and dragged the upper half of my body onto a large stump."
        "He held my chest down."
        "I suddenly felt strangely overwhelmed by my senses."
        "The strong arm pinning me to the stump."
        "The smell of cut lumber."
        "The painful surface of the marked up, jagged wood."
        "Movement in the corner of my eye... was that..?"
        "Please no..."
        m wistful2 "Don't worry, I'll do ya quick."
        "His boot replaced his hand on my back." with vpunch
        "The voice of defeat told me not to squirm anymore."
        "I clenched my teeth and bared the back of my neck."
        scene black
        hide screen effect_health
        hide screen status
        stop music
        stop ambient
        play sound "music/sfx_axe_chop.ogg"
        "I heard the dull thump and felt the force of the axe." with vpunch
        "But I didn't feel any pain."
        "For one horrifying, dizzying moment, I could feel the world spinning without my body."
        "And then nothing."
        $ quick_menu = False
        window hide
        hide screen status
        $ persistent.endings_mason.add("You lost your head")
        $ persistent.deathcounter += 1
        $ renpy.save_persistent()
        call achievement_checker from _call_achievement_checker_4
        play music "<from 0.3>music/you_died.ogg"
        scene bg_endslate with blooddissolve
        show screen bg_endslate_text("You Died","You lost your head")
        $ renpy.pause(hard=True)
    elif True:
        $ arrivedby = "special"
        "Sleeping here would be crazy!"
        jump mason_turn_nostats

label event_mason_firedeath:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        $ sleep = 0
        call mason_display_subroutine from _call_mason_display_subroutine_13
        "The sound of a crack tore me out of my shallow sleep." with vpunch
    elif True:
        "The sound of the fire crackling seemed a bit hypnotic."
        "I stared into the flames as my muscles relaxed from a tension I didn't realize I had."
        "For a moment, I could imagine I was just camping."
        play sound "music/sfx_twig_snap_1.ogg"
        "That everything was okay."
        "It made it easy to nearly miss the crack that came from behind me."
    scene cg_mason_campfire
    $ persistent.cgs_mason.add("cg_mason_campfire")
    $ renpy.save_persistent()
    play sound "music/sfx_impact_forest.ogg"
    play ambient "music/ambient_medium_fire.ogg" fadein 1.0
    "I couldn't turn around in time to see the large hands that knocked me to the ground." with vpunch
    "The force and weight behind his tackle left me unable to take in a breath."
    "As I tried in vain to take in a single gulp of air, I stared into the embers of the fire only inches from my face."
    play music "music/masons_theme.ogg" fadein 1.0
    m surprised "What were you thinking?"
    "He pressed on the back of my neck, though it meant little since I couldn't even move my chest."
    m smirk "You should have known better!"
    m normal "Could see the smoke from the other side of the valley I bet."
    "I replied with a rasping inhale, just barely managing to finally take in some air."
    "I could feel his hand wrap around the back of my head."
    "He pushed my face, grinding on the dirt, closer to the embers."
    "The intense heat became blistering and I panicked."
    if meme_mode:
        "At least something smelled super delicious."
        "Like barbeque or something..."
    "I squirmed with all the adrenaline I could muster."
    "I tried to move my arms, legs... a kick, an elbow... anything."
    "He was too heavy."
    "I writhed under him, not even able to fully scream."
    "He seemed to enjoy the sound of my hoarse, panicked cry."
    $ stat_health -= 5
    "I could feel my skin burning."
    if sexcontent != "no":
        "I tried to jerk away under him."
        m smirk "Squirm..."
        "I froze."
        "Something about the tone of his voice changed."
        m predatory "I told ya to squirm."
        $ stat_health -= 5
        play sound "music/sfx_knife_stab.ogg"
        "I screamed as the blade of a knife plunged into my shoulder from behind." with vpunch
        "My cry wavered as I instinctively moved my arm, only amplifying the pain."
        "I didn't notice his weight lift from me."
        "Or the sound of rustling clothing."
        "It wasn't until I heard the blade sawing through the back of my pants that I realized his intention had shifted."
        "In a split second, the shock of cold air hit my skin."
        "I tried to lunge forward, but his large hand grabbed the back of my head."
        "He slammed my face back into the ground." with vpunch
        "Once again I was reminded of the coals right next to my face."
        "I let out a choked whine as I tried to get away from the fire."
        m "Nng... That's better."
        "Something thick and hot pressed between my legs."
        "No!"
        "For a moment, my brain couldn't make sense of the two threats, or decide which direction to try and flee."
        "But that changed when he shoved himself roughly into me."
        "The position was wrong and my skin felt like it was tearing."
        "I screamed and pushed forward, right into the coals."
        "Tears exploded from my eyes, my body was trying in vain to combat the sparks and heat."
        "The arm holding my head dragged me backwards, slightly dulling the heat."
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        "Before I could appreciate it, he slammed into me again, deeper than before." with vpunch
        "It was thick and dry and it felt like it was burning there too."
        "My raw throat was struggling to keep screaming."
        "He began to move consistently as I dissolved into broken wailing."
        "His weight and movements were breaking me down."
        "His thrusting was painfully hard but deliberately slow."
        "My body and mind were giving out."
        m smile "Hah... not squealing anymore..?"
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        "He jerked forward in a thrust that shoved my whole body." with vpunch
        "Right back into the glowing coals."
        "I began hoarsely screaming and writhing again as the flesh on my face began to sizzle."
        m predatory "AAhhnngg!"
        "That really seemed to set him off."
        "I kept trying to get away from the fire, but it was impossible with his weight slamming into me."
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        "Pain was devouring my face as he ground my head into the base of the fire."
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        "Somehow, it wasn't enough to distract me from his last thrust stuck deep in me." with vpunch
        "The pulsing and twiching inside my bruised and bleeding body."
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "Suddenly, to my relief, my head was pulled up and away from the coals."
    "His fist in my hair and the painful position were nothing compared to the cool air replacing the fire."
    "My comfort drained as he whispered next to my ear."
    m serious "Fun's over."
    $ stat_health -= 100
    "I stared into the trees as I felt the blade drag slowly across my throat."
    scene black with eyedissolve
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    "I wretched and felt the air and blood pour from my neck instead."
    "I fell to the ground." with vpunch
    $ quick_menu = False
    window hide
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_mason.add("Your smoke gave you away")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_5
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","Your smoke gave you away.")
    $ renpy.pause(hard=True)

label event_mason_pepper_1:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        "I woke up and rubbed my eyes."
        "Then I looked up at the sky."
    elif True:
        "I stopped for a moment and looked up."
    "It was striking."
    "I had never seen the stars so clearly."
    "It was beautiful and unsettling."
    "I had the strangest sense of butterflies in my stomach as for a split second... I felt like I could fall up, away from the earth."
    "As soon as it came, it passed."
    "I stared up at the stars."
    $ arrivedby = "special"
    jump mason_turn_nostats

label event_mason_pepper_2:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        "I groaned as I slowly woke."
    $ persistent.cgs_mason.add("cg_mason_clouds")
    $ renpy.save_persistent()
    scene cg_mason_clouds with dissolve
    "Clouds again..."
    "I found myself staring up at the cold grey sky."
    "I could scream but no one would hear me."
    "No one who would understand or care."
    "It felt as though sounds here were just swallowed up into the soft colourless void."
    "I've never heard such a silence..."
    "I've never felt so alone."
    call mason_display_subroutine from _call_mason_display_subroutine_20
    $ arrivedby = "special"
    jump mason_turn_nostats

label event_mason_cold_1:
    $ phase = "event"
    "I shivered violently."
    "It felt like the cold was going right through my entire body."
    $ arrivedby = "special"
    jump mason_turn_nostats

label event_mason_cold_2:
    $ phase = "event"
    "A cold wind rushed through the trees."
    "I tried to shield myself from the bite."
    $ stat_sanity -= 10
    "The pain in my limbs and face felt like tiny knives."
    $ arrivedby = "special"
    jump mason_turn_nostats

label event_mason_cold_3:
    $ phase = "event"
    "I watched the tiny clouds formed by my breath in the icy air."
    "Somehow, it didn't seem so cold."
    "I wasn't shivering anymore."
    "I felt tired... where was I again?"
    "I looked at the ground around me."
    $ stat_sanity -= 20
    "Maybe if I just rest a little..."
    $ arrivedby = "special"
    jump mason_turn_nostats

label event_mason_colddeath:
    $ phase = "event"
    if arrivedby != "sleep":
        "I couldn't move my legs anymore."
        "I finally felt warm."
        "Maybe too warm even... but I'm too tired to take my clothes off."
        "I laid down on the ground."
        "I'll just rest and everything will be fine."
        scene black with eyedissolve
        stop music fadeout 1.0
        stop ambient fadeout 1.0
        "I closed my eyes."
        "Just for a few minutes."
    elif True:
        "As I slept, the cold crept into my body."
        "I never felt the ice crystals form in my blood."
        "I never felt the frost creep over my skin and into my eyes."
        "And I never woke up."
    $ quick_menu = False
    window hide
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_mason.add("The cold took you")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_6
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","The cold took you")
    $ renpy.pause(hard=True)

label event_mason_mapswamp:
    $ phase = "event"
    "I stopped in the trees."
    p "Hm."
    "I pulled out my map and looked at it."
    "Its hard to tell where I am in here, but it really looks like there's a direction I haven't gone."
    "I looked towards the north."
    "The brush got a lot thicker."
    "It might be hard to get through..."
    "But that means it's harder for him too."
    "It might be worth it."
    menu:
        " "
        "Fight through the bush and go north" if True:
            "I have to try it."
            "I put away my map and walked forward, fighting through the growth."
            $ map_location = "Swamp"
            $ arrivedby = "new"
            if fire != 0:
                $ fire = 0
                $ location_temp = "cold"
                stop music fadeout 0.5
                hide campfire with dissolve
                "I quickly put out my fire."
            jump mason_turn_order
        "Leave it alone" if True:
            "I decided not to go north."
            "It's too much effort and I need to conserve my energy."
            $ arrivedby = "special"
            jump mason_turn_nostats

label event_mason_nightmare:
    $ phase = "event"
    hide screen effect_health
    hide screen effect_ice
    scene black with dissolve
    stop ambient fadeout 1.0
    play music "music/music_nightmare.ogg" fadein 1.0
    "He was chasing me."
    show cg_mason_nightmare_swamp
    show cg_mason_nightmare_treesleft
    show cg_mason_nightmare_treesright
    with Dissolve(3.0)
    "I ran through the trees."
    "The hollow thud of my feet on rotting ground echoed my heartbeat."
    "Wind and branches clawed at my body,"
    "Desperately clinging tighter and tighter as I ran with more desperation."
    "My footfalls increasing pace with the terror bubbling up,"
    "Threatening to choke me-"
    show cg_mason_nightmare_swamp:
        easein 1.0 zoom 1.2
    show cg_mason_nightmare_treesleft:
        easein 1.0 zoom 1.5 alpha 0.0 xalign 1.5
    show cg_mason_nightmare_treesright:
        easein 1.0 zoom 1.5 alpha 0.0 xalign -0.5
    "Then, suddenly, I spilled out into the open."
    "I gasped and sucked in a breath."
    "I filled myself with the damp and gentle decay."
    "It was warm... and welcome."
    "A gravity pulls my attention to the water."
    "Black water..."
    "The inky surface was as still as the night around me."
    scene black with dissolve
    "Something pulled me."
    play sound "music/sfx_water_swish.ogg"
    scene cg_mason_nightmare_water at top with dissolve
    "I stepped forward into the water."
    "I wandered forward, deeper, beckoned."
    "As I slid deeper, my legs brushed against roots... claws..."
    "Bones..."
    play sound "<from 1.0>music/sfx_water_submerge.ogg"
    scene cg_mason_nightmare_water:
        easein_expo 1.0 yalign 1.0
    pause(1.0)
    scene black with dissolve
    lich "So you've started to wander..."
    "I couldn't move."
    "A deep sense of dread filled me to the core."
    lich "Hunter's prey..."
    lich "This place and time will define you."
    lich "I'll be waiting."
    stop music fadeout 1.0
    if map_location == "Waterfall":
        play ambient "music/ambient_creek.ogg" fadein 1.0
    elif True:
        play ambient "music/ambient_forest.ogg" fadein 1.0
    show screen effect_health
    show screen effect_ice
    jump mason_turn_nostats

label event_mason_offerbones:
    $ phase = "event"
    $ event_mason_offerbones = 1
    "I approached the edge of the inky swamp."
    "Maybe I've gone crazy."
    "I looked down at the bones I was holding."
    "But if the nightmare was real..."
    "At the very least, this will make me feel better."
    play sound "music/sfx_water_splash.ogg"
    "I dropped the bones into the water."
    play music "music/music_nightmare.ogg" fadein 3.0
    show cg_mason_lich1 at flicker
    pause(1.0)
    lich empty "You've returned..."
    lich empty "And you brought me a gift."
    "The voice was quiet and calm, but I couldn't quite tell where it was coming from."
    "I couldn't look away from the unreal creature in front of me."
    "Just like my nightmare... I couldn't move."
    lich empty "You're different... aren't you?"
    "Did it want me to respond?"
    "I slowly nodded."
    "It seemed pleased."
    lich empty "Maybe it's time for the beast to meet his end."
    hide cg_mason_lich1
    pause(1.0)
    show cg_mason_lich2 at flicker
    lich empty "Prey... [player_name]..."
    lich empty "I've seen his dreams."
    lich empty "There's a loaded gun behind the bear's skin."
    hide cg_mason_lich2 with dissolve
    stop music fadeout 5.0
    "My eyes widened."
    "Is this thing serious?"
    "If I can just get it..."
    "Huh?"
    p "H... hello?"
    "Just the breeze through the trees."
    "I shook my head."
    "Was that even r-"
    lich normal "I'll be watching."
    "I whipped around and looked for the source of the voice."
    "Nothing but the swamp."
    "I shivered."
    $ arrivedby = "special"
    jump mason_turn_nostats

label event_mason_baneberry_freakout:
    $ phase = "event"
    "The berries were horribly bitter."
    "I couldn't manage any more than a handful."
    "A few minutes after eating them, I began to feel uneasy."
    p "Ugh..."
    play music "music/ambient_dire_situation.ogg" fadein 1.0
    play sound "music/sfx_ears_ring.ogg"
    "I felt a strange pressure on my head."
    "I shook my head, trying to get it to stop."
    "Bright blue shapes exploded into my vision."
    play sound "music/sfx_impact_forest.ogg"
    "I fell backwards." with vpunch
    p "Fuck... ngh..."
    "I couldn't get up. The entire universe seemed to be swirling around me, like I was in a snowglobe."
    "I tried to gently lie down as the pain started."
    $ stat_sanity -= 10
    "My stomach... all my guts were on fire."
    "I was barely aware of myself anymore as I writhed and moaned on the ground."
    "My heart was fluttering."
    if map_location == "Swamp":
        jump event_mason_baneberry_drown
    $ stat_sanity -= 20
    "Am I going to die here?"
    "Like this..?"
    "The pain and dancing shapes were a torture I could never have even imagined."
    "I curled up on the cold ground."
    "The blurry spinning forest was going to swallow me."
    "I tried to swallow myself, but my throat was too dry."
    $ stat_sanity -= 10
    "I... give up..."
    scene black with dissolve
    stop music fadeout 5.0
    "I laid there for a long time."
    "About an hour later, I noticed I was able to swallow normally."
    call mason_display_subroutine from _call_mason_display_subroutine_19
    "I groaned and tried to sit up."
    "It was going away..."
    "Nothing was spinning anymore."
    "I let out a sigh of relief."
    "I got back to my feet with some effort."
    "Somehow, I felt exhausted from the ordeal."
    "I shook my head one last time." with hpunch
    "And then threw the remaining red berries as hard as I could."
    $ arrivedby = "special"
    jump mason_turn_order

label event_mason_baneberry_drown:
    $ phase = "event"
    "The..."
    $ stat_sanity -= 20
    "The water..."
    "I sunk my fingers into the cold, damp earth."
    "I pulled my body forward over the rocks and rotting leaves."
    $ stat_sanity -= 20
    "Trees, roots, leaves, dirt, spines, spinning..."
    "The air moved and breathed with me."
    "Heaving, pulsing."
    "The water."
    "The water is still..."
    "I touched the surface of the dark mirror."
    $ stat_sanity -= 20
    "The water is still.{w=0.3} The water is still.{w=0.2} The water is still.{w=0.1} The water is still.{w=0.1} The water is still.{w=0.1} The water is still.{w=0.1} The water is still.{w=0.05} The water is still.{w=0.05} The water is still.{w=0.05} The water is still.{nw}"
    "I clawed at the ground and dragged my body to it." with hpunch
    "Shaking..."
    "Grasping, I plunged my hands into the bog."
    play sound "music/sfx_water_swish.ogg"
    if meme_mode:
        "I slipped into the bone soup."
    elif True:
        "I pulled myself forward."
    $ stat_sanity -= 20
    scene black with dissolve
    hide screen effect_health
    hide screen effect_ice
    play ambient "music/ambient_underwater.ogg" fadein 1.0
    stop music fadeout 10.0
    "I slipped under the surface silently."
    "The water closed around me."
    "The buzzing, pulsing pain faded from my body."
    $ stat_sanity -= 20
    "Gravity and light disappeared."
    "Water, cool and soothing, flowed into me."
    "I felt...{w} Held."
    show cg_mason_baneberry_drown_1:
        alpha 0.0
        xanchor 0.5
        yanchor 0.5
        yalign 0.5
        xalign 0.5
        easein 0.5 alpha 0.5
    pause 0.5
    show cg_mason_baneberry_drown_1:
        alpha 0.5
        xanchor 0.5
        yanchor 0.5
        yalign 0.5
        xalign 0.5
        easeout 0.5 alpha 0.0
    lich empty "You're here early..."
    $ persistent.cgs_mason.add("cg_mason_baneberry_drown")
    $ renpy.save_persistent()
    show cg_mason_baneberry_drown_1:
        alpha 0.0
        xanchor 0.5
        yanchor 0.5
        yalign 0.5
        xalign 0.5
        easein 10.0 alpha 1.0
    "That cold voice..."
    lich empty "Have you been lonely?"
    "I made no answer."
    "I couldn't."
    lich empty "I understand."
    lich empty "I've been lonely too..."
    lich empty "And so empty..."
    lich empty "Don't worry."
    lich empty "You can stay here."
    lich empty "You will stay in the water..."
    window hide
    pause 0.5
    show cg_mason_baneberry_drown_3:
        alpha 0.0
        xanchor 0.5
        yanchor 0.5
        yalign 0.5
        xalign 0.5
        easein 1.0 alpha 1.0
    pause 2.0
    show cg_mason_baneberry_drown_2:
        alpha 0.0
        xanchor 0.5
        yanchor 0.5
        yalign 0.5
        xalign 0.5
        zoom 1.0
        easein_expo 0.5 alpha 1.0 zoom 2.0 xoffset -400 yoffset 100
    play sound "music/sfx_scrape_slow.ogg"
    scene black with Dissolve(0.25)
    pause(3.0)
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_mason.add("The water is still")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_7
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","The water is still")
    $ renpy.pause(hard=True)

label event_mason_fish_cook:
    $ phase = "event"
    "I took out the fish I caught earlier."
    if meme_mode:
        "It looked at me, seemingly crying."
        p "Sorry fish. This is the way things have to go."
        "I shoved my knife into it quickly, trying to be merciful."
        "It still let out a tiny scream."
    "I tried my best to clean it with my knife before putting a stick through it."
    "I held it over the fire and relaxed a bit."
    "This might be fun in another circumstance..."
    "As it cooked I began to smell it."
    "My stomach growled."
    if "item_fish" in inventory:
        $ inventory.remove("item_fish")
        $ inventory.append("item_cookedfish")
    if "item_fish_cute" in inventory:
        $ inventory.remove("item_fish_cute")
        $ inventory.append("item_cookedfish_cute")
    $ renpy.notify("Cooked Fish Added!")
    show screen inventory
    pause(1.5)
    hide screen inventory
    "Once it was nearly blackened on the outside and flaky on the inside, I took it away from the flame."
    "Finally... some real food!"
    $ arrivedby = "special"
    jump mason_turn_order

label event_mason_beartrap_drop:
    $ phase = "event"
    "Ughhhh."
    "I can't carry this fucking thing anymore."
    $ inventory.remove("item_beartrap")
    $ renpy.notify("You are no longer encumbered.")
    $ encumbered = 0
    play sound "<from 0.0 to 1.0>music/sfx_bear_trap_drop.ogg"
    "I hoisted the metal trap off my back and dropped it to the ground with a thud."
    p "Ahhh..."
    "That feels so much better..."
    $ arrivedby = "special"
    jump mason_turn_nostats

label event_mason_beartrap_failset:
    $ phase = "event"
    "If I can set this..."
    "I swung the trap off my back and on to the ground with a dull thud."
    "Phew...That thing is {i}really{/i} heavy."
    "I looked over the device."
    "To get it open again... I guess I just need to press these side spring things down?"
    "I stepped on one side of the trap."
    "To my surprise, I barely pushed it down at all."
    "I put all my weight on it."
    "It moved down a bit, but sprung back up."
    "There's no way I can press both sides down and pull it open..."
    "I struggled with it for another few minutes before giving up."
    "There must be something about this thing that I'm missing."
    "I let out a defeated sigh and swung the trap back over my shoulder."
    "...Damn."
    $ arrivedby = "special"
    jump mason_turn_order

label event_mason_beartrap_set:
    $ phase = "event"
    "I spotted a clamp on a table among some other metal tools."
    "Wait..."
    "I could use that!"
    "I snatched the heavy tool."
    "It's a bit rusty but it's the perfect size."
    "I swung the trap down off my back and laid it on the floor."
    "I licked my lips in concentration and positioned the screw clamp around one of the springs."
    play sound "music/sfx_bear_trap_set.ogg"
    "It took some effort to twist the screw, but I managed to actually push the spring down."
    "Halfway there!"
    "I looked on the table for something to keep the spring closed and spotted a C shaped metal holder."
    "It was the same rusty metal as the clamp..."
    "This must be what these tools are for."
    "I placed the holder on the spring and got to work on the other side."
    "I sweated with effort and nervously listened for footsteps."
    "I'm so close now..."
    "There!"
    p "Phew!"
    "I wiped my forehead and looked down at my handiwork."
    "The savage looking trap was set once again."
    "Who even sells this shit?"
    "It must be illegal."
    "I shook my head and got back to the task at hand."
    "I needed a plan."
    "I scanned the floor of the cabin for a good spot."
    "Oh?"
    "I grinned at large fur on the floor."
    "Easy."
    "I dragged the heavy trap over carefully and covered it gingerly with the skin."
    "It's not as obvious anymore..."
    "But I still need him distracted."
    "I gulped."
    "The best bait... would be me."
    "I wanted to just leave the trap, but this would be the only way I could make sure he wouldn't see it."
    "I steadied my nerves and took my position in the corner of the room."
    "If he's looking at me, he won't see it."
    "And if this doesn't work... I'd be dead eventually anyway."
    "It really is the only way."
    "I clenched my teeth and waited."
    "I was weary and terrified, but I stayed alert."
    "It felt like hours."
    "Until finally, I heard a rustling next to the door."
    "Adrenaline flooded my body."
    "This is it!"
    play music "music/masons_theme.ogg" fadein 1.0
    show mason question with dissolve
    "The door creaked open, and there he was."
    "He looked surprised for a moment, before gaining his composure."
    m smug "Ya came right to me, eh?"
    "I need to do something."
    show mason question
    "I pulled out my little knife and got into a fighting stance."
    m excited "HA hah!"
    m "I like this!"
    show mason knife
    "He pulled out his own knife."
    "It wasn't much larger than mine."
    m "Yer shakin' like a leaf."
    "I gritted my teeth and held my stance."
    "Come on... Just a little closer..."
    "I made a partial lunge forward."
    "That was enough. He came at me quickly-"
    play sound "music/sfx_bear_trap_snap.ogg"
    show mason trapped at bounce, center
    m "AAUUGHHH!!!"
    $ persistent.cgs_mason.add("cg_mason_trapped")
    $ renpy.save_persistent()
    scene cg_mason_trapped with dissolve
    m empty "Rrraughh... you..."
    "I was frozen for a moment."
    "It worked!"
    "Although... now he was between me and the door."
    "A glint caught my eye."
    "He dropped his knife!"
    "A shaky smirk crossed my lips."
    "At the same time, a spark of fear showed in his eyes."
    "He was practically growling."
    "...Like a cornered animal."
    "I climbed over the chair, just out of his reach, and got behind him."
    "He awkwardly tried to turn to face me, but he froze when he felt my blade on his throat."
    $ persistent.cgs_mason.add("cg_mason_kill")
    $ renpy.save_persistent()
    scene cg_mason_kill1 with dissolve
    if achievement.has("ach_catching_bears") != True:
        $ persistent.ach_catching_bears = True
        $ achievement.grant("ach_catching_bears")
        init:
            $ achievement.register("ach_catching_bears")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_catching_bears == True and achievement.has("ach_catching_bears") != True:
                $ achievement.grant("ach_catching_bears")
                $ achievement.register("ach_catching_bears")
                $ achievement.sync()
    call cutthroat_checker from _call_cutthroat_checker
    "I gripped his hair and pulled his head back."
    "Something inside me was roaring."
    "Maybe it was the adrenaline."
    "Maybe I'd just been through too much."
    if meme_mode:
        p "Look at me."
        p "I am the hunter now."
    elif True:
        "I looked into his eyes."
        p "Fun's over."
    stop music fadeout 1.0
    scene cg_mason_kill2 with dissolve
    "With one overly harsh movement, I brought the blade through his neck."
    "The gash was enormous and immediately poured blood out and on to the cabin floor."
    scene cg_mason_kill3 with dissolve
    "The grisly sight didn't bother me at all."
    "Rather, I felt a rush."
    "I felt high."
    "Is this why he does all of this?"
    "I wiped my blade on his motionless coat."
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    scene black with dissolve
    "After I made my kill, it was relatively easy to search the place at my leisure."
    "I patched myself up and kept looking."
    "I eventually found keys, a compass, and some crude notes about a stashed jeep."
    "He kept it covered, far from the cabin."
    "As I drove back to civilization, I felt like I was watching someone else."
    "It was surreal."
    "I was really going to go home."
    "But..."
    "I suppose I'll never be the same again."
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_mason.add("Now you are the hunter")
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_8
    play music "<from 0.4>music/music_killer.ogg" fadein 1.0
    scene bg_endslate_survival with zoomdissolve
    show screen bg_endslate_survival_text("You Lived","Now you are the hunter")
    $ renpy.pause(hard=True)

label event_mason_beartrap_death:
    $ phase = "event"
    stop ambient fadeout 1.0
    play sound "music/sfx_bear_trap_snap.ogg"
    if health > 10:
        $ stat_health -= 10
    if fire != 0:
        $ fire = 0
        $ location_temp = "cold"
        stop music
        hide campfire
    scene black
    pause(0.2)
    $ persistent.cgs_mason.add("cg_mason_beartrapped")
    $ renpy.save_persistent()
    if 8 <= hours <= 18:
        scene cg_mason_beartrapped_day:
            zoom 1.7
            xalign 0.9
            yalign 0.5
    elif (hours == 7) or (hours == 19):
        scene cg_mason_beartrapped_twilight:
            zoom 1.7
            xalign 0.9
            yalign 0.5
    elif True:
        scene cg_mason_beartrapped_night:
            zoom 1.7
            xalign 0.9
            yalign 0.5
    p "EEAAGHHH!" with vpunch
    if 8 <= hours <= 18:
        show cg_mason_beartrapped_day:
            easein_expo 0.3 xalign 0.5 yalign 0.5 zoom 1.0
    elif (hours == 7) or (hours == 19):
        show cg_mason_beartrapped_twilight:
            easein_expo 0.3 xalign 0.5 yalign 0.5 zoom 1.0
    elif True:
        show cg_mason_beartrapped_night:
            easein_expo 0.3 xalign 0.5 yalign 0.5 zoom 1.0
    play sound "music/sfx_scrape_fast.ogg"
    play music "music/ambient_dire_situation.ogg" fadein 1.0
    "Pain exploded up my leg."
    "I looked down and saw metal jaws clamped into the flesh of my ankle."
    "I made a smothered sound as I tried to hold in another scream."
    "The silence around me told me that I had already made far too much noise."
    "I whimpered as I bent down to inspect the trap."
    "It's a goddamn bear trap..."
    "A really big and sharp one..."
    "I gripped the two jaws and tried to pull them apart."
    "They didn't budge at all."
    "I breathed hard and put all of my strength into it."
    "They moved only the slightest bit."
    "Just enough to send a new rush of pain up my leg as my strength gave out."
    "No no... fuck fuck fuck."
    "I let myself slump to the ground and suppressed the urge to start crying."
    "I examined my leg again."
    "The teeth were deep in my flesh, but not quite to the bone."
    "The pressure was cutting off my circulation."
    "There's no way I can... cut my leg off."
    "Not with this tiny knife."
    "I let out a whimper of despair."
    "... I have to pry it off."
    "That's the only way out of this."
    "I grabbed the jaws again and wrenched on them with every desperate muscle in my body."
    p "Please... PLEASE!"
    "Nothing..."
    "I... I can't..."
    stop music fadeout 1.0
    scene black with eyedissolve
    play sound "music/sfx_impact_forest.ogg"
    "I let myself fall to the ground." with vpunch
    "I laid there in a daze of terror and pain."
    pause(1.0)
    "I don't know how long I stayed that way."
    "The frozen ground began to numb my body."
    $ hours = 12
    call mason_display_subroutine from _call_mason_display_subroutine_14
    play sound "music/sfx_twig_snap_1.ogg"
    "Until the snap of a twig behind me distracted me."
    "I twisted my body to see the source of the sound."
    play music "music/masons_theme.ogg" fadein 1.0
    scene cg_mason_beartrapped_looming with dissolve
    $ persistent.cgs_mason.add("cg_mason_beartrapped_looming")
    $ renpy.save_persistent()
    p "...No..."
    m empty "Ahh."
    m empty "Got yerself bit did ya?"
    "I wanted to scramble away, put any distance between him and myself."
    "But the pain in my leg was too intense to move."
    "He walked to me and looked at my ankle."
    "Before I could process his intention, he lifted his leg and stepped on my caught knee."
    "I howled in pain."
    m empty "Got ya real good..."
    "I clenched my teeth and gripped handfuls of dirt to try and distract myself from the pain."
    "He stepped off me and clucked his tongue."
    scene cg_mason_beartrapped_loomingknife with dissolve
    m empty "Leg's no good to you now... I s'pose we should just get it off, eh?"
    "My head was already fuzzy with pain and fear."
    "What the hell did he mean, 'get it off'?"
    "A white handle caught my eye."
    "He was gripping a strange looking knife."
    "My breath caught in my throat."
    p "No!"
    p "No no no, please don't!"
    "I cringed as he bent low to cut the straps of my bag."
    m empty "Won't be needing this n'more."
    "He tossed the bag and its contents away from me."
    p "Stop! Please!"
    scene cg_mason_beartrapped_crouch with dissolve
    $ persistent.cgs_mason.add("cg_mason_beartrapped_crouch")
    $ renpy.save_persistent()
    "He crouched by my leg, completely ignoring my pleas."
    $ stat_health -= 5
    "He pushed the knife into my leg, above the jaws of the trap."
    "I yelled again and squirmed, trying in vain to get away from the pain."
    m empty "Hrm."
    "He shifted his position and knelt down with his knee on my abdomen."
    "His weight crushed the air out of me."
    "I couldn't move at all."
    if meme_mode:
        menu:
            "Grab his ass" if True:
                "I reached out and grabbed a meaty handful of ass."
                "He didn't even seem to notice, he was so focused on my leg."
                "Well, if I'm going to die I might as well go out copping a feel."
            "Do nothing" if True:
                pass
    $ stat_health -= 5
    "Once again, I felt the knife in my leg and gurgled an airless scream."
    "I frantically and uselessly gripped the back of his coat."
    $ stat_health -= 10
    "Soon I felt a sickening pull as he grasped the tendons in my leg and sawed through them."
    "I was shaking in pain and shock."
    play sound "music/sfx_blood_drip.ogg"
    scene cg_mason_beartrapped_gore with dissolve
    $ persistent.cgs_mason.add("cg_mason_beartrapped_gore")
    $ renpy.save_persistent()
    "I looked at my leg and wish I hadn't."
    "All the flesh was peeled away from..."
    m empty "Knife aint gonna cut through that."
    scene black with dissolve
    scene cg_mason_beartrapped_gore2 with dissolve
    "I could hear static."
    "Oh god, please just pass out..."
    "Unfortunately, the pain kept me alert."
    "He had gotten up..."
    "I could see my exposed bone, and it became clear what he was planning to do."
    "I didn't have the energy to beg this time."
    "I just sobbed as he positioned himself."
    scene black
    $ stat_health -= 20
    hide screen effect_health
    hide screen effect_ice
    play sound "<from 0.0 to 1.0>music/sfx_impact_bone.ogg"
    "I closed my eyes as he brought down his boot with all his weight behind it." with vpunch
    "I screamed in agony as my bone was shattered."
    stop music fadeout 1.0
    "Finally, I felt my consciousness slipping."
    "I welcomed the loss of sensation."
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_mason.add("You were caught in his trap")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_9
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You were caught in his trap")
    $ renpy.pause(hard=True)

label event_mason_snare_death:
    $ phase = "event"
    scene black
    play sound "music/sfx_cord.ogg"
    p "AAH!" with vpunch
    $ persistent.cgs_mason.add("cg_mason_snare")
    $ renpy.save_persistent()
    if 8 <= hours <= 18:
        scene cg_mason_snare_day at swing, center with dissolve
    elif (hours == 7) or (hours == 19):
        scene cg_mason_snare_twilight at swing, center with dissolve
    elif True:
        scene cg_mason_snare_night at swing, center with dissolve
    "Something..."
    "I was hanging upside down!"
    "I took a moment to calm myself down."
    "I can't afford to keep making noise..."
    "After a few deep breaths, I looked up at the trap."
    "My ankle was in a tight snare..."
    "The wire shone with a sinister glint."
    "I suspected that it would be cutting into my flesh if it weren't for the boots I was wearing."
    "I was beginning to lose feeling in my foot."
    menu:
        " "
        "Cut the wire" if True:
            "I remembered the small knife I was given."
            "If I can just get up to it..."
            $ stat_energy -= 1
            "I grasped my clothing and grunted, trying to get my hands to my feet."
            "I was shaking and straining."
            "Once I managed to get close, I held on tightly with one hand while fumbling for my knife."
            "Once I had it, I frantically tried to cut at the wire holding my leg."
            "I kept sweating and sawing."
            "Something in me refused to check my progress."
            $ stat_energy -= 1
            "My energy ran out before my denial could."
            "I fell back away from my foot with a pained yelp." with vpunch
            "The force made the snare even tighter and pulled the knife out of my grip."
            "I looked at my knife on the ground."
            "The edge was completely ruined."
            $ stat_sanity -= 10
            "I didn't damage the snare at all."
        "Untie the trap base" if True:
            "I think I saw this in a movie once."
            "You just need to swing back and forth..."
            "I wiggled my body and tried to throw my weight."
            "Eventually, I managed to get a rhythm going."
            "I swung towards the tree nearest to me."
            "Once it was in range, I grabbed the trunk and held on tightly."
            "Where is the rest of the snare!?"
            "I felt around the trunk in vain before looking up."
            "The wire seemed to just dissppear into the branches."
            "I couldn't spot the counterweight."
            "My hands began to slip from the trunk as I grunted with effort."
            "My shaking arms couldn't keep hold."
            if 8 <= hours <= 18:
                scene cg_mason_snare_day at swing, center
            elif (hours == 7) or (hours == 19):
                scene cg_mason_snare_twilight at swing, center
            elif True:
                scene cg_mason_snare_night at swing, center
            "I fell away from the trunk and dangled again." with vpunch
            $ stat_sanity -= 10
            "Now the snare was tighter and I had nothing to show for it..."
    "I groaned in defeat."
    "I was exhausted."
    "Blood was rushing to my head and it was getting harder to think."
    scene black with eyedissolve
    "I don't know what to do..."
    "I dangled there, floating in and out of consciousness, unaware of how much time was passing."
    $ hours = 9
    pause(1.0)
    "I realized that the thumping of blood in my ears was accompanied by other thumps- growing louder."
    "I wriggled in place, trying to turn around."
    "I could hear the crunch of the forest floor under his feet."
    play music "music/masons_theme.ogg" fadein 1.0
    $ persistent.cgs_mason.add("cg_mason_upsidedown")
    $ renpy.save_persistent()
    scene cg_mason_upsidedown with eyedissolve_reverse
    "Then thick hands grasped my waist and turned me around."
    "I couldn't stop a whimper from escaping my throat."
    m empty "I didn't really think this one was going to work!"
    "I followed his gaze to the wire."
    "He must be talking about the snare."
    "He casually pulled out a small knife with a white handle."
    p "No no no!"
    "I wriggled in vain, completely unable to get any distance from him."
    m "Have you been waiting long for me?"
    menu:
        " "
        "Answer him" if True:
            "Maybe if I cooperate..."
            p "I've been here for... maybe an hour or two..?"
            "He looked a bit surprised and chuckled deeply."
            "I guess he wasn't expecting an answer."
        "Stay quiet" if True:
            "I kept my jaw clenched shut."
            "It wasn't much comfort, but the idea of at least dying with my dignity was something."
        "Try to stall him" if True:
            "I panicked, trying to find something to slow him down."
            "My eyes kept going back to the knife."
            p "Ah... T-that's an interesting knife!"
            "He paused."
            "Then a warm smile spread over his face."
            scene cg_mason_upsidedown2 with dissolve
            m empty "Can't blame you for admirin'!"
            "He flipped the knife in his hands."
            m empty "Sandy might've been my wife, had I been more societally inclined."
            "I squinted in confusion."
            "He was looking at the knife wistfully."
            "I was willing to take the opportunity to draw this out."
            p "Er... 'Sandy'?"
            m empty "Mhm."
            "The knife glinted in his hands."
            m empty "I was a young spry thing, and she was the prettiest girl in the village."
            m empty "I wasn't much of a proper kid, but I managed to ask her on a date."
            "I couldn't believe he was actually talking."
            "I tried to think of ways to escape while I nodded and urged him to continue."
            m empty "Wouldn't ya be surprised, but she agreed!"
            "He laughed gruffly."
            m empty "So I took her up camping."
            m empty "Real camping... none of that fancy tent nonsense mind you."
            m empty "Anyhow, she got settled happy and I went out and got a nice fat rabbit for dinner."
            m empty "I got to work cleanin' it and she come running over!"
            m empty "She looked up at me with those big old doe eyes."
            m empty "Scareder than the rabbit been!"
            "His voice became softer, as if this was somehow the most romantic part of the story."
            m empty "And I knew then, just what I had to do."
            "He rubbed the knife slowly and I gulped."
            "At some point I had stopped thinking of escape plans and gotten caught up in his story."
            "That smooth white knife hilt..."
            "It was definitely bone."
            $ stat_sanity -= 30
            m empty "My first real hunt..."
            "I squirmed in discomfort."
            "I sincerely regretted asking about that knife."
            scene cg_mason_upsidedown with dissolve
            m empty "Tsk, that's enough talkin'."
        "Try to 'distract' him" if sexcontent != "no":
            p "Hey! Wait!"
            p "L-look... don't kill me..."
            m empty "Hm?"
            "He seemed mildly amused."
            "Like he'd humor me, but only for a second."
            "I gulped and bent my neck and back, pushing my face closer to his lower body."
            "I hoped that was enough to demonstrate what I was offering..."
            "I was straining from the effort, but his expression didn't change."
            "I felt my cheeks burning in humiliation and hoped that my face was already red from being hung upside-down."
            "He casually hooked a thumb into his waistband."
            "I looked back up and saw the flash of his teeth."
            "He definitely understood."
            "Suddenly he stepped forward, obscuring my view of his face and pressing his bulging pants against me."
            "I jolted in surprise."
            "How long has he been hard!?"
            m empty "Aight, heh. Let's see what you can do..."
            $ persistent.cgs_mason_sex.add("cg_mason_x_upsidedown")
            $ renpy.save_persistent()
            if sexcontent == "yes":
                scene cg_mason_x_upsidedown with dissolve
            "As he unzipped his pants and exposed himself, I worried that I'd made a terrible mistake."
            "It's just as thick and big as the rest of him..."
            "Of course."
            "Above, I felt him grip my free leg."
            "I'm in no position to back out now..."
            "I opened my mouth and leaned forward to get my lips around him."
            "I tried to ignore the musky scent and the pressure of too much blood in my head."
            "I focused on survival for a moment, until the flesh in my mouth twitched and he moaned gruffly above me."
            "My wandering thoughts were brought harshly back as a large hand gripped the back of my head."
            "My split second of protest was pushed back down my throat."
            "I tried to shake my head to indicate I wasn't ready."
            "His only reply was to grip my head tighter to keep it still as he pushed further."
            "My jaw strained around him and I began to panic as I felt the round head push against the back of my mouth."
            "I can't take anymore!"
            "I tried to kick, but it just caused the snare to dig in to my ankle."
            "He pushed harder, forcing my throat open painfully."
            "I was physically incapable of getting any sound out, so my only reaction was awkward, panicked twitching."
            "The pressure from inside my throat closed my airway."
            "I heard him groan in pleasure as I twitched."
            "He began slow and shallow thrusting, keeping himself lodged deep."
            "I could feel his entire cock sliding in my throat."
            "I could hardly even gag with the pressure."
            "His slow movements indicated he was savouring the sensation as my lungs began to burn."
            "I kept trying to suck in a breath of air in vain, and from the sounds he was making, he was enjoying that too."
            "I can't die like {i}this{/i}..."
            "I tried to shake my head free again, but I was weakening."
            "The hiss of rustling leaves around me began to sound hollow."
            "Just as my vision began to darken, he pulled himself out of my throat."
            "I immediately gagged and started coughing."
            "I wheezed and gulped in air."
            m empty "Mmmm..."
            "I dizzily tried to collect myself as spit ran down my face."
            "I couldn't focus anymore."
            "I could only flinch and make a scratchy whimper as he rubbed his entire length on my face, coating it in more spit."
            "The coppery taste on my tongue told me I must be bleeding too, but my entire head was in pain, so I couldn't tell where."
            "Then he shifted and pressed the blunt tip against my lips again."
            "I tried to object but my voice was completely broken."
            "This time he shoved himself in fully."
            "I jerked from the pain in my throat."
            m empty "Ahh, that's better..."
            "The air gave me the strength to try and push him away."
            m empty "AH!"
            "My struggle seemed to excite him."
            "As he moved again, his rhythm was jerky and random."
            "I clawed desperately at his legs."
            "I felt his fingernails dig into my scalp as he slammed my face into himself."
            "I couldn't breathe or move."
            "My entire face was buried in his flesh as the cock in my mouth pulsed."
            "I could feel his cum shoot into my throat, well past the point of swallowing."
            "Once he started pulling slowly out of me, gravity let the cum follow."
            "I instantly started violently coughing."
            "Spit and cum was forced out of my nose and throat."
            "I could feel tears as well, from the pressure and humiliation of it all."
            scene cg_mason_upsidedown with dissolve
            "As everything dripped from my face, I watched him adjust himself and pull up his pants."
            "I felt a tiny rush of hope."
            p "Ah.. are you going to... let me go..?"
            m empty "Hwah? HAHAHA!"
            "His laughter made my blood run cold."
            m empty "Now I never did agree to that."
            "I saw the flash of his knife."
            p "No!!!"
    "He easily pushed my coat down to my face, exposing my waist."
    "The cold air on my skin sent a violent shiver through my body."
    "No, no no!"
    "I writhed as he moved the blade to my skin."
    m empty "Try and hold still..."
    $ stat_health -= 10
    "I cried out as I felt the blade sink in to my belly."
    $ stat_health -= 10
    "My cry became a blood curdling scream as he dragged it down towards my ribs."
    play sound "music/sfx_blood_drip.ogg"
    scene cg_mason_snare_blood with dissolve
    "I convulsed, the pain and blood pounding in my head were making me dizzy."
    "Hot blood was running up my body and over my face."
    $ stat_health -= 10
    "I could feel his large hand slip into the hole in my torso."
    "The sensation muted me."
    $ stat_health -= 10
    "He was pulling things out of me..."
    $ stat_health -= 10
    "I could feel the weight of my organs shift to the outside of my body."
    "Between the blood pouring over my face and pooling in my head, I felt like I was drowning."
    "I didn't have the strength to writhe anymore."
    "He worked quietly."
    "All I could hear was the wet constant dripping of my blood on the leaves below."
    "The pain began to subside."
    "Soon, all I could feel was dizziness and cold."
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    scene black with eyedissolve
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    "Then, nothing at all."
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_mason.add("You were caught and cleaned")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_10
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You were caught and cleaned")
    $ renpy.pause(hard=True)

label event_mason_snare_deer:
    $ phase = "event"
    play sound "<from 0.0 to 1.5>music/sfx_shriek.ogg"
    "I stopped dead."
    "Was that a scream?"
    "I instinctively crouched low and tried to get out of sight."
    if meme_mode:
        play sound "music/sfx_wilhelm.ogg"
    elif True:
        play sound "<from 2.0 to 3.5>music/sfx_shriek.ogg"
    "I heard another sound..."
    "I relaxed a tiny amount."
    "I don't think it was human."
    menu:
        " "
        "Investigate the sound" if True:
            if fire != 0:
                $ fire = 0
                $ location_temp = "cold"
                stop music fadeout 0.5
                hide campfire with dissolve
                "I hastily put out my fire."
            "I crept towards the sound, keeping myself as hidden as possible."
            "A flash of movement in my vision had me take cover again."
            "I breathed slowly and tried to calm the adrenaline."
            "I tried not to think about curiosity and cats."
            "I peeked slowly from my cover at the source of movement."
            $ persistent.cgs_mason.add("cg_mason_deer")
            $ renpy.save_persistent()
            scene cg_mason_deer1 with dissolve
            play music "music/ambient_drone_intermittent.ogg" fadein 1.0
            "A deer..?"
            "At first I thought it was floating in mid air, until I saw the glint of wire."
            "The snare!"
            "The deer kicked weakly."
            "I touched my own neck."
            $ stat_sanity -= 10
            "It was a horrible sight, but the idea of food did cross my mind."
            "My conflicted thoughts were cut short by the rhythmic thumping of heavy boots."
            scene black with dissolve
            stop music fadeout 1.0
            "I froze behind my cover."
            "Shit!"
            scene cg_mason_deer2 with dissolve
            play music "music/masons_theme.ogg" fadein 1.0
            "I didn't dare move a single muscle as he came into view and approached the struggling deer."
            "All my concentration went into staying still as terror pumped through my veins."
            m empty "Ahh!"
            m empty "Now what're you doing in here?"
            "He was... talking to the deer."
            "I cringed as he held the deer's face roughly."
            m empty "This wasn't for you."
            "His rough handling caused the deer to kick again."
            "The snare around its neck probably made it impossible to scream anymore."
            "I could hear him chuckling softly."
            $ stat_sanity -= 10
            "It made me feel sick."
            m empty "I s'pose I can still make use of ya."
            scene cg_mason_deer2_blood with dissolve
            play sound "music/sfx_blood_drip.ogg"
            "I saw the flash of a knife, and a moment later, blood was pouring down from a gash in the deer's throat."
            "... At least it wasn't suffering anymore..."
            scene black with dissolve
            stop music fadeout 5.0
            "He grunted, hoisting the deer up as he opened the loop of the snare."
            "He heaved the whole carcass over his shoulder."
            "I dipped behind cover just as he turned around."
            "I remained still as I heard his heavy footsteps leave the area."
            "I didn't get up for a while afterwards."
            $ stat_sanity -= 10
            "It was hard to shake the image of the deer from my mind."
            "Eventually, I managed to climb to my feet."
            "I have to forget about it and move on."
            "At least... he should be busy for a bit."
            stop music fadeout 1.0
        "Get out of here" if True:
            "Whatever is screaming is not my problem."
            "I'm not going to risk drawing any attention to myself."
            "I quickly and carefully crept away from the sound."
            $ map_location = "Thicket"
            $ arrivedby = "new"
            if fire != 0:
                $ fire = 0
                $ location_temp = "cold"
                stop music fadeout 0.5
                hide campfire with dissolve
    jump mason_turn_order

label event_mason_bear_death:
    $ phase = "event"
    $ sleep = 0
    scene black
    $ persistent.cgs_mason.add("cg_mason_bear")
    $ renpy.save_persistent()
    stop ambient fadeout 1.0
    play music "music/ambient_dire_situation.ogg" fadein 1.0
    play sound "music/sfx_impact_forest.ogg"
    "I awoke to a slam on my chest." with vpunch
    "I could barely make sense of the pain as my brain struggled to wake up in panic."
    if meme_mode:
        scene cg_mason_bear1_hat with dissolve
    elif True:
        scene cg_mason_bear1 with dissolve
    play sound "<from 0.0 to 1.0>music/sfx_bear_growl.ogg"
    "A dark, enormous shape covered me."
    "Then I heard the loud sniffing and began to make out some details in the dark."
    "A bear."
    if meme_mode:
        scene cg_mason_bear2_hat with dissolve
    elif True:
        scene cg_mason_bear2 with dissolve
    "I screamed involuntarily, and the bear reacted."
    $ stat_health -= 20
    play sound "music/sfx_bone_snap.ogg"
    "Inches of claws sank into my chest with an impossible weight behind them." with vpunch
    "I fumbled for my knife."
    "I managed to grasp it and take a swipe at the face in front of me."
    play sound "<from 0.0 to 3.0>music/sfx_bear_roar.ogg"
    "It screamed with me."
    $ stat_health -= 100
    scene black with dissolve
    play sound "music/sfx_impact_forest.ogg"
    stop music
    "I kept screaming as huge jaws clamped down on my neck." with vpunch
    "My scream became a gurgle as the flesh from my throat was torn away."
    "I had no time to process anything."
    "Thankfully, everything went dark quickly."
    "In a way, as everything faded, I thought this beast was merciful."
    $ quick_menu = False
    window hide
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_mason.add("You smelled delicious")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_11
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You smelled delicious")
    $ renpy.pause(hard=True)

label event_mason_death_health:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        $ sleep = 0
        call mason_display_subroutine from _call_mason_display_subroutine_17
        "I slowly opened my eyes."
        scene cg_mason_bleedout
        $ persistent.cgs_mason.add("cg_mason_bleedout")
        $ renpy.save_persistent()
        "... Blood." with eyedissolve
    elif True:
        if arrivedby == "idle":
            "I looked blearily at the blood below me."
        elif True:
            "As I tried to take another step, my knees buckled beneath me."
        scene cg_mason_bleedout
        $ persistent.cgs_mason.add("cg_mason_bleedout")
        $ renpy.save_persistent()
        play sound "music/sfx_impact_forest.ogg"
        "I fell to the ground." with vpunch
    "I wheezed and tried to push myself up."
    "My shaking arms wouldn't cooperate."
    "Part of me felt like I should be panicking."
    "But I was too exhausted."
    "The sound of leaves rustling was a strange lullaby."
    "It was cold, but my pain was fading."
    "I struggled to breathe for a while, just listening to the life around me."
    label bloodjumper:
    if meme_mode:
        "I wrote the words \"Fuck You\" on the ground in my blood."
    elif True:
        "My blood seeped into the ground."
    scene black with eyedissolve
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    "Then, I closed my eyes."
    $ quick_menu = False
    window hide
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_mason.add("You bled out")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_12
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You bled out")
    $ renpy.pause(hard=True)

label event_mason_knife_suicide:
    $ phase = "event"
    play sound "music/sfx_scrape_slow.ogg"
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    "I shakily withdrew my knife and held it in front of me."
    "For a split second, I saw the hollow reflection of an exhausted face in the metal."
    "That can't be my face."
    "My eyes are already dead..."
    if map_location != "House":
        "A cold wind turned the rustling leaves into a chaotic static."
    elif True:
        "A cold wind outside turned the muted rustling leaves into a soft static."
    "Already dead..."
    "I held the knife up to my throat."
    "It's wrong that my body is still standing when the rest of me died already."
    "I pressed it, testing the sensation of blade digging into my skin."
    "I thought of him."
    "Out there... hunting for me."
    "He wants to feel my skin splitting open."
    $ stat_health -= 3
    "I felt the burning slide of metal and blood trickling down my neck."
    "Well..."
    "My eyes rolled back."
    $ stat_health -= 30
    play sound "music/sfx_blood_drip.ogg"
    "Blood was gushing now and the pain was both intense and somehow far from me."
    "He won't have that pleasure."
    scene black with eyedissolve
    hide screen effect_health
    hide screen effect_ice
    play sound "music/sfx_impact_forest.ogg"
    "My legs crumpled under me." with vpunch
    pause(1.0)
    scene black with dissolve
    show bluefire with dissolve
    "The dirt and rotting leaves welcomed my body."
    scene black with dissolve
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_mason.add("You denied him the pleasure")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_13
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You denied him the pleasure")
    $ renpy.pause(hard=True)

label event_mason_timedeath:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        $ sleep = 0
        call mason_display_subroutine from _call_mason_display_subroutine_15
        "I could barely move my stiff body."
        "I shook myself awake and stood up slowly."
    if fire != 0:
        $ fire = 0
        $ location_temp = "cold"
        stop music fadeout 0.5
        hide campfire with dissolve
        call mason_display_subroutine from _call_mason_display_subroutine_16
        "I watched as the flames in front of me died."
    if map_location == "House":
        "Something is calling me."
        "I couldn't hear it, but I could feel it."
        $ map_location = "Meadow"
        call mason_display_subroutine from _call_mason_display_subroutine_18
        "I walked outside, and pushed through the trees."
    "I felt a spark of cold on my face."
    play music "music/music_snow.ogg" fadein 3.0
    stop ambient fadeout 1.0
    scene cg_mason_snow with dissolve
    hide screen effect_health
    hide screen effect_ice
    if achievement.has("ach_acolyte_of_decay") != True:
        $ persistent.ach_acolyte_of_decay = True
        $ achievement.grant("ach_acolyte_of_decay")
        init:
            $ achievement.register("ach_acolyte_of_decay")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_acolyte_of_decay == True and achievement.has("ach_acolyte_of_decay") != True:
                $ achievement.grant("ach_acolyte_of_decay")
                $ achievement.register("ach_acolyte_of_decay")
                $ achievement.sync()
    $ persistent.cgs_mason.add("cg_mason_snow")
    $ renpy.save_persistent()
    "I looked up to the sky."
    "It's... snowing."
    p "... Ahh."
    "I stared up at the moon."
    "This is it, isn't it?"
    "I can't make a fire anymore."
    if "item_trail_mix" not in inventory and "item_fish" not in inventory and "item_cookedfish" not in inventory and "item_baneberries" not in inventory and "item_saskatoons" not in inventory:
        "I'm starving and there's nothing left to eat."
    "It's been days."
    "I've gone past the point of panic..."
    "Then past the point of despair."
    "Around me, snow began falling in clumps."
    "Silently obscuring the world surrounding me."
    "Like a dream..."
    "I looked up at the snow slowly pouring from the sky."
    "I didn't know I could be so alone."
    lich "You have never been alone."
    "I spun around, trying to find the voice."
    "It didn't seem to come from any direction."
    p "H... hello?"
    "I guess it isn't so strange to be hearing voices now."
    "I stilled myself and tried to listen."
    lich "You don't have to be afraid."
    p "Where- Who are you?"
    if player_name.upper() == "LAWRENCE" or player_name.upper() == "LAW":
        lich "I have the same name as you."
    elif True:
        lich "I don't need a name anymore."
    "..."
    lich "I've been watching you."
    "I'm probably not even hearing anyone."
    "I'm just hallucinating."
    lich "You move in a delicate way."
    lich "A timid touch with time."
    lich "I've watched you dip your toes in the water just to step back."
    lich "Always stepping back."
    "I shivered in the darkness."
    if persistent.deathcounter == 420 and meme_mode:
        lich "You have tasted death before though... haven't you?"
        lich "420 times..."
        "The creature let out a long and strange laugh."
        lich "That reminds me of when I used to be more human."
        lich "Ahhh..."
        lich "I miss weed."
    elif persistent.deathcounter >= 100:
        lich "You have tasted death before though... haven't you?"
        lich "In fact, it clings to you."
        "The voice chuckled softly."
        lich "You and I have that in common."
        lich "A taste of death... over [persistent.deathcounter] times..."
        lich "Well, you're an expert by now."
    elif persistent.deathcounter == 69 and meme_mode:
        lich "You have tasted death before though... haven't you?"
        lich "Yes... 69 times..."
        lich "And death was tasting you back..."
        lich "... Nice..."
    elif persistent.deathcounter >= 2:
        lich "You have tasted death before though... haven't you?"
        lich "Yes... [persistent.deathcounter] times..."
    elif persistent.deathcounter >= 1:
        lich "You have tasted death before though... haven't you?"
        lich "Only once! But you know its taste."
    elif True:
        lich "Oh."
        lich "But there's something very special about you..."
        "I swore I almost felt a cold caress."
        lich "You've never tasted death. Not even once."
        lich "You came straight to me..."
        "The voice I heard all around me swelled with emotion."
        lich "Made for me... You came to me..."
        lich "That must have been difficult."
        lich "You are so pure... I understand your sacrifice."
        lich "And I appreciate it very much."
    "I felt a hint of warmth as a tear rolled down my cheek."
    "The voice was so soft now."
    lich "There's no more chrome and glass."
    lich "No more howling into empty streets."
    lich "You came here, to the root and bone..."
    lich "Softly rotting..."
    "I stepped forward."
    "I tried to speak, but my face was so cold."
    "I fell to my knees."
    lich "Shhh."
    lich "I've found a place on the edge of a knife,"
    lich "Between decay and the devil."
    lich "You've come home."
    lich "You'll never hurt again."
    "I looked up as the snow landed on my face."
    "At the moon..."
    lich "Yes. You belong with me."
    "Something wrapped around me."
    if persistent.deathcounter == 0:
        $ persistent.greencounter = True
        $ renpy.save_persistent()
        lich "Mine, forever."
        if achievement.has("ach_green") != True:
            $ persistent.ach_green = True
            $ achievement.grant("ach_green")
            init:
                $ achievement.register("ach_green")
                $ achievement.sync()
                $ renpy.save_persistent()
                if persistent.ach_green == True and achievement.has("ach_green") != True:
                    $ achievement.grant("ach_green")
                    $ achievement.register("ach_green")
                    $ achievement.sync()
    stop music fadeout 10.0
    scene black with eyedissolve
    "The pain from the cold slipped away."
    "Just as the voice promised."
    "I got to my feet and I began walking."
    "The forming ice crystals under my skin were crunching."
    "But I walked anyway."
    "There was no pain."
    "And I wasn't in control anymore."
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_mason.add("You changed")
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_14
    play music "music/music_changed.ogg" fadein 1.0
    scene bg_endslate_change with Dissolve(2.0)
    show screen bg_endslate_change_text("You Changed"," ")
    $ renpy.pause(hard=True)

label event_mason_tourniquet:
    $ phase = "event"
    "I'm not going to last much longer like this..."
    "I have to do something."
    "I pulled out the small knife from my bag and looked at my clothing."
    "It's already so cold..."
    "But I'm losing too much blood."
    "I started cutting some fabric from the bottom of my shirt."
    "Once I had a couple strips, I began to tie them above the wounds on my arm and leg."
    $ stat_sanity -= 5
    "I winced in pain." with vpunch
    "I wish I didn't have to do this..."
    "I wish I wasn't here."
    "I steeled myself and tied the knots tight."
    $ wound = 1
    $ renpy.notify("The bleeding has slowed.")
    "This should help me last a little longer..."
    $ arrivedby = "special"
    jump mason_turn_nostats
label event_mason_sleepfail:
    $ phase = "event"
    "I tried to fall asleep..."
    "But I just wasn't tired enough."
    $ arrivedby = "special"
    jump mason_turn_nostats
label event_mason_drawmap:
    $ phase = "event"
    "I pulled the paper and pencil out of the bag."
    "I could draw a map and get my bearings with this..."
    "I had a thought that this might have been the exact reason he put paper in the bag."
    "I shook my head."
    "It doesn't matter."
    $ renpy.notify("Map Added!")
    "I scrawled a quick drawing of my surroundings and shoved the 'map' back in the bag."
    $ arrivedby = "special"
    jump mason_turn_nostats
label event_mason_eat_trailmix:
    $ phase = "event"
    $ inventory.remove("item_trail_mix")
    "I pulled the bag of trail mix out of the bag."
    "I popped it open and sniffed inside."
    "I considered the idea that he might be trying to poison me."
    "But... why would he do that?"
    "He's made it pretty clear that he wants to 'hunt' me."
    "I grit my teeth at my own indecision before defiantly popping an almond into my mouth."
    "..."
    "It seems fine."
    $ stat_food += 24
    "Before long, I was devouring the contents of the bag."
    "I was a little annoyed with myself for eating the whole thing, but the relief of not being hungry was worth it."
    $ arrivedby = "special"
    jump mason_turn_nostats
label event_mason_eat_saskatoons:
    $ phase = "event"
    $ inventory.remove("item_saskatoons")
    "I grabbed my handful of berries and popped one in my mouth."
    "A little tart... but not bad!"
    $ stat_food += 10
    "I quickly ate the rest of the berries."
    "Ahh... that feels a little better."
    $ arrivedby = "special"
    jump mason_turn_nostats
label event_mason_eat_fish:
    $ phase = "event"
    if "item_fish" in inventory:
        $ inventory.remove("item_fish")
    if "item_fish_cute" in inventory:
        $ inventory.remove("item_fish_cute")
    "I held out the fish that I caught."
    if meme_mode:
        "I stared into its pleading eyes."
    elif True:
        "I stared into its dead eyes for a moment."
    p "Thanks for helping me not die..."
    "I pulled out the little knife from my bag and went to work cutting a piece off."
    if meme_mode:
        "It made a tiny scream before going limp in my hand."
    "C'mon... people pay good money for this in some places."
    "I tentatively nibbled at the chunk I carved."
    "It's... not that bad."
    $ stat_food += 12
    "I ate the rest of the fish meat quickly and quietly."
    p "Ahh..."
    "I felt a bit better."
    $ arrivedby = "special"
    jump mason_turn_nostats
label event_mason_eat_cookedfish:
    $ phase = "event"
    if "item_cookedfish" in inventory:
        $ inventory.remove("item_cookedfish")
    if "item_cookedfish_cute" in inventory:
        $ inventory.remove("item_cookedfish_cute")
    "I held out my fish and grabbed the small knife from my bag."
    "I carved a bit of cooked meat away and placed it in my mouth."
    "!!!"
    "I don't know if it's just from being out here in the cold or starving, but..."
    "The flaky soft fish tasted amazing."
    $ stat_food += 24
    "I tried to savour my meal, but I could hardly stop myself."
    "Once it was gone, I sighed and wiped my mouth."
    "I felt a lot better after that."
    $ arrivedby = "special"
    jump mason_turn_nostats
label event_mason_put_out_fire:
    $ fire = 0
    $ location_temp = "cold"
    stop music fadeout 0.5
    hide campfire with dissolve
    "I quickly put out my fire."
    $ arrivedby = "special"
    jump mason_turn_nostats



label game_start_celia:
    $ food = 20
    $ energy = 24
    $ gamepath = "celia"
    $ map_location = "Room"
    $ inventory.append("item_shackles")
    $ renpy.music.set_volume(0.2, channel="ambient")
    play ambient "music/ambient_lights_hum_loop.ogg" fadein 3.0

    "My head hurts..."
    "I slowly opened my eyes and pried my face off the hard surface it was stuck to."
    scene bg_celia_room:
        yanchor 0.0
        yalign 1.0
    show sprite_celia_desk:
        yalign 1.0
        xalign 0.5
    with dissolve
    "A desk..?"
    play sound "music/sfx_chain.ogg"
    "I tried to pull away from the desk, making a loud clang." with hpunch
    "Handcuffs..."
    "Each of my hands was handcuffed to a desk leg, keeping me painfully seated in the chair and bent low."
    "And my clothing..."
    "I didn't recognize it."
    c empty "{i}Finally.{/i}"
    scene bg_celia_room:
        yalign 1.0
        easeout_expo 0.25 yalign 0.0
    show sprite_celia_desk:
        yalign 1.0
        xalign 0.5
        yoffset 0
        easeout_expo 0.25 yoffset 200
    pause(0.25)
    show celia relaxed behind sprite_celia_desk with dissolve:
        zoom 0.9
        yoffset -50
        xalign 0.5
    play music "music/celias_theme.ogg" fadein 1.0
    "I gasped at the face of the woman looking down at me."
    p "Who?"
    c "I don't know what they drugged you with, but I was starting to worry you'd just lay there drooling forever."
    c relaxed "Are you awake now?"
    p "Uh-"
    c normal "Good."
    $ celia_name = "Celia"
    c "My name is Celia."
    if meme_mode:
        c "You may call me Celia or 'Mommy'."
        p "Wait, what was that last one?"
        c "I said 'Ma'am'."
    elif True:
        c "You may call me Celia or 'Ma'am'."
    show celia relaxed
    "She stepped a bit closer, eyeing me up and down."
    "Something about her sharp gaze sent a shiver down my spine."
    c "This is the part where you introduce yourself."
    menu:
        " "
        "Say my name" if True:
            $ celia_love += 1
            p "Uh... my name is [player_name]."
            if player_name.lower() == "derek":
                $ celia_love -= 1
                c disgusted "Tch."
                c "What an ugly name."
            elif (player_name.lower() == "harold" or player_name.lower() == "harry"):
                $ celia_love -= 1
                c disgusted "Tch."
                c "... My rotten luck."
            elif True:
                "I didn't see the point of resisting in this position."
                "For a moment she just kept looking at me."
                "Appraising."
                c normal "Good."
        "\"I don't have to tell you anything.\"" if True:

            c question "Oh?"
            $ celia_love -= 1
            c semiserious "I suppose you don't {i}have{/i} to do anything."
            "She pulled something small and black from her pocket."
            "As she stepped closer, I realized it was a taser."
            "I heard the sharp crack as she turned it on."
            p "Wait-"
            show celia sadistic
            "She slammed it down onto the back of my handcuffed hand." with vpunch
            $ stat_health -= 5
            $ stat_sanity -= 10
            p "HRNNG!" with smallshake
            "My ears were still ringing as she began talking again."
            c normal "You can behave however you like."
            c semiserious "But I think you'll find that you're not immune to the consequences of your decisions."
            "I gritted my teeth as she put the device back in her pocket."
            c question "Now, shall we continue, [player_name]?"
            "... She already knew my damn name!"
            c mocking "Oh don't look so surprised."
        "Stay quiet" if True:

            "..."
            c serious "Hm."
            c semiserious "I understand that you're new and don't quite understand our dynamic yet."
            "She pulled something small and black from her pocket."
            "As she stepped closer, I realized it was a taser."
            "I heard the sharp crack as she turned it on for a moment, demonstrating."
            c serious "My requests aren't really optional."
            c semiserious "I think you'll find that it's in your best interest to follow them."
            "She looked down at me, waiting for an answer."
            menu:
                " "
                "Say my name" if True:
                    p "...My name is [player_name]."
                    show celia relaxed
                    "Her posture relaxed and she put the taser back into her pocket."
                    c normal "Now that wasn't so hard, hm?"
                "Refuse to speak" if True:
                    c serious "Tch."
                    show celia angry
                    "She slammed it down onto the back of my handcuffed hand." with vpunch
                    $ stat_health -= 5
                    $ stat_sanity -= 10
                    p "HRNNG" with smallshake
                    "My ears were still ringing as she began talking again."
                    c relaxed "You can behave however you like."
                    c semiserious "But I think you'll find that you're not immune to the consequences of your decisions."
                    "I gritted my teeth as she put the device back in her pocket."
                    c normal "Now, shall we continue, [player_name]?"
                    "... She already knew my damn name!"
                    c mocking "Oh don't look so surprised."
    show celia relaxed
    "She walked in front of the desk and tapped it gently with her nail."
    c semiserious "You were very expensive."
    c relaxed "So I'm expecting you to perform."
    c "Just do as you're told. It isn't that hard."
    c normal "If you're good, you get to live."
    c "I'll bring you food and take care of you."
    c semiserious "If you're not, then you suffer."
    c normal "Simple."
    show celia surprised
    "Suddenly, the sound of a phone alert dinged."
    c serious "..."
    c "Tsk."
    hide celia with dissolve
    show celia phone behind sprite_celia_desk with dissolve:
        zoom 0.75
        xalign 0.25
        yoffset 0
    "She turned around and started rapidly tapping at her phone."
    if meme_mode:
        c "These fucking games are so needy."
        c "Just let me see the art, you don't need to ping me 47 times a day!"
    elif True:
        c "Fucking... moron..."
    "My gaze wandered around the old, dirty room."
    "It definitely looks like it was abandoned..."
    "My eyes locked on to a dark stain by my feet."
    "What the fuck..."
    "That was definitely... blood..."
    "My attention was snapped away from the stained carpet as I heard her hiss a string of curses under her breath."
    c "All right..."
    show celia serious with dissolve:
        zoom 0.9
        xalign 0.5
        yoffset -50
    c "Apparently I have to go babysit some manchildren at work."
    c "I have to go."
    show celia surprised
    p "Wait!"
    p "I think there's been some kind of mistake-"
    p "I didn't sign up for this! I was kidnapped!"
    show celia laughing at laugh:
        yoffset -50
    c "Pffft- Hahaha!"
    c normal "That's not my problem."
    c relaxed "Now shut up. I'll be back later."
    "She stepped towards the door."
    p "Wh- you're just gonna leave me like this!?"
    "I pulled at the handcuffs."
    if pronoun == "he":
        c semiserious "Be a good rat and stay put."
    elif True:
        c normal "If you're a good little mouse, then maybe we'll get you somewhere more comfortable next time, hm?"
    "She pulled open the door."
    hide celia with dissolve
    stop music fadeout 1.0
    "And then she was gone."
    "I listened to the click of her heels on the floor disappear outside."
    $ arrivedby = "special"
    "Soon after, only the mechanical hum of the fluorescent lights remained."

label celia_turn_order:
    $ phase = "event"
    hide screen mini_screen
    hide screen inventory_item
    hide screen status_update_health
    hide screen status_update_sanity
    hide screen status_update_energy
    hide screen status_update_food
    hide screen status_update_temp_increase
    hide screen status_update_temp_decrease
    hide screen notify
    $ hours += 1
    $ total_hours += 1
    $ stat_food -= 1
    if wound == 1:
        $ stat_health -= 3
    if wound == 2:
        $ stat_health -= 5
    if sleep > 0:
        $ energy += 3
        if energy >= 24:
            $ energy = 24
            $ sleep = 0
            $ arrivedby = "wakeup"
    elif True:
        if food <= 0:
            $ stat_energy -= 3
        elif True:
            $ stat_energy -= 1
    if map_location != "Basement":
        if sanity < 10:
            $ renpy.music.set_volume(1.0, channel="ambient")
        elif sanity < 30:
            $ renpy.music.set_volume(0.75, channel="ambient")
        elif sanity < 50:
            $ renpy.music.set_volume(0.5, channel="ambient")
        elif sanity < 70:
            $ renpy.music.set_volume(0.35, channel="ambient")
        elif True:
            $ renpy.music.set_volume(0.2, channel="ambient")
    if sanity <= 50 and event_celia_sound_1 == 0:
        $ event_celia_sound_1 = 1
        play sound ["<silence 4.0>","<from 0.0 to 1.0>music/sfx_laugh.ogg"]
    if sanity <= 20 and event_celia_sound_2 == 0:
        $ event_celia_sound_2 = 1
        play sound ["<silence 10.0>","music/sfx_sigh.ogg"]
    call celia_display_subroutine from _call_celia_display_subroutine
    label celia_turn_nostats:
        call celia_event_subroutine from _call_celia_event_subroutine
        $ phase = "adventure"
        $ renpy.pause(hard=True)

label celia_display_subroutine:
    if sleep > 0:
        scene black with eyedissolve
    elif True:
        if map_location == "Room":
            window show
            $ persistent.bgs_seen.add("bg_celia_room")
            $ renpy.save_persistent()
            if celia_bound == 1:
                scene bg_celia_room:
                    yalign 0.0
                show sprite_celia_desk:
                    yoffset 200
                with dissolve
            elif True:
                if celia_room_window_smashed == 1:
                    scene bg_celia_room:
                        yalign 0.0
                    show bg_celia_room_broken
                    with dissolve
                elif True:
                    scene bg_celia_room:
                        yalign 0.0
                    with dissolve
        elif map_location == "Office":
            window show
            $ persistent.bgs_seen.add("bg_celia_office")
            $ renpy.save_persistent()
            scene bg_celia_office with dissolve
        elif map_location == "Basement":
            window show
            $ persistent.bgs_seen.add("bg_celia_basement")
            $ renpy.save_persistent()
            scene bg_celia_basement with dissolve
        elif map_location == "Lounge":
            window show
            $ persistent.bgs_seen.add("bg_celia_lounge")
            $ renpy.save_persistent()
            scene bg_celia_lounge with dissolve
        elif map_location == "Elevator":
            window show
            $ persistent.bgs_seen.add("bg_celia_elevator")
            $ renpy.save_persistent()
            scene bg_celia_elevator with dissolve
        elif map_location == "Break Room":
            window show
            $ persistent.bgs_seen.add("bg_celia_breakroom")
            $ renpy.save_persistent()
            scene bg_celia_breakroom with dissolve
    return




label celia_event_subroutine:

    if energy <= 0:
        label celia_energy_passout:
            $ phase = "event"
            $ arrivedby = "sleep"
            "My vision wavered."
            "I'm so tired..."
            "I couldn't keep my eyes open any longer."
            "I found a vaguely comfortable position and laid down."
            $ sleep = 12
            jump celia_turn_order

    if sanity <= 0:
        jump event_celia_basement_cage

    if total_hours > 23 and event_celia_harrison == 0:
        jump celia_event_harrison
    if total_hours > 40 and event_celia_spacer == 0:
        jump event_celia_spacer
    if total_hours > 60 and event_celia_donuts == 0:
        jump event_celia_donuts
    if event_celia_donuts == 1 and event_celia_complain == 0 and sleep > 0:
        jump event_celia_complain
    if total_hours > 86 and event_celia_complain == 1 and event_celia_endgame == 0:
        jump event_celia_endgame


    if event_celia_harrison == 1 and arrivedby == "idle" and event_celia_findpin == 0 and map_location == "Room":
        $ event_celia_findpin = 1
        jump event_celia_findpin
    if total_hours > 60 and food <= 5 and event_celia_headache == 0 and arrivedby == "idle":
        jump event_celia_headache
    if sanity <= 50 and event_celia_sanity_1 == 0 and arrivedby == "idle":
        jump event_celia_sanity_1
    if sanity <= 30 and event_celia_sanity_2 == 0 and event_celia_sanity_1 == 1 and arrivedby == "idle":
        jump event_celia_sanity_2
    if food <= 0 and event_celia_starving == 0 and arrivedby == "idle":
        $ event_celia_starving = 1
        jump event_celia_starving
    if meme_mode and total_hours == 50 and map_location == "Room":
        jump event_celia_drunk



    if map_location == "Room":

        if sleep > 1:
            label celia_room_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump celia_turn_order
        if arrivedby == "wakeup":
            label celia_room_wakingup:
                $ phase = "event"
                "I gasped as I woke up."
                if meme_mode:
                    p "This isn't my house."
                    p "Ugh..."
                    p "Still smells like moldy carpet in here."
                elif True:
                    "I looked around myself and remembered where I was."
                    "I groaned and shook myself alert."
                $ arrivedby = "special"
                jump celia_turn_nostats

        if arrivedby == "new":
            $ arrivedby = "idle"
            "I entered the small, dim room."
        elif arrivedby == "idle":
            if celia_room_idling == 0:
                $ celia_room_idling += 1
                "There doesn't seem to be anything I can do."
                if celia_desk_escape_attempt >= 3:
                    "I leaned against the wall and tried to get comfortable."
                elif True:
                    "I laid my head down and tried to get comfortable."
            elif celia_room_idling == 3:
                $ celia_room_idling += 1
                if celia_desk_escape_attempt >= 3:
                    "I shuffled uncomfortably."
                    "I think I can smell some kind of mold..."
                elif True:
                    "I shuffled slightly in the chair."
                    "I think I can smell some kind of mold..."
            elif celia_room_idling == 5:
                $ celia_room_idling += 1
                "I tried to keep my mind from wandering."
                "What the hell does this woman... Celia... even want with me?"
                "Why is she doing this?"
                if celia_desk_escape_attempt >= 3:
                    "My head drooped."
                elif True:
                    "My forehead hit the desk with a light thud."
                "There's nothing I can do to figure any of this out."
            elif True:
                $ celia_room_idling += 1
                if celia_bound == 1:
                    "I stayed in the room at the desk."
                elif True:
                    "I stayed in the room."

        label celia_room_travel:
            $ phase = "adventure"
            menu:
                " "
                "Stay here" if True:
                    $ map_location = "Room"
                    $ arrivedby = "idle"
                    jump celia_turn_order
                "Leave the room" if celia_bound == 0 and event_celia_room_door_locked == 1 and celia_room_window_smashed == 0 and "item_pin" not in inventory:
                    jump event_celia_room_door_locked
                "{image=menu_pin}Leave the room{space=60}" if celia_bound == 0 and event_celia_room_door_locked == 1 and celia_room_window_smashed == 0 and "item_pin" in inventory and not renpy.variant("small"):
                    jump event_celia_unlock_room
                "{image=menu_pin_large}Leave the room{space=60}" if celia_bound == 0 and event_celia_room_door_locked == 1 and celia_room_window_smashed == 0 and "item_pin" in inventory and renpy.variant("small"):
                    jump event_celia_unlock_room
                "Leave the room" if (celia_bound == 0 and event_celia_room_door_locked == 0) or (celia_bound == 0 and celia_room_window_smashed == 1):
                    $ map_location = "Lounge"
                    $ arrivedby = "new"
                    jump celia_turn_order
        return



    if map_location == "Lounge":

        if sleep > 1:
            label celia_lounge_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump celia_turn_order
        if arrivedby == "wakeup":
            label celia_lounge_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I slowly woke up."
                if meme_mode:
                    "I sucked in a deep breath."
                    p "Mondays, amirite?"
                    "I had no idea what day it is, but it's the thought that counts."
                elif True:
                    "I raised myself off the dusty office chair."
                $ arrivedby = "special"
                jump celia_turn_nostats

        if event_celia_enter_lounge == 0:
            $ event_celia_enter_lounge = 1
            "I peeked out of the room."
            "A long hallway ended in what appeared to be a sort of lounge area."
            "More cabinets and papers littered the place."
            "Past the lounge area was a door that looked like it went to another office."
            "However, my attention was much more focused on what appeared to be an elevator."
            "That could be my ticket out of here!"
        elif True:
            if arrivedby == "new":
                $ arrivedby = "idle"
                "I entered the larger open area from the hallway."
            elif arrivedby == "idle":
                "I stayed on the dusty seat in the open area."
        label celia_lounge_travel:
            $ phase = "adventure"
            menu:
                " "
                "Stay here" if True:
                    $ map_location = "Lounge"
                    $ arrivedby = "idle"
                    jump celia_turn_order
                "Go to the small office" if True:
                    $ map_location = "Room"
                    $ arrivedby = "new"
                    jump celia_turn_order
                "Try the elevator" if event_celia_try_elevator == 0:
                    jump event_celia_try_elevator
                "Try the door at the end of the lounge" if event_celia_try_office == 0:
                    jump event_celia_try_office
                "Try the door by the elevator" if event_celia_enter_breakroom == 0:
                    "I moved the handle on the door."
                    "It's unlocked!"
                    $ map_location = "Break Room"
                    $ arrivedby = "new"
                    jump celia_turn_order
                "Go in the elevator" if event_celia_try_elevator == 1:
                    $ map_location = "Elevator"
                    $ arrivedby = "new"
                    if meme_mode:
                        play music "music/music_elevator_muzak.ogg" fadein 1.0
                    jump celia_turn_order
                "Go to the lounge office" if event_celia_try_office == 1:
                    if celia_office_locked == 0:
                        $ map_location = "Office"
                        $ arrivedby = "new"
                        jump celia_turn_order
                    if celia_office_locked == 1:
                        "The door is locked..."
                        $ arrivedby = "special"
                        jump celia_turn_nostats
                "Go to the break room" if event_celia_enter_breakroom == 1:
                    $ map_location = "Break Room"
                    $ arrivedby = "new"
                    jump celia_turn_order
        return



    if map_location == "Elevator":

        if sleep > 1:
            label celia_elevator_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump celia_turn_order
        if arrivedby == "wakeup":
            label celia_elevator_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                if meme_mode:
                    "-Record scratch- You're probably wondering how I got here."
                    "I shook my head abruptly, and peeled myself off the dirty elevator floor."
                elif True:
                    "I looked around myself and remembered where I was."
                    "I groaned and slowly got up from the hard floor."
                $ arrivedby = "special"
                jump celia_turn_nostats


        if arrivedby == "new":
            $ arrivedby = "idle"
            "I entered the small elevator."
        elif arrivedby == "idle":
            "I stayed in the elevator."
        label celia_elevator_travel:
            $ phase = "adventure"
            menu:
                " "
                "Stay here" if True:
                    $ map_location = "Elevator"
                    $ arrivedby = "idle"
                    jump celia_turn_order
                "Leave the elevator" if True:
                    if meme_mode:
                        stop music fadeout 1.0
                    $ map_location = "Lounge"
                    $ arrivedby = "new"
                    jump celia_turn_order
        return



    if map_location == "Office":

        if sleep > 1:
            label celia_office_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump celia_turn_order
        if arrivedby == "wakeup":
            label celia_office_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                if meme_mode:
                    "It smells like an alcoholic's torture office..."
                    "I looked around myself."
                    p "Oh."
                elif True:
                    "I looked around myself and remembered where I was."
                    "I groaned and shook myself awake."
                $ arrivedby = "special"
                jump celia_turn_nostats

        if event_celia_enter_office == 0:
            $ event_celia_enter_office = 1
            "I tentatively entered the room."
            "Definitely an office..."
            "It's cleaner though. Someone's been in here..."
            "I stopped in place as I noticed something out of place."
            "A picture of a man, printed out and blown up."
            "And... darts in it."
            "Celia must use this room."
            "And she must really hate whoever that man is."
            "Something about this room made me really nervous."
            "But she might keep something useful in here..."
        elif True:
            if arrivedby == "new":
                $ arrivedby = "idle"
                "I crept into the large office."
            elif arrivedby == "idle":
                "I stayed and rested in the large office."
        label celia_office_travel:
            $ phase = "adventure"
            menu:
                " "
                "Stay here" if True:
                    $ map_location = "Office"
                    $ arrivedby = "idle"
                    jump celia_turn_order
                "Leave the office" if True:
                    $ map_location = "Lounge"
                    $ arrivedby = "new"
                    jump celia_turn_order
                "Use the number pad" if event_celia_unlock_basement == 0 and event_celia_discover_basement == 1 and celia_basement_locked == 1:
                    window hide
                    scene bg_celia_numpad with dissolve
                    show screen numpad_input("") with dissolve

                    $ numpad_input = renpy.input("",allow="0123456789",length=4,screen="numpad_input")

                    if numpad_input == "0247":
                        jump event_celia_numpad_correct
                    elif numpad_input == "":
                        jump event_celia_numpad_empty
                    elif numpad_input == "6969" or numpad_input == "69":
                        jump event_celia_numpad_69
                    elif numpad_input == "0420" or numpad_input == "4200" or numpad_input == "420":
                        jump event_celia_numpad_420
                    elif numpad_input == "1988":
                        jump event_celia_numpad_1988
                    elif numpad_input == "8008":
                        jump event_celia_numpad_8008
                    elif True:
                        jump event_celia_numpad_incorrect
                "Go downstairs" if celia_basement_locked == 0:
                    $ map_location = "Basement"
                    $ arrivedby = "new"
                    jump celia_turn_order

        return



    if map_location == "Break Room":

        if sleep > 1:
            label celia_breakroom_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump celia_turn_order
        if arrivedby == "wakeup":
            label celia_breakroom_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                if meme_mode:
                    "I looked around myself."
                    "This really isn't that different from the break room at work."
                    p "Back to the grind, I guess..."
                elif True:
                    "I looked around myself and remembered where I was."
                    "I groaned and shook myself awake."
                $ arrivedby = "special"
                jump celia_turn_nostats

        if event_celia_enter_breakroom == 0:
            $ event_celia_enter_breakroom = 1
            "I entered the room and looked around."
            "This must be... some kind of break room."
            "Or at least it used to be."
            "Wait!"
            "I focused on the sink at the side of the room."
            "Water!"
            "I quickly ran up and turned the tap."
            "..."
            "Nothing."
            "Ugh... I guess no one is paying for plumbing here."
            "I sighed and sat down."
        elif True:
            if arrivedby == "new":
                $ arrivedby = "idle"
                "I entered the break room."
            elif arrivedby == "idle":
                "I stayed and rested in the break room."
        label celia_breakroom_travel:
            $ phase = "adventure"
            menu:
                " "
                "Stay here" if True:
                    $ map_location = "Break Room"
                    $ arrivedby = "idle"
                    jump celia_turn_order
                "Leave the break room" if True:
                    $ map_location = "Lounge"
                    $ arrivedby = "new"
                    jump celia_turn_order
        return



    if map_location == "Basement":
        if sleep > 1:
            label celia_basement_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump celia_turn_order
        if arrivedby == "wakeup":
            label celia_basement_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                "I looked around myself and remembered where I was."
                if meme_mode:
                    "Wait, this isn't Strade's basement..."
                elif True:
                    "I groaned and shook myself awake."
                $ arrivedby = "special"
                jump celia_turn_nostats

        if event_celia_enter_basement == 0:
            $ renpy.music.set_volume(1.0, channel="ambient")
            play ambient "music/ambient_basement.ogg"
            $ event_celia_enter_basement = 1
            "What the fuck?"
            "I froze and stared."
            $ stat_sanity -= 10
            "A tarp..."
            "Blood..."
            "And whatever the hell was going on with those mannequins."
            "What has she been doing down here..?"
        if arrivedby == "new":
            $ renpy.music.set_volume(1.0, channel="ambient")
            play ambient "music/ambient_basement.ogg"
            $ arrivedby = "idle"
            "I slowly went down the concrete stairs and into the deep basement."
        elif arrivedby == "idle":
            "I stayed in the basement."
        label celia_basement_travel:
            $ phase = "adventure"
            menu:
                " "
                "Stay here" if True:
                    $ map_location = "Basement"
                    $ arrivedby = "idle"
                    jump celia_turn_order
                "Go back upstairs" if event_celia_basement_caught == 0:
                    $ map_location = "Office"
                    $ arrivedby = "special"
                    $ renpy.music.set_volume(0.2, channel="ambient")
                    play ambient "music/ambient_lights_hum_loop.ogg"
                    call celia_display_subroutine from _call_celia_display_subroutine_1
                    "I'd better move this bookshelf again."
                    "I grunted as I pushed the shelf back to where I found it."
                    jump celia_turn_order
                "Go back upstairs" if event_celia_basement_caught == 1:
                    jump event_celia_basement_whip
        return



label celia_search_subroutine:
    $ phase = "event"
    if map_location == "Room":
        if celia_bound == 1:
            "I scanned the room around me."
            "There's a ton of old office supplies, shelves, and drawers to go through."
            "...But I can't move."
            $ arrivedby = "special"
            jump celia_turn_order
        elif True:
            menu:
                " "
                "Search filing cabinets" if True:
                    if "item_battery_taser" not in inventory and "item_taser" in inventory:
                        "I rummaged through the cabinets."
                        "I flipped through piles of old paper."
                        "Ah hah!"
                        "A pile of batteries."
                        "God I hope these still have some charge."
                        "I grabbed the newest looking ones and slipped them into the taser."
                        "I clicked it closed and prayed as I held my finger over the button."
                        play sound "<from 0.0 to 0.5>music/sfx_taser.ogg"
                        "My prayers were answered with a crack and flash of light."
                        $ inventory.remove("item_taser")
                        $ inventory.append("item_battery_taser")
                        $ renpy.notify("Taser charged up!")
                        show screen inventory
                        pause(1.5)
                        hide screen inventory
                        p "Yes!!!"
                        $ arrivedby = "special"
                        jump celia_turn_order
                    elif True:
                        "I rummaged through all of the cabinets and paper."
                        "Almost nothing but paper..."
                        "A rusty stapler... batteries..."
                        "There doesn't seem to be anything else I can use in here."
                        $ arrivedby = "special"
                        jump celia_turn_order
                "Search drawers" if True:
                    if "item_office_key" not in inventory:
                        "I started at one end of the room and started going through everything."
                        "Every shelf and drawer was filled with dusty, discoloured paper."
                        "Wherever this place is... people haven't been here in a while."
                        "I kept shuffling through everything."
                        p "Oh..."
                        "At the back of a filing cabinet-"
                        "Something small and metal."
                        $ inventory.append("item_office_key")
                        $ renpy.notify("Office Key Added!")
                        show screen inventory
                        pause(1.5)
                        hide screen inventory
                        "A key!"
                        "I quickly put it in my pocket."
                        "This is bound to come in handy."
                        $ arrivedby = "special"
                        jump celia_turn_order
                    elif True:
                        "I carefully went through the drawers again."
                        "Ah!"
                        "A spider..."
                        "There's nothing I can use in here."
                        $ arrivedby = "special"
                        jump celia_turn_order
                "Search floor" if True:
                    if event_celia_harrison == 1 and event_celia_findpin == 0:
                        $ event_celia_findpin = 1
                        jump event_celia_findpin
                    "I checked the floor."
                    "Dirt, dust... and some creepy stains."
                    "Aside from some garbage, there's nothing here."
                    $ arrivedby = "special"
                    jump celia_turn_order

    if map_location == "Lounge":
        menu:
            " "
            "Search cabinets" if True:
                if event_celia_try_elevator == 1 and "item_celia_map" not in inventory:
                    "I checked a cabinet full of papers and blueprints."
                    "Wait... In the elevator, it said I'm on 'B1'."
                    "Hmm."
                    "I flipped through the floor plans and spotted what I was looking for."
                    "B1!"
                    $ inventory.append("item_celia_map")
                    $ renpy.notify("Basement Map Added!")
                    show screen inventory
                    pause(1.5)
                    hide screen inventory
                    "I can keep track of where I am with this."
                    $ arrivedby = "special"
                    jump celia_turn_order
                elif "item_celia_map" in inventory:
                    "I opened the cabinets again."
                    "I flipped through the papers."
                    "There's nothing else here."
                    $ arrivedby = "special"
                    jump celia_turn_order
                elif True:
                    "I checked through the cabinets."
                    "There's a ton of paper and documents in here."
                    "I think some of these are blueprints or floor plans..."
                    "But I don't know where I am."
                    $ arrivedby = "special"
                    jump celia_turn_order
            "Search the seats" if True:
                "I searched through the seats."
                "They're really dusty."
                "Some have rodent sized holes..."
                "I shuddered."
                "Definitely nothing useful."
                $ arrivedby = "special"
                jump celia_turn_order
            "Search drawers" if True:
                if item_basement_key_search == 0:
                    $ item_basement_key_search += 1
                    "I started going through the many drawers in the room."
                    "I can't believe there's so much paper here..."
                    "Weren't these important to somebody..?"
                    "Everybody just forgot them here."
                    $ stat_sanity -= 5
                    "As I opened another drawer, I realized I was shaking."
                    "I wasn't thinking about the papers."
                    "...Does anyone know that I'm missing?"
                    "Where am I..?"
                    "I shut my eyes tight and stopped myself from shedding any tears."
                    "I don't have time for that."
                    "I breathed deeply and searched more drawers."
                    "Nothing but forgotten documents..."
                    $ arrivedby = "special"
                    jump celia_turn_order
                elif True:
                    "I mechanically checked the drawers again."
                    "Paper, garbage, paper..."
                    "There's nothing here."
                    $ arrivedby = "special"
                    jump celia_turn_order

    if map_location == "Office":
        menu:
            " "
            "Search the desk" if True:
                if celia_brandy >= 6:
                    "I drunkenly rummaged through her desk, looking for the brandy."
                    p "Heh..."
                    p "...."
                    p "Wuh?"
                    window hide
                    show cg_celia_stream at truecenter with dissolve
                    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


                    $ renpy.notify("DLC: 'The Show Must Go On' unlocked!")
                    $ persistent.bluecounter = True
                    $ renpy.save_persistent()
                    if achievement.has("ach_blue") != True:
                        $ persistent.ach_blue = True
                        $ achievement.grant("ach_blue")
                        init:
                            $ achievement.register("ach_blue")
                            $ achievement.sync()
                            $ renpy.save_persistent()
                            if persistent.ach_blue == True and achievement.has("ach_blue") != True:
                                $ achievement.grant("ach_blue")
                                $ achievement.register("ach_blue")
                                $ achievement.sync()
                    pause
                    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


                    window auto
                    "What is this for..?"
                    "It's creepy."
                    "I don't like it..."
                    hide cg_celia_stream with dissolve
                    "I put it back where I found it."
                    $ arrivedby = "special"
                    jump celia_turn_order
                if event_office_search == 0:
                    $ event_office_search += 1
                    "This desk looks recently used."
                    "I checked the desk drawers."
                    "Papers, makeup, money."
                    "I briefly considered the cash..."
                    "But money isn't going to help me here."
                    "Oh wait..."
                    "At the back, there was a bottle of expensive looking brandy and an empty flask."
                    "I pulled the bottle out."
                    if event_celia_brandy_poisoned == 1:
                        "I'd better not touch it anymore."
                    menu:
                        " "
                        "Take a swig" if event_celia_brandy_poisoned == 0:
                            $ celia_brandy += 1
                            "I carefully opened the bottle."
                            "I tilted it back and swallowed a mouthful."
                            $ stat_sanity += 10
                            "I jerked back slightly as the burn spread down my throat."
                            "That stuff is strong..."
                            "It was somehow a little comforting though."
                            menu:
                                " "
                                "Drink more" if True:
                                    $ celia_brandy += 1
                                    "I took another few swigs."
                                    "The burn was strong now and the buzz of inebriation slowed my thoughts down."
                                    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


                                    $ stat_sanity -= 20
                                    p "Ugh..."
                                    "I shoved the bottle back where I found it."
                                    "That's enough of that..."
                                "Put it back" if True:
                                    "I placed the bottle where I found it."
                        "{image=menu_rat_poison}Use rat poison{space=60}" if "item_rat_poison" in inventory and not renpy.variant("small"):
                            label rat_poison_jumper_2:
                            "I pulled out the small packet of powder."
                            "... This might actually work."
                            $ inventory.remove("item_rat_poison")
                            $ renpy.notify("Brandy poisoned!")
                            $ event_celia_brandy_poisoned = 1
                            "I carefully opened the packet and poured the powder into the bottle."
                            "I let out the breath I'd been holding."
                            "Now all I can do is wait..."
                        "{image=menu_rat_poison_large}Use rat poison{space=60}" if "item_rat_poison" in inventory and renpy.variant("small"):
                            jump rat_poison_jumper_2
                        "Put it back" if True:
                            "I briefly imagined her drinking at this desk."
                            "The image was... kind of sad."
                            "I placed the bottle where I found it."
                    $ arrivedby = "special"
                    jump celia_turn_order
                elif True:
                    $ event_office_search += 1
                    "I rummaged through the desk again."
                    "The only interesting thing here is the booze."
                    if event_celia_brandy_poisoned == 1:
                        "I'd better not touch it anymore."
                    menu:
                        " "
                        "Take a swig" if event_celia_brandy_poisoned == 0:
                            $ celia_brandy += 1
                            "I tilted it back and swallowed a mouthful."
                            if celia_brandy == 1:
                                $ stat_sanity += 10
                            elif True:
                                if celia_brandy == 2:
                                    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


                                    $ stat_sanity -= 20
                                elif celia_brandy == 3:
                                    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


                                    $ stat_sanity -= 20
                                elif celia_brandy == 4:
                                    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


                                    $ stat_sanity -= 20
                                elif celia_brandy == 5:
                                    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


                                    $ stat_sanity -= 20
                                elif celia_brandy == 6:
                                    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


                                    $ stat_sanity -= 20
                                elif True:
                                    $ stat_sanity -= 20
                            "Ugh..."
                            "Burns."
                        "{image=menu_rat_poison}Use rat poison{space=60}" if "item_rat_poison" in inventory and not renpy.variant("small"):
                            label rat_poison_jumper_1:
                            "I pulled out the small packet of powder."
                            "... This might actually work."
                            $ inventory.remove("item_rat_poison")
                            $ renpy.notify("Brandy poisoned!")
                            $ event_celia_brandy_poisoned = 1
                            "I carefully opened the packet and poured the powder into the bottle."
                            "I let out the breath I'd been holding."
                            "Now all I can do is wait..."
                        "{image=menu_rat_poison_large}Use rat poison{space=60}" if "item_rat_poison" in inventory and renpy.variant("small"):
                            jump rat_poison_jumper_1
                        "Put it back" if True:
                            "I placed the bottle where I found it."
                    $ arrivedby = "special"
                    jump celia_turn_order
            "Search the storage" if True:
                if ("item_taser" in inventory) or ("item_battery_taser" in inventory):
                    "I opened the various office drawers."
                    "There's hardly anything in here."
                    "Nothing I can use."
                    $ arrivedby = "special"
                    jump celia_turn_order
                elif True:
                    "I started going through the office storage."
                    "A lot of empty drawers..."
                    "So far, nothing I can actually use."
                    "Woah!"
                    "In a drawer, by itself, there was a black device."
                    $ inventory.append("item_taser")
                    $ renpy.notify("Taser Added!")
                    show screen inventory
                    pause(1.5)
                    hide screen inventory
                    "This is definitely a taser."
                    "It's the kind you have to touch someone with."
                    "I tentatively pressed the button."
                    "... Nothing."
                    "I checked over it and popped the back open."
                    "No batteries..."
                    "I huffed in annoyance."
                    "Well I'm still keeping it."
                    $ arrivedby = "special"
                    jump celia_turn_order
            "Search the floor" if True:
                if event_celia_discover_basement == 0:
                    $ event_celia_discover_basement = 1
                    "I checked around the office floor."
                    "It's actually pretty clean in here."
                    "There's pretty much nothing on the flo-"
                    "Huh?"
                    "There's something going up the wall behind the bookcase..."
                    "I grabbed the bookcase and shoved it to the side."
                    "A door!"
                    "I looked down."
                    "... With a keypad."
                    "I could feel my heartrate increasing."
                    "If she took this much care to hide this..."
                    "It must be the way out."
                    $ arrivedby = "special"
                    jump celia_turn_order
                elif True:
                    "I glanced around the floor again."
                    "There's nothing here."
                    $ arrivedby = "special"
                    jump celia_turn_order

    if map_location == "Elevator":
        if "item_note" in inventory:
            "I searched around the elevator."
            "There's really not much in here..."
            $ arrivedby = "special"
            jump celia_turn_order
        elif True:
            "I checked all over the small area."
            "Not much to see in here..."
            "I closely examined the elevator's button panel."
            "It has one of those little holes..."
            if "item_pin" not in inventory:
                $ arrivedby = "special"
                jump celia_turn_order
            "Wait!"
            show screen inventory
            pause(1.5)
            hide screen inventory
            "I grabbed the pin from my pocket."
            "Come on..."
            "I pressed the pin in and felt a pop."
            "The front panel of the buttons came right off."
            "Before I could look at the wiring, I was distracted by a piece of paper."
            "What the hell?"
            "I carefully pulled out and unfolded the paper."
            window hide
            show cg_celia_note at truecenter with dissolve
            pause
            window auto
            "\"0247\""
            "Is this blood!?"
            "I stared at the paper."
            hide cg_celia_note with dissolve
            if event_celia_discover_basement == 0:
                "I have no idea what this means."
            elif True:
                "Maybe I can use this..."
            $ inventory.append("item_note")
            $ renpy.notify("Items Added!")
            show screen inventory
            pause(1.5)
            hide screen inventory
            "I folded it up and put it in my pocket."
            "Then I looked back at the buttons panel."
            "... I don't think I can mess with this either."
            "I carefully put the faceplate back in place and sighed."
            "So much for that."
            $ arrivedby = "special"
            jump celia_turn_order
    if map_location == "Basement":
        menu:
            " "
            "Search shelves" if True:
                "I looked over the shelves at the back of the room."
                "Light bulbs... cans of paint..."
                "There's some repair supplies..."
                "I don't think I can use any of this stuff though."
                $ arrivedby = "special"
                jump celia_turn_order
            "Search floor" if True:
                if "item_wire" not in inventory:
                    "I started to look around the disturbing room."
                    "There's so many stains..."
                    "I shook my head."
                    "I need to concentrate."
                    "There was a lot of junk around, but it was hard to imagine being able to use any of it."
                    "I nearly gave up before a small glint caught my eye."
                    "I went back over to a pile of junk in a corner."
                    "... It's a spool of wire."
                    "I bent down to pick it up."
                    "I pulled a bit off the roll."
                    "This is really strong..."
                    "And sharp."
                    "I think I might be able to use this."
                    $ inventory.append("item_wire")
                    $ renpy.notify("Wire Added!")
                    show screen inventory
                    pause(1.5)
                    hide screen inventory
                    "I shoved it into my pocket."
                    $ arrivedby = "special"
                    jump celia_turn_order
                elif True:
                    "I rummaged through the junk in the room again."
                    "There doesn't seem to be anything else I can use."
                    $ arrivedby = "special"
                    jump celia_turn_order
            "Search walls" if True:
                "I looked over the walls."
                "I can't seem to find another door."
                "Is there really no way out of here?"
                $ arrivedby = "special"
                jump celia_turn_order

    if map_location == "Break Room":
        menu:
            " "
            "Search the cabinets" if True:
                if "item_rat_poison" not in inventory and event_celia_brandy_poisoned != 1:
                    "I opened the cabinets."
                    "Ugh... paper plates and plastic cutlery."
                    "And a lot of garbage."
                    "I stopped at the cabinet under the sink."
                    "Various cleaners..."
                    "Wait a minute."
                    "I double checked a box in the back."
                    "... Rat poison."
                    "I thought hard for a moment."
                    $ inventory.append("item_rat_poison")
                    $ renpy.notify("Rat Poison Added!")
                    show screen inventory
                    pause(1.5)
                    hide screen inventory
                    "I pulled out a packet of powder."
                    "I might be able to use this..."
                    $ arrivedby = "special"
                    jump celia_turn_order
                elif True:
                    "I checked through the cabinets again."
                    "There's a lot of garbage."
                    "But I don't think I can use any of it."
                    $ arrivedby = "special"
                    jump celia_turn_order
            "Search the fridge" if True:
                "I opened the fridge."
                if meme_mode:
                    "Nothing but a dead lizard."
                elif True:
                    "... And saw nothing."
                "I guess it was too much to expect any food to be left here."
                $ arrivedby = "special"
                jump celia_turn_order
            "Search the vending machine" if True:
                if event_celia_soda_get == 0:
                    "I tapped at the screen on the machine."
                    "It's not powered."
                    "I checked around the back, but I couldn't find a cord for it."
                    "I sighed in frustration."
                    "I guess I could... try reaching up in there."
                    menu:
                        " "
                        "Reach inside" if True:
                            "I carefully put my arm inside the old machine."
                            "I can't... feel anything."
                            "I strained to reach further."
                            "I started moving faster."
                            "Something about this is making me nervous..."
                            "Come on..."
                            "I couldn't reach high enough..."
                            "There's... Oh?"
                            "I felt the distinct shape of a can in the bottom corner of the machine."
                            "Jackpot!"
                            $ event_celia_soda_get = 1
                            $ inventory.append("item_soda")
                            $ renpy.notify("Soda Added!")
                            show screen inventory
                            pause(1.5)
                            hide screen inventory
                            "I pulled out my prize."
                            "Diet ginger ale..."
                            "Well... beggars can't be choosers I guess."
                        "Leave it alone" if True:
                            "I don't really need to mess with this."
                            "There's probably nothing in it anyway."
                    $ arrivedby = "special"
                    jump celia_turn_order
                elif True:
                    "I searched around the vending machine again."
                    if meme_mode:
                        "Can't... reach anything..."
                        "My hand grabbed something warm and soft."
                        p "Huh?"
                        "I pulled it out cautiously."
                        "A mouse stared back at me."
                        p "Ahh!"
                        "I dropped it and it ran away immediately."
                        p "Uh... sorry, I guess."
                    elif True:
                        "Nothing else in here."
                    $ arrivedby = "special"
                    jump celia_turn_order



label celia_desk_struggle:
    $ phase = "event"
    if celia_bound == 1:
        if celia_desk_escape_attempt == 0:
            $ celia_desk_escape_attempt += 1
            play sound "music/sfx_chain.ogg"
            "I pulled at the handcuffs."
            "The long chains each led to a desk leg and kept me painfully bent over the table."
            "I tried to lift the table."
            p "Hrrggg!"
            "Something's stuck..."
            "I tried to look below, but the cuffs kept me in place."
            "... I think the desk is bolted to the floor or something."
            jump celia_turn_order
        if celia_desk_escape_attempt == 1:
            $ celia_desk_escape_attempt += 1
            play sound "music/sfx_chain.ogg"
            "I pulled harder."
            $ stat_sanity -= 3
            "The metal cuffs were digging into my wrists."
            "I strained painfully against the cuffs."
            $ stat_sanity -= 3
            "Panic drove me until they cut into the skin."
            "The pain became too much, and I dropped back down."
            "I think I heard a crack."
            jump celia_turn_order
        if celia_desk_escape_attempt == 2:
            $ celia_desk_escape_attempt += 1
            $ celia_bound = 0
            "I took in several deep breaths."
            "This is going to hurt."
            play sound "music/sfx_chain.ogg"
            "I wrenched against the cuffs again."
            $ stat_sanity -= 5
            $ stat_health -= 3
            p "Auuuggh!"
            "The cuffs cut deep into my skin, pulling it back."
            "I put in all of my strength."
            scene black
            play sound "music/sfx_crash_wood.ogg"
            "I heard a loud crack and fell backwards." with vpunch
            "The desk fell backwards on top of me."
            scene bg_celia_room
            "I scrambled to get out from it and see what I'd done."
            "The cuffs fell to my sides as I looked at the damage."
            "The feet of the desk were indeed bolted to the floor."
            "And they still were."
            "The desk itself snapped off from the legs."
            "I breathed a sigh of relief that turned into a hiss of pain."
            "I really mangled my wrists..."
            "But now at least I'm free."
            jump celia_turn_order
label event_celia_room_key_attempt:
    $ phase = "event"
    $ event_celia_room_key_attempt = 1
    "I tried the key hole."
    "... I can't fit the key in at all."
    "Ugh... this key must be for something else."
    jump celia_turn_nostats
label event_celia_room_door_locked:
    $ phase = "event"
    "I tried to open the door."
    "The handle wouldn't turn."
    "It clacked as I tried pulling it harder, hoping maybe it was just stuck."
    "... It's definitely locked."
    "I examined the handle."
    "It has one of those tiny holes in it to unlock it in emergencies..."
    "... But I have nothing small enough to fit in there."
    "I looked through the blurry glass, trying to see outside my prison."
    "Then I tapped the glass."
    "I looked back behind me at the metal cabinets."
    menu:
        "... I could probably break this glass."
        "Smash the window" if True:
            $ map_location = "Lounge"
            $ arrivedby = "new"
            $ celia_room_window_smashed = 1
            "I grabbed the smallest metal filing cabinet."
            p "Urgh..."
            "It's still heavy."
            "I stood away from the window, readying myself."
            play sound "music/sfx_glass.ogg"
            show bg_celia_room_broken
            "Then I ran at the window and hurled the cabinet at the glass." with vpunch
            "It was jarring to suddenly hear something so loud."
            "Once I gathered myself, I checked the door."
            "Sure enough, the glass was completely shattered."
            "I carefully peered through the open window into the hallway beyond."
            "This is definitely some kind of abandonded office building."
            "I reached through the open hole to the handle on the other side."
            "I sighed with relief when I felt a simple turning lock."
            "I flipped it and opened the door with a soft creak."
            "Then I walked into the hallway."
            jump celia_turn_order
        "Leave the window alone" if True:
            "I'd better not."
            "She's going to come back eventually..."
            jump celia_turn_nostats

label celia_event_harrison:
    $ phase = "event"
    if map_location != "Room":
        jump event_celia_first_night_caught
    $ total_hours += 4
    $ hours += 4
    if celia_bound == 1:
        if arrivedby != "sleep":
            play sound "<from 0.0 to 3.0>music/sfx_heels.ogg" fadein 2.0
            "The faint hum of the lights was interrupted by the light tapping of someone approaching the door."
            "My heart rate jumped."
            "A second later, she entered the room."
        elif True:
            $ sleep = 0
            call celia_display_subroutine from _call_celia_display_subroutine_2
            play sound "music/sfx_door_open.ogg"
            "The sound of a door opening startled me awake."
        if celia_office_locked == 0 or celia_brandy >= 2:
            play music "music/celias_theme.ogg"
            jump event_celia_stripsearch
        show celia behind sprite_celia_desk with dissolve:
            zoom 0.9
            xalign 0.5
            yoffset -50
        play music "music/celias_theme.ogg" fadein 1.0
        c "There you are~"
        c relaxed "Did you have a comfortable night?"
        "I honestly had no idea what time it was."
        "I kept my head low."
        c serious "Hm."
        c normal "Well, now we've actually got plenty of time to break you in."
        c semiserious "I have a special job for you that I've been waiting for."
        "She produced a black bag and another set of handcuffs."
        "Something about my expression must have caught her eye, because she let out a light laugh."
        c normal "Don't worry, I'm not going to {i}kill{/i} you."
        c relaxed "Not if you behave, anyway."
        c semiserious "We're just going to play a little role playing game."

    if celia_bound == 0:

        if celia_room_window_smashed == 1:
            label event_celia_brokenwindow:
            if arrivedby != "sleep":
                "The faint hum of the lights was interrupted by the light tapping of someone approaching the door."
                "My heart rate jumped."
                play music "<from 35.5>music/celias_theme.ogg" fadein 1.0
                c surpangry "... What the hell!?"
            elif True:
                $ sleep = 0
                call celia_display_subroutine from _call_celia_display_subroutine_3
                play music "<from 35.5>music/celias_theme.ogg" fadein 1.0
                c surpangry "... What the hell!?"
                "I was startled awake."
            show celia angry:
                zoom 0.9
                alpha 0.0
                xalign 0.25
                yoffset -50
                easein 0.3 xalign 0.5 alpha 1.0
            "She flew around the corner into the room, fuming."
            c "What did you do to the door!?"
            show celia gunangry
            "Before I could say anything, I was staring down the barrel of her gun."
            c "So..."
            "I tried to step back as she approached."
            c gun "You're a shit disturber, huh?"
            "She moved quickly with smooth strides, closing the distance between us."
            "With the gun pointed directly at my face, I was frozen up."
            play sound "music/sfx_gunshot.ogg"
            $ stat_sanity -= 10
            scene white with vpunch
            pause(1.0)
            play sound "music/sfx_ears_ring.ogg"
            show bg_celia_room:
                yoffset -360
            with dissolve
            "I had fallen to my knees in shock."
            "Am I alive?"
            "She didn't shoot me..?"
            "I had just barely begun to realize that she took the shot right beside my head to stun me."
            $ stat_sanity -= 5
            $ stat_health -= 5
            play sound "music/sfx_taser.ogg"
            "My body seized up as my back was tased." with largeshake
            scene black with vpunch
            "I fell to the floor."
            "I could just barely hear her voice."
            c angry "... motherfuckers."
            pause(1.0)
            c surpangry "They said you were {i}docile{/i}."
            pause(1.0)
            c angry "... sell ME a defective..."
            if meme_mode:
                c "I'm gonna leave them SUCH a shit review."
            "I groaned as I felt the floor move under me."
            c annoyed "Still with me?"
            $ stat_health -= 5
            scene cg_celia_glass_1
            $ persistent.cgs_celia.add("cg_celia_glass")
            $ renpy.save_persistent()
            play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
            "A sharp kick to the side brought me coughing back into full consciousness." with hpunch
            c annoyed "I'm not done with you."
            c bored "You might be garbage... but I'm gonna get my money's worth one way or another."
            "Something pressed my head to the floor." with vpunch
            $ stat_health -= 3
            play sound "music/sfx_glass_grind.ogg"
            "The broken glass from the door dug into my face."
            c smile "You're going to {i}eat{/i} your mistake."
            p "W... what?"
            "I realized it was her foot on my head, as it pushed again." with vpunch
            c annoyed "You heard me."
            "The glass!?"
            p "I can't..."
            "She let out an exasperated sigh."
            c smile "You can."
            c sadistic "And you will."
            $ stat_sanity -= 5
            $ stat_health -= 5
            play sound "music/sfx_taser.ogg"
            "The taser jabbed into the back of my neck again." with largeshake
            scene black with eyedissolve
            "I couldn't feel anything for a moment."
            "I couldn't think straight."
            $ stat_health -= 3
            "A sharp pain in my throat brought me back once more."
            $ stat_health -= 3
            play sound "music/sfx_glass_grind.ogg"
            "I slowly became more aware of shards of glass being shoved into my mouth." with vpunch
            scene cg_celia_glass_1 with eyedissolve_reverse
            "Adrenaline surged and I tried to scream."
            $ stat_health -= 10
            "The motion just constricted my throat around the shards."
            $ stat_health -= 3
            scene cg_celia_glass_2 with dissolve
            "Blood sprayed from my mouth as I tried to spit out the glass."
            "I couldn't move my arms..."
            "Her hand shoved more glass at my face."
            "I jerked away and kept trying to cough or spit it out." with vpunch
            $ stat_health -= 10
            "More blood."
            c smile "You're making a mess~"
            "I tried to beg, but everything just caused more damage... more blood."
            "The pain was too much..."
            "Nothing in my body seemed to work from the shock."
            "I began to choke on blood and shards."
            c normal "Aww... having trouble breathing?"
            "Every time I tried to take a breath in, more blood and pain filled my chest."
            c smile "I have to admit... you were pretty cute though."
            scene black with eyedissolve
            stop music fadeout 3.0
            stop ambient fadeout 3.0
            "I can't breathe..."
            "The pain finally began to subside as I felt my body twitching."
            "I never heard her walk away."
            $ quick_menu = False
            window hide
            hide screen effect_health
            hide screen effect_ice
            hide screen status
            $ persistent.endings_celia.add("You ate your mistake")
            $ persistent.deathcounter += 1
            $ renpy.save_persistent()
            call achievement_checker from _call_achievement_checker_15
            play music "<from 0.3>music/you_died.ogg"
            scene bg_endslate with blooddissolve
            show screen bg_endslate_text("You Died","You ate your mistake")
            $ renpy.pause(hard=True)

        if arrivedby != "sleep":
            "The faint hum of the lights was interrupted by the light tapping of someone approaching the door."
            "My heart rate jumped."
            show celia surprised with dissolve:
                zoom 0.9
                xalign 0.5
                yoffset -50
            play music "<from 35.5>music/celias_theme.ogg" fadein 1.0
            "A second later, she entered the room."
        elif True:
            $ sleep = 0
            call celia_display_subroutine from _call_celia_display_subroutine_5
            play sound "music/sfx_door_open.ogg"
            "The sound of a door opening startled me awake."
            show celia surprised with dissolve:
                zoom 0.9
                xalign 0.5
                yoffset -50
            play music "<from 35.5>music/celias_theme.ogg" fadein 1.0
            "I jolted awake at the sight of Celia entering the room."
        "She stopped dead, seeing the overturned desk."
        show celia serious
        "She quickly focused on me and my obvious lack of restraints."
        menu:
            "Her stance instantly changed and she grabbed something on her hip."
            "Fight her" if True:
                $ event_celia_tased = 1
                $ celia_love -= 1
                show celia angry
                "This is my chance!"
                "I lunged at her, swinging the long chain still attached to my wrist."
                $ stat_health -= 5
                $ stat_sanity -= 10
                "Then I fell to the ground screaming." with largeshake
                "Explosive pain was radiating from two needles lodged in my torso."
                if pronoun == "he":
                    c question "Nice try, rat."
                elif True:
                    c question "Nice try, little mouse."
                "She moved behind my writhing form and replaced my cuffs with a smaller set."
                c serious "If you think you can pull one over me that easily..."
                c "Well..."
                "She shoved me lightly with her foot."
                c semiserious "I suppose you'll get the idea soon enough."
                c "You should hope you're a fast learner."
                "She straightened her clothing, satisfied with my defeated state."
                c normal "Now, we're going to play a little role playing game."
                c semiserious "Let's see how fast you can catch on."
            "Surrender" if True:
                show celia surprised
                p "W-wait!"
                p "I'm sorry!"
                "I crouched low and put my hands on the floor."
                show celia serious
                "She narrowed her eyes."
                p "I just... it was so uncomfortable."
                p "I'm not trying to pull anything!"
                "She glanced at the desk again."
                c "Lie down on the floor."
                c "Face down."
                "I complied quickly."
                "Whatever she has, I don't need to find out."
                "She walked over slowly and replaced my cuffs with a smaller set."
                c "Tch."
                "I looked up, realizing her annoyance seemed to be directed at the desk, rather than me."
                c mocking "Cheap trash furniture..."
                c serious "Should have expected that."
                "She turned back to me."
                c semiserious "I have a special job for you that I've been waiting for."
                "She produced a black bag and another set of handcuffs."
                "Something about my expression must have caught her eye, because she let out a light laugh."
                c "Don't worry, I'm not going to {i}kill{/i} you."
                c serious "Not if you behave, anyway."
                c normal "We're just going to play a little role playing game."
    $ celia_bound = 0
    $ arrivedby = "idle"
    $ event_celia_harrison = 1
    show cg_burlap_room
    show cg_burlap_over
    hide celia
    "She walked behind me and placed the bag over my head."
    menu:
        " "
        "\"What are you doing!?\"" if True:
            $ celia_love -= 1
            c annoyed "Ugh. Pay attention."
            c "I just told you what we're doing."
        "\"I'm not playing anything.\"" if True:
            $ celia_love -= 1
            $ stat_sanity -= 5
            play sound "music/sfx_impact_thud.ogg"
            "My head was instantly slammed into the table." with vpunch
            p "Augh..."
            if pronoun == "he":
                c annoyed "Maybe you're used to being in charge."
                c "Or maybe you're just stupid."
                c "Either way, I think you should put some thought into the position you're in."
            elif True:
                c annoyed "You should really consider your position before bothering to speak."
        "\"Please, I don't want to do this...\"" if True:
            $ celia_love += 1
            c "Ohh~?"
            c "You're already begging?"
            "I felt her hand touch my shoulder briefly."
            c smile "I think you're going to be good at this."
        "\"This is a little weird, but kinda hot...\"" if meme_mode:
            $ celia_love += 1
            play sound "music/sfx_impact_thud.ogg"
            c annoyed "Shut up!" with vpunch
        "Stay silent" if True:
            pass
    "I felt the drawstring of the bag tighten around my head."
    "It was scratchy, but still loose enough to breathe through the bag."
    if celia_desk_escape_attempt != 3:
        "I felt the click of a second pair of handcuffs around one of my hands."
        "I felt a surge of adrenaline."
        "She's going to uncuff me from the desk..."
        menu:
            "This could be my chance..."
            "Fight back" if True:
                $ celia_love -= 2
                "I waited as she started to remove the cuff from my left hand."
                "As soon as I felt the metal drop away, I lunged in her direction."
                "She yelled angrily as my elbow connected with her." with vpunch
                "I frantically tried to land another hit or grab for her, but she was already out of reach."
                "My right hand was still cuffed to the desk."
                "I stretched out, trying to grasp anything."
                "She was completely silent."
                "What is she waiting fo-"
                $ stat_sanity -= 10
                $ stat_health -= 5
                $ event_celia_tased = 1
                play sound "music/sfx_taser.ogg"
                "I clenched my teeth as electric agony shot through my body from my back." with largeshake
                "I collapsed awkwardly against the desk."
                "I couldn't do anything but groan in pain as she yanked my free arm and cuffed my hands behind my back."
                "Then I heard her voice right beside my head."
                c smile "You can squirm all you want."
                c sadistic "I'll just enjoy it more when you start screaming."
                "She grabbed me roughly from the desk and shoved me down to my knees on the floor."
            "Stay calm" if True:
                "I wasn't really in a good position to fight back."
                "I can't see at all."
                "The thought of being moved from my uncomfortable position at the desk was enough to make me compliant."
                "I felt her open the cuff on my left hand."
                "I let my arm go limp as the metal dropped away."
                "I heard her make a small sound of approval before she closed the second pair of cuffs, binding my hands together behind my back."
                "It was a relief to finally be out of that position."
                "She grabbed my shoulders and guided me away from the desk."
                "I couldn't see anything, so I stepped forward timidly."
                c smile "On your knees."
                "There wasn't much point in arguing."
                "I crouched down and lowered myself to my knees as instructed."
    $ inventory.remove("item_shackles")
    c normal "Now..."
    play sound "music/sfx_chair_squeak.ogg"
    "I heard the creak of the office chair I previously occupied."
    c smile "It's time for some fun."
    if player_name.upper() == "EDWARD":
        c normal "Your name is-"
        c surprised "Oh wait..."
        c smile "Isn't it already Edward?"
        c normal "Well, looks like you'll have an easy time slipping into the role."
    elif True:
        c normal "Your name is 'Edward'."
    c annoyed "You steal ideas and have the composure of a weasel."
    play sound "<from 0.5>music/sfx_chair_squeak.ogg"
    "I heard the chair creak again and her voice was closer."
    c "You're a bottom-feeding parasite who is incapable of original thought."
    "Her voice had taken on a much sharper tone."
    c smile "Isn't that right?"
    menu:
        " "
        "\"Uh... Yes ma'am?\"" if True:
            $ celia_love += 1
            c "That's right~"
            play sound "music/sfx_impact_thud.ogg"
            "I felt her heel on my back for an instant before being shoved face-first to the ground." with vpunch
        "\"I'm not playing along!\"" if True:
            $ celia_love -= 1
            $ stat_sanity -= 5
            $ stat_health -= 3
            play sound "music/sfx_impact_thud.ogg"
            "Something hard slammed into the side of my head, nearly knocking me to the ground." with vpunch
            c annoyed "I'm getting bored with your attitude, {i}Edward{/i}."
            "I yelped as I was kicked forward, falling face first onto the floor."
        "Refuse to answer" if True:
            $ celia_love -= 1
            c annoyed "..."
            play sound "music/sfx_impact_thud.ogg"
            "I felt her heel on my back for an instant before being shoved face-first to the ground." with vpunch
            c sadistic "First time in your life, you don't have something to say, Edward?"
    "I groaned against the scratchy black bag as I felt her walk to my side and place a heel on my back."
    c angry "You fucking {i}vermin{/i}."
    "She started pressing the sharp heel of the shoe into my flesh."
    c sadistic "You think you can screw with me?"
    c annoyed "You..."
    "I writhed as she ground the heel down."
    c smile "Are worthless."
    "I couldn't help but whine in pain."
    "The sound seemed to affect her, since the weight of her foot left my back."
    "I laid still as she paced quickly next to me."
    c annoyed "..."
    c "Get up."
    "I got up off the floor onto my knees."
    $ stat_sanity -= 5
    $ stat_health -= 3
    play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
    "Two angry taps of her shoes approaching were all the warning I had before being kicked ruthlessly in the side." with hpunch
    "I couldn't breathe."
    "I curled on my side, gasping, trying to get my lungs to work."
    c sadistic "I'll {i}crush{/i} you."
    $ stat_sanity -= 5
    $ stat_health -= 3
    play sound "<from 5.0 to 6.0>music/sfx_impact.ogg"
    "I barely got a single gasp in before a second kick stabbed into my stomach." with hpunch
    "I clamped my mouth shut to keep the contents of my stomach down."
    c annoyed "Everyone will see you..."
    c smile "Broken..."
    c sadistic "And I'll {i}laugh{/i}."
    "When I finally managed to wheeze, I immediately began coughing."
    "I laid on the ground, coughing and suppressing pained whimpers."
    "I couldn't tell where she was."
    "I listened and began to notice her breathing."
    "She was practically panting."
    menu:
        " "
        "Stay quiet" if True:
            "I focused on breathing and stayed as still as possible."
            "I didn't want to make her any more worked up."
            "To my relief, I heard her taking in longer breaths."
            "I heard her sit in the chair."
            c smile "... You do look better like that."
            if sexcontent != "no":
                jump event_celia_harrison_masturbation
            elif True:
                "She laughed softly."
                jump event_celia_harrison_end
        "Apologize" if True:
            $ celia_love += 1
            p "I'm sorry..."
            "Her breathing became quiet."
            "I might as well play along."
            p "I- I am worthless."
            "My voice was shaking with uncertainty."
            "I hoped this is what she wanted."
            "She was silent for a long moment."
            "Then I heard her sit down in the chair again."
            c smile "Crawl for me."
            "There's no point in salvaging pride now."
            "I barely held in a whimper as I scrambled to get back onto my knees from the floor."
            "I struggled for balance with my hands cuffed together."
            "I awkwardly crawled towards the sound of her voice."
            if sexcontent != "no":
                jump event_celia_harrison_masturbation
            elif True:
                "She laughed softly."
                jump event_celia_harrison_end
        "\"You need to calm down.\"" if meme_mode == False:
            label celia_calm_down:
            $ stat_sanity -= 5
            $ stat_health -= 3
            $ celia_love -= 2
            play sound "music/sfx_impact_thud.ogg"
            "I barely finished my sentence before being kicked in the chest." with hpunch
            c angry "You little BITCH!"
            "I felt her hand grasp my head through the bag."
            p "Wai-"
            play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
            "She slammed my face into the floor." with vpunch
            $ stat_sanity -= 5
            $ stat_health -= 3
            play sound "music/sfx_impact_thud.ogg"
            "I screamed as she lifted it and slammed it down again." with vpunch
            "I heard a crack."
            "The warm coppery liquid on my lips was enough to tell me that my nose was probably broken."
            "I groaned dizzily and slumped onto my side."
            if pronoun == "he":
                c smile "You're not the first rat who couldn't behave."
            elif True:
                c smile "You're not the first mouse who couldn't behave."
            c "I can afford a replacement."
            c annoyed "You-"
            "She shoved my head painfully with her foot."
            c smile "Are disposable."
            c normal "... So you'd better keep that in mind."
            "I reeled as she straighted herself up."
            jump event_celia_harrison_end
        "\"Would you chill? WOULD YOU CHILL!?\"" if meme_mode:
            jump celia_calm_down
    label event_celia_harrison_masturbation:
        "I flinched as I felt her shoe on my head through the bag."
        "But she didn't put as much pressure on as before."
        "She seemed to be just resting it there."
        "I didn't dare move, so I just laid there and tried to ignore my throbbing ribs."
        "I felt her foot move a bit and heard some soft shuffling."
        "I tried to stay calm instead of imagining what she would do next."
        "My fear slowly turned to curiosity as I heard nothing from her but breathing."
        "What..?"
        "I kept listening, realizing that her breathing was getting a bit louder."
        "Then I noticed the weight of her foot was shifting... rhythmically."
        "Oh my god... is she..."
        play sound "music/sfx_chair_squeak.ogg"
        c horny "Hnnn~"
        "I instantly froze up."
        "D-did she just moan!?"
        "My mind went in several directions at once before settling on just staying still."
        "At least she's not kicking me..."
        play sound "<from 0.5>music/sfx_chair_squeak.ogg"
        "The pressure of her foot increased, lightly grinding my face into the bag."
        "I accidentally let out a muffled whimper."
        "She responded with a harder press and a more audible moan."
        play sound "<from 0.5>music/sfx_chair_squeak.ogg"
        "Her foot jerked against my head and I heard her breathing slow and deepen."
        "I could feel my own face flushing as she shoved me a final time, breathing out a cry through clenched teeth." with vpunch
        play sound "music/sfx_chair_squeak.ogg"
        "I jerked in surprise as the chair suddenly creaked and she got up."
        "She took only a moment to catch her breath and pat her clothing."
        jump event_celia_harrison_end
    label event_celia_harrison_end:
        if celia_love >= 3:
            c normal "... Very good."
            c smile "You're a natural~"
        elif celia_love < 0:
            c bored "..."
            c "Good enough for now."
        elif True:
            c smile "... Good."
            c normal "You did well."
        "I heard her pacing for a few moments."
        scene bg_celia_room
        show celia serious:
            zoom 0.9
            xalign 0.5
            yoffset -50
        with vpunch
        "She walked back to me and yanked my bag off abruptly."
        "I kept still as she stared at me sharply."
        "She seemed to be mulling over some decision."
        show celia relaxed
        "Suddenly, she stood up straighter and walked to the door."
        c semiserious "I think we're done here, for now."
        "Her gaze dropped to my handcuffs and she chewed her lip for a moment."
        "I tried to appear as non-threatening as possible."
        if celia_love > 2:
            c mocking "... I guess I'll take those."
            c semiserious "Stay still."
            "I watched her produce a tiny key and bend down."
            "I stayed perfectly still."
            play sound "<from 1.0>music/sfx_chain.ogg"
            "She popped open the metal restraints and took them."
            c serious "Don't make me regret that."
        elif True:
            c serious "... I guess I'll take those."
            play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
            "She roughly shoved me down and grabbed the cuffs." with vpunch
            c "Stay still."
            play sound "<from 1.0>music/sfx_chain.ogg"
            "She popped open the metal restraints and took them."
            c mocking "I can't have you choking yourself out with them."
            c serious "Do NOT make me regret that."
        stop music fadeout 1.0
        hide celia with dissolve
        "Without any other words, she headed to the door and slipped out."
        play sound "music/sfx_unlock.ogg"
        "I heard the click of a lock and her quick steps fading away."
        "I sat up, wincing."
        "Well... I can sort of move around at least now."
        "I rubbed the red marks on my wrists and thought about what to do next."
        $ arrivedby = "special"
        jump celia_turn_nostats

label event_celia_spacer:
    $ phase = "event"
    $ event_celia_spacer = 1
    if map_location != "Room":
        jump event_celia_first_night_caught
    if event_celia_set_trap == 1:
        jump event_celia_wire_trap_end
    if map_location == "Room" and event_celia_brandy_poisoned == 1:
        jump event_celia_brandy_poisoned_death
    if celia_room_window_smashed == 1:
        jump event_celia_brokenwindow
    $ total_hours += 4
    $ hours += 4
    if arrivedby != "sleep":
        play sound "music/sfx_door_open.ogg"
        "I was startled by the sound of the door opening."
        play music "music/celias_theme.ogg"
        show celia serious with dissolve:
            zoom 0.9
            xalign 0.5
            yoffset -50
        "It was her again... and she didn't look happy."
    elif True:
        $ sleep = 0
        call celia_display_subroutine from _call_celia_display_subroutine_6
        play sound "music/sfx_door_open.ogg"
        "I was startled awake by the sound of the door opening."
        play music "music/celias_theme.ogg"
        show celia serious with dissolve:
            zoom 0.9
            xalign 0.5
            yoffset -50
        "It was her again... and she didn't look happy."
    $ event_celia_room_door_locked = 1
    if celia_office_locked == 0 or celia_brandy >= 2:
        jump event_celia_stripsearch
    "I instinctively moved back into the corner of the room."
    if celia_love >= 0:
        stop music fadeout 1.0
        c "Relax."
        c bored "You're just keeping me company today."
    elif True:
        show celia relaxed
        "She looked me over and seemed to relax a little."
        p "Wha-"
        hide celia with dissolve
        "She turned back to the door."
        p "Wait!"
        "My head and stomach were both aching."
        p "I'm... hungry..."
        show celia serious with dissolve:
            zoom 0.9
            xalign 0.5
            yoffset -50
        c "..."
        c mocking "I don't really think you've earned anything yet."
        c semiserious "Maybe next time I'll bring you something~"
        stop music fadeout 1.0
        hide celia with dissolve
        "Before I could protest, she turned and walked away."
        "The door clicked behind her and I slumped against the wall."
        $ stat_sanity -= 10
        "Fuck..."
        "I thought I could hear her outside the room for the next couple hours."
        "But after that, only the awful hum from the lights remained."
        $ arrivedby = "special"
        jump celia_turn_nostats
    c "Come on."
    "She turned and motioned for me to follow."
    c serious "Now!"
    hide celia with dissolve
    "She disappeared outside the door."
    "I tentatively stepped outside."
    $ map_location = "Lounge"
    call celia_display_subroutine from _call_celia_display_subroutine_7
    if event_celia_enter_lounge == 1:
        "I gulped and made sure to try and pretend I hadn't seen the hallway before."
        "I took extra time to look at everything as if it were my first time outside the tiny room, but she barely seemed to be paying any attention to me."
    elif True:
        $ event_celia_enter_lounge = 1
        "A long hallway ended in what appeared to be a sort of lounge area."
        "More cabinets and papers littered the place."
        "Past the lounge area was a door that looked like it went to another office."
        "However, my attention was much more focused on what appeared to be an elevator."
        "Could that be the way out..?"
    if meme_mode:
        scene cg_celia_lounge_feet with dissolve
    elif True:
        scene cg_celia_lounge with dissolve
    $ persistent.cgs_celia.add("cg_celia_lounge")
    $ renpy.save_persistent()
    "She collapsed into one of the dusty lounge chairs."
    "I stood there, dazed from the bizarre situation."
    c empty "Sit."
    "I jumped slightly at the abrupt command."
    menu:
        " "
        "Sit on the floor" if True:
            $ celia_love += 1
            "I moved quickly to an empty spot on the floor in front of her and sat down."
            "It was dusty and dirty, but I barely noticed."
        "Sit on a chair" if True:
            "I looked around at the room and chose a chair across from her."
            "It was dusty from disuse but more comfortable than I expected."
    c empty "Good."
    c empty "Just... sit there."
    c empty "... Oh, right."
    c empty "You're probably hungry by now right?"
    "To my embarassment, I perked up like a dog."
    if meme_mode:
        scene cg_celia_lounge_happy_feet with dissolve
    elif True:
        scene cg_celia_lounge_happy with dissolve
    c empty "That's what I thought."
    if meme_mode:
        scene cg_celia_lounge_feet with dissolve
    elif True:
        scene cg_celia_lounge with dissolve
    "She moved her coat and rustled through a plastic bag I hadn't noticed before."
    "Then she held two items out to me."
    "Oh my god."
    "A bottle of water and some kind of wrapped deli sandwich."
    "I gingerly accepted them."
    "Seeing the food awakened my hunger so quickly that it startled me."
    "She seemed to sink into her chair."
    "She looked exhausted."
    "I couldn't wait any longer."
    $ stat_food += 10
    "I immediately opened the water and drank."
    "I tried to eat carefully and quietly."
    "I realized too late that she was aware I was staring at her."
    c empty "What is that look for?"
    menu:
        " "
        "\"Why would you want to relax... uh... here?\"" if True:
            if meme_mode:
                scene cg_celia_lounge_angry_feet with dissolve
            elif True:
                scene cg_celia_lounge_angry with dissolve
            "She narrowed her eyes at me."
            c empty "No."
            if meme_mode:
                scene cg_celia_lounge_feet with dissolve
            elif True:
                scene cg_celia_lounge with dissolve
            c empty "No, my home filled with 20 year old doe-eyed cooks and cleaners and whatever the fuck else is not more comfortable."
            c empty "My disgusting piece of shit husband runs the place like he's some kind of discount Hugh Hefner."
            "I watched her nails dig into the armrests until she suddenly let go and collapsed back into the chair."
            c empty "I don't even care that he fucks them."
            "She let out half a bitter laugh."
            c empty "Saves me the trouble."
            c empty "..."
            c empty "It's their faces."
            c empty "Subservient mewling sheep, always looking at the floor."
            c empty "They're so young... but they're already broken."
            c empty "Someone bought their dignity and they gave it up just like that."
            c empty "Without a fight."
            if meme_mode:
                scene cg_celia_lounge_angry_feet with dissolve
            elif True:
                scene cg_celia_lounge_angry with dissolve
            c empty "... It disgusts me."
            "I flinched as her sharp gaze flicked back to mine."
            "I couldn't help but gulp at the parallels between her 'sheep' and myself."
            menu:
                " "
                "Look away" if True:
                    $ celia_love -= 1
                    if meme_mode:
                        scene cg_celia_lounge_feet with dissolve
                    elif True:
                        scene cg_celia_lounge with dissolve
                    c empty "Tsk."
                "\"That doesn't sound that comfortable...\"" if True:

                    if meme_mode:
                        scene cg_celia_lounge_feet with dissolve
                    elif True:
                        scene cg_celia_lounge with dissolve
                    "She gestured sarcastically at our surroundings."
                    c empty "Hence my arrival here."
                "\"Do I... disgust you?\"" if True:

                    $ celia_love += 1
                    if meme_mode:
                        scene cg_celia_lounge_happy_feet with dissolve
                    elif True:
                        scene cg_celia_lounge_happy with dissolve
                    "To my surprise, she let out a laugh."
                    c empty "Oh... Mouse..."
                    c empty "Aren't you just {i}precious{/i}."
                    if meme_mode:
                        scene cg_celia_lounge_feet with dissolve
                    elif True:
                        scene cg_celia_lounge with dissolve
                    "... She never answered the question."
        "\"Isn't keeping me here more work for you?\"" if True:

            $ celia_love -= 1
            if meme_mode:
                scene cg_celia_lounge_angry_feet with dissolve
            elif True:
                scene cg_celia_lounge_angry with dissolve
            c empty "..."
            c empty "You might want to think twice before you convince me how difficult you are to keep."
            c empty "If the pleasure of your company can't outweigh your inconvenience..."
            c empty "I'd have to just put you down."
            if meme_mode:
                scene cg_celia_lounge_feet with dissolve
            elif True:
                scene cg_celia_lounge with dissolve
        "Say nothing" if True:

            "I looked down at the floor."
            "I don't need to be provoking her right now."
    "She closed her eyes and leaned back."
    "I briefly looked around the room with a jolt of adrenaline."
    "She's hardly paying attention-"
    if meme_mode:
        scene cg_celia_lounge_angry_feet with dissolve
    elif True:
        scene cg_celia_lounge_angry with dissolve
    c empty "Don't even think about it."
    "I froze."
    "Can she read my mind!?"
    c empty "We're going to have a simple, relaxing evening."
    c empty "I'm not going to hear my husband's voice and {i}you're{/i} not going to give me any trouble."
    if meme_mode:
        scene cg_celia_lounge_feet with dissolve
    elif True:
        scene cg_celia_lounge with dissolve
    "I slowly let the air out of my lungs."
    "Maybe I should just enjoy the 'break.'"
    $ stat_food += 5
    "I returned my attention to the deli sandwich."
    "I don't know if it was the hunger..."
    "But it tasted like the best sandwich I'd ever had."
    "I almost began to relax when I heard the buzz of a phone."
    play music "music/celias_theme.ogg"
    if meme_mode:
        scene cg_celia_lounge_angry_feet with dissolve
    elif True:
        scene cg_celia_lounge_angry with dissolve
    c empty "For {i}FUCK'S{/i} sake!"
    if meme_mode:
        scene cg_celia_lounge_phone_feet with dissolve
    elif True:
        scene cg_celia_lounge_phone with dissolve
    "She growled as she pulled out her phone."
    "For a split second, I felt sorry for whoever was on the other line, until I remembered my own position."
    c empty "No, I'm not home."
    c empty "I'm not at the office either- what do you want?"
    c empty "It's none of your goddamned business, Harold!"
    c empty "..."
    c empty "Fine."
    c empty "Yeah. I'll be there by seven."
    if meme_mode:
        scene cg_celia_lounge_angry_feet with dissolve
    elif True:
        scene cg_celia_lounge_angry with dissolve
    "I flinched as she turned off the phone and fumed."
    c empty "Tsk. Come on."
    scene bg_celia_lounge
    show celia serious:
        zoom 0.9
        xalign 0.5
        yoffset -50
    with dissolve
    "She motioned for me to get up."
    p "I-"
    c angry "I DON'T WANT TO THINK ABOUT MEN FOR ANOTHER SECOND!"
    "I recoiled from her sudden outburst."
    if celia_love < 3:
        c annoyed "Shut up and follow me."
    elif True:
        if pronoun == "he":
            c bored "... Not you."
            c "You don't count."
        c bored "Just... follow me."
    "I got up and followed her angry pace back to my small prison."
    $ map_location = "Room"
    call celia_display_subroutine from _call_celia_display_subroutine_8
    show celia serious with dissolve:
        zoom 0.9
        xalign 0.5
        yoffset -50
    c "Get in."
    "I swear I could feel her anger in waves radiating from her body."
    "I don't want that anger to be directed my way..."
    hide celia with dissolve
    stop music
    play sound "music/sfx_door_slam.ogg"
    "I obeyed and heard the door slam behind me."
    "I was sweating."
    "I think I dodged a bullet..."
    "I slumped to the floor."
    "Alone again..."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_donuts:
    $ phase = "event"
    $ event_celia_donuts = 1
    if map_location != "Room":
        jump event_celia_first_night_caught
    if event_celia_set_trap == 1:
        jump event_celia_wire_trap_end
    if map_location == "Room" and event_celia_brandy_poisoned == 1:
        jump event_celia_brandy_poisoned_death
    if celia_room_window_smashed == 1:
        jump event_celia_brokenwindow
    $ total_hours += 4
    $ hours += 4
    if arrivedby != "sleep":
        play sound "music/sfx_door_open.ogg"
        "The click of the door interrupted my thoughts."
        "I jumped at the sound."
        play music "music/celias_theme.ogg"
        c "Knock knock~"
    elif True:
        $ sleep = 0
        call celia_display_subroutine from _call_celia_display_subroutine_9
        play music "music/celias_theme.ogg"
        c "Knock knock~"
        "I was startled awake, my heart pounding."
    $ event_celia_room_door_locked = 1
    if celia_office_locked == 0 or celia_brandy >= 2:
        jump event_celia_stripsearch
    show celia relaxed with dissolve:
        zoom 0.9
        xalign 0.5
        yoffset -50
    "She entered the room briskly, and I realized I had flinched backward."
    show celia semiserious
    "She definitely noticed."
    c question "Ah... feeling a bit jumpy still?"
    c semiserious "I suppose that's only natural."
    "I noticed then that she was carrying a cardboard box."
    c relaxed "Well there's no need to be so skittish."
    c "I was thinking about you all day at work today..."
    c normal "And I decided to bring you a little treat!"
    "I flinched as she stepped closer."
    c "Here~"
    "She placed the box on my lap."
    "There was something tense in her voice."
    "Something that made me scared to open the box."
    "I looked up at her."
    c semiserious "Go on."
    "I tentatively lifted the top."
    scene cg_celia_donuts with dissolve
    $ persistent.cgs_celia.add("cg_celia_donuts")
    $ renpy.save_persistent()
    "Huh?"
    "It's just... a box of donuts."
    "And they smell good..."
    "My stomach growled."
    menu:
        " "
        "\"I can eat these?\"" if True:
            $ donut_answer = 1
            $ celia_love += 1
            call celia_display_subroutine from _call_celia_display_subroutine_10
            show celia:
                zoom 0.9
                xalign 0.5
                yoffset -50
            if pronoun == "he":
                c surprised "Oh?"
                c semiserious "My my, what a gentleman."
                c normal "They're {i}all{/i} yours."
            elif True:
                c normal "Well, of course you can, Mouse."
                c semiserious "They're for {i}you{/i}."
        "\"I'm allergic.\"" if True:
            $ donut_answer = 2
            call celia_display_subroutine from _call_celia_display_subroutine_11
            show celia:
                zoom 0.9
                xalign 0.5
                yoffset -50
            $ celia_love -= 1
            c surprised "Oh?"
            c bored "Well, that's a shame."
            pause (0.5)
            show celia gun
            pause (0.5)
            c "I suppose you'll just have to do your best anyway, won't you?"
        "\"I prefer timbits.\"" if meme_mode == True:
            $ donut_answer = 2
            call celia_display_subroutine from _call_celia_display_subroutine_4
            show celia mocking:
                zoom 0.9
                xalign 0.5
                yoffset -50
            $ celia_love -= 1
            c angry "You idiot!"
            c "They were bought out! They're not even Canadian anymore!"
            pause (0.5)
            show celia gun
            pause (0.5)
            c "Now EAT."
        "Say nothing" if True:
            $ donut_answer = 2
            call celia_display_subroutine from _call_celia_display_subroutine_12
            show celia serious:
                zoom 0.9
                xalign 0.5
                yoffset -50
            $ celia_love -= 1
            c "..."
            pause (0.5)
            show celia gun
            pause (0.5)
            c "Eat them."
    if donut_answer == 2:
        "Is that a fucking gun!?"
        "Would she really shoot? Why!?"
        "I gulped as I stared down the barrel of the gun."
        p "I... sure."
        p "Yeah..."
        scene cg_celia_donuts with dissolve
        "I slowly looked back down into the box."
        "They do just look like normal donuts."
        "I was sweating."
        "She wouldn't poison me though, right?"
        "Why would she go through the trouble?"
        "And why would she bring a gun!?"
        if pronoun == "he":
            c smile "Come on, Piggy."
            c sadistic "Get to work."
        elif True:
            c "Come on, Mouse."
            c smile "Don't keep me waiting..."
        "I shook my head slightly."
        "I don't have a choice."
    call celia_display_subroutine from _call_celia_display_subroutine_37
    show celia relaxed:
        zoom 1
        xalign 0.5
        yoffset -100
    "I trembled slightly as I took a donut from the box."
    show bg_celia_room:
        easein 0.5 yoffset -100
    show celia semiserious:
        easein 0.5 yoffset -250
    "And I took a bite."
    $ stat_food += 2
    "It's... good."
    "It just tastes like a normal donut."
    $ stat_food += 2
    show celia hungry
    "I began to register how hungry I was, and took another bite."
    show bg_celia_room:
        easein 0.5 yoffset 0
    show celia semiserious:
        easein 0.5 yoffset -100
    "I almost forgot about her presence for a second before I glanced up and saw her intense stare."
    "She was focused on me like a laser."
    show bg_celia_room:
        easein 0.5 yoffset -100
    show celia semiserious:
        easein 0.5 yoffset -250
    if donut_answer == 2:
        "Something about it was terrifying, but both my hunger and the threat of the gun had me taking another mechanical bite."
    elif True:
        "I was too hungry to worry about being watched."
    $ stat_food += 5
    "I silently ate the donut and swallowed."
    show bg_celia_room:
        easein 0.5 yoffset 0
    show celia relaxed:
        easein 0.5 yoffset -100
    "After I finished it, I glanced up to her."
    c semiserious "I didn't tell you to stop."
    show bg_celia_room:
        easein 0.5 yoffset -100
    show celia semiserious:
        easein 0.5 yoffset -250
    "I glanced back down at the box."
    "She doesn't expect me to eat all of these... does she?"
    $ stat_food += 5
    "I grabbed another one and started eating."
    c hungry "How does it taste?"
    "I swallowed my current mouthful."
    p "Uh... good?"
    c question "Describe.{w} It."
    show celia relaxed
    "I shivered."
    p "It's... sweet?"
    p "The icing is smooth and the dough is really cakey and soft..."
    "I had no idea what I was doing."
    c hungry "Mmmm~"
    "I gathered a bit of courage between bites."
    p "Uh... Why..?"
    c serious "Shut up and eat."
    if celia_love >= 1:
        show bg_celia_room:
            easein 0.5 yoffset 0
        show celia serious:
            easein 0.5 yoffset -100
        "I must have looked as confused as I felt because she sighed and began to answer."
        c "..."
        c annoyed "They were on my desk this morning."
        c "I'm sure it was that {i}snake{/i}, Jennifer."
        c "Little fake congratulations note on it and everything."
        "I made sure to keep eating, but I still couldn't make sense of the story."
        p "I'm not sure I... uh..."
        c surprised "..."
        c semiserious "Oh."
        c "Ignorance really is bliss, isn't it?"
        show celia mocking
        "She sighed wistfully."
        c relaxed "You don't get to where I am by eating whatever you want."
        c "If you're not an old man, you've got to do a lot more than just be good at your job."
        c mocking "That hardly counts for anything."
        c semiserious "I have to be {i}flawless{/i}."
        c normal "I need to recognize sabotage for what it is."
        c "And I have to stay two"
        show celia relaxed
        extend " steps"
        show celia semiserious
        extend " ahead."
        "I gulped and shakily returned my attention to the pastries."
    elif True:
        pass
    show bg_celia_room:
        easein 0.5 yoffset -100
    show celia serious:
        easein 0.5 yoffset -250
    c "A chocolate one next."
    "I quickly picked out a chocolate donut as instructed."
    $ stat_food += 5
    "She took a few deep breaths, watching me chew."
    show celia relaxed
    "Somehow, it seemed to calm her down."
    "I kept eating the donut awkardly as she stared."
    if celia_love >= 1:
        "I got to the fourth donut and I began to struggle."
        "I was so hungry before..."
        "But now I'm starting to feel sick."
        show celia serious
        p "I... don't think I can eat any more..."
        "She studied me for a moment and bit her lip."
        show celia semiserious
        c "One more."
        show celia relaxed
        "I breathed hard."
        "I can do this..."
        $ stat_food += 5
        "I slowly grabbed another donut and bit in."
        "I struggled to keep it down."
        show celia semiserious
        "I was squirming slightly, trying to find a position that didn't hurt as much."
        show bg_celia_room:
            easein 0.5 yoffset 0
        show celia hungry:
            easein 0.5 yoffset -100
        "I glanced up and saw that she seemed to be deeply enjoying the show."
        $ stat_food += 5
        show bg_celia_room:
            easein 0.5 yoffset -100
        show celia hungry:
            easein 0.5 yoffset -250
        "I just focused on the pastry and kept eating."
        c normal "There's a good little mouse~"
        $ stat_food += 5
        "I managed to stuff the last bit down and groaned softly."
        "My insides were aching."
        "But Celia looked extremely satisfied."
        show bg_celia_room:
            easein 0.5 yoffset 0
        show celia relaxed:
            easein 0.5 yoffset -100
        "She walked to me and took the box."
        c semiserious "Not bad~"
        "I flinched slightly as she extended her hand."
        show celia normal
        "To my surprise, she just brushed a crumb from my face."
        "I sat there, stunned, while my stomach lurched."
        c "I wish I could stay a little longer..."
        c annoyed "But I could only afford a quick visit today."
        c semiserious "You understand, right?"
        p "Ughh..."
        "I couldn't think straight."
        "I really did feel sick."
        show celia laughing at laugh:
            yoffset -100
        c "Haha!"
        c semiserious "I'll be back soon."
        stop music fadeout 1.0
        hide celia with dissolve
        "With that, she turned around and left, closing the door behind her."
        "I laid down and waited to feel better."
        p "Hrnn..."
        $ arrivedby = "special"
        jump celia_turn_nostats
    elif True:
        "I got to the fourth donut and I began to struggle."
        show bg_celia_room:
            easein 0.5 yoffset 0
        show celia relaxed:
            easein 0.5 yoffset -100
        p "I... don't think I can eat any more..."
        show celia serious
        "Something in her expression changed."
        c "You're not even halfway done."
        show celia gun
        "She flashed the gun again to remind me what my choices were."
        show bg_celia_room:
            easein 0.5 yoffset -100
        show celia gun:
            easein 0.5 yoffset -250
        "I groaned and grabbed another donut."
        show celia serious
        $ stat_food += 5
        $ stat_sanity -= 5
        "I tried to set my body on autopilot, eating without thinking."
        "The sweet taste and texture quickly became sickening."
        show celia semiserious
        "She leaned closer, her focus becoming a lot more predatory."
        "As I picked up another one, I lurched."
        $ stat_sanity -= 5
        "A shooting pain went through my gut, bringing tears up to my eyes."
        show celia hungry
        p "Please... I really can't..."
        $ stat_health -= 3
        play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
        scene black
        "Before I could react, the side of her gun was colliding with my face." with hpunch
        "I fell onto the dirty floor with the rest of the donuts scattering around me."
        show bg_celia_room:
            yoffset -100
        show celia semiserious:
            yoffset -250
            xalign 0.5
        with eyedissolve_reverse
        pause(0.5)
        show bg_celia_room:
            easein 0.5 yoffset 0
        show celia semiserious:
            easein 0.5 yoffset -100
        pause(0.5)
        c question "{i}Is it too much?{/i}"
        show celia semiserious
        "Her mocking tone of voice suggested she wasn't waiting for an answer."
        "I groaned in pain and clutched at my stomach."
        show celia sadistic
        pause (0.3)
        scene black
        play sound "music/sfx_impact_thud.ogg"
        "She knelt down to grab the back of my head and slammed it down into one of the donuts on the floor." with vpunch
        $ stat_sanity -= 5
        "I coughed and tried to breathe."
        play sound "music/sfx_impact_thud.ogg"
        "She slammed my face down one more time before standing up." with vpunch
        show bg_celia_room:
            yoffset -100
        show celia semiserious:
            yoffset -250
            xalign 0.5
        with eyedissolve_reverse
        pause(0.5)
        "I gasped as I rolled onto my side and choked back a sob."
        "It felt like I was going to explode."
        c annoyed "Tch. What a mess."
        "I couldn't tell if she meant me or the donuts."
        show celia semiserious
        "She nudged my body with her foot."
        c mocking "You're really not useful for {i}anything{/i} are you?"
        c semiserious "I came here with the easiest job in the world and you {i}still{/i} fucked it up."
        $ stat_health -= 3
        $ stat_sanity -= 5
        play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
        "I cried out as she kicked me in the gut with no warning." with hpunch
        c annoyed "I paid so much for you, too."
        c serious "What a ripoff."
        "She walked over to the door."
        c semiserious "You can make it up to me next time."
        stop music fadeout 1.0
        hide celia with dissolve
        show bg_celia_room:
            easein 0.5 yoffset 0
        "She slipped out the door while I writhed."
        "I never wanted to see another donut in my life."
        $ arrivedby = "special"
        jump celia_turn_nostats

label event_celia_complain:
    $ phase = "event"
    pause 1.0
    if map_location != "Room":
        jump event_celia_first_night_caught
    if event_celia_set_trap == 1 and map_location == "Room":
        jump event_celia_wire_trap_end
    if map_location == "Room" and event_celia_brandy_poisoned == 1:
        jump event_celia_brandy_poisoned_death
    if celia_room_window_smashed == 1:
        jump event_celia_brokenwindow
    $ event_celia_complain = 1
    $ total_hours += 4
    $ hours += 4
    $ stat_energy += 12
    $ sleep = 0
    if celia_office_locked == 0 or celia_brandy >= 2:
        call celia_display_subroutine from _call_celia_display_subroutine_13
        play music "music/celias_theme.ogg"
        jump event_celia_stripsearch
    $ map_location = "Basement"
    stop ambient fadeout 1.0
    $ renpy.music.set_volume(1.0, channel="ambient")
    play ambient "music/ambient_basement.ogg" fadein 1.0
    scene bg_celia_basement with Dissolve(2.0)
    p "Ughhnnn..."
    "I had a pounding headache."
    p "W... Where am I?"
    if event_celia_enter_basement == 1:
        "Wait... I recognized this room."
        "Why am I down here!?"
    elif True:
        "I didn't recognize this room."
        "How did I get here!?"
    show celia relaxed with dissolve:
        zoom 0.9
        yoffset -50
        xalign 0.5
    c "Wow... it took you forever to wake up."
    c normal "That was supposed to be the weak dose!"
    "I tried to back away, but I couldn't."
    "With a pang of terror, I realized I couldn't move."
    "I looked down at my body and saw I was completely tied up with bright red rope."
    c semiserious "Well, you seem to be able to struggle, at least."
    c relaxed "How do you feel?"
    menu:
        " "
        "Say nothing" if True:
            "I stayed quiet and stopped struggling."
            c sympathy "Can't work your mouth yet, hm?"
            c relaxed "That's okay."
            c semiserious "We'll get it moving again."
        "Be tough" if True:
            show celia surprised
            p "I'm... fine."
            show celia normal
            "Celia cracked an amused grin."
            c "Aren't you a trooper?"
            c semiserious "That's a good attitude."
        "Be honest" if True:
            $ celia_love += 1
            p "My head hurts... Everything hurts..."
            c sympathy "Hmm~ Knocked you out a little too hard huh?"
            c mocking "That's what I get for buying drugs from the internet, I guess."
            c normal "Hopefully you'll perk up as we get busy!"
    "She pushed me from my slumped position onto my back." with vpunch
    "I couldn't do anything but fall- the intricate pattern of rope held my limbs together."
    "I tried to push down the rising panic in my chest."
    "When did she even drug me?"
    "When I was sleeping..?"
    c mocking "Here's the thing."
    c semiserious "I had a {i}really{/i} shitty day today."
    scene cg_celia_straddle with dissolve
    $ persistent.cgs_celia.add("cg_celia_straddle")
    $ renpy.save_persistent()
    "I gasped as she sat down, straddling my waist."
    "I didn't expect her to get this close."
    c empty "And this {i}is{/i} what I bought you for."
    "I jerked against my bindings as I saw her pull out an expensive looking knife."
    c empty "Oh!"
    c empty "Don't worry!"
    c empty "You don't have to do anything complicated at all, this time."
    c empty "It'll be really easy."
    stop ambient fadeout 1.0
    play music "<from 35.5>music/celias_theme.ogg" fadein 1.0
    scene cg_celia_straddle_knife with dissolve
    $ persistent.cgs_celia.add("cg_celia_straddle_knife")
    $ renpy.save_persistent()
    c empty "I just need you to bleed for me."
    $ stat_sanity -= 5
    $ stat_health -= 1
    "I yelled in protest as she pressed the knife to the side of my face."
    "I screamed more in fear than pain."
    "The knife was so sharp that I didn't feel it as much as I expected to, but the panic tightening in my chest was only getting worse."
    scene cg_celia_straddle with dissolve
    c empty "See?"
    c empty "It's not so bad."
    "She held the knife to my face and caressed me."
    "The blood on her fingers told me that knife really did cut in deep despite the sensation."
    scene cg_celia_straddle_knife2 with dissolve
    c empty "You should see your face right now!"
    c empty "You're so cute..."
    $ stat_sanity -= 5
    $ stat_health -= 2
    "I strained against the ropes as she dipped the blade down to my collar bone and slid it through the thin layer of flesh there."
    "I grunted and screamed."
    c empty "I know, I know."
    "She pressed the knife to my arm."
    c empty "It's okay, you scream all you want~"
    $ stat_sanity -= 5
    $ stat_health -= 2
    "I tried to grit my teeth as she kept pressing the knife into my skin."
    "She moved it so slowly, going deeper."
    "I couldn't hold it in."
    $ stat_sanity -= 5
    $ stat_health -= 5
    "I screamed in earnest as the knife penetrated the muscle."
    p "Please... No more..."
    "She was panting softly."
    "She ignored my plea and just picked another place to drag the knife over."
    $ stat_sanity -= 5
    $ stat_health -= 5
    "I writhed, screaming and sweating as she kept making cut after cut."
    "I couldn't keep focus."
    "My body and mind were on fire."
    "What... is happening..?"
    "Is it the drug she used on me?"
    if sexcontent != "no":
        "I wheezed as the pressure on my waist increased."
        if sexcontent == "yes":
            scene cg_celia_straddle_sex with dissolve
        $ persistent.cgs_celia_sex.add("cg_celia_straddle_sex")
        $ persistent.cgs_celia.add("cg_celia_straddle_bag")
        $ renpy.save_persistent()
        "I automatically looked toward the source of the pressure, and my breath caught in my throat."
        "Her straddling position and short skirt revealed bare thighs and black lace panties."
        "I slammed my head back down and immediately felt my face get hotter."
        p "I-"
        "Should I apologize!?"
        "Will she be angry?"
        c empty "Ohh~?"
        "She bent low over me."
        if pronoun == "he":
            c empty "Look at you... are you a pig now, pervert?"
            c empty "Do you like what you see?"
        elif True:
            c empty "Do you like what you see?"
        "That has to be a trick question."
        p "I, um..."
        "She wasn't waiting for an answer."
        "She slid her hips up my waist and put her knees on my arms."
        "The cuts on my face and body were still screaming in pain, but somehow the inside of her thigh brushing against my cheek took precedence in my mind."
        if pronoun == "he":
            c empty "Why don't you make yourself useful... hm?"
        elif True:
            c empty "Why don't you show me what you can do, Mousey?"
        "I was shaking."
        $ stat_sanity -= 5
        "My wounds... the cold floor..."
        if sexcontent == "yes":
            scene cg_celia_straddle_sex2 with dissolve
        $ persistent.cgs_celia_sex.add("cg_celia_straddle_sex2")
        $ renpy.save_persistent()
        "The heat of her body, and her hand slowly pushing her panties to the side."
        "Her perfectly manicured fingers trailed my blood onto her skin."
        "I don't have a choice here."
        "I was already opening my mouth."
        "My tongue was trembling, but as soon as I tasted her warm flesh I became more sure."
        "She let out a moan... the kind you hear in a porno."
        "It sounded fake somehow."
        "A strange part inside of me was unhappy with that."
        "So I moved my tongue and pressed my lips to her."
        "How can someone so evil be so soft..."
        "Her thighs pressed against the side of my face."
        "I could taste my own blood."
        "She twitched with my motions and began to thrust against me."
        "Everything became hotter and wetter-"
        "And then she made another sound."
        "She didn't sound like a porno, she was no longer performing."
        "This sound was like an animal and it shot right through me to my core."
        "I pushed my tongue inside and sucked on her most sensitive skin."
        "I couldn't feel the cuts anymore."
        "I could feel the palm of her hand against my head, steadying me as she ground her hips against me."
        "It was messy and tight and sometimes I couldn't breathe but I kept my tongue moving."
        "She began to cry out, her movements were all sharp and jagged."
        "Her body was pulsing all around me, I swear I could hear her blood beating through her thighs."
        "Adrenaline kept my mouth open and my tongue stiff as she used me."
        "She became shaky herself, before I felt her nails dig into my scalp."
        "Pain shot through me to accompany her last loud cry."
        if meme_mode:
            $ stat_food += 10
        "I moaned into her flesh despite myself."
        "Her cry sounded like pain, while I bled in pleasure."
        if sexcontent == "yes":
            scene cg_celia_straddle_sex with dissolve
        "Too soon, she moved away from me and the heat was replaced by stinging cold air."
        "She was still panting, and her face was flushed."
        c empty "You... really are something else..."
        stop music fadeout 5.0
        stop ambient fadeout 5.0
        scene black with dissolve
        "I felt her weight lift from my body, and immediately my vision began to spot."
        "The strange adrenaline and euphoria of the moment was giving way to aching pain and hissing static in my ears."
        play sound "<from 0.0 to 2.0>music/sfx_heels.ogg" fadeout 1.0
        "I tried to focus as I heard her shoes click."
        "I can't..."
        pause 1.0
        $ map_location = "Room"
        $ renpy.music.set_volume(0.2, channel="ambient")
        play ambient "music/ambient_lights_hum_loop.ogg" fadein 1.0
        call celia_display_subroutine from _call_celia_display_subroutine_14
        "I slowly woke up, groaning in pain."
        "I must have passed out..."
        "I looked around at the familiar room."
        "Ugh... I'm back here..."
        $ arrivedby = "special"
        jump celia_turn_nostats
    elif True:
        scene cg_celia_straddle_bag with dissolve
        $ persistent.cgs_celia.add("cg_celia_straddle_bag")
        $ renpy.save_persistent()
        "But I barely noticed the thin plastic slide over my face."
        "Until one frozen, clear moment I saw her vicious eyes through the bag."
        p "NOOoo-Ach-"
        "I couldn't breathe in."
        $ stat_sanity -= 5
        "She held the bag to my neck as I helplessly bucked."
        "I was no longer in control of my body."
        "I tried to thrash, to breathe, to scream-"
        "I could barely move."
        "My vision was stained red as the bag was smeared with my blood."
        "I tried to see her through it."
        "The expression..."
        "Our eyes met and suddenly she let go."
        "I gasped desperately as the bag slid off of my face."
        "She only stared at me as I coughed."
        p "W... Why!?"
        "She cupped my face gently, as if she hadn't been the one just suffocating me."
        c empty "Don't worry..."
        c empty "I'm not going to {i}break{/i} you."
        c empty "I just wanted to see how far you'll bend..."
        "I wheezed under her."
        "She's crazy..."
        "I tried again to focus."
        "I think she was talking to me again, but I couldn't hear her over the static hissing in my ears."
        stop music fadeout 1.0
        stop ambient fadeout 1.0
        scene black with eyedissolve
        "I can't..."
        pause 1.0
        $ map_location = "Room"
        $ renpy.music.set_volume(0.2, channel="ambient")
        play ambient "music/ambient_lights_hum_loop.ogg" fadein 1.0
        call celia_display_subroutine from _call_celia_display_subroutine_15
        "I slowly woke up, groaning in pain."
        "I must have passed out..."
        "I looked around at the familiar room."
        "Ugh... I'm back here..."
        $ arrivedby = "special"
        jump celia_turn_nostats

label event_celia_endgame:
    $ phase = "event"
    $ event_celia_endgame = 1
    if arrivedby != "sleep":
        if map_location == "Elevator":
            "I was startled by the sound of voices above me."
            "Oh shit!"
            $ map_location = "Lounge"
            if meme_mode:
                stop music fadeout 1.0
            call celia_display_subroutine from _call_celia_display_subroutine_35
            "I slammed the buttons and left the elevator as quickly as possible."
        elif True:
            "I was startled by a low, mechanical hum."
            "After listening for a moment, I realized it must be the elevator."
    elif True:
        $ sleep = 0
        call celia_display_subroutine from _call_celia_display_subroutine_16
        "Something woke me up."
        "I lifted myself up and listened."
        if map_location == "Elevator":
            "I was startled by the sound of voices above me."
            "Oh shit!"
            if meme_mode:
                stop music fadeout 1.0
            $ map_location = "Lounge"
            call celia_display_subroutine from _call_celia_display_subroutine_36
            "I slammed the buttons and left the elevator as quickly as possible."
        elif True:
            "A mechanical hum..."
            "The elevator!?"
    if map_location != "Room":
        $ map_location = "Room"
        call celia_display_subroutine from _call_celia_display_subroutine_17
        if event_celia_set_trap == 1:
            "I sprinted to the small room I was kept in, then carefully stepped over my wire trap and closed the door."
        elif True:
            "I sprinted to the small room I had been kept in and closed the door."
    elif True:
        "I moved to the corner of the room and waited."
    "I could hear a voice..."
    "Wait..."
    "Two voices!?"
    "They sounded angry."
    "Shouting..."
    "One was definitely Celia, but the other sounded like a man..."
    "I flinched back as they got closer."
    if event_celia_set_trap != 1:
        show harold:
            alpha 0.0
            xalign 0.5
            yalign 1.0
            easein 0.2 alpha 1.0 xalign 0.75
        play music "<from 35.5>music/celias_theme.ogg" fadein 1.0
        play sound "music/sfx_door_slam.ogg"
        "The door flew open and a man barged in." with hpunch
        h "What the-"
        h "And what the hell is {i}this!?{/i}"
        show celia angry:
            zoom 0.9
            alpha 0.0
            xalign 0.5
            yoffset -50
            easein 0.2 alpha 1.0 xalign 0.25
        "I couldn't seem to react fast enough as Celia pushed past him and grabbed me."
        show celia angry:
            alpha 1.0
            xalign 0.25
            easein 0.2 alpha 0.0 xalign 0.0
        "While I was just barely registering the man in the doorway, I felt the blade of a knife press threateningly against my neck." with vpunch
        hide celia
        $ harold_name = "Harold"
        c angry "Not another {b}step{/b}, Harold!"
        menu:
            " "
            "Cry for help" if True:
                show harold surprised
                if meme_mode:
                    p "Help me! I'm just a poor little meow meow!"
                    h "Huh?"
                elif True:
                    p "Please! Help me!"
                "I strained against her, the panic outweighing the pain of the knife cutting into my skin."
                p "She'll kill me!!!"
                $ stat_health -= 5
                "The blade thrust up under my chin as her other hand clamped on my mouth, smothering my scream."
                c "Shut up!"
                c "And you..."
            "Explain the situation to him" if True:
                show harold surprised
                p "She kidnapped me! She trapped me here for days!"
                p "She's been torturing m-"
                $ stat_health -= 5
                "The blade thrust up under my chin as her other hand clamped on my mouth, smothering the rest of my sentence."
                c "Shut up!"
                c "And you..."
            "Stay quiet" if True:
                "I didn't dare make another sound."
                "I could feel the knife shaking against my skin."
                "Her body was pressed against my back... I could feel her breathing."
        "She pointed the knife out toward 'Harold'."
        show black behind harold:
            alpha 0.0
            easein 20 alpha 0.75
        c "You stupid bastard! You ruin everything!"
        h angry "Oh {i}I{/i} ruin everything?"
        h "I give you all the freedom and time in the world to do whatever you want..."
        h "And you fuck around in some condemned asbestos trap with some kind of homeless person?"
        h "And- and what?"
        h "Kidnapping, I guess?"
        c "Shut up!"
        "He ignored her completely."
        h "What if someone found this?"
        h "What if the {i}media{/i} found this?"
        show bg_celia_room behind black at heartbeat:
            yalign 0.0
        c "Take another step and I'll kill [pp_obj]!!!"
        h "Celia, please."
        h "Do you really think I care if you get your blouse dirty?"
        "My blood ran cold as I watched him take a step forward."
        "He's... not bluffing."
        h "You're going to clean this shit up, and we're going to go home."
        "The knife wasn't pressed against my throat anymore..."
        "But she was clutching me close."
        h "Get out of the way, Celia."
        "She was trembling..."
        show bg_celia_room:
            yalign 0.0
        hide black
        with dissolve
        "Then, she let me go and stepped away."
        h "I'm tired of cleaning up your messes."
        scene cg_celia_harold_shot with dissolve
        $ persistent.cgs_celia.add("cg_celia_harold_shot")
        $ renpy.save_persistent()
        p "What-"
        play sound "music/sfx_gunshot.ogg"
        stop ambient
        stop music
        scene black with vpunch
        if meme_mode:
            p "AUGH!"
            p "YOU SHOT ME, YOU CUCK!"
        pause 1.0
        $ quick_menu = False
        window hide
        hide screen effect_health
        hide screen effect_ice
        hide screen status
        $ persistent.endings_celia.add("You were cleaned up")
        $ persistent.deathcounter += 1
        $ renpy.save_persistent()
        call achievement_checker from _call_achievement_checker_16
        play music "<from 0.3>music/you_died.ogg"
        scene bg_endslate with blooddissolve
        show screen bg_endslate_text("You Died","You were cleaned up")
        $ renpy.pause(hard=True)
    elif True:
        play sound "music/sfx_door_slam.ogg"
        "I watched, stunned, as the door flew open and a large man tripped on the wire I set for Celia."
        play sound "music/sfx_impact_thud.ogg"
        play music "<from 35.5>music/celias_theme.ogg" fadein 1.0
        if meme_mode:
            scene cg_celia_harold_tripped_feet with vpunch
        elif True:
            scene cg_celia_harold_tripped with vpunch
        $ persistent.cgs_celia.add("cg_celia_harold_tripped")
        $ renpy.save_persistent()
        "He smashed into the floor with a loud thud."
        "I looked up and saw Celia behind him, for a moment just as stunned as I was."
        "She took a step back into the doorway."
        "There's no way past her..."
        "I had to think fast."
        "I leapt on top of the man and pulled out the rest of my wire."
        scene cg_celia_harold_choked with dissolve
        $ persistent.cgs_celia.add("cg_celia_harold_choked")
        $ renpy.save_persistent()
        "I wrapped it around his neck and turned back to her."
        c empty "What... is this?"
        menu:
            " "
            "A hostage" if True:
                p "Don't come any closer or I'll kill him!"
                p "Just... let me go!"
                scene cg_celia_harold_choked_2 with dissolve
                "She stared incredulously for a moment before cracking into a laugh."
                $ harold_name = "Harold"
                c empty "You think I'm worried about {i}Harold?{/i}"
                c empty "Please, by all means."
                c empty "Do kill him."
                h empty "You... hrk... bitch!!!"
                "The man bucked under me."
                "I tightened the wire in response."
                "What am I doing!?"
                "He began to thrash in panic, and make gurgling noises."
                "I looked back at her."
                menu:
                    " "
                    "Kill him" if True:
                        scene cg_celia_harold_kill_1 with dissolve
                        $ persistent.cgs_celia.add("cg_celia_harold_kill_1")
                        $ renpy.save_persistent()
                        "I don't have time to think about this."
                        "I kept the wire tight, even as it dug into my hands."
                        "I don't even know who he is."
                        "I can't think, my head is pounding..."
                        "Blood ran down my hands as his struggling began to weaken."
                        "I kept looking back at her, but her expression was unreadable."
                        "She just watched."
                        "My hands began to shake as I felt his body twitch under me."
                        "I felt nauseous."
                        "What am I doing..."
                        scene cg_celia_harold_kill_2 with dissolve
                        $ persistent.cgs_celia.add("cg_celia_harold_kill_2")
                        $ renpy.save_persistent()
                        "He slumped to the floor."
                        "What have I done?"
                        "I could feel tears pricking my eyes."
                        label event_celia_sorryrat:
                        "I began to turn back to her-"
                        $ stat_health -= 100
                        stop music fadeout 1.0
                        stop ambient fadeout 1.0
                        play sound "music/sfx_knife_stab.ogg"
                        "Pain shot through my body." with vpunch
                        "My back-"
                        "She was behind me, and her knife was lodged in my back."
                        if celia_love > 4:
                            c sad "I'm sorry, [player_name]."
                        elif pronoun == "he":
                            c bored "Sorry, Rat."
                        elif True:
                            c bored "Sorry, Mouse."
                        scene black with dissolve
                        "I lurched forward from the pain."
                        if celia_love > 4:
                            c sad "I know..."
                        "I coughed and tasted blood filling my mouth."
                        c "He called the police."
                        if celia_love > 4:
                            c sad "I have to go..."
                        elif True:
                            c annoyed "I can't stay here anymore."
                        "I tried to talk, tried to do anything."
                        "I couldn't move."
                        "Only more blood came from my throat."
                        "I could feel her arms around me."
                        if celia_love > 4:
                            c sad "For what it's worth..."
                            c sad "It was fun while it lasted."
                        elif True:
                            c bored "For what it's worth..."
                            c smile "It was fun while it lasted."
                        $ quick_menu = False
                        window hide
                        hide screen effect_health
                        hide screen effect_ice
                        hide screen status
                        $ persistent.endings_celia.add("You ran out of time")
                        $ persistent.deathcounter += 1
                        $ renpy.save_persistent()
                        call achievement_checker from _call_achievement_checker_17
                        play music "<from 0.3>music/you_died.ogg"
                        scene bg_endslate with blooddissolve
                        show screen bg_endslate_text("You Died","You ran out of time")
                        $ renpy.pause(hard=True)
                    "Spare him" if True:
                        "I can't do this!"
                        "I don't know what I'm doing!"
                        scene cg_celia_roomcorner with dissolve
                        $ persistent.cgs_celia.add("cg_celia_roomcorner")
                        $ renpy.save_persistent()
                        "I dropped the spool of wire and tried to scramble off the man's back-"
                        $ stat_health -= 100
                        stop music fadeout 1.0
                        stop ambient fadeout 1.0
                        play sound "music/sfx_knife_stab.ogg"
                        "Pain shot through my body." with vpunch
                        "My back-"
                        "She was behind me, and the blade of a knife was buried between my shoulders."
                        if celia_love > 4:
                            c sad "I'm sorry, [player_name]."
                        elif pronoun == "he":
                            c bored "Sorry, Rat."
                        elif True:
                            c bored "Sorry, Mouse."
                        scene black with eyedissolve
                        "I lurched forward as she slid the knife out of my flesh."
                        "I coughed and tasted blood filling my mouth."
                        c annoyed "He called the police."
                        scene cg_celia_slitharold_1 with eyedissolve_reverse
                        $ persistent.cgs_celia.add("cg_celia_slitharold")
                        $ renpy.save_persistent()
                        "I wavered as I saw her grasp his hair and pull up his head."
                        scene cg_celia_slitharold_2 with dissolve
                        "He screamed defiantly as she quickly slit his throat."
                        scene black with eyedissolve
                        "She unceremoniously dropped his head back onto the floor."
                        "I couldn't make sense of anything."
                        "What was happening?"
                        "Blood was spreading on the floor."
                        "I coughed and more warm liquid filled my mouth."
                        "I collapsed next to the dying man."
                        if celia_love > 4:
                            c sad "I have to go..."
                        elif True:
                            c annoyed "I can't stay here anymore."
                        "I tried to talk, tried to do anything."
                        "I couldn't move."
                        "Only more blood came from my throat."
                        "I could feel her hand on my back."
                        if celia_love > 4:
                            c sad "For what it's worth..."
                            c sad "It was fun while it lasted."
                        elif True:
                            c bored "For what it's worth..."
                            c smile "It was fun while it lasted."
                        $ quick_menu = False
                        window hide
                        hide screen effect_health
                        hide screen effect_ice
                        hide screen status
                        $ persistent.endings_celia.add("You ran out of time")
                        $ persistent.deathcounter += 1
                        $ renpy.save_persistent()
                        call achievement_checker from _call_achievement_checker_18
                        play music "<from 0.3>music/you_died.ogg"
                        scene bg_endslate with blooddissolve
                        show screen bg_endslate_text("You Died","You ran out of time")
                        $ renpy.pause(hard=True)
            "A gift" if True:

                $ celia_love += 1
                p "I..."
                p "I'll kill him for you..."
                if celia_love == 9 and achievement.has("ach_yes_mommy") != True:
                    $ persistent.ach_yes_mommy = True
                    $ achievement.grant("ach_yes_mommy")
                    init:
                        $ achievement.register("ach_yes_mommy")
                        $ achievement.sync()
                        $ renpy.save_persistent()
                        if persistent.ach_yes_mommy == True and achievement.has("ach_yes_mommy") != True:
                            $ achievement.grant("ach_yes_mommy")
                            $ achievement.register("ach_yes_mommy")
                            $ achievement.sync()
                "I looked back to her."
                "I don't even know who he is."
                "The man bucked under me."
                scene cg_celia_harold_kill_1 with dissolve
                $ persistent.cgs_celia.add("cg_celia_harold_kill_1")
                $ renpy.save_persistent()
                "I tightened the wire in response."
                c surprised "..."
                "What am I doing!?"
                "He began to thrash in panic, and make gurgling noises."
                c smile "Do it."
                "Her command rang through me."
                "I ran on instinct."
                "I pulled on the wire until my hands bled."
                "He was trying to scream, but he couldn't."
                "He was big, but he wasn't flexible."
                "The wire was digging into his throat and he couldn't do anything to shake me off his back."
                "I could feel her watching me."
                "My hands were steady."
                "It seemed easier with someone commanding me."
                "I was just following an order."
                "His struggling grew weaker, but I kept the wire tight."
                "After a while, he was only twitching under me."
                "I couldn't feel my fingers."
                scene cg_celia_harold_kill_2 with dissolve
                $ persistent.cgs_celia.add("cg_celia_harold_kill_2")
                $ renpy.save_persistent()
                "He slumped to the floor."
                if celia_love > 7:
                    call celia_display_subroutine from _call_celia_display_subroutine_18
                    show celia shocked with dissolve:
                        zoom 0.9
                        xalign 0.5
                        yoffset -50
                    stop music fadeout 1.0
                    stop ambient fadeout 1.0
                    "I turned back to look at her."
                    "She was... shaking?"
                    p "...Celia?"
                    c "You did it..."
                    c "He's actually dead..."
                    "I felt dizzy."
                    p "W... What now?"
                    c "..."
                    c worried "The police are already coming."
                    c "..."
                    c "If you're still here..."
                    c serious "You can't stay."
                    "She extended her hand."
                    "I pulled the bloody wire from my hands and I shakily reached out for her."
                    "She pulled me onto my unsteady feet."
                    c "We killed him together."
                    "She was breathing hard."
                    "She pulled me along by the hand like a child."
                    c angry "We have to go!"
                    $ map_location = "Elevator"
                    if meme_mode:
                        play music "music/music_elevator_muzak.ogg" fadein 1.0
                    call celia_display_subroutine from _call_celia_display_subroutine_19
                    play sound "music/sfx_beep.ogg"
                    "We reached the elevator, and I watched her use a key card."
                    scene black with dissolve
                    "... I'm actually leaving this building."
                    stop music fadeout 1.0
                    "It seemed so surreal to be walking through the ground floor with her."
                    "I could see the street lights outside through windows."
                    $ renpy.music.set_volume(1.0, channel="ambient")
                    play ambient "music/ambient_muffled_city.ogg" fadein 1.0
                    scene cg_celia_leave_1 with dissolve
                    $ persistent.cgs_celia.add("cg_celia_leave")
                    $ renpy.save_persistent()
                    "She let go of my hand and looked me in the eyes."
                    c empty "I can't stay here."
                    c empty "They're going to find out what happened."
                    c empty "So I need to disappear."
                    "I watched her face as she battled with some internal decision."
                    c empty "By the time they find out it was me..."
                    c empty "I'll be long gone."
                    scene cg_celia_leave_2 with dissolve
                    c empty "You have to get out of here."
                    c empty "No one will ever know you were involved."
                    menu:
                        " "
                        "Run" if True:
                            "I wasn't going to think twice."
                            stop music fadeout 1.0
                            stop ambient fadeout 1.0
                            scene black with dissolve
                            "I nodded once and pushed the office building's door open."
                            "I ran out into the street filled with street noise and rain."
                            "I kept running for as long as I could."
                            "And I never looked back."
                            $ quick_menu = False
                            window hide
                            hide screen effect_health
                            hide screen effect_ice
                            hide screen status
                            $ persistent.endings_celia.add("You were released")
                            $ renpy.save_persistent()
                            call achievement_checker from _call_achievement_checker_19
                            play music "music/music_city_lights.ogg" fadein 1.0
                            scene bg_endslate_survival with zoomdissolve
                            show screen bg_endslate_survival_text("You Lived","You were released")
                            $ renpy.pause(hard=True)
                        "{image=menu_sanity}Stay{space=60}" if sanity <= 30 and not renpy.variant("small"):
                            label menu_sanity_jumper_1:
                            p "I want to stay with you."
                            scene cg_celia_leave_3 with dissolve
                            "She stiffened in shock."
                            c empty "... What?"
                            p "Well... you have money, right?"
                            p "We could run together."
                            p "We could start over together..."
                            "I thought I could see an extra shine in her eye through her confusion."
                            c empty "But what about-"
                            p "I don't want to go back to my old life."
                            p "Please let me come with you!"
                            c empty "..."
                            c empty "This makes no sense... this is insane..."
                            p "I'm the one that killed him."
                            p "We both have to run."
                            p "We can figure the rest out later."
                            "I bit my lip and reached out."
                            "I held her hand in my own, ignoring the cuts from the wire."
                            "She looked down at the blood between our fingers."
                            scene cg_celia_leave_2 with dissolve
                            c empty "... Okay."
                            scene cg_celia_leave_4 with dissolve
                            if achievement.has("ach_romantically_insane") != True:
                                $ persistent.ach_romantically_insane = True
                                $ achievement.grant("ach_romantically_insane")
                                init:
                                    $ achievement.register("ach_romantically_insane")
                                    $ achievement.sync()
                                    $ renpy.save_persistent()
                                    if persistent.ach_romantically_insane == True and achievement.has("ach_romantically_insane") != True:
                                        $ achievement.grant("ach_romantically_insane")
                                        $ achievement.register("ach_romantically_insane")
                                        $ achievement.sync()
                            c empty "We'll run."
                            stop music fadeout 1.0
                            stop ambient fadeout 1.0
                            scene black with dissolve
                            $ quick_menu = False
                            window hide
                            hide screen effect_health
                            hide screen effect_ice
                            hide screen status
                            $ persistent.endings_celia.add("You ran away together")
                            $ renpy.save_persistent()
                            call achievement_checker from _call_achievement_checker_20
                            play music "music/music_city_lights.ogg" fadein 1.0
                            scene bg_endslate_survival with zoomdissolve
                            show screen bg_endslate_survival_text("You Lived","You ran away together")
                            $ renpy.pause(hard=True)
                        "{image=menu_sanity_large}Stay{space=60}" if sanity <= 30 and renpy.variant("small"):
                            jump menu_sanity_jumper_1
                elif True:
                    jump event_celia_sorryrat

label event_celia_first_night_caught:
    $ phase = "event"
    if map_location == "Elevator":
        jump event_celia_caught_elevator
    if map_location == "Basement" and event_celia_basement_caught == 0:
        jump event_celia_basement_caught
    if arrivedby != "sleep":
        play music "<from 35.5>music/celias_theme.ogg" fadein 1.0
        c surpangry "What the hell!?"
        "I whipped around, startled."
        "Where did she come from!?"
    elif True:
        $ sleep = 0
        call celia_display_subroutine from _call_celia_display_subroutine_20
        play music "<from 35.5>music/celias_theme.ogg" fadein 1.0
        c surpangry "What the hell!?"
        "I was startled awake by the sound of her voice."
    c "What are you doing out here!?"
    p "I... I-"
    "Wait... does she have a gun?"
    show celia gunangry:
        zoom 0.8
        alpha 0.0
        xalign 0.25
        yoffset -50
        easein 0.3 xalign 0.5 alpha 1.0
    c "Don't move!"
    p "Wai-"
    c "I SAID DON'T MOVE!"
    $ stat_sanity -= 20
    $ stat_health -= 50
    $ persistent.cgs_celia.add("cg_celia_ceiling_gun")
    $ renpy.save_persistent()
    play sound "music/sfx_gunshot.ogg"
    queue sound "music/sfx_ears_ring.ogg"
    scene black with vpunch
    "The force and noise knocked me backwards." with vpunch
    "I fell to the ground as my body began to register the pain."
    scene cg_celia_ceiling with Dissolve(2.0)
    "The sound of her approach was lost to the blood pounding in my ears."
    $ stat_health -= 10
    "I reached down to clutch at the wound on my thigh."
    "I blearily tried to hold it as blood poured from the wound."
    scene cg_celia_ceiling_gun with dissolve
    c empty "Wh-"
    c empty "Why are you bleeding so much!?"
    $ stat_health -= 10
    "My leg was beginning to feel cold."
    "Panic was slowing my thoughts down."
    c empty "No no no!"
    c empty "I only shot you in the leg!"
    c empty "Stop bleeding!"
    if celia_love > 5:
        c empty "S...stop..."
        c empty "I paid! I paid for you!"
        c empty "You can't just leave me!!!"
    elif celia_love > 0:
        c empty "I paid for you!"
        c empty "You're not allowed to die unless I make you!"
        c empty "You belong to ME!"
    elif True:
        c empty "You stupid son of a bitch!"
        c empty "Do you have any idea how much you cost me!?"
    $ stat_health -= 10
    "The cold feeling was spreading."
    "I couldn't seem to lift my arms."
    scene black with eyedissolve
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    if celia_love > 5:
        c empty "You're all that I have..."
    elif celia_love > 0:
        pass
    elif True:
        c empty "Tch... worthless."
    $ stat_health -= 30
    hide screen effect_health
    hide screen effect_ice
    "I couldn't see or feel much anymore."
    "But I could still hear her..."
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_celia.add("You were shot down")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_21
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You were shot down")
    $ renpy.pause(hard=True)

label event_celia_brandy_poisoned_death:
    $ phase = "event"
    if arrivedby != "sleep":
        play sound "music/sfx_door_slam.ogg"
        "I jumped as the door slammed open."
    elif True:
        $ sleep = 0
        call celia_display_subroutine from _call_celia_display_subroutine_21
        play sound "music/sfx_door_slam.ogg"
        "I woke up to the sound of the door slamming open."
    play music "<from 35.5>music/celias_theme.ogg" fadein 1.0
    c poisoned "You..."
    $ stat_health -= 5
    play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
    queue sound "music/sfx_ears_ring.ogg"
    scene black with vpunch
    "I had no time to react before something hard slammed into the side of my head." with vpunch
    "I fell to my knees, then the floor."
    "My ears were ringing."
    "She hit me with a flask..."
    $ persistent.cgs_celia.add("cg_celia_poisoned")
    $ renpy.save_persistent()
    scene cg_celia_poisoned with dissolve
    c empty "You think I don't know what you did!?"
    "She held me down and coughed violently."
    p "I-"
    play sound "music/sfx_impact_thud.ogg"
    "She grabbed my throat and slammed it." with vpunch
    "I tried to pull her hand away."
    "But my head was still throbbing and I couldn't focus."
    "I couldn't breathe."
    c empty "Stop... struggling..."
    "I desperately grabbed at her arm."
    "Suddenly, her hand left my throat."
    "I gasped in-"
    "And she shoved the flask into my mouth."
    "I convulsed as the liquid filled my throat... and my lungs."
    $ persistent.cgs_celia.add("cg_celia_poisoned2")
    $ renpy.save_persistent()
    scene cg_celia_poisoned2 with dissolve
    "I heard her laughing as I coughed and sputtered."
    $ stat_health -= 5
    "It felt like liquid fire, spreading inside me."
    "I clawed at her, as her laughter turned to coughing too."
    c empty "Now you're coming with me..."
    "I could feel her shaking and weakening over me."
    c empty "Fuck this place... and these people."
    c empty "You're mine..."
    "She held my face."
    c empty "You'll always be-"
    stop music fadeout 3.0
    scene black with vpunch
    "She collapsed on top of me and I wheezed."
    "It was harder to cough."
    "The pain was fading."
    "I could feel her still."
    "She wasn't breathing anymore."
    stop ambient fadeout 1.0
    hide screen effect_health
    hide screen effect_ice
    "I didn't have the strength to move at all."
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_celia.add("You got a taste of your own medicine")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_22
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You got a taste of your own medicine")
    $ renpy.pause(hard=True)

label event_celia_starving:
    $ phase = "event"
    play sound "music/sfx_hunger.ogg"
    "I nearly jumped at the sound of a low growl."
    p "Ugh..."
    "It was just my stomach..."
    $ stat_sanity -= 10
    "I'm absolutely starving..."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_basement_caught:
    $ phase = "event"
    if arrivedby != "sleep":
        pass
    elif True:
        $ sleep = 0
        call celia_display_subroutine from _call_celia_display_subroutine_22
        "I woke up suddenly."
    $ event_celia_basement_caught = 1
    play sound "<from 11.0>music/sfx_unlock_digital.ogg"
    "Huh?"
    "I thought I heard something..."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_try_office:
    $ phase = "event"
    $ event_celia_try_office = 1
    "I walked through the lounge to the office door."
    "No window... can't see inside."
    "But there might be stairs inside or some kind of way out..."
    "I rattled the doorknob."
    "Ugh... of course."
    $ sanity -= 5
    "It's locked."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_numpad_incorrect:
    $ phase = "event"
    play sound "music/sfx_wrong.ogg"
    "... Damn."
    call celia_display_subroutine from _call_celia_display_subroutine_23
    "I guess that's not it."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_numpad_empty:
    $ phase = "event"
    call celia_display_subroutine from _call_celia_display_subroutine_38
    "I left the number pad."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_numpad_69:
    $ phase = "event"
    play sound "music/sfx_wrong.ogg"
    "Hehe, nice."
    call celia_display_subroutine from _call_celia_display_subroutine_39
    call ach_pinpad_stupid from _call_ach_pinpad_stupid
    "It may not have opened the door, but it made me feel a little better."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_numpad_420:
    $ phase = "event"
    play sound "music/sfx_wrong.ogg"
    "Heh... blaze it..."
    call celia_display_subroutine from _call_celia_display_subroutine_40
    call ach_pinpad_stupid from _call_ach_pinpad_stupid_1
    "Am I going crazy down here?"
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_numpad_8008:
    $ phase = "event"
    play sound "music/sfx_wrong.ogg"
    "Heh..."
    "Boob."
    call celia_display_subroutine from _call_celia_display_subroutine_42
    call ach_pinpad_stupid from _call_ach_pinpad_stupid_2
    "It may not have opened the door, but it made me feel a little better."
    $ arrivedby = "special"
    jump celia_turn_nostats

label ach_pinpad_stupid:
    if achievement.has("ach_real_mature") != True:
        $ persistent.ach_real_mature = True
        $ achievement.grant("ach_real_mature")
        init:
            $ achievement.register("ach_real_mature")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_real_mature == True and achievement.has("ach_real_mature") != True:
                $ achievement.grant("ach_real_mature")
                $ achievement.register("ach_real_mature")
                $ achievement.sync()
    return

label event_celia_numpad_1988:
    $ phase = "event"
    play sound "music/sfx_wrong.ogg"
    "..."
    call celia_display_subroutine from _call_celia_display_subroutine_41
    "You know, they say that's the year the accident happened."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_numpad_correct:
    $ phase = "event"
    play sound "<from 0.0 to 2.0>music/sfx_unlock_digital.ogg"
    $ map_location = "Basement"
    $ celia_basement_locked = 0
    if event_celia_enter_basement == 0:
        "... Oh!?"
        "It worked!"
        if "item_note" not in inventory:
            "I suppose it was a {i}lucky guess{/i}."
        "I opened the door and stepped into darkness."
        scene bg_celia_stairs with dissolve
        $ persistent.bgs_seen.add("bg_celia_stairs")
        $ renpy.save_persistent()
        "...Stairs?"
        "My excitement died in my throat."
        "... Down."
        "Well..."
        "Whatever is down there, she's worked hard to hide it."
        "I have to check it out."
        "I descended the stairs and turned the corner."
        call celia_display_subroutine from _call_celia_display_subroutine_24
        $ arrivedby = "special"
        jump celia_turn_nostats
    elif True:
        call celia_display_subroutine from _call_celia_display_subroutine_25
        $ arrivedby = "new"

label event_celia_unlock_office:
    $ phase = "event"
    $ event_celia_try_office = 1
    $ map_location = "Office"
    $ celia_office_locked = 0
    $ arrivedby = "special"
    if event_celia_enter_office == 0:
        if event_celia_try_office == 0:
            $ event_celia_try_office = 1
            "I looked around the area for a door to try."
            "That door at the end of the lounge looks promising..."
            "I pressed my key into the lock."
        elif True:
            "I pressed the key into the lock of the door at the end of the lounge."
        "To my surprise, it easily went all the way in."
        "Holy shit, this is the right key!"
        play sound "music/sfx_unlock.ogg"
        "I slowly opened the door."
    elif True:
        play sound "music/sfx_unlock.ogg"
        "I used the key and quickly unlocked the door."
    call celia_display_subroutine from _call_celia_display_subroutine_26
    jump celia_turn_nostats

label event_celia_lock_office:
    $ phase = "event"
    $ celia_office_locked = 1
    $ arrivedby = "special"
    play sound "music/sfx_unlock.ogg"
    "I slid the key into the lock and locked the door."
    jump celia_turn_nostats

label event_celia_unlock_room:
    $ phase = "event"
    $ event_celia_room_door_locked = 0
    $ arrivedby = "special"
    "I pushed the pin into the hole in the door handle."
    play sound "music/sfx_unlock.ogg"
    "After some nudging, I managed to get a click."
    "I turned the handle."
    "It's open..."
    $ map_location = "Lounge"
    call celia_display_subroutine from _call_celia_display_subroutine_27
    jump celia_turn_nostats

label event_celia_findpin:
    $ phase = "event"
    "Wait."
    "What's that?"
    "I saw something shine on the floor in front of the door."
    "I crawled over to pick it up."
    $ inventory.append("item_pin")
    $ renpy.notify("Pin Added!")
    show screen inventory
    pause(1.5)
    hide screen inventory
    "It looks like a hair pin."
    "Maybe she dropped it on her way out..."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_drink_soda:
    $ phase = "event"
    "I cracked open the can."
    "I have no idea how old this is..."
    "But I'm {i}seriously{/i} thirsty."
    "I lifted the can to my lips."
    "It's..."
    "It's warm but it tastes fine!"
    "I quickly gulped the rest."
    $ stat_food += 10
    $ stat_sanity += 20
    $ inventory.remove("item_soda")
    "I sighed with relief."
    "My head already feels better."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_try_elevator:
    $ phase = "event"
    $ event_celia_try_elevator = 1
    "I approached the elevator."
    "The lights are all on... this should be working."
    "I pressed the 'up' arrow."
    "..."
    "I heard something!"
    "My heart started hammering as the elevator doors opened in front of me."
    $ map_location = "Elevator"
    if meme_mode:
        play music "music/music_elevator_muzak.ogg" fadein 1.0
    call celia_display_subroutine from _call_celia_display_subroutine_28
    "I rushed inside."
    "It was surprisingly clean compared to the rest of what I've seen."
    "Eight floors... three basements."
    "I looked up above the door."
    "Apparently I'm on B1. No wonder I haven't seen any windows."
    "I pressed the button for ground floor."
    play sound "music/sfx_beep.ogg"
    "I jumped at the loud beep."
    "What!?"
    "A light was flashing... next to a slot."
    "A card slot."
    $ stat_sanity -= 10
    "No... no no no."
    "I frantically tried the other buttons."
    "Even the second basement."
    "Everything just made the light flash."
    "I groaned in defeat."
    "This fucking thing won't go anywhere without some kind of card key..."
    $ arrivedby = "special"
    jump celia_turn_order

label event_celia_taser_battle:
    $ phase = "event"
    "Two can play at that game."
    "I made a motion as if I was removing my jacket, discretely finding the taser in the pocket."
    $ persistent.cgs_celia.add("cg_celia_taserbattle_1")
    $ renpy.save_persistent()
    scene cg_celia_taserbattle_1 with dissolve
    play sound "music/sfx_taser.ogg"
    "I whipped around and slammed the weapon into her chest."
    "Her knees buckled, and she stumbled backwards."
    "She wasn't able to speak through the shock, but her expression said more than enough."
    "\"Only one of us is getting out of this.\""
    "I pressed the taser against her, listening to clicks and watching her convulse."
    "She crumpled downwards, dropping her gun."
    "For a moment, I felt a wave of satisfaction."
    "I kept the weapon on her, refusing to let up."
    "I was nearly on top of her when I realized the clicking had stopped."
    "It's already out!?"
    "I felt her twitch."
    "I have to think fast!"
    "I kicked the gun away from us as she grabbed my arm."
    scene black
    "She threw me off balance, sending us both to the floor." with hpunch
    $ persistent.cgs_celia.add("cg_celia_taserbattle_2")
    $ renpy.save_persistent()
    scene cg_celia_taserbattle_2 with dissolve
    c empty "You..."
    "All traces of poise and flawless presentation were gone."
    "I was so focused on the gun, I hadn't realized that she grabbed my taser."
    $ stat_health -= 5
    play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
    queue sound "music/sfx_ears_ring.ogg"
    "I had no time to flinch as she smashed it into the side of my head." with hpunch
    c empty "FUCKING ANIMAL!"
    "My ears were ringing, I reeled from the blow."
    $ stat_health -= 5
    scene black
    play sound "<from 5.0 to 6.0>music/sfx_impact.ogg"
    "She whipped it into my face again with even more force." with hpunch
    "I couldn't think."
    "I groaned and shielded my face."
    "She had stopped beating me with the spent taser..."
    scene cg_celia_taserbattle_3 with dissolve
    "When I looked again my blood ran cold."
    "She had the gun again, looming over me."
    "I felt the barrel press against my neck."
    "I couldn't do anything but stare."
    play sound "music/sfx_gunshot.ogg"
    $ stat_health -= 100
    scene black with vpunch
    pause 1.0
    $ quick_menu = False
    window hide
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_celia.add("You fought and lost")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_23
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You fought and lost")
    $ renpy.pause(hard=True)

label event_celia_basement_cage:
    $ phase = "event"
    "Something in me seemed to break."
    "I began to sob uncontrollably."
    "I couldn't stop myself."
    scene black with dissolve
    "I curled into a ball and screamed."
    p "I CAN'T TAKE THIS ANYMORE!"
    "..."
    "I don't know how long I stayed that way."
    "I couldn't move."
    "I could hardly breathe."
    "When I finally heard her approach me, I felt an odd sense of relief."
    call celia_display_subroutine from _call_celia_display_subroutine_29
    play music "music/celias_theme.ogg" fadein 1.0
    show celia angry with dissolve:
        zoom 0.9
        xalign 0.5
        yoffset -50
    if map_location != "Room":
        c angry "How did you get out here!?"
        c serious "..."
    c angry "What the hell is going on with you..?"
    show celia surprised
    p "JUST KILL ME ALREADY!"
    show celia annoyed
    "I completely broke down and began to sob again."
    "I was practically screaming."
    "I nearly choked as my body was wracked with despair."
    c "..."
    if map_location == "Basement":
        c serious "I think it's time for the cage."
    elif True:
        c serious "I think it's time for you to go downstairs."
    "I wasn't listening."
    "And I didn't notice her pulling out a small syringe."
    c "Shh."
    c semiserious "This will help you feel better."
    "... Huh..?"
    pause(1.0)
    scene black with eyedissolve
    pause(2.0)
    "My head was pounding."
    $ persistent.cgs_celia.add("cg_celia_basement_cage")
    $ renpy.save_persistent()
    scene cg_celia_basement_cage_alone with dissolve
    stop music fadeout 1.0
    play ambient "music/ambient_dire_situation.ogg" fadein 1.0
    p "Uuu... Uh!?"
    "I can't talk!?"
    "The pain in my head..."
    "My mouth..."
    "I opened my mouth, and a shaking finger confirmed my fear."
    "Blood... My tongue..."
    "It's gone..."
    "Tears rolled down my aching cheeks."
    "I tried to move."
    "I couldn't stand."
    "With a wave of dread, I realized that a metal cage surrounded me."
    if event_celia_enter_basement == 1:
        "I recognized this room."
        "I was in the basement."
    elif True:
        "Beyond my cage was a tarp... and blood stains."
        "A terrible chill ran down my spine."
        "This is not a good place to be."
    "I tried to move to get a better look, but a jolt of pain from my ankles distracted me."
    "I inspected the sore area and balked."
    "My mutilated mouth could only express my terror with a muffled moan."
    "Crude stitches held a gash on the back of each of my ankles closed."
    "I tried to move my feet and began to panic when I couldn't."
    "She cut something..."
    "I can't move my feet."
    "Oh god, I can't walk."
    "I let out the closest thing to a scream I could."
    "The panic exploded and I grabbed the bars of the cage."
    "I pulled and cried in anguish."
    "They didn't budge at all."
    "The sound of slow footsteps on the nearby stairs told me I had alerted my captor."
    scene cg_celia_basement_cage with dissolve
    "She sauntered to my cage and smiled down at me."
    if pronoun == "he":
        c empty "No more walking around like you own the place, hm?"
    elif True:
        c empty "Sorry honey, but bad little mice get the snip!"
    "She let out a quiet, cruel laugh."
    c empty "I suppose it was irresponsible to leave you loose."
    c empty "I should have kept a better eye on you."
    c empty "But that won't be a problem anymore!"
    c empty "From now on, you can stay down here~"
    "She took time to look over my body."
    "She seemed satisfied with her work."
    "I moaned in protest and rattled the cage."
    c empty "Oh, careful now!"
    c empty "Your stitches need to heal up."
    "I looked down."
    "How could anyone do this!?"
    c empty "I know you're upset now."
    c empty "But I'm sure you'll adjust."
    c empty "Every minute of every single day, you'll be in there... waiting for me."
    "She paused, looking me over again."
    c empty "Eventually you'll learn to appreciate it."
    c empty "You'll {i}beg{/i} for me."
    c empty "And I'll take good care of you..."
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black with Dissolve(2.0)
    pause 1.5
    "The days went by and all her words came true."
    "Sometimes she came with food and supplies, and sometimes she came with blades and a cruel smile."
    "But just like she promised, I began to beg for her."
    "As days stretched into weeks, the loneliness became maddening."
    "Even when she tortured me, I craved her attention."
    "She was the only living thing in the dead world of my metal cage."
    "I became an animal for her."
    "In that dark, deep basement, nothing else mattered."
    "I forgot about the rest of the world."
    "I would never see it again."
    $ quick_menu = False
    window hide
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_celia.add("You became her broken toy")
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_24
    play music "<from 0.4>music/music_but_at_what_cost.ogg" fadein 1.0
    scene bg_endslate_survival with zoomdissolve
    show screen bg_endslate_survival_text("You Lived","You became her broken toy")
    $ renpy.pause(hard=True)

label event_celia_headache:
    $ phase = "event"
    $ event_celia_headache = 1
    "I squinted at the overhead lights."
    p "Ughh..."
    "I realized my head was pounding."
    $ sanity -= 10
    "I held my face in my hands and groaned."
    "How long has it been since I've eaten any real food?"
    "Or water..."
    "I tried to swallow, but my mouth was dry."
    if event_celia_donuts == 1:
        "All I've eaten is-"
        "I didn't want to think about sugar again."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_sanity_1:
    $ phase = "event"
    $ event_celia_sanity_1 = 1
    "Has that noise always been so loud?"
    "The mechanical hum of the lights and the drone of the ventilation system..."
    "I covered my ears."
    "It seemed to vibrate right through my skin."
    p "Hrrr..."
    "I gasped in surprise when I realized I'd been digging my nails painfully into my head."
    "My ears were ringing..."
    "I have... to get out of here..."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_sanity_2:
    $ phase = "event"
    $ event_celia_sanity_2 = 1
    play sound "<from 2.0>music/sfx_laugh.ogg"
    "What was that?"
    "I whipped my head and looked behind me."
    "What..."
    "There's nothing behind me."
    "I thought I heard..."
    "I couldn't stop the chill that crawled up the skin on my back."
    "I jumped and spun again."
    "That feeling when someone is right next to your ear..."
    "My heart was pounding."
    "I was panting."
    p "WHO'S THERE!?"
    "My own hoarse voice sounded alien to me."
    "I looked down at my shaking hands."
    "Why am I shouting..?"
    "There's nothing here..."
    "I fought back the urge to cry."
    "I can't do this anymore..."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_set_trap:
    $ phase = "event"
    $ event_celia_set_trap = 1
    "I pulled out the spool of wire."
    "Unravelling a bit, I watch the light glint off of it."
    "It's strong and hard to see..."
    "The idea for a trap quickly took shape in my mind."
    "The doorframe is metal."
    "I crouched down to take a look."
    "Screws..."
    "Ah!"
    "I pulled out the office key and used it to loosen the screws on either side of the doorframe."
    "Now I have something to tie the wire to!"
    "I twisted the wire around one protruding screw, then the other."
    "I bent the wire back and forth and used the key to cut it off."
    "I was sweating from the effort by the time I finished."
    "But..."
    "This looks like a really good trap."
    "The wire, only inches off the floor across the doorway, was tough to spot."
    "There's no way she'd notice it while she tried to enter the room."
    "She'll trip for sure..."
    "And when she does..."
    "I chewed my lip."
    "Well, one step at a time."
    $ arrivedby = "special"
    jump celia_turn_nostats

label event_celia_wire_trap_end:
    $ phase = "event"
    if arrivedby != "sleep":
        "From my place against the wall I heard the telltale clack of shoes on the floor outside the room."
    elif True:
        $ sleep = 0
        call celia_display_subroutine from _call_celia_display_subroutine_30
        "I jolted awake at the sound of approaching footsteps."
    "My heart raced as I moved to the wall beside the door."
    "It was like being on autopilot."
    "I held my breath, trying to listen through the pounding heartbeat in my ears."
    "The click of the knob turning..."
    play music "<from 35.5>music/celias_theme.ogg" fadein 1.0
    c surpangry "H-AHH!"
    $ persistent.cgs_celia.add("cg_celia_fallen")
    $ renpy.save_persistent()
    if meme_mode:
        scene cg_celia_fallen_feet with vpunch
    elif True:
        scene cg_celia_fallen with vpunch
    "She crashed ungracefully to the floor."
    "She didn't manage to break her fall at all."
    "She was groaning in pain, but my focus was on the shining rectangle that slipped from her pocket."
    "Beside her sprawled body was a card key."
    "For a split second, I stood there as she was stunned into silence."
    menu:
        " "
        "Run" if True:
            "I sprung into action and snatched the card."
            c empty "Get back here!"
            $ map_location == "Lounge"
            call celia_display_subroutine from _call_celia_display_subroutine_31
            "I moved faster than I ever have in my life."
            $ persistent.cgs_celia.add("cg_celia_escape")
            $ renpy.save_persistent()
            scene cg_celia_escape_1 with dissolve
            "I sprinted through the hallway and to the elevator."
            "I slammed the button repeatedly and slipped into the opening door."
            "I slid the card into the slot."
            "{i}Please please please work...{/i}"
            "I heard her groaning in the other room."
            play sound "music/sfx_beep.ogg"
            "The light turned green!"
            play sound "<from 0.5 to 0.8>music/sfx_heels.ogg"
            "I heard the clack of a shoe."
            "I pressed the ground floor button with the frequency of a hummingbird's wingbeat."
            "I heard her moan in pain and stumble into the hallway."
            "I pressed the 'close door' button over and over."
            "PLEASE!"
            "The doors began to move."
            c nosebleed "No... no NO NO!"
            "She stumbled into view."
            scene cg_celia_escape_2 with dissolve
            c empty "NO!!!"
            stop music
            stop ambient
            play sound "music/sfx_elevator_door.ogg"
            scene cg_celia_escape_3 with dissolve
            if meme_mode:
                play music "music/music_elevator_muzak.ogg" fadein 1.0
            pause(1.0)
            "I stared at the closed doors."
            "The sound of her fists pounding on the other side faded into the sound of my own heartbeat pounding on the inside of my head."
            "I did it..."
            scene black with dissolve
            stop music fadeout 1.0
            "The door opened into a dark, empty office building."
            "I took the key card and ran forward toward the light."
            "I burst out from the glass entrance door and into the street light."
            "Fresh air... rain... the sound of other human beings."
            "The real world."
            "I'm... free."
            "I ran out into the night."
            $ quick_menu = False
            window hide
            hide screen effect_health
            hide screen effect_ice
            hide screen status
            $ persistent.endings_celia.add("You left her behind")
            $ renpy.save_persistent()
            call achievement_checker from _call_achievement_checker_25
            play music "music/music_city_lights.ogg" fadein 1.0
            scene bg_endslate_survival with zoomdissolve
            show screen bg_endslate_survival_text("You Lived","You left her behind")
            $ renpy.pause(hard=True)
        "Attack" if True:
            "I didn't think."
            "I just moved."
            "I jumped onto her back and pulled out the wire spool."
            c empty "W- wait!"
            "I saw flecks of blood on the floor in front of her face."
            $ persistent.cgs_celia.add("cg_celia_wirekill_1")
            $ renpy.save_persistent()
            scene cg_celia_wirekill_1 with dissolve
            "I pulled a length of cord and yanked it up under her neck."
            if meme_mode:
                p "YOU'RE NOT GONNA GASLIGHT GATEKEEP GIRLBOSS YOUR WAY OUT OF THIS ONE!"
            "I felt her entire body stiffen under me with panic."
            "She scrambled desperately as I pushed my knee into her back and pulled harder on the wire."
            "I think she was trying to scream."
            "I pulled so hard the wire was cutting into the flesh of my hands."
            "I didn't care."
            "She thrashed under me like an animal."
            "She couldn't seem to make any sound."
            "I could see blood on her neck and her fingers as she tried to pull the wire away."
            "The only sound was the dull thudding from her writhing and my hoarse breathing."
            "I felt like I was an animal too."
            "I used all my strength, fueled by my own fear and panic."
            "The wire was cutting into both of us."
            "The thudding became quieter and the struggle became easier."
            "But I didn't ease up."
            "I pulled the wire as her resistance waned."
            "Through her fingers and into her vulnerable neck."
            "I kept pulling."
            "Blood dripped from my hands."
            scene black with dissolve
            stop music fadeout 1.0
            $ renpy.music.set_volume(1.0, channel="ambient")
            play ambient "music/ambient_drone_intermittent.ogg" fadein 1.0
            "Soon, she wasn't moving anymore."
            "Only my panting was left in the room."
            "Still, I kept the wire tight."
            "I stayed there for long minutes after she stopped moving."
            "I had to be sure."
            "I don't know how long I stayed like that."
            "The shaking of my hands caught my eye and brought me back into time."
            $ persistent.cgs_celia.add("cg_celia_wirekill_2")
            $ renpy.save_persistent()
            scene cg_celia_wirekill_2 with vpunch
            "I let out a ragged breath and let go of the wire."
            "I grimaced as I realized the wire wouldn't fall."
            "I pulled it out of my flesh."
            "It didn't seem to hurt."
            "I looked past my bleeding hands."
            if achievement.has("ach_have_a_nice_trip") != True:
                $ persistent.ach_have_a_nice_trip = True
                $ achievement.grant("ach_have_a_nice_trip")
                init:
                    $ achievement.register("ach_have_a_nice_trip")
                    $ achievement.sync()
                    $ renpy.save_persistent()
                    if persistent.ach_have_a_nice_trip == True and achievement.has("ach_have_a_nice_trip") != True:
                        $ achievement.grant("ach_have_a_nice_trip")
                        $ achievement.register("ach_have_a_nice_trip")
                        $ achievement.sync()
            call cutthroat_checker from _call_cutthroat_checker_1
            "She's dead."
            $ map_location = "Room"
            call celia_display_subroutine from _call_celia_display_subroutine_32
            "I stumbled backwards off of her."
            if meme_mode:
                "She dead as hell."
            elif True:
                "She's dead!"
            "I shakily got to my feet after a couple of failed tries."
            "God... I killed her."
            "I killed her."
            "There's blood everywhere."
            "The card."
            "I spotted the white card that fell from her pocket."
            "I snatched it off the ground and held it."
            "My hand smeared red all over it."
            "I closed my eyes for a moment and then began to move."
            $ map_location = "Elevator"
            if meme_mode:
                stop ambient fadeout 1.0
                play music "music/music_elevator_muzak.ogg" fadein 1.0
            call celia_display_subroutine from _call_celia_display_subroutine_33
            "I walked through the hallway to the elevator."
            "I carefully slipped the card into the key slot."
            play sound "music/sfx_beep.ogg"
            "The light turned green."
            "I slowly pushed the button for the ground floor."
            "The doors closed and the elevator moved."
            "I was moving."
            "I was leaving."
            scene black with dissolve
            play sound "music/sfx_ding.ogg"
            if meme_mode:
                stop music fadeout 1.0
                play ambient "music/ambient_drone_intermittent.ogg" fadein 1.0
            "A small tone sounded and I left the elevator."
            "I walked into the dark, abandoned office building."
            "I walked toward the light."
            "Slowly, I pushed open one last door, and I was outside."
            "The street light shimmered as rain fell on my face."
            "I'm outside..."
            "The sound of the busy street was surreal."
            "I turned and walked down the street as the blood was slowly washed from my hands."
            $ quick_menu = False
            window hide
            hide screen effect_health
            hide screen effect_ice
            hide screen status
            $ persistent.endings_celia.add("You killed for your freedom")
            $ renpy.save_persistent()
            call achievement_checker from _call_achievement_checker_26
            play music "<from 0.4>music/music_but_at_what_cost.ogg" fadein 1.0
            scene bg_endslate_survival with zoomdissolve
            show screen bg_endslate_survival_text("You Lived","You killed for your freedom")
            $ renpy.pause(hard=True)

label event_celia_caught_elevator:
    $ phase = "event"
    if arrivedby != "sleep":
        play sound "music/sfx_ding.ogg"
        "I was startled by the sound of a mechanical 'ding'."
    elif True:
        $ sleep = 0
        call celia_display_subroutine from _call_celia_display_subroutine_34
        play sound "music/sfx_ding.ogg"
        "I was startled awake by the sound of a mechanical 'ding'."
    "Before I could react, the elevator began to move."
    "What the hell!?"
    "I watched the numbers light up..."
    "My heart pounded as I saw the display light up for the ground floor."
    "In the single second between the chime and the doors opening, my mind raced."
    $ persistent.cgs_celia.add("cg_celia_elevator_1")
    $ renpy.save_persistent()
    scene cg_celia_elevator_1 with dissolve
    play sound "music/sfx_elevator_door.ogg"
    play music "<from 35.5>music/celias_theme.ogg" fadein 1.0
    "The doors slid open, and all my hope drained out."
    "We stood motionless, facing each other, for a single moment that seemed to stretch."
    $ stat_health -= 50
    $ stat_sanity -= 50
    $ persistent.cgs_celia.add("cg_celia_elevator_2")
    $ renpy.save_persistent()
    play sound "music/sfx_knife_stab.ogg"
    if meme_mode:
        scene cg_celia_elevator_2_feet with vpunch
    elif True:
        scene cg_celia_elevator_2 with vpunch
    pause
    "... What?"
    scene black with dissolve
    "I fell back onto the elevator floor."
    "She... she..."
    "I gasped fruitlessly for air."
    $ persistent.cgs_celia.add("cg_celia_elevator_3")
    $ renpy.save_persistent()
    scene cg_celia_elevator_3 with dissolve
    c empty "What did you think you were doing?"
    c empty "How did you even get out of that room?"
    "My mouth moved, trying to form a response."
    "I coughed and blood filled my throat."
    c empty "I guess it doesn't matter anymore..."
    "Her voice was sounding far away."
    "I could tell now that I was passing out."
    if celia_love > 2:
        c empty "I actually liked you, you know."
        c empty "This is such a damn waste."
    elif True:
        c empty "You've been a pain from the start."
        c empty "I guess it's time to put you down and start over."
    scene black with dissolve
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    "I felt sharp metal against my throat."
    $ stat_health -= 100
    "I couldn't scream as it separated my flesh."
    "I could only lie there as my own warm blood pooled around my face."
    $ quick_menu = False
    window hide
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_celia.add("You were caught in the elevator")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_27
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You were caught in the elevator")
    $ renpy.pause(hard=True)

label event_celia_stripsearch:
    $ phase = "event"
    "As she walked in, I could tell something was wrong."
    "Her calculating expression sent a shiver up my neck."
    c "Well."
    "She stepped closer."
    c question "It seems you've been busy."
    show celia semiserious:
        zoom 0.9
        xalign 0.5
        yoffset -50
    "What is she talking about?"
    label event_celia_strip_jump:
    "I began to sweat."
    c serious "Stand up straight."
    if celia_brandy > 2:
        c "..."
        c "Wait a second..."
        c angry "Are you DRUNK!?"
    "I wasn't sure if it was fear or hesitation, but I failed to move for a moment."
    show celia gunangry
    "My heart immediately began pounding as I saw her slowly pull out a pistol."
    "I stood up straight."
    if celia_brandy > 2:
        c "Sneaky little rat..."
        if meme_mode:
            p "Well what do you expect..."
            "I tried to hold in a burp and failed."
            p "What else am I a'sposed to do down here?"
    elif True:
        "What did I do!?"
    c "Strip."
    "I balked."
    p "Wh-"
    c "{i}I don't like repeating myself.{/i}"
    "She aimed the gun at my legs."
    "Shit shit shit!"
    if "item_battery_taser" in inventory:
        menu:
            " "
            "Start stripping" if True:
                pass
            "{image=menu_battery_taser}Attack her{space=60}" if not renpy.variant("small"):
                jump event_celia_taser_battle
            "{image=menu_battery_taser_large}Attack her{space=60}" if renpy.variant("small"):
                jump event_celia_taser_battle
    show bg_celia_room:
        easein 0.5 yoffset -200
    show celia gunangry:
        easein 0.5 zoom 1.0 yoffset -250
    "I shakily undid the buttons on the blazer I had been placed in at some point before waking up here."
    "These aren't even my clothes..."
    "As I pulled the jacket off, I paused for a split second in horror."
    "The stuff in my pockets..."
    "I threw the blazer on the floor, hoping she didn't notice my pause."
    "I squeezed my eyes shut and pulled off the shirt."
    "She knows... she has to know."
    "Dread was weighing my limbs down."
    "I undid the pressed formal pants."
    "I kept shaking and sweating."
    "I tried to just concentrate on my task."
    "Don't think about the gun, don't think about the hand holding it..."
    show bg_celia_room:
        easein 0.3 yoffset 0
    show celia gunangry:
        easein 0.3 zoom 0.9 yoffset -50
    "I froze."
    "She's looking right into my eyes."
    "She can tell. She knows everything."
    "I flinched as she began to speak."
    c gun "I didn't tell you to stop."
    show bg_celia_room:
        easein 0.9 yoffset -200
    show celia gunangry:
        easein 0.9 zoom 1.0 yoffset -250
    "All that's left is my underwear."
    "With a tilt of her head and a flick of the gun, the message was crystal clear."
    "The fear for my life kept me from any shame until this point."
    "But as I slowly pulled off my underwear, the exposure hit me like a wave."
    "She kept her eyes on me as she bent down to pick up the blazer."
    "I tried to cover myself."
    c "Hands down."
    "I stiffly complied, feeling my face getting hotter."
    "I really shouldn't be concerned about my nudity at a time like this..."
    "I chewed my lip."
    "A new wave of fear took my attention away from my embarassment as she rummaged through the pockets."
    show bg_celia_room:
        easein 0.5 yoffset 0
    show celia gun:
        easein 0.5 zoom 0.9 yoffset -50
    c "You HAVE been busy."
    "My blood turned to ice as she dropped the blazer and its contents."
    p "I..."
    "I tried to think of an excuse-"
    show celia gunangry
    $ stat_health -= 20
    $ stat_sanity -= 20
    scene black
    play sound "music/sfx_gunshot.ogg"
    p "AHhhhh!!" with vpunch
    "I fell to the ground, screaming."
    "Pain exploded from a bullet hole below my knee."
    "I crumpled around it, watching blood begin to pour from it."
    "My mind was racing through incomplete thoughts."
    $ persistent.cgs_celia.add("cg_celia_strip_gun")
    $ renpy.save_persistent()
    scene cg_celia_strip_gun
    play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
    "My panic was interrupted by a kick forcing me flat on my back." with vpunch
    $ stat_health -= 5
    $ stat_sanity -= 5
    "I screamed again as she stepped on the fresh wound."
    c empty "It's a shame you had to be {i}so much trouble{/i}."
    c empty "You're actually pretty cute when all you're wearing is blood..."
    $ stat_health -= 20
    $ stat_sanity -= 20
    play sound "music/sfx_gunshot.ogg"
    "Another explosion in my shoulder." with vpunch
    play sound "music/sfx_ears_ring.ogg"
    "My ears were ringing so loudly, I couldn't tell if I was still screaming or not."
    "Panic blurred my vision."
    "Is she talking..?"
    "I think I'm begging now. I can't hear myself."
    "There's blood everywhere, all over my skin."
    if meme_mode:
        "I shakily reached up and stuck my finger in the barrel of the gun."
        p "Heh... now you can't shoot..."
    elif True:
        "I tried to focus."
        "I stared down the barrel of the gun and saw her finger move."
        "No-"
    play sound "music/sfx_gunshot.ogg"
    $ stat_health -= 100
    scene black with vpunch
    pause 1.0
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    $ quick_menu = False
    window hide
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_celia.add("You were stripped")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_28
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You were stripped")
    $ renpy.pause(hard=True)

label event_celia_basement_whip:
    $ phase = "event"
    "I walked back up the stairs to the door."
    "..."
    "It's closed..?"
    scene black
    play sound "music/sfx_unlock.ogg"
    queue sound "music/sfx_impact_thud.ogg"
    p "Wh-wha-augh!"
    pause(0.5)
    $ stat_health -= 10
    play sound "<from 0.0 to 1.0>music/sfx_impact_bone.ogg"
    "I hit the ground with a horrifying crack." with vpunch
    "I could barely process what happened."
    scene bg_celia_basement with Dissolve(1.5)
    play music "music/celias_theme.ogg"
    "She was there..."
    "She kicked me down the stairs."
    show celia serious with dissolve:
        zoom 0.9
        xalign 0.5
        yoffset -80
    c "So..."
    c "Are you going to tell me what you thought you were doing down here?"
    "I couldn't answer."
    "I could barely breathe."
    "The pain from the fall had spread through my body in waves until they felt strong enough to choke me."
    "A terrified croaking sound escaped me instead as I saw my twisted ankle."
    "That's {i}definitely{/i} broken."
    if event_celia_complain == 0:
        c relaxed "Hm."
        "I watched as she sauntered across the room."
        c semiserious "Do you know what I use this room for?"
        "She grabbed what looked like a bright red rope from a shelf."
        "I tried to move, to get up- but it just sent a new white hot wave of pain up my legs."
    elif True:
        c question "I'm surprised you'd want to come back down here."
        "She held up some familiar looking red rope."
        c semiserious "But since you're so eager..."
    "She tied the rope and walked over to me."
    "I could do nothing but whimper in agony as she bent down to lower the loop of rope over my neck."
    c relaxed "Come on."
    $ stat_sanity -= 10
    show black with dissolve
    "I screamed in pain as she suddenly grabbed my legs and dragged me awkwardly into the center of the room."
    scene bg_celia_basement with dissolve:
        zoom 1.2
        xalign 1.0
        yalign 0.0
    show celia bored with dissolve:
        xalign 0.5
        yoffset -80
    c bored "Phew..."
    c normal "All right, this part is probably going to hurt."
    "I watched in horror as she tossed the rope up a few times, finally getting it through a pulley screwed into the ceiling."
    "She can't be..."
    show bg_celia_basement:
        easein 0.2 yoffset -100
    show celia semiserious:
        easein 0.2 yoffset -50
    pause(0.1)
    play sound "music/sfx_rope.ogg"
    "She pulled the rope down, hard." with vpunch
    $ stat_health -= 5
    "The noose pulled me up by my neck."
    "I grabbed at in in panic as another scream was stunted by the rope."
    "My weight was shifted to my broken ankle."
    "I couldn't focus through the pain."
    "I think she attached the rope to something?"
    "As my feet left the floor, I was choked completely."
    scene black with dissolve
    "She's going to hang me!?"
    "I gasped in a breath as I felt a chair slide under my injured legs."
    $ persistent.cgs_celia.add("cg_celia_whip1")
    $ renpy.save_persistent()
    if meme_mode:
        scene cg_celia_whip1_feet with dissolve
    elif True:
        scene cg_celia_whip1 with dissolve
    c empty "That's better~"
    "I struggled painfully as she admired her handiwork, panting slightly from the effort."
    "I couldn't take the weight off my throbbing ankle without strangling myself."
    c empty "You seem to be having trouble!"
    "She's enjoying this..."
    c empty "But you don't think I'll just let you hang there like that, do you?"
    c empty "No..."
    "She grabbed something else from a shelf."
    $ persistent.cgs_celia.add("cg_celia_whip2")
    $ renpy.save_persistent()
    if meme_mode:
        scene cg_celia_whip2_feet with dissolve
    elif True:
        scene cg_celia_whip2 with dissolve
    c empty "You're not getting off that easy."
    $ stat_health -= 5
    play sound "<from 0.0 to 1.0>music/sfx_impact_whip.ogg"
    "She wound up, and the whip cracked on my body." with vpunch
    "I cried out as she grinned."
    c empty "Looks like I still know how to use it..."
    $ stat_health -= 5
    play sound "<from 1.5 to 2.2>music/sfx_impact_whip.ogg"
    "She landed another stinging lash across my torso." with vpunch
    "I tried to scream, cry, or even beg."
    "But it was a struggle just to breathe."
    $ stat_health -= 5
    play sound "<from 3.5>music/sfx_impact_whip.ogg"
    c empty "Hahaha!" with vpunch
    $ stat_health -= 5
    play sound "<from 0.0 to 1.0>music/sfx_impact_whip.ogg"
    c empty "Come on, don't fall~" with vpunch
    "I can't..."
    $ stat_health -= 5
    play sound "<from 3.5>music/sfx_impact_whip.ogg"
    "I can't keep my legs..." with vpunch
    $ stat_health -= 20
    play sound "<from 0.0 to 1.5>music/sfx_rope.ogg" fadeout 1.0
    scene black
    stop music fadeout 3.0
    stop ambient fadeout 3.0
    "My knees buckled out from under me." with vpunch
    c annoyed "Hey."
    c "We're not done!"
    "I could hear her begin to yell, but I couldn't make out the words anymore."
    $ quick_menu = False
    window hide
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_celia.add("You were strung up")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_29
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You were strung up")
    $ renpy.pause(hard=True)
label event_celia_sleepfail:
    $ phase = "event"
    "I tried to fall asleep..."
    "But I just wasn't tired enough."
    $ arrivedby = "special"
    jump celia_turn_nostats
label event_celia_drunk:
    $ total_hours += 1
    $ phase = "event"
    if arrivedby != "sleep":
        "I froze as I heard the familiar approach of footsteps."
    elif True:
        $ sleep = 0
        call celia_display_subroutine from _call_celia_display_subroutine_43
        "I was woken by the familiar approach of footsteps."
    play sound "music/sfx_door_slam.ogg"
    play music "music/celias_theme.ogg" fadein 1.0
    show celia drunk:
        zoom 0.9
        xalign 0.5
        yoffset -50
    c "Whu..."
    c "What are you doing here?"
    "I looked around myself incredulously."
    p "Deadass?"
    p "You're keeping me here."
    p "I can't leave."
    c "No... What?"
    "She stumbled a little bit and seemed to be trying to focus."
    "She absolutely reeked of alcohol."
    p "I think you're drunk..?"
    c "..."
    c "I put in the app... I said uhhh..."
    c "I put home in."
    "I couldn't tell what she was trying to say."
    p "CELIA. I THINK YOU'RE DRUNK."
    c "Huh?"
    "Oh my god."
    c "Oh, wait."
    c "This is..."
    c "Oh yeah..."
    hide celia with dissolve
    stop music fadeout 1.0
    play sound "music/sfx_door_slam.ogg"
    "Just as quickly as she barged in, she left."
    "What the hell!?"
    $ arrivedby = "special"
    jump celia_turn_nostats



label game_start_derek:
    $ gamepath = "derek"
    $ location_temp = "hot"
    $ map_location = "Camp"
    $ food = 20
    $ energy = 24

    play ambient "music/ambient_desert.ogg" fadein 5.0
    play sound "music/sfx_atv_approach_stop.ogg"
    "The sound of a motor began to cut through the darkness."
    p "Ughnn..."
    "Before I opened my eyes, I felt someone grab my arms."
    d grumpy "How are you {i}still{/i} asleep?"
    if meme_mode:
        d mocking "You know..."
        d "You wouldn't be here if you invested in NFTs."
        "Urgh... what?"
    scene bg_derek_camp with eyedissolve_reverse
    play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
    "My eyes snapped open as the hands dragging me dropped my head unceremoniously onto the hot sand." with vpunch
    play music "music/dereks_theme.ogg" fadein 1.0
    d "Wakey wakey!"
    "I coughed in the dry heat."
    p "Where-"
    "My question died in my throat as I looked around and realized that there were more people here."
    show dragon:
        xalign 0.28
        yalign 1.0
        alpha 0.0
        easein 0.25 xalign 0.25 alpha 1.0
    dragon "Wow. Even cuter than the last one."
    show komodo:
        xalign 0.72
        yalign 1.0
        alpha 0.0
        easein 0.25 xalign 0.75 alpha 1.0
    komodo "Yeah..."
    komodo "Hey Derek, how much did you pay this time?"
    $ derek_name = "Derek"
    d angry "Shut the fuck up!"
    show komodo:
        xalign 0.75
        yalign 1.0
        easein 0.25 xalign 0.65
    komodo "{size=-10}He's not even denying it.{/size}"
    dragon "Ha!"
    hide komodo
    hide dragon
    with dissolve
    "What the hell is going on?"
    "It was apparent that the angry blonde guy was the one that brought me here."
    "My arms were tied behind my back and my legs were tied together..."
    "I struggled to push myself to sit upright so I could see better."
    "There were other people tied up like me. Two men and a crying woman."
    menu:
        " "
        "Watch the men in masks" if True:
            "I turned my attention back to our captors."
            $ derek_name = "\"Scorpion\""
            d "I told you to call me Scorpion!"
            if meme_mode:
                $ derek_name = "Derek"
                dragon "Derek, no one is ever going to call you Scorpion."
                dragon "It's never going to happen."
                komodo "It's not gonna happen Derek."
            elif True:
                dragon "Hahaha!"
                dragon "Maybe you shouldn't have told us your name then, idiot."
            d "You don't have any idea who you're talking to!"
            d "I could make you disappear, no one would ever find the body!"
            komodo "Try it."
            "He's so mad his fist is shaking..."
            "Whoever these people are, they don't seem to be 'friends'."
        "Try to communicate with the other captives" if True:
            "I leaned in quietly towards the other captives before whispering."
            p "What is happening? Where are we?"
            cham "..."
            rich "..."
            tom "... I think they're gonna kill us."
            "The woman started crying harder."
            "I looked down at myself."
            "Just a tank and underwear, same as the others."
            if meme_mode:
                "I reached over and nonchalantly smacked the skinny one."
            "Are they really..?"
    "I froze as I saw another mask."
    "The three arguing men were so loud that I didn't notice a fourth man in the back."
    show machete:
        alpha 0.0
        yalign 1.0
        xalign 0.5
        easein 0.25 xalign 0.5 alpha 1.0
    machete "..."
    "He seemed to be staring right at me..."
    d normal "Come onnnn, let's just start!"
    $ derek_name = "Derek"
    dragon "Jesus Christ, Derek."
    dragon "You have the patience of a toddler."
    d angry "Shut up!"
    d "I've waited a whole fucking year for this!"
    hide machete with dissolve
    "The sound of an approaching motor caught everyone's attention."
    d normal "{i}Finally!{/i}"
    "I struggled against my binding."
    "The terror building in my chest was telling me that I really didn't want to find out what these people were waiting for."
    "The sound of the engine stopped with the muttering of the three men."
    "The rope wasn't budging."
    d "There he is~!"
    "Another man in a mask emerged, roughly dragging a bound woman."
    "She was fully awake and wildly thrashing."
    "I recoiled back automatically as he came close and dumped her face-first in the sand next to me."
    $ jack_name = "Jack"
    d "Damn, Jack."
    d "Another wild one!"
    jaq "LET ME G-"
    "I flinched as I watched him kick her down to silence her."
    jack "It's better that way."
    show jack:
        alpha 0.0
        yalign 1.0
        xalign 0.45
        easein 0.25 xalign 0.5 alpha 1.0
    "The older looking masked man stood up straight, cracking his back and neck."
    jack "So, are we ready to get started then?"
    d "Hell yeah!"
    dragon "We should do first blood again."
    dragon "It really sets the mood for the rest of them."
    d mocking "Pfft. {i}\"Sets the mood\"{/i}."
    komodo "It's important."
    jack "Sure. Might as well kick it off."
    d grumpy "Yeah, okay."
    d normal "... Which one though?"
    jack "I want to chase mine."
    dragon "We can do one of ours."
    komodo "Hey, wait!"
    dragon "We only really {i}need{/i} one."
    komodo "... Yeah."
    komodo "All right, fine."
    d "Oh- oh! The girl then!"
    d "The crybaby!"
    cham "No, please..."
    jack "You two okay with dropping one of yours?"
    komodo "Yeah, sure."
    hide jack with dissolve
    "The one named \"Jack\" approached the sobbing woman and grabbed her."
    "He dragged her into the middle of the group."
    menu:
        " "
        "Look away" if True:
            "I couldn't keep watching."
            scene black with eyedissolve
            "I squeezed my eyes shut."
            d normal "Look how much she's crying already!"
            d "Hahaha! I haven't even done anything yet!"
            cham "P-please! Don't!"
            "This has to be some kind of prank or something..."
            d high "Keep begging..."
            cham "PLEASE!"
            "I nearly opened my eyes before a scream tore through the air."
            "I lowered my head instead."
            "I can't watch this... I can't."
            "I heard the men moving and jeering."
            "I cringed as she began to shriek."
            "Whatever they were doing... they were taking their time."
            "Her screaming felt like it was going through my whole body."
            "I needed to think about something else."
            "I turned to the other captives."
        "Keep watching" if True:

            "I couldn't look away."
            $ persistent.cgs_derek.add("cg_derek_cham")
            $ renpy.save_persistent()
            scene cg_derek_cham with dissolve
            d empty "Look how much she's crying already!"
            d empty "Hahaha! I haven't even done anything yet!"
            "The panic on her face rose to a new level as Derek pulled out a large knife."
            cham empty "P-please! Don't!"
            "He grabbed a fistful of her hair and pushed the knife up to her throat."
            d empty "Keep begging..."
            "She sobbed loudly."
            cham empty "PLEASE!"
            "Suddenly, she shrieked."
            "While I was watching Derek, Jack had stabbed a switchblade into her thigh."
            "My heart leapt into my throat."
            "This is real. This isn't a joke."
            "They're going to kill her."
            if sexcontent != "no":
                "I began to feel sick as I watched Derek squeeze the woman's breast as he laughed in her face."
                "Jack cut away her underwear with the bloody switchblade he ripped out of her leg."
                "They're not just going to kill her."
            elif True:
                "I began to feel sick as I watched Derek cut the skin around her neck while laughing in her face."
                "Jack withdrew his knife and began stabbing her legs repeatedly."
                "Blood was pouring from her wounds."
            $ stat_sanity -= 10
            scene black with eyedissolve
            "I... I can't watch this anymore!"
            "I couldn't move or scream or do anything to help her."
            "I could only shrink back as I heard more shuffling, laughing, and screaming."
            "Her crying and terrified screams only seemed to excite them all more."
            "I cringed away from the growing frenzy."
            "She had stopped begging a while ago- she was only screaming worldlessly now."
            $ stat_sanity -= 10
            "It rang through my head as I kept my head down and my eyes closed."
            "I was shaking as I realized tears were rolling down my face, too."
            "She was choking and sobbing now."
            if sexcontent != "no":
                "The rhythmic slapping of flesh told me what else was happening."
                "I felt sick."
            "I couldn't take it anymore."
            "I looked away to the faces of the other captives."
        "Try to distract them" if True:

            jump event_derek_firstblooddeath
    $ persistent.cgs_derek.add("cg_derek_victims")
    $ renpy.save_persistent()
    scene cg_derek_victims with dissolve
    "The skinny man was staring at the ground."
    "The other man had his eyes shut tight, tears streaming down his face."
    "The woman that Jack brought was watching every move with so much rage that it sent a chill through me."
    "We were probably all thinking the same thing:"
    "\"We're next.\""
    "A glint of metal caught my attention past the chaos."
    "It was the last man. With the plain mask."
    "He finally moved from his position."
    "The others were too engrossed in their torture to notice his approach."
    $ persistent.cgs_derek.add("cg_derek_machete")
    $ renpy.save_persistent()
    scene cg_derek_machete with dissolve
    "I sucked in a breath as I saw him raise a large machete."
    scene black
    play sound "<from 0.0 to 1.0>music/sfx_axe_chop.ogg"
    "My body jerked as I watched him bring down the weapon with so much force that she was instantly beheaded." with vpunch
    "I don't know if it was shock or if everything really did go quiet for a moment."
    "It felt like slow motion. Like in a nightmare."
    call derek_display_subroutine from _call_derek_display_subroutine
    d angry "What the FUCK!?"
    d "You could have cut my hands off!"
    "The two men in lizard masks laughed to each other."
    $ machete_name = "Machete"
    jack "Always right to the point, eh Machete?"
    show jack:
        xalign 0.03
        yalign 1.0
        alpha 0.0
        easein 0.25 xalign 0.0 alpha 1.0
    "Jack straightened himself up."
    show machete:
        xalign 0.97
        yalign 1.0
        alpha 0.0
        easein 0.25 xalign 1.0 alpha 1.0
    machete "... I'm here to kill."
    "The other man stared for a second before barking out a sharp laugh."
    jack "Aren't we all."
    "They all seemed to calm down while they cleaned off their blades and backed away from the corpse."
    jack "All right. Let's get this party started for real."
    "I tried not to look at the woman's body and the spreading dark red in the sand beneath her severed head."
    hide machete with dissolve
    hide jack with dissolve
    "The man with the plain mask approached us."
    "I scrambled, trying to get away to no avail."
    "He knelt down in front of the crying man and cut the ropes on his arms."
    "The captive wasted no time in getting up and running out into the desert."
    "He did the same with the skinny man, then the woman."
    "The woman seemed to hesitate slightly before she ultimately ran as well."
    "Then he turned to me."
    machete "..."
    if meme_mode:
        "He knelt down and cut my ropes quickly."
        p "Thank you, sir!"
    elif True:
        "I knew he was just going to cut my rope too but I couldn't stop the terror flooding into my body as he got close."
        "At this distance I could see into the eye-holes of his mask."
        "I'd never seen such raw... hatred."
        "He wasn't laughing."
        "As soon as I felt the rope fall away, my body reacted on its own."
    scene black with dissolve
    "I leapt to my feet and ran with every bit of strength I could muster."
    stop music fadeout 1.0
    "I don't know how long I ran for, but eventually the heat and exhaustion won the battle against my terror and I collapsed to the ground." with vpunch
    $ persistent.bgs_seen.add("bg_derek_desert")
    $ renpy.save_persistent()
    scene bg_derek_desert with dissolve
    $ map_location = "Desert"
    $ arrivedby = "special"
    "I heaved and groaned on the coarse sand."
    $ stat_temp += 5
    "It's so hot..."
    "If those psychos don't kill me... this desert probably will."
    "I have to try and think straight and figure out what I'm going to do next."
    "I blinked in the bright sunlight and tried to get my bearings."
    "Aside from sandy nothing... there seemed to be a rocky hill up ahead to my right and a sort of fissure down to my left."
    "... And the camp with those men behind me."

label derek_turn_order:
    $ phase = "event"
    hide screen mini_screen
    hide screen inventory_item
    hide screen status_update_health
    hide screen status_update_sanity
    hide screen status_update_energy
    hide screen status_update_food
    hide screen status_update_temp_increase
    hide screen status_update_temp_decrease
    hide screen notify
    $ hours += 1
    $ total_hours += 1
    $ thirst -= 1
    if location_temp == "hot":
        $ stat_temp += 5
    if location_temp == "xhot":
        $ stat_temp += 10
    if location_temp == "cool":
        if temp >= 60:
            $ stat_temp -= 10
    $ stat_food -= 1
    if wound == 1:
        $ stat_health -= 3
    if wound == 2:
        $ stat_health -= 5
    if sleep > 0:
        $ energy += 3
        if energy >= 24:
            $ energy = 24
            $ sleep = 0
            $ arrivedby = "wakeup"
    elif True:
        if food <= 0 or encumbered == 1:
            $ stat_energy -= 3
        elif True:
            $ stat_energy -= 1
    if grace_period > 0:
        $ grace_period -= 1
    call derek_display_subroutine from _call_derek_display_subroutine_1
    call derek_stat_subroutine from _call_derek_stat_subroutine
    label derek_turn_nostats:
        call derek_event_subroutine from _call_derek_event_subroutine
        $ phase = "adventure"
        $ renpy.pause(hard=True)


label derek_stat_subroutine:
    if health <= 0:
        jump event_derek_death_health
    if temp >= 100:
        jump event_derek_hotdeath
    if thirst <= 0:
        jump event_derek_thirst_death
    if thirst <= 48 and event_derek_thirst_1 == 0:
        $ event_derek_thirst_1 = 1
        jump event_derek_thirst_1
    if thirst <= 24 and event_derek_thirst_2 == 0:
        $ event_derek_thirst_2 = 1
        jump event_derek_thirst_2
    if thirst <= 12 and event_derek_thirst_3 == 0:
        $ event_derek_thirst_3 = 1
        jump event_derek_thirst_3
    if 60 <= temp <= 69 and location_temp == "cool":
        $ event_derek_hot_1 = 0
    if 70 <= temp <= 79 and (location_temp == "xhot") and sleep <= 0 and event_derek_hot_1 == 0:
        jump event_derek_hot_1
    if 70 <= temp <= 79 and location_temp == "cool":
        $ event_derek_hot_2 = 0
    if 80 <= temp <= 89 and (location_temp == "hot" or location_temp == "xhot") and sleep <= 0 and event_derek_hot_2 == 0:
        jump event_derek_hot_2
    if 80 <= temp <= 89 and location_temp == "cool":
        $ event_derek_hot_3 = 0
    if 90 <= temp <= 99 and (location_temp == "hot" or location_temp == "xhot") and sleep <= 0 and event_derek_hot_3 == 0:
        jump event_derek_hot_3
    if sanity <= 30 and event_derek_sanity_1 == 0 and sleep <= 0 and map_location != "Cave" and arrivedby == "new":
        $ event_derek_sanity_1 = 1
        jump event_derek_sanity_1
    if sanity <= 10 and event_derek_sanity_2 == 0 and sleep <= 0:
        $ event_derek_sanity_2 = 1
        jump event_derek_sanity_2
    return

label derek_display_subroutine:
    if sleep > 0:
        scene black with eyedissolve
    elif True:
        if map_location == "Desert":
            window show
            $ persistent.bgs_seen.add("bg_derek_desert")
            $ renpy.save_persistent()
            scene bg_derek_desert with dissolve
        elif map_location == "Fissure":
            window show
            $ persistent.bgs_seen.add("bg_derek_fissure")
            $ renpy.save_persistent()
            scene bg_derek_fissure with dissolve
        elif map_location == "Hill":
            window show
            $ persistent.bgs_seen.add("bg_derek_hill")
            $ renpy.save_persistent()
            scene bg_derek_hill with dissolve
        elif map_location == "Cave":
            $ persistent.bgs_seen.add("bg_derek_cave")
            $ renpy.save_persistent()
            if arrivedby != "idle":
                window show
                scene bg_derek_cave with dissolve
                if rich_location == "Cave":
                    show rich with dissolve:
                        yalign 1.0
                        xalign 0.50
                if tom_location == "Cave":
                    show tom with dissolve:
                        yalign 1.0
                        xalign 0.0
                if jaq_location == "Cave":
                    show jaq with dissolve:
                        yalign 1.0
                        xalign 1.0
        elif map_location == "Camp":
            window show
            $ persistent.bgs_seen.add("bg_derek_camp")
            $ renpy.save_persistent()
            scene bg_derek_camp with dissolve
        elif map_location == "Deep Desert":
            window show
            $ persistent.bgs_seen.add("bg_derek_deepdesert")
            $ renpy.save_persistent()
            scene bg_derek_deepdesert with dissolve
    return




label derek_event_subroutine:

    if total_hours == 16:
        $ derek_location = "Desert"
    elif total_hours == 18:
        $ derek_location = "Desert"
    elif total_hours == 33:
        $ derek_location = "Desert"
    elif total_hours == 34:
        $ derek_location = "Desert"
    elif total_hours == 37:
        $ derek_location = "Desert"
    elif total_hours == 39:
        $ derek_location = "Desert"
    elif total_hours == 57:
        $ derek_location = "Desert"
    elif total_hours == 58:
        $ derek_location = "Desert"
    elif total_hours == 60:
        $ derek_location = "Desert"
    elif total_hours == 62:
        $ derek_location = "Desert"
    elif total_hours == 64:
        $ derek_location = "Desert"
    elif total_hours == 84:
        $ derek_location = "Desert"
    elif total_hours == 85:
        $ derek_location = "Desert"
    elif True:
        $ derek_location = "Camp"

    if derek_location == map_location and grace_period == 0 and derek_location != "Camp":
        jump event_derek_encounter_1

    if map_location == "Camp" and derek_status == "Stabbed" and event_derek_derekvsmachete == 0 and arrivedby == "new" and (hours >= 20 or hours <= 6):
        jump event_derek_derekvsmachete

    if map_location == "Fissure" and 36 <= total_hours <= 42 and event_derek_jack_jaq == 0:
        jump event_derek_jack_jaq

    if energy <= 0:
        label derek_energy_passout:
            $ phase = "event"
            $ arrivedby = "sleep"
            "My vision wavered."
            "I tried to move but I couldn't."
            "I collapsed to the ground. I didn't have the energy to move on."
            "I struggled for a moment longer, then passed out."
            $ sleep = 12
            jump derek_turn_order

    if map_location == "Hill" and event_derek_get_map == 0 and sleep <= 0:
        $ event_derek_get_map = 1
        "I climbed up to the highest part of the hill."
        "A breeze flowed past."
        $ event_derek_map_activation = 1
        $ renpy.notify("Map Added!")
        "I can pretty much see all around..."
        "... No signs of civilization at all."
        "Well, nothing but that little camp I woke up in."
        $ arrivedby = "special"
        jump derek_turn_order

    if map_location == "Cave" and 48 <= total_hours <= 54 and event_derek_save_rich == 0 and arrivedby == "idle" and (tom_location == "Cave" or jaq_location == "Cave"):
        $ event_derek_save_rich = 1
        jump event_derek_save_rich

    if map_location == "Cave" and total_hours >= 60 and event_derek_endgame == 0 and arrivedby == "new" and jaq_location == "Cave":
        $ event_derek_endgame = 1
        jump event_derek_endgame

    if map_location == "Cave" and total_hours >= 60 and event_derek_endgame == 0 and arrivedby == "idle" and jaq_location == "Cave":
        if (tom_location == "Cave" or rich_location == "Cave"):
            "I relaxed and dozed against the wall of the cave for a bit while the others talked amongst themselves."
        elif True:
            "I relaxed and dozed against the wall of the cave for a bit while Jaqueline stared intently at the floor, deep in thought."
        $ event_derek_endgame = 1
        jump event_derek_endgame

    if map_location == "Cave" and total_hours >= 60 and event_derek_endgame == 0 and jaq_location != "Cave" and tom_location == "Cave" and event_derek_tomleave == 0:
        $ event_derek_tomleave = 1
        jump event_derek_tomleave




    if map_location == "Desert":
        if 8 <= hours <= 18:
            $ location_temp = "xhot"
        elif hours == 7 or hours == 19:
            $ location_temp = "hot"
        elif True:
            $ location_temp = "cool"
        if sleep > 1:
            label derek_desert_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump derek_turn_order
        if arrivedby == "wakeup":
            label derek_desert_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                "I looked around myself and remembered where I was."
                if meme_mode:
                    "I spit out a mouthful of sand."
                elif True:
                    "I groggily got back up."
                $ arrivedby = "special"
                jump derek_turn_nostats


        if arrivedby == "new":
            $ arrivedby = "idle"
            if 8 <= hours <= 18:
                "I made it into the open desert... The sun is high and it's boiling hot."
            elif hours == 7:
                "I made it into the open desert... It's already starting to get hot."
            elif hours == 19:
                "I made it into the open desert... It's just starting to cool down."
            elif True:
                "I made it into the open desert."
        elif arrivedby == "idle":
            $ arrivedby = "idle"
            "I stayed in the desert."
        label derek_desert_travel:
            $ phase = "adventure"
            menu:
                "It's really quiet... for now."
                "Stay here" if True:
                    if 8 <= hours <= 18:
                        $ location_temp = "xhot"
                    elif hours == 7 or hours == 19:
                        $ location_temp = "hot"
                    elif True:
                        $ location_temp = "cool"
                    $ map_location = "Desert"
                    $ arrivedby = "idle"
                    jump derek_turn_order
                "Walk towards the camp" if True:
                    if sanity <= 0:
                        jump event_derek_sanity_sequence
                    $ location_temp = "cool"
                    $ map_location = "Camp"
                    $ arrivedby = "new"
                    jump derek_turn_order
                "Walk down to the fissure" if True:
                    if sanity <= 0:
                        jump event_derek_sanity_sequence
                    $ location_temp = "cool"
                    $ map_location = "Fissure"
                    $ arrivedby = "new"
                    jump derek_turn_order
                "Walk up to the hill" if True:
                    if sanity <= 0:
                        jump event_derek_sanity_sequence
                    if 8 <= hours <= 18:
                        $ location_temp = "hot"
                    elif True:
                        $ location_temp = "cool"
                    $ map_location = "Hill"
                    $ arrivedby = "new"
                    play ambient "music/ambient_desert_wind.ogg" fadein 1.0
                    jump derek_turn_order


        return



    if map_location == "Camp":
        $ location_temp = "cool"
        if sleep > 1:
            label derek_camp_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump derek_turn_order
        if arrivedby == "wakeup":
            label derek_camp_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                "I looked around myself and remembered where I was."
                if meme_mode:
                    p "Oh FUCK."
                    p "Damn, why'd I sleep here?"
                elif True:
                    "I groggily got back up."
                $ arrivedby = "special"
                jump derek_turn_nostats

        if 9 <= hours <= 17 and event_derek_first_visit_is_free == 1:
            jump event_derek_campdaydeath

        if (hours <= 5 or hours >= 20) and event_derek_first_visit_is_free == 1 and derek_status != "Dead":
            jump event_derek_campnightdeath

        if arrivedby == "new":
            $ arrivedby = "idle"
            "I've made it into the camp."
            "Somehow, I don't think anyone is here..."
            "I'd better not stay here long."
        elif arrivedby == "idle":
            $ arrivedby = "idle"
            if 8 <= hours <= 18:
                "I stayed in the shade of the camp."
            elif True:
                "I stayed near the camp."
        label derek_camp_travel:
            $ phase = "adventure"
            menu:
                " "
                "Stay here" if True:
                    $ location_temp = "cool"
                    $ map_location = "Camp"
                    $ arrivedby = "idle"
                    jump derek_turn_order
                "Go back into the desert" if True:
                    if sanity <= 0:
                        jump event_derek_sanity_sequence
                    $ event_derek_first_visit_is_free = 1
                    if 8 <= hours <= 18:
                        $ location_temp = "xhot"
                    elif hours == 7 or hours == 19:
                        $ location_temp = "hot"
                    elif True:
                        $ location_temp = "cool"
                    $ map_location = "Desert"
                    $ arrivedby = "new"
                    jump derek_turn_order

        return



    if map_location == "Fissure":
        $ location_temp = "cool"
        if event_derek_jack_countdown >= 3 and 8 <= hours <= 18:
            jump event_derek_jack_fissure

        if sleep > 1:
            label derek_fissure_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump derek_turn_order
        if arrivedby == "wakeup":
            label derek_fissure_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                "I looked around myself and remembered where I was."
                if meme_mode:
                    "Fuck..."
                    "I was hoping I'd at least wake up in Hell this time."
                elif True:
                    "I groggily got back up."
                $ arrivedby = "special"
                jump derek_turn_nostats

        if arrivedby == "new":
            $ arrivedby = "idle"
            "I crawled down into the rocky fissure."
            if 8 <= hours <= 18:
                "I sighed with relief as I slid into a small shaded alcove to get out of the sun."
        elif arrivedby == "idle":
            $ arrivedby = "idle"
            "I stayed in the fissure area."
        label derek_fissure_travel:
            $ phase = "adventure"
            menu:
                " "
                "Stay here" if True:
                    $ event_derek_jack_countdown += 1
                    $ location_temp = "cool"
                    $ map_location = "Fissure"
                    $ arrivedby = "idle"
                    jump derek_turn_order
                "Go to the open desert" if True:
                    if sanity <= 0:
                        jump event_derek_sanity_sequence
                    $ event_derek_jack_countdown = 0
                    if 8 <= hours <= 18:
                        $ location_temp = "xhot"
                    elif hours == 7 or hours == 19:
                        $ location_temp = "hot"
                    elif True:
                        $ location_temp = "cool"
                    $ map_location = "Desert"
                    $ arrivedby = "new"
                    jump derek_turn_order

        return



    if map_location == "Hill":
        if 8 <= hours <= 18:
            $ location_temp = "hot"
        elif True:
            $ location_temp = "cool"
        if sleep > 1:
            label derek_hill_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump derek_turn_order
        if arrivedby == "wakeup":
            label derek_hill_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                "I gasped as I woke up."
                "I looked around myself and remembered where I was."
                if meme_mode:
                    p "AAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!"
                    p "I'm okay."
                elif True:
                    "I groggily got back up."
                $ arrivedby = "special"
                jump derek_turn_nostats

        if arrivedby == "new":
            $ arrivedby = "idle"
            "I hiked up the rocky hill."
            "I can see a bit better from here."
            if 8 <= hours <= 18:
                "There doesn't seem to be a way out of the sun, though."
        elif arrivedby == "idle":
            $ arrivedby = "idle"
            "I stayed up on the hill."
        label derek_hill_travel:
            $ phase = "adventure"
            menu:
                " "
                "Stay here" if True:
                    if 8 <= hours <= 18:
                        $ location_temp = "hot"
                    elif True:
                        $ location_temp = "cool"
                    $ map_location = "Hill"
                    $ arrivedby = "idle"
                    jump derek_turn_order
                "Go to the open desert" if True:
                    if sanity <= 0:
                        jump event_derek_sanity_sequence
                    if 8 <= hours <= 18:
                        $ location_temp = "xhot"
                    elif hours == 7 or hours == 19:
                        $ location_temp = "hot"
                    elif True:
                        $ location_temp = "cool"
                    $ map_location = "Desert"
                    $ arrivedby = "new"
                    play ambient "music/ambient_desert.ogg" fadein 1.0
                    jump derek_turn_order
                "Go into the cave" if event_derek_cave_discovery == 2:
                    $ location_temp = "cool"
                    $ map_location = "Cave"
                    $ arrivedby = "new"
                    play ambient "music/ambient_cave.ogg" fadein 1.0
                    jump derek_turn_order

        return



    if map_location == "Cave":
        $ location_temp = "cool"
        if sleep > 1:
            label derek_cave_sleep:
                $ phase = "event"
                $ arrivedby = "sleep"
                $ renpy.pause(1.0)
                jump derek_turn_order
        if arrivedby == "wakeup":
            label derek_cave_wakingup:
                $ phase = "event"
                $ arrivedby = "wokeup"
                if jaq_location == "Cave":
                    "I gasped as I woke up."
                    jaq "Hey."
                    jaq "Have a good nap?"
                    show jaq normal
                    if meme_mode:
                        p "I had the funniest dream... You were there..."
                        jaq "Pfft."
                    elif True:
                        "I groaned in reply and got back up."
                elif tom_location == "Cave":
                    "I gasped as I woke up."
                    tom "Oh, you're awake!"
                    tom worried "Are you doing okay? I didn't want to disturb you..."
                    if meme_mode:
                        p "Tom, you delicate angel, you could never disturb me."
                        tom wistful "G-geez..."
                    elif True:
                        "I groaned while nodding in reply and got back up."
                elif True:
                    "I gasped as I woke up."
                    "I looked around myself and remembered where I was."
                    if meme_mode:
                        p "Ugh."
                        "I got back up."
                        p "Stinky-ass cave."
                    elif True:
                        "I groggily got back up."
                $ arrivedby = "special"
                jump derek_turn_nostats

        if arrivedby == "new":
            $ arrivedby = "idle"
            "I carefully entered the hidden cave."
            if 8 <= hours <= 18:
                "My eyes adjusted to the darkness."
            if tom_location == "Dead" and jaq_location != "Cave" and jaq_location != "Endcamp":
                "Ugh."
                $ stat_sanity -= 10
                "I tried not to look at the bloody body."
            if tom_location == "Cave":
                tom "Hey again."
                tom worried "{nw}"
        elif arrivedby == "idle":
            $ arrivedby = "idle"
            "I stayed in the cave."
        label derek_cave_travel:
            $ phase = "adventure"
            menu:
                " "
                "Stay here" if True:
                    $ location_temp = "cool"
                    $ map_location = "Cave"
                    $ arrivedby = "idle"
                    jump derek_turn_order
                "Leave the cave" if True:
                    if 8 <= hours <= 18:
                        $ location_temp = "hot"
                    elif True:
                        $ location_temp = "cool"
                    $ map_location = "Hill"
                    $ arrivedby = "new"
                    play ambient "music/ambient_desert_wind.ogg" fadein 1.0
                    jump derek_turn_order
                "Talk to Tom" if tom_location == "Cave":
                    $ location_temp = "cool"
                    $ map_location = "Cave"
                    $ arrivedby = "idle"
                    jump event_derek_talk_tom
                "Talk to Jaqueline" if jaq_location == "Cave":
                    $ location_temp = "cool"
                    $ map_location = "Cave"
                    $ arrivedby = "idle"
                    jump event_derek_talk_jaq
                "Talk to Richard" if rich_location == "Cave" and meme_mode == False:
                    $ location_temp = "cool"
                    $ map_location = "Cave"
                    $ arrivedby = "idle"
                    jump event_derek_talk_rich
                "Talk to Dick" if rich_location == "Cave" and meme_mode:
                    $ location_temp = "cool"
                    $ map_location = "Cave"
                    $ arrivedby = "idle"
                    jump event_derek_talk_rich

        return


label derek_search_subroutine:
    $ phase = "event"
    if map_location == "Camp":
        if event_derek_searchcamp == 0:
            $ event_derek_searchcamp = 1
            "There's some chairs..."
            "A burnt out fire."
            "I looked for weapons, but I couldn't find anything."
            "No food..."
            "I saw a glint of metal."
            "I rushed over behind a chair and saw a couple canteens."
            "My breath hitched."
            "Water!?"
            "I quickly lifted them and checked."
            "Light..."
            "I unscrewed the caps."
            "... Empty."
            "I dropped them."
            "There's nothing here I can use..."
            $ arrivedby = "special"
            jump derek_turn_order
        elif True:
            "There's nothing here I can use..."
            $ arrivedby = "special"
            jump derek_turn_order
    if map_location == "Desert":
        "There doesn't seem to be anything here."
        $ arrivedby = "special"
        jump derek_turn_order
    if map_location == "Hill":
        if tom_location != "Peril":
            "I searched over the sharp rocks."
            "There's nothing useful here at all..."
            $ arrivedby = "special"
            jump derek_turn_order
        elif True:
            if 7 <= hours <= 19:
                if event_derek_cave_discovery == 0:
                    "I searched over the sharp rocks."
                    "There's nothing useful here at all..."
                    $ arrivedby = "special"
                    jump derek_turn_order
                elif True:
                    "I searched where I had found the strange door earlier."
                    "Still here..."
                    jump event_derek_cave_enter_menu
            elif True:
                if event_derek_cave_discovery == 0:
                    "I searched over the sharp rocks."
                    "A strange glow caught my eye."
                    "I carefully walked over to where the ground seemed to be flickering with a soft light."
                    "Upon closer inspection, the hillside was covered by a camouflaged cloth."
                    "I tentatively lifted the cloth."
                    "It's a door..?"
                elif True:
                    "I search for the glow of the door."
                    "It's still here..."
                label event_derek_cave_enter_menu:
                menu:
                    " "
                    "Leave it alone" if True:
                        $ event_derek_cave_discovery = 1
                        "My curiosity was strong..."
                        "But my survival instinct was stronger."
                        "Whatever is in there must have been set up by the masked men."
                        "I'm not messing with that."
                        "I walked away from the door to a safe distance on the hillside."
                        $ arrivedby = "special"
                        jump derek_turn_order
                    "Go inside" if True:
                        $ event_derek_cave_discovery = 2
                        "I have to see what's in here."
                        "There's nothing for me out here anyway."
                        "I gulped and cautiously opened the door just enough to slide in."
                        "I tried to make as little noise as possible."
                        if total_hours < 24:
                            jump event_derek_komodo_ambush
                        elif 24 <= total_hours <= 30:
                            jump event_derek_rescue_tom
                        elif True:
                            jump event_derek_dead_tom

    if map_location == "Cave":
        if event_derek_search_cave == 0:
            if tom_location == "Cave":
                $ event_derek_search_cave = 1
                "I searched around the small cave."
                tom "What are you doing?"
                p "I'm trying to find something useful in here."
                tom "Oh..."
                tom "I've been looking around too and there's nothing in here."
                tom "Except for the candles... and the... drawings on the floor."
                "I looked down."
                "There were weird symbols carved into the floor."
                tom "I'm pretty sure those creeps were trying to summon a demon or something."
                p "Ugh."
                "I sighed, resigning to the fact that there was nothing useful to find."
                $ arrivedby = "special"
                jump derek_turn_order
            elif True:
                $ event_derek_search_cave = 1
                "I searched around the small cave."
                "There were strange drawings in the dirt, and blood dripping all over the floor."
                "The candles had long since burnt out."
                "Aside from that... there's nothing much in here."
                $ arrivedby = "special"
                jump derek_turn_order
        elif True:
            "I searched the cave again."
            "There's nothing in here."
            $ arrivedby = "special"
            jump derek_turn_order
    if map_location == "Fissure":
        if event_derek_search_fissure == 0:
            $ event_derek_search_fissure = 1
            "I searched around myself."
            "Nothing but a dead lizard..."
            if meme_mode:
                menu:
                    "Eat lizard" if True:
                        "I picked up the dried up tiny lizard and stuffed it into my gaping maw."
                        "It was crunchy and somehow a bit chewy."
                        $ stat_food += 1
                        "And it tasted exactly like a dried up dead lizard."
                    "Leave lizard" if True:
                        "Of course I'm not going to eat that."
                        "Why would anyone eat that?"
            $ arrivedby = "special"
            jump derek_turn_order
        elif True:
            if event_derek_search_fissure == 1:
                $ event_derek_search_fissure = 2
                "I kept walking through the recess between the rocks."
                if meme_mode:
                    "Oh fuck yeah! Crevice water!"
                elif True:
                    "Oh- is that?"
                    "A shallow pool of water, barely larger than a puddle."
                    "Water..."
                if tom_name == "Tom":
                    "Wait."
                    "Didn't Tom mention water in the fissure?"
                    "I looked down."
                    "I'm pretty sure he said it was poisoned."
            elif True:
                "I approached the water I found earlier."
            menu:
                " "
                "Drink the water" if meme_mode == False:
                    label event_derek_drink_poison:
                        if map_location == "Cave":
                            jump event_derek_drink_poison_cave
                        elif True:
                            if total_hours < 24:
                                jump event_derek_komodo_sacrifice
                            elif True:
                                jump event_derek_paralyzed_machete
                "Slurp the crevice water" if meme_mode:
                    if map_location == "Cave":
                        jump event_derek_drink_poison_cave
                    elif True:
                        if total_hours < 24:
                            jump event_derek_komodo_sacrifice
                        elif True:
                            jump event_derek_paralyzed_machete
                "Fill canteen" if "item_canteen_empty" in inventory:
                    if tom_name == "Tom":
                        "Maybe it could come in handy for something."
                    elif True:
                        "I should take this now."
                        "I dipped the canteen into the water and filled it."
                    $ inventory.remove("item_canteen_empty")
                    $ inventory.append("item_canteen_poison")
                    $ renpy.notify("Canteen Refilled!")
                    show screen inventory
                    pause(1.5)
                    hide screen inventory
                    "I'm definitely going to need it later."
                    $ arrivedby = "special"
                    jump derek_turn_order
                "Leave it alone" if True:
                    if tom_name == "Tom":
                        "Yeahhh."
                        "Fuck that."
                    elif True:
                        "I looked at the water."
                        if meme_mode:
                            "Maybe it's piss..."
                            "Huh? I started to hear a strange angry whisper in my head."
                            "\"THERE IS NO PISS\""
                            "I must be going crazy out here from the sun..."
                        "Maybe I shouldn't just be drinking any stagnant water I find around."
                        "I'll just survive without it for now..."
                        "I can always come back."
                    $ arrivedby = "special"
                    jump derek_turn_order




label event_derek_hot_1:
    $ phase = "event"
    $ event_derek_hot_1 = 1
    "I wiped the sweat from my brow."
    "It's so hot... and dry."
    "I gulped and tried to ignore the sting of the sun."
    $ arrivedby = "special"
    jump derek_turn_nostats

label event_derek_hot_2:
    $ phase = "event"
    $ event_derek_hot_2 = 1
    "I stumbled slightly."
    "The heat felt like it was coming in waves."
    $ stat_sanity -= 5
    "The wavering horizon was beginning to make me feel sick."
    $ arrivedby = "special"
    jump derek_turn_nostats

label event_derek_hot_3:
    $ phase = "event"
    $ event_derek_hot_3 = 1
    "I fell to my knees."
    "I feel sick..."
    $ stat_sanity -= 10
    "My head hurts... everything is spinning."
    "I can hardly move anymore."
    "I struggled to get back to my feet, swaying dizzily."
    "If I don't get out of the sun..."
    $ arrivedby = "special"
    jump derek_turn_nostats

label event_derek_drink_water:
    $ phase = "event"
    "I opened the canteen and took a precautionary sniff."
    if meme_mode:
        "It doesn't smell like water..."
        "It smells familiar."
        $ stat_food += 10
        $ remaining_temp = temp - 50
        $ thirst += 12
        $ stat_temp -= remaining_temp
        $ inventory.remove("item_canteen_full")
        $ inventory.append("item_canteen_empty")
        "I took a sip."
        p "Ugh!"
        "It's warm milk..."
        p "Welp. Beggars can't be choosers."
        "I drank the rest."
    elif True:
        "It smells okay..."
        "And I really can't afford to be picky out here."
        $ stat_food += 10
        $ remaining_temp = temp - 50
        $ thirst += 12
        $ stat_temp -= remaining_temp
        $ inventory.remove("item_canteen_full")
        $ inventory.append("item_canteen_empty")
        "I started with a sip and soon found myself gulping."
        "I was so thirsty..."
        "It was empty too soon."
    if map_location == "Deep Desert":
        "It... didn't help at all."
        "I don't feel better."
        if achievement.has("ach_doomed_drink") != True:
            $ persistent.ach_doomed_drink = True
            $ achievement.grant("ach_doomed_drink")
            init:
                $ achievement.register("ach_doomed_drink")
                $ achievement.sync()
                $ renpy.save_persistent()
                if persistent.ach_doomed_drink == True and achievement.has("ach_doomed_drink") != True:
                    $ achievement.grant("ach_doomed_drink")
                    $ achievement.register("ach_doomed_drink")
                    $ achievement.sync()
        jump event_derek_sanity_sequence_4_water
    "Well... I feel a lot better anyway."
    $ arrivedby = "special"
    jump derek_turn_nostats

label event_derek_plant_poison:
    $ phase = "event"
    "I pulled out my canteen."
    "I stooped over the empty canteens in the shade."
    $ inventory.remove("item_canteen_poison")
    $ renpy.notify("Canteen Dropped!")
    $ event_derek_poison_planted = 1
    "And I dropped mine with the others."
    "Maybe one of these fuckers will drink it."
    $ arrivedby = "special"
    jump derek_turn_nostats

label event_derek_encounter_1:
    $ phase = "event"
    $ grace_period = 3
    if event_derek_encounter_1 == 0:
        if arrivedby == "sleep" or arrivedby == "wakeup":
            $ sleep = 0
            call derek_display_subroutine from _call_derek_display_subroutine_2
            "I snapped awake."
            "What... was that?"
        play sound "music/sfx_atv_motor_far.ogg"
        "I heard something..."
        "The distant high-pitched motor of some kind of vehicle."
        "That can't be good."
        menu:
            " "
            "Run" if True:
                play sound "music/sfx_atv_motor.ogg"
                "I'm not staying here to find out what or who that is."
                "I ran as fast as I could down towards the fissure."
                $ grace_period = 3
                $ location_temp = "cool"
                $ map_location = "Fissure"
                $ arrivedby = "new"
                jump derek_turn_order
            "Hide" if True:
                $ event_derek_encounter_1 = 1
                $ grace_period = 3
                "There's no time to run..."
                play sound "music/sfx_atv_motor.ogg"
                "I got down low to the ground and tried to be as still and quiet as possible."
                "As the motor drew closer, I began to hear more sounds."
                "Terrified yelps and mocking laughter."
                "I peeked out towards the cacophony."
                "It was the skinny guy... and one of the psychos on a quad bike chasing him."
                "I gasped as the running man turned directly toward me."
                "Did he see me!?"
                "Shit shit... there's no time to think!"
                "The thudding and yelling closed in on my position instantly and for a long second, the running man looked into my eyes."
                rich scared "H-hey!! There's someone hiding here!"
                if meme_mode:
                    p "What the FUCK {i}Richard!{/i}"
                elif True:
                    p "What the fuck!"
                "I got up to my knees in time to see his pursuer heading straight for me."
                "I got up and sprinted."
                "The running man split off from me."
                play sound "music/sfx_atv_motor.ogg"
                "I looked behind to see which target the bike was chasing."
                "It's me..."
                play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
                "I turned ahead too late to stop myself from tripping over a dry bush." with vpunch
                play sound "music/sfx_atv_approach_stop.ogg"
                "I barely had time to register the pain of the fall before four wheels skidded to a stop right next to me."
                d "Hahaha!"
                $ persistent.cgs_derek.add("cg_derek_quadbat")
                $ renpy.save_persistent()
                scene cg_derek_quadbat with dissolve
                play music "music/dereks_theme.ogg" fadein 1.0
                "He got off the bike, lazily swinging a metal bat."
                d empty "He sold you out!"
                d empty "How does that make you feel?"
                "I tried to scramble away from him."
                d empty "Hey!"
                $ stat_health -= 3
                play sound "music/sfx_impact_bat.ogg"
                "I cried out sharply as he slammed the bat down on my leg." with vpunch
                d empty "I asked you a question!"
                menu:
                    " "
                    "Angry" if True:
                        p "Mad! God damn it!"
                        "He barked another laugh."
                        d empty "Yeah... I bet you are..."
                    "Scared" if True:
                        p "I... I don't know!"
                        d empty "Awww... too scared to be mad?"
                    "Say nothing" if True:
                        d empty "..."
                        "He raised the bat again."
                        p "Wait!"
                        $ stat_health -= 5
                        play sound "music/sfx_impact_bat.ogg"
                        "I screamed as he ignored my protest and bludgeoned my other leg." with vpunch
                        d empty "Go ahead and challenge me..."
                        d empty "I'm {i}very{/i} good at getting what I want."
                "He stepped closer to me."
                d empty "I knew we'd meet again, you know."
                d empty "In fact I'm glad I found you instead."
                d empty "You..."
                "I tried to move back as I saw him raise the bat again."
                $ stat_health -= 10
                scene black
                play sound "music/sfx_impact_bat.ogg"
                queue sound "music/sfx_ears_ring.ogg"
                "Pain and sound exploded from the side of my head as I was knocked into the dirt." with hpunch
                "Everything's... ringing..."
                "I tasted blood."
                d high "Belong to me."
                $ persistent.cgs_derek.add("cg_derek_crouchknife")
                $ renpy.save_persistent()
                scene cg_derek_crouchknife with eyedissolve_reverse
                "I looked back up to see he was crouched over me, his bat replaced with a large knife."
                d empty "I could kill you right now, if I wanted to."
                d empty "But..."
                d empty "I've been waiting a really long time to have this kind of fun."
                "He gripped my chin and forced me to look right at him."
                d empty "I've got a little deal for you, so listen up."
                d empty "It's a special deal. Just for you, since you're mine."
                d empty "You do as I say, {i}exactly as I say{/i}, and I'll let you go."
                d empty "You can run around in the sand again."
                d empty "But if you fuck it up, I'll just finish you off and go find that other guy again."
                d empty "So... what's it gonna be?"
                menu:
                    " "
                    "Refuse" if True:
                        p "Fuck you!"
                        p "You'd just kill me any-"
                        $ stat_health -= 10
                        scene cg_derek_crouchknife_angry
                        play sound "music/sfx_knife_stab.ogg"
                        "He quickly flipped the knife in his hand and drove it into my shoulder." with vpunch
                        p "AAAHHHHHH!"
                        d empty "{i}Really{/i} poor decision making on your part."
                        "I stifled another cry of pain as he slid the knife back out of my body."
                        d empty "I'm gonna get what I want whether you cooperate or not."
                        $ stat_health -= 3
                        "He gripped my head and sliced the blade through my cheek."
                        "I couldn't fight the urge to cry out again."
                        "I could feel hot blood dripping from my face and shoulder."
                        "My head was still throbbing."
                        d empty "Cry."
                        "I bit my tongue."
                        "I'm not going to cry for this asshole."
                        "He dropped my head roughly and raised the knife over my legs."
                        d empty "Beg for me... come on."
                        "I was shaking."
                        d empty "DO IT!!!"
                        menu:
                            " "
                            "Beg" if True:
                                "I couldn't hold it anymore."
                                p "P... Please stop..."
                                $ stat_sanity -= 10
                                "Once the tears broke through, I began to shake and cry more."
                                p "Please don't hurt me anymore."
                                scene cg_derek_crouchknife with dissolve
                                d empty "Ahh..."
                                d empty "I knew you'd break..."
                                $ stat_health -= 10
                                $ wound = 2
                                play sound "music/sfx_knife_stab.ogg"
                                "I screamed in surprise and pain as he stabbed the knife deep into my thigh." with vpunch
                                $ renpy.notify("You are gravely wounded.")
                                "I started choking on sobs as he tore the knife back out."
                                if sexcontent != "no":
                                    d empty "Ughh... Fuck."
                                    $ persistent.cgs_derek_sex.add("cg_derek_missionary")
                                    $ renpy.save_persistent()
                                    if sexcontent == "yes":
                                        scene cg_derek_missionary with dissolve
                                    "He quickly grabbed me and pushed me flat on my back."
                                    "My bloody wounds stung from the contact with the ground and I cried more."
                                    "I immediately tensed up as I felt him yank my underwear down."
                                    p "W-what!? Stop!"
                                    "I tried to move but he shoved me back down."
                                    "His weight was on top of me quickly."
                                    "I yelped as I felt his fingers between my legs."
                                    p "No no no!"
                                    "He pushed them inside, invading me roughly and quickly as he started breathing harder."
                                    "I writhed, trying to buck him off, but I was still so weak from the blow to the head."
                                    "I felt him position himself, still for just a second."
                                    "I screamed involuntarily as he pushed himself inside as roughly and quickly as he could."
                                    d empty "Aghnnn..."
                                    "I felt his hand wrap around my throat."
                                    d empty "Keep crying..."
                                    "I barely registered his command."
                                    "It meant nothing, as I was sobbing in pain already."
                                    "I could feel the tears running down my face and neck as his thrusts jerked my body."
                                    "He was panting hard as I was just fighting to breathe."
                                    "His grip loosened slightly as he focused more on my bloody body."
                                    "As I took a large gasp of air which was inevitably spent on another miserable wail, he slammed into me harder than before."
                                    "He moaned as he clutched my neck harder."
                                    scene black with eyedissolve
                                    "I tried not to think about anything inside of me as he finished."
                                    "Finally, he was pulling himself off me."
                                    call derek_display_subroutine from _call_derek_display_subroutine_3
                                    "I immediately grabbed at my underwear to pull them back on."
                                    "As if that would help somehow."
                                    "I heard him zip up, but I kept my head down."
                                    $ stat_health -= 2
                                    scene black
                                    play sound "music/sfx_impact_thud.ogg"
                                    "Without warning, he kicked me swiftly in the gut." with hpunch
                                    "I curled in pain but couldn't seem to breathe."
                                    call derek_display_subroutine from _call_derek_display_subroutine_4
                                    show derek with dissolve
                                    d smug "I told you I'd get what I want."
                                    hide derek with dissolve
                                    "I kept gasping for air as he got back on his bike."
                                    play sound "music/sfx_atv_motor.ogg"
                                    "The motor roared back to life."
                                    d mocking "Let's see who finds you next!"
                                    stop music fadeout 1.0
                                    "The bike skidded and turned, throwing rocks over me."
                                    "I finally managed to gasp and start coughing."
                                    "Everything hurts... and I'm bleeding..."
                                    $ arrivedby = "special"
                                    jump derek_turn_nostats
                                elif True:
                                    d empty "Hahaha!"
                                    call derek_display_subroutine from _call_derek_display_subroutine_5
                                    show derek with dissolve
                                    "He finally got off of me and stood up."
                                    d "Ah... fuck, that's good."
                                    $ stat_health -= 2
                                    play sound "music/sfx_impact_thud.ogg"
                                    "Without warning, he kicked me swiftly in the gut." with hpunch
                                    "I curled in pain but couldn't seem to breathe."
                                    d mocking "I told you I'd get what I want."
                                    hide derek with dissolve
                                    "I kept gasping for air as he got back on his bike."
                                    play sound "music/sfx_atv_motor.ogg"
                                    "The motor roared back to life."
                                    d high "Let's see who finds you next!"
                                    stop music fadeout 1.0
                                    "The bike skidded and turned, throwing rocks over me."
                                    "I finally managed to gasp and start coughing."
                                    "Everything hurts... and I'm bleeding..."
                                    $ arrivedby = "special"
                                    jump derek_turn_nostats
                            "Keep refusing" if True:
                                "I looked down to the ground and kept my mouth shut."
                                "I'm probably going to die out here."
                                "And something tells me that crying is going to make everything worse with this guy."
                                if meme_mode:
                                    d empty "So... no head?"
                                elif True:
                                    d empty "You..."
                                "I looked at him defiantly."
                                d empty "Rraagh!"
                                $ stat_health -= 10
                                $ persistent.cgs_derek.add("cg_derek_angrystab")
                                $ renpy.save_persistent()
                                scene cg_derek_angrystab with dissolve
                                play sound "music/sfx_knife_stab.ogg"
                                "He instantly lunged at me with the knife, plunging it into my thigh as I tried to back out of the way." with vpunch
                                p "AHHHHH!"
                                $ stat_health -= 10
                                play sound "music/sfx_knife_stab.ogg"
                                "He ripped the knife out and stabbed it back in, sending a lightning bolt of pain through my body from my gut." with vpunch
                                $ stat_health -= 10
                                play sound "music/sfx_knife_stab_repeated.ogg"
                                "I screamed as he kept wildly stabbing, again and again." with vpunch
                                d empty "I told you to fucking CRY, you little bitch!"
                                $ stat_health -= 20
                                "My screaming became gurgling as blood filled my lungs."
                                d empty "Ha... heh..."
                                "He was wiping my blood on his face."
                                d empty "Should have done what you were told."
                                scene black with eyedissolve
                                hide screen effect_health
                                hide screen effect_ice
                                "I couldn't feel it as much anymore."
                                if sexcontent != "no":
                                    d angry "I'm gonna fuck your corpse and leave it out here!!!"
                                elif True:
                                    "I could hear him shouting something, but everything sounded so far away."
                                $ quick_menu = False
                                stop music fadeout 1.0
                                stop ambient fadeout 1.0
                                pause 1.0
                                window hide
                                hide screen status
                                $ persistent.endings_derek.add("You refused to cry")
                                $ persistent.deathcounter += 1
                                $ renpy.save_persistent()
                                call achievement_checker from _call_achievement_checker_30
                                play music "<from 0.3>music/you_died.ogg"
                                scene bg_endslate with blooddissolve
                                show screen bg_endslate_text("You Died","You refused to cry")
                                $ renpy.pause(hard=True)
                    "Accept" if True:
                        p "I'll do what you want!"
                        "I want to live, dammit..."
                        "I can swallow my pride."
                        "He stood up and flashed the knife."
                        d empty "Get up on your knees."
                        $ persistent.cgs_derek.add("cg_derek_favour")
                        $ renpy.save_persistent()
                        scene cg_derek_favour1_dark with Dissolve(0.5)
                        show cg_derek_favour1:
                            alpha 0
                            easein 2.0 alpha 1.0
                        "I gulped and reluctantly obeyed."
                        d empty "Now..."
                        d empty "Stick out your tongue."
                        "I eyed the knife nervously."
                        "My heart was pounding."
                        "If I say no... whatever he'll do would definitely be worse."
                        "I opened my mouth and stuck out my tongue."
                        "He leaned in and placed the knife's blade in my mouth."
                        if pronoun == "he":
                            d empty "Good boy."
                        elif pronoun == "she":
                            d empty "Good girl."
                        elif True:
                            d empty "There you go~"
                        "I scrunched my eyes shut and braced for the pain, but it didn't prepare me."
                        $ stat_health -= 3
                        "He dragged the blade slowly through my tongue."
                        "Pain blossomed and burned from my mouth as it filled with blood."
                        "When the blade was gone I doubled over and groaned from the agony, letting the blood spill from my lips."
                        d empty "Let me see."
                        "I was trembling now."
                        "I raised my head and opened my mouth again."
                        scene cg_derek_favour2 with dissolve
                        d empty "..."
                        "His satisfied smile was making me feel sick."
                        d empty "Hahaha!"
                        d empty "You look good like that."
                        d empty "Not just the blood, but that super pathetic look on your face..."
                        "I quickly looked down."
                        d empty "Ah ah ah. We're not done yet."
                        "I gritted my teeth."
                        "I can't take much more of this..."
                        if sexcontent != "no":
                            if meme_mode:
                                "He leaned back against the quad and started unzipping his pants before undoing his belt."
                                "Why... would anyone do it that way..."
                            elif True:
                                "He leaned back against the quad and started unzipping his pants."
                            $ persistent.cgs_derek_sex.add("cg_derek_favoursex")
                            $ renpy.save_persistent()
                            if sexcontent == "yes":
                                scene cg_derek_favoursex with dissolve
                            "I balked at his display."
                            "He can't be serious."
                            d empty "Come on. You remember the deal..."
                            "He said he'd let me go..."
                            "I could survive this..."
                            "I grimaced as he shamelessly held his cock in front of me."
                            "I have to try, don't I?"
                            "If I want to live?"
                            "I uselessly wiped the blood from my still bleeding mouth and leaned forward."
                            "I'll pretend I'm somewhere else."
                            $ sanity -= 10
                            "I opened my mouth and licked it, inhaling another pained gasp."
                            "Fuck, it HURTS."
                            "He was leaning back still, and apparently enjoying the show."
                            "When I closed my mouth around him, he suddenly grasped the back of my head and shoved me further down."
                            "I gagged from both the invasion and the agonizing pain of the open wound on my tongue."
                            "I could feel him in my throat."
                            "I couldn't make any sound at all, but I could feel tears welling up and falling down my face."
                            "He moaned as I twitched in pain."
                            "He pulled out just enough for me to choke and gasp, before thrusting ruthlessly against my tongue again."
                            "Even without him, my mouth was too full of metallic blood, choking me."
                            "He was using two hands to hold my head, fucking my throat as I cried."
                            "He wasn't letting me breathe..."
                            "Please, just let me pass out..."
                            "His movements grew more violent, snapping me out of my stupor."
                            d empty "Ah... I'm gonna fucking cum down your throat..."
                            "He ground into my face hard, and I could feel his cock pulsing."
                            "He didn't lie. It was too far in my throat to even swallow."
                            call derek_display_subroutine from _call_derek_display_subroutine_6
                            show derek with dissolve
                            "He finally pulled out, leaving me to fall to the ground, gasping for air."
                            "My whole face was throbbing and covered in various fluids."
                            d "... You did a good job~"
                            play sound "music/sfx_metal_drop.ogg"
                            "I flinched as I heard a thud of something hitting the ground next to me."
                            d "Good enough for a reward."
                            "... A canteen?"
                            if meme_mode:
                                d smug "... Enjoy..."
                            elif True:
                                d smug "Have some water to wash that down, haha!"
                            hide derek with dissolve
                            "He got back into the seat of the bike."
                            play sound "music/sfx_atv_motor.ogg"
                            "The motor roared back to life."
                            d mocking "Let's see who finds you next!"
                            stop music fadeout 1.0
                            "The bike dug in and threw rocks up at me as he took off laughing."
                            $ inventory.append("item_canteen_full")
                            $ renpy.notify("Filled Canteen Added!")
                            show screen inventory
                            pause(1.5)
                            hide screen inventory
                            "I grabbed the canteen, and wiped my face again."
                            if meme_mode:
                                "I've definitely had better."
                            elif True:
                                "Well... I'm alive."
                            $ arrivedby = "special"
                            jump derek_turn_nostats
                        elif True:
                            "He leaned back against the quad and tapped his foot on the ground."
                            d empty "Lick my boot."
                            "I looked up at him in disbelief."
                            "His expression made it pretty clear he was serious..."
                            "I looked down as he tapped his foot again."
                            "Fuck..."
                            "I already let him cut my tongue."
                            "I can't stop now."
                            "I lowered myself down to his foot."
                            "I opened my mouth."
                            "It hurts so bad... I don't want to..."
                            $ sanity -= 10
                            "I forced myself down and I dragged my burning tongue over the dirty boot."
                            "I breathed raggedly, the pain was making me gasp."
                            "I made sure I did it slowly and properly. I did not want to have to do it again."
                            "I finally raised my head up, shaking, from the now bloody boot."
                            "He was grinning wildly."
                            d empty "Ahaha! Nice!"
                            d empty "Mmmm... look at your {i}face{/i}..."
                            d empty "You did good."
                            call derek_display_subroutine from _call_derek_display_subroutine_7
                            show derek with dissolve
                            "I flinched as he reached to pull something off the quad."
                            play sound "music/sfx_metal_drop.ogg"
                            "Then threw it on the ground beside me."
                            d "Good enough for a reward."
                            "... A canteen?"
                            d smug "You can have some water to wash the dirt down with."
                            hide derek with dissolve
                            "He got back into the seat of the bike."
                            play sound "music/sfx_atv_motor.ogg"
                            "The motor roared back to life."
                            d mocking "Let's see who finds you next!"
                            stop music fadeout 1.0
                            "The bike dug in and threw rocks up at me as he took off laughing."
                            $ inventory.append("item_canteen_full")
                            $ renpy.notify("Filled Canteen Added!")
                            show screen inventory
                            pause(1.5)
                            hide screen inventory
                            "I grabbed the canteen, somewhat surprised to still be alive."
                            $ arrivedby = "special"
                            jump derek_turn_nostats
    elif True:

        if event_derek_encounter_2 == 0:
            jump event_derek_encounter_2
        elif True:
            $ arrivedby = "special"
            jump derek_turn_nostats

label event_derek_encounter_2:
    $ phase = "event"
    $ event_derek_encounter_2 = 1
    if arrivedby == "sleep" or arrivedby == "wakeup":
        $ sleep = 0
        call derek_display_subroutine from _call_derek_display_subroutine_8
        play sound "music/sfx_atv_motor.ogg"
        "The sound of roaring dragged me out of sleep."
        "Huh?"
    elif True:
        play sound "music/sfx_atv_motor_far.ogg"
        "...Wait."
        "I stilled myself for a moment and listened."
    "An all too familiar motor was roaring closer to me."
    "I scanned the horizon and spotted him approaching."
    "I immediately ducked low..."
    "But I saw him clearly."
    "There's nothing out here. He must have seen me."
    "I looked up and saw the vehicle approaching my exact direction."
    "He definitely saw me."
    "I got back up and started sprinting."
    "No..."
    "I can't outrun him on foot."
    play sound "music/sfx_atv_motor.ogg"
    "The quad motor swelled louder."
    "I kept running, adrenaline taking my body to its limits."
    "Louder."
    $ stat_health -= 3
    $ persistent.cgs_derek.add("cg_derek_sand")
    $ renpy.save_persistent()
    scene cg_derek_sand
    play sound "music/sfx_impact_bat.ogg"
    "His metal bat swept at the back of my knees, sending me sprawling into the sand in front of me." with vpunch
    play sound "music/sfx_rocks.ogg"
    "Sand and rocks sprayed over my body as he ground to a stop."
    play music "music/dereks_theme.ogg" fadein 1.0
    d "Hahaha!"
    d "We meet again..."
    "I tried to get up, but his foot landed on my back and kept me on the ground."
    if wound != 2:
        d mocking "{i}How's your tongue feel?{/i}"
    elif True:
        d mocking "{i}How's your leg feel?{/i}"
    if meme_mode:
        p "Your fucking guyliner looks terrible."
        d angry "NO IT DOESN'T!"
    elif True:
        p "..."
        d normal "Ha!"
    "He moved his foot to my head and pressed it into the dirt."
    d high "You know, I really should thank you though."
    d normal "This has been a great vacation."
    "He dug his heel in a bit to emphasize his words."
    d mocking "You've been fun."
    menu:
        " "
        "Beg" if True:
            "Panic rose through my gut."
            p "Please wait!"
            p "Please!"
            p "Don't kill me..."
            "For a moment, he just stayed still."
            "Then he removed his foot from my head, but before I could feel any sort of relief, he started laughing."
            play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
            "He pushed me onto my back with his foot." with hpunch
            d "You're {i}really{/i} pathetic."
            $ persistent.cgs_derek.add("cg_derek_straddle")
            $ renpy.save_persistent()
            scene cg_derek_straddle1 with dissolve
            "He sauntered over my body and sat down, straddling my waist."
            d empty "And I've done this before."
            d empty "I've watched people die out here."
            "He leaned in closer and spoke near my ear."
            d empty "I mean, everyone breaks eventually..."
            "He let out a derogatory laugh."
            d empty "But this time I barely had to {i}try!{/i}"
            if "item_sacrificial_knife" in inventory:
                $ time = 1.0
                $ timer_range = 1.0
                $ timer_jump = 'event_derek_stabderek_timeout'
                $ timer_button_jump = 'event_derek_stabderek_button'
                $ timer_button_text = 'Use the knife'
                show screen timer_button
                " "
                $ renpy.choice_for_skipping()
                $ renpy.pause(hard=True)
                label event_derek_stabderek_button:
                hide screen timer_button
                $ persistent.cgs_derek.add("cg_derek_stabbed")
                $ renpy.save_persistent()
                stop music
                play sound "music/sfx_knife_stab.ogg"
                scene cg_derek_stabbed at top with vpunch
                pause(1.0)
                "I withdrew the knife and plunged it into him."
                "For a moment that seemed too long, he just stared at me."
                scene cg_derek_stabbed:
                    easein_expo 0.5 yalign 1.0
                "Then we both looked down at the knife I'd taken from the cave- handle deep in the flesh of his gut."
                "I sprung into motion."
                scene black with dissolve
                play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
                "I threw him to the side as he sputtered wordlessly." with hpunch
                "I yanked the knife from him, drawing out a scream that was still tempered with shock."
                call derek_display_subroutine from _call_derek_display_subroutine_9
                show derek stabbed
                with dissolve
                play music "music/ambient_dire_situation.ogg" fadein 1.0
                d "Y-you..."
                if pronoun == "she":
                    d "Fucking... bitch..."
                elif True:
                    d "Piece of shit..."
                if meme_mode:
                    p "You kiss your dad with that mouth?"
                    "He was shaking, unable to answer."
                elif True:
                    "I stared at him with the knife clutched tight in my hand."
                "Still dripping with his blood."
                menu:
                    " "
                    "Kill him" if True:
                        $ derek_status = "Dead"
                        "I can't leave this to chance."
                        scene black with dissolve
                        "While he tried to talk, I stepped forward."
                        play sound "<from 0.0 to 1.0>music/sfx_knife_stab.ogg"
                        stop music
                        "I slashed through his throat with no hesitation." with hpunch
                        "He wasn't even able to scream."
                        $ persistent.cgs_derek.add("cg_derek_throat")
                        scene cg_derek_throat with dissolve
                        $ persistent.derek_killed = True
                        $ renpy.save_persistent()
                        play sound "music/sfx_rocks.ogg"
                        if achievement.has("ach_no_you") != True:
                            $ persistent.ach_no_you = True
                            $ achievement.grant("ach_no_you")
                            init:
                                $ achievement.register("ach_no_you")
                                $ achievement.sync()
                                $ renpy.save_persistent()
                                if persistent.ach_no_you == True and achievement.has("ach_no_you") != True:
                                    $ achievement.grant("ach_no_you")
                                    $ achievement.register("ach_no_you")
                                    $ achievement.sync()
                        call cutthroat_checker from _call_cutthroat_checker_2
                        "I stood motionless as he fell back into the sand."
                        "He didn't move."
                        "I breathed evenly."
                        $ stat_sanity -= 20
                        "It seemed strange that I felt calm."
                        "But... I guess it didn't matter."
                        "He was going to kill me."
                        "I had to do this."
                        "I walked closer and wiped the blade on his clothing."
                        call derek_display_subroutine from _call_derek_display_subroutine_28
                        "Then I looked at the sky and began walking back to open desert."
                        $ arrivedby = "special"
                        jump derek_turn_nostats
                    "Leave him" if True:
                        $ derek_status = "Stabbed"
                        "My hands were shaking."
                        "I looked at the knife."
                        "He... he's bleeding a lot."
                        "I took a step backwards."
                        d deranged "H... Heh..."
                        if meme_mode:
                            d "Gonna stab me?"
                            d "Better make it count."
                            d "Better make it hurt."
                            d "Better kill me in one shot."
                        elif True:
                            d "You'd better fucking... kill me."
                        "I took another step back, further from him."
                        d "If I..."
                        hide derek with dissolve
                        play sound "music/sfx_rocks.ogg"
                        "He seemed to be trying to talk, but he fell forward and groaned in pain instead."
                        scene black with dissolve
                        stop music fadeout 1.0
                        "I turned and started running."
                        "I've incapacitated him."
                        "I got away."
                        "I ran until I was sure he wouldn't be able to see me."
                        "That's enough."
                        "I don't... have to kill anyone."
                        call derek_display_subroutine from _call_derek_display_subroutine_32
                        "Then I looked at the sky and began walking back to open desert."
                        $ arrivedby = "special"
                        jump derek_turn_nostats
            elif True:
                jump event_derek_stabderek_timeout
        "Fight" if True:
            "I struggled and wrenched my head free."
            d angry "Hey!"
            "I scrambled to get to my feet-"
            $ stat_health -= 3
            play sound "music/sfx_impact_thud.ogg"
            "Until the metal bat slammed in the side of my ribs." with hpunch
            "I fell back down."
            $ persistent.cgs_derek.add("cg_derek_bat")
            $ renpy.save_persistent()
            scene cg_derek_bat with dissolve
            "He pushed me onto my back with his foot as I struggled to breathe."
            d empty "Do you think you're going to run away?"
            "He looked at my legs, then back to the bat in his hands."
            p "Wait! NO!"
            $ stat_health -= 10
            play sound "music/sfx_impact_bat.ogg"
            "He slammed the bat down onto my leg with massive force." with vpunch
            "Air found its way into my lungs just to be forced out again in a blood curdling scream."
            "The snap of my bone was audible."
            $ stat_health -= 3
            play sound "music/sfx_impact_bat.ogg"
            "As I tried to grab at my injured leg, he kicked me back down and smashed the bat down onto my wrist." with vpunch
            $ stat_health -= 3
            play sound "music/sfx_impact_thud.ogg"
            "I choked out only half a scream before he did the same to the other arm." with vpunch
            $ persistent.cgs_derek.add("cg_derek_straddle")
            $ renpy.save_persistent()
            scene cg_derek_straddle1 with dissolve
            "He sauntered over my broken body and sat, straddling my waist."
            $ stat_sanity -= 20
            label event_derek_stabderek_timeout:
            d empty "No more running for you..."
            p "W...Why!? Why are you doing this!?"
            "How could anyone do this?"
            "He grabbed my face and looked into my eyes."
            "Something about his eyes betrayed the cocky smile."
            "There was something so cold... It sent a chill through my body."
            d empty "You think everything's gonna turn out okay?"
            d empty "Everything will balance out with some... cosmic scale?"
            "His thumb moved closer to my mouth and I squirmed."
            d empty "Do you think I'm evil?"
            "He didn't wait for an answer to any of these questions."
            d empty "There's no such thing."
            "He pushed his thumb into my mouth."
            menu:
                " "
                "Bite him" if True:
                    scene cg_derek_straddle3
                    play sound "<from 0.0 to 1.0>music/sfx_impact_bone.ogg"
                    "I clamped my teeth down on him as hard as I could." with vpunch
                    "Somewhere in my mind I knew It was over anyway."
                    "But I'm not going out without a fight."
                    "He howled in pain and pulled, trying to get free from my teeth."
                    "When he finally yanked his thumb free, I tasted fresh blood."
                    $ stat_health -= 100
                    scene black
                    play sound "music/sfx_impact_bat.ogg"
                    stop music
                    stop ambient
                    "I managed one satisfied bloody grin before the bat came crashing down on my head." with vpunch
                    $ quick_menu = False
                    window hide
                    hide screen effect_health
                    hide screen effect_ice
                    hide screen status
                    pause 1.0
                    $ persistent.endings_derek.add("He didn't let you run")
                    $ persistent.deathcounter += 1
                    $ renpy.save_persistent()
                    call achievement_checker from _call_achievement_checker_31
                    play music "<from 0.3>music/you_died.ogg"
                    scene bg_endslate with blooddissolve
                    show screen bg_endslate_text("You Died","He didn't let you run")
                    $ renpy.pause(hard=True)
                "Stay still" if True:
                    if wound != 2:
                        "I winced as he pushed his thumb in further, against my cut tongue."
                    elif True:
                        "I winced as he pushed his thumb in further, against my tongue."
                    d empty "Nothing is going to stop me."
                    d empty "There's {i}nothing{/i} here."
                    "Pained sounds escaped me as he pressed into my injured flesh."
                    scene cg_derek_straddle2 with dissolve
                    if sexcontent != "no":
                        d empty "I'm going to buy and fuck and kill whatever I want."
                    elif True:
                        d empty "I'm going to buy and kill whatever I want."
                    d empty "And you..."
                    "I saw the blade of his knife for a split second before it was pressed against my neck."
                    scene cg_derek_straddle1 with dissolve
                    d empty "-are entertainment."
                    $ stat_health -= 100
                    play sound "music/sfx_blood_drip.ogg"
                    "Burning pain poured from my neck into the rest of my body."
                    "I couldn't speak or scream."
                    scene black with dissolve
                    hide screen effect_health
                    hide screen effect_ice
                    stop music fadeout 1.0
                    stop ambient fadeout 1.0
                    "And he didn't look away."
                    pause 1.0
                    $ quick_menu = False
                    window hide
                    hide screen status
                    $ persistent.endings_derek.add("He didn't let you run")
                    $ persistent.deathcounter += 1
                    $ renpy.save_persistent()
                    call achievement_checker from _call_achievement_checker_32
                    play music "<from 0.3>music/you_died.ogg"
                    scene bg_endslate with blooddissolve
                    show screen bg_endslate_text("You Died","He didn't let you run")
                    $ renpy.pause(hard=True)

label event_derek_campnightdeath:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        $ sleep = 0
        call derek_display_subroutine from _call_derek_display_subroutine_10
        "Huh?"
    elif True:
        if arrivedby == "new":
            "I cautiously approached the camp."
            "It doesn't look like anyone is here..."
            "Are they really all gone?"
            "I entered the shaded area."
        elif True:
            pass
    "I heard a footstep and tried to turn around."
    $ stat_health -= 3
    $ persistent.cgs_derek.add("cg_derek_sand")
    $ renpy.save_persistent()
    scene cg_derek_sand_night
    play music "music/dereks_theme.ogg" fadein 1.0
    play sound "music/sfx_impact_bat.ogg"
    "The metallic crack of a metal bat rang through the air as I was sent sprawling." with vpunch
    "I registered the pain only after I hit the ground."
    "I tensed up from the agony that spread out from the back of my legs."
    "Before I could move, a knee landed sharply on my back." with vpunch
    d incredulous1 "Why did you come back HERE?"
    "He grabbed my wrists and wrenched them together behind me."
    d incredulous2 "Are you actually that {i}stupid?{/i}"
    "I heard a quick zip noise and felt the painfully tight binding of a plastic tie."
    p "Wh- I-"
    d normal "Wait wait wait..."
    d mocking "Let me guess."
    d high "You thought you were gonna look through our supplies and find a way out of here, right?"
    d normal "Haha..."
    d "Like we'd just be leaving that shit around!"
    d laughing "AHAHAHA!"
    "His laughter slowly died down as he yanked me by the arm across the sand."
    "I tried to struggle out of his grip, but he just adjusted around my efforts and dumped me a little ways away from the camp."
    $ persistent.cgs_derek.add("cg_derek_fireworks_crouch")
    $ renpy.save_persistent()
    scene cg_derek_fireworks_crouch with dissolve
    "He abruptly flipped me over to face him."
    d empty "I brought the {i}dumbest{/i} one."
    d empty "But don't worry-"
    d empty "I like the dumb ones~"
    scene cg_derek_fireworks_empty with dissolve
    "He stood up and walked back into the camp."
    d "I was planning on saving these for the end, but..."
    d high "What do you say we do some celebrating, just the two of us?"
    "I tried to start moving away, but I couldn't get up fast enough with my hands tied behind my back."
    $ persistent.cgs_derek.add("cg_derek_fireworks_gerb")
    $ renpy.save_persistent()
    scene cg_derek_fireworks_gerb with dissolve
    "He returned and kneeled in front of me."
    "In his hands..."
    "Some kind of little tube?"
    "Confusion quickly changed to fear as I watched him pull out a lighter and start flicking it."
    p "W-what is that!?"
    d empty "It's called a 'gerb'."
    p "Wha-"
    $ stat_health -= 3
    scene white with dissolve
    play ambient "music/sfx_fireworks_sparkler.ogg" fadein 1.0
    "I yelped in surprise and pain as a bright light sent sparks all over my body."
    $ stat_health -= 5
    "My yelp turned into screaming as the screeching explosive threw more and more sparks, burning my skin."
    d laughing "Ahahaha!"
    scene cg_derek_sand_night with Dissolve(2.0)
    stop ambient fadeout 1.0
    "I curled in on myself as the sparks finally died down."
    "My skin..."
    "I couldn't even move my arms to touch my injuries."
    if meme_mode:
        "I coughed."
        p "What... did your dad not let you play with bottle rockets or something?"
        d angry "..."
        d horny "Alright."
    elif True:
        "I whimpered in pain as I saw him moving."
        d normal "Not bad..."
        d high "For a start."
        p "Please..."
    d "Okay, let's make the next one more interesting."
    d mocking "Lay back."
    scene cg_derek_fireworks_empty
    "I gasped as he shoved me backwards onto the sand." with vpunch
    "My arms were tied uncomfortably underneath me."
    d high "How long do you think I can hold this one?"
    p "What? Stop!"
    "What was he grabbing? I couldn't see-"
    d "Come on, how long?"
    p "Let me go!"
    d mocking "Fine, you don't get to place a bet."
    $ persistent.cgs_derek.add("cg_derek_fireworks_drop")
    $ renpy.save_persistent()
    scene cg_derek_fireworks_drop with dissolve
    "He finally came back into view."
    "A long string with fireworks attached all down the sides dangled above me."
    p "W... What..."
    "I saw the flicker of the lighter again and began to panic."
    p "WAIT!"
    "He lit the bottom of the firework."
    scene white with dissolve
    play sound "music/sfx_fireworks_pops.ogg" fadeout 3.0
    "A second later, the bottom tubes began to explode."
    "I cried out and tried to block my body with my legs, despite the awkward position."
    "The small explosions burned my legs and filled my nose with the smell of burning metal."
    "I closed my eyes and choked on a sob that was drowned out by the loud cracks."
    d incredulous1 "Woops..."
    "The rest of the exploding firework fell down onto my torso and face."
    $ stat_health -= 3
    "I screamed as the explosions burned my already damaged body."
    "I writhed and tried to get it off me as Derek howled with laughter."
    scene black with eyedissolve
    "I kept shaking long after the popping stopped."
    d normal "Haha... Wow..."
    d "I didn't think I'd drop it that fast..."
    d high "But you started making those cute noises and I couldn't concentrate."
    d mocking "Honestly, it's {i}your{/i} fault."
    "I have to get away from him..."
    scene cg_derek_sand_night with eyedissolve_reverse
    "I tried turning onto my side and getting to my knees."
    d normal "Ah ah, hey, come on."
    d mocking "We're not done yet."
    "I cried as he grabbed me and turned me back over, scraping my burnt flesh."
    if sexcontent != "no":
        d hornyblush "Oh... Fuck..."
        d "Wait here."
        "I couldn't move if I tried."
        "I sobbed into the sand."
        "Everything hurt so much..."
        "I heard his footsteps and raised my head."
        "I stiffened when I saw what he was carrying."
        "Duct tape... and a ring gag."
        p "No! No no no!"
        "He grabbed my head and pried apart my teeth with careless force."
        "He jammed the metal ring into my mouth, forcing it open."
        "I tried to pull away in vain as he fastened it around my head."
        $ persistent.cgs_derek.add("cg_derek_fireworks_gag1")
        $ renpy.save_persistent()
        scene cg_derek_fireworks_gag1 with dissolve
        "He pulled my shoulders until I was propped up on my knees."
        "I had a pretty good idea what his intention was."
        "However, my expectations were clouded with terrified confusion as he brandished a large knife."
        "I tried to shuffle backwards as he grabbed my underwear."
        "I froze as he easily cut them off me."
        "Modesty was far from my mind- which was much more concerned with trying to figure out {i}why{/i}."
        "Why would he-"
        "Panic exploded again as he produced a firecracker."
        "I tried to yell, to tell him to stop..."
        "But the gag keeping my mouth open only let me make awkward, scared noises."
        "He held my shoulder as his other hand searched between my legs."
        "He looked into my eyes as his fingers violated me."
        "He relished my fear as he pushed the firecracker inside me."
        "I realized with disgust that he was already panting."
        d empty "Let's see who explodes first..."
        "I emphatically shook my head, trying everything to get him to stop."
        "He lit the fuse."
        d empty "Now..."
        $ persistent.cgs_derek_sex.add("cg_derek_fireworks_gag2")
        $ renpy.save_persistent()
        if sexcontent == "yes":
            scene cg_derek_fireworks_gag2 with dissolve
        "He grabbed a fist of my hair and kept my face close as he unzipped."
        "He pulled his cock out and rubbed it on my tear streaked face as I trembled."
        $ stat_health -= 10
        play sound "music/sfx_fireworks_bang.ogg"
        if meme_mode:
            d empty "Fire in the hole!"
        "I screamed through the gag as the firecracker exploded inside me." with vpunch
        d empty "Woah!"
        "He held my shaking, sobbing head against himself as he spoke."
        d empty "I thought that would take longer..."
        "I felt like I was going to pass out from the pain."
        "Blood was running down my legs."
        d empty "Did it hurt..?"
        "He moaned as he pushed the tip of his cock into my pried-open mouth without waiting for any kind of answer."
        "My sobs immediately turned into chokes as he pushed deeper."
        d empty "Ffffuck..."
        "I couldn't move."
        "He held my head tightly with both hands and pushed into my throat as I choked."
        "Pain throbbed from my core."
        "He began to move, thrusting, as I began to lose connection with reality."
        "Pain, fear, and the effort of trying to breathe between his movements was too much."
        "The pulsing got a little further away."
        d empty "Hey!"
        "He shook my head and slapped me."
        "I turned my bleary eyes up at him, which seemed to satisfy him."
        "He moaned over me, drinking in my pain."
        "He pulled my face against him and buried himself deep in my throat."
        "I barely had the strength to gag."
        "I couldn't breathe."
        "He moved only slightly, enough to pleasure himself without pulling out."
        "I couldn't breathe!!!"
        "Some base survival instinct awakened enough energy to make me fight his grip, trying to pull my head away."
        d empty "You can breathe after I cum..."
        scene black with eyedissolve
        "Something inside me seemed to finally break and fade away."
        "Tears rolled down my face as he moaned and bucked."
        "The sounds he made seemed far away again."
        "I didn't seem to register the time between him finally pulling out and my own coughing gasps for air."
        "I fell to the ground, motionless." with vpunch
        scene cg_derek_sand_night with eyedissolve_reverse
        "Was time still passing?"
        d horny "One more thing..."
        d mocking "Open wide..."
        "He shoved something into my mouth, which was still forced open."
        "He pressed duct tape over my open mouth."
        "I didn't fight him."
        d normal "Geez... I really busted you huh?"
        d high "Come on, you can at least TRY to have a little fun."
        "I heard the flick of the lighter one last time as a fuse leading into my mouth was lit."
        stop music fadeout 1.0
        stop ambient fadeout 1.0
        scene black with eyedissolve
        "I closed my eyes."
        "This time, I didn't even hear it explode."
    elif True:
        d horny "Wait here."
        "I couldn't move if I tried."
        "I sobbed into the sand."
        "Everything hurt so much..."
        "I heard his footsteps and raised my head."
        "I stiffened when I saw what he was carrying."
        "Duct tape... and some kind of firecracker."
        "He ripped a piece of tape off the roll."
        "Before I realized what was happening, he grabbed my head and pried apart my teeth with careless force."
        $ persistent.cgs_derek.add("cg_derek_fireworks_gag1")
        $ renpy.save_persistent()
        scene cg_derek_fireworks_gag1 with dissolve
        "He forced the firecracker into my mouth."
        "I tried to spit it out, but he slapped the tape over my mouth."
        "I screamed into the tape."
        "I tried to get away."
        "I couldn't do anything."
        "He held my face and the flick of the lighter filled my eyes."
        "The fuse was lit and I screamed."
        "I screamed my muffled cries and tears rolled down my face."
        "He stood back and laughed."
        stop music fadeout 1.0
        stop ambient fadeout 1.0
        scene black with eyedissolve
        "This time, I didn't even hear it explode."
    $ quick_menu = False
    window hide
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_derek.add("You played with fireworks")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_33
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You played with fireworks")
    $ renpy.pause(hard=True)

label event_derek_campdaydeath:
    $ phase = "event"
    "I slowly approached the small structure in the heat."
    "There's... shade..."
    "I took a step forward."
    "Then something moved."
    play music "music/jacks_theme.ogg"
    jack "Oh?"
    "I flinched as I heard the voice."
    "No! I didn't see anyone!"
    "He stepped into view."
    show jack with dissolve
    jack "You're not the one I brought."
    "As he began to take steps toward me, I instinctively took matching steps backward."
    jack "You don't look like you can run very far at all..."
    "His steps started getting faster."
    "I need to leave, NOW."
    "I turned on my heel as he leaned into a sprint."
    $ map_location = "Desert"
    call derek_display_subroutine from _call_derek_display_subroutine_11
    "I ran away from the camp."
    "I could hear his heavy footfalls behind me."
    "Fuck!"
    "What was I thinking!?"
    "I was already so exhausted..."
    "I gulped and ran harder."
    "My body was pulling from some kind of energy I didn't know about."
    "He's not giving up."
    "I kept running, squeezing my eyes shut and sweating."
    "He's right behind me..."
    play sound "music/sfx_rocks.ogg"
    "A stumble." with vpunch
    "I kept going."
    "I'm slowing down, aren't I?"
    "A hand grasped at my flimsy shirt, brushing it."
    "Panic, and running faster."
    "I have to..."
    "I have to!"
    "Everything hurt, the heat made the air feel thick."
    "How is he still only just behind me?"
    "A hand, swiping at my back again."
    "My brain is screaming to run but my body is beginning to disobey."
    "My legs falter."
    "Another swipe... the same distance."
    $ map_location = "Fissure"
    call derek_display_subroutine from _call_derek_display_subroutine_12
    "He's playing with me."
    "This is a game."
    "The realization comes as my legs crumple under me."
    play sound "music/sfx_impact_thud.ogg"
    "I was driven painfully into the sand by his bodyweight." with vpunch
    "I can't..."
    $ persistent.cgs_derek.add("cg_derek_jack_choke")
    $ renpy.save_persistent()
    scene cg_derek_jack_choke1 with dissolve
    "I'm so dizzy from the heat and running that I barely notice as he turns my limp body over to face him."
    jack empty "Caught you..."
    "I gasped for air, completely unable to get my body to move."
    "His hands wrapped around my neck."
    "No..."
    "His grip tightened, and I tried to fight-"
    "But I could barely lift my arms."
    "He leaned in close."
    jack empty "You're making this really easy for me."
    if meme_mode:
        p "H- How did you even catch me?"
        p "You're a fucking smoker, I can smell it!"
        jack empty "COCAINE!" with vpunch
    "I choked on my last wheeze."
    if meme_mode:
        "Well... that explains that I guess."
    "I couldn't breathe."
    "I grabbed uselessly at his arms."
    "They may as well have been made of rock."
    scene cg_derek_jack_choke2 with dissolve
    "I could only lie there as my lungs pulled again and again at the inside of my chest."
    "His hands kept tightening."
    "No amount of panic could move my body now."
    "I laid there under him as, mercifully, dizziness dulled out the rest of any other sensation."
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene white with dissolve
    "The sun..."
    $ quick_menu = False
    window hide
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_derek.add("You wandered into the camp")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_34
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You wandered into the camp")
    $ renpy.pause(hard=True)

label event_derek_jack_jaq:
    $ phase = "event"
    $ event_derek_jack_jaq = 1
    if arrivedby == "sleep" or arrivedby == "wakeup":
        $ sleep = 0
        call derek_display_subroutine from _call_derek_display_subroutine_13
        "I was jolted awake by the sound of a scream."
    elif True:
        "The dry air was cut with a sharp scream."
    "I instinctively dropped lower, out of sight."
    "The commotion drew closer."
    play music "music/jacks_theme.ogg" fadein 5.0
    jaq angry "Get the fuck away from me!"
    "I heard the scrape and hurried shuffle of rocks nearby."
    "My mind raced as I heard the thump of someone falling to the ground."
    "Two voices were grunting in effort."
    "The urge to look was overwhelming."
    menu:
        " "
        "Peek" if True:
            "I turned around and carefully raised my head up."
            "One of the masked men... and one of the captives."
            "It was clear the man had the upper hand, despite the captive's desperate struggling."
            jack serious "I think you've been running long enough."
            jaq "Eat shit!"
            "I stared in horror as she threw a handful of sand directly at the mask's eye holes."
            "The retaliation was immediate."
            play sound "<from 0.0 to 1.0>music/sfx_impact_thud.ogg"
            "He punched her in the face so savagely that she went limp."
            "He sat up over her and took a canteen from his hip."
            "He took several gulps and looked back down at her."
            if event_derek_poison_planted == 1:
                jump event_derek_jack_poisoned
            "Then I saw the flash of a blade."
            "If I don't do something, he's going to kill her!"
            menu:
                " "
                "Intervene" if True:
                    p "STOP!"
                    "He froze."
                    "The mask slowly turned to me as regret flushed through my body."
                    "The woman under him bucked suddenly, throwing him off."
                    "There was no time to think."
                    p "Over here!"
                    "She ran towards me and I extended my hand."
                    "He lept to his feet."
                    play sound "music/sfx_rocks.ogg"
                    "I pulled her down into the fissure and in front of me."
                    p "RUN!"
                    "She found her footing."
                    "I watched her gain distance for a split second-"
                    $ persistent.cgs_derek.add("cg_derek_sand")
                    $ renpy.save_persistent()
                    scene cg_derek_sand
                    play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
                    "Before I was tackled to the ground." with vpunch
                    "She paused and looked back, clearly pained at my position."
                    p "GO!"
                    "I did feel some relief as I watched her take off in a sprint."
                    $ persistent.cgs_derek.add("cg_derek_jackmask")
                    $ renpy.save_persistent()
                    scene cg_derek_jackmask with dissolve
                    "However it quickly died out as the man on top of me turned me over to face him."
                    if pronoun == "he":
                        jack empty "Look at you, a {i}white knight{/i} in a place like this."
                    elif True:
                        jack empty "You know, I really don't mind the trade."
                    jack empty "See where your altruism's gotten you?"
                    "I have to fight."
                    "There's no other options left."
                    scene black
                    play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
                    "I wrenched out of his grip and lashed out, hitting him in the jaw and sending his mask flying." with vpunch
                    $ persistent.cgs_derek.add("cg_derek_jackknife")
                    $ renpy.save_persistent()
                    scene cg_derek_jackknife with dissolve
                    jack empty "Augh... ha..."
                    jack empty "Is that how you wanna play it?"
                    "He raised his fist, and my blood ran cold as I finally got a good look at his weapon."
                    "Brass knuckles with a blade."
                    scene bg_derek_fissure with hpunch
                    play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
                    "I rolled out of the way a split second before his fist collided with the ground by my head."
                    jack naked "C'MERE!"
                    "I tried to scramble to my feet, but he yanked me back by the collar of the flimsy top."
                    $ stat_health -= 5
                    play sound "music/sfx_knife_stab.ogg"
                    "I instinctively blocked my face, taking a slash with the blade of his weapon to my forearms instead."
                    play sound "music/sfx_rocks.ogg"
                    "I fell backwards." with vpunch
                    $ stat_health -= 15
                    $ persistent.cgs_derek.add("cg_derek_jackknife_pin")
                    $ renpy.save_persistent()
                    scene cg_derek_jackknife_pin
                    play sound "music/sfx_knife_stab.ogg"
                    "I screamed as the same blade pinned my shoulder to the ground." with vpunch
                    "I grasped at his arm, trying to get free as he kept grinding it into my body."
                    jack empty "Quit squirming!"
                    $ stat_health -= 10
                    play sound "music/sfx_gore_2.ogg"
                    "I screamed again as he twisted the knife in my shoulder."
                    $ stat_health -= 5
                    scene black
                    play sound [ "<from 0.0 to 1.0>music/sfx_impact_thud.ogg","music/sfx_ears_ring.ogg" ]
                    "Before I could recover, he tore the knife out and hit me in the side of the head with the metal knuckles." with hpunch
                    "Pain exploded from my head, my ears were ringing."
                    $ persistent.cgs_derek.add("cg_derek_jackknife_close")
                    $ renpy.save_persistent()
                    scene cg_derek_jackknife_close with eyedissolve_reverse
                    "I barely noticed him grab my face at first."
                    jack empty "Now {i}you're{/i} gonna squeal for me."
                    "The blade kept getting closer to my face."
                    "I tried to squirm out, but he held my head with an iron grip."
                    scene black with eyedissolve
                    "Closing my eyes did nothing."
                    "He pressed the blade slowly into my eyelid."
                    $ stat_health -= 10
                    $ stat_sanity -= 50
                    play sound "music/sfx_knife_stab.ogg"
                    "I screamed with everything in my body as it penetrated further, into my eye."
                    "I kept screaming as he pulled it out."
                    "The pain was too much."
                    "I heaved and sobbed."
                    $ stat_health -= 10
                    play sound "music/sfx_gore_1.ogg"
                    "He kept me pinned with one hand as the point of his blade pushed into my gut."
                    "I couldn't stop screaming."
                    "He never moved quickly."
                    $ stat_health -= 10
                    "I wailed as I bled, as the knife kept pushing in."
                    play sound "music/sfx_knife_stab_repeated.ogg"
                    "Again and again."
                    "Until finally, after what felt like an eternity..."
                    "I couldn't scream anymore."
                    hide screen effect_health
                    hide screen effect_ice
                    stop music fadeout 1.0
                    stop ambient fadeout 1.0
                    pause 1.0
                    $ quick_menu = False
                    window hide
                    hide screen status
                    $ persistent.endings_derek.add("You gave your life in exchange")
                    $ persistent.deathcounter += 1
                    $ renpy.save_persistent()
                    call achievement_checker from _call_achievement_checker_35
                    play music "<from 0.3>music/you_died.ogg"
                    scene bg_endslate with blooddissolve
                    show screen bg_endslate_text("You Died","You gave your life in exchange")
                    $ renpy.pause(hard=True)
                "Stay quiet" if True:
                    "I can't!"
                    "I can't fight him now. At this point it's just her... or both of us."
                    jack "Come on."
                    jack normal "Wake up."
                    jaq hurt "Ughn..."
                    jack "That's right..."
                    "He grabbed her hair and then shoved the knife in her face."
                    jack serious "Time for you to squeal for me."
                    "He barely finished talking before he brought the knife down to her lower abdomen and slid it deep into her skin."
                    "I winced as I watched her body arch in agony."
                    "She didn't scream."
                    jack normal "What's that?"
                    jack intense "So much to say before, and now you're suddenly shy?"
                    "He leaned in and twisted the blade."
                    "Her shriek tore through the air."
                    "I couldn't see his face through the mask."
                    "But somehow, from the way he leaned in over her..."
                    "I could tell he was smiling."
                    "I seemed to be frozen. I couldn't stop watching."
                    "He held her down and stabbed her again."
                    "Slowly."
                    "She screamed wordlessly, writhing in vain."
                    $ stat_sanity -= 10
                    "I began to feel sick."
                    "Blood spilled out over the sand and her screams grew weaker."
                    "Something about how easily the knife went in..."
                    $ stat_sanity -= 10
                    "Why are people so soft?"
                    "I began to feel lightheaded."
                    "I can't watch this anymore!"
                    stop music fadeout 5.0
                    "I sank down again, well out of sight."
                    "A slight breeze made me realize that my face was covered in tears."
                    "Fuck..."
                    "I stayed in the fissure, motionless, until I was sure it was over."
                    "Until I was sure he was long gone..."
                    "I wiped my face off."
                    "... I have to get out of here."
                    $ jaq_location = "Dead"
                    $ arrivedby = "special"
                    jump derek_turn_nostats
        "Stay down" if True:
            "I stayed down low in the fissure."
            "Whatever's going on out there..."
            "I'm better off staying out of it."
            jack serious "I think you've been running long enough."
            "I think I recognized that voice."
            "It was one of the masked men..."
            jaq angry "Eat shit!"
            "The other voice..."
            "She sounded exhausted..."
            "I kept still as I heard more shuffling and struggling."
            play sound "<from 0.0 to 1.0>music/sfx_impact_thud.ogg"
            "He grunted angrily- then suddenly the dull thud of someone being hit."
            "Hard."
            "I listened for the woman, but I could only hear him panting."
            "Is... is she..?"
            if event_derek_poison_planted == 1:
                "I couldn't resist the urge to look."
                "I peeked over the ledge and saw him looking down at her."
                jump event_derek_jack_poisoned
            "I resisted the curiosity and kept my head down."
            jack "Come on."
            jack normal "Wake up."
            jaq hurt "Ughn..."
            jack "That's right..."
            "I had a really bad feeling this was going to get a lot worse."
            jack serious "Time for you to squeal for me."
            "I squeezed my eyes shut, but only silence followed."
            jack normal "What's that?"
            jack intense "So much to say before, and now you're suddenly shy?"
            "I jolted as a shriek suddenly tore through the air."
            "I shrank down, trying to be as small and invisible as possible."
            "She kept screaming."
            "I shivered as her cries got weaker."
            "I can't do anything..."
            stop music fadeout 5.0
            "Soon there was silence again."
            "I heard a small amount of shuffling as he got up."
            "It's..."
            "It's definitely over."
            "I stayed until I was certain that he must be gone."
            "... I have to get out of here."
            $ jaq_location = "Dead"
            $ arrivedby = "special"
            jump derek_turn_nostats

label event_derek_jack_poisoned:
    $ phase = "event"
    "I stayed still, watching."
    "I waited for him to move..."
    "Then, I noticed something strange."
    "His chin drooped and he wavered slightly."
    jaq hurt "Ughn..."
    "He didn't seem to notice that she was coming to."
    "She gasped as he suddenly fell to the side."
    "Wait-"
    p "Hey! Come here!"
    "She jolted at the sound of my voice and looked over to the fissure."
    p "Come on! Quick!"
    "She pushed him off herself and scrambled over to me."
    show jaq worried with dissolve
    jaq question "You're one of the people who were tied up, too..."
    p "Yeah."
    p "I think he drank the water I left in the camp..."
    show jaq worried
    "She glanced back at him, then studied my face."
    show jaq question
    p "It... I'm pretty sure it was poisoned."
    p "But that's not important!"
    p "We have to get out of here!"
    show jaq normal
    "It only took her a moment to decide to trust me."
    jaq "Okay."
    jaq question "But where can we go?"
    menu:
        " "
        "\"I don't know...\"" if True:
            stop music fadeout 3.0
            jaq angry "What!?"
            jaq "You don't even have a plan?"
            show jaq worried
            "I stammered as she sighed."
            jaq "Look, if that's the case, we should split up."
            jaq "No offense, but I can hide better by myself."
            "I couldn't really argue with that."
            p "I understand..."
            "She turned to leave the fissure."
            jaq normal "For what it's worth..."
            jaq "Good luck."
            jaq worried "I hope you don't die out there."
            hide jaq with dissolve
            "I watched her climb up the rocks and out of sight."
            "Well... at least she's not dead."
            $ jaq_location = "Wander"
            $ arrivedby = "special"
            jump derek_turn_nostats
        "\"We should stay here.\"" if True:
            stop music fadeout 3.0
            jaq angry "What!?"
            jaq "There's no way I'm staying here."
            show jaq worried
            "I stammered as she sighed."
            jaq "That asshole could get up any time."
            jaq "And he'll know we probably didn't go far."
            jaq "No offense, but I can hide better by myself."
            "I couldn't really argue with that."
            p "I understand..."
            "She turned to leave the fissure."
            jaq normal "For what it's worth..."
            jaq "Good luck."
            jaq worried "I hope you don't die out there."
            hide jaq with dissolve
            "I watched her climb up the rocks and out of sight."
            "Well... at least she's not dead."
            $ jaq_location = "Wander"
            $ arrivedby = "special"
            jump derek_turn_nostats
        "\"I know about a hidden cave.\"" if event_derek_cave_discovery == 2:
            stop music fadeout 3.0
            jaq "What!? Really?"
            show jaq normal
            "I nodded."
            p "I can show you."
            jaq question "Well, what are we waiting for?"
            jaq worried "That asshole could get up any time."
            "I gulped."
            "She's right."
            $ map_location = "Desert"
            call derek_display_subroutine from _call_derek_display_subroutine_14
            "I led her through the desert towards the hill."
            jaq "Stay low... The prick without a mask has been driving around out here."
            if derek_status != "Fine":
                if wound == 2:
                    "I grab my injured leg spitefully."
                elif True:
                    "I ran my injured tongue against my teeth spitefully."
                p "I wouldn't worry about {i}him{/i} anymore."
                "She looked at me with curiousity, but dropped the subject in favour of focusing on getting somewhere safe."
            elif True:
                if wound == 2:
                    "I shuddered and clutched my leg subconsciously."
                elif True:
                    "I shuddered and ran my injured tongue against my teeth subconsciously."
                p "I... I know."
            $ map_location = "Hill"
            play ambient "music/ambient_desert_wind.ogg" fadein 1.0
            call derek_display_subroutine from _call_derek_display_subroutine_15
            "We got up the hill and I showed her the cloth covering the door."
            jaq "Damn..."
            jaq "That IS well hidden."
            "She stopped in front of it."
            jaq "But is it safe..?"
            if tom_location == "Dead":
                p "It's..."
                p "Well I think it's safe for us now."
                "She moved to open the door."
                p "-Wait."
                p "There's uh..."
                p "Well, one of the others didn't make it."
                p "They got him."
                p "... And he's still in there."
                "She looked down for a moment."
                jaq "Well... we don't have much choice either way."
                $ map_location = "Cave"
                $ arrivedby = "new"
                play ambient "music/ambient_cave.ogg" fadein 1.0
                call derek_display_subroutine from _call_derek_display_subroutine_16
                "She opened the door and went down inside."
                "The candles had gone out..."
                "And he was still there."
                jaq sad "Jesus..."
                p "Yeah..."
                jaq sad "Well... we should bury him."
                "I heaved a sigh."
                "She's right."
                "We can't just stay in here with a dead body."
                jaq normal "Come on."
                $ map_location = "Hill"
                play ambient "music/ambient_desert_wind.ogg" fadein 1.0
                call derek_display_subroutine from _call_derek_display_subroutine_17
                "We moved quickly."
                "It didn't take long with two of us."
                "It wasn't a good grave, but he was covered."
                "Dirty and tired, we went back to the cave."
                $ jaq_location = "Cave"
                $ map_location = "Cave"
                $ arrivedby = "new"
                play ambient "music/ambient_cave.ogg" fadein 1.0
                call derek_display_subroutine from _call_derek_display_subroutine_18
                jaq "There..."
                jaq worried "At least we have some place to hide now."
                "I nodded solemnly."
                jaq normal "So... you never even told me your name yet."
                p "Oh!"
                p "I'm [player_name]... what's yours?"
                if player_name.lower() == "derek":
                    jaq question "Oh. Uh..."
                    jaq worried "That's unfortunate."
                    p "I know..."
                    $ jaq_name = "Jaqueline"
                    jaq normal "Anyways, my name is Jaqueline."
                elif True:
                    $ jaq_name = "Jaqueline"
                    jaq "Jaqueline."
                "Somehow, without speaking, we knew there was no room for pleasantries."
                "We looked at each other instead with grim understanding."
                if achievement.has("ach_you_could_use_a_stiff_drink") != True:
                    $ persistent.ach_you_could_use_a_stiff_drink = True
                    $ achievement.grant("ach_you_could_use_a_stiff_drink")
                    init:
                        $ achievement.register("ach_you_could_use_a_stiff_drink")
                        $ achievement.sync()
                        $ renpy.save_persistent()
                        if persistent.ach_you_could_use_a_stiff_drink == True and achievement.has("ach_you_could_use_a_stiff_drink") != True:
                            $ achievement.grant("ach_you_could_use_a_stiff_drink")
                            $ achievement.register("ach_you_could_use_a_stiff_drink")
                            $ achievement.sync()
                $ arrivedby = "special"
                jump derek_turn_nostats
            elif True:
                p "It is."
                p "There's another one of us in there hiding, too."
                jaq surprised "Really?"
                "She quickly opened the door and rushed inside."
                $ map_location = "Cave"
                $ arrivedby = "new"
                play ambient "music/ambient_cave.ogg" fadein 1.0
                call derek_display_subroutine from _call_derek_display_subroutine_19
                tom surprised "Ahh!"
                p "Tom! Tom, it's okay!"
                p "She's one of us."
                tom normal "Oh... my god."
                tom "You gave me a heart attack, just barging in here."
                show jaq with dissolve:
                    xalign 1.0
                    yalign 1.0
                jaq worried "Heh... sorry."
                p "Tom, this is... uh..."
                $ jaq_name = "Jaqueline"
                jaq normal "My name is Jaqueline."
                tom happy "It's nice to meet you, Jaqueline!"
                tom wistful "Err... well, this isn't 'nice', but..."
                jaq worried "I know what you mean."
                show tom normal
                "She turned to me."
                jaq question "What about you?"
                "I realized I hadn't even given her my name yet."
                p "Oh... I'm [player_name]."
                if player_name.lower() == "derek":
                    jaq question "Oh. Uh..."
                    jaq worried "That's unfortunate."
                    p "I know..."
                elif True:
                    show jaq normal
                    "She gave me a quick nod."
                "Somehow, without speaking, we knew there was no room for pleasantries."
                show tom worried
                "We looked at each other instead with grim understanding."
                "She sat down with a soft sigh."
                jaq normal "It is nice to be able to relax for a moment at least."
                "I could tell everyone seemed exhausted."
                "But a little bit of hope fluttered in my chest."
                "Maybe with some of us together..."
                "We can get out of here."
                if achievement.has("ach_you_could_use_a_stiff_drink") != True:
                    $ persistent.ach_you_could_use_a_stiff_drink = True
                    $ achievement.grant("ach_you_could_use_a_stiff_drink")
                    init:
                        $ achievement.register("ach_you_could_use_a_stiff_drink")
                        $ achievement.sync()
                        $ renpy.save_persistent()
                        if persistent.ach_you_could_use_a_stiff_drink == True and achievement.has("ach_you_could_use_a_stiff_drink") != True:
                            $ achievement.grant("ach_you_could_use_a_stiff_drink")
                            $ achievement.register("ach_you_could_use_a_stiff_drink")
                            $ achievement.sync()
                $ jaq_location = "Cave"
                $ arrivedby = "special"
                jump derek_turn_nostats

label event_derek_jack_fissure:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        jack "Well, look here."
        $ sleep = 0
        call derek_display_subroutine from _call_derek_display_subroutine_20
        play music "music/jacks_theme.ogg" fadein 1.0
        show jack with dissolve
        "My eyes snapped open."
    elif True:
        play sound "music/sfx_rocks.ogg"
        "The sound of a few rocks falling was all the warning I had before a figure leapt into the fissure beside me."
        play music "music/jacks_theme.ogg" fadein 1.0
        show jack with dissolve
        jack "Well, look here."
    menu:
        " "
        "Run" if True:
            scene black with dissolve
            "I scrambled backward, fumbling with my footing."
            "Adrenaline surged through my body."
            jack intense "Hey!"
            "I got my bearings and sprinted down the fissure, looking for a way out."
            "I could hear the pounding of his footfalls right behind me."
            "No..."
            play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
            "His weight slammed into me from behind, as sand and sharp rocks ground into me from below." with vpunch
            call derek_display_subroutine from _call_derek_display_subroutine_21
            show jack with dissolve
            "I twisted myself back around to face the man in the mask."
            "I was panting but he seemed barely out of breath."
        "Surrender" if True:
            "I backed up against the wall of the fissure."
            "There's no point in running now..."
    if pronoun == "they":
        jack "Trying to hide in the cracks, cutie?"
    elif pronoun == "she":
        jack "Trying to hide in the cracks, little girl?"
    elif True:
        jack "Trying to hide in the cracks, little boy?"
    "I bit the inside of my lip, trying frantically to find some way out of this."
    jack "You should be {i}glad{/i} I'm the one that found you."
    jack "{i}I won't hurt you{/i}."
    "He was subtly adjusting his position to any direction I looked while he spoke."
    "Keeping me completely cornered."
    menu:
        " "
        "Beg" if True:
            p "Please..."
            p "Let me go!"
            p "I'll do whatever you want!"
            jack "You don't have to do anything now."
            jack "Just relax..."
        "Antagonize" if True:
            p "Fuck off, you dog mask wearing freak!"
            "He stared for a moment."
            "Then let out a coarse laugh."
            jack "I like you."
            jack "And it's a {i}jackal{/i}... can't you tell?"
            if meme_mode:
                p "I don't know, it kind of makes you look like a nekomimi."
                jack "A... a what?"
                p "Like \"Nyah~\""
                jack "What."
                p "You know, like \"N-"
                jack "Shut the fuck up!"
            elif True:
                "Something about the mocking tone in his voice sent a chill down my spine."
        "Stay silent" if True:
            "He bent in closer."
            "He smelled like cigarettes."
            jack "Like a deer in headlights."
            "He scoffed."
            jack "Guess this will be over quick, then."
    "He stepped closer."
    "I have to do something."
    scene black with dissolve
    menu:
        " "
        "Push past him" if True:
            "I mustered my energy and tried to push past him."
            label event_derek_menu_push:
            "I was immediately pulled back by an arm around my waist."
            "As I struggled, he put me in a headlock."
            jack "No no no."
            jack serious "That's not how this goes."
            $ stat_health -= 40
            play sound "music/sfx_knife_stab.ogg"
            "Pain exploded from my side."
            "A hand over my mouth stopped my delayed scream."
        "Attack him" if True:
            "I gathered my courage and lunged for him."
            "I was immediately pulled back by an arm around my waist."
            "I wildly tried to escape his grasp, but it only tightened."
            jack serious "Stop. Squirming."
            play sound "music/sfx_knife_stab.ogg"
            $ stat_health -= 40
            "Pain cut through my body as something sharp was plunged into my side."
            "A hand over my mouth stopped my delayed scream."
        "Use the knife" if "item_sacrificial_knife" in inventory:
            "I grabbed the knife I got from the cave and kept it hidden behind my back."
            "Now!"
            "I lunged forward with the blade."
            "In a single moment, his brass knuckles smashed into my wrist."
            play sound "<from 0.0 to 1.0>music/sfx_knife_drop.ogg"
            "I watched helplessly as my only weapon went sailing into the rocks."
            jump event_derek_menu_push
    $ persistent.cgs_derek.add("cg_derek_jack_knuckles")
    $ renpy.save_persistent()
    scene cg_derek_jack_knuckles
    play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
    "He shoved me back against the wall of the fissure and showed his weapon." with vpunch
    "A short knife attached to brass knuckles."
    "I grasped at the wound in my side, blood already soaking through the flimsy clothing I had been put in."
    p "W-why?"
    "I coughed as he knelt over me and held the blade to my throat."
    if sexcontent == "no":
        jack empty "'Why?' yourself."
        jack empty "I can practically smell your anxiety."
        "He leaned in."
        jack empty "I bet you've spent your whole life being afraid."
        jack empty "And where did that get you, huh?"
    elif True:
        jack empty "'Why?' yourself."
        jack empty "I can practically smell your anxiety."
        "He leaned in, pressing his body up close and speaking low into my ear."
        jack empty "I bet you've spent your whole life being afraid."
        "I tensed up as I realized he was completely hard."
        jack empty "And where did that get you, huh?"
        menu:
            "Push him away" if True:
                p "Augh! Get off of me!"
                "I shoved at him and tried to get away."
                "He scoffed and grabbed me by the arm again."
                jack empty "I don't think so."
            "Stay still" if True:
                "I froze up."
                p "I... I uh..."
                "He was staring at me."
                "Something seemed to change in his demeanor."
                scene cg_derek_sand:
                    zoom 1.5
                    yalign 1.0
                "I gasped as he suddenly grabbed me harshly and threw me onto the ground." with vpunch
                p "Wait!"
                "He got on top of my back and pushed my face into the sand." with vpunch
                jack serious "Shut up."
                "He yanked the thin underwear down and off me so hard that it tore."
                "The unmistakable sound of a zipper caught my attention before I had a chance to be embarassed."
                "I knew exactly what he was doing."
                "He positioned himself quickly with a rustling of leather."
                "I tried to cry out as I felt him push at my entrance, but I was silenced by another shove into the ground." with vpunch
                "It didn't stop me from screaming when he slammed into me with no warning or preparation." with vpunch
                "He held my face down as I kept screaming, it was tearing and burning."
                "He thrusted quickly and violently, more like beating than fucking somehow."
                "I choked as I tried to breathe in a mixture of sand and tears."
                "I vaguely heard a groan above me... Apparently my struggling made him more excited."
                "The pain seemed to numb slightly as he began to move more easily..."
                "I was obviously bleeding."
                "I tried to calm down and breathe, but I was shaking."
                "Then I noticed his pace changing, slowing down."
                "The deliberately slow pace felt worse somehow."
                "I couldn't help but moan in pain."
                "He was leaning closer over me now."
                "I could hear him panting right next to my head."
                "And I could smell cigarettes..."
                "It was too hot, his weight, and the burning pain..."
                "Then he slammed into me, harder than before." with vpunch
                "I cried out in shock as I felt his teeth clamp on my shoulder."
                "He bit down hard, breaking the skin."
                "I hated that I was still sensitive enough to feel him cumming inside me."
                "Then he finally relented, breathing hard behind me."
                "I was barely aware as he got up. I couldn't move."
                "I knew I was a bloody mess."
                jump event_derek_jack_die
    $ stat_health -= 10
    play sound "<from 0.0 to 1.0>music/sfx_impact_bone.ogg"
    "I had no time to react as he readied his metal-clad fist and punched me head on." with vpunch
    "I heard something crunch."
    "I doubled over, groaning in agony as I held my bleeding face."
    "He grabbed my hair and forced my head back up to look at him."
    jack empty "All that time... running away."
    jack empty "You've been acting like the wrong kind of animal."
    jack empty "Human beings are made to kill each other."
    $ stat_health -= 10
    $ persistent.cgs_derek.add("cg_derek_sand")
    $ renpy.save_persistent()
    scene cg_derek_sand
    play sound "music/sfx_impact_thud.ogg"
    "Another blow sent me to ground." with vpunch
    "I can't move..."
    label event_derek_jack_die:
    "Sounds and light began to pulse and fade."
    "He grabbed my head again from behind."
    $ stat_health -= 100
    play sound "music/sfx_knife_stab.ogg"
    "Without another word, he slammed the blade into the side of my neck." with hpunch
    scene black with eyedissolve
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    hide screen effect_health
    hide screen effect_ice
    play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
    "A single pained gurgle escaped me before I was dropped unceremoniously into the dirt."
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_derek.add("You were caught by Jack")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_36
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You were caught by Jack")
    $ renpy.pause(hard=True)

label event_derek_rescue_tom:
    $ phase = "event"
    $ map_location = "Cave"
    $ arrivedby = "new"
    play ambient "music/ambient_cave.ogg" fadein 1.0
    call derek_display_subroutine from _call_derek_display_subroutine_22
    "I carefully stepped through the door and into the cave."
    "I froze at the sound of voices."
    $ dragon_name = "Dragon"
    play music "music/lizards_theme.ogg" fadein 1.0
    komodo "Thanks, Dragon~"
    dragon "Mm."
    komodo "Okay, where's the-"
    $ komodo_name = "Komodo"
    dragon "Komodo."
    $ persistent.cgs_derek.add("cg_derek_helptom")
    $ renpy.save_persistent()
    scene cg_derek_helptom with dissolve
    "One of the other captives was on a dirt 'table' in the middle of the cave."
    "He looked terrified, but he wasn't moving."
    "I watched silently as one of them brandished a knife."
    "Oh no..."
    menu:
        " "
        "Intervene" if True:
            p "Stop!"
            call derek_display_subroutine from _call_derek_display_subroutine_23
            show dragon:
                yalign 1.0
                xalign 0.30
                alpha 0
                easein 0.5 alpha 1 xalign 0.25
            show komodo:
                yalign 1.0
                xalign 0.70
                alpha 0
                easein 0.5 alpha 1 xalign 0.75
            "Both lizard masks turned to me."
            "Oh God, what have I done..."
            label event_derek_savetom_timeout:
            scene black with dissolve
            "The large man with the knife barrelled at me."
            "There was no room to dodge."
            $ stat_health -= 50
            $ persistent.cgs_derek.add("cg_derek_dragonstab")
            $ renpy.save_persistent()
            scene cg_derek_dragonstab
            play sound "<from 0.0 to 1.0>music/sfx_impact_bone.ogg"
            "I screamed as the knife plunged into my chest." with vpunch
            "His weight easily crushed me against the dirt."
            "I was completely pinned down."
            "He turned and looked back at his companion."
            komodo empty "Just kill [pp_obj]."
            komodo empty "We already started with the other one."
            "The man pinning me down nodded."
            p "Wait! WAIT!"
            $ stat_health -= 50
            play sound "music/sfx_gore_2.ogg"
            "He grabbed my face and I felt the jagged blade tear through my throat."
            "As I tried to scream, blood came from my neck and mouth."
            "I struggled against him for a few long seconds as he held me tight."
            scene black with eyedissolve
            stop music fadeout 1.0
            stop ambient fadeout 1.0
            "Until I couldn't move anymore."
            $ quick_menu = False
            window hide
            hide screen effect_health
            hide screen effect_ice
            hide screen status
            $ persistent.endings_derek.add("You tried to be a hero")
            $ persistent.deathcounter += 1
            $ renpy.save_persistent()
            call achievement_checker from _call_achievement_checker_37
            play music "<from 0.3>music/you_died.ogg"
            scene bg_endslate with blooddissolve
            show screen bg_endslate_text("You Died","You tried to be a hero")
            $ renpy.pause(hard=True)
        "Wait" if True:
            "I held still."
            "I have to be careful about this."
            "I looked at the captive again."
            "He wasn't tied down at all."
            "They must have done something to him..."
            "I don't think I can count on him helping."
            "The two masked men were concentrating on the captive in the middle."
            "They were muttering over him..."
            "I held in a gasp as I watched one of them cut their victim."
            "He didn't make a sound..?"
            "He must be paralyzed..."
            "But his eyes were wide open, tears flowing down his face."
            "I have to do something..."
            "The two in masks prodded at their victim while talking quietly."
            "He's not screaming..."
            "I don't think he can."
            "I was sure they must be able to hear my breathing, but they were deeply concentrating on their task."
            komodo empty "What do you think, then?"
            "What do I do!?"
            dragon empty "Just don't mess around with the center yet."
            dragon empty "You have to go slowly."
            "I watched in horror as the glinting blade was brought closer to the innocent man's body."
            "They're gonna kill him!!!"
            play sound "music/sfx_rocks.ogg"
            "The tension in my legs caused my foot to shift." with vpunch
            call derek_display_subroutine from _call_derek_display_subroutine_24
            show dragon:
                yalign 1.0
                xalign 0.30
                alpha 0
                easein 0.5 alpha 1 xalign 0.25
            show komodo:
                yalign 1.0
                xalign 0.70
                alpha 0
                easein 0.5 alpha 1 xalign 0.75
            $ time = 1.0
            $ timer_range = 1.0
            $ timer_jump = 'event_derek_savetom_timeout'
            $ timer_button_jump = 'event_derek_savetom_button'
            $ timer_button_text = 'Grab Komodo'
            show screen timer_button
            "Shit!"
            $ renpy.choice_for_skipping()
            $ renpy.pause(hard=True)
            label event_derek_savetom_button:
            hide screen timer_button
            scene black with dissolve
            "The large man with the knife barrelled at me."
            "I grabbed the slender one and whipped him in front of my body."
            $ persistent.cgs_derek.add("cg_derek_loveanddeath")
            $ renpy.save_persistent()
            play sound "<from 0.0 to 1.0>music/sfx_impact_bone.ogg"
            scene cg_derek_loveanddeath
            "We both fell backwards under the force of Dragon's attack." with vpunch
            "D-did he..?"
            dragon empty "..."
            dragon empty "No no no no no..."
            $ komodo_name = "Mike"
            scene black with dissolve
            dragon scared "MIKE!"
            play sound "<from 0.0 to 1.0>music/sfx_knife_drop.ogg"
            "He dropped the knife and grabbed the other masked man's face."
            "I squirmed out from under him... He didn't seem to be paying any attention to me at all."
            $ persistent.cgs_derek.add("cg_derek_loveanddeath2")
            $ renpy.save_persistent()
            scene cg_derek_loveanddeath2 with dissolve
            dragon empty "Please..."
            "The injured man coughed."
            "He'd been stabbed right in the chest."
            $ dragon_name = "Jace"
            komodo empty "J... Jace, it's okay."
            komodo empty "You didn't mean to."
            komodo empty "I know you didn't mean to."
            "I tore my eyes away from the bizarre scene to search the floor."
            "The knife..."
            "I bent down and grabbed it."
            "Neither one of them noticed me."
            "I held the bloody knife up."
            "There's no way out of this cave but through them."
            "I think the big one is crying..."
            menu:
                " "
                "Stab him in the back" if True:
                    label dragon_stabbed:
                    "He's distracted."
                    "I'm never getting another chance like this."
                    $ stat_sanity -= 10
                    scene black with dissolve
                    play sound "<from 0.0 to 1.0>music/sfx_knife_stab.ogg"
                    "I plunged the blade into his back, burying it completely in his flesh." with vpunch
                    "He roared in pain, but he didn't turn around."
                    $ stat_sanity -= 5
                    play sound "<from 0.3 to 1.0>music/sfx_knife_stab_repeated.ogg"
                    "I wrenched the hooked blade out of him and stabbed again." with vpunch
                    if meme_mode:
                        p "What? Nothing to say now?"
                        p "I thought you guys loved pain. {noalt}:3c{/noalt}"
                    elif True:
                        "I'm not taking any chances!"
                    stop music fadeout 5.0
                    "I held the knife down in him, over the two bodies."
                    "I realized I was shaking and panting."
                    "Neither of them were breathing anymore..."
                    "I don't know how long I stayed like that... until a soft groan of pain caught my attention."
                    label event_derek_dragonkilled:
                    call derek_display_subroutine from _call_derek_display_subroutine_25
                    "The captive!"
                    "I pulled the blade out, unwilling to let it go- and I rushed to the side of the table with the bleeding victim."
                    "He seemed to be able to move slightly."
                    p "They... I got them."
                    if achievement.has("ach_interrupted_intimacy") != True:
                        $ persistent.ach_interrupted_intimacy = True
                        $ achievement.grant("ach_interrupted_intimacy")
                        init:
                            $ achievement.register("ach_interrupted_intimacy")
                            $ achievement.sync()
                            $ renpy.save_persistent()
                            if persistent.ach_interrupted_intimacy == True and achievement.has("ach_interrupted_intimacy") != True:
                                $ achievement.grant("ach_interrupted_intimacy")
                                $ achievement.register("ach_interrupted_intimacy")
                                $ achievement.sync()
                    p "You're okay now."
                    "I could see the relief wash over him."
                    "He's bloody... but I don't think they injured him too badly."
                    "We both stayed silent for a few minutes as we tried to process what had just happened."
                    p "I uh..."
                    p "I'm gonna move those bodies."
                    p "I'll be right back."
                    $ map_location = "Hill"
                    play ambient "music/ambient_desert_wind.ogg" fadein 1.0
                    call derek_display_subroutine from _call_derek_display_subroutine_26
                    "I push the door open and smelled the fresh air."
                    "Then I took the next couple of hours to drag the bodies out of the cave and cover them with sand and rocks."
                    "I wasn't really too concerned about giving them a 'burial'..."
                    "But this cave is the safest place I can think of right now and I don't want to share it with dead bodies."
                    "It was a fair bit of labour, but I think it was worth it."
                    "I dusted off my hands and cautiously went back into the cave."
                    $ map_location = "Cave"
                    $ arrivedby = "new"
                    play ambient "music/ambient_cave.ogg" fadein 1.0
                    call derek_display_subroutine from _call_derek_display_subroutine_27
                    $ hours += 3
                    $ total_hours += 3
                    p "Hello..?"
                    tom "... Hi."
                    show tom worried with dissolve
                    "I looked and saw that he had managed to get up."
                    p "You can move again!"
                    tom normal "Ah... barely."
                    tom "There was water in the fissure."
                    tom worried "I think they poisoned it..."
                    if "item_canteen_poison" in inventory:
                        "I immediately remembered refilling my canteen."
                        "... I'd better not drink that."
                    p "Well... it looks like it's wearing off."
                    p "So that's something."
                    "He looked down at the floor."
                    tom "What should we do..?"
                    "I looked around."
                    p "You're probably still messed up."
                    p "And this place is pretty well hidden..."
                    p "Maybe they were the only ones who knew about it."
                    show tom normal
                    "He nodded, seeming to catch on to what I was getting at."
                    tom "We can just wait here."
                    p "Well..."
                    p "I don't think anyone's coming to rescue us."
                    show tom worried
                    p "We'll just die of thirst or something."
                    p "... I think I have to go back out and find us a way to leave this place."
                    "He seemed reluctant at first, but then resigned."
                    tom "You're right."
                    tom normal "Ah!"
                    tom "Thank you, by the way."
                    tom "For saving me..."
                    p "Of course."
                    $ tom_name = "Tom"
                    tom "Uh... I'm Tom."
                    tom "What can I call you?"
                    p "Oh... I'm [player_name]."
                    p "It's... nice to meet you."
                    if player_name.lower() == "derek":
                        tom worried "Oh..."
                        tom "Uh..."
                        p "I know."
                    elif True:
                        tom worried "Yeah, I wish I wasn't here either."
                        p "Yeah..."
                    "I looked down and remembered the knife."
                    $ inventory.append("item_sacrificial_knife")
                    $ renpy.notify("Knife Added!")
                    show screen inventory
                    pause(1.5)
                    hide screen inventory
                    if achievement.has("ach_what_do_you_have_there") != True:
                        $ persistent.ach_what_do_you_have_there = True
                        $ achievement.grant("ach_what_do_you_have_there")
                        init:
                            $ achievement.register("ach_what_do_you_have_there")
                            $ achievement.sync()
                            $ renpy.save_persistent()
                            if persistent.ach_what_do_you_have_there == True and achievement.has("ach_what_do_you_have_there") != True:
                                $ achievement.grant("ach_what_do_you_have_there")
                                $ achievement.register("ach_what_do_you_have_there")
                                $ achievement.sync()
                    "This is bound to come in handy."
                    $ tom_location = "Cave"
                    $ arrivedby = "special"
                    jump derek_turn_nostats
                "Slap his sunburn" if meme_mode:
                    "I wound up for a full strength slap."
                    p "No mercy!"
                    "The impact of hand on red hot flesh rang throughout the cave."
                    "He screamed with the agony of a thousand suns."
                    jump dragon_stabbed
                "Refuse to kill" if True:
                    "My hands were shaking."
                    "I can't do this!"
                    scene black with dissolve
                    "I stumbled backwards."
                    "The motion caught the attention of the big guy."
                    dragon angry "You..."
                    "Shit!"
                    "Suddenly everything was a blur."
                    "It's too dark!"
                    "Hands clasped around my neck."
                    stop music
                    play sound "<from 0.0 to 1.0>music/sfx_knife_stab.ogg"
                    "... And then they loosened."
                    "I looked down at the blood running from the knife on to my body."
                    "I held it out and he..."
                    play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
                    "He coughed once and fell to the side, off my blade."
                    "Blood pooled from his body."
                    "I realized I was shaking and panting."
                    "I don't know how long I stayed like that... until a soft groan of pain caught my attention."
                    jump event_derek_dragonkilled

label event_derek_dead_tom:
    $ phase = "event"
    $ map_location = "Cave"
    $ arrivedby = "new"
    call derek_display_subroutine from _call_derek_display_subroutine_29
    $ tom_location = "Dead"
    "I descended into the small underground cave."
    $ stat_sanity -= 30
    "Oh God."
    play sound "music/sfx_scrape_fast.ogg"
    $ persistent.cgs_derek.add("cg_derek_deadtom")
    $ renpy.save_persistent()
    scene cg_derek_deadtom with dissolve
    "It's... one of the other captives."
    "As I looked closer, I saw more and more cuts all over his body."
    "The smell of wet blood mixed with earth made me nauseous."
    "I tried not to imagine what happened to him."
    "Or how long... it must have taken."
    call derek_display_subroutine from _call_derek_display_subroutine_30
    "I turned my eyes to the floor."
    $ arrivedby = "special"
    jump derek_turn_nostats

label event_derek_komodo_ambush:
    $ phase = "event"
    $ map_location = "Cave"
    $ arrivedby = "new"
    call derek_display_subroutine from _call_derek_display_subroutine_31
    "What the hell?"
    "As my eyes adjusted, the first thing I saw was candles."
    "Who-"
    play music "music/lizards_theme.ogg" fadein 1.0
    $ dragon_name = "Dragon"
    komodo surprised "Dragon!"
    $ stat_health -= 10
    play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
    "A sharp blow to the back of the head sent me sprawling forward on the raised dirt 'table' in the middle of the cave." with vpunch
    komodo normal "Nice."
    "I scrambled to push myself up, but a large hand shoved me back down."
    dragon "Where's the rope?"
    komodo "Got it."
    "I tried harder to squirm out, but the grasp holding me down got much heavier."
    "I wheezed as the air was pushed from me."
    komodo "Put [pp_pos] arms out."
    "My arms were wrenched out in front of me as I was pushed face-first into the table."
    "I couldn't do anything to stop him from quickly tying my wrists together with a thin, scratchy rope."
    $ komodo_name = "Komodo"
    dragon "Komodo..."
    dragon "Maybe we should just use {i}[pp_obj]{/i} and do it now?"
    komodo "..."
    "He seemed to be taking his time deciding."
    "What is it they wanted to do..?"
    komodo "No. We need more time to get ready."
    dragon "..."
    komodo "Hey! Don't worry!"
    komodo "That doesn't mean we're gonna let [pp_obj] go."
    $ persistent.cgs_derek.add("cg_derek_kdloom")
    $ renpy.save_persistent()
    scene cg_derek_kdloom with dissolve
    "I was suddenly flipped over onto my back on the dirt table between them."
    komodo empty "Extra blood will make it better."
    dragon empty "What if we can't find our boy after?"
    komodo empty "Relax."
    komodo empty "Jack is busy with the girl he brought."
    komodo empty "I don't know what the fuck Machete wants, but he brought his own guy too."
    komodo empty "And Derek's an idiot."
    komodo empty "There's nothing to worry about."
    dragon empty "..."
    komodo empty "We'll do it properly!"
    dragon empty "... Okay."
    komodo empty "Gimme the knife."
    "I gasped in fear as I saw an overly ornate knife passing hands between them."
    "My body filled with adrenaline."
    "I lurched upward, trying to thrash my way free."
    play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
    "The one named 'Dragon' grabbed my shoulders and slammed me back down to the table." with vpunch
    if meme_mode:
        p "So are you guys like... you know..."
    elif True:
        p "No no no! Stop!"
    $ persistent.cgs_derek.add("cg_derek_kdgut1")
    $ renpy.save_persistent()
    scene cg_derek_kdgut1 with dissolve
    "Komodo raised the knife above my abdomen."
    if meme_mode:
        p "LIKE, IF YOU WERE IN A HOT TUB TOGETHER, WOULD YOU BE FOUR OR LESS FEET APART?"
    elif True:
        p "PLEASE!"
        p "DON'T DO THIS!"
    "My yelling and squirming were completely ignored."
    $ stat_sanity -= 30
    $ stat_health -= 50
    $ persistent.cgs_derek.add("cg_derek_kdgut2")
    $ renpy.save_persistent()
    scene cg_derek_kdgut2
    play sound "music/sfx_knife_stab.ogg"
    "I let out a bloodcurdling scream as he plunged the knife into my belly, just below my ribcage." with vpunch
    "Agony clouded my vision."
    $ stat_health -= 10
    play sound "music/sfx_gore_1.ogg"
    "I gagged and whimpered as I felt the blade push further up into me under my ribs."
    p "N... nn..."
    dragon empty "Did you have to do it so quickly..?"
    "I couldn't fight anymore."
    $ stat_health -= 20
    scene cg_derek_kdloom with dissolve
    p "HNNkk!"
    play sound "music/sfx_gore_2.ogg"
    "The knife seemed to hurt more coming out than when it went in."
    "Blood poured from me as I stared at the wet blade."
    "I convulsed as I tried to keep breathing."
    dragon empty "You {i}always{/i} do that."
    komodo empty "You know we don't have time to play around."
    scene black with eyedissolve
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    hide screen effect_health
    hide screen effect_ice
    "I couldn't keep my eyes open."
    $ stat_health -= 20
    komodo "This is just the appetizer."
    pause 1.0
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_derek.add("You paved the way for sacrifice")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_38
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You paved the way for sacrifice")
    $ renpy.pause(hard=True)

label event_derek_hotdeath:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        $ sleep = 0
        scene black
        "..."
    elif True:
        scene black with eyedissolve
        "..." with vpunch
    "What..."
    "Happened?"
    "... Everything hurts..."
    "I can't move..."
    $ persistent.cgs_derek.add("cg_derek_nightsky")
    $ renpy.save_persistent()
    scene cg_derek_nightsky with eyedissolve_reverse
    "How long has it been..?"
    "I was barely able to turn my head to see my severely sunburnt skin."
    "... I must have passed out."
    "Everything is spinning..."
    "I don't even have the energy to lift my hand."
    $ persistent.cgs_derek.add("cg_derek_nightsky_machete1")
    $ renpy.save_persistent()
    play music "music/machetes_theme.ogg" fadein 1.0
    scene cg_derek_nightsky_machete1 with dissolve
    "!!!"
    machete empty "..."
    "It's one of them!"
    "I knew I should be scared, but everything still felt so fuzzy."
    p "Are you real..?"
    machete empty "..."
    p "Who? What..?"
    $ persistent.cgs_derek.add("cg_derek_nightsky_machete2")
    $ renpy.save_persistent()
    scene cg_derek_nightsky_machete2 with dissolve
    p "W-what are you-"
    machete empty "It's better this way."
    label instachop:
    scene black
    $ stat_health -= 100
    play sound "music/sfx_axe_chop.ogg"
    stop ambient
    stop music
    hide screen effect_health
    hide screen effect_ice
    "The blade came down with no hesitation." with vpunch
    pause 1.0
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_derek.add("The heat got to you")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_39
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","The heat got to you")
    $ renpy.pause(hard=True)

label event_derek_firstblooddeath:
    $ phase = "event"
    "I couldn't just let this happen."
    "I struggled to get up on my knees."
    p "Stop!"
    show jack with dissolve
    jack "Oh?"
    "Suddenly all of their attention was on me."
    "A wave of fear and regret passed through my body."
    jack "What's wrong?"
    jack "Do you want to take her place?"
    d surprise "What!?"
    d "[pp_is_c] mine!"
    jack "You know the rules."
    d grumpy "But you just called dibs on yours-"
    jack "Are you going to fight me on this?"
    d "..."
    d "No..."
    jack "Good."
    if meme_mode:
        "I squinted at the interaction."
        "Something smells pretty strongly of daddy issues here."
    hide jack with dissolve
    "Suddenly, Jack was grabbing me by the arm and dragging me into the middle" with vpunch
    "The two with lizard masks moved the crying woman back to her original spot."
    jack "Let's get started on our eager volunteer."
    $ persistent.cgs_derek.add("cg_derek_firstblood_1")
    $ renpy.save_persistent()
    scene cg_derek_firstblood_1 with dissolve
    play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
    "Derek knelt down and slapped my face with no warning." with hpunch
    "The yelp I let out from the sting seemed to really capture his attention."
    "He flashed a knife deliberately in my field of vision."
    d empty "Beg for me..."
    menu:
        " "
        "Beg" if True:
            p "Please, don't do this!"
            p "Please, please!"
            "There was no point in trying to keep my pride now."
            "I just wanted to survive."
            $ stat_sanity -= 5
            $ stat_health -= 2
            "I cried out in pain and surprise as he dragged the knife roughly along my collar anyway."
            d empty "Just like that..."
        "Refuse" if True:
            "I kept my mouth shut."
            "Why would I give him what he wants now?"
            d empty "Tsk."
            $ stat_sanity -= 5
            $ stat_health -= 2
            "I cried out in pain as he dragged the knife roughly along my collar."
            d empty "Hah..."
        "\"You hit like a girl.\"" if meme_mode:
            play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
            scene black with vpunch
            d angry "WHAT."
            p "Heh... heh."
            $ stat_sanity -= 5
            $ stat_health -= 10
            play sound "<from 0.0 to 1.0>music/sfx_impact_thud.ogg"
            "He kicked me with an angry scream." with vpunch
            jack "Settle DOWN Derek!"
            d grumpy "Hrn..."
            $ stat_sanity -= 5
            $ stat_health -= 2
            "I cried out in pain as he dragged the knife roughly along my collar."
            d mocking "Hah..."
    $ persistent.cgs_derek.add("cg_derek_firstblood_2")
    $ renpy.save_persistent()
    scene cg_derek_firstblood_2 with dissolve
    "The knife hurt, but something in his intense focus was more concerning to me."
    "He stared right into my eyes as he cut me."
    if sexcontent != "no":
        "It was enough to stop me from noticing the hands on my legs."
    elif True:
        "It was enough to stop me from noticing the touch of a blade on my leg."
    "When I finally realized, it was too late."
    $ stat_sanity -= 5
    $ stat_health -= 10
    play sound "music/sfx_knife_stab.ogg"
    "I shrieked as another knife plunged deep into my leg." with vpunch
    "I couldn't stop from crying in pain now."
    "Derek held my face tightly in front of him."
    "I wanted to stop crying, but his excited grin scared me more."
    "My body was shaking from the pain in my leg as he ran his thumb over my cheek, through my tears."
    "This can't be happening."
    p "Stop... please..."
    "Once again, Derek's fixated stare distracted me from what was going on behind me."
    if sexcontent != "no":
        "Jack's hands gripped my hips and lifted me."
        "My whole body jerked as he touched me."
        "Where was my underwear!? Did he cut it off!?"
        $ stat_sanity -= 5
        "I squirmed and flushed with disgusted embarassment as I felt him touch me."
    elif True:
        $ stat_sanity -= 5
        $ stat_health -= 10
        play sound "music/sfx_knife_stab.ogg"
        "Jack's knife stabbed into the meat of my thigh again as I screamed." with vpunch
        $ stat_sanity -= 5
        $ stat_health -= 10
        play sound "music/sfx_knife_stab.ogg"
        "He withdrew the knife slowly before stabbing again and again." with vpunch
    "Derek was laughing like a hyena."
    "There was too much going on at once."
    $ stat_sanity -= 5
    $ stat_health -= 5
    "More blades cut into my back, filling my mind with pain again."
    "I tried to look back, they must be all around me now- but Derek was still gripping my face."
    if sexcontent != "no":
        "Something pressed against my flesh behind me and I knew what was coming next."
        p "No!"
        $ stat_sanity -= 20
        "Jack's fingers dug into my thighs as he thrust into me."
    elif True:
        "I could feel my grip on reality leaving me."
        "I wasn't in control."
    "I screamed, ignoring Derek's excitement at my reaction."
    $ stat_sanity -= 5
    $ stat_health -= 10
    "Knives were still cutting into my back, and I could feel myself breaking down."
    "I sobbed, not even knowing what direction I could squirm if I still had the strength."
    if sexcontent != "no":
        "I could hear Jack panting behind me, thrusting painfully hard."
    d empty "You're going all quiet!"
    "I didn't have the strength to scream anymore."
    if sexcontent != "no":
        d empty "Well... if {i}you're{/i} not gonna use your mouth..."
    elif True:
        "He pushed his knife into my mouth and tugged against the side."
        d empty "I can make you cry again..."
    scene black
    "My mental preparations turned to confusion as I saw his expression change."
    d surprise "Hey, wait!"
    $ stat_health -= 100
    stop music
    stop ambient
    hide screen effect_health
    hide screen effect_ice
    play sound "<from 0.0 to 1.0>music/sfx_axe_chop.ogg"
    "Something hit me on the back of my neck and sent the world spinning." with vpunch
    "I can't... feel my body?"
    d angry "God DAMN it! Machete!"
    "Everything was fading."
    "It didn't hurt anymore."
    if meme_mode:
        "EPILOGUE:"
        "When the ropes were cut on the remaining victims, Chamomile and Jaqueline ran away together."
        "Jack found them quickly and assumed he could easily assault them."
        "He was wrong."
        "The ladies ganged up on him, tackled him to the ground, and ripped the weapons off him."
        "They stabbed him in the gut with zero hesitation and let him bleed out in the sun."
        "At night, they rested on the hill and discovered the entrance to the cave."
        "Chamomile led the way, and they confronted Komodo and Dragon."
        "Komodo and Dragon were out-armed; Jaq and Cham still had Jack's knife and brass knuckles."
        "They beat the lizards down and saved Tom."
        "The three of them all had a weapon, so they immediately stormed the camp."
        "They defeated Derek easily, and slashed his throat in revenge for [player_name]."
        "They found the map to the escape vehicles and they drove to civilization."
        "They all had a delicious meal and booked group therapy."
        "They stayed friends for the rest of their days."
        "THE END"
        pause 1.0
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_derek.add("You volunteered for first blood")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_40
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You volunteered for first blood")
    $ renpy.pause(hard=True)

label event_derek_komodo_sacrifice:
    $ phase = "event"
    "It tastes... bitter..."
    "I tried to spit the rest out."
    "But I already swallowed a bunch..."
    "Maybe if I just-"
    play sound "music/sfx_rocks.ogg"
    "I took a step forward and stumbled." with vpunch
    "What..?"
    "My heart started pounding as I tried to take another step."
    play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
    "I fell to the ground." with vpunch
    "Something's wrong with my arms and legs!"
    $ stat_sanity -= 5
    "I can't move!!!"
    "I realized that I was hyperventilating."
    "I can't panic now. That's not going to help."
    "Whatever it is... has to wear off."
    "I just have to hope that... no one finds me."
    $ hours += 1
    $ total_hours += 1
    scene black with eyedissolve
    "..."
    "It isn't getting better."
    "My arms and legs are paralyzed..."
    "I'm itchy... I can still feel everything."
    "That's a good sign right..?"
    $ hours += 1
    $ total_hours += 1
    call derek_display_subroutine from _call_derek_display_subroutine_35
    "It's hot... I'm overheating..."
    "It feels like it's coming from my gut."
    scene black with eyedissolve
    "I still can't move."
    $ hours = 1
    call derek_display_subroutine from _call_derek_display_subroutine_36
    "..."
    "It's been hours..."
    play sound "music/sfx_rocks.ogg"
    "The sound of footsteps crunching over rocks suddenly sent my heart pounding again."
    "I can't... turn to look!"
    play music "music/lizards_theme.ogg" fadein 1.0
    if meme_mode:
        komodo "What's up, fucker?"
    elif True:
        komodo "Well, hello there!"
    "I could feel a foot nudging me."
    komodo "You drank the water, didn't you?"
    "I tried to scream, but only an awkward croak came out."
    "Something must be paralyzed in my throat too."
    dragon "We could use [pp_obj]."
    komodo "Yeah..."
    komodo "We spent so much time picking out those soft lambs though..."
    dragon "We don't even know if the boy is still alive."
    dragon "And besides..."
    dragon "[pp_sub_c] came to us. Maybe it's meant to be."
    komodo "Good point."
    komodo "All right, let's get our guest of honour all set up, eh?"
    "The other one nodded and grabbed me."
    "I tried in vain to struggle as he heaved my limp body over his shoulder."
    $ map_location = "Hill"
    play ambient "music/ambient_desert_wind.ogg" fadein 1.0
    call derek_display_subroutine from _call_derek_display_subroutine_37
    "They carried me up the rocks of the hill and stopped to grab a camouflaged cloth, revealing a makeshift door."
    "I wheezed, trying to scream again, as they pulled me inside the cave behind the door."
    play ambient "music/ambient_cave.ogg" fadein 1.0
    $ map_location = "Cave"
    $ arrivedby = "new"
    call derek_display_subroutine from _call_derek_display_subroutine_38
    "... Candles?"
    $ persistent.cgs_derek.add("cg_derek_cave")
    $ renpy.save_persistent()
    scene cg_derek_cave
    "The air was knocked out of me as the man carrying me dumped me on a raised dirt platform." with vpunch
    $ dragon_name = "Dragon"
    komodo "Thanks, Dragon~"
    dragon "Mm."
    komodo "Okay, where's the-"
    komodo "God damn, I can't see anything in here..."
    $ komodo_name = "Komodo"
    dragon "Komodo."
    "I watched as the one named 'Dragon' held out a complicated looking dagger."
    komodo "Ah."
    scene cg_derek_cave_k with dissolve
    komodo empty "Now..."
    komodo empty "Let's see if you can scream like that."
    "He held the knife above my torso."
    "I only twitched as I tried to flinch."
    $ stat_sanity -= 10
    $ stat_health -= 3
    play sound "music/sfx_knife_stab.ogg"
    "The blade pressed into my belly, easily cutting through the flimsy tank top and my flesh beneath it."
    "I tried to scream."
    "I wanted to scream."
    "But all that came out was rasping air."
    scene cg_derek_cave_kd_kknife with dissolve
    dragon empty "Wow..."
    komodo empty "Yeah. That stuff you got is really good..."
    komodo empty "Look at [pp_obj]..."
    komodo empty "[pp_is_c] trying so hard..."
    $ stat_health -= 3
    play sound "music/sfx_knife_stab.ogg"
    "He slid the knife around and made another deep cut."
    komodo empty "Don't worry. You don't really need to scream."
    komodo empty "What's important here is that you {i}feel{/i} it properly."
    if meme_mode:
        "I was definitely 'feeling' it, Mr. Krabs."
    elif True:
        "I was definitely 'feeling' it."
    "I could feel everything so well... it didn't seem possible for a cut to hurt that much."
    if meme_mode:
        dragon empty "{font=images/feral.regular.ttf}{size=12}Grace us with His agony.{/size}{/font}"
    elif True:
        dragon empty "{font=images/gatosrunes.ttf}{size=12}Grace us with His agony.{/size}{/font}"
    "What is he whispering?"
    komodo empty "You're part of something very important."
    komodo empty "We're going to fix the world."
    if meme_mode:
        dragon empty "{font=images/feral.regular.ttf}{size=14}In Chaos we find Reverence.\nIn Pain we find Comfort.{/size}{/font}"
    elif True:
        dragon empty "{font=images/gatosrunes.ttf}{size=14}In Chaos we find Reverence.\nIn Pain we find Comfort.{/size}{/font}"
    $ stat_health -= 5
    $ stat_sanity -= 10
    play sound "music/sfx_gore_1.ogg"
    "The blade dug in again. Deep. Too deep."
    "I can't move... I can't stop it."
    komodo empty "The world's gone numb..."
    "Hot tears welled up and fell down the sides of my face."
    komodo empty "We all enter this world screaming."
    komodo empty "It's the natural state we all came from."
    dragon empty "You're going too fast."
    if meme_mode:
        komodo empty "I am not, relax."
        dragon empty "You are! You're gonna hit an artery and [pp_is] gonna bleed out!"
        komodo empty "Do I look like I'm anywhere near an artery?"
        dragon empty "How would I know?"
        komodo empty "Well you went to college."
        dragon empty "I dropped out!"
        dragon empty "And it's not like I took some kind of medical thing."
        komodo empty "Well I watched every season of Home so I know where not to cut, okay?"
        dragon empty "You watched every season of {i}what?{/i}"
        komodo empty "Home. You know..."
        komodo empty "The one with the hundred dalmatians guy."
        dragon empty "What the fuck are you talking about?"
        "I looked back and forth between them, sweating."
        komodo empty "The guy who was the bad guy in the live action hundred dalmations!"
        dragon empty "..."
        dragon empty "Are you talking about fucking {i}House?{/i}"
        komodo empty "Yeah. Whatever."
        "The blonde one started laughing."
        dragon empty "It was the main character's {i}name!{/i}"
        dragon empty "They said it like forty times an episode!"
        p "Um, I don't think that show had like... real medical information in it..."
        komodo empty "Shut up!!!"
        scene cg_derek_cave_kd_dknife with dissolve
    elif True:
        "The heat... the candles..."
        komodo empty "Hah... fine."
        komodo empty "You do it."
        scene cg_derek_cave_kd_dknife with dissolve
        "The fire..."
        "Dragon took the knife and held it over a candle."
        "He looked in my eyes with no fear or remorse."
        "Who are these people!?"
    $ stat_health -= 5
    $ stat_sanity -= 10
    "Agony shot through my body again as he dragged the heated blade through the skin over my ribs."
    "I laid there motionless as everything exploded in my mind."
    "Why!?"
    if meme_mode:
        dragon empty "{font=images/feral.regular.ttf}{size=14}Feed to Him your pain.{/size}{/font}"
    elif True:
        dragon empty "{font=images/gatosrunes.ttf}{size=14}Feed to Him your pain.{/size}{/font}"
    komodo empty "How does it feel?"
    komodo empty "Do you feel closer to Him yet?"
    "My terrified breathing hitched as Komodo stuck his fingers into the deep wound on my belly."
    "His long fingers scraped down my skin, dragging blood with them."
    "What is happening..."
    "What the fuck are these people talking about!?"
    "Is this just a nightmare..?"
    $ stat_health -= 10
    "I kept gasping and choking, unable to even squirm, as Dragon made new cuts over my arms and legs."
    "He moved so slowly and deliberately."
    dragon empty "The bag."
    komodo empty "Oh!"
    scene cg_derek_cave_d with dissolve
    "Komodo briefly left my field of view."
    "He returned immediately and gave a small bag to Dragon."
    scene cg_derek_cave_kd_salt with dissolve
    dragon empty "Thank you."
    "He then seemed to speak directly to me."
    dragon empty "Take a deep breath."
    dragon empty "It's time to open your mind and accept the agony."
    "As soon as he pulled his hand from the little bag and retrieved white powder, I guessed what was happening."
    "It has to be sal-"
    $ stat_sanity -= 10
    "My body twitched as a half-formed scream managed to escape my core." with vpunch
    "He pushed the salt into my open flesh, sending searing pain through every nerve."
    "Hissing static and shining lights coaxed my throbbing consciousness a bit further from reality."
    "Yet I could still feel..."
    scene cg_derek_cave_perv with dissolve
    if sexcontent != "no":
        "Komodo's fingers kept trailing down my body."
        "That knife was tearing my skin apart, but I still felt him..."
        "They dipped inside my underwear and yet again I couldn't even flinch."
        "That heat..."
        "He touched my most sensitive skin and the pain mixed with the new sensation explosively."
        "The heat that was building inside me roared to life."
        "I couldn't separate the torment of the knife from the fingers touching me..."
        "Massaging me."
        "I wanted to scream."
        "I wanted to moan."
        "Blinding, pulsing, pain..."
        "And pleasure..."
        "My mind is on fire."
    elif True:
        "Komodo's fingers kept finding their way inside my flesh."
        "I could feel so many tiny rivers of blood on my body now."
        "And the blinding, pulsing, pain."
        "I couldn't even have imagined pain like this."
    "Blurry and wild, their faces and the candle flames."
    $ persistent.cgs_derek.add("cg_derek_cave_sacrifice")
    $ renpy.save_persistent()
    scene cg_derek_cave_sacrifice with dissolve
    "Then the knife again, held over my center."
    if meme_mode:
        dragon empty "{font=images/feral.regular.ttf}{size=20}Accept this gift and come to us.{/size}{/font}"
    elif True:
        dragon empty "{font=images/gatosrunes.ttf}{size=20}Accept this gift and come to us.{/size}{/font}"
    "No!"
    $ stat_health -= 100
    $ stat_sanity -= 10
    scene cg_derek_cave_sacrifice2
    play sound "music/sfx_knife_stab.ogg"
    "He brought the knife down and into me with purpose." with vpunch
    if meme_mode:
        dragon empty "{font=images/feral.regular.ttf}{size=26}Sensation has rotted away on this plane. You are needed.{/size}{/font}"
    elif True:
        dragon empty "{font=images/gatosrunes.ttf}{size=26}Sensation has rotted away on this plane. You are needed.{/size}{/font}"
    "I can't... I can't..."
    $ persistent.cgs_derek.add("cg_derek_cave_guts")
    $ renpy.save_persistent()
    scene cg_derek_cave_guts with dissolve
    play sound "music/sfx_gore_2.ogg"
    "I lurched at the sight of the bloody mass he pulled from me."
    "The agony... the sickening pulling sensation of parts of me being pulled from their home."
    if meme_mode:
        dragon empty "{font=images/feral.regular.ttf}{size=30}Come to us!{/size}{/font}"
    elif True:
        dragon empty "{font=images/gatosrunes.ttf}{size=30}Come to us!{/size}{/font}"
    scene black with eyedissolve
    stop music fadeout 1.0
    stop ambient fadeout 2.0
    "The blurring shapes faded to darkness as I grew colder."
    "I'm dying... aren't I?"
    play music [ "<silence 1.0>", "music/music_175oz.ogg" ]
    play ambient "music/ambient_medium_fire.ogg" fadein 1.0
    window hide
    hide screen status
    hide screen effect_health with dissolve
    pause (1.0)
    $ persistent.cgs_derek.add("cg_derek_demon")
    $ renpy.save_persistent()
    scene cg_derek_demon with firedissolve
    if achievement.has("ach_evil_never_dies") != True:
        $ persistent.ach_evil_never_dies = True
        $ achievement.grant("ach_evil_never_dies")
        init:
            $ achievement.register("ach_evil_never_dies")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_evil_never_dies == True and achievement.has("ach_evil_never_dies") != True:
                $ achievement.grant("ach_evil_never_dies")
                $ achievement.register("ach_evil_never_dies")
                $ achievement.sync()
    if meme_mode:
        demon empty "{cps=10}{font=images/feral.regular.ttf}{size=40}My first gift...{/size}{/font}{/cps}"
        demon empty "{cps=10}{font=images/feral.regular.ttf}{size=40}I will treasure you.{/size}{/font}{/cps}"
    elif True:
        demon empty "{cps=10}{font=images/gatosrunes.ttf}{size=40}My first gift...{/size}{/font}{/cps}"
        demon empty "{cps=10}{font=images/gatosrunes.ttf}{size=40}I will treasure you.{/size}{/font}{/cps}"
    scene black with Dissolve(3.0)
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    pause 1.0
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_derek.add("You were sacrificed")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_41
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You were sacrificed")
    $ renpy.pause(hard=True)

label event_derek_paralyzed_machete:
    $ phase = "event"
    "It tastes... bitter..."
    "I tried to spit the rest out."
    "But I already swallowed a bunch..."
    "Maybe if I just-"
    play sound "music/sfx_rocks.ogg"
    "I took a step forward and stumbled." with vpunch
    "What..?"
    "My heart started pounding as I tried to take another step."
    play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
    "I fell to the ground." with vpunch
    "Something's wrong with my arms and legs!"
    $ stat_sanity -= 5
    "I can't move!!!"
    "I realized that I was hyperventilating."
    "I can't panic now. That's not going to help."
    "Whatever it is... has to wear off."
    "I just have to hope that... no one finds me."
    $ hours += 1
    $ total_hours += 1
    if map_location != "Cave":
        scene black with eyedissolve
        "..."
        "It isn't getting better."
        "My arms and legs are paralyzed..."
        "And it feels like there's something watching me."
        $ hours = 1
        call derek_display_subroutine from _call_derek_display_subroutine_40
        "It's been hours..."
        "I need to move... I need to get somewhere safe..."
        "I heard footsteps over the sand."
        "Once more, I tried in vain to get up."
        scene black with dissolve
        "I could only lay there helplessly as the footsteps got closer."
    elif True:
        scene black with eyedissolve
        "I must have passed out..."
        "I felt something dragging me over rocks."
        "Huh?"
    play music "music/machetes_theme.ogg" fadein 1.0
    $ persistent.cgs_derek.add("cg_derek_watermachete1")
    scene cg_derek_watermachete1 with dissolve
    machete empty "..."
    "Terror flooded my motionless body as the white mask came into view above me."
    machete empty "You can't run."
    "I couldn't answer..."
    "But it wasn't really a question anyway."
    "For a moment, the weapon in his hand seemed too heavy in his grip."
    $ persistent.cgs_derek.add("cg_derek_watermachete2")
    $ renpy.save_persistent()
    scene cg_derek_watermachete2 with dissolve
    "Then he raised it like it was nothing."
    "The illusion was gone."
    $ stat_health -= 100
    play sound "<from 0.0 to 1.0>music/sfx_axe_chop.ogg"
    scene black with vpunch
    hide screen effect_health
    hide screen effect_ice
    stop music
    stop ambient
    "There was no time left for fear."
    pause 1.0
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_derek.add("You drank the water")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_42
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You drank the water")
    $ renpy.pause(hard=True)

label event_derek_derekvsmachete:
    $ phase = "event"
    $ event_derek_derekvsmachete = 1
    if arrivedby == "new":
        "I cautiously approached the camp."
        "After seeing no activity, I got closer and kept quiet."
    "A soft groan made me freeze in place."
    "I spent a couple seconds searching for the source until I saw him."
    "It's him..."
    "'Derek'."
    "He was laying down, bandaged and moaning in pain."
    "I guess I didn't hit him anywhere too vital..."
    "Another source of movement almost made me jump."
    "I stayed crouched just out of sight and completely silent."
    play music "music/ambient_dire_situation.ogg" fadein 3.0
    scene cg_derek_vsmachete0 with dissolve
    "Another man was here."
    "The man in the blank mask."
    "He was moving silently and carefully."
    "I don't think Derek knows he's there..."
    "What... is he doing?"
    $ persistent.cgs_derek.add("cg_derek_vsmachete")
    $ renpy.save_persistent()
    scene cg_derek_vsmachete1 with dissolve
    "My eyes widened in shock as I saw him position the machete he was carrying over Derek."
    menu:
        " "
        "Stay quiet" if True:
            $ derek_status = "Dead"
            $ machete_unlock = 1
            play sound "<from 0.0 to 1.0>music/sfx_axe_chop.ogg"
            scene cg_derek_vsmachete2 with dissolve
            "He plunged the weapon into Derek's throat."
            "I stared in shock as he kept the machete in place."
            "Derek didn't make a sound at all."
            "He just sort of... went limp."
            $ persistent.cgs_derek.add("cg_derek_vsmachete_hush")
            $ renpy.save_persistent()
            scene cg_derek_vsmachete3 with dissolve
            "Then, in one swift motion, he pulled the machete free."
            "My blood froze in my body as he turned away and looked directly at me."
            "I couldn't think."
            "I couldn't move."
            scene cg_derek_vsmachete4 with dissolve
            "He slowly raised his finger in front of his mask, as if to ask me for silence."
            "I nodded."
            "What the hell else could I do?"
            stop music fadeout 1.0
            call derek_display_subroutine from _call_derek_display_subroutine_41
            "Then, he just turned from me and walked out of the camp."
            "He's not going to attack me?"
            "Why did he kill Derek..?"
            "I shook my head."
            "I can't stay here thinking about this."
            "I need to count my blessings and get out of here."
            "I slipped out of the camp and walked back out into the open desert."
            $ map_location = "Desert"
            call derek_display_subroutine from _call_derek_display_subroutine_42
            $ arrivedby = "special"
            jump derek_turn_nostats

        "{image=menu_sanity}Stop him{space=60}" if sanity < 50 and not renpy.variant("small"):
            label menu_sanity_jumper_2:
            $ persistent.cgs_derek.add("cg_derek_vsmachete5")
            $ renpy.save_persistent()
            scene cg_derek_vsmachete5 with dissolve
            play sound "music/sfx_scrape_fast.ogg"
            play music "music/dereks_theme.ogg"
            p "W-wait!"
            "As soon as the sound escaped me, both men turned their full attention to me."
            "I instantly regretted my actions."
            call derek_display_subroutine from _call_derek_display_subroutine_43
            "To my surprise, the man with the blank mask turned and started running."
            "I stared after him."
            "What the hell is going on!?"
            $ stat_health -= 10
            play sound "<from 0.0 to 1.0>music/sfx_knife_stab.ogg"
            "My entire body locked up in pain as I was stabbed in the back." with vpunch
            $ persistent.cgs_derek.add("cg_derek_sand")
            $ renpy.save_persistent()
            scene cg_derek_sand_night with dissolve
            play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
            "I fell to the ground, shock keeping a scream locked in my throat." with vpunch
            "My lower back... The pain was intense but I don't think he hit anything vital."
            d ragged "... You..."
            "He sounded ragged."
            d "I told you that you should have killed me."
            play sound "<from 0.0 to 1.0>music/sfx_impact_thud.ogg"
            "I wheezed as his knee and full weight suddenly dropped on my back." with vpunch
            "Panic exploded as I felt a needle push into my neck."
            p "Wh-wh-what-?"
            stop music fadeout 3.0
            scene black with eyedissolve
            hide screen effect_health
            hide screen effect_ice
            p "What..."
            pause(3.0)
            "I drifted in and out of consciousness."
            "I thought I heard motors..."
            "I thought I felt motion."
            "Something in my arm..."
            "I couldn't tell how much time was passing."
            scene bg_derek_theritz with eyedissolve_reverse
            $ persistent.bgs_seen.add("bg_derek_theritz")
            $ renpy.save_persistent()
            play music "music/ambient_dire_situation.ogg" fadein 5.0
            "I woke up with a headache."
            "I groaned in pain as I realized I was standing up."
            if achievement.has("ach_lifestyles_of_the_rich_and_imprisoned") != True:
                $ persistent.ach_lifestyles_of_the_rich_and_imprisoned = True
                $ achievement.grant("ach_lifestyles_of_the_rich_and_imprisoned")
                init:
                    $ achievement.register("ach_lifestyles_of_the_rich_and_imprisoned")
                    $ achievement.sync()
                    $ renpy.save_persistent()
                    if persistent.ach_lifestyles_of_the_rich_and_imprisoned == True and achievement.has("ach_lifestyles_of_the_rich_and_imprisoned") != True:
                        $ achievement.grant("ach_lifestyles_of_the_rich_and_imprisoned")
                        $ achievement.register("ach_lifestyles_of_the_rich_and_imprisoned")
                        $ achievement.sync()
            play sound "<from 0.0 to 0.9>music/sfx_chain.ogg"
            "I tried to pull away and found that my arms were chained."
            "As my memory began to return, so did the panic."
            "Where the fuck am I!?"
            "This isn't the desert..."
            "In fact this place looks really fancy and clean..."
            "Who-"
            "Panic turned into cold dread as I remembered Derek."
            "There's no other options..."
            p "HEY!"
            p "SOMEONE! HELP ME!"
            "As soon as I stopped, I heard footsteps moving away from the door outside the room."
            p "WAIT!"
            p "DON'T LEAVE ME!"
            "Rushed footsteps returned."
            play music "music/dereks_theme.ogg" fadein 1.0
            if meme_mode:
                if sexcontent == "yes":
                    show derek fancynude with dissolve
                elif True:
                    show derek fancynudecensor with dissolve
            elif True:
                show derek fancy with dissolve
            "Who..."
            "Is that-"
            d "Look who's finally awake~"
            "I didn't recognize him at first."
            d "Don't worry. I've had your back all patched up."
            "I couldn't think of what to say. Too much was running through my mind."
            d "Nothing to say, huh?"
            d "You DO remember me, don't you?"
            if meme_mode:
                if sexcontent == "yes":
                    d fancymadnude "You... {i}stabbed{/i} me."
                elif True:
                    d fancymadnudecensor "You... {i}stabbed{/i} me."
            elif True:
                d fancymad "You... {i}stabbed{/i} me."
            "I subconsciously tried to back further into the wall."
            p "I... remember."
            if meme_mode:
                if sexcontent == "yes":
                    d fancynude "Good... good."
                elif True:
                    d fancynudecensor "Good... good."
            elif True:
                d fancy "Good... good."
            d "You know, after you ran off, I had a {i}lot{/i} of time to think."
            d "Out there in the desert..."
            d "I thought about all the things I wanted to do to you."
            d "And I realized that I was pretty much out of time."
            d "... So I took you home."
            "I looked at my surroundings again."
            $ persistent.cgs_derek.add("cg_derek_theritz")
            $ renpy.save_persistent()
            if meme_mode:
                scene cg_derek_theritz_nude with dissolve
            elif True:
                scene cg_derek_theritz with dissolve
            d empty "I'm gonna make you cry... and beg."
            d empty "I'm gonna make you wish you died out there."
            "I shivered as he sneered."
            d empty "Everyone on the premises answers to me."
            d empty "No one will help you."
            d empty "You are property."
            d empty "{i}My{/i} property."
            d empty "And I'm going to use you for a long, {i}long{/i} time."
            scene black with dissolve
            stop music fadeout 1.0
            pause 1.0
            $ quick_menu = False
            window hide
            hide screen status
            $ persistent.endings_derek.add("He took you home")
            $ renpy.save_persistent()
            call achievement_checker from _call_achievement_checker_43
            play music "<from 0.4>music/music_but_at_what_cost.ogg" fadein 1.0
            scene bg_endslate_survival with zoomdissolve
            show screen bg_endslate_survival_text("You Lived","He took you home")
            $ renpy.pause(hard=True)
        "{image=menu_sanity_large}Stop him{space=60}" if sanity < 50 and renpy.variant("small"):
            jump menu_sanity_jumper_2
label event_derek_talk_tom:
    $ phase = "event"
    if event_derek_talk_tom == 0:
        $ event_derek_talk_tom = 1
        p "So uhhh... are you okay?"
        tom normal "I guess, relatively?"
        tom "I can get around and help with stuff, if that's what you mean."
        menu:
            " "
            "\"I'm glad to hear it! You're doing great!\"" if True:
                tom "Oh... Uh..."
                tom happy "Thank you."
                tom "I'll do my best!"
            "\"You don't look so good...\"" if True:
                tom worried "Well..."
                tom "I mean I'm not really okay."
                tom "I don't think I'll ever be okay again, after this."
                show tom normal
                p "... We're gonna get through this, Tom."
                $ stat_sanity += 5
                p "We'll do it together."
                tom wistful "... Thanks."
        $ arrivedby = "special"
        jump derek_turn_nostats
    elif event_derek_talk_tom == 1:
        $ event_derek_talk_tom = 2
        p "So, what was your life like before this?"
        tom normal "Well..."
        tom "I was going to college."
        tom wistful "For- for music."
        p "Music?"
        tom happy "Yeah."
        tom "A couple friends and I made an indie band."
        tom wistful "We have a Soundcloud and stuff... but..."
        tom "Well, we only have like, 25 followers."
        tom "And most of those are friends."
        tom happy "So I'm taking a course in music production."
        p "That's really cool!"
        tom wistful "Yeah..."
        p "We're going to get home."
        p "And then you can show me some of your work, okay?"
        tom "..."
        p "Promise?"
        $ stat_sanity += 10
        tom happy "... Okay."
        $ arrivedby = "special"
        jump derek_turn_nostats
    elif event_derek_talk_tom == 2:
        $ event_derek_talk_tom = 3
        p "Um, Tom?"
        tom "Yeah?"
        show tom normal
        p "How did you get here?"
        p "If you don't mind me asking... it's okay if you don't want to talk about it."
        tom worried "I..."
        tom "Well it's kind of fuzzy, to be honest."
        tom "I remember being alone on campus pretty late."
        tom "But after that..."
        tom "I don't remember ever seeing those two guys with the lizard masks."
        tom "At least until they were dragging me and..."
        tom "..."
        tom "And that blonde girl."
        tom "She..."
        tom "I saw her before. On campus."
        tom "I think they took us both from the same college."
        p "There wasn't any... auction?"
        tom normal "Huh?"
        tom "Not as far as I know."
        tom "I think they kidnapped us from campus and took us here."
        tom worried "I wonder if anyone is looking for us yet..."
        p "I'm sure they are."
        tom "Yeah..."
        $ arrivedby = "special"
        jump derek_turn_nostats
    elif True:
        "I looked at Tom, then back down to the floor."
        "There really isn't much more to say."
        $ arrivedby = "special"
        jump derek_turn_nostats
label event_derek_talk_jaq:
    $ phase = "event"
    if event_derek_talk_jaq == 0:
        $ event_derek_talk_jaq = 1
        p "So..."
        p "I assume you were brought here by one of them, too?"
        jaq worried "... Yeah."
        jaq "It was the guy in the leather jacket. The one with the dog mask or whatever."
        jaq angry "That mask doesn't do shit. I know exactly who he is."
        p "Wh... you do!?"
        jaq worried "Yeah. It's a creepy asshole from my gym."
        jaq "I caught him staring at me plenty of times."
        jaq "I even changed my schedule, but somehow he was still in there when I went."
        jaq "I should have called the cops... or... or done something..."
        p "There's no way you could have known."
        jaq angry "Bullshit."
        jaq "I..."
        jaq worried "..."
        jaq "Sorry. There's no point in dwelling on that now. I know."
        "I decided to try and change the subject slightly."
        p "So... this might seem weird, but you don't remember any sort of... auction?"
        jaq question "Auction?"
        jaq worried "No."
        jaq angry "That fucker pulled a knife on me, tied me up, and stuffed me in the trunk of some smelly car."
        jaq worried "I was in there for {i}hours{/i}."
        "I looked down, trying to process the information."
        if event_derek_talk_tom == 3:
            show tom normal
            p "Tom said the two guys in lizard masks took him from a college campus..."
            tom surprised "O-Oh yeah!"
            tom normal "Me and the blonde girl that they-"
            tom worried "They..."
            tom "The blonde girl."
        p "And I don't remember much at all."
        p "Other than waking up in some sort of auction."
        p "The guy without the mask."
        p "... Derek."
        p "I think he 'bought' me."
        p "Then I was knocked out... and I woke up here with everyone else."
        "The cave slipped into silence as we sat, deep in thought."
        $ arrivedby = "special"
        jump derek_turn_nostats
    elif event_derek_talk_jaq == 1:
        $ event_derek_talk_jaq = 2
        "I decided to try and break the uncomfortable silence."
        show jaq normal
        p "So Jaqueline..."
        p "What sort of other stuff did you do before this?"
        jaq worried "... Why does it matter?"
        p "Uh... well..."
        if tom_location == "Cave":
            show tom worried
            "She looked away from me and to Tom."
            "He was looking at the dirt floor and trying not to cry."
        elif True:
            "I shifted uncomfortably."
        "She sighed and softened her posture."
        jaq normal "I'm a painter."
        jaq worried "Not like, the fun kind, or anything."
        jaq normal "I just paint walls of commercial buildings and stuff."
        jaq "It's boring, but it's easy and it pays good enough."
        show jaq worried
        "She looked off to the side."
        jaq "Mostly I just like to go to the gym... and hang out with friends at the bar..."
        jaq "I guess it wasn't much of a life."
        show jaq normal
        p "Hey, it sounds pretty good to me!"
        p "And... and you're gonna get home."
        show jaq worried
        if tom_location == "Cave" or rich_location == "Cave":
            if tom_location == "Cave":
                show tom wistful
            p "We all are."
        elif True:
            p "We both are."
        show jaq normal
        $ arrivedby = "special"
        jump derek_turn_nostats
    elif event_derek_talk_jaq == 2:
        $ event_derek_talk_jaq = 3
        p "Hey... you have a pretty serious look on your face."
        p "What's on your mind?"
        jaq "I'm thinking about getting the fuck out of here."
        jaq worried "Well... specifically {i}how{/i}."
        p "Got any ideas?"
        if tom_location == "Cave":
            show tom surprised
        jaq serious "We're going to have to fight them."
        if tom_location == "Cave":
            show tom worried
        jaq "I don't see any way around it."
        if tom_location == "Cave":
            "Tom shifted uncomfortably, clearly worried about that concept."
        jaq "The only place we can be sure they'll be at is that camp they set up."
        jaq normal "... But that's also where their supplies will be."
        show jaq worried
        "She leaned back and sighed."
        jaq "We don't even have any weapons."
        if "item_sacrificial_knife" in inventory:
            menu:
                " "
                "Stay silent" if True:
                    "I decided not to bring up the knife I found."
                    "There's only one..."
                    "And I can be sure to use it when we need it."
                "\"I have a knife.\"" if True:
                    "I brought out the decorative knife and showed it to Jaqueline."
                    show tom normal
                    jaq surprised "Holy shit!"
                    jaq question "Where the hell did you get THAT?"
                    show tom worried
                    "Tom recoiled a bit from the sight of it."
                    p "I got it from those lizard mask guys."
                    p "They were... attacking Tom with it."
                    p "I sneaked in and managed to..."
                    p "Kill them."
                    jaq surprised "What!?"
                    show jaq question
                    "She sat up straighter."
                    show tom normal
                    jaq smile "Then that means... there's only three of them left!"
                    if (derek_status == "Dead" or derek_status == "Stabbed"):
                        if machete_unlock == 1:
                            show jaq question
                            p "Actually... two."
                            show jaq surprised
                            show tom surprised
                            if meme_mode:
                                p "I managed to stab the twink guy."
                            elif True:
                                p "I managed to stab Derek."
                            show tom normal
                            show jaq serious
                            p "Then I followed him back to camp and..."
                            show jaq question
                            p "Well, I'm not really sure what I saw."
                            p "But he's definitely dead now."
                            show jaq smile
                            show tom wistful
                            jaq "Even better!"
                        elif True:
                            show jaq question
                            p "Actually... two."
                            show jaq surprised
                            show tom surprised
                            if meme_mode:
                                p "I managed to stab the twink guy."
                            elif True:
                                p "I managed to stab Derek."
                            jaq "You did!?"
                            show jaq question
                            jaq "Are you sure he's actually dead?"
                            if derek_status == "Stabbed":
                                p "I mean... I'm pretty sure."
                                p "I got him pretty good!"
                            elif True:
                                p "Oh, I made sure."
                            show jaq smile
                            show tom wistful
                            jaq "Well that's even better odds!"
                    jaq "So..."
                    show tom normal
                    jaq question "Do you know how to use that thing?"
                    p "The... the knife?"
                    if derek_status == "Dead" and machete_unlock == 0:
                        show jaq semiserious
                        show tom wistful
                        p "I think I did a pretty good job with it so far."
                    elif True:
                        p "I mean..."
                        show tom wistful
                        show jaq semiserious
                        p "Pointy side out, right..?"
                    "My attempt at humour didn't seem to amuse Jaqueline."
                    jaq normal "Look... I've taken self defense classes."
                    jaq "I could use it."
                    jaq serious "And... I want another chance at that guy."
                    menu:
                        " "
                        "Give Jaqueline the knife" if True:
                            show jaq normal
                            "I honestly don't really want to stab anyone else."
                            show tom normal
                            "I handed it over."
                            $ inventory.remove("item_sacrificial_knife")
                            $ renpy.notify("Sacrificial Knife Removed!")
                            $ event_derek_jaq_knife = 1
                            "She studied it in her hands."
                            jaq worried "Jesus, this thing is creepy."
                            jaq normal "But it's sharp."
                            jaq semiserious "That's all that matters."
                            "I nodded in agreement."
                            jaq normal "Thank you, [player_name]."
                            jaq "You won't regret this."
                            "I managed a weak smile."
                            show jaq smile
                            p "I really do think we have a better chance this way."
                            show jaq normal
                            $ arrivedby = "special"
                            jump derek_turn_nostats
                        "Keep the knife" if True:
                            show jaq normal
                            p "I don't know..."
                            p "I think I can handle it."
                            jaq "..."
                            jaq worried "Yeah, I suppose you're right."
                            jaq semiserious "But you better be watching our backs, ok?"
                            show jaq normal
                            show tom normal
                            p "You got it."
                            $ arrivedby = "special"
                            jump derek_turn_nostats
        elif True:
            "I leaned back and sighed."
            "She's right."
        p "I'm sure we can figure something out..."
        jaq worried "Yeah."
        jaq "I guess we'll have to."
        $ arrivedby = "special"
        jump derek_turn_nostats
    elif True:
        "I looked at Jaqueline, who appeared to be deep in thought."
        "Maybe I shouldn't interrupt her."
        $ arrivedby = "special"
        jump derek_turn_nostats
label event_derek_talk_rich:
    $ phase = "event"
    $ arrivedby = "special"
    if event_derek_talk_rich == 0:
        $ event_derek_talk_rich = 1
        "I turned to the man with the bruise."
        p "So, how did you get here?"
        show rich normal
        "He eyed me suspiciously."
        rich "Same as you."
        rich worried "What does it matter anyway?"
        if tom_location == "Cave":
            show tom worried
        rich "They dragged us here to kill us."
        rich "We don't have any food or water."
        rich "We're all hurt and exhausted."
        "I looked down."
        if jaq_location == "Cave":
            show jaq worried
        rich angry "So we're either gonna go out there and get killed, or we're gonna stay in here and die of thirst or whatever."
        rich "We're fucked."
        show rich worried
        "I tried to think of a response."
        $ stat_sanity -= 5
        "But I couldn't really dispute any of that..."
        $ arrivedby = "special"
        jump derek_turn_nostats
    elif event_derek_talk_rich == 1:
        $ event_derek_talk_rich = 2
        p "How did you get that bruise?"
        rich worried "..."
        p "I saw it on you when you got here."
        rich normal "Look, I'm only here because there's nowhere else to go."
        if meme_mode:
            p "Oh yeah?"
            p "Are you touchy about it?"
            p "Don't wanna talk about it?"
            p "Don't want to elaborate on what you were up to when you were caught? Huh?"
        rich angry "Mind your own business."
        show rich worried
        $ arrivedby = "special"
        jump derek_turn_nostats
    elif True:
        if meme_mode:
            "I looked over to Dick."
        elif True:
            "I looked over to Richard."
        "The look on his face told me he wasn't willing to chat anymore."
        $ arrivedby = "special"
        jump derek_turn_nostats

label event_derek_save_rich:
    $ phase = "event"
    if jaq_location == "Cave":
        jaq "Hey."
        jaq question "Do you hear that?"
        p "Huh?"
        jaq semiserious "Shhh."
    elif True:
        tom "Hey... [player_name]?"
        tom "Do you... hear that?"
        p "Huh?"
        tom worried "Outside..."
    "I listened carefully."
    "Then I heard it."
    "Rocks moving... hurried steps."
    if tom_location == "Cave":
        show tom normal
    if jaq_location == "Cave":
        show jaq normal
    p "Someone is outside..."
    if jaq_location == "Cave":
        jaq question "Think we should look?"
    elif True:
        tom "Think we should look?"
    menu:
        " "
        "Take a look" if True:
            p "We have to check."
            if jaq_location == "Cave":
                show jaq semiserious
                "Jaqueline tensed up."
                jaq question "Are you sure?"
                show jaq semiserious
            elif True:
                show tom worried
                "Tom fidgeted nervously."
                tom normal "Are you sure?"
            p "Yeah... it could be one of us."
            "I walked over to the cave entrance as quietly as possible."
            "Then I slowly moved the door and covering, peeking out a crack."
            $ map_location = "Hill"
            play ambient "music/ambient_desert_wind.ogg" fadein 1.0
            call derek_display_subroutine from _call_derek_display_subroutine_33
            "..."
            show rich turned with dissolve
            rich "God... I think I lost him..."
            "I gasped at the sight of him."
            if event_derek_encounter_1 == 1:
                "It's the guy who threw me under the bus to Derek!"
                "Anger welled up in my chest."
            elif True:
                "It's another captive!"
            menu:
                " "
                "Save him" if True:
                    if event_derek_encounter_1 == 1:
                        "I pushed the anger back down."
                        "This is life or death."
                        "I can't afford to hold a grudge here..."
                    elif True:
                        "I have to help him!"
                "Leave him" if True:
                    if event_derek_encounter_1 == 1:
                        "He's already shown he can't be trusted."
                        "I'm not going to put anyone else at risk."
                    elif True:
                        "..."
                        "It's just too much of a risk."
                    $ arrivedby = "new"
                    $ map_location = "Cave"
                    call derek_display_subroutine from _call_derek_display_subroutine_44
                    play ambient "music/ambient_cave.ogg" fadein 1.0
                    "I closed the door and went back into the cave without alerting him."
                    if jaq_location == "Cave":
                        jaq question "Well?"
                        "I shook my head."
                        if tom_location == "Cave":
                            show tom worried
                        jaq worried "Ah."
                    elif True:
                        tom "Well?"
                        "I shook my head."
                        tom worried "Oh..."
                    jump event_derek_dont_save_rich
                "Throw a rock at him" if meme_mode:
                    "I grabbed a rock and chucked it at his head."
                    hide rich with Dissolve(0.1)
                    show rich surprised with Dissolve(0.1)
                    rich "Ow, what the fuck!?"
                    scene black with dissolve
                    play sound "<from 0.0 to 4.3>music/sfx_impact.ogg"
                    "I leaped out at him and attacked him."
                    "He was caught off guard, and I landed several blows before he could react."
                    "He regained his balance and assessed the situation before turning on his heel and running."
                    p "YEAH, YOU BETTER RUN!"
                    $ arrivedby = "new"
                    $ map_location = "Cave"
                    call derek_display_subroutine from _call_derek_display_subroutine_34
                    play ambient "music/ambient_cave.ogg" fadein 1.0
                    "I dusted off my hands and went back into the cave."
                    if jaq_location == "Cave":
                        jaq question "Well?"
                        p "Must have been one of those desert mice."
                        jaq "I heard pained grunts."
                        p "It was a big mouse."
                        if tom_location == "Cave":
                            show tom worried
                        jaq worried "Ah."
                    elif True:
                        tom "Well?"
                        p "Must have been one of those desert mice."
                        tom worried "I thought I heard pained grunts..."
                        p "It was a big mouse."
                    jump event_derek_dont_save_rich
            p "Psst!"
            hide rich with Dissolve(0.1)
            show rich surprised with Dissolve(0.1)
            rich "Huh?"
            p "Over here!"
            "I opened the door to the cave."
            rich normal "Woah!"
            rich "It's YOU!"
            p "Yeah! Shh!"
            p "Get in here!"
            scene black with dissolve
            "He stumbled over rocks towards the entrance and climbed inside."
            $ arrivedby = "new"
            $ map_location = "Cave"
            call derek_display_subroutine from _call_derek_display_subroutine_45
            play ambient "music/ambient_cave.ogg" fadein 1.0
            $ rich_location = "Cave"
            if jaq_location == "Cave":
                jaq question "Well..?"
                show rich with dissolve
                "The thin, exhausted looking man crawled into the cave after me."
                jaq surprised "Oh!"
                show jaq normal
            elif True:
                tom worried "Did you find any-"
                show rich with dissolve
                "The thin, exhausted looking man crawled into the cave after me."
                tom surprised "Oh!"
                show tom normal
            rich worried "I thought I was gonna die out there."
            p "We're safe here."
            p "For now..."
            "He was breathing hard and leaned against the wall."
            if event_derek_encounter_1 == 1:
                show rich normal
                "He stopped for a moment and stared at me."
                rich worried "Uh... look..."
                rich "About before..."
                "I waited for him to continue, probably revealing my feelings easily in my expression."
                rich "I'm sorry."
                rich normal "I just got really scared and I panicked."
                p "Yeah... sure."
            elif True:
                rich worried "That asshole with the... fox mask."
                rich "He chased me forever."
            p "Well... you can rest here for now... uh..."
            if meme_mode:
                $ rich_name = "Dick"
            elif True:
                $ rich_name = "Richard"
            rich normal "Richard."
            if meme_mode:
                p "Dick."
                rich "I... yeah."
                rich "Fine."
            elif True:
                p "Richard."
            p "I'm [player_name]."
            p "We can catch our breath, then we'll figure out what to do later."
            show rich worried
            if jaq_location == "Cave" and tom_location == "Cave" and achievement.has("ach_buddies") != True:
                $ persistent.ach_buddies = True
                $ achievement.grant("ach_buddies")
                init:
                    $ achievement.register("ach_buddies")
                    $ achievement.sync()
                    $ renpy.save_persistent()
                    if persistent.ach_buddies == True and achievement.has("ach_buddies") != True:
                        $ achievement.grant("ach_buddies")
                        $ achievement.register("ach_buddies")
                        $ achievement.sync()
            "He nodded in agreement and found a place to settle down."
            $ arrivedby = "special"
            jump derek_turn_nostats
        "Stay inside the cave" if True:
            if jaq_location == "Cave":
                show jaq worried
            if tom_location == "Cave":
                show tom worried
            p "We can't take any chances."
            if jaq_location == "Cave":
                jaq question "What if it's one of ours?"
                p "..."
                p "At this point... the chances of that are pretty low."
                jaq worried "... Yeah."
                jaq "I guess you're right."
                jaq "We better sit tight."
                show jaq normal
            elif True:
                tom worried "What if it's another captive?"
                p "..."
                p "At this point... the chances of that are pretty low."
                tom normal "... Oh."
                tom worried "I guess you're right..."
                p "We better sit tight."
            label event_derek_dont_save_rich:
            if meme_mode:
                pass
            elif True:
                "We continued to listen to the steps around us."
                "As we stayed in perfect silence, they eventually faded away."
                "I sighed in relief."
            $ arrivedby = "special"
            jump derek_turn_nostats
label event_derek_sanity_sequence:
    $ phase = "event"
    $ map_location = "Deep Desert"
    call derek_display_subroutine from _call_derek_display_subroutine_46
    $ renpy.music.play("music/music_achtung.ogg", channel='music', loop=True, synchro_start=True, fadein=5.0)
    $ renpy.music.play("music/music_achtung_2.ogg", channel='music2', loop=True, synchro_start=True, fadein=5.0)
    $ renpy.music.set_volume(0, 0, channel="music2")

    "... Where am I?"
    "I walked forward, then turned around."
    "I don't..."
    "Remember this place."
    label event_derek_sanity_menu_1:
    scene bg_derek_deepdesert
    $ phase = "adventure"
    menu:
        " "
        "Go forward" if True:
            $ phase = "event"
            "I think I'm already going the right way."
            "I just need to keep going."
            jump event_derek_sanity_sequence_2
        "Use the sky" if True:
            $ phase = "event"
            if 7 <= hours <= 19:
                "I looked up at the sky."
                "Okay the sun rises... in the east, and sets in the west..."
                "And it's..."
                "Which way did I come from?"
                "North is..."
                "I don't know where I came from..."
                "I clutched my head."
                "This isn't helping!"
                jump event_derek_sanity_sequence_2
            elif True:
                "Okay, so I just need to use the stars."
                "There's the big dipper and... uh..."
                "Where is it?"
                "I don't..."
                "I can't tell where anything is."
                "They just look... wrong."
                "I can't tell which stars are which!"
                "This isn't helping!"
                jump event_derek_sanity_sequence_2
        "Go back where you came from" if True:
            $ phase = "event"
            "Well wherever I am is wrong, so I just need to go back."
            "I turned around and started walking."
            "I walked for an hour..."
            "But nothing familiar seemed to come into view."
            "Did I get something wrong?"
            jump event_derek_sanity_sequence_2
label event_derek_sanity_sequence_2:
    $ phase = "event"
    $ hours += 1
    $ total_hours += 1
    if 8 <= hours <= 18:
        $ stat_temp += 5
    elif hours == 7 or hours == 19:
        $ stat_temp += 10
    elif True:
        if temp >= 60:
            $ stat_temp -= 10
    $ stat_food -= 1
    if wound == 1:
        $ stat_health -= 3
    if wound == 2:
        $ stat_health -= 5
    if sleep > 0:
        $ energy += 3
        $ sleep -= 1
        if energy > 24:
            $ energy = 24
            $ sleep = 0
    elif True:
        if food <= 0 or encumbered == 1:
            $ stat_energy -= 3
        elif True:
            $ stat_energy -= 1
    scene black with dissolve
    scene bg_derek_deepdesert with dissolve
    "I walked forward some more."
    "Okay."
    "I need to not panic."
    "If I just calm down..."
    "I can get back."
    label event_derek_sanity_menu_2:
    $ phase = "adventure"
    menu:
        "Keep walking forward" if True:
            $ phase = "event"
            "I just need to keep at it."
            "I walked towards the horizon."
            "I bet everything is just over there."
            "I wiped my sweat and tried to ignore my own heavy breathing."
            "I have to keep walking..."
            jump event_derek_sanity_sequence_3
        "Turn around" if True:
            $ phase = "event"
            "I switched direction and started walking."
            "Process of elimination."
            "This has to be the right way now."
            "I walked towards the horizon."
            "I bet everything is just over there."
            "I wiped my sweat and tried to ignore my own heavy breathing."
            "I have to keep walking..."
            jump event_derek_sanity_sequence_3
label event_derek_sanity_sequence_3:
    $ phase = "event"
    $ hours += 1
    $ total_hours += 1
    if 8 <= hours <= 18:
        $ stat_temp += 5
    elif hours == 7 or hours == 19:
        $ stat_temp += 10
    elif True:
        if temp >= 60:
            $ stat_temp -= 10
    $ stat_food -= 1
    if wound == 1:
        $ stat_health -= 3
    if wound == 2:
        $ stat_health -= 5
    if sleep > 0:
        $ energy += 3
        $ sleep -= 1
        if energy > 24:
            $ energy = 24
            $ sleep = 0
    elif True:
        if food <= 0 or encumbered == 1:
            $ stat_energy -= 3
        elif True:
            $ stat_energy -= 1
    scene black with dissolve
    scene bg_derek_deepdesert with dissolve
    "My legs are feeling... weak."
    "I looked in every direction."
    "It's just... nothing."
    "I don't know where I am on Earth at all."
    "I'm alone..."
    "I want to go home."
    "I just want to go home..."
    "I fell to my knees."
    "Why did this happen?"
    "Where am I?"
    "I squeezed the sand in my hands."

    $ renpy.music.set_volume(0, 3, channel="music")
    $ renpy.music.set_volume(1.0, 3, channel="music2")

    label event_derek_sanity_menu_3:
    scene bg_derek_deepdesert at pulse
    $ phase = "adventure"
    menu:
        " "
        "Pull it together" if True:
            $ phase = "event"
            jump event_derek_sanity_sequence_4
        "Try harder" if True:
            $ phase = "event"
            jump event_derek_sanity_sequence_4
        "Keep going" if True:
            $ phase = "event"
            jump event_derek_sanity_sequence_4
label event_derek_sanity_sequence_4:
    $ phase = "event"
    $ hours += 1
    $ total_hours += 1
    if 8 <= hours <= 18:
        $ stat_temp += 5
    elif hours == 7 or hours == 19:
        $ stat_temp += 10
    elif True:
        if temp >= 60:
            $ stat_temp -= 10
    $ stat_food -= 1
    if wound == 1:
        $ stat_health -= 3
    if wound == 2:
        $ stat_health -= 5
    if sleep > 0:
        $ energy += 3
        $ sleep -= 1
        if energy > 24:
            $ energy = 24
            $ sleep = 0
    elif True:
        if food <= 0 or encumbered == 1:
            $ stat_energy -= 3
        elif True:
            $ stat_energy -= 1
    scene black with dissolve
    call derek_display_subroutine from _call_derek_display_subroutine_49
    "I strained to get back to my feet."
    label event_derek_sanity_sequence_4_water:
    "I took a step forward and fell." with vpunch
    "No... no no no..."
    "Please, just let me find my way back!"
    "I crawled forward."
    "..."
    "Why..."
    scene bg_derek_deepdesert at pulse
    "I collapsed into the sand."
    if meme_mode:
        demon "{cps=10}{font=images/feral.regular.ttf}{size=25}You{/size}{/font}r min{font=images/feral.regular.ttf}{size=25}d i{/size}{/font}s broken.{/cps}"
    elif True:
        demon "{cps=10}{font=images/gatosrunes.ttf}{size=25}You{/size}{/font}r min{font=images/gatosrunes.ttf}{size=25}d i{/size}{/font}s broken.{/cps}"
    "That voice again..."
    "I looked up and listened."
    demon "{cps=10}It's fun to watch...{/cps}"
    "I can... understand it now?"
    demon "{cps=10}Death is only the beginning...{/cps}"
    scene black with eyedissolve
    $ renpy.music.set_volume(1.0, 0, channel="music")
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    stop ambient fadeout 1.0
    "I closed my eyes."
    "I had no strength left to fight."
    demon "{cps=10}Hahaha...{/cps}"
    $ quick_menu = False
    window hide
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_derek.add("You wandered the desert")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_44
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You wandered the desert")
    $ renpy.pause(hard=True)

label event_derek_endgame:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        jaq "Hey."
        jaq "Wake up."
        $ sleep = 0
        call derek_display_subroutine from _call_derek_display_subroutine_50
        "I groaned and sat up."
    elif True:
        jaq question "Hey... you got a minute, [player_name]?"
    p "What's up?"
    if tom_location == "Cave":
        show tom worried
    if rich_location == "Cave":
        show rich normal
    if tom_location == "Cave" or rich_location == "Cave":
        jaq worried "We've been talking it over and..."
    elif True:
        jaq worried "I've been thinking it over and..."
    jaq semiserious "I think we need to make a move."
    jaq normal "Go on the offensive, I mean."
    p "You think we should try to attack them?"
    jaq semiserious "Yeah."
    jaq "It's really our only chance."
    jaq worried "There's nothing to eat or drink anywhere."
    jaq "And they have to have gotten here somehow."
    jaq semiserious "If we want to make it out of here... we're going to have to get our hands dirty."
    menu:
        " "
        "\"I agree, it's now or never.\"" if True:
            if tom_location == "Cave":
                show tom wistful
            jaq smile "Yes!"
            if tom_location == "Cave" or rich_location == "Cave":
                jaq "We've got a much better chance with you on board, too."
            elif True:
                jaq "We've got a much better chance together than apart."
            if tom_location == "Cave":
                show tom normal
            jaq semiserious "So, here's the plan."
            if 7 <= hours <= 19:
                jaq "We'll have to wait until it's dark."
                jaq serious "Then, we're gonna hit them right at their camp."
                $ hour_adder = 24 - hours
                $ hours += hour_adder
                $ total_hours += hour_adder
            elif True:
                jaq serious "We're gonna hit them right at their camp."
            jaq semiserious "It's the best chance we'll get to find them, and to get their supplies."
            if tom_location == "Cave" or rich_location == "Cave":
                jaq "We'll use the darkness to sneak up."
                jaq "Then, hopefully, we can surround them."
                jaq "You guys keep an eye on me, and I'll point out a target."
                jaq serious "And we'll all jump him."
                jaq semiserious "We might be able to get the upper hand."
                "Everyone looked at each other."
                if tom_location == "Cave":
                    tom normal "Well..."
                    tom worried "I'll do my best."
                    tom "I think that's the best plan we could really hope for."
                elif True:
                    rich worried "That's as good a plan as any, I guess."
                    rich normal "We might as well go for it."
                p "Agreed."
                jaq "All right, come on."
                scene black with dissolve
            play ambient "music/ambient_desert.ogg" fadein 1.0
            $ map_location = "Camp"
            jump event_derek_endgame_2
        "\"I just don't think we can take that risk...\"" if True:
            if rich_location == "Cave":
                show rich worried
            if tom_location == "Cave":
                show tom worried
            jaq angry "Seriously!?"
            jaq serious "..."
            jaq worried "Well, it's not like I can force you."
            if tom_location == "Cave" or rich_location == "Cave":
                jaq semiserious "We're not going to die here of thirst without fighting."
                jaq "We're gonna go, with or without you."
            elif True:
                jaq semiserious "I'm not going to die here of thirst without fighting."
                jaq "I'm gonna go, with or without you."
            jaq "There's just no other option left."
            "She started to leave, then paused and looked back."
            jaq worried "... Don't die, [player_name]."
            $ event_derek_endgame_missed = 1
            $ arrivedby = "special"
            if tom_location == "Cave":
                $ tom_location = "Endcamp"
            if jaq_location == "Cave":
                $ jaq_location = "Endcamp"
            if rich_location == "Cave":
                $ rich_location = "Endcamp"
            call derek_display_subroutine from _call_derek_display_subroutine_51
            "I watched her leave and wondered if I was making the right choice."
            "I sat down in the cave, alone."
            jump derek_turn_nostats
label event_derek_endgame_2:
    $ phase = "event"
    $ persistent.cgs_derek.add("cg_derek_showdown_far")
    $ renpy.save_persistent()
    scene cg_derek_showdown_far with dissolve
    "We travelled quickly to the camp."
    "It was extremely quiet..."
    jaq "Hey... there it is."
    jaq "I think I see one of them!"
    p "Okay, how should we go in?"
    if tom_location == "Cave" and rich_location != "Cave":
        jaq "I'll sneak in behind, and you two can stay on this side."
        jaq serious "I'm gonna jump him."
        tom surprised "What!?"
        jaq normal "Do you have a better idea?"
        tom worried "What if I... distract him?"
        tom normal "I'll come in from the side, you come in from the back, and when he sees me, you can jump him."
        jaq surprised "That's... actually a really good idea."
        jaq normal "[player_name], your job is making sure that Tom's okay."
        p "Got it."
        jaq serious "Come on, then."
        jump event_derek_endgame_live
    elif True:

        if tom_location != "Cave" and rich_location != "Cave":
            jaq "I'll sneak in behind, and you can stay on this side."
        elif True:
            jaq "I'll sneak in behind, and you guys can stay on this side."
        jaq serious "I'm gonna jump him."
        p "What!? Now!?"
        jaq normal "Do you have a better idea?"
        if rich_location == "Cave":
            rich "Let's just get this over with."
        p "..."
        jaq serious "Come on, then."
        if rich_location == "Cave":
            jump event_derek_endgame_sabotage
        elif True:
            jump event_derek_endgame_onlyjaq

label event_derek_endgame_live:
    $ phase = "event"

    if event_derek_jaq_knife == 0:
        "I nervously approached the camp."
        "Jaqueline was already out of sight."
        "Now that I was closer, I could get a better look."
        play music "music/jacks_theme.ogg" fadein 5.0
        $ persistent.cgs_derek.add("cg_derek_showdown_close")
        $ renpy.save_persistent()
        scene cg_derek_showdown_close with dissolve
        "It's the man with the dog mask..."
        play sound "music/sfx_bottle_clink.ogg"
        scene black with dissolve
        "The clink of an empty bottle immediately grabbed everyone's attention."
        "I looked at the source of the sound and saw a very terrified Tom."
        "The man wasted no time lunging towards Tom with a knife."
        p "No!"
        "He slashed at Tom before I could get to them."
        $ persistent.cgs_derek.add("cg_derek_showdown_baddog")
        scene cg_derek_showdown_baddog
        play sound "<from 0.0 to 1.0>music/sfx_knife_stab.ogg"
        "I jumped at him, plunging my knife into his shoulder." with vpunch
        "He howled in pain as Tom scrambled away from us."
        scene black with dissolve
        "His attention was turned to me."
        jaq surprised "Wait!"
        tom surprised "[player_name]!!!"
        $ persistent.cgs_derek.add("cg_derek_showdown_jackstab1")
        scene cg_derek_showdown_jackstab1
        play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
        "He pushed me to the ground." with vpunch
        "My knife was still in his shoulder!"
        "I desperately tried to reach it."
        if machete_unlock == 1:
            jump event_derek_endgame_machete
        $ stat_health -= 100
        $ persistent.cgs_derek.add("cg_derek_showdown_jackstab2")
        $ renpy.save_persistent()
        scene cg_derek_showdown_jackstab2
        play sound "<from 0.0 to 1.0>music/sfx_impact_thud.ogg"
        "His own knife slammed into my chest." with vpunch
        stop music fadeout 15.0
        "Everything seemed to slow down."
        scene cg_derek_showdown_jackstab2_blur with dissolve
        "I heard screaming."
        scene black with eyedissolve
        hide screen effect_health
        hide screen effect_ice
        "Motion blurred above me as the knife was torn from his shoulder."
        "They're fighting..."
        "I can't move."
        "I think..."
        "I think they got him."
        "That brought a smile to my face."
        pause 1.0
        $ quick_menu = False
        window hide
        hide screen effect_health
        hide screen effect_ice
        hide screen status
        $ persistent.endings_derek.add("You went down in the escape")
        $ persistent.deathcounter += 1
        $ renpy.save_persistent()
        call achievement_checker from _call_achievement_checker_45
        play music "<from 0.3>music/you_died.ogg"
        scene bg_endslate with blooddissolve
        show screen bg_endslate_text("You Died","You went down in the escape")
        $ renpy.pause(hard=True)
    elif True:
        "I nervously approached the camp."
        "Jaqueline was already out of sight."
        "Now that I was closer, I could get a better look."
        play music "music/jacks_theme.ogg" fadein 5.0
        $ persistent.cgs_derek.add("cg_derek_showdown_close")
        $ renpy.save_persistent()
        scene cg_derek_showdown_close with dissolve
        "It's the man with the dog mask..."
        scene black with dissolve
        play sound "music/sfx_bottle_clink.ogg"
        "The clink of an empty bottle immediately grabbed everyone's attention."
        "I looked at the source of the sound and saw a very terrified Tom."
        "The man wasted no time lunging towards Tom with a knife."
        p "No!"
        "He slashed at Tom before I could get to them."
        $ persistent.cgs_derek.add("cg_derek_showdown_backstab")
        $ renpy.save_persistent()
        scene cg_derek_showdown_backstab
        play sound "<from 0.0 to 1.0>music/sfx_knife_stab.ogg"
        "I lunged towards Tom as Jaqueline sprang from behind the masked man and plunged our knife into his back." with hpunch
        "We stood back as he howled in pain."
        scene black with dissolve
        "He spun around with the knife still lodged in his back, grabbing Jaqueline."
        "He can't stop all of us!"
        play sound "<from 1.0>music/sfx_knife_stab_repeated.ogg"
        "I leapt forward and gripped the hilt of the blade, ripping it out of his back."
        "He screamed into his mask as he stumbled."
        "Jaqueline grabbed his arm and twisted it to the side to throw him off balance."
        play sound "<from 0.0 to 1.0>music/sfx_knife_drop.ogg"
        "As soon as he fell, she stomped on his hand holding his own knife."
        "Adrenaline surged in my body."
        "I'm not taking any more chances."
        $ persistent.cgs_derek.add("cg_derek_showdown_neck")
        $ renpy.save_persistent()
        scene cg_derek_showdown_neck with dissolve
        "I jumped on top of him, tore his mask off, and held my knife under his neck."
        p "You picked the wrong people, you son of a bitch."
        "I could see him gritting his teeth."
        "Nothing more to say."
        "I didn't hesitate."
        scene black
        play sound "<from 0.0 to 1.0>music/sfx_knife_stab.ogg"
        "I tore the blade across his neck." with hpunch
        stop music fadeout 5.0
        scene cg_derek_showdown_bleedout with dissolve
        "Tom made some sound behind me."
        "I looked to see that he'd turned away."
        "But Jaqueline kept her eyes on the man bleeding out beneath me."
        "I soon knew exactly what she was thinking as she spat on him."
        "He wasn't moving anymore."
        call derek_display_subroutine from _call_derek_display_subroutine_52
        "I got back up, shakily."
        "I didn't think I had it in me to..."
        show tom worried with dissolve:
            yalign 1.0
            xalign 0.20
        tom "Uh..."
        tom "I think we better look through his jacket."
        "I was snapped out of my thoughts."
        show jaq semiserious with dissolve:
            yalign 1.0
            xalign 0.80
        jaq "He's right."
        jaq worried "If there's a ticket out of here, it's on him."
        "Tom gulped and bent down to search the body."
        tom surprised "Woah!"
        tom happy "Guys! There's keys... and a map!"
        jaq smile "Sounds like we're getting the fuck out of here!"
        if achievement.has("ach_better_together") != True:
            $ persistent.ach_better_together = True
            $ achievement.grant("ach_better_together")
            init:
                $ achievement.register("ach_better_together")
                $ achievement.sync()
                $ renpy.save_persistent()
                if persistent.ach_better_together == True and achievement.has("ach_better_together") != True:
                    $ achievement.grant("ach_better_together")
                    $ achievement.register("ach_better_together")
                    $ achievement.sync()
        scene black with dissolve
        stop ambient fadeout 1.0
        "Thankfully, the map was relatively easy to follow."
        "It led to a covered stash of fueled up vehicles."
        "With the keys, we got moving immediately."
        "Within a few hours, we made it to a gas station and civilization."
        "It would take a long time to recover."
        "But we were alive."
        $ quick_menu = False
        play music "<from 0.5>music/music_desert_escape.ogg" fadein 1.0
        pause 1.0
        window hide
        hide screen effect_health
        hide screen effect_ice
        hide screen status
        $ persistent.endings_derek.add("You escaped with friends")
        $ renpy.save_persistent()
        call achievement_checker from _call_achievement_checker_46
        scene bg_endslate_survival with zoomdissolve
        show screen bg_endslate_survival_text("You Lived","You escaped with friends")
        $ renpy.pause(hard=True)
label event_derek_endgame_sabotage:
    $ phase = "event"
    "I nervously approached the camp."
    "Everyone was already out of sight."
    "Now that I was closer, I could get a better look."
    play music "music/jacks_theme.ogg" fadein 5.0
    $ persistent.cgs_derek.add("cg_derek_showdown_close")
    $ renpy.save_persistent()
    scene cg_derek_showdown_close with dissolve
    "It's the man with the dog mask..."
    "I looked out and was able to just make out Jaqueline."
    "It looks like she's getting ready to attack..."
    "I steeled myself."
    scene black with dissolve
    rich scared "Behind you!"
    "I jumped at the sudden shout."
    "The man in the mask looked and saw Jaqueline."
    "I checked behind myself."
    "No..."
    "The masked man lunged at Jaqueline."
    "He wasn't warning us!"
    if meme_mode:
        "I spotted Dick..."
    elif True:
        "I spotted Richard..."
    "Running away."
    "A scream ripped my attention away from the traitor."
    p "NO!!!"
    $ persistent.cgs_derek.add("cg_derek_showdown_jaqdown")
    $ renpy.save_persistent()
    scene cg_derek_showdown_jaqdown with dissolve
    "Jaqueline was already on the ground, bleeding."
    "He turned to me."
    if tom_location == "Cave":
        "I thought about Tom."
        "We don't really have a chance anymore..."
        "Maybe at least he can escape."
        p "Tom! Just run!"
    "His attention was completely on me now."
    "I stepped backwards."
    jack empty "You guys really fucked up this time."
    "He held up the knife, still dripping with Jaqueline's blood."
    jack empty "Don't worry..."
    jack empty "Once I'm done with you, I'll give your coward friend what he deserves too."
    scene black with dissolve
    "He laughed as he lunged for me."
    if "item_sacrificial_knife" in inventory:
        "I fumbled for the knife I'd gotten from the cave."
        play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
        "I flinched as he faked a punch before kicking my legs out from under me." with vpunch
        play sound "<from 0.0 to 1.0>music/sfx_knife_drop.ogg"
        "I cried out in despair as the knife was thrown from me."
    elif True:
        play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
        "I flinched as he faked a punch before kicking my legs out from under me." with vpunch
    $ persistent.cgs_derek.add("cg_derek_showdown_jackstomp")
    $ renpy.save_persistent()
    scene cg_derek_showdown_jackstomp with dissolve
    "He placed a boot on my chest, keeping me down."
    jack empty "I'd really like to play with you longer."
    jack empty "But I don't want to let him get too far."
    $ stat_health -= 10
    play sound "<from 0.0 to 1.0>music/sfx_impact_bone.ogg"
    "He brought his foot back up, and before I could shield myself, he brought it down on my head." with vpunch
    $ stat_health -= 40
    play sound "<from 1.5 to 2.5>music/sfx_impact_bone.ogg"
    "The force dazed me as he did it again, harder." with vpunch
    "I heard a crack."
    $ stat_health -= 100
    scene black
    play sound "<from 2.9>music/sfx_impact_bone.ogg"
    stop music
    stop ambient
    hide screen effect_health
    hide screen effect_ice
    "I was helpless by the time he stomped a final time." with vpunch
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_derek.add("You were betrayed")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_47
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You were betrayed")
    $ renpy.pause(hard=True)
label event_derek_endgame_onlyjaq:
    $ phase = "event"
    "I nervously approached the camp."
    "Jaqueline was already out of sight."
    "Now that I was closer, I could get a better look."
    play music "music/jacks_theme.ogg" fadein 5.0
    $ persistent.cgs_derek.add("cg_derek_showdown_close")
    $ renpy.save_persistent()
    scene cg_derek_showdown_close with dissolve
    "It's the man with the dog mask..."
    "I looked out and was able to just make out Jaqueline."
    scene black with dissolve
    "She nodded to me and lunged forward."
    if event_derek_jaq_knife == 1:
        play sound "<from 0.0 to 1.0>music/sfx_knife_stab.ogg"
        "She leapt at him from the darkness and plunged the knife into his shoulder."
        "He roareded in pain and surprise, then turned, slamming her to the side."
    elif True:
        "She leapt at him from the darkness and kicked at him, trying to throw him off balance."
        "He stumbled as he yelled in surprise-"
        "But he quickly gained his footing and turned, slamming her to the side."
    "It's now or never."
    if "item_sacrificial_knife" in inventory:
        "I ran at him with the knife and slashed at him."
    elif True:
        "I ran at him, readying a punch."
    "But he managed to dodge my attack."
    play sound "<from 0.0 to 1.0>music/sfx_impact_sand.ogg"
    "I stumbled forward, and he quickly swiped me off balance." with vpunch
    "I fell face first into the ground below."
    $ persistent.cgs_derek.add("cg_derek_showdown_attempted")
    $ renpy.save_persistent()
    scene cg_derek_showdown_attempted with dissolve
    "I couldn't get up in time as he turned back to Jaqueline."
    p "NO!!!"
    if event_derek_jaq_knife == 1 or "item_sacrificial_knife" in inventory:
        "He unsheathed his own knife and crouched over her."
    elif True:
        "He unsheathed a knife and crouched over her."
    jack empty "Nice try."
    scene black with dissolve
    play sound "<from 0.0 to 1.0>music/sfx_knife_stab.ogg"
    "I scrambled to get up but couldn't stop him from plunging the knife into Jaqueline."
    p "No... no..."
    jack "Don't worry..."
    jack serious "You're next."
    $ stat_health -= 10
    scene black
    play sound [ "<from 0.0 to 1.0>music/sfx_impact_thud.ogg","music/sfx_ears_ring.ogg" ]
    "His boot slammed into my gut." with vpunch
    "For a moment, there was only the ringing in my ears and the click of a lighter."
    $ persistent.cgs_derek.add("cg_derek_showdown_standover")
    $ renpy.save_persistent()
    scene cg_derek_showdown_standover with dissolve
    "I curled in pain as I heard Jaqueline's wet coughing."
    jack empty "You guys coming to me is kind of admirable."
    $ persistent.cgs_derek.add("cg_derek_showdown_closeup")
    $ renpy.save_persistent()
    scene cg_derek_showdown_closeup with dissolve
    if achievement.has("ach_tricky_timing") != True:
        $ persistent.ach_tricky_timing = True
        $ achievement.grant("ach_tricky_timing")
        init:
            $ achievement.register("ach_tricky_timing")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_tricky_timing == True and achievement.has("ach_tricky_timing") != True:
                $ achievement.grant("ach_tricky_timing")
                $ achievement.register("ach_tricky_timing")
                $ achievement.sync()
    "He kneeled down over me, and I smelled the acrid tar-smoke."
    jack empty "It was a nice try."
    "I squirmed under him, but I couldn't get away."
    if meme_mode:
        "He moved the cigarette closer to me, and before he could react, I grabbed it with my teeth and swallowed it with one gulp."
        jack empty "WHAT THE FUCK!"
        jack empty "I only had one left!!!"
        p "Hrk!"
        play sound "<from 0.0 to 1.0>music/sfx_knife_stab.ogg"
        "His weird little brass knuckles blade thing was in my throat so fast I couldn't even cough."
        $ stat_health -= 100
        scene black with eyedissolve
        stop music fadeout 1.0
        hide screen effect_health
        hide screen effect_ice
        jack intense "Die already!"
    elif True:
        "He pressed the lit cigarette against my shoulder as I tried to stifle a groan of pain with clenched teeth."
        "I almost didn't notice the blade slide against my throat."
        p "Please... No..."
        play sound "<from 0.0 to 1.0>music/sfx_knife_stab.ogg"
        "I screamed as the knife was pushed through my jaw, up..."
        $ stat_health -= 100
        scene black with eyedissolve
        stop music fadeout 1.0
        hide screen effect_health
        hide screen effect_ice
        "And further as my scream became a gurgle."
    $ quick_menu = False
    pause 1.0
    window hide
    hide screen status
    $ persistent.endings_derek.add("Your fight is over")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_48
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","Your fight is over")
    $ renpy.pause(hard=True)

label event_derek_endgame_machete:
    $ phase = "event"
    stop music
    $ persistent.cgs_derek.add("cg_derek_showdown_machetejack")
    $ renpy.save_persistent()
    if meme_mode:
        play sound "music/sfx_bonk.ogg"
        scene cg_derek_showdown_machetejack_bonk
    elif True:
        play sound "<from 0.5>music/sfx_axe_chop.ogg"
        scene cg_derek_showdown_machetejack
    p "AHH!" with vpunch
    "Wh... What the hell?"
    call derek_display_subroutine from _call_derek_display_subroutine_53
    show machete with dissolve
    "The masked man behind my attacker wrenched the machete out of his skull and tossed his body aside."
    "I stared in awe and confusion."
    "Jaqueline and Tom remained frozen."
    p "Wha... You..."
    "I gulped, looking at the large, bloody weapon in his hand."
    machete "You don't have to worry."
    machete "I'm not going to hurt you."
    show machete done
    "To all of our surprise, he dropped his weapon into the sand."
    machete "... That was the last one."
    p "I don't... understand."
    machete "You'll find keys and a map in the jacket."
    hide machete with dissolve
    "Jaqueline wasted no time, immediately searching the dead man's body."
    jaq surprised "Oh my god."
    jaq "Tom! [player_name]! He wasn't lying..."
    jaq happy "There's a map... it shows where their vehicles are!"
    tom happy "We-we're actually going to get out of here!"
    "Footsteps in the sand caught my attention."
    "The man who helped us had turned his back and started to leave."
    p "Wait!"
    show machete done with dissolve
    p "Thank you..."
    p "You saved us..."
    menu:
        " "
        "\"Can we at least know your name?\"" if True:
            machete "..."
            machete "My name doesn't matter."
        "\"Can we at least see your face?\"" if True:
            machete "..."
            machete "My face doesn't matter."
        "\"Can we at least see your dick?\"" if meme_mode:
            show machete
            "He picked the machete back up."
            p "WAI-"
            jump instachop
        "\"That girl from the first day...\"" if True:
            machete "..."
            machete "I had to stop her suffering."
            machete "I knew by then there was nothing I could do to save her..."
            machete "Not in front of all of them."
            "I couldn't see his eyes, but something about his posture seemed tortured by the memory."
            "I didn't press the issue."
        "\"What about the victim you brought here?\"" if True:
            machete "..."
            machete "Richard."
            machete "One of the first things I did to find these people was to pose as a young, vulnerable woman online."
            machete "It didn't help me much in tracking them down, but I did find Richard."
            machete "He was quick to reply to my trap, and after some searching I could tell that my false persona was by no means his first victim."
            machete "... I had to bring someone to come here..."
            machete "He was an easy choice."
            "I was suddenly a lot less worried about where Richard ended up."
    machete "Look..."
    machete "I'm not some sort of hero or vigilante."
    "He slowly reached back and unclasped the necklace he was wearing."
    machete "All I wanted was revenge."
    machete "{i}This{/i} is who saved you."
    $ persistent.cgs_derek.add("cg_derek_machete_sister")
    $ renpy.save_persistent()
    scene cg_derek_machete_sister with dissolve
    "He opened the locket and showed the picture to me."
    "A girl..?"
    machete empty "My older sister."
    machete empty "They took her."
    machete empty "And they killed her."
    machete empty "At first I didn't know what happened. I called the police, I searched everywhere. For months."
    machete empty "Of course the cops didn't help. Nobody seemed to care."
    machete empty "The empty space she left in my life started to feel like a black hole, swallowing everything I ever cared about."
    machete empty "I couldn't eat. I couldn't sleep. I lost myself."
    machete empty "The only thing I cared about was destroying whatever destroyed her."
    machete empty "I understand perfectly well that revenge isn't justice."
    machete empty "But how could I possibly have justice?"
    machete empty "She was one of a kind, and now she's gone forever."
    machete empty "Every single day I wake up and she's gone."
    machete empty "All her dreams and her future, gone."
    machete empty "There's no justice for that."
    machete empty "There never could be."
    machete empty "... All that was left was revenge."
    machete empty "It took years to find them, and to trick them into letting me in. It cost me everything."
    call derek_display_subroutine from _call_derek_display_subroutine_54
    show machete done with dissolve
    "He closed the locket and stepped back."
    machete "I did what I came out here to do."
    machete "I knew it wasn't going to make me feel better."
    machete "... Nothing can bring her back."
    p "I... I'm sorry."
    tom "You should come back with us..."
    machete "No."
    machete "I'll find my own way to wherever I'm supposed to go."
    "Even without the machete, he was still very intimidating."
    "I didn't want to argue."
    p "Okay..."
    jaq "Tom is injured."
    jaq "We're all dehydrated."
    jaq "We need to go."
    "I nodded and we reluctantly set off, leaving him standing there."
    scene black with dissolve
    hide screen effect_health
    hide screen effect_ice
    stop ambient fadeout 1.0
    "Thankfully, the map was relatively easy to follow."
    "Within a few hours, we made it to a gas station and civilization."
    "It would take a long time to recover."
    "But we were alive."
    "And I never forgot the man with the machete."
    if achievement.has("ach_a_new_day") != True:
        $ persistent.ach_a_new_day = True
        $ achievement.grant("ach_a_new_day")
        init:
            $ achievement.register("ach_a_new_day")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_a_new_day == True and achievement.has("ach_a_new_day") != True:
                $ achievement.grant("ach_a_new_day")
                $ achievement.register("ach_a_new_day")
                $ achievement.sync()
    play music "music/music_machete_ending.ogg" fadein 2.0
    pause 1.5
    $ quick_menu = False
    window hide
    hide screen status
    $ persistent.endings_derek.add("The machete was laid to rest")
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_49
    scene cg_endscreen_machete with zoomdissolve
    show screen bg_endslate_survival_text_white("You Lived","The machete was laid to rest")
    $ renpy.pause(hard=True)

label event_derek_tomleave:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        tom "Hey...uh... [player_name]?"
        $ sleep = 0
        if arrivedby == "sleep":
            call derek_display_subroutine from _call_derek_display_subroutine_60
        p "Hrrugh?"
        "I shook myself awake and looked up to see Tom."
        tom "Sorry to wake you, but..."
    elif True:
        tom "Hey...uh... [player_name]?"
    tom "I've been thinking..."
    tom "And I think I have to leave."
    tom "I know I'll probably die out there."
    tom "But I'm getting dizzy. I have this horrible headache."
    tom worried "People can't go very long without water..."
    p "But... where will you go?"
    tom normal "I don't know."
    tom "I..."
    tom worried "I'm too scared to fight them."
    tom "I'm gonna just make a break for it."
    p "Tom..."
    tom "I'm sorry [player_name]."
    if rich_location == "Cave":
        rich "I think Tom's got the right of it."
        rich "We're gonna die slow in here."
        rich "... I'm leaving too."
    p "..."
    if rich_location == "Cave":
        p "Well... good luck guys."
    elif True:
        p "Well... good luck Tom."
    p "I mean it."
    tom "..."
    $ tom_location = "Gone"
    $ rich_location = "Gone"
    call derek_display_subroutine from _call_derek_display_subroutine_55
    "Maybe I should get out of here too."
    $ arrivedby = "special"
    jump derek_turn_nostats

label event_derek_death_health:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        pass
    elif True:
        "I feel... cold..."
        scene black with eyedissolve
        "I felt myself falling." with vpunch
        "I moved a shaky hand and felt my own blood on the ground."
    "I can't open my eyes."
    if map_location == "Cave" and jaq_location == "Cave":
        jaq "[player_name]!!!"
        "... Huh?"
    elif map_location == "Cave" and tom_location == "Cave":
        tom "[player_name]..? [player_name]!!!"
        "... Huh?"
    hide screen effect_health with dissolve
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    "I can't hear anything anymore."
    window hide
    hide screen status
    if derek_status == "Dead" and "item_sacrificial_knife" in inventory and "You were sacrificed" in persistent.endings_derek:
        show cg_derek_shadowdemon_1 with Dissolve(2.0)
        menu:
            "Offer the knife" if True:
                if meme_mode:
                    demon "{cps=10}{font=images/feral.regular.ttf}{size=25}Oh?{/size}{/font}{/cps}"
                    demon "{cps=10}{font=images/feral.regular.ttf}{size=25}You brought me a gift..?{/size}{/font}{/cps}"
                    demon "{cps=10}{font=images/feral.regular.ttf}{size=25}And you brought me blood!{/size}{/font}{/cps}"
                    demon "{cps=10}{font=images/feral.regular.ttf}{size=25}If a pact is what you're after, a pact is what you'll get.{/size}{/font}{/cps}"
                    demon "{cps=10}{font=images/feral.regular.ttf}{size=25}Yes... I'll stay with you forever.{/size}{/font}{/cps}"
                elif True:
                    demon "{cps=10}{font=images/gatosrunes.ttf}{size=25}Oh?{/size}{/font}{/cps}"
                    demon "{cps=10}{font=images/gatosrunes.ttf}{size=25}You brought me a gift..?{/size}{/font}{/cps}"
                    demon "{cps=10}{font=images/gatosrunes.ttf}{size=25}And you brought me blood!{/size}{/font}{/cps}"
                    demon "{cps=10}{font=images/gatosrunes.ttf}{size=25}If a pact is what youre after, a pact is what youll get.{/size}{/font}{/cps}"
                    demon "{cps=10}{font=images/gatosrunes.ttf}{size=25}Yes... Ill stay with you forever.{/size}{/font}{/cps}"
                $ persistent.redcounter = True
                if achievement.has("ach_red") != True:
                    $ persistent.ach_red = True
                    $ achievement.grant("ach_red")
                    init:
                        $ achievement.register("ach_red")
                        $ achievement.sync()
                        $ renpy.save_persistent()
                        if persistent.ach_red == True and achievement.has("ach_red") != True:
                            $ achievement.grant("ach_red")
                            $ achievement.register("ach_red")
                            $ achievement.sync()
                play sound [ "music/sfx_fire_whoosh.ogg" ]
                show cg_derek_shadowdemon_2
                pause(0.5)
            "Die" if True:
                pass
    elif True:
        play sound [ "<silence 1.7>","music/sfx_fire_whoosh.ogg" ]
        show cg_derek_shadowdemon with Dissolve(2.0)
        pause(0.5)
    scene black with dissolve
    hide screen status
    $ quick_menu = False
    $ persistent.endings_derek.add("You bled out")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_50
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You bled out")
    $ renpy.pause(hard=True)

label event_derek_thirst_1:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        $ sleep = 0
        call derek_display_subroutine from _call_derek_display_subroutine_56
        "I woke up abruptly and rubbed the back of my neck."
    elif True:
        "I stopped for a moment and rubbed the back of my neck."
    "I'm thirsty..."
    "I'm getting a headache too..."
    "I wish I could find some water..."
    $ arrivedby = "special"
    jump derek_turn_nostats
label event_derek_thirst_2:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        $ sleep = 0
        call derek_display_subroutine from _call_derek_display_subroutine_57
        "I abruptly woke up with a pounding headache."
    "Ugh..."
    "My mouth is so dry."
    $ stat_sanity -= 10
    "I feel weak and this headache is driving me crazy."
    "I need water..."
    $ arrivedby = "special"
    jump derek_turn_nostats
label event_derek_thirst_3:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        $ sleep = 0
        call derek_display_subroutine from _call_derek_display_subroutine_58
        "I woke up feeling awful."
        "It took a long time to stand up again."
    "I don't... feel good..."
    "I stumbled slightly."
    "Everything feels like it's spinning..."
    "Everything hurts."
    $ stat_sanity -= 30
    $ arrivedby = "special"
    jump derek_turn_nostats
label event_derek_thirst_death:
    $ phase = "event"
    if arrivedby == "sleep" or arrivedby == "wakeup":
        $ sleep = 0
        call derek_display_subroutine from _call_derek_display_subroutine_59
        "I woke up slowly."
        "I crawled to my knees."
    elif True:
        "I fell to my knees."
    "I felt something running past my lips."
    "Blood..."
    "My nose is bleeding."
    if meme_mode:
        demon "{cps=10}{font=images/feral.regular.ttf}{size=25}Hahaha...{/size}{/font}{/cps}"
        "I'm... I'm hearing things."
        demon "{cps=10}{font=images/feral.regular.ttf}{size=25}Coward.{/size}{/font}{/cps}"
    elif True:
        demon "{cps=10}{font=images/gatosrunes.ttf}{size=25}Hahaha...{/size}{/font}{/cps}"
        "I'm... I'm hearing things."
        demon "{cps=10}{font=images/gatosrunes.ttf}{size=25}Coward.{/size}{/font}{/cps}"
    "Part of me feels sick..."
    "And dizzy..."
    "Am I still dreaming?"
    "I can't... breathe."
    scene black
    "The ground rose up to meet me." with vpunch
    $ quick_menu = False
    window hide
    hide screen effect_health
    hide screen effect_ice
    hide screen status
    $ persistent.endings_derek.add("You succumbed to thirst")
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    call achievement_checker from _call_achievement_checker_51
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You succumbed to thirst")
    $ renpy.pause(hard=True)
label event_derek_sanity_1:
    $ phase = "event"
    "My feet dragged through the sand."
    "I looked down and stared."
    "All these grains used to be something..."
    "Smashed up sea shells and bones."
    "Things that die..."
    "Leaving behind a hundred million shattered pieces."
    "..."
    "That's what will happen to me."
    "I'll be shattered into a hundred million pieces and no one will ever know what I used to be."
    "I tried to shake the idea out of my head."
    $ arrivedby = "special"
    jump derek_turn_nostats
label event_derek_sanity_2:
    $ phase = "event"
    if meme_mode:
        demon "{cps=10}{font=images/feral.regular.ttf}{size=25}Come closer.{/size}{/font}{/cps}"
        demon "{cps=10}{font=images/feral.regular.ttf}{size=25}I can hear you screaming.{/size}{/font}{/cps}"
    elif True:
        demon "{cps=10}{font=images/gatosrunes.ttf}{size=25}Come closer.{/size}{/font}{/cps}"
        demon "{cps=10}{font=images/gatosrunes.ttf}{size=25}I can hear you screaming.{/size}{/font}{/cps}"
    "I spun around wildly."
    "W-who was that?"
    "..."
    if map_location == "Cave":
        if jaq_location == "Cave":
            jaq question "Are you okay..?"
            p "Uh..."
            p "Yeah."
            show jaq normal
        elif tom_location == "Cave":
            tom "Are you okay..?"
            p "Uh..."
            p "Yeah."
        elif True:
            "There's no one around..."
    "I shook my head."
    "I need to keep it together."
    $ arrivedby = "special"
    jump derek_turn_nostats
label event_derek_drink_poison_cave:
    $ phase = "event"
    if tom_location == "Cave":
        tom surprised "Wait!"
        tom "You didn't get that water from the fissure did you?"
        p "Yeah, why?"
        tom "Please don't drink that!"
        tom worried "That's the water I drank... before those two guys..."
        "I pushed the canteen away from my face."
        p "That's what paralyzed you?"
        tom normal "Yeah."
        "I looked sadly at the canteen before turning it over and watching the contents splash to the ground."
        $ inventory.remove("item_canteen_poison")
        $ inventory.append("item_canteen_empty")
        $ renpy.notify("Canteen Emptied.")
        show screen inventory
        pause(1.5)
        hide screen inventory
        p "I knew it was too good to be true..."
        $ arrivedby = "special"
        jump derek_turn_nostats
    elif jaq_location == "Cave":
        jaq "Hey."
        jaq "You didn't get that water from the fissure did you?"
        p "Yeah, why?"
        jaq "I wouldn't drink it if I were you."
        jaq "I saw the two creeps in lizard masks pour something in that water."
        "I sniffed at the water..."
        "Something does smell weird."
        "I looked sadly at the canteen before turning it over and watching the contents splash to the ground."
        $ inventory.remove("item_canteen_poison")
        $ inventory.append("item_canteen_empty")
        $ renpy.notify("Canteen Emptied.")
        show screen inventory
        pause(1.5)
        hide screen inventory
        p "I knew it was too good to be true..."
        $ arrivedby = "special"
        jump derek_turn_nostats
    elif True:
        jump event_derek_paralyzed_machete
label event_derek_sleepfail:
    $ phase = "event"
    "I tried to fall asleep..."
    "But I just wasn't tired enough."
    $ arrivedby = "special"
    jump derek_turn_nostats
label event_derek_panic:
    $ phase = "event"
    "I laid a hand on my chest to feel my pounding heart."
    "Why is it so hard to breathe?"
    jump event_derek_sanity_menu_1
label achievement_checker:
    $ ach_game_endings = (len(persistent.endings_derek)) + (len(persistent.endings_mason)) + (len(persistent.endings_celia))
    $ ach_game_art = (len(persistent.cgs_derek)) + (len(persistent.cgs_mason)) + (len(persistent.cgs_celia))
    $ ach_game_bgs = (len(persistent.bgs_seen))
    if persistent.deathcounter >= 1 and achievement.has("ach_let_the_games_begin") != True:
        $ persistent.ach_let_the_games_begin = True
        $ achievement.grant("ach_let_the_games_begin")
        init:
            $ achievement.register("ach_let_the_games_begin")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_let_the_games_begin == True and achievement.has("ach_let_the_games_begin") != True:
                $ achievement.grant("ach_let_the_games_begin")
                $ achievement.register("ach_let_the_games_begin")
                $ achievement.sync()
    if persistent.deathcounter >= 100 and achievement.has("ach_deadicated") != True:
        $ persistent.ach_deadicated = True
        $ achievement.grant("ach_deadicated")
        init:
            $ achievement.register("ach_deadicated")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_deadicated == True and achievement.has("ach_deadicated") != True:
                $ achievement.grant("ach_deadicated")
                $ achievement.register("ach_deadicated")
                $ achievement.sync()
    if persistent.deathcounter >= 500 and achievement.has("ach_riverwalker") != True:
        $ persistent.ach_riverwalker = True
        $ achievement.grant("ach_riverwalker")
        init:
            $ achievement.register("ach_riverwalker")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_riverwalker == True and achievement.has("ach_riverwalker") != True:
                $ achievement.grant("ach_riverwalker")
                $ achievement.register("ach_riverwalker")
                $ achievement.sync()
    if len(persistent.endings_derek) >= 21 and achievement.has("ach_practically_fremen") != True:
        $ persistent.ach_practically_fremen = True
        $ achievement.grant("ach_practically_fremen")
        init:
            $ achievement.register("ach_practically_fremen")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_practically_fremen == True and achievement.has("ach_practically_fremen") != True:
                $ achievement.grant("ach_practically_fremen")
                $ achievement.register("ach_practically_fremen")
                $ achievement.sync()
    if len(persistent.endings_celia) >= 14 and achievement.has("ach_number_one_employee") != True:
        $ persistent.ach_number_one_employee = True
        $ achievement.grant("ach_number_one_employee")
        init:
            $ achievement.register("ach_number_one_employee")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_number_one_employee == True and achievement.has("ach_number_one_employee") != True:
                $ achievement.grant("ach_number_one_employee")
                $ achievement.register("ach_number_one_employee")
                $ achievement.sync()
    if len(persistent.endings_mason) >= 15 and achievement.has("ach_top_tier_ranger") != True:
        $ persistent.ach_top_tier_ranger = True
        $ achievement.grant("ach_top_tier_ranger")
        init:
            $ achievement.register("ach_top_tier_ranger")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_top_tier_ranger == True and achievement.has("ach_top_tier_ranger") != True:
                $ achievement.grant("ach_top_tier_ranger")
                $ achievement.register("ach_top_tier_ranger")
                $ achievement.sync()
    if ach_game_endings >= 50 and achievement.has("ach_death_expert") != True:
        $ persistent.ach_death_expert = True
        $ achievement.grant("ach_death_expert")
        init:
            $ achievement.register("ach_death_expert")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_death_expert == True and achievement.has("ach_death_expert") != True:
                $ achievement.grant("ach_death_expert")
                $ achievement.register("ach_death_expert")
                $ achievement.sync()
    if (ach_game_endings + ach_game_art + ach_game_bgs) >= 93 and achievement.has("ach_people_person") != True:
        $ persistent.ach_people_person = True
        $ achievement.grant("ach_people_person")
        init:
            $ achievement.register("ach_people_person")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_people_person == True and achievement.has("ach_people_person") != True:
                $ achievement.grant("ach_people_person")
                $ achievement.register("ach_people_person")
                $ achievement.sync()
    if (ach_game_endings + ach_game_art + ach_game_bgs) >= 140 and achievement.has("ach_art_connoisseur") != True:
        $ persistent.ach_art_connoisseur = True
        $ achievement.grant("ach_art_connoisseur")
        init:
            $ achievement.register("ach_art_connoisseur")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_art_connoisseur == True and achievement.has("ach_art_connoisseur") != True:
                $ achievement.grant("ach_art_connoisseur")
                $ achievement.register("ach_art_connoisseur")
                $ achievement.sync()
    if ach_game_bgs >= 21 and ach_game_art >= 115 and achievement.has("ach_art_collector") != True:
        $ persistent.ach_art_collector = True
        $ achievement.grant("ach_art_collector")
        init:
            $ achievement.register("ach_art_collector")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_art_collector == True and achievement.has("ach_art_collector") != True:
                $ achievement.grant("ach_art_collector")
                $ achievement.register("ach_art_collector")
                $ achievement.sync()
    if "Now you are the hunter" in persistent.endings_mason and "You killed for your freedom" in persistent.endings_celia and persistent.derek_killed == True and achievement.has("ach_cutthroat") != True:
        $ persistent.ach_cutthroat = True
        $ achievement.grant("ach_cutthroat")
        init:
            $ achievement.register("ach_cutthroat")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_cutthroat == True and achievement.has("ach_cutthroat") != True:
                $ achievement.grant("ach_cutthroat")
                $ achievement.register("ach_cutthroat")
                $ achievement.sync()
    return
label cutthroat_checker:
    if persistent.ach_no_you == True and persistent.ach_catching_bears == True and persistent.ach_have_a_nice_trip == True and achievement.has("ach_cutthroat") != True:
        $ persistent.ach_cutthroat = True
        $ achievement.grant("ach_cutthroat")
        init:
            $ achievement.register("ach_cutthroat")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_cutthroat == True and achievement.has("ach_cutthroat") != True:
                $ achievement.grant("ach_cutthroat")
                $ achievement.register("ach_cutthroat")
                $ achievement.sync()
    return
label game_start_fox:
    $ gamepath = "fox"
    $ location_temp = "warm"
    $ food = 20
    $ energy = 24
    call screen showconfirm(message="You are now entering 'The Show Must Go On' DLC.\n\nThis content has its own warnings, so please check them out if you have any concerns.\n\nThe sexual content toggle for this DLC affects some scenes, but doesn't remove sexual content entirely. I tried my best to censor it.", yes_action=Jump("showDLCstart"), no_action=ShowMenu("warnings"))
    label showDLCstart:
    play music "music/ambient_fox_01.ogg" fadein 1.0
    "The first thing I noticed was a pounding headache."
    play sound "music/sfx_keyboard_1.ogg" volume 0.5
    "Then, a strange sound."
    "Clicking?"
    play sound "music/sfx_keyboard_2.ogg"
    "I strained to hear as the clicking became the rapid tapping of a keyboard."
    $ persistent.cgs_fox.add("cg_foxbg_dark")
    $ renpy.save_persistent()
    scene darkroom with eyedissolve_reverse
    "I opened my eyes."
    show darkroom:
        xalign 0.5
        yalign 1.0
        easein 0.5 xalign 0.25 yalign 1.0
        pause 0.25
        easein 0.5 xalign 0.75 yalign 1.0
        pause 0.25
        easein 0.5 xalign 0.5 yalign 1.0
    "It's dark..."
    "Why am I so uncomfortable?"
    "I began to register my position, kneeling on the floor with my arms above my head."
    play sound "music/sfx_chain_short.ogg"
    "I tried to lower my arms and heard the unsettling clink of heavy chains."
    fox "Oh?"
    show darkroom:
        xalign 0.5
        yalign 1.0
        easein 0.25 xalign 0.5 yalign 0.6
    show camera1:
        xalign 0.80
        yalign 0.0
        alpha 0.0
        easein 0.25 xalign 0.80 alpha 1.0 yalign 0.4
    show fox:
        xalign 0.45
        yalign 1.0
        alpha 0.0
        yoffset 0
        pause 0.25
        easein 0.25 xalign 0.5 alpha 1.0
    pause 0.5
    show fox:
        alpha 1.0
    show camera1:
        alpha 1.0
    "Someone was in front of me."
    show darkroom:
        easein 0.25 xalign 0.5 yalign 0.4
    show camera1:
        easein 0.25 xalign 0.80 yalign 1.2
    show fox:
        easein 0.25 xalign 0.5 yoffset 225
    fox eyeswide "Look who's awake!"
    fox cocked "Right on schedule~"
    play sound "<from 0 to 1.5>music/sfx_chain_long.ogg"
    "I jerked in surprise away from him, but the chains held me in place."
    "The voice was strange... Flat and mechanical."
    "I couldn't make out his face."
    fox -cocked "So how are you?"
    fox "Do you remember what happened?"
    "As my brain started waking up, a thousand questions started to bubble to the surface."
    menu:
        " "
        "\"Where am I?\"" if True:
            fox "You're exactly where you asked to be."
            "He chucked softly."
            fox cocked "But don't worry about that~"
        "\"Who are you?\"" if True:
            fox "I'm the announcer from the auction."
            fox "You asked to come with me."
            fox cocked "Don't you remember?"
            fox "But don't worry about that~"
        "\"What's on your head?\"" if True:
            fox cocked "Really?"
            fox cocked "Of all the things to be concerned about, you want to know about my ears?"
            fox -cocked "Haha!"
            fox cocked "But don't worry about that~"
        "Try to answer his questions" if True:
            $ fox_love += 1
            p "I... it hurts..."
            p "I was at the auction... and... you're the announcer?"
            fox cocked "Yes, yes, that's right. Now don't worry about all that."
        "Scream" if True:
            $ fox_love -= 1
            show fox angry
            "I mustered my energy and screamed as loud as I could."
            play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
            queue sound "music/sfx_ears_ring.ogg"
            "The sound was cut immediately by a hard slap to the side of my face." with hpunchhard
            hide fox with dissolve
            show fox close:
                xalign 0.5
                yalign 0.0
            with dissolve
            fox close "Shut up."
            fox "You're only annoying the two of us."
            fox "This room is underground, soundproofed, and carefully hidden."
            $ stat_sanity -= 5
            fox "No one will hear you."
            "I groaned, trying to get my bearings again."
            fox happy "That is... until I want them to~"
            hide fox with dissolve
            show fox cocked:
                xalign 0.5
                yalign 1.0
                yoffset 225
            with dissolve
            fox cocked "But don't worry about that right now."
    fox "You made a choice."
    fox "A choice to become my lovely co-star! {image=icon_heart}"
    fox -cocked "And I have to admit, I'm a bit giddy!"
    fox "No one's ever {i}asked{/i} to come with me before."
    fox "And it's been {i}so long{/i} since I've put on a show."
    show darkroom:
        easein 0.5 xalign 0.3 yalign 0.5
    show camera1:
        easein 0.5 xalign 1.3 yalign 0.8
    show fox:
        easein 0.5 xalign 3.5 yoffset 100
    show camera2:
        xalign -0.5
        yalign 1.2
        easein 0.5 xalign 0.1 yalign 0.8
    "As he spoke, I tried to take note of my surroundings."
    show darkroom:
        easein 0.5 xalign 0.5 yalign 0.3
    show camera1:
        easein 0.5 xalign 0.8 yalign 1.8
    show fox:
        easein 0.5 xalign 0.5 yoffset 400
    show camera2:
        easein 0.5 xalign -0.5 yalign 1.8
    "It's so dark..."
    show darkroom:
        easein 0.5 xalign 0.7 yalign 0.6
    show camera1:
        easein 0.5 xalign 0.3 yalign 0.0
    show fox:
        easein 0.5 xalign -3.0 yoffset 0
    show camera3:
        xalign 1.5
        yalign 1.8
        easein 0.5 xalign 0.9 yalign 0.0
    if meme_mode:
        "It smells like bleach and shame in here..."
    elif True:
        "But..."
    show darkroom:
        easein 1 xalign 0.5 yalign 0.4
    show camera1:
        easein 1 xalign 0.80 yalign 1.2
    show fox:
        easein 1 xalign 0.5 yoffset 225
    show camera3:
        easein 1 xalign 1.5 yalign 1.2
    "I looked at the man in front of me."
    "Aside from the strange ears and what appeared to be a tail..."
    if meme_mode:
        "He's kindaaa... twinky."
    elif True:
        "He's so short. And he has a slender build."
    "A little flame of hope came to life in my chest."
    "I definitely made the right choice. I could have a chance, in a fight..."
    if meme_mode:
        "I could take a twink. I know it."
    show darkroom:
        easein 0.5 xalign 0.5 yalign 0.6
    show camera1:
        easein 0.5 xalign 0.80 yalign 0.0
    show fox:
        easein 0.5 xalign 0.5 yoffset 0
    "I looked down at myself and my train of thought was completely derailed."
    "Underwear? And it's... lacy. This definitely isn't mine..."
    show darkroom:
        easein 1 xalign 0.5 yalign 0.4
    show camera1:
        easein 1 xalign 0.80 yalign 1.2
    show fox:
        easein 1 xalign 0.5 yoffset 225
    fox eyeswide "Ah yes, your outfit."
    fox cocked "I thought it would be perfect for your first show. What do you think?"
    menu:
        " "
        "\"Give my clothing back you motherfucker!\"" if not meme_mode:
            label showDLC_grumpyoutfit:
            show fox eyeswide
            $ fox_love -= 1
            fox -eyeswide "Hahaha!"
            fox "I suppose there's no accounting for taste~"
            fox cocked "Besides, it's not really about what {i}you{/i} prefer anyway."
            "He chuckled, supposedly amused by his own train of thought."
        "\"It's fine, but...\"" if meme_mode:
            show fox eyeswide
            p "I look better in jewel tones."
            p "I feel like that should have been obvious."
            jump showDLC_grumpyoutfit
        "\"Can't I have some clothing..?\"" if True:
            fox -cocked "Oh, I'm afraid not."
            fox "It's really more of a 'bare skin' type of show we're doing."
            fox cocked "You get it, don't you?"
            "He laughed quietly to himself."
        "\"I hate this girly stuff!\"" if pronoun == "she":
            jump showDLC_grumpyoutfit
        "\"I'm not a girl!!!\"" if pronoun == "he" or pronoun == "they":
            jump showDLC_grumpyoutfit
        "\"I guess it's cute...\"" if True:
            $ fox_love += 1
            fox eyeswide "Oh~? You like it?"
            fox cocked "It does look {i}so{/i} cute on you..."
            fox "I spent quite a bit of time picking out the right set. {image=icon_heart}"
        "\"When did I change? Did you..?\"" if True:
            $ show_event_dressup = 1
            hide fox with dissolve
            show fox close:
                xalign 0.5
                yoffset 0
            with dissolve
            "He leaned down close to me and spoke in a low voice."
            fox happy "Would you like to see?"
            show fox close happy:
                xalign 0.5
                alpha 1.0
                easein 0.25 xalign 0.45 alpha 0.0
            "I didn't know how to reply, but he didn't wait for an answer anyway."
            hide fox
            "Instead he picked something up off to the side."
            play sound "music/sfx_beep.ogg" volume 0.1
            "I heard a soft beep."
            $ persistent.cgs_fox.add("cg_fox_camera")
            $ renpy.save_persistent()
            show cam:
                xalign 1.0
                yalign 2.0
                alpha 0.0
                easeout 0.25 yalign 1.0 alpha 1.0
            "Then the small screen of a camcorder was thrust in front of my face."
            show cam wide with dissolve
            play ambient "music/sfx_camcorder.ogg" volume 2
            "It took a second for my eyes to adjust, but..."
            if meme_mode:
                p "Bro, what?"
                p "I can't see shit."
            elif True:
                "Skin..?"
                "My throat tightened as I realized I was looking at myself."
            show cam close with dissolve
            "The camera swept over my body before being jostled, as if it was given to someone else."
            show cam claws with dissolve
            "Then he entered the shot."
            if meme_mode:
                p "You need to fix your camera, man."
                p "It's so grainy."
            elif True:
                "I shuddered involuntarily as I watched his hands trail all over my skin."
                "I was still in my underwear, as I had been at the auction."
                "He was silent... he pulled up a bit of my underwear-"
                "I wanted to scream at myself to wake up."
            show cam nude with dissolve
            "He tore through the underwear with his bare hands and... claws?"
            if meme_mode:
                p "Why did you even film it in the dark?"
                fox angry "Would you SHUT THE FUCK UP AND WATCH?" with vpunch
            elif True:
                "I could feel myself flushing, but I couldn't look away."
                "My naked body was completely exposed to him."
                "And I had no idea."
                "I wanted to say something, but the words just wouldn't come out."
            show cam dangle with dissolve
            "A set of lacy underwear was dangled in the camera's view."
            "He slowly slipped them onto my limp body."
            show cam done with dissolve
            "He seemed to be very careful with his claws, avoiding both the lingerie and my skin."
            "Then, once it was on my body, he stopped for a moment to admire his work."
            "With a growing sense of unease, I saw that the underwear fit me perfectly."
            show cam done2 with dissolve
            "The version of him in the video circled back around to take the camera back."
            show cam -done2 -close with dissolve
            stop ambient
            "And he did a final, agonizingly slow sweep over my body before the video cut out."
            show cam:
                pause 0.5
                xalign 1.0
                yoffset 0
                alpha 1.0
                easeout 0.25 yoffset 500 alpha 0.0
            p "I..."
            hide cam
            show fox close:
                xalign 0.45
                yalign 0.0
                alpha 0.0
                easein 0.25 xalign 0.5 alpha 1.0
            fox "What do you think?"
            p "It's... you..."
            fox happy "My fans found it {i}very{/i} exciting."
            "His... what?"
            "He seemed delighted by my frozen reaction."
            fox "Yes... that was my little 'teaser'."
            p "Other people saw..?"
            fox "Oh yes."
            fox -happy "And they're so eager to see more!"
            hide fox with dissolve
            show fox:
                yalign 0.0
                xalign 0.5
                yoffset -50
            with dissolve
    fox cocked "We're going to have so much fun!"
    fox -cocked "And I just KNOW Chat will love you."
    p "Chat?"
    "The question popped out before I could think about it."
    fox "Yes, darling. In just a few moments, we're going live!"
    fox "It's a BIG audience we've gathered!"
    fox eyeswide "Oh! And I almost forgot!"
    $ fox_name = "Fox"
    fox -eyeswide "You can call me 'Fox'. Everyone else does."
    hide fox with dissolve
    show darkroom:
        easein 0.25 yalign 0.5
    show camera1:
        easein 0.25 yalign 0.8
    pause 0.25
    show fox close touch with dissolve:
        yoffset 0
        xoffset 0
    "He placed a finger to my lips, and I felt the odd sensation of a claw above it."
    fox "Don't worry, I don't need your name."
    if player_name.upper() == "STRADE":
        fox horny "..."
        fox -horny "No. I won't be needing your name at all."
    elif player_name.upper() == "LAW" or player_name.upper() == "LAWRENCE":
        fox "..."
        fox happy "I already know your name..."
    elif player_name.upper() == "REN":
        fox "..."
        fox happy "I already know YOUR name!"
    elif True:
        fox happy "I already know it!"
    hide fox with dissolve
    show fox oncomputer with dissolve
    "I opened my mouth to protest, but he had already turned away."
    "I looked at the equipment surrounding me."
    "They're... cameras?"
    play sound "music/sfx_keyboard_3.ogg"
    "A deep fear started to creep up my throat."
    p "Wait, you can't film me! You can't-"
    stop music fadeout 5.0
    fox "Shh, shh. We're starting!"
    fox "Hello? Can you hear me?"
    fox "How's the feed?"
    "I could tell he wasn't speaking to me."
    "I couldn't quite see around him..."
    fox "Haha! Yes! Yes you too~ My goodness, you got in here fast!"
    show fox comp behind camera1 with dissolve
    "He cleared his throat and stood up straight."
    play music "music/ambient_fox_02.ogg"
    fox "Good evening, everyone!"
    fox "I'm so glad you could join me on such short notice-"
    fox "Oh? Oh yes! I missed you too!"
    fox "Yes! My beautiful patrons of exquisite taste~"
    fox presenting "Welcome back!"
    "He lifted his voice and spoke in a deeply expressive way to his audience."
    "It overcame the mechanical flatness that seemed to be caused by his mask."
    fox "I've got such a treat for you today!"
    if player_name.upper() == "STRADE":
        fox lookback "A fresh face! Please say hello to... our star!"
    elif True:
        fox lookback "A fresh face! Please say hello to [player_name]!"
    if pronoun == "they":
        fox -lookback "[pp_sub_c] were going to be used for other business, but [pp_sub] wanted to come here instead!"
    elif True:
        fox -lookback "[pp_sub_c] was going to be used for other business, but [pp_sub] wanted to come here instead!"
    "I squinted at the computer screen."
    "It was some kind of chatroom, and a video feed... of me."
    "These people are {i}watching{/i} me?"
    menu:
        " "
        "Beg them to help you" if True:
            $ chat_love += 1
            $ show_pollstat_1 = 1
            show fox comp lookback
            p "Help me!"
            p "Please! I was kidnapped! I didn't ask to be here!"
            p "P-please... call the police..."
            "My voice wavered with my conviction as I saw Fox standing by, uncaring."
            "As if this was exactly what he expected."
            "I tried to see the computer screen..."
            show fox -lookback
            "He addressed the camera."
            fox "Yep. Another one in the 'beg' bucket!"
            fox presenting "Honestly, I don't know why you guys bet on anything else~"
            fox -presenting "Hahaha! Sorry, Diamond. But let's see how your other bets go? Hm?"
            fox "There's a good sport!"
            "No one was calling the police."
            "No one seemed to care at all."
        "Insult them" if True:
            $ chat_love -= 1
            $ show_pollstat_1 = -1
            show fox comp lookback
            p "What are you looking at!?"
            p "You sick fucks!"
            p "Why aren't you calling the police!?"
            p "What's wrong with you!?"
            "I strained against the chains."
            show fox laugh
            "His sharp laugh cut through the air again."
            fox -lookback "So feisty! {image=icon_heart}"
            fox "We do love the spirited ones don't we?"
            fox presenting "Oh! And a big win for Diamond!"
            fox -presenting "You really do have such excellent intuition!"
            "What the fuck is he talking about?"
            "What IS this!?"
            "I gritted my teeth."
            "Yelling isn't getting me anywhere..."
        "Plug your own channel" if meme_mode:
            show fox comp lookback
            p "Hey folks! I'm [player_name]!"
            p "You can find me streaming on my own channel, Monday to Saturday at-"
            "I felt a warning kick." with vpunch
            show fox comp
            p "Oh, okay. I see how it is."
        "Stay silent" if True:
            show fox oncomputer
            $ fox_love += 1
            "I sank lower into my position, held up by shackles."
            "There's no point in screaming or crying, I can tell."
            "I need to be patient and careful, and wait for my moment..."
    fox oncomputer "Oh Rancor, that is {i}disgusting!{/i} Hahaha!" with dissolve
    fox "Maybe later, maybe later."
    fox comp "Come on now, you guys know the drill." with dissolve
    fox "We need to pace ourselves... we need to make it {i}last{/i}, right?"
    fox lookback "Let's start small."
    hide fox with dissolve
    show fox close:
        xalign 0.5
        yalign 0.0
    with dissolve
    "He suddenly got close to me."
    "He gently grabbed one of my pinkie fingers."
    "I tried to pull it away, but my hands were shackled together and chained up."
    fox happy "Get those bets ready! This counts as first blood alright?"
    p "St-"
    $ stat_health -= 1
    $ stat_sanity -= 10
    show black
    play sound "music/sfx_bone_snap_2.ogg"
    p "AAAHHHHH!" with vpunch
    "He yanked my finger backwards with vicious force."
    show fox -happy
    "My scream dissolved into a pained groan."
    hide black with eyedissolve_reverse
    "I looked back up to him, half expecting him to be facing the computer."
    "But he wasn't."
    "He was staring intently at me."
    "My hands were shaking as I tried to hold back tears."
    fox "Not bad... not bad at all!"
    fox happy "Should I leave it there? Or put it back?"
    "I opened my mouth and choked down a whimper before speaking."
    menu:
        " "
        "\"Put it back...\"" if True:
            $ fox_love += 1
            "He seemed pleased by my request."
            fox "Of course!"
            $ stat_health -= 1
            $ stat_sanity -= 5
            show fox -happy
            play sound "music/sfx_bone_crunch.ogg"
            "He immediately grabbed my finger and pulled it back into place." with vpunch
            "The wet grinding sound in my hand made me feel sick."
            "But I managed to endure it without screaming."
            $ stat_sanity += 10
            "And it did seem to feel... slightly better."
        "\"Leave it alone!\"" if True:
            $ fox_love -= 1
            show fox -happy
            p "Don't touch me!"
            show fox happy
            "He bent in front of me as his eyes betrayed a grin."
            fox "As you wish!"
    hide fox with dissolve
    show fox comp with dissolve
    "I flinched as he moved, but it was only to turn to the screen again."
    fox "So? What do we think?"
    fox "Yes... I think so too..."
    "His tail swished behind him excitedly."
    fox "Already?"
    "He laughed sharply."
    fox presenting "Well, with a donation like that, your wish is my command!"
    fox comp cocked "So. Feet {i}again{/i}, Pandemonium?"
    fox -cocked "I'm just teasing of course! {image=icon_heart}"
    fox "Let's see what we can do~"
    show fox comp lookback
    "He took a theatrical bow before stepping back towards me."
    p "Wait! Don't-"
    hide fox with Dissolve(0.25)
    show fox close touch with Dissolve(0.25)
    "He ignored me completely as he bent down to my level."
    show fox happy
    if sexcontent != "no":
        "My protests cut off in surprise as he reached behind me and cupped my ass."
        "I heard him breathing through the mask as he took a moment to squeeze the flesh."
    elif True:
        "My protests cut off in surprise as he reached behind me."
    "He slid his hands slowly down, into the crook of my legs."
    hide fox with dissolve
    show darkroom:
        easein_bounce 0.25 xalign 0.5 yalign 0.6
    show camera1:
        easein_bounce 0.25 xalign 0.80 yalign 0.0
    play sound "music/sfx_chain_short.ogg"
    "Then he pulled, yanking my shins out painfully from under me."
    "I yelped as my weight dropped entirely to my shackled wrists above me."
    p "What are you doing!?"
    show fox comp:
        zoom 1.2
        yalign 1.0
        yoffset 0
        xoffset 100
    with Dissolve(0.25)
    "He continued to ignore me and adjusted a camera."
    "Now that my feet were in front of me, I realized that they, too, were shackled together."
    hide fox with dissolve
    show fox close touch with dissolve
    "I shuddered as he held one of my feet and rubbed with a clawed thumb."
    fox "Take a good look, guys~"
    show fox knife
    "The glint of a knife seemed to stop my heart for a moment."
    fox "Things are about to get messy..."
    "I tried to jerk my foot out of his grasp, but his grip was as tight as the iron shackles." with hpunchtiny
    $ stat_health -= 1
    $ stat_sanity -= 5
    hide fox with Dissolve(0.25)
    $ persistent.cgs_fox.add("cg_fox_ultraclose2")
    show fox ultraclose with Dissolve(0.25)
    "Pain streaked up my leg as he pressed the tip of the knife into my sole."
    "I clenched my jaw and tried not to scream."
    "I didn't want to give these people what they surely wanted."
    "I didn't want to look, but..."
    $ persistent.cgs_fox.add("cg_fox_ultraclose3")
    $ renpy.save_persistent()
    show fox happy
    "He caught my gaze and a knowing look crossed his eyes."
    $ stat_health -= 5
    $ stat_sanity -= 10
    show fox ultraclose eyeswide
    play sound "music/sfx_knife_stab.ogg"
    "He plunged the knife deep into the bones and tendons of my foot." with vpunch
    "I only realized I was shrieking a moment later."
    fox ultraclose happy "Ahhhh~"
    fox ultraclose -happy "We've got plenty of blood now!"
    "I was shaking uncontrollably, and hanging from my wrists made it terribly obvious."
    if sexcontent != "no":
        $ persistent.cgs_fox.add("cg_fox_ultraclose_cocked")
        $ renpy.save_persistent()
        if pronoun == "they":
            fox ultraclose cocked "They've gotten nice and wet... What do you think, Chat?"
        elif True:
            fox ultraclose cocked "[pp_is_c] gotten nice and wet... What do you think, Chat?"
    "He leaned closer to me."
    fox ultraclose happy "Should I have a feel~?"
    "He didn't look at his screens or wait for an answer."
    p "No!!!"
    $ stat_health -= 1
    $ stat_sanity -= 5
    play sound "music/sfx_gore_2.ogg" volume 0.25
    "He shoved his thumb into the wound in my foot, tearing another scream from me with his thick claw." with vpunch
    fox "Hahaha!"
    $ persistent.cgs_fox.add("cg_fox_ultraclose_cocked")
    $ renpy.save_persistent()
    fox ultraclose cocked "\"No\"?"
    $ stat_health -= 1
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "My vision wavered as he massaged his thumb roughly in the wound." with vpunchtiny
    fox ultraclose eyeswide "But you begged for this!"
    fox ultraclose -eyeswide "Or did you forget?"
    p "Please... I didn't..."
    hide fox with Dissolve(0.25)
    $ persistent.cgs_fox.add("cg_fox_close_knife")
    $ renpy.save_persistent()
    show fox close knife with Dissolve(0.25)
    "He flipped the knife in a show for the camera."
    fox close touch happy "You did~"
    fox "And I think Chat would like to see some more blood."
    fox close touch -happy "Isn't that right?"
    hide fox with Dissolve(0.25)
    show fox oncomputer:
        yoffset -150
    with dissolve
    "He finally relinquished my foot and turned to his monitors."
    if meme_mode:
        fox "..."
        "He seemed to be reading some comments."
        fox "There's {i}two{/i} other cameras."
        fox "Stop talking about my ass!"
        fox "..."
        fox "No, I'm not going to \"whip it out\"."
        "He sounded like he was trying not to laugh."
    elif True:
        "After reading for a moment, he chuckled."
    fox comp "You guys are so one-track minded~ That's why I love you!" with dissolve
    "As the pain from my foot turned into a duller ache, I noticed the pain in my wrists again."
    show fox comp lookback
    "I struggled to get my feet back under myself, and he noticed."
    fox "Here, let me help you with that."
    hide fox with dissolve
    show darkroom:
        easein_bounce 0.25 xalign 0.5 yalign 0.5
    show camera1:
        easein_bounce 0.25 xalign 0.80 yalign 1.0
    play sound "music/sfx_chain_short.ogg"
    "I cursed myself for flinching from him again, but he simply pushed my legs into their first position."
    show fox close touch with dissolve
    fox "Now..."
    fox close touch happy "Chat is still {i}thirsty{/i}. What do you think?"
    menu:
        " "
        "\"Fuck you!\"" if True:
            $ chat_love += 1
            $ show_pollstat_2 = 1
            $ fox_love -= 1
            show fox close touch
            "He laughed sharply."
            fox "I had a feeling you'd say something like that."
            hide fox with dissolve
            show fox close whisper with dissolve
            "He leaned in close to me and lowered his voice to a whisper."
            fox "{i}Chat adores the feisty ones~{/i}"
        "\"Do whatever you want...\"" if True:
            $ chat_love -= 1
            $ show_pollstat_2 = -1
            $ fox_love -= 1
            show fox ultraclose cocked with dissolve
            fox "Do you really mean it?"
            show fox ultraclose -cocked
            "He let out a single sharp laugh."
            fox ultraclose happy "I'm so glad I have your blessing~"
        "Remain silent" if True:
            $ chat_love -= 1
            $ show_pollstat_2 = -1
            $ fox_love -= 1
            $ show_silence += 1
            "He waited a moment for a reply that wasn't coming."
            fox close touch -happy "Nothing?"
            hide fox with dissolve
            show fox comp shrug with dissolve
            fox "..."
            fox comp lookback "I guess we'll just have to work a little harder, hm?"
        "Beg him to stop" if True:
            $ chat_love -= 1
            $ show_pollstat_2 = -1
            $ fox_love += 1
            p "Please stop... Please, I'll do whatever you want! Just stop-"
            show fox ultraclose eyeswide with Dissolve(0.2)
            "I gasped as he lunged close to me without warning and cradled my jaw in his hand." with vpunchtiny
            fox "You will... you will do whatever I want."
            show fox ultraclose -eyeswide
            "He lowered his voice to a whisper."
            fox "{i}I want you to keep begging and crying for the cameras...{/i}"
            fox "{i}And I want you to bleed...{/i}"
    show fox close touch with dissolve
    "He moved to give a clear view for the cameras."
    show fox close knife
    "He raised the knife, my blood still clinging to the edge."
    show fox ultraclose happy with dissolve
    "I sucked in a breath in preparation as he lowered it to the skin of my chest."
    $ stat_health -= 1
    play sound "<from 0 to 1.0>music/sfx_fabric_tear.ogg"
    "He raked it shallowly across my body, slicing apart the lacy top he dressed me in."
    "It stung, but I kept my composure as well as I could."
    "For a moment I wondered why he would cut apart the underwear he must have bought."
    "I looked down at his knife and the absurdity of that thought almost made me laugh."
    $ stat_sanity -= 5
    "What is happening to me!?"
    $ stat_health -= 1
    show fox ultraclose -happy
    "The sting of the blade interrupted the chaos of my thoughts."
    "I couldn't suppress a groan this time; He was cutting deeper than before."
    "A hot trickle of blood made its way over my heaving chest."
    "I barely registered a low hum coming from him as he stroked warm fingers over my bloody chest."
    "The sensation made me shiver involuntarily."
    fox ultraclose happy "Lovely..."
    "He raised the knife to my collarbone."
    $ stat_health -= 1
    "I winced before the knife touched me, but it didn't prepare me for the intense pain."
    show fox ultraclose eyeswide
    "I couldn't help but cry out. It hurt so much worse than the other cuts."
    "His other hand had dipped to my waist."
    "My composure was breaking, I could feel it."
    "He kept cutting, and I kept crying."
    show fox ultraclose cocked
    "When I raised my voice, his hand squeezed my waist, digging claws into my skin."
    "I glanced down and choked."
    "My entire body was covered in blood now."
    "Is he going to kill me like this..?"
    show fox close whisper with dissolve
    "As if he could read minds, he stilled his hands and leaned in close."
    "I could hear him breathing hard through the mask."
    "I didn't dare speak."
    hide fox with dissolve
    show fox comp with dissolve
    "His ear twitched towards the computers, and then he stood up."
    show fox oncomputer with dissolve
    "He wiped off the blade as he read the words on screen."
    fox "Yeah... I got a little carried away, haha!"
    fox comp shrug "But can you blame me?" with dissolve
    "His hips swayed to the side as if all he'd done was some kind of charming foible."
    fox comp -shrug "OH! {i}Wow!{/i}"
    fox "Thank you for the very generous donation, Woundfucker!"
    fox comp cocked "Is there something special you'd like to see?"
    fox comp -cocked "{i}Anything{/i} for my most loyal customer~"
    fox comp cocked "Hm?"
    fox comp -cocked "Oh of course! Is that all?"
    show fox comp lookback
    "He suddenly turned back to me."
    p "God... No more!"
    hide fox with dissolve
    "He circled behind me and crouched in a fluid motion."
    play sound "<from 0 to 0.45>music/sfx_chain_retracted.ogg"
    "I flinched at the sound of a metallic click."
    "But to my surprise, the wrist shackles were disconnected from the chain above me."
    show darkroom:
        xalign 0.5
        yalign 0.5
        easein_bounce 0.25 xalign 0.5 yalign 1.0
    show camera1:
        xalign 0.80
        yalign 1.0
        easein_bounce 0.25 xalign 0.80 yalign -0.8
    play sound "<from 0 to 1.5>music/sfx_chain_long.ogg"
    "I fell forward clumsily until I was caught by clawed hands."
    fox "No, no, come on back up~"
    show darkroom:
        yalign 1
        easeout 0.25 yalign 0.5
    show camera1:
        yalign -0.8
        easeout 0.25 yalign 1.0
    play sound "music/sfx_chain_short.ogg"
    "He pulled me back upright on my knees against him with surprising firmness."
    "My hands were still bound by the shackles, but I relished the release of the strain from hanging."
    "But my relief was short-lived as he grabbed my chin from behind and forced me to look into the cameras." with hpunchtiny
    fox eyeswide "You've been so quiet, darling!"
    fox -eyeswide "Why don't you say something nice for your admirers?"
    "His claws dug into my cheeks in direct contrast to his sickly sweet tone of voice."
    menu:
        " "
        "Stay quiet" if True:
            $ chat_love -= 1
            $ show_pollstat_3 = -1
            $ fox_love -= 1
            $ show_silence += 1
            "I clenched my jaw shut."
            fox angry "Tch."
            "He leaned forward and spoke in a voice only I could hear."
            fox "{i}Nobody likes a boring performer, you know.{/i}"
            fox "{i}If they don't like you... {w=0.5}{cps=20}I have no use for you.{/cps}{/i}"
            "He turned back to the camera and addressed whoever was watching."
            fox happy "I guess [pp_is] just shy!"
        "\"Please... I don't want to die...\"" if True:
            $ chat_love -= 1
            $ show_pollstat_3 = -1
            $ fox_love += 1
            "My voice trembled and broke. I didn't care."
            "He gleefully pressed his face beside mine."
            fox happy "You're so cute! {image=icon_heart}"
            fox -happy "I could just {i}eat you up!{/i}"
        "\"... Hi...\"" if True:
            $ chat_love += 1
            $ show_pollstat_3 = 1
            $ fox_love += 1
            fox "Ahah!"
            fox eyeswide "[pp_is_c] so shy!"
            "He forced my head to shake with his hand." with hpunch
            fox -eyeswide "That's okay though~"
            fox happy "We can see you're trying your best, can't we? {image=icon_heart}"
        "Spit at the camera" if True:
            $ chat_love += 2
            $ show_pollstat_3 = 2
            $ fox_love -= 2
            "I spat as hard as I could at the camera in front of me."
            fox angry "Ugh!"
            "I realized with some sense of satisfaction that I got the lens."
            show darkroom:
                xalign 0.5
                yalign 0.5
                easein_bounce 0.25 xalign 0.5 yalign 1.0
            show camera1:
                xalign 0.80
                yalign 1.0
                easein_bounce 0.25 xalign 0.80 yalign -0.8
            play sound "music/sfx_chain_short.ogg"
            "He shoved me forward onto my face." with vpunch
            "I struggled with my shackled wrists underneath me."
            $ stat_health -= 5
            $ stat_sanity -= 5
            play sound "<from 0.0 to 1.0>music/sfx_impact_thud.ogg"
            "-Until a swift kick collided with my ribs." with hpunchhard
            "Pain exploded through my torso."
            "I couldn't breathe."
            "I laid there paralyzed as his shoes walked past me to the camera."
            "A flash of metal on the tip of a shoe told me why it hurt so much."
            "I wondered if he broke a rib."
            fox "Tch. There."
            fox eyeswide "How is it? Nice and clear again?"
            fox angry "Yes, {i}very funny{/i}."
            fox "You guys are so-"
            "He started laughing."
            fox eyeswide "Really? You bet that much?"
            fox happy "You really do have excellent intuition, Diamond."
            fox "Congratulations on your big win!"
            fox eyeswide "Hm? Oh yes!"
            fox -eyeswide "Of course I haven't forgotten~"
            show darkroom:
                yalign 1
                easeout 0.25 yalign 0.5
            show camera1:
                yalign -0.8
                easeout 0.25 yalign 1.0
            play sound "music/sfx_chain_short.ogg"
            "A hand clasped around my neck and yanked me backwards onto my knees again."
            "I wheezed, still struggling to breathe."
            fox "Break time's over!"
    hide fox
    "Something wrapped around my neck from behind."
    $ stat_sanity -= 5
    "A wave of panic washed over me as I tried to grasp it with my bound hands."
    show darkroom:
        yalign 0.5
        easein_bounce 0.25 yalign 0.45
    show camera1:
        yalign 1.0
        easein_bounce 0.25 yalign 1.1
    play sound "<from 0 to 0.5>music/sfx_rope.ogg"
    "It was some sort of cable- pulling tighter and tighter."
    "I couldn't grab it."
    "I can't breathe!"
    "I tried to throw myself to the side, but all it did was tighten the wire around my neck." with hpunch
    "With increased urgency, I clawed at my own neck."
    "I can't-"
    fox "You know, Woundfucker..."
    "Panic eclipsed all other sensation."
    "I dug my own fingernails deep into my neck."
    fox eyeswide "I think I snaked this one from your boy!"
    "It wouldn't move. It's too tight, I can't..."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "The shackles on my wrists got heavier and heavier."
    fox -eyeswide "It was a little funny~ I think he was a bit upset!"
    "The wire... I have to..."
    "My shaking hands kept dropping as I mentally screamed at myself to lift them."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "To pull the wire off, to do anything."
    fox "He has good taste. Just like his old man! {image=icon_heart}"
    "My hands fell into my lap like lead."
    show black:
        alpha 0.0
        linear 3.0 alpha 1.0
    $ renpy.music.set_volume(0.0, 3.0, channel="music")
    "My vision darkened."
    "Fox's voice became jovial static."
    show black
    "I couldn't feel anything... nothing at all."
    pause(3.0)
    hide black
    show darkroom:
        xalign 0.5
        yalign 1.0
    show camera1:
        xalign 0.80
        yalign -0.8
    $ renpy.music.set_volume(1.0, 0.0, channel="music")
    play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
    "Something hit me." with vpunch
    "My desperate lungs tore a violent inhale from the air."
    "My body exploded into a terrible mess of coughing and sobbing."
    "I began to writhe against the ground."
    "When did I fall?"
    "What... is happening?"
    fox "... onation..."
    fox "We can wrap it up with..."
    p "Nghhh..."
    fox eyeswide "How's it going, sweetie?"
    p "Huh..?"
    fox "Fullyloaded wants to see you perform!"
    "I was still gasping, I could barely understand what was happening."
    fox -eyeswide "You need to {i}wake up!{/i}"
    "He grabbed my head."
    $ stat_health -= 5
    $ stat_sanity -= 5
    play sound "<from 0.0 to 1.0>music/sfx_impact_bone.ogg"
    "Before I could register what was happening, he slammed my face into the floor." with vpunchhard
    "I felt the crunch on the front of my face throughout my whole body."
    "I was fully paralyzed with agony."
    show darkroom:
        yalign 1
        easein_bounce 0.25 yalign 0.5
    show camera1:
        yalign -0.8
        easein_bounce 0.25 yalign 1.0
    play sound "<from 0 to 0.45>music/sfx_chain_retracted.ogg"
    queue sound "music/sfx_chain_short.ogg"
    "He pulled my wrists up and re-attached them to the chain above."
    "Blood streamed down my face."
    "I couldn't do anything but stare in shock."
    "He grabbed the sides of my head and forced me to look straight ahead."
    fox "Are you guys ready for the finale~?"
    if sexcontent != "no":
        "He pressed himself into the back of my head."
        "I froze in recognition as I felt his erection rub against the nape of my neck."
    "I was surprised to feel him let go and walk away."
    show fox comp gun with dissolve
    "When he came back, my blood ran cold."
    show fox gunup
    "He waved a gun in clear view of the cameras."
    p "No! W-wait!"
    fox gunback "Shhh, shh."
    fox "I'm not going to kill you."
    fox "... If you do a {i}good job{/i}, anyway~"
    fox "Actually..."
    show fox gun
    "He turned to his monitors."
    fox gunup "Why don't we play a little game?"
    fox "It'll be fun! {image=icon_heart}"
    show fox oncomputer with dissolve
    play sound "music/sfx_keyboard_2.ogg"
    "I heard the rapid tapping of a keyboard."
    show screen showDLC_vote(_layer="polllayer") with dis
    $ show_votepos = 5
    $ show_voteneg = 5
    fox comp gun "I've made a poll!" with Dissolve(0.25)
    show fox gunback
    "He turned back to me with a horrific glint in his eye."
    $ persistent.cgs_fox.add("cg_fox_gunjob_far")
    $ renpy.save_persistent()
    show fox gunjob far with dissolve
    play sound "music/sfx_gun_click.ogg"
    "I cringed involuntarily as he approached me and raised the gun to my face."
    if player_name.upper() == "STRADE":
        fox "Our toy here is going to open [pp_pos] mouth..."
    elif True:
        fox "[player_name] here is going to open [pp_pos] mouth..."
    if sexcontent != "no":
        fox "And give the barrel of the gun the best blowjob we've ever seen~!"
    elif True:
        fox "And suck on this gun until we're satisfied~!"
    p "What!?"
    fox "-And you guys will vote on whether or not... I pull the trigger!"
    fox "What do you think?"
    show fox comp gun with dissolve
    "I trembled as he read the screens."
    show fox comp gunback
    "He looked back at me."
    fox "You'd better get to work~"
    $ show_votepos += -1
    $ show_voteneg -= -1
    fox gunjob far "{i}They've already started voting{/i}."
    menu:
        " "
        "Refuse to participate" if True:
            $ show_votepos += -1
            $ show_voteneg -= -1
            p "I... I'm not doing that."
            "He's going to kill me anyway. I might as well keep my dignity."
            fox gunjob far eyeswide "Really?"
            fox gunjob far -eyeswide "{i}Are you sure?{/i}"
            $ show_votepos += -2
            $ show_voteneg -= -2
            p "You heard me!"
            show fox gunjob lookback
            "He glanced back at his monitor."
            $ show_votepos += -2
            $ show_voteneg -= -2
            fox "Oh my."
            fox "Chat seems to have made up their mind."
            fox "Well, thank you all for joining me for another wonderful stream!"
            fox "Everybody say \"Bye bye\"!"
            show fox gunjob far
            stop ambient fadeout 1.0
            "He looked back at me."
            fox gunjob far serious "Bye bye."
            $ renpy.hide_screen("showDLC_vote", layer="polllayer")
            play sound "music/sfx_gunshot.ogg"
            scene black with vpunch
            jump showDLC_dead_night1
        "Obey reluctantly" if True:
            $ chat_love += 3
            $ show_pollstat_4 = 3
            $ fox_love += 1
            "I don't... have a choice."
            "I leaned forward and opened my mouth."
            hide fox with dissolve
            show fox gunjob with dissolve
            "He gleefully shoved the gun inside."
            $ show_votepos += show_pollstat_1
            $ show_voteneg -= show_pollstat_1
            p "Hrk!"
            "I immediately tasted blood."
            "I suppressed a groan."
            "It must be from my nose... I'm sure it's broken."
            "It still hurts..."
            "My whole body hurts."
            "I steeled myself and stuck my tongue out along the gun barrel."
            "I can't think about that now. I need to just do this."
            $ show_votepos += -1
            $ show_voteneg -= -1
            show black with eyedissolve
            "I squeezed my eyes shut and tried to ignore the pain."
            "Ignore the gun."
            "Ignore the sound of him..."
            hide black with eyedissolve_reverse
            show fox gunjob narrow
            if sexcontent != "no":
                "Undoing his belt..?"
                "I risked a glance and my suspicions were confirmed."
                "He undid his pants and started palming himself."
            elif True:
                "Breathing..."
            "Eugh..."
            "Just lick the gun."
            $ show_votepos += show_pollstat_2
            $ show_voteneg -= show_pollstat_2
            "I moved my mouth and tried to make a show of it."
            "I felt sick..."
            if sexcontent != "no":
                "I could hear him panting."
            "No! Concentrate!"
            fox "Now you're getting it..."
            if sexcontent != "no":
                "He was practically moaning."
            "I made a show of licking the length of the gun barrel."
            $ show_votepos += -1
            $ show_voteneg -= -1
            "I couldn't stop myself from shuddering."
            fox gunjob -narrow "{i}Good{/i}..."
            if chat_love > 3:
                fox "It looks like Chat likes it too..."
            elif True:
                fox "You might have to work a little harder to impress Chat though..."
            $ show_votepos += show_pollstat_3
            $ show_voteneg -= show_pollstat_3
            "I wrapped my lips around the gun to stop myself from grimacing in disgust."
            "My thoughts wandered to the people watching."
            "\"Chat\"."
            "How many people were watching this..?"
            "I was shaking."
            fox "Come on..."
            "A tear rolled down my cheek as I felt a hot flush of shame."
            $ show_votepos += -1
            $ show_voteneg -= -1
            "I can't. I can't think about that."
            "I focused on my single task."
            "On survival."
            fox gunjob narrow "Just a little more~"
            if chat_love == 4:
                $ show_votepos += -1
                $ show_voteneg -= -1
            $ show_votepos += show_pollstat_4
            $ show_voteneg -= show_pollstat_4
            "I obeyed him and ignored everything else."
            "It's just..."
            "It's just a gun..."
        "Obey confidently" if True:
            $ chat_love += 1
            $ show_pollstat_4 = 1
            $ fox_love += 3
            "I can do this..."
            "I just have to imagine it's... it's not a gun."
            "I leaned forward and opened my mouth."
            hide fox with dissolve
            show fox gunjob with dissolve
            "He gleefully shoved the gun inside."
            $ show_votepos += show_pollstat_1
            $ show_voteneg -= show_pollstat_1
            p "Hng!"
            "I immediately tasted blood."
            "It must be from my face."
            "My nose must be broken..."
            "I won't let that distract me!"
            $ show_votepos += -1
            $ show_voteneg -= -1
            "I stuck my tongue out and made sure the cameras could see."
            "I'll give you a fucking show..."
            "I leaned further forward, straining against the chain above."
            show fox gunjob narrow
            "He responded by pushing the gun deep in my throat."
            $ show_votepos += show_pollstat_2
            $ show_voteneg -= show_pollstat_2
            "I choked briefly but kept my mind on task."
            "My life depends on this."
            "My body hurts so much..."
            "I turned a pained groan into a moan."
            show fox gunjob -narrow
            "I heard his breath catch, even through the mask."
            "It's working!"
            $ show_votepos += -1
            $ show_voteneg -= -1
            "I made sure to keep moving my tongue."
            "I was concentrating so hard on the cameras, I nearly missed the sounds he made."
            show fox gunjob narrow
            if sexcontent != "no":
                "Undoing his belt..?"
                "I risked a glance and my suspicions were confirmed."
                "He undid his pants and started palming himself."
            elif True:
                "Breathing hard..."
            "I'll take that as a good sign."
            "If he likes it..."
            "Maybe they like it."
            $ show_votepos += show_pollstat_3
            $ show_voteneg -= show_pollstat_3
            "I let out another moan for the cameras."
            "And if they like it, hopefully..."
            if sexcontent != "no":
                "I could hear him panting."
            $ show_votepos += -1
            $ show_voteneg -= -1
            "This isn't so hard."
            fox "Now you're getting it..."
            if sexcontent != "no":
                "He was practically moaning."
            "I made a show of licking the length of the gun barrel."
            "I was shivering."
            fox "{i}Good{/i}..."
            if chat_love > 3:
                fox "It looks like Chat likes it too..."
            elif True:
                fox "You might have to work a little harder to impress Chat though..."
            "I wrapped my lips around the gun."
            "My thoughts wandered to the people watching."
            "\"Chat\"."
            "How many people were watching this..?"
            "My shivering became shaking."
            fox "Come on..."
            if chat_love == 4:
                $ show_votepos += -1
                $ show_voteneg -= -1
            "I could feel a hot flush flooding my face."
            "Is it them watching me?"
            "Is it him?"
            "Or... or am I..."
            "I have to focus!"
            "On survival."
            fox "Just a little more~"
            $ show_votepos += show_pollstat_4
            $ show_voteneg -= show_pollstat_4
            "I obeyed him and ignored everything else."
            "It's just..."
            "It's just a gun..."
    if chat_love >= 5:
        hide fox with dissolve
        show fox gunjob far with dissolve
        "I gasped as the gun was suddenly withdrawn from my mouth."
        fox gunjob far eyeswide "You're a natural~!"
        $ renpy.hide_screen("showDLC_vote", layer="polllayer")
        fox "And it looks like Chat was impressed!"
        show fox ultraclose with dissolve
        "He placed the gun on a table."
        "A little flutter of hope lit up in my chest."
        fox ultraclose eyeswide "They like you~ and they want to see more!"
        p "They... do?"
        fox ultraclose happy "That's right, darling!"
        if sexcontent != "no":
            "He was still breathing hard... and still touching himself."
        elif True:
            "He was still breathing hard."
        fox ultraclose -happy "Although..."
        fox "I think we should give them one more little treat before we wrap up for the night."
        hide fox with dissolve
        show darkroom:
            yalign 0.5
            easein_bounce 0.25 yalign 0.6
        show camera1:
            yalign 1.0
            easein_bounce 0.25 yalign 0.6
        play sound "music/sfx_chain_short.ogg"
        if sexcontent != "no":
            "The chain above me loosened as he shoved my head down."
            p "Whu-"
        "He grabbed my head in an iron grip."
        show darkroom:
            yalign 0.6
            xalign 0.5
            easeout 0.25 yalign 0.4 xalign 0.2 rotate 10
        show camera1:
            yalign 0.6
            xalign 0.8
            easeout 0.25 yalign 2.0 xalign 1.5
        pause 0.25
        $ persistent.cgs_fox.add("cg_fox_standover")
        $ renpy.save_persistent()
        if sexcontent == "yes":
            $ persistent.cgs_fox_sex.add("cg_fox_nsfw1")
            $ renpy.save_persistent()
            show fox standover cock:
                xalign 0.5
                yalign 0.5
            with dissolve
        elif True:
            show fox standover:
                xalign 0.5
                yalign 0.5
            with dissolve
        "Two clawed fingers forced the eyelid of my right eye open."
        "Panic flooded back through my system."
        p "What are you doing!?"
        if sexcontent != "no":
            $ persistent.cgs_fox_sex.add("cg_fox_nsfw2")
            $ renpy.save_persistent()
            "His other hand went back to work, stroking himself."
            if sexcontent == "yes":
                show fox cock with dissolve
            "He positioned himself above my eye."
        elif True:
            "His claw hovered over my exposed eye."
        p "No! Don't!"
        if sexcontent != "no":
            "His moans started to sound like growling."
        "I can't move! I can't-"
        $ stat_health -= 5
        $ stat_sanity -= 5
        scene black
        hide fox
        play sound "<from 0.0 to 0.5>music/sfx_gore_2.ogg" volume 0.5
        if sexcontent != "no":
            "In a single instant, hot cum shot into my eye, and I instinctively jerked my head." with vpunch
        elif True:
            "He shoved the claw into my eye." with vpunch
        "I screamed at the searing pain in my skull."
        if sexcontent != "no":
            "His claw had plunged into my eye when I moved."
        "My scream trailed off into an agonized groan."
        "His painful grip stayed for so long."
        show darkroom behind black:
            yalign 1.0
            xalign 0.5
        show camera1 behind black:
            yalign -0.5
            xalign 0.8
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

        hide black with dissolve
        "Until it finally dropped away."
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

        if sexcontent != "no":
            "My face was drenched in blood, and other liquids I didn't want to think about."
        elif True:
            "My face was absolutely covered. In blood, and..."
        if sexcontent != "no":
            "His heavy breathing finally evened out and he tucked himself back into his pants."
            "The humiliation was just a faraway buzzing in comparison to the agony."
        "My eye... I can't see from it..."
        "Did he, did he really..?"
        show darkroom:
            yalign 1.0
            easeout 0.25 yalign 0.5
        show camera1:
            yalign -0.5
            easeout 0.25 yalign 1.0
        pause 0.25
        show fox comp cocked with dissolve
        "My attention snapped back to him as he composed himself with a satisfied sigh."
        fox "I thought you might like that... Haha!"
        "He was talking to {i}them{/i} again."
        fox comp -cocked "A perfect end to a perfect stream~"
        fox comp presenting "Thank you so much for joining me, my delightful patrons!"
        if player_name.upper() == "STRADE":
            fox comp lookback "And let's show a little appreciation for our lovely star!"
        elif True:
            fox comp lookback "And let's show a little appreciation for our lovely star, [player_name]!"
        fox comp -lookback "Hahaha!"
        fox "Yes, I agree~"
        fox "Well, I'm sure we'll have plenty of fun {i}next time{/i} too!"
        fox "Good night for now! {image=icon_heart}"
        "He made the motion of blowing a kiss to the camera."
        stop ambient fadeout 10.0
        show fox oncomputer with dissolve
        play sound "music/sfx_keyboard_1.ogg" volume 0.5
        "Then he clicked something and tapped away at the keyboard."
        jump showDLC_intermission_1
    elif True:
        hide fox with dissolve
        show fox gunjob lookback with dissolve
        stop ambient fadeout 1.0
        "My thoughts were interrupted as the gun was suddenly pulled from my mouth."
        "He was looking at the screen."
        if fox_love >= 5:
            fox gunjob far eyeswide "What a damn shame."
            fox gunjob far -eyeswide "I thought you did really well~"
            "Wait... what?"
            fox gunjob far serious "But they're the ones in charge."
        elif True:
            fox gunjob far eyeswide "Uh oh!"
            fox gunjob far -eyeswide "Chat says your time is up~! {image=icon_heart}"
        if meme_mode:
            show fox gunjob eyeswide
            p "WHAT!?"
            fox gunjob far "They-"
            p "The fuck you MEAN?"
            p "I gave the best goddamned glock gluck gluck these people have ever SEEN!"
            fox gunjob far serious "... Don't call it that."
            p "Oh yeah?"
            p "What are you gonna do? Shoot me?"
        $ renpy.hide_screen("showDLC_vote", layer="polllayer")
        stop ambient
        play sound "music/sfx_gunshot.ogg"
        scene black with vpunch
        jump showDLC_dead_night1

label showDLC_dead_night1:
    if achievement.has("ach_show_1") != True:
        $ persistent.ach_show_1 = True
        $ achievement.grant("ach_show_1")
        init:
            $ achievement.register("ach_show_1")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_show_1 == True and achievement.has("ach_show_1") != True:
                $ achievement.grant("ach_show_1")
                $ achievement.register("ach_show_1")
                $ achievement.sync()
    scene black with dissolve
    hide screen status
    $ quick_menu = False
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You failed to perform - Show 1")
    $ renpy.pause(hard=True)
label showDLC_intermission_1:
    hide fox with dissolve
    show fox -oncomputer:
        yoffset 225
        yalign 1.0
        xalign 0.5
    with dissolve
    "He sighed and turned to me."
    "I squinted up at him painfully with my one good eye."
    hide fox with dissolve
    show fox eyeswide nomask:
        xalign 0.5
        yalign 1.0
        yoffset 225
    play music "music/ambient_fox_extra_01.ogg" fadein 1.0
    "To my surprise, he had pulled off his mask."
    if achievement.has("ach_show_1") != True:
        $ persistent.ach_show_1 = True
        $ achievement.grant("ach_show_1")
        init:
            $ achievement.register("ach_show_1")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_show_1 == True and achievement.has("ach_show_1") != True:
                $ achievement.grant("ach_show_1")
                $ achievement.register("ach_show_1")
                $ achievement.sync()
    fox "Well... you've survived a show!"
    fox "That's not very common you know. You should be proud of yourself!"
    "I had no idea what to feel."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    "Everything hurt so much."
    fox cocked nomask "As {i}adorable{/i} as you are like that, we should get you cleaned up."
    "His voice sounded different without the mask."
    show black with eyedissolve
    hide fox
    "My brain was barely holding on to the concept."
    $ persistent.cgs_fox.add("cg_fox_nomask")
    $ renpy.save_persistent()
    show fox ultraclose eyeswide nomask
    hide black with eyedissolve_reverse
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    fox "Hey..."
    "Suddenly he was holding my face, looking at me."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    p "Uhnnn..."
    "Snapping fingers..."
    "I'm tired..."
    stop music fadeout 2.0
    scene black with eyedissolve
    pause(3.0)
    $ persistent.cgs_fox.add("cg_foxbg_light")
    $ renpy.save_persistent()
    play music "music/ambient_fox_03.ogg" fadein 1.0
    scene lightroom:
        yalign 0.0
        xalign 0.5
    with eyedissolve_reverse
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    fox light "Theeeere you go."
    p "Huh..?"
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    show lightroom:
        yalign 0.0
        easeout 0.25 yalign 0.45
    show fox light:
        xalign 0.5
        yoffset 1200
        easeout 0.25 yoffset 0
    fox "You passed out."
    show lightroom:
        yalign 0.45
    fox "Can't blame you, really. You did lose a lot of blood."
    "I gasped as I saw him clearly for the first time."
    "He's older than I realized... and he really is short..."
    show fox light tail
    "But clearly inhuman as well."
    show lightroom:
        easein 0.25 xalign 0.3
        pause 0.5
        easeout 0.15 xalign 0.5
        easein 0.25 xalign 1.0
        pause 0.5
        easeout 0.25 xalign 0.5
    show fox light:
        easein 0.25 xalign 1.8
        pause 0.5
        easeout 0.15 xalign 0.5
        easein 0.25 xalign -2.0
        pause 0.5
        easeout 0.25 xalign 0.5
    "I looked around at the empty room around me."
    "Why can't I see-"
    "I held up a hand to touch my eye and found bandages."
    p "M-my eye!"
    fox light cocked "Mmmm, yes~"
    fox "Bit of a shame, but you have a spare, hm?"
    p "I did what you said!"
    p "I survived! You said..."
    fox light -cocked "That's right!"
    fox light smile "And you did very well~ {image=icon_heart}"
    p "Aren't you... gonna let me go..?"
    show fox light laugh at laugh
    "He responded in that sharp bark of a laugh."
    fox light smile "Oh, sweetie."
    fox light -smile "You're not going to be leaving."
    "A lump caught in my throat."
    fox "You have a job now!"
    fox "You need to keep {i}performing{/i}."
    p "What!?"
    fox "In fact, you'd better get some rest."
    fox light smile "You'll want to heal as best you can for our {i}next{/i} show!"
    hide fox with dissolve
    "He stepped towards the door."
    "No! That can't be it!"
    show lightroom:
        easeout 0.25 yalign 0.4
        easein 0.15 yalign 0.5
        easein_bounce 0.25 yalign 1.0
    pause 0.65
    play sound "music/sfx_impact_thud.ogg" volume 0.5
    $ stat_health -= 1
    "I lunged forward and immediately crumpled to the floor"
    "Searing pain shot up my foot."
    fox light "Yeah... you might want to stay off that foot."
    fox "Don't want to tear your stitches now!"
    "I cradled my foot and tried not to cry."
    if player_name.upper() == "STRADE":
        fox "Good night~"
    elif True:
        fox "Good night, [player_name]~"
    p "Wait!"
    show lightroom:
        easein 0.25 yalign 0.5
    pause 0.25
    show lightroom:
        xalign 0.5
        yalign 0.5
    show fox light with dissolve
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    menu:
        " "
        "\"... Nothing...\"" if True:
            $ fox_love += 1
            fox "..."
            fox "Sleep tight."
        "\"Who are you?\"" if True:
            fox light cocked "Did you forget?"
            fox light -cocked "I told you that you can call me Fox."
            p "But..."
            p "Who are you really?"
            p "{i}What{/i} are you?"
            fox light cocked "Have you been under a rock for the last five years?"
            "Embarrassment crept up my face."
            if meme_mode:
                p "I-I heard, yeah... {i}'furry'{/i}... right?"
                fox light serious "What? No."
                fox "Get your shit together."
            elif True:
                p "I-I heard, yeah... {i}'beastkin'{/i}... right?"
                fox light -cocked "Well then. You're all up to speed."
            p "But I-"
            fox light "Sleep tight."
        "\"Why are you doing this?\"" if True:
            show fox light laugh at laugh
            fox light laugh "Haha! \"Why?\""
            fox light -laugh "They always ask {i}why{/i}..."
            fox light "Fine, I'll tell you."
            fox light smile "Because I'm {i}really{/i} fucking good at it."
            "I didn't know how to respond to that."
            "I could only stare at him in disbelief."
            fox light -smile "Sleep tight."
        "\"Let me GO!\"" if True:
            $ fox_love -= 1
            show fox light laugh at laugh
            "He laughed again."
            "This time I noticed his sharp teeth."
            fox light -laugh "You know I'm not going to let you go."
            fox "You're going to keep performing..."
            fox "As long as Chat finds you more interesting alive than dead."
            fox light cocked "So maybe, you should think about working on your act."
            fox light -cocked "Sleep tight~"
    hide fox with dissolve
    play music "music/ambient_fox_04.ogg" fadein 1.0
    play sound "music/sfx_door_slam.ogg"
    "I stared at the door."
    "Then I looked around myself."
    if meme_mode:
        "Absolutely nothing, aside from a litter box in the corner and some kind of foam mattress."
    elif True:
        "Absolutely nothing, aside from a toilet in the corner and some kind of foam mattress."
    menu:
        " "
        "Try to escape" if True:
            "I huffed and stood up straight."
            "I have to try."
            "I tried the door first."
            "..."
            "Locked. And extremely heavy duty."
            "I sighed."
            "I guess I should have expected that."
            "I spent another hour or so examining the room."
            "The mattress, toilet, and every corner, every seam of wall to floor."
            "But..."
            "There's nothing."
            $ stat_sanity -= 10
            "This was a huge waste of time."
            show lightroom:
                easein_bounce 0.25 yalign 0.0
            "I flopped down on the foam pad."
            "I gazed up at the ceiling and noticed one of the lights was out."
            "Wait."
            "That's not a light."
            $ stat_sanity -= 10
            "It's a camera..."
            "He could have been watching me. He might be watching me now."
            "I curled up, disturbed."
            scene black with eyedissolve
            "I can't think about that now."
            "I need to just get some rest."
        "Go to sleep" if True:
            "I dragged myself painfully, wearily to the foam pad on the floor."
            show lightroom:
                easein_bounce 0.25 yalign 0.0
            "And I flopped down."
            "There's no point in working myself up now."
            scene black with eyedissolve
            "My body hurts too much."
            "I just want to sleep."
    pause(2.0)
    $ stat_sanity += 20
    show lightroom:
        xalign 0.5
        yalign 0.5
    with eyedissolve_reverse
    "I woke up slowly, my body aching."
    "The memory of the night before came flooding back to me with a wave of panic."
    "As I stared at my empty confines, the panic slowly turned to misery."
    show lightroom:
        easein 0.25 yalign 0.75
    "I looked down at myself and froze."
    "Plain underwear..."
    if show_event_dressup == 1:
        "He undressed me when I was knocked out, {i}again!{/i}"
    elif True:
        "He undressed me when I was knocked out!"
    show lightroom:
        easein 0.25 yalign 0.0
    "I shivered at the thought before laying back down."
    "There's no point in getting upset now."
    scene black with eyedissolve
    "I rolled over and closed my eyes."
    "I stayed in that room for what felt like days, but it was impossible to tell."
    "No windows... no change in the lights."
    "Nothing to look at, at all."
    "The maddening silence was only broken once every several hours;"
    "A meager meal of bread and water in a paper cup being pushed through a slot at the bottom of the door."
    "I considered starving myself."
    "But I didn't have the strength."
    "So I ate."
    "And I rested. I tried to pretend I was in a hospital."
    "That everything was fine..."
    "Some of my wounds began to feel a little better."
    "But my eye didn't."
    "It felt hot and itchy."
    "I was too afraid to lift the bandages."
    "{i}Coward.{/i}"
    "I shook the thought from my head."
    "I let myself drift away into a wavering unconsciousness."
    stop music fadeout 3.0
    pause(2.0)
    $ stat_sanity += 20
label showDLC_show_2:
    scene lightroom:
        yalign 0.5
        xalign 0.5
    with eyedissolve_reverse
    play music "music/ambient_fox_03.ogg"
    "The sound of the heavy door swinging open jolted me out of a restless nap."
    show fox light with dissolve
    if player_name.upper() == "STRADE":
        fox "Hello..."
    elif True:
        fox "Hello, [player_name]."
    fox light cocked "It's time for you to get to work again~"
    "I shot upright and I unconsciously shuffled backwards."
    "He's back... He came back..."
    show goonk behind fox:
        alpha 0
        xalign 0.5
        yalign 1.0
        easein 0.25 xalign 0.8 alpha 1.0
    pause 0.5
    show goonr behind goonk:
        alpha 0
        xalign 0.5
        yalign 1.0
        easein 0.25 xalign 0.2 alpha 1.0
    pause 0.75
    show lightroom:
        easein_expo 1.0 yalign 0.4
    show goonr:
        yoffset 0
        easein_expo 1.0 yoffset 100
    show goonk:
        yoffset 0
        easein_expo 1.0 yoffset 100
    show fox light cocked:
        yoffset 0
        easein_expo 1.0 yoffset 80
    pause 1.0
    show goonr:
        yoffset 100
        yalign 1.0
        xalign 0.2
        alpha 1.0
    show goonk:
        yoffset 100
        yalign 1.0
        xalign 0.8
        alpha 1.0
    "Before I could say anything, two huge guards entered the room behind him."
    "They made him look even shorter, but somehow..."
    "The air of malice still came directly from him."
    fox light -cocked "You need to get dressed."
    p "D-dressed?"
    "My own voice sounded foreign to me."
    "I realized I hadn't spoken in days."
    "He threw a wad of black netting in front of me."
    fox light cocked "Yes, {i}dressed{/i}."
    "I grabbed and examined the wad of material."
    "It unfurled into some sort of bodysuit made entirely of... fishnet."
    "Complete with underwear that looked much too small for me."
    "I looked back up to him. Surely he doesn't..."
    show fox light serious
    "He sighed with obvious annoyance."
    fox "We're on a {i}schedule{/i}. You can get dressed, or I'll have them do it for you."
    "I looked at the pair of goons and gulped."
    menu:
        " "
        "Get dressed" if True:
            $ fox_love += 1
            show fox light -serious
            p "I can do it myself!"
            p "I..."
            "I held up the scant netting."
            "Ugh..."
            "I hooked a thumb in my underwear and looked up, half expecting them to turn around."
            "But of course they didn't."
            show lightroom:
                easein_expo 0.25 yalign 0.5
            show goonr:
                easein_expo 0.25 yoffset 0
            show goonk:
                easein_expo 0.25 yoffset 0
            show fox light cocked:
                easein_expo 0.25 yoffset 0
            "I shakily removed my underwear, trying to cover myself."
            "Thankfully, they seemed to not react at all."
            "I hastily pulled on the new underwear."
            "I was a bit relieved to find that it was extremely stretchy."
            "But it was still... terribly revealing."
            "I sighed in defeat and pulled the fishnet over my body."
            show lightroom:
                easein_expo 0.25 yalign 0.4
            show goonr:
                easein_expo 0.25 yoffset 100
            show goonk:
                easein_expo 0.25 yoffset 100
            show fox light cocked:
                easein_expo 0.25 yoffset 80
            fox light cocked "Ahh, lovely~ {image=icon_heart}"
            fox light -cocked "Stand up straight and turn."
            "I could feel myself flushing hotly."
            "I tried to remind myself that this is surely better than what's coming."
            "... The thought didn't help much."
            "I obeyed him and turned around slowly."
            fox light smile "Perfect."
            "He {i}did{/i} sound pretty happy."
            "Hopefully I bought myself some mercy..."
            show fox light -smile
            show goonk:
                easein_expo 0.25 xalign 1.0 alpha 0.0
            "He made a motion towards me, and a guard approached."
            "I stayed still as he circled behind me and pulled my arms back." with vpunch
            play sound "<from 0 to 0.25>music/sfx_chain_retracted.ogg"
            "A click- and the familiar weight of metal shackles weighed my wrists down."
        "Refuse" if True:
            $ fox_love -= 1
            p "I'm... not wearing this."
            fox "Suit yourself."
            show goonk:
                easein_expo 0.25 xalign 1.0 alpha 0.0
            pause 0.5
            show goonr:
                easein_expo 0.25 xalign 0.0 alpha 0.0
            "He motioned lazily toward me, and the guards immediately went into action."
            p "Wait! I-"
            hide fox with dissolve
            show lightroom:
                easeout 0.25 yalign 0.4
                easein 0.15 yalign 0.5
                easein_bounce 0.25 yalign 1.0
            pause 0.55
            play sound "music/sfx_impact_thud.ogg" volume 0.5
            "Rough hands grabbed me and shoved me down to the floor with brutal speed."
            "The rest of my sentence came out as a wheeze as I was pressed into the concrete."
            "I could hardly get out a yelp of suprise as my underwear was yanked off."
            "The new pair was pulled on almost as quickly."
            "The rest of the outfit was pulled over me with the same mechanical efficiency."
            "I was entirely powerless to do anything about it."
            show lightroom:
                easein_bounce 0.5 yalign 0.5
            pause 0.5
            show fox light serious with dissolve
            "Then, I was pulled to my feet."
            "I winced as my weight fell on my still-injured sole." with vpunch
            "It distracted me from my arms being pulled behind my back."
            play sound "<from 0 to 0.25>music/sfx_chain_retracted.ogg"
            "A click- and the familiar weight of metal shackles weighed my wrists down."
            show goonk:
                yoffset 0
                easein_expo 0.25 xalign 0.8 alpha 1.0
            pause 0.5
            show goonr:
                yoffset 0
                easein_expo 0.25 xalign 0.2 alpha 1.0
            fox "You're lucky you're going on camera right away."
            show lightroom:
                easein_expo 1.0 yalign 0.4
            show goonr:
                yoffset 0
                easein_expo 1.0 yoffset 100
            show goonk:
                yoffset 0
                easein_expo 1.0 yoffset 100
            show fox light cocked:
                yoffset 0
                easein_expo 1.0 yoffset 80
            pause 0.75
            show goonk smile
            show goonr smile
            fox light -serious "Or I would have let them do a lot more than {i}dress{/i} you."
            show fox light serious
    fox "Now, come on."
    fox "We don't have any more time."
    scene black with dissolve
    stop music fadeout 1.0
    "The guard pushed me forward and out of the room."
    "I was walked down a few dark hallways before we stopped at another heavy door."
    "As I was pushed through into the darkness, I smelled old blood."
    play music "music/ambient_fox_06.ogg" fadein 1.0
    scene darkroom:
        xalign 0.5
        yalign 0.4
    show camera1:
        xalign 0.80 yalign 1.0 yoffset 100
    with dissolve
    "I saw the screens... the chain."
    show darkroom:
        easein_bounce 0.25 yalign 0.5
    show camera1:
        easein_bounce 0.25 yoffset 0
    play sound "music/sfx_chain_short.ogg"
    "I was pushed to my knees below it."
    "Not this room... Not this room!"
    "I couldn't stop the panic from buzzing in my brain."
    play sound "<from 0 to 0.25>music/sfx_chain_retracted.ogg"
    "My feet were shackled to the floor."
    "Please... not again..."
    play sound "<from 0 to 0.25>music/sfx_chain_retracted.ogg"
    "My wrist shackles were attached the chain."
    fox "That'll be all."
    play sound "music/sfx_door_slam.ogg"
    "Heavy footsteps left the room, and the door thudded shut with terrifying finality."
    "There was an awful voice in my head, repeating the same thing over and over."
    "{i}You're not going to survive this again.{/i}"
    "A hand grabbed my face."
    show fox close touch with dissolve
    fox "Are you ready?"
    if fox_love >= 3:
        fox "Just take a deep breath."
        fox "I think you'll..."
        fox "..."
        fox "Well, we're about to go on~"
    show fox oncomputer with dissolve
    "He let me go without waiting for an answer."
    play sound "music/sfx_keyboard_2.ogg"
    "Then he tapped at the keyboard."
    "He rolled his shoulders and sighed."
    show fox comp with dissolve
    "Then he straightened."
    fox comp presenting "Hello my dear friends, and welcome back!"
    fox "I see it's gotten a bit busier in here!"
    fox comp -presenting "How exciting!"
    fox comp cocked "I bet I can guess why that is~"
    if player_name.upper() == "STRADE":
        fox "You've fallen in love with our toy, haven't you? {image=icon_heart}"
    elif True:
        fox "You've fallen in love with [player_name], haven't you? {image=icon_heart}"
    show fox comp -cocked
    "He laughed- not in his usual bark, but the light and controlled laugh of a host."
    fox "Well, I'm {i}pleased{/i} to share [pp_obj] with you~"
    show fox comp lookback:
        easein 0.25 xalign 0.3
    "He stepped out of the way and gestured to me."
    "I slumped into my bonds."
    "I know them now... There's no point in begging or crying for help."
    fox "Oh, come on now."
    fox "Don't be shy!"
    fox comp lookback laugh "Say hi to your admirers!"
    menu:
        " "
        "\"Hi.\"" if True:
            $ fox_love += 1
            "I looked into the camera and spoke clearly."
            "There's no point in resisting now."
            show fox close touch:
                xalign 0.5
            with dissolve
            "He grabbed my face again, squeezing my cheeks and shaking it slightly." with hpunchtiny
            fox close touch happy "So cute~!"
            hide fox with dissolve
            show fox comp with dissolve
            "He turned back to the camera."
        "\"Please go easy on me...\"" if True:
            $ fox_love += 2
            $ chat_love += 1
            "I looked at the camera and tried to smile."
            "I knew it was shaky and weak, but..."
            "Maybe... maybe if I charm them, they won't..."
            show fox eyeswide:
                xalign 0.5
                yalign 1.0
                yoffset 180
            with dissolve
            fox eyeswide "Oh..."
            fox cocked "How {i}adorable{/i}~"
            "He stared at me for a moment."
            hide fox with dissolve
            show fox comp with dissolve
            "Then he turned back to the camera."
        "\"Eat shit and die!\"" if True:
            $ chat_love += 2
            $ fox_love -=1
            show fox comp lookback -laugh
            "I was surprised at the bubble of anger in my chest."
            "That I even had the energy to feel it still."
            fox "Hm."
            show fox comp:
                xalign 0.5
            "He scoffed before turning back to his screens."
            fox comp presenting "... Ha!"
            fox "You guys really like the {i}spicy{/i} ones, hm?"
            fox comp -presenting "And I see some happy gamblers already!"
            fox comp cocked "Well. You all are in for a treat~"
            fox comp -cocked "We've barely gotten started!"
        "Stay silent" if True:
            $ chat_love -= 1
            $ fox_love -=1
            $ show_silence += 1
            fox comp lookback -laugh "..."
            fox "Not in the mood for conversation, hm?"
            if show_silence >= 3:
                fox "Our stoic little star..."
            fox "Well, that's alright~"
            fox comp lookback laugh "We'll have you singing soon enough!"
            "He chuckled softly."
            show fox comp:
                xalign 0.5
            "Then he turned back to the camera."
    fox "Now, I was thinking we'd start off with-"
    fox oncomputer "Mm?" with dissolve
    fox comp "\"What happened to [pp_pos] eye?\"" with dissolve
    fox "Ah, how careless of me. My apologies."
    fox comp cocked "Some of you weren't here last time!"
    fox comp presenting "Allow me to show off our {i}previous work!{/i}"
    hide fox with dissolve
    show camera1 tripod with dissolve
    "He lifted a camera off of its tripod."
    $ persistent.cgs_fox.add("cg_fox_holdingcam")
    $ renpy.save_persistent()
    show fox holdingcam:
        yalign 0.0
        xoffset 0
    with dissolve
    "Then he brought it close to me."
    "I could feel myself cringing away from the invasive lens."
    show fox holdingcam:
        xoffset 0
        alpha 1.0
        easeout 0.25 xoffset -50 alpha 0.0
    "He circled behind me."
    hide fox
    fox "The foot was fun~!"
    fox "It looks like it's... healing pretty well."
    "I yelped involuntarily as a claw prodded the stitches at the bottom of my foot."
    "It was certainly rough enough to draw blood, but I couldn't see."
    show fox holdingcam:
        alpha 0.0
        xoffset 50
        easeout 0.25 xoffset 0 alpha 1.0
    "He came back around."
    fox "Can you see the bruises?"
    fox "Oh!"
    "He shoved the camera close to my chest."
    fox "It's a little hard to tell with the fishnets right now, but we had to sew [pp_obj] up here, too~"
    fox "And of course..."
    "He brought the camera up to my face, hovering above the bandage over my eye."
    fox "I suppose you'd like to see what's under here, hmmm~?"
    "Without warning, he unhooked the back of the bandage and hastily unwrapped it."
    p "Ah! W-wait!"
    "The last part was stuck..."
    $ stat_sanity -= 5
    $ stat_health -= 1
    play sound "<from 0.5 to 1.0>music/sfx_fabric_tear.ogg" volume 0.5
    "He tugged it and it tore away from the flesh and dried fluid it was fused with." with hpunch
    "Stinging pain returned... and I felt a warm drop roll down my face."
    fox "Wow..."
    fox "Maybe we should have changed that bandage... it doesn't look so good."
    "He actually sounded a little bit apologetic."
    "I assumed it was just for the cameras."
    hide fox with dissolve
    show camera1 with dissolve
    show fox comp with dissolve
    "He delicately placed the camera back on its tripod and took a moment to read his screens."
    fox "Hahaha!"
    fox "Now, now."
    fox comp cocked "You {i}know{/i} that kills them. Every time."
    fox comp -cocked "We can't do that before we've even done anything..."
    fox comp presenting "Where's the fun in {i}that?{/i}"
    fox comp "Let's start with something a little more... nuanced."
    hide fox with dissolve
    "He left for a moment as he retrieved something."
    show fox comp soldering with dissolve
    "Then he held it up to the camera."
    fox "You've got to be {i}patient{/i} if you want to appreciate the finer things in life."
    fox "Haha! So... plenty of you seem to remember what this is."
    fox comp soldering cocked "Anyone have any design ideas~?"
    "He went silent for a moment as he seemed to consider whatever 'Chat' was writing."
    if fox_love >= 3:
        $ show_design = "heart"
        fox comp soldering -cocked "Hmmm. Hmmm."
        fox "Interesting ideas..."
        fox comp soldering cocked "I'm not so sure about the artistic vision though..."
        fox comp soldering -cocked "Let's do a {i}classic{/i} design, for old time's sake!"
    elif True:
        $ show_design = "diamond"
        fox comp soldering -cocked "Oh ho!"
        fox "So many suggestions!"
        fox comp soldering cocked "You all want a piece of the canvas, hm~?"
        fox comp soldering -cocked "Woah!"
        fox "Sorry everyone!"
        show fox comp soldering shrug
        "He chuckled and shrugged in an overly animated way."
        fox "Looks like {i}big spender Diamond{/i} wants to make her mark!"
        fox comp soldering -shrug "Your wish is my command~"
        fox "A diamond for the lady, and a show for the rest of us! {image=icon_heart}"
    fox comp soldering cocked "Shall we get to work then~?"
    hide fox with dissolve
    "Fear prickled up my neck as he made his way to me."
    show fox close soldering:
        yalign 0
        xalign 0.5
    with dissolve
    "He lifted the item in front of me this time."
    fox "Do {i}you{/i} know what this is?"
    menu:
        " "
        "\"Please don't hurt me any more, {i}please!{/i}\"" if True:
            $ fox_love += 1
            $ chat_love -= 1
            fox close touch "Aww~ {image=icon_heart}" with dissolve
            show fox close touch happy
            "He cupped the side of my face gently."
            fox "You know that's not going to work, sweetie."
            show fox close whisper with dissolve
            "He leaned in close, next to my ear."
            fox "But I {i}do{/i} love to hear it..."
            show fox close touch happy with dissolve
            fox "Let's get started, shall we?"
            show fox close touch happy:
                xalign 0.5
                alpha 1.0
                easeout 0.25 xalign 0.45 alpha 0.0
        "\"Just get it over with!\"" if True:
            $ chat_love += 1
            fox close touch happy "Hahaha!" with dissolve
            fox "So spirited~!"
            fox "So full of energy..."
            fox close touch -happy "{i}Let's see how well that lasts.{/i}"
            show fox close touch:
                xalign 0.5
                alpha 1.0
                easeout 0.25 xalign 0.45 alpha 0.0
        "\"A... glue gun? I-I don't know.\"" if True:
            $ fox_love += 1
            $ chat_love += 1
            show fox close touch happy with dissolve
            "He leaned back and barked out a laugh."
            fox "That's close, I suppose!"
            fox "Close enough."
            fox close touch -happy "Let's get started, shall we?"
            show fox close touch:
                xalign 0.5
                alpha 1.0
                easeout 0.25 xalign 0.45 alpha 0.0
        "\"That's a soldering gun.\"" if True:
            $ fox_love += 1
            $ chat_love -= 1
            "The shape was unmistakable."
            "A lump formed in my throat."
            fox close soldering eyeswide "Ohhh~"
            fox "So, you're cute {i}and{/i} clever..."
            fox close soldering -eyeswide "That's absolutely right! {image=icon_heart}"
            "I could feel myself beginning to shake."
            "I knew exactly what was about to happen."
            fox close touch happy "Let's get started, shall we?" with dissolve
            show fox close touch happy:
                xalign 0.5
                alpha 1.0
                easeout 0.25 xalign 0.45 alpha 0.0
        "Remain silent" if not meme_mode:
            $ fox_love -= 1
            $ chat_love -= 1
            $ show_silence += 1
            if show_silence >= 3:
                fox close serious "Nothing? Again?"
                fox "I can forgive a little stage fright.."
                fox "But I don't think Chat is enjoying your {i}bland{/i} performance at all."
            elif True:
                if player_name.upper() == "STRADE":
                    fox close serious "I asked you a {i}question{/i}."
                elif True:
                    fox close serious "I asked you a {i}question{/i}, [player_name]."
                fox "It's {i}rude{/i} to ignore me."
                fox "And you know that Chat abhors a bland performance~"
            fox "Well."
            fox close soldering "I think I can cure your silence anyway~"
            show fox close soldering:
                xalign 0.5
                alpha 1.0
                easeout 0.25 xalign 0.45 alpha 0.0
        "\"A bedazzler?\"" if meme_mode:
            fox close "A what?"
            p "A bedazzler. It bedazzles stuff."
            p "With like, rhinestones..."
            fox close serious "..."
            fox "No."
            fox "No, it is not a 'bedazzler'."
            show fox close serious:
                xalign 0.5
                alpha 1.0
                easeout 0.25 xalign 0.45 alpha 0.0
    "He circled around to my back again, where I couldn't see."
    hide fox
    fox "Hm."
    fox "Your cute little fishnet is in the way~"
    "I felt a few claws touch my bare skin."
    "I couldn't help but shiver and arch away."
    "I could hear his breathing get deeper."
    "I steadied myself and prepared for pain-"
    play sound "<from 9.3 to 10.5>music/sfx_fabric_tear.ogg" volume 0.5
    "But I only heard the faint tear of fishnet instead."
    "When...? When then?"
    $ stat_sanity -= 5
    "The slow anticipation of the agony I knew was coming threatened to push me into insanity."
    "Warmth spread over a small area of my spine."
    "It felt kind of nice, until-"
    $ stat_health -= 1
    $ stat_sanity -= 5
    play sound "<from 12.5>music/sfx_bbq.ogg"
    "I shrieked in agony." with vpunch
    "A searing hot point was pressed to my back."
    "I tried to wrench my body away from it, straining against the shackles." with hpunchtiny
    fox "Stay {i}still{/i} darling."
    "He hissed into my ear."
    "I could hardly hear him over my own screaming."
    $ stat_health -= 1
    $ stat_sanity -= 5
    play sound "<from 12>music/sfx_bbq.ogg" volume 0.3
    "He dragged the point over my skin." with vpunchtiny
    "Burning, sizzling."
    "I could... smell my skin..."
    "I twisted in my bonds and wretched from the awful smell of my own flesh cooking."
    fox "Relax..."
    "I couldn't think. I needed to escape the pain."
    "The burning!"
    "The horrific instrument was lifted from my skin, only to be brought down again-"
    "Directly over my spine."
    $ stat_health -= 1
    $ stat_sanity -= 5
    play sound "music/sfx_chain_short.ogg"
    "I screamed as my body slammed against the restraints." with vpunch
    "My shoulder! Something..."
    "I couldn't concentrate."
    "Tears flowed freely down one side of my face from my undamaged eye."
    "I couldn't stop screaming."
    "He kept dragging the searing point through my skin."
    "For what felt like an eternity."
    "Until he finally lifted it, pausing."
    "The pain washed over me in residual tidal waves."
    "I felt like I was drowning in it."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "Dizzy..."
    show fox comp lookback with dissolve
    "I heard his footsteps..."
    show camera1 tripod with dissolve
    show fox comp lookback:
        xalign 0.5
        xoffset 0
        alpha 1.0
        easeout 0.5 xoffset 50 alpha 0.0
    pause 0.25
    hide fox
    "He took the camera somewhere behind me."
    fox "Well?"
    fox "Pretty cute, right~?"
    "I blinked and tried to see the screen."
    "The feed of my own mutilated back..."
    "The shape..."
    if meme_mode:
        "It's an 'S'."
        "It's... really cool."
    elif True:
        "A [show_design]."
    show fox comp:
        xalign 0.5
        xoffset -50
        alpha 0.0
        easeout 0.25 xoffset 0 alpha 1.0
    pause 0.5
    show camera1 with dissolve
    "I heard him laugh. It sounded hollow and far away."
    show fox comp cocked
    fox "[pp_pos_c] arm?"
    show fox comp lookback
    fox "Really?"
    show fox ultraclose with dissolve
    "Suddenly he was holding my face again."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    fox "Wake up, sweetie!"
    fox ultraclose cocked "Does your shoulder hurt?"
    "I groaned, slowly absorbing his words."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "My shoulder...?"
    $ stat_health -= 1
    "I tried to move it and cried out again."
    "What..?"
    fox ultraclose -cocked "Ahh, you dislocated it."
    fox ultraclose cocked "I {i}told{/i} you not to squirm so much! Didn't I~?"
    hide fox with dissolve
    play sound "<from 0 to 0.45>music/sfx_chain_retracted.ogg"
    "I heard a metallic click."
    play sound "<from 0 to 1.5>music/sfx_chain_long.ogg"
    "I screamed as my wrists and the heavy metal cuffs attached to them suddenly fell down." with vpunch
    show darkroom:
        easein_bounce 0.25 yalign 0.7
    show camera1:
        easein_bounce 0.25 yalign 0.0
    "I crumpled forward into a sobbing heap."
    fox "You want me to push it back in?"
    menu:
        " "
        "\"Don't touch me!\"" if True:
            $ chat_love += 2
            $ fox_love -= 1
            "He scoffed dryly."
            fox angry "Maybe I shouldn't."
            fox -angry "But I suppose you aren't thinking straight..."
            fox "Pets don't always know what's best~"
            fox happy "That's what owners are for."
        "\"Yes...\"" if True:
            $ fox_love += 1
            fox "{i}That's a good pet...{/i}"
            fox happy "I'll make you feel better~"
        "Refuse to speak" if True:
            $ show_silence += 1
            fox "Hmm..."
            fox "I'll take that as a yes."
    "He bent down and grabbed my wrists out from under me."
    show darkroom:
        easein_bounce 0.25 yalign 0.8
    show camera1:
        easein_bounce 0.25 yalign -0.5
    play sound "music/sfx_chain_short.ogg"
    "The motion sent another dizzying wave of pain from my shoulder."
    play sound "<from 0 to 0.45>music/sfx_chain_retracted.ogg"
    "I saw him opening the shackles with a key."
    "I briefly considered using the opportunity to escape-"
    menu:
        " "
        "Try to escape" if True:
            $ fox_love -= 2
            $ chat_love += 2
            "This might be the only chance I'll ever get!"
            play sound "music/sfx_impact_thud.ogg" volume 0.5
            "I shoved him away from me with my good arm and tried to stand." with hpunch
            fox angry "Ugh!"
            show darkroom:
                easeout 0.25 yalign 0.7
                easein_bounce 0.5 yalign 1.0
            show camera1:
                easeout 0.25 yalign -0.2
                easein_bounce 0.5 yalign -1.0
            play sound "music/sfx_chain_short.ogg"
            "I fell forward."
            "My legs were weak and still shackled to the floor."
            "No!!!"
            fox "Heh..."
            fox happy "Hahaha!"
            $ stat_health -= 5
            play sound "<from 0.0 to 1.0>music/sfx_impact.ogg"
            "I cried out as his boot slammed down on my ravaged back." with vpunchhard
            fox angry "That was stupid."
            fox "Brave, maybe. But {i}stupid{/i}."
            $ stat_health -= 1
            "The heel ground down." with vpunch
            "He scoffed lightheartedly."
            fox -angry "Chat thought it was pretty cute, though."
            "I groaned in pain as his boot left my back."
            play sound "music/sfx_impact_thud.ogg" volume 0.25
            "I felt his knee replace it." with vpunchtiny
            "Then he grabbed the wrist of my injured arm."
            p "Wait! Waitwaitwai-"
            play sound "music/sfx_bone_crunch.ogg"
            "I shrieked as he yanked my arm outwards." with hpunchhard
            $ stat_health += 1
            $ stat_sanity += 10
            "But I felt the bone sink back into its socket."
            "The pain died down immediately and significantly."
            "Tears of relief rolled down my cheek and onto the floor."
            show darkroom:
                easein_bounce 0.25 yalign 0.5
            show camera1:
                easein_bounce 0.25 yalign 1.0
            play sound "music/sfx_chain_short.ogg"
            "He pushed me back into a seated position and clamped the cuffs back over my wrists."
            play sound "<from 0 to 0.45>music/sfx_chain_retracted.ogg"
            "I hissed in pain as he raised my arms and clipped them back onto the chain." with vpunchtiny
            fox eyeswide "Be careful now~"
            "His voice dropped to a dangerous growl."
            fox -eyeswide "That shoulder is still {i}delicate{/i}."
        "Stay still" if True:
            "No."
            "I'm too weak and my feet are still attached to the floor."
            "And something was telling me that it was important to stay on his good side."
            "He grasped the wrist of my injured arm."
            if fox_love >= 4:
                fox -happy "Take a deep breath, and make sure your tongue isn't between your teeth."
                fox "This is going to hurt for a moment, but then it will feel a lot better."
                fox "Are you ready?"
                "I nodded weakly."
            elif True:
                fox happy "Here we go!"
            play sound "music/sfx_bone_crunch.ogg"
            "I screamed as he pulled my arm out to the side." with hpunchhard
            $ stat_health += 1
            $ stat_sanity += 10
            "But I felt the bone sink back into its socket."
            "The pain died down immediately and significantly."
            play sound "<from 0 to 0.45>music/sfx_chain_retracted.ogg"
            "Before I could appreciate the relief, he was closing the shackles around my wrists."
            show darkroom:
                easein_bounce 0.25 yalign 0.5
            show camera1:
                easein_bounce 0.25 yalign 1.0
            play sound "music/sfx_chain_short.ogg"
            "I hissed in pain as he raised my arms and clipped them back onto the chain."
            fox eyeswide "Be careful now~"
            fox -eyeswide "That shoulder is still... {i}delicate{/i}."
            "He leaned in close to me."
            fox "{i}Try to keep your weight off it.{/i}"
    show fox comp with dissolve
    "He casually turned back to the screens."
    show fox oncomputer with dissolve
    "He took a moment to read before chuckling quietly."
    fox comp "Oh, I agree~" with dissolve
    fox "I'll have to watch the footage back myself. I was busy!"
    show fox comp lookback
    "He turned back to me."
    fox "Chat tells me that you looked {i}incredibly cute{/i} while I was working on your back."
    fox "They {i}really{/i} liked it~"
    fox comp lookback laugh "And they're {i}itching{/i} to see more!"
    "I shrank away from him slightly."
    "Not more..."
    show fox lookback laugh:
        easein 0.25 alpha 0.0 xalign 0.45
    stop music fadeout 2.0
    "He swooped gracefully behind me and crouched so that his face was right beside mine."
    hide fox
    "I flinched as he pressed against my back, reigniting the pain in my burns."
    stop music fadeout 3.0
    "He spoke clearly to the cameras."
    play music "music/ambient_fox_extra_02.ogg" fadein 1.0
    fox eyeswide "Are you ready for more, Chat~?"
    "I jolted as I felt his hands slide over my thighs."
    "I couldn't stop a whimper as his claws dug in to the soft flesh on the inside."
    "He dug the claws in and pulled, forcing my legs apart." with hpunchtiny
    "The camera... they're..."
    "Despite everything, I could feel shame heating my face again."
    "I lowered my head, trying to escape the sensation."
    fox "Come on now~"
    "I could feel the cold metal of his mask against my cheek."
    fox -eyeswide "Don't be {i}shy{/i}..."
    $ stat_health -= 1
    $ stat_sanity -= 5
    play sound "<from 0 to 1.0>music/sfx_fabric_tear.ogg"
    "I held in a cry as he raked the claws through my skin, tearing the fishnet." with hpunchtiny
    "He dug them in ruthlessly, keeping my legs pried open."
    if show_virgin_question == 1:
        fox eyeswide "You said you were a virgin, didn't you?"
        "I shot up straight at the sudden question."
        "What!?"
        "My mind raced until I remembered the auction."
        fox -eyeswide "I wonder if you told the truth~"
        p "I... I-"
        fox "I bet you did though... {i}didn't you?{/i}"
        "That low growl was under his voice again."
        fox happy "Chat {i}loves{/i} that. I don't even have to check to see."
        fox -happy "It doesn't really matter to me, though."
        "He reached a hand up to my chin and held it up for the camera."
        fox happy "Because we're going to put on a show like they've never seen!"
        "His voice went quiet."
        fox -happy "Aren't we~?"
    elif True:
        fox eyeswide "I bet Chat is getting {i}very{/i} excited."
        fox "I don't even have to check to see."
        "He reached a hand up to my chin and held it up for the camera."
        fox happy "We're going to put on a show like they've never seen!"
        "His voice went quiet."
        fox -happy "Aren't we~?"
    if sexcontent != "no":
        "Any question about what he meant disappeared as he roughly grabbed the front of the underwear I was forced to wear."
        play sound "<from 8 to 9.0>music/sfx_fabric_tear.ogg" volume 0.5
        "I yelled as he pulled back, his claws easily tearing the fabric away and grazing my sensitive flesh." with hpunchtiny
        "I gasped and automatically tried to close my legs-"
        "But his iron grip returned and he held them open, claws digging in again." with hpunch
    elif True:
        "I tried to close my legs, but he held them open with an iron clawed grip." with hpunch
    "How is he so strong!?"
    "I cringed, mind racing, trying to forget the cameras."
    "Trying to stop my body from shaking."
    fox eyeswide "Take a good look, Chat!"
    fox -eyeswide "This might get a bit... Intense~"
    "I breathed a sigh of relief as his hands relinquished my thighs."
    "I clamped them back together as he stood up and walked away."
    play sound "music/sfx_chain.ogg" volume 0.4
    "I could hear the shuffling of objects... chains..."
    "I somehow felt more exposed in front of the cameras without him there."
    "He returned, holding things I couldn't make out- and dragging a large wedge."
    show wedge:
        alpha 0.0
        yalign 1.0
        xalign -0.5
        linear 0.25 alpha 1.0
        easein_bounce 1.0 xalign 0.5
    play sound "<from 6 to 7>music/sfx_floor_scrape.ogg"
    "He pushed the wedge in front of me."
    "Something clicked on the floor, holding the wedge in place."
    show fox comp gag behind wedge with dissolve
    "Then he returned to his position in front of the screens and held up some kind of belt."
    "No, it was..."
    "A gag."
    if sexcontent != "no":
        show fox comp toys
        "Then he waggled something else in front of the camera with a light chuckle."
        fox "Isn't it funny?"
        fox "It reminds me of hentai~"
        fox comp toys cocked "You like it?"
        fox comp toys -cocked "Hahaha! Oh, no. It's going in [pp_pos] mouth."
        fox "I know, I know you like the screaming."
        fox "But this is all part of the game!"
        fox comp toys cocked "We need to fill up [pp_pos] throat~ {image=icon_heart}"
        p "Wait, what!?"
        fox "Lend me your faith, beloved friends~"
        fox comp toys -cocked "It'll be {i}fun!{/i}"
        "What did he mean!?"
        $ persistent.cgs_fox.add("cg_fox_ultraclose_gag")
        $ renpy.save_persistent()
        show fox ultraclose gag zorder 1 with dissolve
        "He returned, kneeling in front of me and pushing the object through the gag."
        "I could finally see it..."
        "Some sort of... tentacle..."
        "This must be a joke."
        fox "Open wiiide~"
        "I didn't even have a chance to resist or comply."
        show fox ultraclose -gag
        "He jabbed two claws in my mouth-"
        "And that was enough to shove the skinny tip of the silicone tentacle in."
        "My protest was cut off by the rest of the tentacle being swiftly pushed in." with vpunchtiny
    elif True:
        show fox comp toys
        "Then he waggled something else in front of the camera with a light chuckle."
        "I couldn't quite see what it was."
        fox comp toys cocked "You like it?"
        fox comp toys -cocked "Hahaha! Oh, no. It's going in [pp_pos] mouth."
        fox "I know, I know you like the screaming."
        fox "But this is all part of the game!"
        p "Wait, what!?"
        fox "Lend me your faith, beloved friends~"
        fox "It'll be {i}fun!{/i}"
        "What did he mean!?"
        $ persistent.cgs_fox.add("cg_fox_ultraclose_gag")
        $ renpy.save_persistent()
        show fox ultraclose gag zorder 1 with dissolve
        "He returned to me, kneeling in front of me and pushing the object through the gag."
        fox "Open wiiide~"
        "I didn't even have a chance to resist or comply."
        show fox ultraclose -gag
        "He jabbed two claws in my mouth-"
        "And that was enough to shove the object in." with vpunchtiny
        "My protest was cut off as my mouth was filled."
    show fox ultraclose kabedon
    "I couldn't do anything but choke as he fastened the rest of the gag around my head." with vpunchtiny
    "My heaving brought tears to my eyes, but I slowly adjusted."
    "I was shaking, but I could still breathe through my nose."
    fox ultraclose cocked "How's that~?"
    "I could only stare at him, panic surely written all over my face."
    fox ultraclose happy "{i}Good...{/i}"
    fox ultraclose eyeswide "You're all ready for the fun part!"
    hide fox with dissolve
    $ persistent.cgs_fox.add("cg_fox_chokechain")
    $ renpy.save_persistent()
    show fox chokechain:
        xalign 0.5
        yalign 0.0
    with dissolve
    play sound "music/sfx_chain.ogg" volume 0.4
    "He held up the last object."
    "A chain..."
    fox "It's a choke chain~!"
    fox "But I've had this one {i}specially made{/i}..."
    "The prongs were sticking straight out.. and they ended in cruelly sharp points."
    $ stat_health -= 1
    show fox ultraclose kabedon with dissolve
    play sound "music/sfx_chain_short.ogg" volume 0.4
    "I tried to jerk away as he lowered the chain around my neck."
    "My attempt was cut short by the metal needles."
    fox ultraclose happy "That's right~ {i}You should be careful.{/i} {image=icon_heart}"
    "The gag and its attachment kept my neck stiff."
    show fox ultraclose happy:
        easein 0.25 alpha 0.0 xalign 0.45
    "I finally understood it. Even breathing and swallowing became a dangerous ordeal."
    hide fox
    "I'll be okay... if I just stay... perfectly still."
    play sound "<from 0 to 0.45>music/sfx_chain_retracted.ogg"
    "The click of my wrist cuffs being unhooked startled me out of my thoughts." with vpunchtiny
    $ stat_health -= 1
    "My hands fell in front of me, causing another grazing by the needles." with vpunchtiny
    "I could only shiver in reply; making sound was impossible."
    play sound "music/sfx_chain_short.ogg" volume 0.4
    "I heard the clink of the chain behind me."
    "I tried to move with it to avoid any more damage."
    play sound "<from 0 to 0.2>music/sfx_chain_retracted.ogg"
    "Another click..." with vpunchtiny
    fox happy "There~!"
    "The steady position of the collar told me he'd hooked it to the same chain my cuffs used to be attached to."
    "I was paralyzed in my position."
    "The fear of the needles kept me still."
    "Then I felt his fingers on my back."
    "Even the feather-light touch sent shockwaves of pain through my destroyed skin."
    "He began to press."
    show darkroom:
        easein_bounce 2.0 yalign 0.6
    show camera1:
        easein_bounce 2.0 yalign 0.7
    show wedge:
        easein_bounce 2.0 yalign 1.3 zoom 1.3
    play sound "music/sfx_chain_short.ogg" volume 0.4
    "I was forced to lean over the wedge."
    $ sanity -= 5
    "Panic shot through me as I tried to steady myself with my hands on the wedge."
    "He kept pushing my back." with vpunchtiny
    "I was trapped between the pain of my skin and the threat of the choke chain."
    "And the awkward balance over the wedge..."
    show darkroom:
        easein_bounce 0.25 yalign 0.65
    show camera1:
        easein_bounce 0.25 yalign 0.65
    show wedge:
        easein_bounce 0.25 yalign 1.35 zoom 1.35
    play sound "music/sfx_chain_short.ogg" volume 0.4
    "I leaned awkwardly forward, trying to steady myself."
    "My legs were already shaking."
    $ stat_health -= 1
    "The barbs of the chain dug into my throat."
    fox "Ready for the hard part?"
    if sexcontent != "no":
        "I heard the unmistakable pop of a button and shuffling of clothing."
        "He can't be..."
        "I stiffened as I felt his fingers spreading my skin."
        "I couldn't escape. I couldn't even make a single sound of protest."
        "He pushed himself against my entrance." with vpunchtiny
        "He forced himself past the resistance." with vpunchtiny
    elif True:
        "I stiffened as I felt the cold side of a blade petting my back."
        "He can't be serious!"
        $ stat_health -= 1
        "He turned the blade and dragged it through my already mangled skin."
        "I couldn't escape. I couldn't even make a single sound of protest."
    "I couldn't scream."
    "I could hear him breathing harder."
    if sexcontent != "no":
        "He moved his grip to my hips and forced himself deeper." with vpunchtiny
    elif True:
        $ stat_health -= 1
        "He carved another line with the knife."
    $ sanity -= 5
    $ stat_health -= 1
    if sexcontent != "no":
        "I lurched forward automatically, I couldn't stop my body from trying to escape the invasion." with vpunchtiny
    elif True:
        "I lurched forward automatically, I couldn't stop my body from trying to escape the pain." with vpunchtiny
    "The prongs dug into my throat in reply."
    if sexcontent != "no":
        "My body moved on instinct again, this time slamming backward into him." with vpunchtiny
        "The reaction elicited an indulgent groan from him."
        fox horny "That's... perfect..."
        "He dug his claws into my thighs and pushed himself deeper."
    elif True:
        "My body moved on instinct again, arching upwards."
        $ stat_health -= 1
        "Right into his blade."
        "He laughed in response as blood began to flow over my back and down my sides."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "Tears wavered in my vision."
    if sexcontent != "no":
        "Why is it thicker!? The base..."
        "My thoughts were dissolved as the rest of his cock was shoved inside." with vpunchtiny
        "The tearing sensation made my knees buckle."
    elif True:
        "The knife tip hit a particularly bad burn on my spine." with vpunch
        "My knees buckled under me."
    $ sanity -= 5
    $ stat_health -= 1
    play sound "music/sfx_chain_short.ogg" volume 0.4
    "My loss of balance was immediately translated into another tightening of the chain."
    "This is too much... I can't take it..."
    $ stat_health -= 1
    if sexcontent != "no":
        "He pulled back and slammed into me again." with vpunch
    elif True:
        "He ruthlessly slashed another deep cut into my flesh." with vpunch
    "I was trembling."
    "Tears were freely falling now."
    "I stared at the camera in front of me."
    "I knew how I must look."
    "How broken..."
    if sexcontent != "no":
        fox horny "You're so {i}tight{/i}..."
    elif True:
        "His free hand found it way to my hip, digging his claws in."
        fox happy "You're so {i}cute{/i} right now..."
    $ stat_health -= 1
    "His claws sunk deeper to punctuate his words."
    if sexcontent != "no":
        "He started to fuck me with an even rhythm." with vpunchtiny
    "My feet were slipping..."
    "The collar..."
    "I was faced with an awful decision."
    menu:
        " "
        "Lean forward into the choke chain" if True:
            show darkroom:
                easein_bounce 0.25 yalign 0.655
            show camera1:
                easein_bounce 0.25 yalign 0.7 zoom 1.05
            show wedge:
                easein_bounce 0.25 yalign 1.4 zoom 1.4
            $ fox_love -= 1
            $ stat_health -= 1
            $ chat_love += 1
            play sound "music/sfx_chain.ogg" volume 0.4
            "My feet faltered and my grip on the wedge slipped."
            "I leaned forward, trying to escape him."
            $ stat_health -= 1
            play sound "music/sfx_chain_short.ogg" volume 0.4
            "The chain around my neck tightened."
            "I heard a low growl from behind me and knew he had noticed."
            if sexcontent != "no":
                "His claws left my hips, and for a moment I felt some relief-"
                "Until I felt his hands on my back."
                $ stat_health -= 2
                "He pressed me down as he kept thrusting into me." with vpunch
            elif True:
                "His claws left my hip, and for a moment I felt some relief-"
                "Until I felt his hand on my back."
                $ stat_health -= 2
                "He pressed me down as he slashed my back." with vpunch
            "The chain... the needles..."
            "I felt the warm trickle of blood running down my neck and over my chest."
            $ stat_health -= 1
            if sexcontent != "no":
                "The spines sank deeper with every thrust." with vpunchtiny
            elif True:
                "The spines sank deeper with every movement." with vpunchtiny
            "Tighter..."
            pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


            "I couldn't breathe any more."
            "He kept pressing..."
            if sexcontent != "no":
                "I could hear him panting... flesh slapping... and the steady drip of blood on the floor." with vpunchtiny
            elif True:
                "I could hear him panting... and the steady drip of blood on the floor."
            if fox_love <= 0:
                jump showDLC_chokedeath
            "He seemed to hesitate for a moment."
            "He relinquished the pressure on my back and I took in a painful gasp of air."
            if sexcontent != "no":
                "He grabbed my hips and returned to his increasingly brutal pace." with vpunchtiny
            elif True:
                $ stat_health -= 1
                "He grabbed me again and returned to carving my skin."
            "I wished he had just let me pass out."
            "My legs couldn't take any more."
            "My hands kept slipping." with vpunchtiny
            "Even without him pushing me down..."
            pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


            "I'm gonna..."
            "My entire body was trembling from the effort."
            "His panting had changed, it sounded like he was stifling himself."
            "The edges of snarls and something else were trying to escape."
            if sexcontent != "no":
                play sound "music/sfx_chain_short.ogg" volume 0.4
                "Suddenly, his claws clamped into my flesh and he slammed my hips onto himself." with vpunch
                "He let out a terrible animalistic moan above me as he came."
                "Even with every muscle in my body on fire, I could feel a pressure inside me growing."
                "The pressure kept growing, inhuman."
                "Why is it so much!?"
                "I shuddered as liquid leaked from our connection and streamed down my leg."
            elif True:
                play sound "<from 0 to 1>music/sfx_knife_drop.ogg" volume 0.4
                "I jolted from surprise as I heard the clang of his knife being tossed to the floor."
                "Both of his hands grasped my shoulders."
                $ stat_health -= 1
                "He raked his claws down my back." with vpunchtiny
                "A blood curdling scream was caught in my throat, trapped by the gag."
                "A fresh gush of tears flowed from my good eye."
            "His breathing finally slowed down."
            play sound "music/sfx_chain.ogg" volume 0.4
            "A click accompanied the chain falling to my back."
            show darkroom:
                easein_bounce 0.25 yalign 0.8
            show camera1:
                easein_bounce 0.25 yalign -0.5
            show wedge:
                easein_bounce 0.25 yalign 2.0
            "With the pressure finally off my neck, I crumpled forward limply."
            if sexcontent != "no":
                "He groaned, seemingly stuck inside me somehow."
                "Then he pushed on my hips, forcing himself out." with vpunch
            "The pain seemed distant now, the oxygen and rest were all that mattered to me."
            if sexcontent != "no":
                "I knew I was a wet, disgusting mess."
            elif True:
                "I knew I was a shredded, bloody mess."
            "But I could breathe."
            "I could hold the chain away from my neck."
            if sexcontent != "no":
                "I ignored the sounds of him fastening clothing, talking breathlessly to his 'Chat'."
            elif True:
                "I ignored the sounds of him talking breathlessly to his 'Chat'."
            show darkroom:
                easein_bounce 0.25 yalign 1.0
            show camera1:
                easein_bounce 0.25 yalign -1.0
            hide wedge with dissolve
            play sound "<from 6 to 7>music/sfx_floor_scrape.ogg"
            "The wedge was pushed away."
            "The horrible chain finally lifted away from me."
            "And finally, the gag on my head unfastened and pulled out of my throat." with vpunchtiny
            pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


            "He was talking. Joking or something. Performing."
            "I couldn't seem to make out the words."
            show darkroom:
                easein_bounce 0.5 yalign 0.5
            show camera1:
                easein_bounce 0.5 yalign 1.0
            play sound "music/sfx_chain_short.ogg"
            "My wrists were pulled up to their original position and attached to the chain above."
            "I hung from them listlessly."
            jump showDLC_eyeremoval
        "Lean backward into him" if True:
            show darkroom:
                easein_bounce 0.25 yalign 0.64
            show camera1:
                easein_bounce 0.25 yalign 0.64
            show wedge:
                easein_bounce 0.25 yalign 1.3 zoom 1.3
            $ fox_love += 3
            play sound "music/sfx_chain_short.ogg" volume 0.4
            "I locked my knees against the wedge and I pushed backward."
            if sexcontent != "no":
                "I sank onto him, forcing myself to take more of his cock."
                "The chain around my neck loosened in response."
                "His shuddering moan told me that he noticed as well."
                "His grip lightened up slightly."
            elif True:
                "I arched my back and held myself up to him."
                "The chain around my neck loosened in response."
                "He clicked his tongue appreciatively and moved the knife over me extremely lightly."
            "I understood the unspoken exchange."
            "This is better than the collar. I can play along..."
            if sexcontent != "no":
                "I moved back against him, trying to match his pace." with vpunchtiny
                fox "Ah~ {i}Fuck...{/i}"
            "The claws still dug in, but it wasn't so bad."
            "My legs were still weakening from the awkward position."
            "I was shaking."
            if sexcontent != "no":
                "But I kept moving." with vpunchtiny
                "I started breathing harder from the effort."
                "Feeling him inside me..."
                "Slamming into me, into my sensitive core..." with vpunchtiny
                "It was just the effort, right?"
                "I was panting as much as the gag would allow."
                "I started to forget the pain all over my body."
                "The threat of the needles around my neck remained, but as long I pushed back..."
                "I pushed back harder." with vpunchtiny
                "I just... need to get away from the collar."
                pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


                "It feels so good..."
                "His grip was getting tighter."
                "I didn't care about the claws any more."
                "I was shaking."
                "My eyelids fluttered."
                "Just keep going!" with vpunchtiny
                "I need it! I need more!"
                $ stat_sanity -= 5
                play sound "music/sfx_chain.ogg" volume 0.4
                "A wave of ecstasy shook me."
                "I slammed myself backward into him." with vpunch
                "I wanted to scream but I couldn't."
                "His panting had changed, it sounded like he was stifling himself."
                $ stat_sanity -= 5
                "Another wave shook me and I ignored everything else." with vpunchtiny
                "All that mattered was the feeling."
                play sound "music/sfx_chain_short.ogg" volume 0.4
                "Suddenly, his claws clamped into my flesh and he slammed my hips onto himself." with vpunch
                "He let out a terrible animalistic moan above me as he came."
                "I welcomed it."
                "I could feel a pressure inside me growing."
                "The pressure kept growing, inhuman."
                "Warm liquid leaked from our connection and streamed down my leg."
                "Our breathing finally slowed down."
                "My senses started coming back through the fog of endorphins."
            elif True:
                $ stat_health -= 1
                "The knife danced over my throbbing skin."
                "He was humming with delight."
                "It hurt like hell, but the effort of leaning over the wedge distracted me from it."
                "I could feel the rivulets of blood trickling down my sides and hips now."
                "I trembled, but I obediently stayed in position."
                "He paused, and I wondered if he was admiring his handiwork."
                play sound "<from 0 to 1>music/sfx_knife_drop.ogg" volume 0.4
                "The clang of his knife being thrown lazily to the side startled me."
                fox happy "It's perfect! {image=icon_heart}"
            play sound "music/sfx_chain.ogg" volume 0.4
            "A click accompanied the remainder of the chain falling to the nape of my neck."
            if sexcontent != "no":
                "My body was completely spent in every way."
                "He groaned, seemingly stuck inside me somehow."
                "Then he pushed on my hips, forcing himself out." with vpunch
            elif True:
                "My body was completely spent."
            show darkroom:
                easein_bounce 0.25 yalign 0.8
            show camera1:
                easein_bounce 0.25 yalign -0.5
            show wedge:
                easein_bounce 0.25 yalign 2.0
            "The pain seemed distant now; my limp body slipped down."
            if sexcontent != "no":
                "I ignored the sounds of him fastening clothing, talking breathlessly to his 'Chat'."
            elif True:
                "I ignored the sounds of him talking spiritedly to his 'Chat'."
            show darkroom:
                easein_bounce 0.25 yalign 1.0
            show camera1:
                easein_bounce 0.25 yalign -1.0
            hide wedge with dissolve
            play sound "<from 6 to 7>music/sfx_floor_scrape.ogg"
            "The wedge was pushed away."
            play sound "music/sfx_chain_short.ogg"
            "The chain finally lifted away from my neck."
            "And finally, the gag on my head unfastened and pulled out of my throat." with vpunchtiny
            "I gasped in relief."
            pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


            "I shook my head and started to notice what I was hearing."
            fox happy "-obedient little pet!"
            if sexcontent != "no":
                fox horny "Oh, I felt it. [pp_sub_c] {i}definitely{/i} came."
                "He laughed lightly, still a little out of breath."
            elif True:
                if pronoun == "they":
                    fox happy "Did you see how hard [pp_sub] were trying!?"
                elif True:
                    fox happy "Did you see how hard [pp_sub] was trying!?"
                "He laughed delightedly."
            fox eyeswide "I can't {i}believe{/i} I almost auctioned [pp_obj]!"
            show darkroom:
                easein_bounce 0.5 yalign 0.5
            show camera1:
                easein_bounce 0.5 yalign 1.0
            play sound "music/sfx_chain_short.ogg"
            "My wrists were pulled up to their original position and attached to the chain above."
            "I hung from them limply."
            jump showDLC_eyeremoval
label showDLC_chokedeath:
    "I tried desperately to push back."
    "Instinctual panic screamed at my muscles to move."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "{i}Anything{/i} to get some air."
    $ stat_health -= 10
    "The spines of the collar were fully buried in my neck." with vpunchtiny
    "No matter how much I tried to my body, I couldn't."
    "I could feel my legs slipping."
    "The weight of my body was enough to choke me now."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    if sexcontent != "no":
        "Even the sensation of him fucking me started to dull." with vpunchtiny
    elif True:
        "Even the sensation of him cutting me started to dull." with vpunchtiny
    "Everything kept getting heavier. Weaker."
    show black:
        alpha 0.0
        linear 5.0 alpha 1.0
    "My vision was fading."
    if sexcontent != "no":
        "I could still hear him, using my body." with vpunchtiny
    elif True:
        "I could still hear him, breathing."
    "But eventually, even that faded away."
    scene black with dissolve
    hide screen status
    if meme_mode:
        fox "Oh... Damn."
        fox happy "Can we get some Fs in chat?"
    $ quick_menu = False
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","Your performance has come to an end - Show 2")
    $ renpy.pause(hard=True)
label showDLC_eyeremoval:
    if fox_love >= 3:
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        show fox close touch with dissolve
        "I felt his hand cup my face."
        fox "Hanging in there?"
        fox close touch happy "I'm a little bit surprised you survived that~!"
        fox close touch -happy "But you did well..."
        "His hand caressed me softly."
        fox close touch horny "You did {i}really{/i} well."
    elif True:
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        show fox close touch with dissolve
        "I felt his hand pat my face."
        fox "Still in there?"
        fox "I'm a little suprised you're alive!"
        show fox close touch happy
        "He let out a bark-laugh."
    show fox comp with dissolve
    "He left my side and went back to his screens."
    "He seemed to be reading."
    fox "Mmm. Mmhmm."
    fox comp lookback "They tell me your eye looks {i}terrible{/i}."
    if meme_mode:
        show fox oncomputer with dissolve
        fox "They said: \"It looks like the inside of a pizza pop.\""
        fox "\"It looks like a Cronenberg movie.\""
        fox "\"-Like someone put an essential oil bath bomb in the microwave.\""
        fox "\"Like a prolapsed-\" oh, gross."
        fox "I'm not saying that one."
        show fox comp lookback with dissolve
        fox comp lookback laugh "Anyway, I'm afraid they're right."
    elif True:
        fox comp lookback laugh "And I'm afraid they're right."
    show fox lookback -laugh
    show darkroom:
        easein 0.25 xalign 0.2
    show camera1:
        easein 0.25 xalign 1.8
    show camera2:
        yalign 1.0
        xalign -0.5
        easein 0.25 xalign 0.4
    show fox lookback:
        easein 0.25 xoffset 800
    "I turned my head away automatically."
    "I didn't know why I felt ashamed of it."
    show darkroom:
        easein 0.5 xalign 0.5
    show camera1:
        easein 0.5 xalign 0.8
    show fox lookback:
        easein 0.5 xoffset 0
    show camera2:
        easein 0.5 xalign -0.5
    fox "I think it might... cause problems, if we leave it like that."
    hide camera2
    fox "I think it's going to have to..."
    show fox close touch with dissolve
    fox "{i}Come out.{/i}"
    menu:
        " "
        "\"Please don't!!!\"" if True:
            $ chat_love -= 1
            "I tried to jerk away from him." with hpunchtiny
            show fox close touch eyeswide
            p "Please! PLEASE!"
            p "No more, I can't take any more!"
            "I knew how pathetic I must look, but I didn't care."
            "The thought of him messing with my eye was too much."
            show fox close touch happy
            "He only laughed in response."
            fox "I know, I know."
            fox close touch cocked "But there's no way around it~"
        "\"Just do whatever you're going to do!\"" if True:
            $ chat_love += 2
            p "You and I both know you're just going to do whatever you want!"
            show fox close touch eyeswide
            p "So stop FUCKING with me and just get it OVER with!!!"
            fox close touch -eyeswide "{i}My, my!{/i}"
            fox close touch cocked "Where did all this energy come from~?"
            "He pinched my cheek condescendingly."
            fox close touch eyeswide "I'm glad you've mustered your resolve!"
            fox close touch -eyeswide "You're going to need it."
        "\"Yes... Please take it out...\"" if True:
            $ chat_love += 1
            $ fox_love += 2
            fox close touch cocked "Oh?"
            p "It hurts..."
            p "I-I know it's fucked up."
            "My voice cracked."
            p "Please fix it... Please make it better..."
            "I started to cry."
            "I knew how pathetic I must look, but I didn't care any more."
            show fox ultraclose with dissolve
            "He cupped my face in both hands."
            fox ultraclose happy "Of {i}course{/i} I will, sweetie."
            fox "I'll do everything I can to make it all better."
            show black with dissolve
            "He touched his mask to my forehead in a gesture like a kiss."
            hide black with dissolve
            $ stat_sanity -= 10
            "It somehow made me feel better."
            show fox close touch cocked with dissolve
            "Something in the back of my head told me it shouldn't..."
            "But I ignored it."
        "Ignore him" if True:
            $ chat_love -= 1
            $ fox_love -= 1
            $ show_silence += 1
            if show_silence >= 4:
                fox "..."
                fox "Quiet as ever, hm?"
            fox "Well."
            fox close touch cocked "You must be tired~"
            fox close touch -cocked "Hang in there, just a bit longer."
    fox "I just need to get some supplies."
    hide fox with dissolve
    "He walked away for a moment and started digging through drawers somewhere in the darkness."
    "I vaguely wondered how he could even see anything in here."
    "He seemed to be taking longer than usual, though."
    "I started feeling more aware of the cameras aimed at me."
    menu:
        " "
        "Look down" if True:
            show darkroom:
                easeout 0.5 yalign 0.7
            show camera1:
                easeout 0.5 yalign 0.0
            "I didn't want to think about those people."
            "Paying to see this..."
            show darkroom:
                easein 0.5 yalign 0.5
            show camera1:
                easein 0.5 yalign 1.0
        "\"I hope karma comes for you fuckers.\"" if True:
            $ chat_love -= 1
            "I glowered at the camera."
            fox happy "You shouldn't antagonize our patrons, darling."
            "I huffed and looked away."
        "Smile" if True:
            $ chat_love += 2
            "I don't know what possessed me to do it but..."
            "I lifted my gaze and shakily attempted a smile."
            "Maybe if I appeal to them..."
            "It's not like there's much of anything else I can do."
    play sound "music/sfx_metal_wheeling.ogg"
    pause 0.5
    show tray:
        yalign 1.3
        xalign -0.1
    with dissolve
    "He finally came back, wheeling a small tray."
    $ persistent.cgs_fox.add("cg_fox_ultraclose_speculum")
    $ renpy.save_persistent()
    show fox ultraclose speculum:
        xalign 0.0
    with dissolve
    "Then he knelt down in front of me and held up a thin metal instrument."
    fox "This is to hold your eye open so I can work."
    menu:
        " "
        "Nod" if True:
            $ fox_love += 1
            p "I... understand."
            show fox ultraclose grab
            "I shivered as he brought the tool to my eye."
            "I bit my lip as he pushed it in, propping my eyelids open painfully." with vpunchtiny
        "Struggle" if True:
            $ chat_love += 1
            "Oh, hell no."
            show fox ultraclose grab
            "He raised it to my face and I twisted away from him." with hpunch
            show fox ultraclose kabedon
            "His other hand grabbed my face with crushing force." with hpunch
            "I winced as his claws dug into my face."
            "He forced my face into position."
            fox ultraclose kabedon angry "Stay. Still."
            show fox ultraclose grab
            "He pushed the instrument into my injured eye, propping my eyelids open painfully."
    show fox ultraclose:
        xalign 0.5
    fox "You might want to..."
    fox "Hm."
    fox "Well you might want to look away with your good eye anyway."
    show fox ultraclose grab
    pause 0.25
    show darkroom:
        easein 0.5 xalign 0.6
    show camera1:
        easein 0.5 xalign 0.7
    show fox ultraclose grab:
        easein 0.5 xalign -0.5
    "As soon as he raised a scalpel, I obediently tried to look away."
    p "I can't..."
    p "I can't do this!"
    fox "Shhhh."
    fox "All you have to do is stay {i}still{/i}."
    if fox_love >= 3:
        show fox close whisper with dissolve
        "He suddenly pressed his face right up beside mine and spoke in a whisper no microphone could pick up."
        fox "I'm only cutting out the bad part, for the audience~"
        fox "If you {i}behave{/i}, I'll have an expert look at it later."
    show fox ultraclose grab with dissolve:
        xalign -0.5
    "He leaned away and twirled the scalpel deftly for the camera."
    "Or was he demonstrating his dexterity... for me?"
    "The idea evaporated from my mind as he raised the scalpel into position."
    $ stat_health -= 1
    $ stat_sanity -= 5
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    play sound "music/sfx_knife_stab.ogg"
    "I bit down on a scream as the blade penetrated the ruined flesh in my eye socket." with vpunchtiny
    $ stat_health -= 1
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    play sound "music/sfx_gore_2.ogg" volume 0.5
    "I could {i}feel{/i} him carving..." with vpunchtiny
    "My entire body was shaking violently."
    play sound "<from 0.3 to 1.0>music/sfx_knife_stab_repeated.ogg"
    "The sound of delicate metal instruments grazing each other punctuated my whimpers."
    $ stat_health -= 1
    "I tried to fight through the pain, to stay still."
    show fox ultraclose kabedon
    pause 0.1
    show darkroom:
        easein_bounce 0.25 xalign 0.5
    show camera1:
        easein_bounce 0.25 xalign 0.8
    $ renpy.music.set_volume(0.1,5,channel="music")
    "I actually welcomed the vicelike grip of his hand steadying my head."
    show fox ultraclose kabedon
    "He was moving quickly."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    show fox ultraclose:
        xalign 0.5
    "So quickly, he was becoming a blur."
    show fox ultraclose grab:
        xalign 0.0
    "The throbbing pain started to subside."
    "That's better..."
    fox "...ssing out?"
    p "... Huh..?"
    show fox oncomputer:
        xalign 0.5
    hide tray
    with dissolve
    "What's happening?"
    fox "... ll want me to..?"
    if sexcontent != "no":
        fox comp "... ould go again... but..." with dissolve
    fox comp "... will kill [pp_obj]..." with dissolve
    if chat_love >= 12:
        fox comp "Yes... I think so too..."
        fox comp presenting "... for another show! {image=icon_heart}"
        fox comp -presenting "... at's what I thought."
        show fox ultraclose happy with dissolve
        fox "Let's get you stitched up~!"
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

        stop music fadeout 1.0
        pause 0.5
        scene black with eyedissolve
        pause 2.0
        $ renpy.music.set_volume(1,channel="music")
        play music "music/ambient_fox_08.ogg" fadein 1.0
        "..."
        if achievement.has("ach_show_2") != True:
            $ persistent.ach_show_2 = True
            $ achievement.grant("ach_show_2")
            init:
                $ achievement.register("ach_show_2")
                $ achievement.sync()
                $ renpy.save_persistent()
                if persistent.ach_show_2 == True and achievement.has("ach_show_2") != True:
                    $ achievement.grant("ach_show_2")
                    $ achievement.register("ach_show_2")
                    $ achievement.sync()
        "Is it over?"
        jump show_DLC_intermission_2
    elif True:
        if fox_love >= 10:
            fox comp cocked "... eally?"
            fox comp lookback "... iked this one..."
            "Why does he sound so sad?"
            fox ultraclose "Take a good look, then~" with dissolve
            show fox ultraclose grab:
                xalign 0.0
            fox "Let's bring this show to an end."
        elif True:
            fox comp cocked "... eally?"
            "I heard him laugh, far away, distorted."
            show fox ultraclose grab:
                xalign 0.0
            fox "... ll right, then. Let's do it." with dissolve
    p "What..?"
    "I felt his hand on my face."
    if sexcontent != "no":
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        if sexcontent == "yes":
            show fox cock with dissolve:
                xalign 0.5
        stop music fadeout 3.0
        play ambient "music/ambient_hypnotoad.ogg" volume 0.50 fadein 5.0
        "A shadow obscured my view."
        "What is he doing?"
        show black:
            alpha 0.0
            linear 5.0 alpha 1.0
        $ stat_health -= 30
        "Thick, hot flesh invaded my eye cavity." with vpunch
        "A sharp gasp from above told me everything I needed to know."
        $ stat_health -= 50
        "The pain turned to pressure, and the sound of squelching blood turned to static." with vpunchtiny
        $ stat_health -= 100
        "And the pressure dissolved into nothing."
        stop ambient fadeout 1.0
    elif True:
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        stop music fadeout 3.0
        play ambient "music/ambient_hypnotoad.ogg" volume 0.50 fadein 5.0
        "Something bigger than the scalpel..."
        "What is he doing?"
        show black:
            alpha 0.0
            linear 5.0 alpha 1.0
        $ stat_health -= 30
        "He pushed a sharp point into my eye cavity." with vpunch
        $ stat_health -= 50
        "The pain turned to pressure." with vpunchtiny
        $ stat_health -= 100
        "And the pressure dissolved into nothing."
        stop ambient fadeout 1.0
    if achievement.has("ach_show_2") != True:
        $ persistent.ach_show_2 = True
        $ achievement.grant("ach_show_2")
        init:
            $ achievement.register("ach_show_2")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_show_2 == True and achievement.has("ach_show_2") != True:
                $ achievement.grant("ach_show_2")
                $ achievement.register("ach_show_2")
                $ achievement.sync()
    scene black with dissolve
    hide screen status
    hide screen effect_health
    $ quick_menu = False
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","Your performance has come to an end - Show 2")
    $ renpy.pause(hard=True)
label show_DLC_intermission_2:
    "I felt as though I drifted in and out of sleep for days."
    "But I couldn't tell."
    "I kept dreaming about pain... and teeth."
    if fox_love < 10:
        "Sometimes I would wake up."
        "And I would remember the room... the dark room."
        "Sometimes there was food."
        "But it was all so foggy and far away."
        "As if I couldn't {i}really{/i} wake up."
    elif True:
        "I felt a shift, something pulling my awareness from the deep murk again."
        "Something petting my head."
        fox empty "Did I wake you?"
        $ persistent.cgs_fox.add("cg_fox_light_sitting")
        $ renpy.save_persistent()
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

        scene lightroom:
            xanchor 0.5
            yanchor 0.5
            rotate -15
            xalign 0.5
            yalign 0.4
        show fox light sitting:
            xalign 0.5
            yalign 0.25
        with eyedissolve_reverse
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

        "My body was so heavy."
        fox light sitting smile "There you are."
        fox light sitting -smile "You've been sleeping so long, I was a little worried you'd slipped into a coma."
        "I looked at him, panic rising, but I couldn't seem to speak."
        fox light sitting smile "Shh. Relax."
        fox "No show today."
        "Those words sent a wave of relief through my body."
        fox "I've gotten you all fixed up. {image=icon_heart}"
        fox light sitting -smile "They couldn't save your eye, but it's been prepared for a prosthetic."
        "I barely remembered my eye."
        "I reached up to touch it automatically."
        "And I recoiled with a gasp as I felt nothing there."
        fox light sitting talk "Don't fiddle with it. It needs to heal more."
        show fox light sitting thinking
        "Something... something about what he said..."
        "A prosthetic..?"
        menu:
            " "
            "\"Why would you help me?\"" if True:
                p "Why would you even bother fixing my eye..?"
                p "If you're just going to kill me."
                "My voice came out as a croak."
                "He looked down at me for a moment before answering."
                fox light sitting smile "Your shows have been {i}very{/i} popular."
                fox light sitting smile2 "It seems that my audience adores you. They're begging to see more."
                fox light sitting bored "But..."
                fox "They're fickle, too."
                fox light sitting smile "You may not live to see that prosthetic."
                "He chuckled softly."
                fox "It's better to be prepared. Just in case."
            "\"Why can't I move?\"" if True:
                "My voice came out as a croak."
                fox light sitting smile "You're on painkillers, darling. Drugs."
                p "... Drugs?"
                fox "To keep you sleeping and healing."
                "I fumbled with this new information, trying to make sense of it."
                "It was hard to form a complete thought."
                fox light sitting smile2 "And you're going to stay on them."
                fox light sitting smile "It's {i}better{/i} that way."
                fox "For now."
            "Stay silent" if True:
                "I waited for him to continue speaking."
                fox light sitting bored "You don't need to worry about anything for now."
                fox light sitting smile2 "The crowd {i}loves{/i} you, so I'm having you properly taken care of."
                fox light sitting smile "You might as well enjoy your break, and the painkillers."
                "Painkillers... that must be why everything is so foggy..."
        show lightroom:
            easein 2.0 yalign 0.45
        show fox light sitting smile:
            easein 2.0 yalign 1.0
        "I relaxed slightly and started to look at him more closely."
        if meme_mode:
            "As I focused, I realized that he was wearing a really fucking ugly hoodie."
            "God... God damn..."
        elif True:
            "As I focused, I realized I'd never really seen his skin before."
            "He's covered in..."
        show lightroom:
            easein 0.25 yalign 0.4
        show fox light sitting bored:
            easein 0.25 yalign 0.25
        fox "It's {i}rude{/i} to stare, you know."
        if meme_mode:
            "I hastily tore my gaze away from the offending garment and fidgeted nervously."
        elif True:
            "I hastily tore my gaze away from his scars and fidgeted nervously."
        show fox light sitting smile
        "He let out a quiet, lighthearted chuff."
        fox "It's fine. You're on a lot of drugs."
        fox light sitting bored "Probably won't even remember this anyway."
        menu:
            " "
            "\"Who did that to you?\"" if True:
                $ fox_love += 1
                fox "..."
                show fox light sitting laugh at laugh
                "He laughed, a single dry bark."
                fox light sitting smile2 "A dead man did."
                fox light sitting smile "You know..."
                fox "I used to think he opened my eyes."
                fox "Then I thought he closed them."
                fox "And now..."
                fox light sitting thinking "I realize he didn't do much at all."
                fox "He may have made the scars, but the scars didn't make me."
                fox light sitting smile2 "I did that myself!"
                show fox light sitting laugh at laugh
                "He laughed again, but this time more heartily."
            "\"Were you in shows too?\"" if True:
                $ fox_love += 1
                fox light sitting question "In shows?"
                fox light sitting bored "Ahh, as the star."
                fox light sitting -bored "I suppose you could say that."
                fox "I've seen a bit of Hell, yes."
                fox light sitting smile "Like you."
                "He pushed a bit of hair from my face, a surprisingly gentle gesture."
            "Stay silent" if True:
                fox "..."
                fox "It's nice to have a quiet moment, anyway."
        fox light sitting smile "Ahh. But I guess it's time for me to go."
        fox light sitting bored "There's always business to attend to."
        p "Wait!"
        fox light sitting question "Hm?"
        menu:
            " "
            "\"Are you going to kill me or not?\"" if True:
                show fox light sitting laugh at laugh
                fox "Haha!"
                fox light sitting smile "Well, that's up to Chat, isn't it?"
                menu:
                    " "
                    "\"I thought {i}you{/i} were the one in charge.\"" if True:
                        $ show_rensdecision = 1
                        fox light sitting thinking "..."
                    "\"I guess so...\"" if True:
                        fox "Yes you do."
                        fox "So you'd better conserve your strength."
                        fox light sitting smile2 "And prepare yourself to put on a good show~"
            "\"Never mind...\"" if True:
                pass
        fox light sitting smile "Get some rest."
        hide fox with dissolve
        "Before I knew it, he was gone."
        show lightroom:
            easein 0.25 rotate 0
        pause 0.25
        hide lightroom
        show lightroom:
            yalign 0.4
            xalign 0.5
            easein_bounce 0.5 yalign 0.0
        "And I was alone again in the empty room."
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

        "I tried to think about what happened, but the mist in my mind closed in again."
        scene black with eyedissolve
        stop music fadeout 1.0
        "And I drifted back to sleep."
    pause(2.0)
    play music "music/ambient_fox_08.ogg" fadein 1.0 if_changed
    "Something was shaking me roughly."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    show lightroom:
        xalign 0.5
        yalign 0.5
    show fox light serious
    show goonk behind fox:
        xalign 0.8
        yalign 1.0
    with eyedissolve_reverse
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    "I reluctantly opened my eye and groaned."
    fox light angry "Be {i}gentle{/i} for fuck's sake."
    fox light serious "I didn't pay for all that medical work for you to {i}tear it all up again{/i}."
    goon "Uh, sorry Sir."
    "I tried to make sense of what was happening."
    show lightroom:
        easein_bounce 0.5 yalign 0.45
    show goonk:
        yoffset 0
        easein_bounce 0.5 yoffset 70
    show fox light serious:
        yoffset 0
        easein_bounce 0.5 yoffset 80
    "I was dragged to my feet."
    fox "Come on. Showtime's in five minutes."
    "Showtime... Showtime!?"
    "The gears in my head started slowly turning, and panic started creeping in to my awareness."
    show lightroom:
        easein_expo 1.0 yalign 0.5
    show goonk:
        easein_expo 1.0 yoffset 0
    show fox light serious:
        easein_expo 1.0 yoffset 0
    "I looked down at my body."
    "Sure enough, I was dressed in another lingerie outfit that barely covered anything."
    "This one was nauseatingly girly. Pink, bows, ruffles, everywhere."
    "A top and bottom, along with a skirt and garters- clearly designed with fetishists in mind."
    p "Ughh..."
    stop music fadeout 1.0
    scene black with dissolve
    "My legs weren't working at all, but that didn't stop the goon from dragging me."
    "Eventually we made it to the heavy door."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    scene darkroom bright:
        xalign 0.5
        yalign 0.4
    show camera1:
        xalign 0.80 yalign 1.0 yoffset 100
    with dissolve
    play music "music/ambient_fox_09.ogg" fadein 2.0
    play music2 [ "<sync music>music/ambient_fox_09_beat.ogg", "music/ambient_fox_09_beat.ogg" ] fadein 2.0
    "The dark room."
    show darkroom bright:
        easein_bounce 0.25 yalign 0.5
    show camera1:
        easein_bounce 0.25 yoffset 0
    "I was shoved forward into the abyss, and pushed into my spot on the floor."
    "My head was swimming. My limbs were numb."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    play sound "<from 0 to 0.45>music/sfx_chain_retracted.ogg"
    "I could barely concentrate, let alone fight them as they snapped the familiar shackles on." with vpunchtiny
    play sound "music/sfx_chain_short.ogg"
    "My wrists were raised above and clipped into place on the chain."
    "I remember this. I remember all of this."
    "I should be afraid."
    fox angry "All right. Out. Out!"
    "I blinked slowly."
    "I should..."
    show fox oncomputer with dissolve
    "The screens are so bright..."
    fox comp presenting "Hello again my friends~!"
    fox comp cocked "I'm so happy to see you all again! {image=icon_heart}"
    fox comp -cocked "And I have got {i}quite the treat{/i} for you today!"
    if player_name.upper() == "STRADE":
        fox comp lookback "Our lovely star is back for an encore!"
    elif True:
        fox comp lookback "Our lovely star, [player_name] is back for an encore!"
    fox close touch "And this time, I thought it would be fun..." with dissolve
    "His hand brushed over my chest possessively."
    fox close touch happy "If [pp_sub] had a bit of a {i}cocktail{/i} before the show~"
    hide fox with dissolve
    show fox comp with dissolve
    fox comp "[pp_is_c] on a few painkillers... {i}among other things{/i}."
    fox "So [pp_is] a little 'out of it'."
    fox comp cocked "\"What is this painkiller pussy shit?\""
    fox comp -cocked "Very astute and vulgar question, darling!"
    fox comp lookback "Physical pain can open {i}and close{/i} many doors."
    fox comp -lookback "Don't worry- you don't have to understand."
    fox comp "I'm only too happy to {i}demonstrate{/i}."
    fox comp cocked "Now. I remember a few people asking for some hardware fun the other day."
    fox comp presenting "So why don't we play another game?"
    show fox comp -presenting
    hide fox comp with dissolve
    show darkroom bright:
        easein 3.0 yalign 0.8
    show camera1:
        easein 3.0 yoffset -300
    $ renpy.music.set_volume(0,3, channel="music")
    "As he walked out of view, I felt my head drooping."
    "I feel so heavy..."
    "Why are the screens {i}so{/i} bright?"
    show darkroom:
        easein_bounce 0.25 yalign 0.5
    show camera1:
        easein_bounce 0.25 yoffset 0
    play sound "music/sfx_air_compressor.ogg"
    $ renpy.music.set_volume(1,0.5, channel="music")
    "I jumped at the sound of a motor." with vpunchtiny
    "I imagined a car, or a train."
    show darkroom:
        easein 0.5 xalign 0.3
    show camera1:
        easein 0.5 xalign 1.3
    show camera2:
        xalign -0.5
        yalign 1.0
        easein 0.5 xalign 0.3
    pause 1.0
    show darkroom:
        easein 0.5 xalign 0.7
    show camera1:
        easein 0.5 xalign 0.0
    show camera2:
        easein 0.5 xalign -2.5
    show camera3:
        xalign 1.5
        yalign 1.0
        easein 0.5 xalign 0.7
    pause 1.0
    p "What!?"
    hide camera2
    show darkroom:
        easein 0.5 xalign 0.5
    show camera1:
        easein 0.5 xalign 0.8
    show camera3:
        easein 0.5 xalign 1.5
    pause 0.5
    show fox comp nailgun lookback with dissolve
    hide camera3
    "He returned to me searching frantically for whatever machine was about to mow me down."
    fox comp nailgun "Most of you have seen this before, yes?"
    play sound "music/sfx_nailgun.ogg"
    "A loud bang sent my body jumping as much as the shackles would allow." with vpunchtiny
    "My pounding heart felt like it was going to explode."
    fox "It's a pneumatic nail gun~"
    if meme_mode:
        fox "And yes, I absolutely {i}do{/i} know how to use it."
    hide fox with dissolve
    "He circled around me and pressed a cold metal tip to my shoulder."
    $ persistent.cgs_fox.add("cg_fox_nailgun_look")
    $ renpy.save_persistent()
    show darkroom:
        easein 0.5 xalign 0.3 yalign 0.3
    show camera1:
        easein 0.5 xalign 1.3 yoffset 300
    show camera2:
        xalign -0.5
        yalign 1.0
        easein 0.5 xalign 0.1 yoffset 300
    show fox nailgun look:
        xalign -1.0
        yalign 1.0
        easein 0.5 xalign 0.2 yoffset 200
    fox "Do you know what a {i}pneumatic nail gun{/i} is, sweetie?"
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "I looked up at him. I couldn't seem to focus."
    menu:
        " "
        "\"I don't know.\"" if True:
            $ fox_love += 1
            p "I don't... I don't..."
            fox "No idea, hm?"
        "\"It's a tool for firing nails.\"" if True:
            p "It's a... a..."
            "I knew the answer on some level, but I couldn't seem to get it out."
            fox "It's a {i}what?{/i}"
            p "A... tool..."
            fox "Well, that's close."
            fox "But I'm afraid I can't give you full marks~"
        "\"Don't shoot me!\"" if True:
            $ fox_love += 1
            p "Don't... don't shoot!"
            "He leaned in closer to me."
            fox "You know that's not the answer."
        "???" if meme_mode:
            p "It's like..."
            "I wavered in place, having trouble connecting words."
            p "It's like a parody..."
            "He leaned in closer to hear me."
            fox nailgun cocked "What do you mean?"
            fox "A parody of what?"
            show fox nailgun look
            p "A PAIR O' DEEZ NUTS!"
            fox nailgun "..."
        "Stay silent" if True:
            $ show_silence += 1
            if show_silence >= 5:
                fox nailgun -look "Ahh, I knew you wouldn't answer~"
            elif True:
                fox nailgun -look "No idea, hm?"
    $ stat_health -= 1
    show fox nailgun -look
    show darkroom red
    play sound "music/sfx_nailgun.ogg"
    "Another bang, and a sickening tingling sensation." with vpunch
    show darkroom with dissolve
    "What..?"
    show darkroom:
        easein 0.5 yalign 0.5
    show camera1:
        easein 0.5 yoffset 0
    show camera2:
        easein 0.5 yoffset 0
    show fox nailgun:
        easein 0.5 yoffset 0
    "I tried to see my shoulder."
    "The light from the screens caught a metallic tip, and a tiny bead of blood welling around it."
    p "Is that... a nail?"
    p "Is it..."
    fox nailgun look "That's right~!"
    "I knew it was supposed to hurt."
    "But it felt different..."
    "Without the pain it just felt like something that wasn't supposed to be there."
    "Digging deep in my arm."
    "No..."
    "Squirming under my skin."
    p "Take it out! Take it... get it out!"
    "I couldn't mask the panic in my voice."
    show darkroom:
        easein 0.5 yalign 0.3
    show camera1:
        easein 0.5 yoffset 300
    show camera2:
        easein 0.5 yoffset 300
    show fox nailgun:
        easein 0.5 yoffset 200
    fox "It's time for question two!"
    "He moved the tip of the gun over my arm, closer to my elbow."
    fox nailgun look "What's my name?"
    menu:
        " "
        "\"It's 'Fox'.\"" if True:
            $ fox_love += 1
            p "Fox! It's... you said..."
            fox nailgun cocked "Aww~ You remembered! {image=icon_heart}"
            fox nailgun look "But unfortunately for you, it's not my real name."
            fox "Come on. You had to know that."
        "\"I don't know!\"" if True:
            $ fox_love += 1
            p "I don't know! You... never said..."
            fox "Oh~?"
            fox nailgun cocked "You're pretty clever... even when you're all fucked up~{image=icon_heart}"
            fox nailgun look "But, I'm afraid that's still not a correct answer."
        "\"Please stop!!!\"" if True:
            $ fox_love += 1
            p "Please! don't... don't shoot..."
            fox "Sorry! That's not an answer~!"
        "Don't answer" if True:
            $ show_silence += 1
            if show_silence >= 5:
                "He shrugged theatrically."
                fox "I'm not really sure why I bother!"
            elif True:
                fox "Don't know~?"
    $ stat_health -= 1
    show fox nailgun -look
    show darkroom red
    play sound "music/sfx_nailgun.ogg"
    "He pulled the trigger." with vpunch
    show darkroom with dissolve
    "My arm was shaking."
    "I wanted it to stop, it just made me feel them more."
    "Under my skin... moving under my skin..."
    show fox nailgun look
    p "PLEASE!"
    p "Take them out!"
    show darkroom:
        easein 0.5 xalign 0.5 yalign 0.7
    show camera1:
        easein 0.5 xalign 0.8 yoffset -280
    show camera2:
        easein 0.5 xalign -0.5 yoffset -280
    show fox nailgun look:
        easein 0.5 xalign -1.0 yoffset -200
    "I hate it... I can't..."
    if meme_mode:
        fox "Seems like a skill issue tbh."
    $ stat_health -= 1
    hide fox
    hide camera2
    "He wrapped his hand around my arm and squeezed, forcing rivulets of blood from the nails."
    "I could feel every bit of them, moving, scraping against bone."
    "I couldn't help but scream." with vpunchtiny
    "It sounded awful, like someone else."
    fox happy "How about an easy one?"
    "I made a sound somewhere between a groan and a sob."
    "I couldn't seem to control myself at all."
    fox -happy "Hey, hey."
    show darkroom:
        easein_bounce 0.25 xalign 0.5 yalign 0.5
    show camera1:
        easein_bounce 0.25 xalign 0.8 yoffset 0
    pause 0.25
    show fox ultraclose grab with dissolve
    "He grabbed my head and forced me to look at him."
    fox "Pay attention, okay?"
    fox "Here's your question~"
    fox ultraclose happy "What are the last five letters of the alphabet?" with dissolve
    p "Huh?"
    p "I..."
    fox ultraclose -happy "Oh, that's definitely not one of them."
    hide fox with dissolve
    "He got up and took his position at my side."
    "I couldn't bear to look."
    "He slid the tip of the gun over my other shoulder."
    p "Wait! I wasn't!"
    "I strained to make my brain work."
    p "Z... Y..."
    "I can't concentrate!"
    "The tip of the gun caressed my shoulder."
    "The sensation of the nails moving deep in my arm was making me feel sick."
    "I couldn't think of anything else."
    fox horny "You're too {i}slow{/i}~"
    $ stat_health -= 1
    show darkroom red
    play sound "music/sfx_nailgun_underwater.ogg"
    "I heard the bang and my body convulsed as another nail was lodged in my arm." with vpunch
    show darkroom with dissolve
    p "Oughh..."
    "The nails..."
    show darkroom:
        easein_bounce 3.0 xalign 0.5 yalign 0.7
    show camera1:
        easein_bounce 3.0 xalign 0.8 yoffset -250
    $ renpy.music.set_volume(0,3, channel="music")
    "I sagged in my bonds, twitching reflexively."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    "He was talking again."
    "I heard words but I didn't understand them."
    "Is he asking me another question?"
    $ stat_health -= 1
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    show darkroom red
    play sound "music/sfx_nailgun_underwater.ogg"
    "He fired another nail into me." with vpunch
    show darkroom with dissolve
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    p "Stop... I don't..."
    p "I can't..."
    "He's asking another question. I know he must be."
    "Is he asking them or me?"
    "What's happening right now?"
    "Metal on my thigh."
    "He's going to shoot me again!"
    "I thrashed, trying to get away." with hpunchhard
    $ stat_health -= 1
    show darkroom red
    play sound "music/sfx_nailgun_underwater.ogg"
    "Another nail." with vpunch
    $ stat_health -= 1
    play sound "music/sfx_nailgun_underwater.ogg"
    "And another." with vpunch
    show darkroom with dissolve
    "Is he laughing?"
    "Wait... is that me? Am I laughing?"
    show darkroom:
        easein 0.5 xalign 0.5 yalign 0.5
    show camera1:
        easein 0.5 xalign 0.8 yoffset 0
    pause 0.5
    show fox ultraclose kabedon with dissolve
    "I felt his hands on my face."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    $ renpy.music.set_volume(1,1, channel="music")
    fox "Stay with us now~ {image=icon_heart}"
    fox "Can you hear me?"
    "I panicked at the sound of another question."
    p "Yes! Yes I hear!"
    show fox ultraclose happy at laugh
    "He barked a laugh."
    fox ultraclose -happy "I don't have the nail gun any more."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "I could hardly concentrate on what he was saying."
    "I could only feel the nails, squirming in my muscles. Burrowing inside me."
    "Heating up my blood..."
    p "Take them out... please take them out..."
    fox ultraclose cocked "Why don't {i}you{/i} take them out?"
    "I looked up at him questioningly."
    hide fox with dissolve
    fox "Here, I'll let you use your hands."
    play sound "<from 0 to 0.45>music/sfx_chain_retracted.ogg"
    "I heard the familiar click of the shackles snapping open."
    play sound "music/sfx_chain_short.ogg"
    "My arms fell forward like dead weights." with vpunch
    "The motion aggravated the nails inside them."
    show fox:
        xalign 0.5
        yalign 1.0
        yoffset 225
    with dissolve
    p "Ougghh..."
    fox cocked "Go ahead."
    show fox -cocked
    "I can pull them out. I need to pull them out now."
    "He's watching..."
    show darkroom:
        easein 0.5 yalign 0.7
    show camera1:
        easein 0.5 yoffset -300
    show fox:
        easein 0.5 yoffset -200
    "I tried to lift my arm."
    "It felt like it was made of lead."
    "Trembling, twitching, my hand approached a nail embedded near my elbow."
    "I gingerly pinched the head of the nail in my fingers."
    "Just pull. Just pull it out."
    "I pulled..."
    play sound "music/sfx_gore_1.ogg" volume 0.2
    "The sensation of it slipping out from the meat of my arm made me lurch." with vpunchtiny
    "I could feel it inside me... sliding, parting my flesh..."
    show fox:
        easein 0.25 xalign 0.4 alpha 0.0
    "Rough metal against a soft part of me that should never have been touched."
    hide fox
    "I pulled, blood and nail emerging from inside me, slowly."
    "Agonizingly slowly."
    "Some insane piece of my mind wished I was in pain."
    "Pain is better. Simpler."
    play sound "music/sfx_drop_nail_1.ogg"
    "Finally, the tip of the nail slipped out and I let it fall to the floor."
    "I shuddered with relief and revulsion at the same time." with hpunchtiny
    fox eyeswide "{i}Good{/i}..."
    fox -eyeswide "Now do the rest."
    show darkroom:
        easein 0.25 xalign 0.5 yalign 0.5
    show camera1:
        easein 0.25 xalign 0.8 yoffset 0
    "I looked for him, bewildered."
    "I could feel panic hammering at the inside of my chest."
    "Why!?"
    p "Please... Can't you..."
    fox horny "{i}No{/i}. {image=icon_heart}"
    "I jumped at the sound of his voice behind me."
    "I gulped and tried to steady myself."
    "I can do it. Just do it faster."
    show darkroom:
        easein 0.5 yalign 0.7
    show camera1:
        easein 0.5 yoffset -300
    "I felt along my skin until I found the head of another nail in my shoulder."
    "{i}Fast{/i}."
    "I grasped the nail."
    "Do it! Do it! Do it! Do it!"
    "I tore the nail out of myself in one motion."
    play sound "music/sfx_drop_nail_2.ogg"
    "I crumpled into a sob as it skittered across the floor." with vpunchtiny
    "Hot blood trickled down my arm."
    fox eyeswide "There you go~!"
    "It feels so awful..."
    "But..."
    "My arm did feel better."
    "They're gone."
    "I heaved a few deep breaths."
    "They're just nails."
    "Just nails."
    "I shook my head and went back to work." with hpunchtiny
    play sound "music/sfx_drop_nail_1.ogg" volume 0.5
    queue sound [ "<silence .5>", "music/sfx_drop_nail_2.ogg" ] volume 0.5
    "I began pulling nails out of my skin more quickly."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    "The sick feeling of them sliding around inside me was enough motivation."
    play sound "music/sfx_drop_nail_2.ogg" volume 0.2
    queue sound "music/sfx_drop_nail_1.ogg" volume 0.2
    queue sound "music/sfx_drop_nail_2.ogg" volume 0.2
    "I pulled them from myself, writhing, pulling..."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    $ renpy.music.set_volume(0,3, channel="music")
    "Dizzy, blurring..."
    show darkroom bright with dissolve
    "But there was another sensation."
    "The holes the nails left started to feel warm."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    "Warm, and tingling."
    play sound "music/sfx_drop_nail_2.ogg"
    "I tore the last nail out of my leg with a moan." with vpunchtiny
    show darkroom bright:
        easein_bounce 0.5 yalign 1.0
    show camera1:
        easein_bounce 0.5 yoffset -600
    "Then I slumped forward."
    "My work was finally done. My body was covered in warm spots."
    "Points of light... like little stars."
    "I laughed to myself." with vpunchtiny
    "What the fuck kind of drugs am I on?"
    show fox behindmc with dissolve
    "Clawed hands snaked around my shoulders to my front."
    "The altered metallic voice spoke right next to my ear."
    $ renpy.music.set_volume(1,10, channel="music")
    fox "You did so {i}well{/i}."
    "My head bobbed dully as the praise sank into my consciousness."
    "I did {i}well{/i}..."
    "The hands moved over my skin."
    "So warm and soft."
    "I sighed out a breath and leaned in to the touch."
    if sexcontent != "no":
        fox "Feels good now, doesn't it?"
        "It did feel good... that's what he was saying, right?"
        hide fox with dissolve
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

        fox eyeswide "Why don't you show Chat all of your {i}new little holes?{/i}"
        show darkroom bright:
            easein 0.5 yalign 0.5
        show camera1:
            easein 0.5 yoffset 0
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

        p "Chat..."
        p "The... the people?"
        fox happy "That's right~!"
        "His hands parted my thighs."
        fox horny "Show them."
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        p "Uhhh..."
        "He felt so warm."
        "I wanted to feel more."
        fox "Like {i}this.{/i}"
        $ stat_health -= 1
        "He pressed a clawed finger over a bloody puncture hole in my thigh."
        "It was soft... the heat of his finger sent an electric tingle up my leg."
        "I stifled a moan."
        "Some voice far in the back of my mind told me that was supposed to hurt."
        "But it didn't."
        "It felt so..."
        $ stat_health -= 1
        "I moved a shaking finger over another bloody nail hole and pressed down."
        p "Ahhn!"
        "The feeling shot up my other leg."
        "I was starting to breathe harder."
        fox "{i}Perfect~{/i}"
        "His voice sounded so good."
        $ stat_health -= 1
        play sound "music/sfx_gore_2.ogg" volume 0.2
        "I immediately shoved a finger into a hole in my arm."
        "The blood was so hot and wet..."
        "I couldn't help myself."
        $ stat_health -= 1
        "I jammed my finger in, parting skin, coaxing more blood from the wound."
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        "Why does it feel SO good!?"
        "Blood ran down my arm as my hips bucked forward under his hands."
        "Is he breathing harder too?"
        fox "You want more."
        "My breath hitched in my chest."
        "I want more..."
        fox eyeswide "Here..."
        "He grabbed my hands and guided them down."
        "He pushed my fingers into the loose pink underwear they'd dressed me in."
        "Any sense of embarassment vanished the second I touched the sensitive flesh."
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        "It feels so... different."
        "I explored myself with my own fingers."
        "I was panting now, hard."
        "I couldn't stop."
        $ stat_health -= 1
        "I bucked involuntarily as claws sank into the punture wounds on my arms." with vpunchtiny
        "All I could feel was heat... pressure... friction."
        "No pain at all..."
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        fox horny "Beg for more."
        p "I... ah..."
        fox "{i}Beg.{/i}"
        p "Please! Ah... More!"
        $ stat_health -= 1
        "Claws clamped down and sank into my flesh." with vpunchtiny
        "My own bloody hands shook with pleasure against my sex."
        "I moaned as I came, wracked by a hazy, magnified orgasm."
        "I could feel every one of his fingers in my skin, fat, and muscle."
        pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


        "Deep inside me."
        show darkroom:
            easein_bounce 0.5 yalign 1.0
        show camera1:
            easein_bounce 0.5 yoffset -600
        "I shuddered as the aftershocks of pleasure kept washing over me."
        hide fox with dissolve
        "Then, his fingers left me."
    elif True:
        hide fox with dissolve
        "Then the hands lifted away."
    "A pathetic, needy sound escaped me as he walked away."
    "The cold air where his body used to be made me shiver."
    "Something isn't right... I know this isn't..."
    show darkroom:
        easein 0.5 yalign 0.5
    show camera1:
        easein 0.5 yoffset 0
    pause 0.5
    show fox comp lookback with dissolve
    fox "Haha! You liked that, hm?"
    fox "See? Didn't I {i}tell{/i} you?"
    fox oncomputer "There's more than one way to skin a-" with dissolve
    fox "Oh? Neko M has an interesting suggestion!"
    "His chuckle sounded like music."
    fox comp shrug "You guys are really in the mood for power tools today!" with dissolve
    fox comp -shrug "Well. You know what I always say~"
    fox comp cocked "Your wish is my command! {image=icon_heart}"
    hide fox with dissolve
    "He walked somewhere into the darkness."
    "My brain replayed the words {i}'power tools'{/i} over and over."
    "That's bad, isn't it?"
    "Isn't it bad?"
    show fox torch:
        yalign 0
        xalign 0.5
        yoffset -100
    with dissolve
    "He returned to me, holding some new object."
    show fox torch flicker
    play sound "music/sfx_blowtorch_1.ogg" volume 0.5
    "I froze at the sudden burst of light and heat."
    hide fox with dissolve
    show fox torch close:
        yoffset 0
    with dissolve
    fox "Neko says you're bleeding a lot."
    fox "-that we should {i}cauterize{/i} your little holes~"
    show darkroom:
        easein 2.0 yalign 0.7
    show camera1:
        easein 2.0 yoffset -180
    show fox torch close:
        easein 2.0 yoffset -240
    "I couldn't fully comprehend what he was saying."
    fox "I have a little challenge for {i}you{/i} too."
    fox "Do you think you can handle it?"
    show darkroom:
        easein 1.0 yalign 0.5
    show camera1:
        easein 1.0 yoffset 0
    show fox torch close:
        easein 1.0 yoffset 0
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    p "... Me?"
    fox torch close happy "That's right~!"
    fox "I'm going to leave your hands free."
    fox torch close -happy "And you're going to keep them down."
    show darkroom:
        easein 0.5 yalign 0.7
    show camera1:
        easein 0.5 yoffset -200
    show fox torch close:
        easein 0.5 yoffset -240
    "I looked down at my hands, attached to my arms, dead weights."
    "I scoffed."
    p "That's easy."
    "He laughed at my response."
    fox "Is it?"
    fox "Just remember."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    fox "Or else I'll burn your hands."
    fox "{i}You don't want that.{/i}"
    p "No, I don't want that."
    "My slurred responses felt automatic."
    "Like someone else was speaking for me."
    "A smile crept to the edges of my lips."
    "That's nice. That's easier."
    "I watched him raise the nozzle of the blowtorch to my arm."
    $ persistent.cgs_fox.add("cg_fox_torch_close_on")
    $ renpy.save_persistent()
    show fox torch flicker close
    play sound "music/sfx_blowtorch_1.ogg"
    "Heat and light exploded from the tip."
    "My eyelids fluttered, bewildered."
    show darkroom:
        easein 0.25 yalign 0.5
    show camera1:
        easein 0.25 yoffset 0
    show fox torch close:
        easein 0.25 yoffset 0
    show afterburn:
        xalign 0.5
        yalign 0.0
        alpha 0.0
        yoffset -240
        easein 0.25 alpha 1.0
        easein_expo 2.0 alpha 0.0 yalign 1.0
    "An echo of the sun was burned into my vision."
    hide afterburn
    "I couldn't blink it away."
    fox "You may not want to look directly at it, pet."
    fox torch close happy "Not if you want your only eye to keep working!"
    "He laughed and I laughed along with him."
    "Yes. I should look away."
    "It's too bright."
    show fox torch flicker close
    play sound "music/sfx_blowtorch_2.ogg"
    "The light flashed again, and I felt the blast of heat."
    p "{i}It's so hot...{/i}"
    "I lifted my hand weakly to touch the hot spot on my arm."
    show fox torch close angry
    "Claws clamped around my wrist." with vpunchtiny
    fox "Keep. Your hands. Down."
    "I gasped at the change in his demeanor."
    "And for some reason, I felt ashamed."
    "How did I forget..?"
    p "Sorry... I'm sorry..."
    show fox torch flicker close
    play sound "music/sfx_blowtorch_2.ogg"
    "His claws disappeared and another miniature sun blossomed at the edge of my vision."
    "I started to notice a strange smell."
    p "It's burning..?"
    show darkroom:
        easeout 4.0 yalign 0.7
    show camera1:
        easeout 4.0 yoffset -200
    show fox torch close fire:
        easeout 4.0 yoffset -240
    play sound "music/sfx_blowtorch_2.ogg"
    "Light flashed, again and again."
    "The smell got stronger."
    "Heat, and burning... the little suns..."
    "Images of campfires started to dance in my head."
    "My mouth watered in memory of things cooked over a flame."
    show fox torch close -fire
    "Cool air washed over the hot spots on my body, and the darkness returned."
    show darkroom:
        easein 0.25 yalign 0.5
    show camera1:
        easein 0.25 yoffset 0
    show fox torch close:
        easein 0.25 yoffset 0
    fox "How do you feel, darling~?"
    p "Uhh..."
    p "Hungry..."
    show fox torch close happy at laugh:
        yoffset 0
    "That familiar fox bark erupted from him."
    fox "Really?"
    p "It... s-smells... like..."
    fox "Ooh~"
    show fox ultraclose cocked:
        yoffset 0
    $ renpy.music.set_volume(0,0.5, channel="music")
    fox "Well, why don't you take a bite?"
    p "A bite..?"
    "He gently picked my arm up from the ground and held it up in front of me." with vpunchtiny
    "I realized the smell was, indeed, coming from me."
    fox ultraclose happy "Go ahead~"
    p "That's my arm?"
    $ renpy.music.set_volume(1,3, channel="music")
    fox ultraclose -happy "Do it."
    "His voice had changed again."
    "That was a command. I have to."
    "I brought my arm up to my face."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    hide fox with dissolve
    show darkroom bright with dissolve
    "And I breathed in the intoxicating scent of charred meat."
    "I want to taste it anyway."
    "I opened my mouth and licked the skin."
    "The texture was so rough, and the sensation sent sparks through me."
    $ stat_health -= 1
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "I sank my teeth in without another thought." with vpunchtiny
    "Tingling heat, pressure, even the slick of my own saliva."
    "It made me crazy."
    $ stat_health -= 3
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "I slowly pulled away a chunk of meat with a moan." with vpunchtiny
    "As I rolled it in my mouth I felt him press up behind me."
    "I chewed and relished the morsel."
    "I was so hungry."
    fox "You're so {i}cute{/i}~"
    fox "They adore you..."
    "\"They\"?"
    show darkroom with dissolve
    "My gaze settled on the camera in front of me."
    fox "{i}Your audience{/i}. Don't you remember?"
    "I swallowed."
    p "... Chat."
    fox happy "That's right!"
    fox -happy "They've been watching you, this whole time."
    show darkroom:
        easein 0.25 yalign 0.6
    show camera1:
        easein 0.25 yoffset -200
    "I looked at the bleeding divot in my arm."
    "Something at the back of my mind was screaming."
    fox "They {i}love{/i} watching you bleed."
    fox "They love watching you {i}fall apart{/i}."
    fox "All your hopes and dreams..."
    fox "All the memories..."
    fox horny "An {i}entire life{/i} spilling out on the floor."
    if sexcontent != "no":
        fox -horny "Some of them are probably masturbating right now, did you know that?"
    "Something was dripping from my chin. I didn't know if it was blood or tears."
    "I was shaking."
    fox "They can all see you."
    "I heard a faint click and the shuffling of him removing his mask."
    "I shivered as his lips touched my ear."
    fox teeth open "{i}But only {b}I{/b} can {b}smell{/b} you.{/i}"
    "The screaming inside me was scratching at me, trying to escape."
    fox teeth -open "Take another bite."
    p "I-I..."
    p "That's my arm, I-"
    $ stat_health -= 1
    show darkroom red
    "Fangs clamped down on my collar, stunning me to silence." with vpunch
    show darkroom red:
        easein_bounce 0.25 yalign 0.5
    show camera1:
        easein_bounce 0.25 yoffset 0
    "Without pain, there was only the pressure and the vague sensation of tearing."
    $ stat_health -= 1
    "He thrashed and pulled for a moment, ripping the skin apart viciously."
    "I felt blood spill out from his mouth, still closed over my neck."
    "Then I felt his tongue, moving slowly over the wound."
    p "A-Ahhhn~"
    "Why did I make that sound!?"
    "I know this is bad, I know it is!"
    "But it's so..."
    show black with eyedissolve
    "I squeezed my eyes shut, trying to ignore it."
    show darkroom behind black
    "All I could sense was his tongue and his heavy breathing."
    hide black with eyedissolve_reverse
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "This isn't helping at all!"
    "He lapped at my wound a few times before he finally withdrew, panting."
    show fox comp maskon with dissolve
    "I sat there, still stunned, as he licked his lips and put his mask back on."
    "He cleared his throat."
    "He seemed... almost embarrassed."
    fox comp lookback "That's... enough."
    "With a quick roll of his shoulders, he turned back to the screens."
    fox comp -lookback "Well! Who's ready for the grand finale?"
    fox comp presenting "You came here for blood, and blood you shall receive~!"
    show fox comp -presenting
    "His demeanor changed again. I couldn't keep track of what was happening."
    fox comp cocked "This next little game is very simple."
    hide fox with dissolve
    "He circled behind me again."
    "I jumped a little when something light fell on my shoulders."
    "Wire..?"
    "It closed around my neck."
    "A bubble of fear made its way to the front of my mind."
    play sound "<from 0 to 0.45>music/sfx_chain_retracted.ogg"
    "He connected the wire loop to the chain above me." with vpunchtiny
    p "Wh- ah-"
    play sound "<from 0 to 0.5>music/sfx_rope.ogg"
    "The wire tightened." with vpunchtiny
    "I had to strain my shackled legs to raise myself enough to breathe."
    "It seemed nearly impossible with my body feeling so heavy."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "My head was swimming."
    show fox hand knife:
        yalign 0.5
        xalign 1.0
    show darkroom bright
    with dissolve
    fox "Here."
    "Huh?"
    "I looked at his offering."
    hide fox with dissolve
    "I gingerly took it into my hands."
    "A knife."
    show fox close long:
        yoffset 0
        xalign 0.5
    with dissolve
    fox "They want to see {i}blood{/i} darling~"
    "Blood. They want to see blood."
    "The unspoken agreement materialized in my head."
    "Cut myself and the wire goes away."
    show darkroom bright:
        easein 0.5 yalign 0.6
    show camera1:
        easein 0.5 yoffset -150
    show fox close long:
        easein 0.5 yoffset -100
    "Right?"
    "That's easy. Nothing hurts right now."
    $ stat_health -= 1
    play sound "music/sfx_knife_stab.ogg"
    "I slashed the blade sloppily across the top of my thigh." with vpunchtiny
    "As expected, blood began to seep out from the wound."
    show darkroom bright:
        easein 0.25 yalign 0.5
    show camera1:
        easein 0.25 yoffset 0
    show fox close long:
        easein 0.25 yoffset 0
    "I looked up expectantly."
    fox close long happy "That's good..."
    fox close long -happy "But..."
    fox close long lust "They want to see more."
    show darkroom bright:
        easein 0.25 yalign 0.6
    show camera1:
        easein 0.25 yoffset -150
    show fox close long:
        easein 0.25 yoffset -100
    $ stat_health -= 1
    play sound "music/sfx_knife_stab.ogg"
    "I slashed again, with little concern for my legs." with vpunchtiny
    "I could barely feel it anyway."
    show darkroom bright:
        easein 0.25 yalign 0.5
    show camera1:
        easein 0.25 yoffset 0
    show fox close long:
        easein 0.25 yoffset 0
    fox close long -lust "No."
    p "Huh..?"
    fox close long lust "Your belly."
    fox "Deeper."
    show darkroom bright:
        easein 0.25 yalign 0.6
    show camera1:
        easein 0.25 yoffset -150
    show fox close long lust:
        easein 0.25 yoffset -100
    "I looked down."
    "Deeper?"
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "I touched the point of the knife to the side of my stomach."
    "I knew the wire must be cutting into my neck."
    "My breaths were so shallow."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "It's like a dream."
    "Just a dream."
    $ stat_health -= 1
    "I pushed the tip inside, filled with wonder at how easy it was."
    "I understand now."
    "They want to see my insides."
    $ stat_health -= 5
    play sound "music/sfx_knife_long.ogg"
    play music2 "music/ambient_fox_heartslow.ogg" fadein 2.0
    "I dragged the blade across my belly, deep, through skin, fat, and muscle." with vpunchtiny
    if fox_love >= 15:
        show darkroom:
            easein 0.1 yalign 0.5
        show camera1:
            easein 0.1 yoffset 0
        show fox close long eyeswide:
            easein 0.1 yoffset 0
        $ renpy.music.set_volume(0.2,1, channel="music")
        fox "... Wait."
        "My hand immediately froze."
        "I looked up at him, knife still inside me, waiting for my next instruction."
        "But... he just stood there."
        hide fox with dissolve
        show fox comp with dissolve
        "He turned to his screens."
        fox "No, of {i}course{/i} not."
        if show_rensdecision == 0:
            fox comp lookback "..."
            $ renpy.music.set_volume(1,1, channel="music")
            fox comp angry "I was just making sure you guys were having fun, of course~!"
            fox comp presenting "As always, I am at your beck and call~"
            show fox comp lookback
            "He turned back to me."
            fox "... Keep going."
            hide fox with dissolve
            "I remembered what I was doing."
            "Right! My insides!"
            show darkroom bright with dissolve
        elif True:
            fox comp presenting "Your wish is my..."
            fox comp over "..."
            fox "Actually... Fuck that."
            fox oncomputer "Show's over." with dissolve
            stop music
            $ renpy.music.set_volume(1, channel="music")
            scene black
            "The screens suddenly went dark."
            "I can't see!"
            play sound "<from 0 to 1>music/sfx_knife_drop.ogg" volume 0.5
            "I felt something grab the knife out of my hands and throw it across the room."
            play sound "music/sfx_cord.ogg" volume 0.5
            queue sound "music/sfx_chain_short.ogg" volume 0.5
            "I gasped as the wire suddenly released and I fell forward onto my knees." with vpunchtiny
            "I took in a few ragged breaths as the wire was pulled away from my neck."
            play sound "<from 0 to 0.45>music/sfx_chain_retracted.ogg" volume 0.5
            "Dizzy and confused, I felt the shackles around my ankles open."
            "I was pushed onto my back."
            p "What's happening..?"
            p "Why did you stop the... the..."
            fox empty "Shut up!"
            fox empty "... Stop talking."
            play sound "music/sfx_door_knock.ogg" volume 0.5
            "I heard a knock at the heavy door."
            $ persistent.cgs_fox.add("cg_fox_keep")
            $ renpy.save_persistent()
            pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>





            show fox keep1
            show darkwipe:
                xalign 1.0
                easeout 0.5 xoffset 1400
            show fox keep2:
                xalign 0.5
                yalign 1.0
                easein 3.0 xalign 0.2 yoffset 10
                easein 3.0 xalign 0.8 yoffset 50
                easein_expo 3.0 xalign 0.5 yoffset 0 yalign 0.0
            goon "You hit the call button Sir..?"
            fox keep1 "Medics. Now."
            goon "I have two here."
            pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


            fox keep2 "The abdomen. Stop the bleeding."
            fox "I want [pp_obj] alive."
            show fox keep3
            stop music2 fadeout 1.0
            pause(1.0)
            if achievement.has("ach_show_keep") != True:
                $ persistent.ach_show_keep = True
                $ achievement.grant("ach_show_keep")
                init:
                    $ achievement.register("ach_show_keep")
                    $ achievement.sync()
                    $ renpy.save_persistent()
                    if persistent.ach_show_keep == True and achievement.has("ach_show_keep") != True:
                        $ achievement.grant("ach_show_keep")
                        $ achievement.register("ach_show_keep")
                        $ achievement.sync()
            fox "This one is {i}mine{/i} now."
            scene black with dissolve
            hide screen status
            hide screen effect_health
            $ quick_menu = False
            play music "music/music_emptylove.ogg"
            scene bg_endslate_survival with zoomdissolve
            show screen bg_endslate_survival_text("You Lived","Fox kept you")
            $ renpy.pause(hard=True)
    show darkroom bright:
        easein 0.25 yalign 0.6
    show camera1:
        easein 0.25 yoffset -150
    "I kind of want to see them too."
    "I've never seen them before!"
    "I didn't know if it was the drugs or lack of oxygen, but I felt giddy."
    $ stat_health -= 1
    "I dropped the knife and touched the wound I created."
    $ stat_health -= 1
    play sound "music/sfx_gore_wet.ogg"
    "My fingertips danced over the edge, then slipped inside."
    "It's so warm!"
    "And soft... and slippery..."
    p "Look..."
    $ stat_health -= 20
    hide fox with dissolve
    show darkroom:
        easein 0.25 yalign 1.0
    show camera1:
        easein 0.25 yoffset -500
    show showguts1:
        yalign 1.0
        xalign 0.5
        yoffset 350
        easein 0.25 yoffset 0
    play sound "music/sfx_gore_wet_2.ogg"
    "I pulled a shape from inside the bloody fissure."
    "The pressure and sense of {i}pulling{/i} within me was so bizarre."
    p "Look! I-"
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    "A cough interrupted my hoarse whisper." with vpunchtiny
    "That's okay. I'll just show them."
    $ persistent.cgs_fox.add("cg_MC_guts2")
    $ renpy.save_persistent()
    $ stat_health -= 50
    show darkroom red:
        easein 1.0 yalign 0.5
    show camera1:
        easein 1.0 yoffset 0
    show showguts1:
        easein 1.0 yoffset 450
    show showguts2:
        yalign 1.0
        xalign 0.5
        yoffset 720
        pause 1.0
        easein 1.0 yoffset 0
    play sound "music/sfx_blood_drip_2.ogg"
    "I pulled from within myself and held up the glistening mass for the camera."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>


    p "{size=12}Look...{/size}"
    "The wire around my neck cut off my ability to talk."
    "I realized it cut off my ability to breathe too."
    show showguts2:
        easeout 0.5 yoffset 720
    pause 0.5
    show darkroom red:
        easein_bounce 0.25 yalign 1.0
    show camera1:
        easein_bounce 0.25 yoffset -500
    play sound "music/sfx_gore_wet.ogg"
    queue sound "music/sfx_blood_drip.ogg"
    "My arms drooped and my offering poured out between my legs."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    stop music fadeout 5.0
    "I smiled to myself."
    pass # <<<COULD NOT DECOMPILE: Unknown AST node: <class 'renpy.ast.Camera'>>>>

    "This is definitely my best show."
    stop music2 fadeout 1.0
    scene black with eyedissolve
    hide screen effect_health with dissolve
    if achievement.has("ach_show_3") != True:
        $ persistent.ach_show_3 = True
        $ achievement.grant("ach_show_3")
        init:
            $ achievement.register("ach_show_3")
            $ achievement.sync()
            $ renpy.save_persistent()
            if persistent.ach_show_3 == True and achievement.has("ach_show_3") != True:
                $ achievement.grant("ach_show_3")
                $ achievement.register("ach_show_3")
                $ achievement.sync()
    play sound "music/sfx_foxlaugh.ogg"
    "He's going to be so happy."
    pause 1.0
    hide screen status
    $ quick_menu = False
    $ persistent.deathcounter += 1
    $ renpy.save_persistent()
    if meme_mode:
        play music "music/ambient_fox_buddy.ogg"
        queue music "<from 0.3>music/you_died.ogg"
    elif True:
        play music "<from 0.3>music/you_died.ogg"
    scene bg_endslate with blooddissolve
    show screen bg_endslate_text("You Died","You were the star of the show - Show 3")
    $ renpy.pause(hard=True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
