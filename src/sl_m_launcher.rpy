init python:
    mods["slavyana_mod__launcher"] = u"Славя-мод"
    try:
        mod_tags["slavyana_mod__launcher"] = ["gameplay:vn","length:days","protagonist:female","character:Семён","character:Славя","character:Алиса","character:Ульяна","character:Лена","character:Ольга Дмитриевна","character:Виола","character:Электроник","character:Шурик","character:Женя"]
    except NameError:
        pass

init:
    $ sl_m_Full = True
    $ sl_m_l_day = 0
    $ slavyana_mod_menu_state = "main"
    $ sl_m_lp = 0

    default persistent.sl_m_hen_txt = True
    default persistent.sl_m_end_count = 0

screen slavyana_mod_lp_counter():
    text "ЛП: [sl_m_lp]" xalign 0.0 yalign 0.0 size 16

# Главное меню мода
screen slavyana_mod_main_menu():
    tag menu
    modal True

    if slavyana_mod_menu_state == "main":
        add "scenario_slavyana/res/images/menu/bg/slavya-mod-title-screen.png"

        text "Build: 10.08.2026":
            xpos 0.0
            ypos 1.0
            xanchor 0.0
            yanchor 1.0
            xoffset 20
            yoffset -20
            size 16
            color "#ffffff80"
            outlines [ (1, "#000000a0", 0, 0) ]
        imagebutton:
            xalign 0.5
            ypos 0.6
            yanchor 1.0
            yoffset -100
            idle "scenario_slavyana/res/images/menu/buttons/play.png"
            hover "scenario_slavyana/res/images/menu/buttons/play_hover.png"
            action Return("play")
        imagebutton:
            xalign 0.5
            ypos 0.6
            yanchor 0.5
            idle "scenario_slavyana/res/images/menu/buttons/select_day.png"
            hover "scenario_slavyana/res/images/menu/buttons/select_day_hover.png"
            action SetVariable("slavyana_mod_menu_state", "days") 
        imagebutton:
            xalign 0.5
            ypos 0.6
            yanchor 0.0
            yoffset 100
            idle "scenario_slavyana/res/images/menu/buttons/titles.png"
            hover "scenario_slavyana/res/images/menu/buttons/titles_hover.png"
            action Return("authors")
        imagebutton:
            xpos 1.0
            xanchor 1.0
            xoffset -20
            ypos 1.0
            yanchor 1.0
            yoffset -20
            idle "scenario_slavyana/res/images/menu/buttons/age_off.png"
            hover "scenario_slavyana/res/images/menu/buttons/age_off_hover.png"
            selected_idle "scenario_slavyana/res/images/menu/buttons/age_on.png"
            selected_hover "scenario_slavyana/res/images/menu/buttons/age_on_hover.png"
            selected persistent.sl_m_hen_txt
            action ToggleVariable("persistent.sl_m_hen_txt")
        imagebutton:
            xpos 1.0
            xanchor 1.0
            xoffset -20
            ypos 1.0
            yanchor 1.0
            yoffset -120
            idle "scenario_slavyana/res/images/menu/buttons/basket.png"
            hover "scenario_slavyana/res/images/menu/buttons/basket_hover.png"
            action Return("wipe")
    elif slavyana_mod_menu_state == "days":
        add "scenario_slavyana/res/images/menu/bg/gal_eve.png"

        grid 3 3:
            xalign 0.5
            yalign 0.4
            spacing 30

            imagebutton:
                idle "scenario_slavyana/res/images/menu/day_buttons/day_1.png"
                hover "scenario_slavyana/res/images/menu/day_buttons/day_1_hover.png"
                action Return("day1")
            imagebutton:
                idle "scenario_slavyana/res/images/menu/day_buttons/day_2.png"
                hover "scenario_slavyana/res/images/menu/day_buttons/day_2_hover.png"
                action Return("day2")
            imagebutton:
                idle "scenario_slavyana/res/images/menu/day_buttons/day_3.png"
                hover "scenario_slavyana/res/images/menu/day_buttons/day_3_hover.png"
                action Return("day3")
            imagebutton:
                idle "scenario_slavyana/res/images/menu/day_buttons/day_4.png"
                hover "scenario_slavyana/res/images/menu/day_buttons/day_4_hover.png"
                action Return("day4")
            imagebutton:
                idle "scenario_slavyana/res/images/menu/day_buttons/day_5.png"
                hover "scenario_slavyana/res/images/menu/day_buttons/day_5_hover.png"
                action Return("day5")
            imagebutton:
                idle "scenario_slavyana/res/images/menu/day_buttons/day_6.png"
                hover "scenario_slavyana/res/images/menu/day_buttons/day_6_hover.png"
                action Return("day6")
            imagebutton:
                idle "scenario_slavyana/res/images/menu/day_buttons/day_7.png"
                hover "scenario_slavyana/res/images/menu/day_buttons/day_7_hover.png"
                action Return("day7")
            imagebutton:
                idle "scenario_slavyana/res/images/menu/day_buttons/epilogue.png"
                hover "scenario_slavyana/res/images/menu/day_buttons/epilogue_hover.png"
                action Return("epilogue")
            null
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
    else:
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
label slavyana_mod__launcher:
    $ new_chapter(0, u"Славя-мод")

# Инициализировать главный экран
label slavyana_mod__launcher0:
    $ reload_names()
    hide slavyana_mod__notebook_interface
    $ sl_m_nb_clear()
    scene black
    play music music_list["forest_maiden"] fadein 1
    show screen slavyana_mod_lp_counter

# Показать главный экран
label slavyana_mod__mainscreen1:
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
        stop music fadeout 2
        scene bg days_day
        $ renpy.pause(2, hard=True)
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
                $ persistent.endings["sl_m_green"] = False
                $ persistent.endings["sl_m_red"] = False
                $ persistent.endings["sl_m_blue"] = False
                $ persistent.sl_m_end_count = 0
                $ sl_m_lp = 0
            "Нет, постойте!":
                pass
        jump slavyana_mod__mainscreen1
    # Быстрый старт дней
    elif _return == "day1":
        $ sl_m_l_day = 1
        call slavyana_mod__l_finish
        jump slavyana_mod__day1
    elif _return == "day2":
        $ sl_m_l_day = 2
        call slavyana_mod__l_finish
        jump slavyana_mod__day1_fast_choice
    elif _return == "day3":
        $ sl_m_l_day = 3
        call slavyana_mod__l_finish
        jump slavyana_mod__day1_fast_choice
    elif _return == "day4":
        $ sl_m_l_day = 4
        call slavyana_mod__l_finish
        jump slavyana_mod__day1_fast_choice
    elif _return == "day5":
        $ sl_m_l_day = 5
        call slavyana_mod__l_finish
        jump slavyana_mod__day1_fast_choice
    elif _return == "day6":
        $ sl_m_l_day = 6
        call slavyana_mod__l_finish
        jump slavyana_mod__day1_fast_choice
    elif _return == "day7":
        $ sl_m_l_day = 7
        call slavyana_mod__l_finish
        jump slavyana_mod__day1_fast_choice
    elif _return == "epilogue":
        $ sl_m_l_day = 8
        call slavyana_mod__l_finish
        jump slavyana_mod__day1_fast_choice
    else:
        jump slavyana_mod__mainscreen1
    return

label slavyana_mod__l_finish:
    scene bg days_eve
    window show
    if sl_m_l_day <= 7:
        "Вернуться в меню по окончанию дня?"
        window hide
        menu:
            "Играть до конца":
                $ sl_m_Full = True
            "После дня вернуться в меню":
                $ sl_m_Full = False
        window show
    if sl_m_l_day > 1:
        $ mt_name = 'Оля'
        $ me_name = 'Семён'
    window hide
    stop music fadeout 2
    return
