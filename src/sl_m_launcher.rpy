init python:
    mods["slavyana_mod"] = u"Славя-мод"
    try:
        mod_tags["slavyana_mod"] = ["gameplay:vn","length:days","protagonist:female","character:Семён","character:Славя","character:Алиса","character:Ульяна","character:Лена","character:Ольга Дмитриевна","character:Виола","character:Электроник","character:Шурик","character:Женя"]
    except NameError:
        pass

screen slavyana_mod_lp_counter():
    text "ЛП: [sl_m_lp]" xalign 0.0 yalign 0.0 size 16

# Главное меню мода
screen slavyana_mod_main_menu():
    tag menu
    modal True

    if slavyana_mod_menu_state == "main":
        add "scenario_slavyana/res/images/menu/bg/slavya-mod-title-screen.png"

        text "Build: 25.09.2026":
            xpos 0.0
            ypos 1.0
            xanchor 0.0
            yanchor 1.0
            xoffset 20
            yoffset -20
            size 16
            color "#ffffff80"
            outlines [ (1, "#000000a0", 0, 0) ]
        vbox:
            xalign 0.5
            yalign 0.5
            ypos 0.6
            spacing 20

            imagebutton:
                idle "scenario_slavyana/res/images/menu/buttons/play.png"
                hover "scenario_slavyana/res/images/menu/buttons/play_hover.png"
                action Return("play")
            imagebutton:
                idle "scenario_slavyana/res/images/menu/buttons/select_day.png"
                hover "scenario_slavyana/res/images/menu/buttons/select_day_hover.png"
                action SetVariable("slavyana_mod_menu_state", "days") 
            imagebutton:
                idle "scenario_slavyana/res/images/menu/buttons/achievements.png"
                hover "scenario_slavyana/res/images/menu/buttons/achievements_hover.png"
                action SetVariable("slavyana_mod_menu_state", "achievements") 
            imagebutton:
                idle "scenario_slavyana/res/images/menu/buttons/titles.png"
                hover "scenario_slavyana/res/images/menu/buttons/titles_hover.png"
                action Return("authors")
        vbox:
            xanchor 1.0
            yanchor 1.0
            xpos 1.0
            ypos 1.0
            xoffset -20
            yoffset -20
            spacing 5

            imagebutton:
                idle "scenario_slavyana/res/images/menu/buttons/basket.png"
                hover "scenario_slavyana/res/images/menu/buttons/basket_hover.png"
                action Return("wipe")
            imagebutton:
                idle "scenario_slavyana/res/images/menu/buttons/age_off.png"
                hover "scenario_slavyana/res/images/menu/buttons/age_off_hover.png"
                selected_idle "scenario_slavyana/res/images/menu/buttons/age_on.png"
                selected_hover "scenario_slavyana/res/images/menu/buttons/age_on_hover.png"
                selected sl_m_hentai
                action ToggleVariable("sl_m_hentai")

    elif slavyana_mod_menu_state == "days":
        add "scenario_slavyana/res/images/menu/bg/gal_eve.png"

        grid 3 3:
            xalign 0.5
            yalign 0.45
            spacing 30

            for i in range(9):
                if i < 6:
                    imagebutton:
                        idle "scenario_slavyana/res/images/menu/day_buttons/day_"+str(i+2)+".png"
                        hover "scenario_slavyana/res/images/menu/day_buttons/day_"+str(i+2)+"_hover.png"
                        action Return("day"+str(i+2))
                elif i == 7:
                    imagebutton:
                        idle "scenario_slavyana/res/images/menu/day_buttons/epilogue.png"
                        hover "scenario_slavyana/res/images/menu/day_buttons/epilogue_hover.png"
                        action Return("epilogue")
                else:
                    null

    elif slavyana_mod_menu_state == "achievements":
        add "scenario_slavyana/res/images/menu/bg/gal_day.png"
        grid 3 3:
            xalign 0.5
            yalign 0.45
            spacing 30

            for i,name in enumerate([
                "green", "red", "blue",
                "solo", "solo_dv", "solo_un",
                False, "solo_us", False
            ]):
                if name == False:
                    null
                elif i == 7 and ((persistent.slavyana_mod_progress or 0) & (1 << 6)):
                    add "scenario_slavyana/res/images/achievement/achievement_" + name + ".png"
                elif (persistent.slavyana_mod_progress or 0) & (1 << i):
                    add "scenario_slavyana/res/images/achievement/achievement_" + name + ".png"
                else:
                    add "scenario_slavyana/res/images/achievement/achievement_locked.png"

    if slavyana_mod_menu_state != "main":
        imagebutton:
            xpos 0.0
            ypos 1.0
            xanchor 0.0
            yanchor 1.0
            xoffset 40
            yoffset -40
            idle "scenario_slavyana/res/images/menu/day_buttons/arrow.png"
            hover "scenario_slavyana/res/images/menu/day_buttons/arrow_active.png"
            action SetVariable("slavyana_mod_menu_state", "main")

# Точка входа в мод
label slavyana_mod:
    python:
        new_chapter(0, u"Славя-мод")
        reload_names()
        sl_m_nb_init()

        # Концовки мода
        Routes = object()
        Routes.Green  = 0
        Routes.Red    = 1
        Routes.Blue   = 2
        Routes.Solo   = 3
        Routes.SoloDV = 4
        Routes.SoloUN = 5
        Routes.SoloUS = 6

        # Текущая концовка
        current_route = 0

    

    scene black
    play music music_list["forest_maiden"] fadein 1
    show screen slavyana_mod_lp_counter

# Главный экран мода
label slavyana_mod__mainscreen:
    python:
        slavyana_mod_menu_state = "main"
        sl_m_lp = 0
        sl_m_hentai = False

    call screen slavyana_mod_main_menu

    # Новая игра
    if _return == "play":
        scene image "scenario_slavyana/res/images/menu/bg/slavya-mod-title-screen.png"
        window hide
        stop music fadeout 2
        play sound sfx_konami_on volume 0.1
        scene black with dissolve2
        jump slavyana_mod__day1
    # Авторы
    elif _return == "authors":
        scene image "scenario_slavyana/res/images/menu/bg/slavya-mod-title-screen.png"
        window hide
        stop music fadeout 2
        scene bg days_day with dissolve2
        play music music_list["lightness_radio_bus"] fadein 3
        jump slavyana_mod__credits
    # Вайп настроек мода
    elif _return == "wipe":
        scene bg ext_shed_sunset
        window show
        "Вы уверены, что хотите сбрость весь прогресс мода?"
        window hide
        menu:
            "Уверен. С глаз долой, из сердца ВОООН!":
                python:
                    sl_m_lp = 0
                    if (persistent.slavyana_mod_progress or None) is not None:
                        persistent.__dict__.pop("slavyana_mod_progress", None)

            "Нет, постойте!":
                pass
        jump slavyana_mod__mainscreen
    # Быстрый старт дней
    elif _return == "day2":
        $ sl_m_l_day = 2
        call slavyana_mod__fast_choice_init
        jump slavyana_mod__day1_fast_choice
    elif _return == "day3":
        $ sl_m_l_day = 3
        call slavyana_mod__fast_choice_init
        jump slavyana_mod__day1_fast_choice
    elif _return == "day4":
        $ sl_m_l_day = 4
        call slavyana_mod__fast_choice_init
        jump slavyana_mod__day1_fast_choice
    elif _return == "day5":
        $ sl_m_l_day = 5
        call slavyana_mod__fast_choice_init
        jump slavyana_mod__day1_fast_choice
    elif _return == "day6":
        $ sl_m_l_day = 6
        call slavyana_mod__fast_choice_init
        jump slavyana_mod__day1_fast_choice
    elif _return == "day7":
        $ sl_m_l_day = 7
        call slavyana_mod__fast_choice_init
        jump slavyana_mod__day1_fast_choice
    elif _return == "epilogue":
        $ sl_m_l_day = 8
        call slavyana_mod__fast_choice_init
        jump slavyana_mod__day1_fast_choice
    else:
        jump slavyana_mod__mainscreen
    return

# Настройки, перед скачком к дню
label slavyana_mod__fast_choice_init:
    $ mt_name = 'Оля'
    $ me_name = 'Семён'
    stop music fadeout 2
    return
