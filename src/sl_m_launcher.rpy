init -5 python:
    def sl_m_link1():
        import webbrowser
        url = "http://goo.gl/7dSUFV"
        webbrowser.open(url)
    def sl_m_link2():
        import webbrowser
        url = "https://goo.gl/HD0Urv"
        webbrowser.open(url)
    def sl_m_link3():
        import webbrowser
        url = "https://goo.gl/Ro288f"
        webbrowser.open(url)
    def sl_m_link4():
        import webbrowser
        url = "http://goo.gl/p6s3aF"
        webbrowser.open(url)

init python:
    from time import localtime, strftime
    t = strftime("%H:%M:%S", localtime())
    hour, min, sec = t.split(":")
    hour = int(hour)
    
    mods["slavyana_mod__launcher"] = u"Славя-мод"
    try:
        mod_tags["slavyana_mod__launcher"] = ["gameplay:vn","length:days","protagonist:female","character:Семён","character:Славя","character:Алиса","character:Ульяна","character:Лена","character:Ольга Дмитриевна","character:Виола","character:Электроник","character:Шурик","character:Женя","special:TODO"]
    except NameError:
        pass

init:  
    $ sl_m_lp = 0

    $ sl_m_Full = False
    $ sl_m_l_day = 0
    
    $ m_back = None
    $ m_back_hover = None
    $ d_back = None
    $ d_back_hover = None
    $ set_back = None
    $ set_back_hover = None

    if persistent.sl_m_hen_txt == None:
        $ persistent.sl_m_hen_txt = True

    if persistent.sl_m_hidden == None:
        $ persistent.sl_m_hidden = False
    if persistent.sl_m_not_fst_hidden == None:
        $ persistent.sl_m_not_fst_hidden = False

    if persistent.sl_m_day1 == None:
        $ persistent.sl_m_day1 = False
    if persistent.sl_m_day2 == None:
        $ persistent.sl_m_day2 = False
    if persistent.sl_m_day3 == None:
        $ persistent.sl_m_day3 = False

label slavyana_mod__launcher:
    $ new_chapter(0, u"Славя-мод")

label slavyana_mod__launcher0:
    $ reload_names()
    #$ sl_m_try = "savename"
    #call sl_m_try
    #$ sl_m_try = None
    if hour in [22,23,24,0,1,2,3,4,5,6]:
        play music music_list["forest_maiden"] fadein 1
    elif hour in [20,21]:
        play music music_list["silhouette_in_sunset"] fadein 1
    elif hour in [7,8]:    
        play music music_list["lightness"] fadein 1
    else:
        play music music_list["a_promise_from_distant_days_v2"] fadein 1

label slavyana_mod_launcher1_1:
    if hour in [22,23,24,0,1,2,3,4,5,6]:
        scene bg main_night with dissolve
        $ m_back = "scenario_slavyana/res/images/menu/bg/m_night.png"
        $ m_back_hover = "scenario_slavyana/res/images/menu/bg/m_night_hover.png"
    elif hour in [20,21] or hour in [7,8]:
        scene bg main_eve with dissolve
        $ m_back = "scenario_slavyana/res/images/menu/bg/m_eve.png"
        $ m_back_hover = "scenario_slavyana/res/images/menu/bg/m_eve_hover.png"
    else:
        scene bg main_day with dissolve
        $ m_back = "scenario_slavyana/res/images/menu/bg/m_day.png"
        $ m_back_hover = "scenario_slavyana/res/images/menu/bg/m_day_hover.png"
    
label slavyana_mod_launcher2:     
    if hour in [22,23,24,0,1,2,3,4,5,6]:
        $ night_time()
        $ persistent.sprite_time = "night"
    elif hour in [20,21] or hour in [7,8]:
        $ sunset_time()
        $ persistent.sprite_time = "sunset"
    else:
        $ day_time()
        $ persistent.sprite_time = "day"

    $ result = renpy.imagemap(m_back, m_back_hover, [
    (637, 32, 1285, 237, "logo"),
    (833, 350, 1087, 401, "play"),
    (765, 521, 1153, 587, "days"),
    (34, 886, 194, 1055, "gallery"),
    (214, 885, 397, 1055, "alisa"),
    (699, 885, 870, 1057, "vk"),
    (875, 885, 1046, 1057, "steam"),
    (1049, 885, 1220, 1057, "ficbook"),
    (1539, 885, 1710, 1057, "settings"),
    (1751, 880, 1882, 1064, "exit")
    ])
    
    if result == "play":
        scene black with dissolve
        stop music fadeout 2
        $ sl_m_Full = True
        #$ make_names_known()
        jump slavyana_mod__day1
    elif result == "days":
        jump slavyana_mod__days
    elif result == "logo":
        jump slavyana_mod__surprise
    elif result == "settings":
        jump slavyana_mod__settings
    elif result == "steam":
        $ sl_m_link1()
        jump slavyana_mod_launcher2
    elif result == "ficbook":
        $ sl_m_link2()
        jump slavyana_mod_launcher2
    elif result == "vk":
        $ sl_m_link3()
        jump slavyana_mod_launcher2
    elif result == "gallery":
        jump slavyana_mod__bknt_gallery
    elif result == "alisa":
        if hour in [22,23,24,0,1,2,3,4,5,6]:
            scene bg ext_square_night with dissolve
        elif hour in [20,21] or hour in [7,8]:
            scene bg ext_square_sunset with dissolve
        else:
            scene bg ext_square_day with dissolve
        if "alisa_mod__launcher" in mods:
            window show
            "Вы действительно желаете перейти в \"Алиса-мод. Допил\"?"
            window hide
            menu:
                "Да, перейти":
                    jump alisa_mod__launcher
                "Нет, остаться":
                    jump slavyana_mod_launcher1_1
        else:
            $ sl_m_link4()
        jump slavyana_mod_launcher2
    elif result == "exit":
        $ reload_names()
        scene black with dissolve
        stop music fadeout 3
        pause (2)
        return

label slavyana_mod__days:
    if hour in [22,23,24,0,1,2,3,4,5,6]:
        scene bg days_night with dissolve
    elif hour in [20,21] or hour in [7,8]:
        scene bg days_eve with dissolve
    else:
        scene bg days_day with dissolve

label slavyana_mod__days2:
    if persistent.sl_m_day2:
        $ d_back = "scenario_slavyana/res/images/menu/day_buttons/d_buttons_full.png"
        $ d_back_hover = "scenario_slavyana/res/images/menu/day_buttons/d_buttons_full_hover.png"
    elif persistent.sl_m_day1:
        $ d_back = "scenario_slavyana/res/images/menu/day_buttons/d_buttons_wd3.png"
        $ d_back_hover = "scenario_slavyana/res/images/menu/day_buttons/d_buttons_wd3_hover.png"
    else:
        $ d_back = "scenario_slavyana/res/images/menu/day_buttons/d_buttons_wd2.png"
        $ d_back_hover = "scenario_slavyana/res/images/menu/day_buttons/d_buttons_wd2_hover.png"

    $ result = renpy.imagemap(d_back, d_back_hover, [
    (833, 208, 1077, 274, "day1"),
    (833, 381, 1082, 447, "day2"),
    (833, 554, 1083, 620, "day3"),
    (126, 859, 548, 1043, "back_days")
    ])
    
    if result == "day1":
        #$ make_names_known()
        $ sl_m_l_day = 1
        jump slavyana_mod__l_finish
    elif result == "day2":
        if persistent.sl_m_day1:
            $ sl_m_l_day = 2
            jump slavyana_mod__l_choice
        else:
            jump slavyana_mod__days2
    elif result == "day3":
        if persistent.sl_m_day2:
            $ sl_m_l_day = 3
            jump slavyana_mod__l_choice
        else:
            jump slavyana_mod__days2
    elif result == "back_days":
        jump slavyana_mod_launcher1_1

label slavyana_mod__l_choice:
    if hour in [22,23,24,0,1,2,3,4,5,6]:
        scene bg int_house_of_sl_night_light with dissolve
        $ sunset_time()
    elif hour in [20,21]:
        scene bg int_house_of_sl_sunset with dissolve
        $ sunset_time()
    else:
        scene bg int_house_of_sl_day with dissolve
        $ day_time()
    $ sl_m_Full = False
    #$ make_names_known()
    $ sl_m_counter = 0
    window show
    if sl_m_l_day == 2:
        "Проставьте выборы предыдущего дня."
    else:
        "Проставьте выборы предыдущих дней."
        window hide
        scene cg d1_sl_dinner_0 with dspr
        $ night_time()
        window show
        "Первый день."
        window hide
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day
    show us normal sport at cleft
    show mt normal pioneer at cright
    with dissolve
    window show
    "После забега."
    window hide
    menu:
        "Помочь Ольге Дмитриевне":
            $ sl_m_day1_help_od = True
        "Помочь Ульяне":
            pass
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    scene bg ext_square_sunset with dissolve
    window show
    "Поиски Семёна. Вначале идём..."
    window hide

label slavyana_mod__l_d1_map:
    $ disable_all_zones()
    $ set_zone("forest","slavyana_mod__l_day1_forest")
    $ set_zone("me_mt_house","slavyana_mod__l_day1_od")
    $ set_zone("medic_house","slavyana_mod__l_day1_mh")
    $ set_zone("dv_us_house","slavyana_mod__l_day1_ul")

label slavyana_mod__l_d1_map2:
    $ sl_m_counter += 1
    $ show_map()
    
label slavyana_mod__d1_map_text:
    window show
    if sl_m_counter == 1:
        "Затем…"
    elif sl_m_counter == 2:
        "Далее…"
    else:
        "Финальный выбор."
    window hide
    $ disable_current_zone()
    jump slavyana_mod__l_d1_map2
    
label slavyana_mod__l_day1_od:
    scene bg ext_house_of_mt_sunset 
    show mt normal pioneer at center
    with dissolve
    pause (2)
    jump slavyana_mod__d1_map_text

label slavyana_mod__l_day1_mh:
    scene bg int_aidpost_day with dissolve
    pause (2)
    jump slavyana_mod__d1_map_text

label slavyana_mod__l_day1_ul:
    scene bg ext_house_of_dv_day with dissolve
    pause (2)
    jump slavyana_mod__d1_map_text

label slavyana_mod__l_day1_forest:
    if sl_m_counter == 1:
        $ sl_m_lp += 1
    scene bg ext_square_sunset with dissolve
    pause (2)
    if sl_m_l_day == 2:
        jump slavyana_mod__l_finish
    scene cg d2_slavya_forest with dissolve
    $ night_time()
    window show
    "Второй день."
    window hide
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_sunset
    show el normal pioneer at left 
    show mt normal pioneer at center 
    show pi normal pioneer at right 
    with dissolve
    window show
    "Вечером у столовой."
    window hide
    menu:
        "Пойти с Семёном":
            $ sl_m_lp += 2
            $ sl_m_day2_go_with_sp = True
        "Остаться":
            scene bg ext_dining_hall_near_sunset with dissolve
            window show
            "Вторая попытка."
            window hide
            menu:
                "Пойти за Семёном":
                    $ sl_m_lp += 1
                    $ sl_m_day2_sp_keys = True
                "Остаться":
                    pass
    if sl_m_l_day == 3:
        jump slavyana_mod__l_finish

label slavyana_mod__l_finish:
    if hour in [22,23,24,0,1,2,3,4,5,6]:
        scene bg int_house_of_sl_night_light with dissolve
        $ sunset_time()
    elif hour in [20,21]:
        scene bg int_house_of_sl_sunset with dissolve
        $ sunset_time()
    else:
        scene bg int_house_of_sl_day with dissolve
        $ day_time()
    window show
    if sl_m_l_day <= 2:
        if sl_m_l_day == 1:
            "Запускать ли следующие дни после окончания выбранного?"
        else:
            "Запускать ли следующий день после окончания выбранного?"
        window hide
        menu:
            "Да":
                $ sl_m_Full = True
            "Нет":
                $ sl_m_Full = False
        window show
    elif sl_m_l_day > 1:
        $ sl_m_meet('mt','Оля')
    "Нажмите, чтобы продолжить..."
    window hide
    scene black with dissolve
    stop music fadeout 2
    if sl_m_l_day == 1:
        jump slavyana_mod__day1
    elif sl_m_l_day == 2:
        jump slavyana_mod__day2
    elif sl_m_l_day == 3:
        jump slavyana_mod__day3

label slavyana_mod__surprise:
    if hour in [22,23,24,0,1,2,3,4,5,6]:
        scene bg ext_square_night with dissolve
    elif hour in [20,21] or hour in [7,8]:
        scene bg ext_square_sunset with dissolve
    else:
        scene bg ext_square_day with dissolve
    $ persistent.sl_m_hidden = True
    if persistent.sl_m_not_fst_hidden:
        menu:
            "Прочитать ещё раз":
                pass
            "Перейти к Ульяна-моду":
                stop music fadeout 2
                jump uliana_mod_day1
            "Вернуться":
                jump slavyana_mod_launcher2
    window show
    fbt "Ого, я смотрю, ты нашёл секретный раздел! Поздравляю!"
    fbt "Теперь тебе, наверное, хочется узнать, что же здесь такое, не правда ли?"
    fbt "Ну что ж, я покажу тебе...{w} Но сначала немного предыстории."
    fbt "Данный фрагмент был разработан в конце 2015 года и был предложен мне для проверки и помощи в разработке."
    fbt "Но потом человек, разрабатывавший это перестал выходить на связь. Поискав по Летосфере, я нашёл его в составе одной, некогда почившей, но к тому моменту уже живой команды мододелов. Собственно, где-то после развала он и пришёл ко мне со своей идеей."
    fbt "Итак, мод был заморожен. Но некоторое время спустя, он ушёл из этой команды, но на связь не выходил. Если он и разрабатывает этот мод, то теперь без меня."
    fbt "Я же решил показать вам всё, что есть у меня по данному моду. Да, возможно, я поступаю весьма нечестно и нехорошо, но увы, я не собираюсь менять своего решения. Я заранее извиняюсь перед всеми моралфагами и перед тем разработчиком за использование сего материала."
    fbt "Итак, я представляю вам...{w} Ульяна-мод. День первый, часть первая."
    window hide
    stop music fadeout 2
    $ persistent.sl_m_not_fst_hidden = True
    jump uliana_mod_day1

label slavyana_mod__settings0:
    if hour in [22,23,24,0,1,2,3,4,5,6]:
        play music music_list["forest_maiden"] fadein 1
    elif hour in [20,21]:
        play music music_list["silhouette_in_sunset"] fadein 1
    elif hour in [7,8]:    
        play music music_list["lightness"] fadein 1
    else:
        play music music_list["a_promise_from_distant_days_v2"] fadein 1

label slavyana_mod__settings:
    if persistent.sl_m_hen_txt:
        if hour in [22,23,24,0,1,2,3,4,5,6]:
            scene bg set_night_yes with dissolve
            $ set_back = "scenario_slavyana/res/images/menu/bg/set_night_yes.png"
            $ set_back_hover = "scenario_slavyana/res/images/menu/bg/set_night_yes_hover.png"
        elif hour in [20,21] or hour in [7,8]:
            scene bg set_eve_yes with dissolve
            $ set_back = "scenario_slavyana/res/images/menu/bg/set_eve_yes.png"
            $ set_back_hover = "scenario_slavyana/res/images/menu/bg/set_eve_yes_hover.png"
        else:
            scene bg set_day_yes with dissolve
            $ set_back = "scenario_slavyana/res/images/menu/bg/set_day_yes.png"
            $ set_back_hover = "scenario_slavyana/res/images/menu/bg/set_day_yes_hover.png"
    else:
        if hour in [22,23,24,0,1,2,3,4,5,6]:
            scene bg set_night_no with dissolve
            $ set_back = "scenario_slavyana/res/images/menu/bg/set_night_no.png"
            $ set_back_hover = "scenario_slavyana/res/images/menu/bg/set_night_no_hover.png"
        elif hour in [20,21] or hour in [7,8]:
            scene bg set_eve_no with dissolve
            $ set_back = "scenario_slavyana/res/images/menu/bg/set_eve_no.png"
            $ set_back_hover = "scenario_slavyana/res/images/menu/bg/set_eve_no_hover.png"
        else:
            scene bg set_day_no with dissolve
            $ set_back = "scenario_slavyana/res/images/menu/bg/set_day_no.png"
            $ set_back_hover = "scenario_slavyana/res/images/menu/bg/set_day_no_hover.png"

label slavyana_mod__settings2:
    $ result = renpy.imagemap(set_back, set_back_hover, [
    (615, 399, 1303, 475, "delete_all"),
    (829, 573, 1084, 623, "autors"),
    (1375, 833, 1579, 1037, "hen_txt_sel"),
    (125, 857, 548, 1042, "back_set")
    ])

    if result == "back_set":
        jump slavyana_mod_launcher1_1
    elif result == "delete_all":
        if hour in [22,23,24,0,1,2,3,4,5,6]:
            scene bg ext_shed_night with dissolve
        elif hour in [20,21] or hour in [7,8]:
            scene bg ext_shed_sunset with dissolve
        else:
            scene bg ext_shed_day with dissolve
        window show
        "Вы уверены?"
        window hide
        menu:
            "Уверен":
                $ persistent.sl_m_day1 = False
                $ persistent.sl_m_day2 = False
                $ persistent.sl_m_day3 = False
                $ persistent.sl_m_hidden = False
                $ persistent.sl_m_not_fst_hidden = False
                $ sl_m_lp = 0
                jump slavyana_mod__settings
            "Нет, постойте!":
                jump slavyana_mod__settings
    elif result == "hen_txt_sel":
        if persistent.sl_m_hen_txt:
            $ persistent.sl_m_hen_txt = False
            if hour in [22,23,24,0,1,2,3,4,5,6]:
                $ set_back = "scenario_slavyana/res/images/menu/bg/set_night_no.png"
                $ set_back_hover = "scenario_slavyana/res/images/menu/bg/set_night_no_hover.png"
            elif hour in [20,21] or hour in [7,8]:
                $ set_back = "scenario_slavyana/res/images/menu/bg/set_eve_no.png"
                $ set_back_hover = "scenario_slavyana/res/images/menu/bg/set_eve_no_hover.png"
            else:
                $ set_back = "scenario_slavyana/res/images/menu/bg/set_day_no.png"
                $ set_back_hover = "scenario_slavyana/res/images/menu/bg/set_day_no_hover.png"
            jump slavyana_mod__settings2
        else:
            $ persistent.sl_m_hen_txt = True
            if hour in [22,23,24,0,1,2,3,4,5,6]:
                $ set_back = "scenario_slavyana/res/images/menu/bg/set_night_yes.png"
                $ set_back_hover = "scenario_slavyana/res/images/menu/bg/set_night_yes_hover.png"
            elif hour in [20,21] or hour in [7,8]:
                $ set_back = "scenario_slavyana/res/images/menu/bg/set_eve_yes.png"
                $ set_back_hover = "scenario_slavyana/res/images/menu/bg/set_eve_yes_hover.png"
            else:
                $ set_back = "scenario_slavyana/res/images/menu/bg/set_day_yes.png"
                $ set_back_hover = "scenario_slavyana/res/images/menu/bg/set_day_yes_hover.png"
            jump slavyana_mod__settings2
    elif result == "autors":
        stop music fadeout 2
        #написать титры здесь, потом сделать нормальные и перекинуть в эпилог
        scene black with dissolve2
        $ renpy.pause(2, hard=True)
        play music music_list["a_promise_from_distant_days"] fadein 3
        $ renpy.show('credits_sl_m credits_sl_m_text', [sl_m_ending_transform], layer='widgetoverlay')
        show cg d1_sl_dinner_0 behind credits with dissolve2
        $ renpy.pause(60, hard=True)  
        stop music fadeout 3
        scene black with dissolve2
        $ renpy.hide('credits_sl_m credits_sl_m_text', layer='widgetoverlay')
        jump slavyana_mod__settings0

#Сделано FireBoTer'ом
#Дизайн - Nenver Kradovich, FireBoTer