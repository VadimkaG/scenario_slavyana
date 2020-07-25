init:
    $ sl_m_bknt = 0
    if persistent.sl_m_bknt1 == None:
        $ persistent.sl_m_bknt1 = False
    if persistent.sl_m_bknt2 == None:
        $ persistent.sl_m_bknt2 = False
    if persistent.sl_m_bknt3 == None:
        $ persistent.sl_m_bknt3 = False
    if persistent.sl_m_bknt4 == None:
        $ persistent.sl_m_bknt4 = False
    if persistent.sl_m_bknt4_1 == None:
        $ persistent.sl_m_bknt4_1 = False
    if persistent.sl_m_bknt4_2_1 == None:
        $ persistent.sl_m_bknt4_2_1 = False
    if persistent.sl_m_bknt4_2_2 == None:
        $ persistent.sl_m_bknt4_2_2 = False
    if persistent.sl_m_bknt5 == None:
        $ persistent.sl_m_bknt5 = False
    if persistent.sl_m_bknt5_1_1 == None:
        $ persistent.sl_m_bknt5_1_1 = False
    if persistent.sl_m_bknt5_1_2 == None:
        $ persistent.sl_m_bknt5_1_2 = False
    if persistent.sl_m_bknt5_2 == None:
        $ persistent.sl_m_bknt5_2 = False
    if persistent.sl_m_bknt6_1 == None:
        $ persistent.sl_m_bknt6_1 = False
    if persistent.sl_m_bknt6_1_2 == None:
        $ persistent.sl_m_bknt6_1_2 = False
    if persistent.sl_m_bknt6_1_1_1 == None:
        $ persistent.sl_m_bknt6_1_1_1 = False
    if persistent.sl_m_bknt6_1_1_2 == None:
        $ persistent.sl_m_bknt6_1_1_2 = False
    if persistent.sl_m_bknt6_2 == None:
        $ persistent.sl_m_bknt6_2 = False
    if persistent.sl_m_bknt6_2_1_1 == None:
        $ persistent.sl_m_bknt6_2_1_1 = False
    if persistent.sl_m_bknt6_2_1_2 == None:
        $ persistent.sl_m_bknt6_2_1_2 = False
    if persistent.sl_m_bknt6_2_2 == None:
        $ persistent.sl_m_bknt6_2_2 = False
    if persistent.sl_m_bknt7_1 == None:
        $ persistent.sl_m_bknt7_1 = False
    if persistent.sl_m_bknt7_1_2 == None:
        $ persistent.sl_m_bknt7_1_2 = False
    if persistent.sl_m_bknt7_1_1_1 == None:
        $ persistent.sl_m_bknt7_1_1_1 = False
    if persistent.sl_m_bknt7_1_1_2 == None:
        $ persistent.sl_m_bknt7_1_1_2 = False
    if persistent.sl_m_bknt7_2 == None:
        $ persistent.sl_m_bknt7_2 = False
    if persistent.sl_m_bknt7_2_1_1 == None:
        $ persistent.sl_m_bknt7_2_1_1 = False
    if persistent.sl_m_bknt7_2_1_2 == None:
        $ persistent.sl_m_bknt7_2_1_2 = False
    if persistent.sl_m_bknt7_2_2 == None:
        $ persistent.sl_m_bknt7_2_2 = False
    if persistent.sl_m_bknt8 == None:
        $ persistent.sl_m_bknt8 = False
    if persistent.sl_m_bknt9 == None:
        $ persistent.sl_m_bknt9 = False

    $ persistent.sl_m_bknt_sc1 = False
    $ persistent.sl_m_bknt_sc2 = False
    $ persistent.sl_m_bknt_sc3 = False
    $ persistent.sl_m_bknt_sc4 = False

label slavyana_mod__bknt_gallery:
    if hour in [22,23,24,0,1,2,3,4,5,6]:
        scene bg gal_night with dissolve
    elif hour in [20,21] or hour in [7,8]:
        scene bg gal_eve with dissolve
    else:
        scene bg gal_day with dissolve

label slavyana_mod__bknt_gallery1:
    $ persistent.sl_m_bknt_sc1 = True
    $ persistent.sl_m_bknt_sc2 = False
    $ persistent.sl_m_bknt_sc3 = False
    $ persistent.sl_m_bknt_sc4 = False
    python:
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/gal_back.png', 'scenario_slavyana/res/images/menu/gallery/gal_back_hover.png', clicked=ui.returns('exit_bknt'), align=(0.01, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/st_forward.png', 'scenario_slavyana/res/images/menu/gallery/st_forward_hover.png', clicked=ui.returns('fw_bknt'), align=(0.99, 0.5))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/one_highlight.png', 'scenario_slavyana/res/images/menu/gallery/one_highlight.png', clicked=ui.returns('not_opened'), align=(0.3, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/two.png', 'scenario_slavyana/res/images/menu/gallery/two_hover.png', clicked=ui.returns('scnd_sc'), align=(0.4, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/three.png', 'scenario_slavyana/res/images/menu/gallery/three_hover.png', clicked=ui.returns('thd_sc'), align=(0.5, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/fourth.png', 'scenario_slavyana/res/images/menu/gallery/fourth_hover.png', clicked=ui.returns('fth_sc'), align=(0.6, 0.97))
        if persistent.sl_m_bknt1:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt1.png", "scenario_slavyana/res/images/menu/bknt_small/bknt1.png", clicked=ui.returns('bknt_w1'), align=(0.2, 0.15))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.2, 0.15))
        if persistent.sl_m_bknt2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt2.png", clicked=ui.returns('bknt_w2'), align=(0.5, 0.15))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.5, 0.15))
        if persistent.sl_m_bknt3:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt3.png", "scenario_slavyana/res/images/menu/bknt_small/bknt3.png", clicked=ui.returns('bknt_w3'), align=(0.8, 0.15))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.8, 0.15))
        if persistent.sl_m_bknt4:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt4.png", "scenario_slavyana/res/images/menu/bknt_small/bknt4.png", clicked=ui.returns('bknt_w4'), align=(0.2, 0.45))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.2, 0.45))
        if persistent.sl_m_bknt4_1:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt4_1.png", "scenario_slavyana/res/images/menu/bknt_small/bknt4_1.png", clicked=ui.returns('bknt_w4_1'), align=(0.5, 0.45))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.5, 0.45))
        if persistent.sl_m_bknt4_2_1:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt4_2_1.png", "scenario_slavyana/res/images/menu/bknt_small/bknt4_2_1.png", clicked=ui.returns('bknt_w4_2_1'), align=(0.8, 0.45))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.8, 0.45))
        if persistent.sl_m_bknt4_2_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt4_2_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt4_2_2.png", clicked=ui.returns('bknt_w4_2_2'), align=(0.2, 0.75))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.2, 0.75))
        if persistent.sl_m_bknt5:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt5.png", "scenario_slavyana/res/images/menu/bknt_small/bknt5.png", clicked=ui.returns('bknt_w5'), align=(0.5, 0.75))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.5, 0.75))
        if persistent.sl_m_bknt5_1_1:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt5_1_1.png", "scenario_slavyana/res/images/menu/bknt_small/bknt5_1_1.png", clicked=ui.returns('bknt_w5_1_1'), align=(0.8, 0.75))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.8, 0.75))
        result = ui.interact()

    if result == "exit_bknt":
        jump slavyana_mod_launcher1_1
    elif result == "fw_bknt":
        jump slavyana_mod__bknt_gallery_sc2
    elif result == "scnd_sc":
        jump slavyana_mod__bknt_gallery_sc2
    elif result == "thd_sc":
        jump slavyana_mod__bknt_gallery_sc3
    elif result == "fth_sc":
        jump slavyana_mod__bknt_gallery_sc4
    elif result == "not_opened":
        jump slavyana_mod__bknt_gallery1
    elif result == "bknt_w1":
        $ sl_m_bknt = 1
        jump slavyana_mod_bknt_show
    elif result == "bknt_w2":
        $ sl_m_bknt = 2
        jump slavyana_mod_bknt_show
    elif result == "bknt_w3":
        $ sl_m_bknt = 3
        jump slavyana_mod_bknt_show
    elif result == "bknt_w4":
        $ sl_m_bknt = 4
        jump slavyana_mod_bknt_show
    elif result == "bknt_w4_1":
        $ sl_m_bknt = 410
        jump slavyana_mod_bknt_show
    elif result == "bknt_w4_2_1":
        $ sl_m_bknt = 421
        jump slavyana_mod_bknt_show
    elif result == "bknt_w4_2_2":
        $ sl_m_bknt = 422
        jump slavyana_mod_bknt_show
    elif result == "bknt_w5":
        $ sl_m_bknt = 5
        jump slavyana_mod_bknt_show
    elif result == "bknt_w5_1_1":
        $ sl_m_bknt = 511
        jump slavyana_mod_bknt_show

label slavyana_mod__bknt_gallery_sc2:
    $ persistent.sl_m_bknt_sc1 = False
    $ persistent.sl_m_bknt_sc2 = True
    $ persistent.sl_m_bknt_sc3 = False
    $ persistent.sl_m_bknt_sc4 = False
    python:
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/gal_back.png', 'scenario_slavyana/res/images/menu/gallery/gal_back_hover.png', clicked=ui.returns('exit_bknt'), align=(0.01, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/st_forward.png', 'scenario_slavyana/res/images/menu/gallery/st_forward_hover.png', clicked=ui.returns('fw_bknt'), align=(0.99, 0.5))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/st_back.png', 'scenario_slavyana/res/images/menu/gallery/st_back_hover.png', clicked=ui.returns('back_bknt'), align=(0.01, 0.5))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/one.png', 'scenario_slavyana/res/images/menu/gallery/one_hover.png', clicked=ui.returns('fst_sc'), align=(0.3, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/two_highlight.png', 'scenario_slavyana/res/images/menu/gallery/two_highlight.png', clicked=ui.returns('not_opened'), align=(0.4, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/three.png', 'scenario_slavyana/res/images/menu/gallery/three_hover.png', clicked=ui.returns('thd_sc'), align=(0.5, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/fourth.png', 'scenario_slavyana/res/images/menu/gallery/fourth_hover.png', clicked=ui.returns('fth_sc'), align=(0.6, 0.97))
        if persistent.sl_m_bknt5_1_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt5_1_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt5_1_2.png", clicked=ui.returns('bknt_w5_1_2'), align=(0.2, 0.15))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.2, 0.15))
        if persistent.sl_m_bknt5_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt5_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt5_2.png", clicked=ui.returns('bknt_w5_2'), align=(0.5, 0.15))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.5, 0.15))
        if persistent.sl_m_bknt6_1:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt6_1.png", "scenario_slavyana/res/images/menu/bknt_small/bknt6_1.png", clicked=ui.returns('bknt_w6_1'), align=(0.8, 0.15))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.8, 0.15))
        if persistent.sl_m_bknt6_1_1_1:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt6_1_1_1.png", "scenario_slavyana/res/images/menu/bknt_small/bknt6_1_1_1.png", clicked=ui.returns('bknt_w6_1_1_1'), align=(0.2, 0.45))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.2, 0.45))
        if persistent.sl_m_bknt6_1_1_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt6_1_1_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt6_1_1_2.png", clicked=ui.returns('bknt_w6_1_1_2'), align=(0.5, 0.45))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.5, 0.45))
        if persistent.sl_m_bknt6_1_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt6_1_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt6_1_2.png", clicked=ui.returns('bknt_w6_1_2'), align=(0.8, 0.45))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.8, 0.45))
        if persistent.sl_m_bknt6_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt6_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt6_2.png", clicked=ui.returns('bknt_w6_2'), align=(0.2, 0.75))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.2, 0.75))
        if persistent.sl_m_bknt6_2_1_1:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt6_2_1_1.png", "scenario_slavyana/res/images/menu/bknt_small/bknt6_2_1_1.png", clicked=ui.returns('bknt_w6_2_1_1'), align=(0.5, 0.75))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.5, 0.75))
        if persistent.sl_m_bknt6_2_1_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt6_2_1_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt6_2_1_2.png", clicked=ui.returns('bknt_w6_2_1_2'), align=(0.8, 0.75))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.8, 0.75))
        result = ui.interact()

    if result == "back_bknt":
        jump slavyana_mod__bknt_gallery1
    elif result == "exit_bknt":
        jump slavyana_mod_launcher1_1
    elif result == "fw_bknt":
        jump slavyana_mod__bknt_gallery_sc3
    elif result == "fst_sc":
        jump slavyana_mod__bknt_gallery1
    elif result == "thd_sc":
        jump slavyana_mod__bknt_gallery_sc3
    elif result == "fth_sc":
        jump slavyana_mod__bknt_gallery_sc4
    elif result == "not_opened":
        jump slavyana_mod__bknt_gallery_sc2
    elif result == "bknt_w5_1_2":
        $ sl_m_bknt = 512
        jump slavyana_mod_bknt_show
    elif result == "bknt_w5_2":
        $ sl_m_bknt = 520
        jump slavyana_mod_bknt_show
    elif result == "bknt_w6_1":
        $ sl_m_bknt = 610
        jump slavyana_mod_bknt_show
    elif result == "bknt_w6_1_1_1":
        $ sl_m_bknt = 6111
        jump slavyana_mod_bknt_show
    elif result == "bknt_w6_1_1_2":
        $ sl_m_bknt = 6112
        jump slavyana_mod_bknt_show
    elif result == "bknt_w6_1_2":
        $ sl_m_bknt = 612
        jump slavyana_mod_bknt_show
    elif result == "bknt_w6_2":
        $ sl_m_bknt = 620
        jump slavyana_mod_bknt_show
    elif result == "bknt_w6_2_1_1":
        $ sl_m_bknt = 6211
        jump slavyana_mod_bknt_show
    elif result == "bknt_w6_2_1_2":
        $ sl_m_bknt = 6212
        jump slavyana_mod_bknt_show

label slavyana_mod__bknt_gallery_sc3:
    $ persistent.sl_m_bknt_sc1 = False
    $ persistent.sl_m_bknt_sc2 = False
    $ persistent.sl_m_bknt_sc3 = True
    $ persistent.sl_m_bknt_sc4 = False
    python:
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/gal_back.png', 'scenario_slavyana/res/images/menu/gallery/gal_back_hover.png', clicked=ui.returns('exit_bknt'), align=(0.01, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/st_forward.png', 'scenario_slavyana/res/images/menu/gallery/st_forward_hover.png', clicked=ui.returns('fw_bknt'), align=(0.99, 0.5))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/st_back.png', 'scenario_slavyana/res/images/menu/gallery/st_back_hover.png', clicked=ui.returns('back_bknt'), align=(0.01, 0.5))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/one.png', 'scenario_slavyana/res/images/menu/gallery/one_hover.png', clicked=ui.returns('fst_sc'), align=(0.3, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/two.png', 'scenario_slavyana/res/images/menu/gallery/two_hover.png', clicked=ui.returns('scnd_sc'), align=(0.4, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/fourth.png', 'scenario_slavyana/res/images/menu/gallery/fourth_hover.png', clicked=ui.returns('fth_sc'), align=(0.6, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/three_highlight.png', 'scenario_slavyana/res/images/menu/gallery/three_highlight.png', clicked=ui.returns('not_opened'), align=(0.5, 0.97))
        if persistent.sl_m_bknt6_2_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt6_2_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt6_2_2.png", clicked=ui.returns('bknt_w6_2_2'), align=(0.2, 0.15))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.2, 0.15))
        if persistent.sl_m_bknt7_1:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt7_1.png", "scenario_slavyana/res/images/menu/bknt_small/bknt7_1.png", clicked=ui.returns('bknt_w7_1'), align=(0.5, 0.15))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.5, 0.15))
        if persistent.sl_m_bknt7_1_1_1:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt7_1_1_1.png", "scenario_slavyana/res/images/menu/bknt_small/bknt7_1_1_1.png", clicked=ui.returns('bknt_w7_1_1_1'), align=(0.8, 0.15))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.8, 0.15))
        if persistent.sl_m_bknt7_1_1_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt7_1_1_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt7_1_1_2.png", clicked=ui.returns('bknt_w7_1_1_2'), align=(0.2, 0.45))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.2, 0.45))
        if persistent.sl_m_bknt7_1_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt7_1_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt7_1_2.png", clicked=ui.returns('bknt_w7_1_2'), align=(0.5, 0.45))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.5, 0.45))
        if persistent.sl_m_bknt7_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt7_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt7_2.png", clicked=ui.returns('bknt_w7_2'), align=(0.8, 0.45))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.8, 0.45))
        if persistent.sl_m_bknt7_2_1_1:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt7_2_1_1.png", "scenario_slavyana/res/images/menu/bknt_small/bknt7_2_1_1.png", clicked=ui.returns('bknt_w7_2_1_1'), align=(0.2, 0.75))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.2, 0.75))
        if persistent.sl_m_bknt7_2_1_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt7_2_1_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt7_2_1_2.png", clicked=ui.returns('bknt_w7_2_1_2'), align=(0.5, 0.75))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.5, 0.75))
        if persistent.sl_m_bknt7_2_2:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt7_2_2.png", "scenario_slavyana/res/images/menu/bknt_small/bknt7_2_2.png", clicked=ui.returns('bknt_w7_2_2'), align=(0.8, 0.75))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.8, 0.75))
        result = ui.interact()

    if result == "back_bknt":
        jump slavyana_mod__bknt_gallery_sc2
    elif result == "exit_bknt":
        jump slavyana_mod_launcher1_1
    elif result == "fw_bknt":
        jump slavyana_mod__bknt_gallery_sc4
    elif result == "fst_sc":
        jump slavyana_mod__bknt_gallery1
    elif result == "scnd_sc":
        jump slavyana_mod__bknt_gallery_sc2
    elif result == "fth_sc":
        jump slavyana_mod__bknt_gallery_sc4
    elif result == "not_opened":
        jump slavyana_mod__bknt_gallery_sc3
    elif result == "bknt_w6_2_2":
        $ sl_m_bknt = 622
        jump slavyana_mod_bknt_show
    elif result == "bknt_w7_1":
        $ sl_m_bknt = 710
        jump slavyana_mod_bknt_show
    elif result == "bknt_w7_1_1_1":
        $ sl_m_bknt = 7111
        jump slavyana_mod_bknt_show
    elif result == "bknt_w7_1_1_2":
        $ sl_m_bknt = 7112
        jump slavyana_mod_bknt_show
    elif result == "bknt_w7_1_2":
        $ sl_m_bknt = 712
        jump slavyana_mod_bknt_show
    elif result == "bknt_w7_2":
        $ sl_m_bknt = 720
        jump slavyana_mod_bknt_show
    elif result == "bknt_w7_2_1_1":
        $ sl_m_bknt = 7211
        jump slavyana_mod_bknt_show
    elif result == "bknt_w7_2_1_2":
        $ sl_m_bknt = 7212
        jump slavyana_mod_bknt_show
    elif result == "bknt_w7_2_2":
        $ sl_m_bknt = 722
        jump slavyana_mod_bknt_show

label slavyana_mod__bknt_gallery_sc4:
    $ persistent.sl_m_bknt_sc1 = False
    $ persistent.sl_m_bknt_sc2 = False
    $ persistent.sl_m_bknt_sc3 = False
    $ persistent.sl_m_bknt_sc4 = True
    python:
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/gal_back.png', 'scenario_slavyana/res/images/menu/gallery/gal_back_hover.png', clicked=ui.returns('exit_bknt'), align=(0.01, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/st_back.png', 'scenario_slavyana/res/images/menu/gallery/st_back_hover.png', clicked=ui.returns('back_bknt'), align=(0.01, 0.5))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/one.png', 'scenario_slavyana/res/images/menu/gallery/one_hover.png', clicked=ui.returns('fst_sc'), align=(0.3, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/two.png', 'scenario_slavyana/res/images/menu/gallery/two_hover.png', clicked=ui.returns('scnd_sc'), align=(0.4, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/three.png', 'scenario_slavyana/res/images/menu/gallery/three_hover.png', clicked=ui.returns('thd_sc'), align=(0.5, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/fourth_highlight.png', 'scenario_slavyana/res/images/menu/gallery/fourth_highlight.png', clicked=ui.returns('not_opened'), align=(0.6, 0.97))
        if persistent.sl_m_bknt8:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt8.png", "scenario_slavyana/res/images/menu/bknt_small/bknt8.png", clicked=ui.returns('bknt_w8'), align=(0.2, 0.15))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.2, 0.15))
        if persistent.sl_m_bknt9:
            ui.imagebutton("scenario_slavyana/res/images/menu/bknt_small/bknt9.png", "scenario_slavyana/res/images/menu/bknt_small/bknt9.png", clicked=ui.returns('bknt_w9'), align=(0.5, 0.15))
        else:
            ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.5, 0.15))
        ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.8, 0.15))
        ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.2, 0.45))
        ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.5, 0.45))
        ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.8, 0.45))
        ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.2, 0.75))
        ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.5, 0.75))
        ui.imagebutton("scenario_slavyana/res/images/menu/gallery/not_opened_idle.png", "scenario_slavyana/res/images/menu/gallery/not_opened_hover.png", clicked=ui.returns('not_opened'), align=(0.8, 0.75))
        result = ui.interact()
    
    if result == "back_bknt":
        jump slavyana_mod__bknt_gallery_sc3
    elif result == "exit_bknt":
        jump slavyana_mod_launcher1_1
    elif result == "fst_sc":
        jump slavyana_mod__bknt_gallery1
    elif result == "scnd_sc":
        jump slavyana_mod__bknt_gallery_sc2
    elif result == "thd_sc":
        jump slavyana_mod__bknt_gallery_sc3
    elif result == "not_opened":
        jump slavyana_mod__bknt_gallery_sc4
    elif result == "bknt_w8":
        $ sl_m_bknt = 8
        jump slavyana_mod_bknt_show
    elif result == "bknt_w9":
        $ sl_m_bknt = 9
        jump slavyana_mod_bknt_show

label slavyana_mod_bknt_show:
    if sl_m_bknt == 1:
        show bknt_w1 at truecenter with dissolve
    elif sl_m_bknt == 2:
        show bknt_w2 at truecenter with dissolve
    elif sl_m_bknt == 3:
        show bknt_w3 at truecenter with dissolve
    elif sl_m_bknt == 4:
        show bknt_w4 at truecenter with dissolve
    elif sl_m_bknt == 410:
        show bknt_w4_1 at truecenter with dissolve
    elif sl_m_bknt == 421:
        show bknt_w4_2_1 at truecenter with dissolve
    elif sl_m_bknt == 422:
        show bknt_w4_2_2 at truecenter with dissolve
    elif sl_m_bknt == 5:
        show bknt_w5 at truecenter with dissolve
    elif sl_m_bknt == 511:
        show bknt_w5_1_1 at truecenter with dissolve
    elif sl_m_bknt == 512:
        show bknt_w5_1_2 at truecenter with dissolve
    elif sl_m_bknt == 520:
        show bknt_w5_2 at truecenter with dissolve
    elif sl_m_bknt == 610:
        show bknt_w6_1 at truecenter with dissolve
    elif sl_m_bknt == 6111:
        show bknt_w6_1_1_1 at truecenter with dissolve
    elif sl_m_bknt == 6112:
        show bknt_w6_1_1_2 at truecenter with dissolve
    elif sl_m_bknt == 612:
        show bknt_w6_1_2 at truecenter with dissolve
    elif sl_m_bknt == 620:
        show bknt_w6_2 at truecenter with dissolve
    elif sl_m_bknt == 6211:
        show bknt_w6_2_1_1 at truecenter with dissolve
    elif sl_m_bknt == 6212:
        show bknt_w6_2_1_2 at truecenter with dissolve
    elif sl_m_bknt == 622:
        show bknt_w6_2_2 at truecenter with dissolve
    elif sl_m_bknt == 710:
        show bknt_w7_1 at truecenter with dissolve
    elif sl_m_bknt == 7111:
        show bknt_w7_1_1_1 at truecenter with dissolve
    elif sl_m_bknt == 7112:
        show bknt_w7_1_1_2 at truecenter with dissolve
    elif sl_m_bknt == 712:
        show bknt_w7_1_2 at truecenter with dissolve
    elif sl_m_bknt == 720:
        show bknt_w7_2 at truecenter with dissolve
    elif sl_m_bknt == 7211:
        show bknt_w7_2_1_1 at truecenter with dissolve
    elif sl_m_bknt == 7212:
        show bknt_w7_2_1_2 at truecenter with dissolve
    elif sl_m_bknt == 722:
        show bknt_w7_2_2 at truecenter with dissolve
    elif sl_m_bknt == 8:
        show bknt_w8 at truecenter with dissolve
    elif sl_m_bknt == 9:
        show bknt_w9 at truecenter with dissolve
    python:
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/gal_back.png', 'scenario_slavyana/res/images/menu/gallery/gal_back_hover.png', clicked=ui.returns('back_bknt_small'), align=(0.01, 0.97))
        ui.imagebutton('scenario_slavyana/res/images/menu/gallery/text.png', 'scenario_slavyana/res/images/menu/gallery/text_hover.png', clicked=ui.returns('bknt_text_open'), align=(0.99, 0.95))
        result = ui.interact()
    if result == "back_bknt_small":
        hide bknt_w1
        hide bknt_w2
        hide bknt_w3
        hide bknt_w4
        hide bknt_w4_1
        hide bknt_w4_2_1
        hide bknt_w4_2_2
        hide bknt_w5
        hide bknt_w5_1_1
        hide bknt_w5_1_2
        hide bknt_w5_2
        hide bknt_w6_1
        hide bknt_w6_1_2
        hide bknt_w6_1_1_1
        hide bknt_w6_1_1_2
        hide bknt_w6_2
        hide bknt_w6_2_1_1
        hide bknt_w6_2_1_2
        hide bknt_w6_2_2
        hide bknt_w7_1
        hide bknt_w7_1_1_1
        hide bknt_w7_1_1_2
        hide bknt_w7_1_2
        hide bknt_w7_2
        hide bknt_w7_2_1_1
        hide bknt_w7_2_1_2
        hide bknt_w7_2_2
        hide bknt_w8
        hide bknt_w9
        with dissolve
        if persistent.sl_m_bknt_sc1:
            jump slavyana_mod__bknt_gallery1
        if persistent.sl_m_bknt_sc2:
            jump slavyana_mod__bknt_gallery_sc2
        if persistent.sl_m_bknt_sc3:
            jump slavyana_mod__bknt_gallery_sc3
        if persistent.sl_m_bknt_sc4:
            jump slavyana_mod__bknt_gallery_sc4
    elif result == "bknt_text_open":
        $ set_mode_nvl()
        window show
        if sl_m_bknt == 1:
            "Итак, мой восьмой день пребывания в Совёнке. Погода замечательная."
        elif sl_m_bknt == 2:
            "Итак, мой восьмой день пребывания в Совёнке. Погода замечательная.\nСегодня к нам заехал ещё один пионер (Семён), прямо посреди смены. Странно. Да и сам он какой-то... необычный, что ли. В зимней одежде, замкнутый, хотя, видно, не дурак. Поначалу был то ли напуган, то ли шокирован чем-то, но сейчас уже вроде понял, что вне опасности. Да и какая опасность может быть в пионерском лагере? Правильно, никакая. Здесь не зона военных действий, не граница с капиталистами, а всего лишь тихая глушь, затерянная среди лесов..."
        elif sl_m_bknt == 3:
            "Итак, мой восьмой день пребывания в Совёнке. Погода замечательная.\nСегодня к нам заехал ещё один пионер (Семён), прямо посреди смены. Странно. Да и сам он какой-то... необычный, что ли. В зимней одежде, замкнутый, хотя, видно, не дурак. Поначалу был то ли напуган, то ли шокирован чем-то, но сейчас уже вроде понял, что вне опасности. Да и какая опасность может быть в пионерском лагере? Правильно, никакая. Здесь не зона военных действий, не граница с капиталистами, а всего лишь тихая глушь, затерянная среди лесов...\nНа ужине Ульяна его разыграла (не знаю как) и Семён упал со стула, заодно разбив тарелку. Я пошла его искать, и чуть не заблудилась ночью в лесу. Хотя, там в это время так же красиво, как и днём, можно было бы ещё немного побродить... Найдя Семёна, я проводила его в столовую, лишний раз убедившись, в том, что он немного странный. Впрочем, может это только поначалу?"
        elif sl_m_bknt == 4:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи."
        elif sl_m_bknt == 410:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Я искала их по всему лагерю, но так и не нашла."
        elif sl_m_bknt == 421:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Благо, Семён мне их вечером отдал."
        elif sl_m_bknt == 422:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Я искала их по всему лагерю, но так и не нашла. Благо, Семён мне их вечером отдал."
        elif sl_m_bknt == 5:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря)."
        elif sl_m_bknt == 511:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Благо, Семён мне их вечером отдал.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря)."
        elif sl_m_bknt == 512:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Я искала их по всему лагерю, но так и не нашла. Благо, Семён мне их вечером отдал.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря)."
        elif sl_m_bknt == 520:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Я искала их по всему лагерю, но так и не нашла.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря)."
        elif sl_m_bknt == 610:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я выиграла у Жени. Но отдала ей свою победу, ведь она, кажется, расстроилась из-за проигрыша."
        elif sl_m_bknt == 6111:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Благо, Семён мне их вечером отдал.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я выиграла у Жени. Но отдала ей свою победу, ведь она, кажется, расстроилась из-за проигрыша."
        elif sl_m_bknt == 6112:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Я искала их по всему лагерю, но так и не нашла. Благо, Семён мне их вечером отдал.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я выиграла у Жени. Но отдала ей свою победу, ведь она, кажется, расстроилась из-за проигрыша."
        elif sl_m_bknt == 612:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Я искала их по всему лагерю, но так и не нашла.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я выиграла у Жени. Но отдала ей свою победу, ведь она, кажется, расстроилась из-за проигрыша."
        elif sl_m_bknt == 620:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я проиграла Жене. Ну что ж, не только же мне выигрывать."
        elif sl_m_bknt == 6211:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Благо, Семён мне их вечером отдал.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я проиграла Жене. Ну что ж, не только же мне выигрывать."
        elif sl_m_bknt == 6212:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Я искала их по всему лагерю, но так и не нашла. Благо, Семён мне их вечером отдал.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я проиграла Жене. Ну что ж, не только же мне выигрывать."
        elif sl_m_bknt == 622:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Я искала их по всему лагерю, но так и не нашла.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я проиграла Жене. Ну что ж, не только же мне выигрывать."
        elif sl_m_bknt == 710:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я выиграла у Жени. Но отдала ей свою победу, ведь она, кажется, расстроилась из-за проигрыша.\nПосле турнира я пошла в своё тайное место в лесу. Но... я привела с собой Семёна, который увидел... то, что не должен был. Я не знаю, что мне теперь делать и просто буду ждать."
        elif sl_m_bknt == 7111:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Благо, Семён мне их вечером отдал.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я выиграла у Жени. Но отдала ей свою победу, ведь она, кажется, расстроилась из-за проигрыша.\nПосле турнира я пошла в своё тайное место в лесу. Но... я привела с собой Семёна, который увидел... то, что не должен был. Я не знаю, что мне теперь делать и просто буду ждать."
        elif sl_m_bknt == 7112:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Я искала их по всему лагерю, но так и не нашла. Благо, Семён мне их вечером отдал.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я выиграла у Жени. Но отдала ей свою победу, ведь она, кажется, расстроилась из-за проигрыша.\nПосле турнира я пошла в своё тайное место в лесу. Но... я привела с собой Семёна, который увидел... то, что не должен был. Я не знаю, что мне теперь делать и просто буду ждать."
        elif sl_m_bknt == 712:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Я искала их по всему лагерю, но так и не нашла.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я выиграла у Жени. Но отдала ей свою победу, ведь она, кажется, расстроилась из-за проигрыша.\nПосле турнира я пошла в своё тайное место в лесу. Но... я привела с собой Семёна, который увидел... то, что не должен был. Я не знаю, что мне теперь делать и просто буду ждать."
        elif sl_m_bknt == 720:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я проиграла Жене. Ну что ж, не только же мне выигрывать.\nПосле турнира я пошла в своё тайное место в лесу. Но... я привела с собой Семёна, который увидел... то, что не должен был. Я не знаю, что мне теперь делать и просто буду ждать."
        elif sl_m_bknt == 7211:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Благо, Семён мне их вечером отдал.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я проиграла Жене. Ну что ж, не только же мне выигрывать.\nПосле турнира я пошла в своё тайное место в лесу. Но... я привела с собой Семёна, который увидел... то, что не должен был. Я не знаю, что мне теперь делать и просто буду ждать."
        elif sl_m_bknt == 7212:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Я искала их по всему лагерю, но так и не нашла. Благо, Семён мне их вечером отдал.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я проиграла Жене. Ну что ж, не только же мне выигрывать.\nПосле турнира я пошла в своё тайное место в лесу. Но... я привела с собой Семёна, который увидел... то, что не должен был. Я не знаю, что мне теперь делать и просто буду ждать."
        elif sl_m_bknt == 722:
            "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи. Я искала их по всему лагерю, но так и не нашла.\nПод вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря). А после ужина, на карточном турнире, я проиграла Жене. Ну что ж, не только же мне выигрывать.\nПосле турнира я пошла в своё тайное место в лесу. Но... я привела с собой Семёна, который увидел... то, что не должен был. Я не знаю, что мне теперь делать и просто буду ждать."
        elif sl_m_bknt == 8:
            "Десятый день в \"Совёнке\". День был трудным и насыщенным. Сначала я отнесла спирт (в виде водки – спасибо медсестре) кибернетикам, за что нас обсмеяла вездесущая Алиса. Потом руководила уборкой площади.\nПосле обеда я ловила сбегавшего от наказания Семёна. Зато он здорово помог мне в библиотеке. Вот только упал на меня в самом конце, но мы остались живы. Перед ужином Оля проявила неслыханное варварство: она хотела оставить Семёна без ужина. Но узнав, что он работал вместе со мной в библиотеке, отступилась (после того, как я поручилась за него). А ещё я помогала готовить дискотеку."
        elif sl_m_bknt == 9:
            "Десятый день в \"Совёнке\". День был трудным и насыщенным. Сначала я отнесла спирт (в виде водки – спасибо медсестре) кибернетикам, за что нас обсмеяла вездесущая Алиса. Потом руководила уборкой площади.\nПосле обеда я ловила сбегавшего от наказания Семёна. Зато он здорово помог мне в библиотеке. Вот только упал на меня в самом конце, но мы остались живы. Перед ужином Оля проявила неслыханное варварство: она хотела оставить Семёна без ужина. Но узнав, что он работал вместе со мной в библиотеке, отступилась (после того, как я поручилась за него). А ещё я помогала готовить дискотеку. Она прошла на славу. Я танцевала с Семёном, это было... замечательно. Я ощущала себя такой счастливой...\nПравда, потом он совершенно неучтиво убежал. Нашла я его на пляже, он был словно неживой. Говорил как робот, сделанный в кружке кибернетики. Правда, под конец он проснулся, но начал говорить что-то глупое и несвязное. Ох уж этот Семён... Как встретила его на уборке площади, так весь день дальше с ним и провела."
        window hide
        $ set_mode_adv()
        jump slavyana_mod_bknt_show

#Сделано FireBoTer'ом