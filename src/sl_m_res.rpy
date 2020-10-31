init python:
    def sl_m_meet(who,name):
        try:
            meet(who,name)
        except NameError:
            gl = globals()
            gl[who+"_name"] = name

init 6 python:
    if persistent.endings["sl_m_green"] == None:
        persistent.endings["sl_m_green"] = False
    if persistent.endings["sl_m_red"] == None:
        persistent.endings["sl_m_red"] = False
    if persistent.endings["sl_m_blue"] == None:
        persistent.endings["sl_m_blue"] = False

    achievments["ACH_SL_M_GREEN"] = persistent.endings["sl_m_green"]
    achievments["ACH_SL_M_RED"] = persistent.endings["sl_m_red"]
    achievments["ACH_SL_M_BLUE"] = persistent.endings["sl_m_blue"]

    ach_table["sl_m_green"] = {
        None : "sl_m_green",
        "english" : "sl_m_green",
        "spanish" : "sl_m_green",
        "italian" : "sl_m_green",
        "chinese" : "sl_m_green",
        "latvian" : "sl_m_green",
        }

    ach_table["sl_m_red"] = {
        None : "sl_m_red",
        "english" : "sl_m_red",
        "spanish" : "sl_m_red",
        "italian" : "sl_m_red",
        "chinese" : "sl_m_red",
        "latvian" : "sl_m_red",
        }

    ach_table["sl_m_blue"] = {
        None : "sl_m_blue",
        "english" : "sl_m_blue",
        "spanish" : "sl_m_blue",
        "italian" : "sl_m_blue",
        "chinese" : "sl_m_blue",
        "latvian" : "sl_m_blue",
        }

init -10:
    python:
        try:
            if not config_session:
                p = "scenario_slavyana/res/images/avatars/mz/sl_m_mz-"
                sl_m_mz_avatar_set = {
                            'body':p+"body.png",
                            -2    :p+"emo01.png",
                            -1    :p+"emo01.png",
                            0     :p+"emo03.png",
                            1     :p+"emo03.png",
                            2     :p+"emo05.png",
                        }
        except NameError:
            p = 'scenario_slavyana/res/images/avatars/mz/sl_m_mz-'
            sl_m_mz_avatar_set = {'body':(p) + ('body.png'), -2:(p) + ('emo01.png'), -1:(p) + ('emo01.png'), 0:(p) + ('emo03.png'), 1:(p) + ('emo03.png'), 2:(p) + ('emo05.png')}

init:
    $ pen_write = "scenario_slavyana/res/sound/pen1.mp3"

    image bknt_clear = "scenario_slavyana/res/images/bknt/bknt.png"
    image bknt_w1 = "scenario_slavyana/res/images/bknt/bknt1.png"
    image bknt_w2 = "scenario_slavyana/res/images/bknt/bknt2.png"
    image bknt_w3 = "scenario_slavyana/res/images/bknt/bknt3.png"
    image bknt_w4 = "scenario_slavyana/res/images/bknt/bknt4.png"
    image bknt_w4_1 = "scenario_slavyana/res/images/bknt/bknt4_1.png"
    image bknt_w4_2_1 = "scenario_slavyana/res/images/bknt/bknt4_2_1.png"
    image bknt_w4_2_2 = "scenario_slavyana/res/images/bknt/bknt4_2_2.png"
    image bknt_w5 = "scenario_slavyana/res/images/bknt/bknt5.png"
    image bknt_w5_1_1 = "scenario_slavyana/res/images/bknt/bknt5_1_1.png"
    image bknt_w5_1_2 = "scenario_slavyana/res/images/bknt/bknt5_1_2.png"
    image bknt_w5_2 = "scenario_slavyana/res/images/bknt/bknt5_2.png"
    image bknt_w6_1 = "scenario_slavyana/res/images/bknt/bknt6_1.png"
    image bknt_w6_1_2 = "scenario_slavyana/res/images/bknt/bknt6_1_2.png"
    image bknt_w6_1_1_1 = "scenario_slavyana/res/images/bknt/bknt6_1_1_1.png"
    image bknt_w6_1_1_2 = "scenario_slavyana/res/images/bknt/bknt6_1_1_2.png"
    image bknt_w6_2 = "scenario_slavyana/res/images/bknt/bknt6_2.png"
    image bknt_w6_2_1_1 = "scenario_slavyana/res/images/bknt/bknt6_2_1_1.png"
    image bknt_w6_2_1_2 = "scenario_slavyana/res/images/bknt/bknt6_2_1_2.png"
    image bknt_w6_2_2 = "scenario_slavyana/res/images/bknt/bknt6_2_2.png"
    image bknt_w7_1 = "scenario_slavyana/res/images/bknt/bknt7_1.png"
    image bknt_w7_1_2 = "scenario_slavyana/res/images/bknt/bknt7_1_2.png"
    image bknt_w7_1_1_1 = "scenario_slavyana/res/images/bknt/bknt7_1_1_1.png"
    image bknt_w7_1_1_2 = "scenario_slavyana/res/images/bknt/bknt7_1_1_2.png"
    image bknt_w7_2 = "scenario_slavyana/res/images/bknt/bknt7_2.png"
    image bknt_w7_2_1_1 = "scenario_slavyana/res/images/bknt/bknt7_2_1_1.png"
    image bknt_w7_2_1_2 = "scenario_slavyana/res/images/bknt/bknt7_2_1_2.png"
    image bknt_w7_2_2 = "scenario_slavyana/res/images/bknt/bknt7_2_2.png"
    image bknt_w8 = "scenario_slavyana/res/images/bknt/bknt8.png"
    image bknt_w9 = "scenario_slavyana/res/images/bknt/bknt9.png"

    image bg main_day = "scenario_slavyana/res/images/menu/bg/m_day.png"
    image bg main_eve = "scenario_slavyana/res/images/menu/bg/m_eve.png"
    image bg main_night = "scenario_slavyana/res/images/menu/bg/m_night.png"
    
    image bg days_day = "scenario_slavyana/res/images/menu/bg/d_day.png"
    image bg days_eve = "scenario_slavyana/res/images/menu/bg/d_eve.png"
    image bg days_night = "scenario_slavyana/res/images/menu/bg/d_night.png"
    
    image bg set_day_no = "scenario_slavyana/res/images/menu/bg/set_day_no.png"
    image bg set_eve_no = "scenario_slavyana/res/images/menu/bg/set_eve_no.png"
    image bg set_night_no = "scenario_slavyana/res/images/menu/bg/set_night_no.png"
    image bg set_day_yes = "scenario_slavyana/res/images/menu/bg/set_day_yes.png"
    image bg set_eve_yes = "scenario_slavyana/res/images/menu/bg/set_eve_yes.png"
    image bg set_night_yes = "scenario_slavyana/res/images/menu/bg/set_night_yes.png"
    
    image bg gal_day = "scenario_slavyana/res/images/menu/bg/gal_day.png"
    image bg gal_eve = "scenario_slavyana/res/images/menu/bg/gal_eve.png"
    image bg gal_night = "scenario_slavyana/res/images/menu/bg/gal_night.png"
    
    image bg ext_aidpost_sunset = "scenario_slavyana/res/images/bg/ext_aidpost_sunset.jpg"
    image bg ext_shed_day = "scenario_slavyana/res/images/bg/ext_shed_day.jpg"
    image bg ext_shed_sunset = "scenario_slavyana/res/images/bg/ext_shed_sunset.jpg"
    image bg ext_shed_night = "scenario_slavyana/res/images/bg/ext_shed_night.jpg"
    image bg ext_houses_night = "scenario_slavyana/res/images/bg/ext_houses_night.jpg"
    image bg ext_house_of_sl_sunset = "scenario_slavyana/res/images/bg/ext_house_of_sl_sunset.jpg"
    image bg ext_house_of_sl_night = "scenario_slavyana/res/images/bg/ext_house_of_sl_night.jpg"
    image bg ext_house_of_sl_night_light = "scenario_slavyana/res/images/bg/ext_house_of_sl_night_light2.jpg"
    image bg ext_square_sunset_party = "scenario_slavyana/res/images/bg/ext_square_sunset_party.jpg"

    image bg int_house_of_sl_night = "scenario_slavyana/res/images/bg/int_house_of_sl_night.jpg"
    image bg int_house_of_sl_sunset = "scenario_slavyana/res/images/bg/int_house_of_sl_sunset.jpg"
    image bg int_library_sunset = "scenario_slavyana/res/images/bg/int_library_sunset.png"
    
    image cg d2_lineup_an = "scenario_slavyana/res/images/cg/d2_lineup.jpg"
    image cg d3_sl_library_an = "scenario_slavyana/res/images/cg/d3_sl_library.jpg"
    image cg d3_sl_library_2_an = "scenario_slavyana/res/images/cg/d3_sl_library_2.jpg"
    image cg d3_sl_bathhouse_hk_alt = im.Scale("scenario_slavyana/res/images/cg/d3_sl_bathhouse_hk_alt.jpg", 1920, 1440)
    image cg d3_sl_dance_an = "scenario_slavyana/res/images/cg/d3_sl_dance.jpg"
    image cg d3_sl_evening_alt = im.Scale("scenario_slavyana/res/images/cg/d3_sl_evening.jpg", 1920, 1440)

    #рукоделие!
    image bg int_house_of_sl_night_light = "scenario_slavyana/res/images/bg/int_house_of_sl_night_light.jpg"

    image cg d5_cake_alt = "scenario_slavyana/res/images/cg/d5_cake.jpg"
    image cg d6_sl_forest_2_alt = "scenario_slavyana/res/images/cg/d6_sl_forest_2.png"
    image cg d6_sl_swim_alt = "scenario_slavyana/res/images/cg/d6_sl_swim.png"
    image cg d6_sl_after_swim = "scenario_slavyana/res/images/cg/d6_sl_after_swim.png"
    image cg d6_sl_hentai_1_alt = "scenario_slavyana/res/images/cg/d6_sl_hentai_1.png"
    #image cg d5_sl_sleep_alt = "scenario_slavyana/res/images/cg/d5_sl_sleep.jpg"
    #image cg d5_sl_sleep_2_alt = "scenario_slavyana/res/images/cg/d5_sl_sleep_2.png"
    image cg under_water = "scenario_slavyana/res/images/cg/under_water.jpg"
    image bg ext_polyana_mere_day = "scenario_slavyana/res/images/bg/ext_polyana_mere_day.png"
    image bg town_snow = "scenario_slavyana/res/images/bg/town_snow.jpg"
    image bg ext_camp_upview_snow = "scenario_slavyana/res/images/bg/ext_camp_upview_snow.png"
    image bg ext_admins_day = "scenario_slavyana/res/images/bg/ext_admins_day.jpg"
    image bg ext_stage_big_sunset = "scenario_slavyana/res/images/bg/ext_stage_big_sunset.jpg"

    image sl_m_green = "scenario_slavyana/res/images/misc/ach/achievement_green.png"
    image sl_m_red = "scenario_slavyana/res/images/misc/ach/achievement_red.png"
    image sl_m_blue = "scenario_slavyana/res/images/misc/ach/achievement_blue.png"

    #Толик
    $ colors['tl'] = {'night': (173, 173, 173, 255), 'sunset': (173, 173, 173, 255), 'day': (173, 173, 173, 255), 'prolog': (173, 173, 173, 255)}
    $ names['tl'] = u"Толик"
    $ store.names_list.append('tl')

    #Борис
    $ colors['bor'] = {'night': "#33ccff", 'sunset': "#33ccff", 'day': "#33ccff", 'prolog': "#33ccff"}
    $ names['bor'] = u"Борис"
    $ store.names_list.append('bor')

    #Незнакомец
    $ colors['stranger'] = {'night': "#950036", 'sunset': "#950036", 'day': "#950036", 'prolog': "#950036"}
    $ names['stranger'] = u"Незнакомец"
    $ store.names_list.append('stranger')

    #спрайты

    #Толик
    image tl pioneer normal = "scenario_slavyana/res/images/sprites/normal/tl/tl_1_pioneer.png"
    image tl pioneer far = "scenario_slavyana/res/images/sprites/far/tl/tl_1_pioneer.png"

    image bor normal close = im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/bor/bor_1_body.jpg")
    image bor serious close = im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/bor/bor_2_body.jpg")

    #Семён, close
    image pi angry pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_angry.png") )

    image pi grin pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_grin.png") )

    image pi normal pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_normal.png") )

    image pi serious pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_serious.png") )

    image pi shocked pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shocked.png") )

    image pi smile pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_smile.png") )

    image pi surprise pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_surprise.png") )

    image pi upset pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_upset.png") )

    image pi angry shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_angry.png") )

    image pi grin shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_grin.png") )

    image pi normal shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_normal.png") )

    image pi serious shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_serious.png") )

    image pi shocked shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shocked.png") )

    image pi smile shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_smile.png") )

    image pi surprise shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_surprise.png") )

    image pi upset shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_upset.png") )

    image pi angry swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_angry.png") )

    image pi grin swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_grin.png") )

    image pi normal swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_normal.png") )

    image pi serious swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_serious.png") )

    image pi shocked swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_shocked.png") )

    image pi smile swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_smile.png") )

    image pi surprise swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_surprise.png") )

    image pi upset swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_upset.png") )

    #Семён, normal
    image pi angry pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_angry.png") )

    image pi grin pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_grin.png") )

    image pi normal pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png") )

    image pi serious pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_serious.png") )

    image pi shocked pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shocked.png") )

    image pi smile pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_smile.png") )

    image pi surprise pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_surprise.png") )

    image pi upset pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_upset.png") )

    image pi angry shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_angry.png") )

    image pi grin shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_grin.png") )

    image pi normal shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png") )

    image pi serious shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_serious.png") )

    image pi shocked shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shocked.png") )

    image pi smile shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_smile.png") )

    image pi surprise shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_surprise.png") )

    image pi upset shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_upset.png") )

    image pi angry swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_angry.png") )

    image pi grin swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_grin.png") )

    image pi normal swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png") )

    image pi serious swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_serious.png") )

    image pi shocked swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shocked.png") )

    image pi smile swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_smile.png") )

    image pi surprise swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_surprise.png") )

    image pi upset swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_upset.png") )

    image pi normal nfd = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_nfd.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_nfd.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_nfd.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png") )

    #Семён, far
    image pi angry pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_angry.png") )

    image pi grin pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_grin.png") )

    image pi normal pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_normal.png") )

    image pi serious pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_serious.png") )

    image pi shocked pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shocked.png") )

    image pi smile pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_smile.png") )

    image pi surprise pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_surprise.png") )

    image pi upset pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_pioneer.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_upset.png") )

    image pi angry shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_angry.png") )

    image pi grin shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_grin.png") )

    image pi normal shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_normal.png") )

    image pi serious shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_serious.png") )

    image pi shocked shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shocked.png") )

    image pi smile shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_smile.png") )

    image pi surprise shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_surprise.png") )

    image pi upset shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shirt.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_upset.png") )

    image pi angry swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_angry.png") )

    image pi grin swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_grin.png") )

    image pi normal swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_normal.png") )

    image pi serious swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_serious.png") )

    image pi shocked swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_shocked.png") )

    image pi smile swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_smile.png") )

    image pi surprise swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_surprise.png") )

    image pi upset swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_swim.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_upset.png") )
    
    ####WINTER_IS_COMING####
    image pi default coat close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_default.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_default.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_default.png") )

    image pi default coat far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_default.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_default.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/far/pi/pi_2_default.png") )

    image pi default coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_default.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_default.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_default.png") )

    image pi normal coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_normal.png") )

    image pi shocked coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_shocked.png") )

    image pi smile coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_smile.png") )

    image pi surprise coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_surprise.png") )
    
    image pi serious coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/normal/pi/pi_2_serious.png") )

    image pi normal coat close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_normal.png") )

    image pi surprise coat close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_surprise.png") )

    image pi smile coat close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_coat.png", (0,0), "scenario_slavyana/res/images/sprites/close/pi/pi_2_smile.png") )
    
    $ style.credits_sl_m = Style(style.default)
    $ style.credits_sl_m.font = 'fonts/corbelb.ttf'
    $ style.credits_sl_m.color = '#fff'
    $ style.credits_sl_m.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    $ style.credits_sl_m.drop_shadow_color = '#000'
    $ style.credits_sl_m.italic = False
    $ style.credits_sl_m.bold = False
    $ style.credits_sl_m.text_align = 0.5
    $ style.credits_sl_m.xmaximum = 0.8
    image credits_sl_m = ParameterizedText(style='credits_sl_m', size=50)
    #$ credits_sl_m_text = "{size=80}Славя-мод{/size}\n\n\nРазработчик: FireBoTer.\n\n\nПомощь в тестировании: Xent2121.\n\n\nПомощь с дизайном главного меню: Nenver Kradovich\n\n\nРесурсы: IIchan Eroge Team (ныне Moonworks и Soviet Games), сообщество игры.\n\n\nОтдельное спасибо всем, кто играет в этот мод и тем, кто помогает исправлять его!\n"

init 55 python:
    colors['fbt'] = {'night': (0, 20, 137, 255), 'sunset': (0, 20, 137, 255), 'day': (0, 20, 137, 255), 'prolog': (0, 20, 137, 255)}
    store.names_list.append('fbt')
    if "scenario__alt_sevendl" in mods and config.version == "1.2":
        names['fbt'] = u"Автор"
    else:
        try:
            set_name('fbt', u"Автор")
        except NameError:
            names['fbt'] = u"Автор"

init -410 python:
    store.map_zones = {
                "un_mi_house":   {"position":[804,146,853,203],"default_bg":bg_tmp_image(u"Лена и Мику")},
                "me_mt_house":   {"position":[957,173,1007,231],"default_bg":bg_tmp_image(u"Я и ОД")},
                "sl_mz_house":   {"position":[1020,243,1079,309],"default_bg":bg_tmp_image(u"Славя и Женя")},
                "estrade":       {"position":[1061, 49,1157,145],"default_bg":bg_tmp_image(u"Сцена")},
                "sy_sh_house":   {"position":[843,283,891,340],"default_bg":bg_tmp_image(u"Электроник и Шурик")},
                "music_club":    {"position":[622,250,701,342],"default_bg":bg_tmp_image(u"Муз. клуб")},
                "admin_house":   {"position":[772,352,880,448],"default_bg":bg_tmp_image(u"Админ. корпус")},
                "wash_house":    {"position":[694,438,791,527],"default_bg":bg_tmp_image(u"Банно-прачечная")},
                "square":        {"position":[885,352,1003,545],"default_bg":bg_tmp_image(u"Площадь")},
                "dining_hall":   {"position":[1010,449,1145,585],"default_bg":bg_tmp_image(u"Столовая")},
                "dv_us_house":   {"position":[711,615,768,674],"default_bg":bg_tmp_image(u"Алиса и Ульяна")},
                "store_house":   {"position":[1148,489,1215,583],"default_bg":bg_tmp_image(u"Склад")},
                "valleyball":    {"position":[1222,488,1320,602],"default_bg":bg_tmp_image(u"Воллейбол")},
                "sport_area":    {"position":[1321,478,1579,658],"default_bg":bg_tmp_image(u"Спорткомплекс")},
                "beach":         {"position":[1185,666,1492,831],"default_bg":bg_tmp_image(u"Пляж")},
                "boat_station":  {"position":[831,771,962,856],"default_bg":bg_tmp_image(u"Лодочный причал")},
                "old_house":     {"position":[228,993,347,1080],"default_bg":bg_tmp_image(u"Старый корпус")},
                "clubs":         {"position":[430,440,651,603],"default_bg":bg_tmp_image(u"Клубы")},
                "library":       {"position":[1160,273,1286,363],"default_bg":bg_tmp_image(u"Библиотека")},
                "badminton":     {"position":[1343,378,1448,475],"default_bg":bg_tmp_image(u"Бадминтон")},
                "medic_house":   {"position":[1037,357,1137,450],"default_bg":bg_tmp_image(u"Медпункт")},
                "camp_entrance": {"position":[271,432,424,567],"default_bg":bg_tmp_image(u"Ворота в лагерь")},
                "forest":        {"position":[550,60,697,199],"default_bg":bg_tmp_image(u"Лес")},
        }

init python:
    notebooks_lines = -1;
    def nb_show():
        global notebooks_lines
        if notebooks_lines < 0:
            renpy.show("bknt_clear",at_list = [ truecenter ])
            notebooks_lines = 0
    def nb_hide():
        global notebooks_lines
        if notebooks_lines >= 0:
            renpy.hide("bknt_clear")
            notebooks_lines = -1
    def notebok_getLinePoition(lineNumber):
        if lineNumber < 25:
            y = 0.339 + (0.014 * lineNumber)
            return Position(xpos=.438, ypos=y,xmaximum=250,text_align=.0)
        else:
            y = 0.339 + (0.014 * (lineNumber-25))
            return Position(xpos=.56, ypos=y,xmaximum=250,text_align=.0)
    def nb(text, **kwargs):
        global notebooks_lines
        if notebooks_lines >= 0:
            renpy.show("nb_line_"+str(notebooks_lines),[notebok_getLinePoition(notebooks_lines)],what=Text("{color=#0400ff}{size=-8}{font=scenario_slavyana/res/Fonts/ofont_ru_Elzevir.ttf}"+text+"{/font}{/size}{/color}"))
            notebooks_lines += 1