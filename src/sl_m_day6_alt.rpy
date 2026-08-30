label slavyana_mod__day6_alt:
    $ renpy.pause(2, hard=True)
    $ backdrop = "days"
    $ new_chapter(6, u"Славя. День шестой")
    $ day_time()
    $ persistent.sprite_time = "day"
    $ renpy.pause(3, hard=True)

    play ambience ambience_int_cabin_night fadein 3
    scene bg int_house_of_sl_day
    show unblink
    window show
    "Я открыла глаза и увидела... {w}Потолок своего домика."
    th "Как странно... Я не могу ничего вспомнить из своего сна."
    "Я поднялась с кровати и взглянула на часы."
    "Было семь утра, поэтому я направилась на пробежку."
    window hide
    stop ambience fadeout 2

    scene bg ext_house_of_sl_day with dissolve2
    play ambience ambience_camp_center_day fadein 3
    pause 1
    scene bg ext_houses_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    pause 2

    #Алиса
    if sl_m_end_dv:
        scene bg ext_washstand_day with dissolve
        window show
        "Я пробежалась до умывальников, умылась, и выбежала в лес."
        scene bg ext_path_day:
            zoom 1.1
            yalign 0.01
            block:
                linear 0.2 pos (0,5)
                linear 0.2 pos (0,0)
            repeat
        "Если я ничего не напутала в поворотах, то сейчас мне надо бежать по прямой и тогда я выбегу к сцене."
        pause 2
        "Однако сцены так и не было видно."
        th "Наша музыкантка из страны Восходящего Солнца, наверняка сейчас спит, как и все остальные."
        "Пронеслось у меня в голове и я остановилась."
        th "Так и потеряться недалеко."
        "Поэтому, я решила повернуть направо, как мне казалось, на Восток."
        scene bg ext_path2_day:
            zoom 1.1
            yalign 0.01
            block:
                linear 0.2 pos (0,5)
                linear 0.2 pos (0,0)
            repeat
        "Пробежав между плотными кустами, я обнаружила, что выбежала прямо перед медпунктом."
        scene bg ext_aidpost_day:
            zoom 1.1
            yalign 0.01
            block:
                linear 0.2 pos (0,5)
                linear 0.2 pos (0,0)
            repeat
        "Я решила завершить круг и побежала дальше."
        scene bg ext_dining_hall_back with dissolve
        play sound music_list["dinner_horn_processed"] volume 0.3
        "На удивление, чёрный ход на кухню был открыт."
        "И, судя по звукам, исходящим оттуда, кто-то копошился внутри..."
        "Я пошла проверить."
        play music music_list["awakening_power"] fadein 3
        "Но не успела я зайти, как из-за двери быстро выползла кастрюля. {w}И так же быстро поползла в противоположную от меня сторону."
        "Я тут же бросилась за ней в погоню!"
        stop sound
        scene bg ext_path2_day:
            zoom 1.1
            yalign 0.01
            block:
                linear 0.2 pos (0,5)
                linear 0.2 pos (0,0)
            repeat
        "Абсолютно непонятным мне образом, как только я ринулась за ней, она сразу пропала из виду."
        scene bg ext_path2_day:
            zoom 1.1
            yalign 0.01
        "Но как только я стала искать её, я заслышала шелест в одном из кустов."
        "Там оказался всего лишь ёжик! {w}И только!"
        th "Тайна пропавшей кастрюли остаётся неразгаданной."
        stop music fadeout 3
        stop ambience fadeout 3
        scene black with dissolve
        "..."
        window hide
        scene bg int_house_of_sl_day with dissolve
        window show
        "Завершив свою пробежку, я вскоре вернулась в домик и переоделась."
        "К этому времени, уже должна была начаться линейка, ведь утренний горн уже прозвучал."
        "Поэтому я поспешила на площадь."
        scene bg ext_square_day with dissolve

    #Лена
    elif sl_m_end_un:
        stop ambience fadeout 2
        scene black with dissolve
        pause 2
        play ambience ambience_camp_center_evening fadein 3
        scene bg ext_square_sunset:
            zoom 1.1
            yalign 0.01
            block:
                linear 0.2 pos (0,5)
                linear 0.2 pos (0,0)
            repeat
        window show
        "Я уже оббежала почти весь лагерь по периметру и возвращалась обратно."
        scene bg ext_square_sunset
        "Но не смогла не заметить, что площадь абсолютна не убрана!"
        th "Нужно будет сегодня обязательно подмести!"
        "Я побежала к своему домику."
        scene bg ext_house_of_sl_sunset with dissolve
        "Уже стоя на пороге, я заглянула в домик."
        stop ambience fadeout 1
        scene bg int_house_of_sl_day with dissolve
        play ambience ambience_int_cabin_night fadein 3
        "Женя ещё спала."
        stop ambience fadeout 1
        scene bg ext_house_of_sl_sunset with dissolve
        play ambience ambience_camp_center_evening fadein 3
        "Я решила не тревожить её и решила чуть-чуть подождать."
        "Поэтому, чтобы не терять времени я решила умыться."
        scene bg ext_houses_sunset with dissolve
        "Я шла пешком, в обычном темпе, торопиться мне не нужно было."
        "По пути к умывальникам, я поднялась на более северную «улицу»."
        play sound sfx_open_door_2 volume 0.1
        "И увидела, как открылась дверь в дальнем домике, в котором жили Лена и Мику."
        "Лена осторожно прикрыла дверь и тоже направилась к умывальникам."
        scene bg ext_washstand_day with dissolve
        "Однако на развилке она повернула в лес и скрылась за деревьями так быстро, что я даже не сразу поняла куда она делась."
        "Несмотря на это происшествие, я заверила себя в том, что Лена вернётся."
        th "Не станет же она там голодать в самом деле!"
        scene bg ext_washstand2_day with dissolve
        "Вода была как всегда закаляюще-холодной. Но неподготовленный организм мог с лёгкостью простудиться."
        "Я умылась, но поняла что не захватила полотенце, поэтому пришлось вытираться руками."
        window hide
        stop ambience fadeout 1
        scene black with dissolve
        stop sound
        window show
        "Я зашагала обратно в домик."
        scene bg int_house_of_sl_day with dissolve
        play ambience ambience_int_cabin_day fadein 3
        show mz normal pioneer glasses with dissolve
        mz "Вот ты где, я уж думала ты куда-то пропала, думала тревогу поднимать."
        sl "Да я ещё раньше заходила, но ты спала."
        mz "Ну тогда прощаю. Снова на линейку пойдёшь?"
        sl "Естественно."
        mz "Ладно уж, пошли."
        window hide
        stop ambience fadeout 1
        scene black with dissolve
        pause 1
        play ambience ambience_camp_center_day fadein 3
        scene bg ext_square_day with dissolve
        window show
        "Подходя к площади, я заметила Электроника, который направлялся в нашу сторону, но затем как-то странно посмотрел, развернулся и направился в противоположную сторону."
        "На площади только собирались пионеры. Поэтому мы с моей соседкой образовали начало строя."
        "Потихоньку стали стекаться пионеры. {w}Алиса, {w}Ульяна, {w}Электроник, который шёл в обратную сторону..."
        "Наконец Оля смогла всех собрать и начала приветственную речь."
        stop ambience fadeout 3

    #Ульяна и одиночка
    else:
        scene bg ext_clubs_day:
            zoom 1.1
            yalign 0.01
            block:
                linear 0.2 pos (0,5)
                linear 0.2 pos (0,0)
            repeat
        "Электроник и Шурик уже проснулись. Как странно, в такую рань все по домикам лежат в кроватях и спят, а они уже на ногах. Какие молодцы!"
        scene bg ext_clubs_day
        show el normal pioneer at left
        show sh normal pioneer at right
        with dissolve
        sl "Привет ребята, не думала что вы уже проснулись."
        sh "А, привет Славя, у нас тут дело есть. Сможешь Семёна позвать?"
        sl "Не знаю, скорее всего он спит."
        sh "Ну, ты постарайся. Если же нет, подойдёшь тогда сюда."
        sl "Хорошо."
        th "Если Семён уже не спит, скорее всего он будет ждать у столовой ещё до звонка."
        window hide
        stop ambience fadeout 1
        scene black with dissolve
        pause 2
        scene bg int_house_of_sl_day with dissolve
        play ambience ambience_int_cabin_day fadein 3
        window show
        "Я осторожно приоткрыла дверь, чтобы взять свою форму и переодеться."
        window hide
        stop ambience fadeout 1
        scene bg ext_house_of_sl_day with dissolve
        play ambience ambience_camp_center_evening fadein 3
        pause 2
        scene bg ext_square_day with dissolve
        window show
        "Походив по площади я лишний раз убедилась, что лагерь всё ещё спит."
        scene bg ext_dining_hall_away_day with dissolve
        "Увы, но у столовой Семёна не было. Тогда я решила проверить в последнем месте, где он ещё мог быть."
        "Скоро должна быть линейка, мне надо поспешить."
        window hide
        stop ambience fadeout 3
        scene black with dissolve
        pause 2
        play ambience ambience_camp_center_evening fadein 3
        scene bg ext_house_of_mt_day with dissolve
        window show
        "Я обошла дом с задней стороны и осторожно заглянула в окошко."
        "Оля и Семён ещё спали."
        th "Придётся сообщить кибернетикам, чтобы зазря не ждали Семёна."
        scene bg ext_clubs_day with dissolve
        show el normal pioneer at left with dissolve
        show sh normal pioneer at right with dissolve
        sh "Понятно."
        el "Славя, а можно поручить тебе... кое-что отнести Виоле?"
        sl "Что?"
        show el upset pioneer at left with dspr
        el "Ну, пожалуйста."
        sl "Я надеюсь ничего запретного?"
        "Я грозно посмотрела на них."
        show el serious pioneer at left with dspr
        el "Н-нет. Просто не заглядывай туда и всё."
        sl "Но если там что-то взрывоопасное или хрупкое, вы лучше уж сразу предупредите."
        show el normal pioneer at left with dspr
        el "Хрупкое."
        sl "Хорошо, буду аккуратнее."
        hide el with dspr
        pause 1
        show el normal pioneer at left with dspr
        "Электроник пропал в клубах, но через пару секунд вышел со свёртком в руках."
        "Похоже это та водка, которую они просили им принести для протирки оптики."
        "Я молча взяла свёрток и направилась в медпункт."
        scene bg ext_aidpost_day with dissolve
        "Чуть недоходя до медпункта я всё же решила развернуть, чтобы во всём убедиться."
        "Да, это водка, при чём почти полная, похоже попользовались очень мало. Зачем же им было это так срочно тогда?"
        "Проверять содержимое я не рискнула, завернув всё обратно."
        play sound sfx_knock_door2
        "Я постучалась."
        window hide
        pause 2
        window show
        "Но вот незадача! Виолы то и не было."
        "Пришлось воспользоваться своими ключами."
        stop ambience fadeout 2
        play sound sfx_open_door_1
        scene bg int_aidpost_day with dissolve
        "Я поставила свёрток недалеко от входа, но так, чтобы не сбила случайно и было заметно."
        scene bg ext_aidpost_day with dissolve
        play ambience ambience_camp_center_day fadein 3
        pause 1
        scene bg ext_square_day with dissolve
        "К этому времени пионеры уже строились на площади, я поспешила занять место в строю."
        stop ambience fadeout 2

    play music music_list["two_glasses_of_melancholy"] fadein 3
    show mt smile pioneer with dissolve
    mt "Доброе утро пионеры! Как вы знаете, сегодня предпоследний день смены. Сделайте всё что вы ещё не успели сделать, но в пределах разумного."
    show mt grin pioneer with dissolve
    "Она улыбнулась."
    show mt smile pioneer with dissolve
    mt "Также, не забудьте собрать свои вещи и заранее помыться в бане, так как душевые всё ещё в ремонте."
    "И похоже так и будут до конца смены."
    mt "Сегодняшняя линейка будет короткой. Строй! Разойдись!"
    hide mt with dspr
    "Пионеры разбрелись кто куда. {w}Но в основном конечно же в столовую."

    #Алиса
    if sl_m_end_dv:
        show el normal pioneer with dissolve
        el "Славя!"
        "Меня окликнул Электроник."
        el "Отойдём в сторонку."
        scene bg ext_clubs_day with dissolve
        show el normal pioneer with dissolve
        sl "А зачем так далеко?"
        el "Скажи пожалуйста Семёну, чтобы он сегодня подошёл к клубам."
        sl "Запретное что-то?"
        show el serious pioneer with dspr
        el "Н-нет нет! Просто {w}это очень ответственное задание!"
        sl "Да?"
        el "Да! Можешь даже к Виоле потом зайти спросить."
        sl "Ну хорошо."
        "Напоследок, он как-то странно взглянул на меня. {w}Словно чего-то боялся."
        hide el with dspr
        th "Не могут же наши кибернетики на конец смены задумать что-то нехорошее, ещё и втянуть в это Семёна."
        "Отбросив эти мысли, я направилась в столовую."

    #Ульяна
    elif sl_m_end_us:
        "И я как-то внезапно осознала, что Семёна с нами нет!"

    stop music fadeout 2
    scene bg int_dining_hall_people_day with dissolve2
    play ambience ambience_dining_hall_full fadein 3

    #Алиса
    if sl_m_end_dv:
        show un normal pioneer with dissolve
        "На завтраке ко мне подсела Лена."
        sl "Привет!"
        un "Привет."
        sl "Не в настроении сегодня?"
        show un shy pioneer with dspr
        un "Почему?"
        sl "Хмурая ты какая-то."
        show un normal pioneer with dspr
        un "Нет, всё хорошо."
        sl "А я сегодня, кстати, во время пробежки мимо столовой пробегала и увидела бегающую кастрюлю."
        show un surprise pioneer with dspr
        un "Это как?"
        "Она удивлённо посмотрела на меня."
        sl "Вот так! Просто выбежала и {i}фить{/i} в кусты."
        window hide
        pause 2
        show un laugh pioneer with dspr
        window show
        "Лена рассмеялась."
        un "Серьёзно что ли? Кастрюли же не бегают сами по себе."
        sl "Я потом в кустах смотрела и увидела там ёжика, но кастрюлю так и не нашла."
        show un smile pioneer with dspr
        un "Понятно."
        sl "Приятного аппетита кстати!"
        un "Тебе тоже."
        "Остаток завтрака я провела в поедании каши."
        th "Надо придумать, что бы такое на память сделать, чтобы потом воспоминания остались."
        window hide
        pause 2
        stop ambience fadeout 1

        play ambience ambience_camp_center_day fadein 3
        scene bg ext_dining_hall_away_day with dissolve
        show us normal pioneer with dissolve
        window show
        "Выходя из столовой, я встретила Ульяну."
        us "Привет Славя, нам надо сетку натянуть на площадке после обеда, Ольга Дмитриевна просила, поможешь?"
        sl "Конечно я помогу вам!"
        us "Хорошо."

        scene bg ext_houses_day with dissolve
        "Для начала, мне надо было выполнить просьбу Электроника и позвать Семёна."
        th "Скорее всего спит ещё."

        scene bg ext_house_of_mt_day with dissolve
        show pi normal pioneer with dissolve
        "Когда я подошла к его домику, он только вышел на улицу."
        sl "Семён!"
        sl "Ты занят?"
        me "Нет..."
        sl "Можешь мне помочь?"
        me "Что такое?"
        sl "Надо зайти в кружок кибернетики и... {w}Я сама точно не знаю, они тебе там всё объяснят."
        me "Хорошо..."
        sl "Спасибо!"
        hide pi with dspr
        "Я улыбнулась ему и пошла на склад. За метлой."
        "По пути к Семёну, я заметила, что площадь не убрана."
        "У меня как раз оставалось время, прежде чем идти на спортивную площадку."
        stop ambience fadeout 1
        scene black with dissolve
        "..."

        play ambience ambience_camp_center_day fadein 3
        scene bg ext_square_day with dissolve
        "Площадь действительно оказалась пыльной. Никто её не подметает кроме меня."
        "На дальней лавке сидели Семён и Лена."
        "Они что-то обсуждали. {w}С таким видом, будто находятся на очной ставке и принимают стратегическое решение об обороне Москвы."
        th "Подслушивать некультурно!"
        "Поэтому, я не стала к ним подходить, а ограничилась лишь наблюдением со стороны."
        window hide
        stop ambience fadeout 2
        scene black with dissolve
        pause 2
        play ambience ambience_camp_center_day fadein 3
        scene bg ext_square_day with dissolve
        window show
        "Подметание заняло у меня всё оставшееся время до обеда."
        stop ambience fadeout 1

        play music music_list["goodbye_home_shores"] fadein 3
        scene bg ext_dining_hall_away_day with dissolve
        show cs normal with dissolve
        "На подходе к столовой, меня встретила Виола."
        cs "Славя, можешь дать мне свои ключи на некоторое время?"
        sl "Конечно, но зачем?"
        cs "Мой ключ от медпункта потерялся."
        sl "А вы осмотрели, может, потеряли?"
        cs "Нет, как бы я закрыла медпункт? И тем более, я осмотрела рядом и не нашла."
        play sound sfx_keys_rattle
        sl "Хорошо, держите!"
        "Я отдала ей свои ключи."
        cs "Спасибо Славя, я обязательно верну."
        sl "Я после обеда на площадку уйду, зайдите туда."
        show cs smile with dspr
        cs "Обязательно."
        stop music fadeout 1

        scene bg int_dining_hall_people_day with dissolve
        "Большая часть столиков оказалась занята. Поэтому, я провела обед в компании неизвестных мне пионеров."
        "Сегодня это был выбор съесть сразу или по-отдельности, состоящий из каши на молоке и гречки с мясом."
        th "Очень странное сочетание, даже для наших поваров."
        window hide
        pause 2

        scene bg ext_playground_day with dissolve2
        window show
        "На спорт площадке я помогла младшим натянуть сетку для волейбола, но я не видела Ульяну."
        "И Виолы тоже нигде не было."
        "Я уже сказала ей, что буду ждать на площадке, поэтому было бы странно с моей стороны вот так вот уйти."
        play music music_list["went_fishing_caught_a_girl"]
        play ambience ambience_soccer_play_background fadein 3
        "Я решила присоединиться к ребятам и сыграть с ними в воллейбол."
        window hide
        pause 3
        "Ребята очень старались, но моё присутствие было решающим аргументом."
        "Поэтому, противоположная команда ожидаемо проиграла, хоть они и не сильно отчаивались по этому поводу."
        stop music fadeout 2
        stop ambience fadeout 3
        show cs normal with dissolve
        "К этому моменту, наконец, подошла Виола."
        play sound sfx_keys_rattle
        cs "Вот твои ключи."
        sl "Кстати, Виола, а что было в том пакете?"
        cs "Откуда ты знаешь?"
        sl "Так меня кибернетики попросили Семёна позвать."
        cs "То же, что в прошлый раз ты относила им."
        sl "Опять? Я же вернула вам."
        cs "Им снова потребовалось."
        sl "Так, и кто же всё-таки забрал ключи?"
        cs "Без понятия."
        sl "Ладно."
        th "Ну, раз они попросили Семёна отнести, значит он заходил в медпункт и мог что-нибудь плохое сделать."
        sl "Хорошо, я уточню."
        hide cs with dspr
        "Мимо проходила Ольга Дмитриевна."
        sl "Оля!"
        show mt normal pioneer with dissolve
        mt "Что такое, Славя?"
        sl "Можешь Семёна позвать, пожалуйста? Мне{w} помощь нужна."
        show mt smile pioneer with dspr
        mt "Хорошо, сейчас."
        scene black with dissolve
        "..."

        scene bg ext_playground_day with dissolve
        show pi normal pioneer
        me "Вы желали меня видеть?"
        "Сказал он шутливо."
        th "А вот мне сейчас не до шуток."
        sl "Да... {w}Слушай, ты не брал случайно ключ от медпункта?"
        me "Нет."
        sl "Просто ты там последнее время частенько бывал."
        show pi angry pioneer
        me "Нет..."
        sl "Может, знаешь кто?"
        show pi normal pioneer
        me "Нет. А что случилось?"
        sl "Ко мне медсестра подходила, просила мой - у меня же есть ключи от всех помещений лагеря. {w}Сказала, что её пропал."
        me "Может, потеряла..."
        sl "Нет, говорит, что потерять точно не могла."
        me "В общем, не знаю я."
        sl "Ладно."
        "Я улыбнулась и побежала к Виоле."

        $ persistent.sprite_time = "day"
        $ day_time()
        scene bg int_aidpost_day with dissolve
        show cs normal with dissolve
        cs "Значит, Семён не брал."
        sl "Да."
        cs "Ещё какие-нибудь догадки есть?"
        sl "Ну, я у ребят ещё спрошу."
        cs "Да и кстати{w}, посылка поддельная."
        sl "Это как?"
        cs "В ней столько же водки, сколько и в порядочном пионере."
        sl "Как вы это поняли?"
        cs "Ты думаешь, пионерам можно доверять такой товар? Я понюхала, запаха нет."
        sl "Теперь ясно, почему потерялся ключ."
        th "Конечно, большинство наших пионеров порядочные, но всё равно это мог сделать кто угодно."
        "Поэтому, я решила проверить кибернетиков на честность."
        window hide
        scene black with dissolve
        stop music fadeout 3
        window hide
        pause 2

        $ persistent.sprite_time = "night"
        $ night_time()
        play ambience ambience_camp_center_night fadein 3
        scene bg ext_square_night with dissolve
        show dv normal pioneer with dissolve
        window show
        "Но не дойдя до них, я встретила Алису, которая сидела на лавке с закрытыми глазами."
        th "А что, она ведь вполне могла!"
        sl "Алиса!"
        dv "Чего тебе?"
        sl "Это ты взяла ключи от медпункта и украла... {w}лекарство?"
        show dv grin pioneer with dspr
        "Она ухмыльнулась."
        sl "Так ты или не ты?"
        show dv normal pioneer with dissolve
        dv "Подумай сама. Зачем мне брать ваши неведомые...{w} лекарства?"
        sl "После истории с памятником, ты первая подозреваемая!"
        dv "Скажи, это был уголь?"
        sl "Нет, но..."
        dv "Ну вот! А из медпункта мне для взрывов более ничего и не надо было. {w}Тем более, у меня больше нет желания этим заниматься."
        play sound music_list["dinner_horn_processed"]
        "Но в этот момент прозвучал сигнал на ужин."
        sl "Ладно, пока что я тебе поверю. Но не думай, что ты вне подозрений!"
        hide dv with dspr
        "Она ушла."
        th "Надо будет и у ребят тоже спросить."

        scene bg ext_dining_hall_away_night with dissolve
        "У столовой я заметила их обоих и пошла с ними."
        window hide
        stop ambience fadeout 1

        $ persistent.sprite_time = "day"
        $ day_time()
        scene bg int_dining_hall_people_day with dissolve
        play ambience ambience_dining_hall_full fadein 3
        show el normal pioneer at left
        show sh normal pioneer at right
        with dissolve
        window show
        "Я села за один стол с ними."
        el "Приятного аппетита."
        sl "Спасибо."
        sl "Вы не брали ключей от медпункта?"
        sh "Нет, зачем? Мы весь день в клубе сидели."
        sl "А что вы там делали?"
        sh "Собирали робота, у нас сроки горят."
        el "А что случилось?"
        sl "У медсестры ключи пропали {w}и в посылке не то, что было изначально."
        show el shocked pioneer at left with dspr
        el "Что?! Но... Мы немного попользовались и отдали!"
        sl "Значит вы не крали?"
        show el normal pioneer at left with dspr
        sh "Нет."
        th "Остаётся проверить Семёна. Если это не он, то я даже не знаю кто ещё может быть."
        "Неожиданно Лена выбежала из столовой. {w}Вместе с ней Ульяна, а за ней погналась Алиса."
        th "Ульяна неисправимая проказница... Что только могло произойти сейчас?"
        window hide
        stop ambience fadeout 1

        $ persistent.sprite_time = "night"
        $ night_time()
        scene bg ext_dining_hall_away_night with dissolve
        play ambience ambience_camp_center_night fadein 3
        window show
        "Я ждала Семёна."
        "Но он не заходил и не выходил."
        "Я решила поискать его."
        window hide
        stop ambience fadeout 3
        scene black with dissolve
        window show
        "Походив по лагерю, заглянув на пляж и пристань, я пришла к выводу, что он пропустил ужин, потому что скорее всего спит."
        "Я скорее побежала к нему."

        scene bg ext_house_of_mt_night with dissolve
        play ambience ambience_camp_center_night fadein 3
        "Я подходила к его домику, когда он вышел из него."
        "Я подбежала к нему."
        show pi normal pioneer with dissolve
        sl "Семён..."
        "Мне пришлось отдышаться для начала."
        sl "Ты точно не брал ключей от медпункта?"
        me "Нет конечно, зачем они мне вообще?"
        sl "Может быть, тогда знаешь, кто взял?"
        me "Нет. А что-то случилось?"
        sl "Да... Пропало кое-что."
        me "Что же?"
        sl "Важное..."
        sl "Лекарства кое-какие."
        me "Ясно. {w}Ну, я не знаю, ты уж извини..."
        sl "Ладно..."
        th "Это серьёзная потеря, о которой придётся сообщить Оле."
        "Но для начала мне стоило её найти."

        scene bg ext_square_and_houses with dissolve
        show mt normal pioneer with dissolve
        "Смеркалось. Начали зажигаться ночные фонари лагеря."
        "Чуть выйдя на площадь, я встретила вожатую, направляющуюся в домик."
        mt "Славя, поздно уже."
        sl "Оля, тут такое дело."
        sl "В общем, спирт из медпункта пропал и нам с Виолой не удалось найти похитителя, вдобавок ещё и ключи Виолины потерялись."
        show mt sad pioneer with dspr
        mt "Да, это печально. Печальнее всего то, что это сделал один из пионеров!"
        show mt normal pioneer with dspr
        mt "Ладно, завтра разберёмся с этим. Иди спать."
        stop ambience fadeout 3
        scene black with dissolve
        "..."
        window hide
        play ambience ambience_int_cabin_night fadein 3
        scene bg int_house_of_sl_night_light with dissolve
        window show
        "Перед сном у меня ещё было время. Я решила сделать запись в своём дневнике."
        
    # Дневник
        scene anim prolog_2
        with fade
        $ set_mode_nvl()
        "Сегодня предпоследний день в «Совёнке», как жаль что смена вот-вот подойдёт к концу. Но я рада, что попала сюда, здесь я встретила много интересных людей."
        "Сегодня Электроник попросил меня сказать Семёну, чтобы доставил какую-то посылку."
        "Не знаю какую, но когда я сегодня пришла к Виоле, она мне сказала что именно у неё пропало."
        "Подозрения конечно сразу же пали на Семёна. Однако, по его словам, у него ничего нет." 
        "Далее я решила проверить Алису, которая вполне могла это сделать. Но и тут меня ждала неудача."
        "В итоге мне пришлось доложить об этом Оле. Похоже, завтра нам придётся разобраться с этим."
        "Пожалуй, завтрашний день проведу с отдыхом от всего. Я хочу запомнить каждое дерево, каждый камушек этого прекрасного места. Взглянуть на всё это в последний раз."
        "Мы ещё увидимся, дорогой дневник."
        nvl clear
        $ set_mode_adv()
    # Конец дневника

        scene bg int_house_of_sl_night
        "Я погасила свет и легла в кровать."
        "Последний день был уже скоро."
        "..."
        window hide

    #Лена
    elif sl_m_end_un:
        "Заходя в столовую, я обнаружила Семёна, который редко успевает на завтрак."
        "Лицо у него было очень напряжённое и задумчивое."
        "Я решила подойти к нему."
        show pi normal pioneer with dissolve
        sl "Привет, можно к тебе?"
        me "Да..."
        "Ответил Семён тоскливо."
        sl "Не в настроении?"
        me "Не особо."
        sl "Что-то случилось?"
        me "Да ничего..."
        sl "Если не хочешь, не рассказывай."
        me "Да рассказывать и не о чем."
        "Я решила не тревожить его и принялась за еду."
        "Завтрак не представлял из себя ничего необычного. Стакан компота и манная каша."
        me "А куда ты вчера ушла?"
        sl "Я? Просто хотелось побыть одной."
        me "Это на тебя не похоже."
        sl "Да? Ну, может быть... {w}Ты тоже не часто бываешь таким угрюмым."
        me "Наверное."
        "Моя тарелка была уже пуста. А вот Семён ел очень медленно."
        sl "Ладно, я пойду..."
        me "Кстати, а ты Лену не видела?"
        sl "Нет, а что?"
        "Я уже знала, что Лена иногда проводит время в лесу в одиночестве, но через пару часов возвращается."
        "Поэтому решила, что Семёну необязательно знать об этом, потому что он, скорее всего, отправится на её поиски и помешает Лене."
        me "Просто её не было на линейке. {w}Странно... Не похоже на неё."
        sl "Да, пожалуй."
        th "Пусть Семён лишний раз не волнуется."
        sl "Ну, думаю, ничего страшного."
        me "Да, конечно, просто спросил..."
        "Я направилась к выходу из столовой."
        stop ambience fadeout 3
        scene black with dissolve
        "..."
        window hide

    #Ульяна
    elif sl_m_end_us:
        "Зайдя в столовую, я тоже не нашла его."
        "Поэтому..."
        "Компанию за завтраком мне составили {w=0.5}{nw}"
        show mi laugh pioneer at left with dspr
        extend "Мику{w=0.5}{nw}"
        show us laugh pioneer at right with dspr
        extend "и Ульяна."
        play music music_list["eat_some_trouble"] fadein 3
        "Эти двое что-то весело обсуждали, да и настроение у обоих было приподнятое."
        sl "Какой-то праздник без меня?"
        show mi smile pioneer at left with dspr
        mi "Да нет, Славечка! Если бы был какой, мы бы тебя обязательно позвали, и всех-всех ребят тоже, какой же праздник, если он проходит без друзей?."
        show us grin pioneer at right with dspr
        us "Мы обсуждаем вчерашний поход."
        show us sad pioneer at right with dspr
        "Но видимо она поняла, что ляпнула не подумав и поспешила закрыть рот рукой."
        sl "Тебя же не было в походе вчера."
        mi "Была, она там такой..."
        show mi shocked pioneer at left
        show us dontlike pioneer at right
        with dspr
        "Ульяна поспешила закрыть рот и Мику."
        show mi normal pioneer at left with dspr
        sl "Ульяна! Я чего то не знаю?"
        show us normal pioneer at right with dspr
        us "Ну, мы уже покушали, приятного аппетита тебе."
        hide mi
        hide us
        with dspr
        stop music fadeout 3
        "И Ульяна быстро потянула за руку Мику к двери."
        th "Что же там такого могло произойти?"
        show mt normal pioneer with dissolve
        "Ко мне подсела Оля."
        mt "Славя, сегодня есть дела по лагерю, поможешь ведь?"
        sl "Конечно!"
        mt "Зайди тогда в административный корпус и Мику позови."
        sl "Хорошо."
        window hide
        stop ambience fadeout 1
        scene black with dissolve

        scene bg ext_house_of_mt_day with dissolve
        play ambience ambience_camp_center_day fadein 3
        window show
        "Я направлялась в сторону клуба Мику, в надежде поискать там её, а заодно и Ульяну."
        "Но обернувшись, я заметила сегодняшнего соню."
        "Он сидел в шезлонге и смотрел себе под ноги."
        "Я поспешила вывести его из ступора."
        show pi normal pioneer with dissolve
        sl "Привет!"
        "Он поднял глаза на меня."
        me "Привет."
        sl "Опять проспал?"
        me "Видимо да."
        sl "Нехорошо это..."
        me "Пожалуй... А ты куда идёшь?"
        sl "Да дела кое-какие."
        me "Ясно..."
        "Наступило молчание. Поэтому я развернулась и собиралась идти, куда направлялась."
        me "Может, посидишь со мной немного?"
        sl "Можно, почему нет?"
        "Я села рядом."
        sl "Тебя что-то беспокоит?"
        me "Да нет, с чего ты взяла?"
        sl "По лицу видно."
        "Мне показалось это забавным и я тихонько рассмеялась."
        me "Да нет..."
        me "Слушай, а у тебя есть младшие братья, сёстры?"
        sl "Есть."
        me "И какие отношения с ними?"
        sl "Нормальные."
        th "Не совсем поняла вопроса."
        sl "А у тебя?"
        me "Нет..."
        "Ответил он после небольшой паузы."
        sl "А почему тогда спрашиваешь?"
        me "Не знаю, просто..."
        me "А ты всегда их понимаешь?"
        sl "Стараюсь."
        me "Просто я иногда совершенно не могу понять детей... {w}Тех, кто младше..."
        sl "Почему?"
        me "Ну, не всегда получается понять мотивацию их поступков. Они зачастую нелогично себя ведут."
        sl "Но разве тебе не было столько же лет, сколько им сейчас?"
        me "Было, конечно..."
        sl "Ну вот! Вспомни себя в то время."
        me "Я таким не был..."
        sl "Что ж, хорошо, если так!"
        "Я рассмеялась."
        me "А ты? {w}Тоже делала всякие глупости?"
        sl "Смотря в каком возрасте."
        me "Ну не знаю... {w}Лет четырнадцать, может..."
        th "Когда я купалась на речке и решила половить рыб, я погналась за ними, оступилась и упала в воду. Родители тогда спасли меня, потому что рядом стояли."
        "Тогда то я и решила научиться плавать."
        th "Или решила выпустить коров, которые были у нас в загоне, на свободу, мне тогда казалось это несправедливым. Родители потом ходили по округе искали их."
        sl "Всякое было..."
        me "Ладно, это всё замечательно, но всё равно ничего не понятно..."
        sl "Может, так и должно быть?"
        me "Может..."
        sl "Ладно, пока тогда, я побегу."
        "Я направилась в клуб Мику."
        stop ambience fadeout 2
        scene black with dissolve
        "..."
        window hide

        play ambience ambience_camp_center_day fadein 3
        scene bg ext_musclub_day with dissolve
        window show
        "Я постучалась, но никто мне не ответил."
        "Поэтому, я заглянула в большое окно клуба, и поняла что внутри никого нет."
        th "Даже и не представляю где можно искать Мику, кроме как в её клубе."
        "Мне пришлось прийти к зданию администрации одной."
        window hide

    #Одиночка
    else:
        "За одним столом со мной сидела гостья из страны восходящего солнца."
        "Болтала обо всём насущном."
        show mi sad pioneer with dspr
        mi "Как же жалко конечно, что смена уже кончается, всё пролетело так незаметно. Я даже не помню что было неделю назад..."
        mi "И родители тоже по мне скучают. Не могу дождаться снова встретиться с ними. Но ещё мне не хочется уезжать отсюда, очень не хочется."
        mi "Моя душа как будто принадлежит этому месту. Я никогда не забуду всех, с кем встретилась здесь. И с тобой Славечка, и с Леночкой, и с Семёнчиком. Со всеми-всеми."
        "Я не совсем внимательно её слушала, но основную суть монолога уловила, изредка стараясь поддержать диалог."
        "Завтрак прошёл достаточно быстро, не стали бы нас откармливать сразу после пробуждения."

        stop ambience fadeout 2
        scene bg ext_dining_hall_away_day with dissolve
        play ambience ambience_camp_center_day fadein 3
        "Когда я вышла из столовой ноги сами понесли меня на сцену."
        scene bg ext_stage_big_sunset with dissolve
        "Два высоких блондина копошились рядом с аппаратурой."
        show el normal pioneer at right
        show sh normal pioneer at left
        with dissolve
        sl "Что делаете?"
        show el shocked pioneer at right
        show sh scared pioneer at left
        with dspr
        sh "А! {w=0.5}{nw}"
        show el normal pioneer at right
        show sh upset pioneer at left
        with dspr
        extend "Славя... Не пугай так!"
        sl "Извини."
        sh "Я уж думал это Алиса или Мику. Да хоть Ольга Дмитриевна, которая сейчас будет отчитывать за порчу общественной собственности."
        "Похоже Электроник заметил меня ещё издалека, так как совсем не удивился моему появлению."
        show sh normal pioneer at left with dspr
        el "Мы хотим в конце смены использовать колонку для музыки, чтобы включить её перед отъездом."
        sl "Как здорово!"
        show el upset pioneer at right with dspr
        el "...да и нам бы не помешали твои ключи."
        sl "Зачем?"
        el "Нам нужно достать провода из под сцены и посмотреть какие могут подойти."
        show el normal pioneer at right with dspr
        "Мне снова пришлось ими воспользоваться. Неким жезлом власти в лагере."
        pause 3
        "Мы провозились с этим добрые два часа."
        th "Никогда бы не подумала, что время можно потратить таак бессмысленно."
        "Достав провода, мы поочерёдно подключили почти что все из них."
        sh "Вот этот в лучшем качестве из всех подходящих. Возьмём его."
        "Наконец сказал Шурик, который словно тянул резину всё это время."
        sh "Всё Славь, спасибо за помощь."
        sl "А я хотела посмотреть, что вы будете дальше делать."
        sh "Серёг, а у тебя то есть с чего сыграть, давай колонки в клуб занесём?"
        show el upset pioneer at right with dspr
        el "А... Н-нет, я что-то не подумал."
        show sh upset pioneer at left with dspr
        sh "Всмысле? А зачем мы тогда всё это проделывали?"
        el "Ну, ты же знаешь."
        "Шурик недоумённо посмотрел на него."
        play sound sfx_dinner_horn_processed
        "Но дальнейшие разборки предотвратил звук горна."
        th "Как быстро время пробежало!"
        sh "Ладно, пошли пообедаем тогда."
        "Мы направились в столовую."
        window hide
        scene black with dissolve
        pause 1
        play ambience ambience_dining_hall_full fadein 3
        scene bg int_dining_hall_people_day with dissolve
        window show
        "В дальнем углу столовой одиноко сидел Семён."
        show pi normal pioneer with dissolve
        sl "Можно присесть?"
        me "Конечно."
        "Электроник и Шурик сели вместе, что-то обсуждая."
        "Я же уделяла всё внимание еде."
        "Семён пришёл раньше нас и уже поел."
        show el normal pioneer at fleft
        show sh normal pioneer at fright
        with dissolve
        me "Слушайте, а вы не знаете случайного пионера... {w}сегодня видел... {w}Ну, он такой..."
        me "Ну, ростом с меня, комплекцией такой же..."
        show el smile pioneer at fleft with dspr
        sl "По такому описанию не поймёшь."
        "Электроник отвлёкся от беседы с Шуриком."
        show sh serious pioneer at fright with dspr
        el "К тому же тут пол-лагеря таких, если уж на то пошло."
        "В целом он был прав."
        sh "А почему спрашиваешь?"
        me "Просто встретился сегодня с ним. {w}И показалось, что раньше его здесь не видел."
        el "А ты посмотри в столовой! {w}Не думаю, что он пропустит обед!"
        me "Точно! {w}Ладно, ребята, приятного аппетита!"
        hide pi with dspr
        "Он встал из-за стола."
        "..."
        window hide
        scene black with dissolve
        pause 1
        play ambience ambience_camp_center_day fadein 3
        scene bg ext_stage_big_sunset with dissolve
        window show
        "После обеда мальчики вернулись шаманить с аппаратурой."
        "Я думала это не займёт много времени, но процесс меня поглотил."
        show el normal pioneer at right
        show sh normal pioneer at left
        with dissolve
        sl "Шурик, сколько времени?"
        "Он вскинул руку перед собой."
        sh "Десять минут второго."
        sl "Ой! Ладно, мне пора уже, столько дел надо сделать ещё!"
        "Они хором попрощались со мной."
        scene bg ext_square_day with dissolve
        "Проходя мимо площади я не могла не заметить, что никто на ней давно уже не убирался."
        "Похоже на ней вообще никто не убирается кроме меня."
        play sound sfx_broom_sweep fadein 3 loop
        "Естественно, я не могла этого так оставить."
        th "Меня словно запрограммировали подмечать малейшую грязь и сразу приниматься за уборку."
        "Но раз уж я захватила с собой метёлку со склада, то чтобы сэкономить время надо будет ещё в библиотеку заглянуть."
        window hide
        stop sound fadeout 2
        stop ambience fadeout 2
        scene black with dissolve
        pause 1
        window show
        "Когда я закончила на площади, то направилась к обиталищу Жени."
        window hide

    #Лена или одиночка
    if sl_m_end_un or sl_m_end_sl:
        scene bg int_library_day with dissolve
        play ambience ambience_int_cabin_day fadein 3
        show mz angry pioneer glasses with dissolve
        window show
        if sl_m_end_un:
          "Я решила заглянуть в библиотеку к своей соседке."
        else:
          sl "Привет, я пришла к тебе подмести."
          mz "Давай."
        "В этот раз Женя была особенно сердитая."
        "Всё было написано на лице."
        sl "Что-то случилось?"
        mz "А? Да нет, а что?"
        sl "Ты вся нахмуренная и сердитая."
        mz "Ну... да."
        sl "И что же?"
        mz "Что?"
        sl "Это я тебя спрашиваю."
        mz "Что ты спрашиваешь?"
        sl "Что произошло-то?"
        mz "Да ничего не произошло."
        sl "Но ты же только что сказала что произошло."
        mz "Ничего я не говорила."
        sl "А по-моему говорила."
        mz "И что я говорила?"
        sl "Так! {w}Стоп!"
        sl "Скажи, почему ты сегодня не в настроении?"
        mz "Со мной всё нормально, не забивай себе голову чепухой."
        sl "Ладно."
        hide mz with dspr
        "Я зашла за стеллажи и начала подметать за ними{w=0.5}{nw}"
        play sound sfx_open_door_2
        extend ", когда дверь в библиотеку открылась."
        "Я не видела кто это был. Но узнала по голосу."
        stop ambience fadeout 3
        play music music_list["meet_me_there"] fadein 3
        el "Ж-жень... Привет."
        mz "Чего пришёл?"
        el "Женя..."
        "Было понятно, что он с трудом подбирает слова."
        "Подслушивать, конечно, очень некультурно, но я осторожно спряталась за стеллажами, чтобы меня нельзя было увидеть, в случае чего."
        el "Сегодня предпоследний день смены и я хотел сказать кое-что."
        el "Завтра мы разъедемся ведь? И, возможно, даже не увидимся если не позаботимся об этом."
        mz "К чему ты клонишь?"
        el "Понимаешь, я с первых дней встречи с тобой... Ну, в общем у меня проснулись к тебе чувства..."
        "Дальше он начал очень быстро тараторить и я услышала как заскрипел стул."
        el "В общем мне кажется... Всмысле, я точно ощущаю чувства к тебе, и ты мне очень нравишься, и я думал, что, может ты хочешь встречаться со мной?"
        stop music
        play music music_list["awakening_power"]
        "А потом он резко выбежал из библиотеки и хлопнул дверьми."
        "Я выглянула."
        "За ним увязалась Женя и тоже хлопнула дверью."
        "Она что-то кричала ему, а затем зашла обратно."
        show mz angry pioneer glasses with dissolve
        sl "Ну, в общем я убралась. {w}Наверное, пойду."
        mz "Иди уже."
        stop music fadeout 3
        scene bg ext_library_day with dissolve

    #Одиночка
    if sl_m_end_sl:
        th "Это было грустно. Неразделённая любовь, неужели и со мной такое может случиться?"
        window hide
        scene black with dissolve
        pause 1

        play ambience ambience_int_cabin_day fadein 3
        scene bg int_house_of_sl_day with dissolve
        window show
        th "Напишу дневник, пока время есть."
        
    # Дневник
        $ set_mode_nvl()
        "Сегодня предпоследний день в «Совёнке», как жаль что смена вот-вот подойдёт к концу. Но я рада, что попала сюда, здесь я встретила много интересных людей."
        "С некоторыми даже подружилась."
        "Например с такими замечательными ребятами, как Серёжа и Саша."
        "На благо лагеря стараются, хотят сделать последний день смены незабываемым. Полдня с ними безрезультатно провозилась, правда, но надеюсь у них получится."
        "Ещё, Семён вдруг оживился: он встретил какого-то пионера и теперь везде его ищет. И как он его найдёт, если даже не может сказать как он выглядел."
        "Из полезных дел сегодня была только уборка на площади." 
        "Завтрашний день будет последним, и я хочу, чтобы он навсегда остался в моей памяти."
        $ set_mode_adv()
    # Конец дневника

        play sound sfx_dinner_horn_processed
        pause 1
        stop ambience fadeout 2
        scene black with dissolve
        "..."
        window hide
        stop sound fadeout 1

        $ persistent.sprite_time = "day"
        $ day_time()
        play ambience ambience_dining_hall_empty fadein 3
        scene bg int_dining_hall_day with dissolve
        window show
        "К моменту когда я вошла в столовую, большая часть пионеров уже поела."
        "Мой ужин прошёл в одиночестве."
        "К моему удивлению, нигде не было видно Семёна."
        th "Даже ему, наверное, было сейчас чем заняться."
        th "Наверняка пытается найти того самого пионера, которого увидел сегодня."
        th "А может, он проводит свой последний день в лагере с друзьями или какой-нибудь девочкой.. {w}Юлей например{w}, хотя, не припомню, такую из наших."
        stop ambience fadeout 3
        scene black with dissolve
        "..."
        window hide
        pause 1

        $ persistent.sprite_time = "night"
        $ night_time()
        play ambience ambience_camp_center_night fadein 3
        scene bg ext_square_night with dissolve
        window show
        "Я решила немного прогуляться перед сном."
        "Я села на лавочку."
        "Время было ещё не совсем позднее, поэтому то и дело проходили мимо пионеры. Кто-то шёл под руку, кто-то просто в компании друзей."
        "Или просто в одиночестве."
        th "Ах, этот свежий воздух!"
        th "Каждый день деревья работают и в процессе фотосинтеза вырабатывают кислород, который смешивается с воздухом, пригодным для дыхания."
        th "Но так ли это на самом деле, неужели деревья сами знают, что им нужно создавать кислород, чтобы им могли дышать остальные живые существа?"
        th "А может, это просто побочный продукт, и именно из-за этого, по наитию и зародилась способная активно передвигаться жизнь?"
        th "Что-то я начала философствовать под ночь. Пойду лучше спать, насиделась я."
        window hide
        stop ambience fadeout 2
        scene black with dissolve
        pause 1

        $ persistent.sprite_time = "day"
        $ day_time()
        play ambience ambience_int_cabin_night fadein 3
        scene bg int_house_of_sl_night_light with dissolve
        window show
        "Внутри никого не оказалось. С минуты на минуту должна была прийти Женя."
        "Я взяла свой дневник и дописала в него несколько строк..."
        
    # Дневник
        $ set_mode_nvl()
        "...Сегодня случилась неприятная сценка в библиотеке: Серёжа решил признаться в любви своей даме сердца, но Женя ясно дала ему понять больше не приближаться к ней."
        "А жаль, из них вышла бы отличная пара. Возможно, я тоже в скором времени встречу своего кавалера."
        $ set_mode_adv()
    # Конец дневника

    #Лена
    if sl_m_end_un:
        th "Это было грустное зрелище."
        "..."
        play ambience ambience_camp_center_day fadein 3
        show bg ext_square_day with dissolve
        show mt normal pioneer with dissolve
        "По пути к столовой, я встретилась с Олей."
        mt "Славь, после обеда поможешь мне в административном корпусе?"
        sl "Конечно."

        scene bg ext_dining_hall_away_day with dissolve
        "В столовую я дошла одна."
        stop ambience fadeout 1

        scene bg int_dining_hall_people_day with dissolve
        play ambience ambience_dining_hall_full fadein 3
        "Всего один столик был свободным. Остальные были уже полностью заняты."
        "Я взяла свою порцию и села за него."
        "Все ребята из моего отряда уже расселись вместе."
        "Поэтому обедала я в одиночестве и думала о том, что из себя представляет здание администрации, ведь осмотреться в нём времени не было."
        window hide
        stop ambience fadeout 3
        scene black with dissolve
        pause 2
        play ambience ambience_camp_center_day fadein 3 

    #Лена или ульяна
    if sl_m_end_un or sl_m_end_us:
        scene bg ext_admins_day with dissolve
        "Рядом со входом уже стояли Ольга Дмитриевна и Мику."
        show mt normal pioneer at left
        show mi normal pioneer at right
        with dissolve
        if sl_m_end_us:
            mt "Славя, я встретила Мику по дороге, но не успела сказать тебе."
            sl "Да ничего страшного."
        mt "Девочки, значит я сейчас буду заниматься бумагами, а вы пока вымойте пол и протрите пыль."

        scene bg ext_shed_day with dissolve
        "Мы пошли с Мику на склад за вёдрами, швабрами и тряпочками."
        "Затем я налила воду в ведро."

        stop ambience fadeout 1
        scene bg int_admins_day with dissolve
        play ambience ambience_int_cabin_day fadein 3
        "Пока Оля убиралась в одном кабинете, мы с Мику протирали пыль и мыли полы в другой."

    #Лена
    if sl_m_end_un:
        show mi normal pioneer with dissolve
        "Мику много и часто рассказывала про Японию и то, как к ней пришла в голову мысль написать ту песню, которую она пела Лене."
        "Слушать это всё было очень интересно, но она постоянно скакала с темы на тему."
        "Её мысли словно мчались по огромной автомагистрали, то и дело подрезая друг друга."
        "Я иногда пыталась что-то сказать, но после этого Мику начинала свой рассказ уже с другого места."
        "Так и проходила наша уборка, пока на полу оставалась хоть маленькая пылинка."
        window hide
        pause 3
        "Закончив, я отряхнула руки, а моя музыкальная приятельница положила тряпку в ведро."
        mi "Я, тогда, пойду, ой, скорее, побегу к себе в домик."
        hide mi with dspr
        "Ну, а я решила даром не тратить время и подмести площадь, пока не убрала метлу далеко."
        window hide
        stop ambience fadeout 1
        scene black with dissolve
        pause 1

        scene bg ext_square_day with dissolve
        play ambience ambience_camp_center_day fadein 3 
        window show
        "Дневное небо было покрыто облаками, но Солнце продолжало светить, словно их и не было."
        "Мимо довольно редко проходили пионеры."
        "Занятие довольно муторное и простое, но я и не заметила как быстро прошло время."
        "По положению Солнца, время сейчас было около 3-5 часов дня."
        "Неожиданно, ко мне подбежал Семён."
        show pi normal pioneer with dissolve
        me "Привет!"
        sl "Привет!"
        me "А ты Лену не видела?"
        th "Если считать, что после пробежки утром то нет."
        sl "Нет, а что?"
        me "Её с утра нигде нет. Не было на завтраке, не было на обеде."
        sl "Странно."
        me "Вот и я думаю, что, мягко говоря, странно. {w}Поможешь мне её найти?"
        sl "Ой, извини. {w}Может, попозже? А то у меня тут уборка..."
        "Семён как то странно посмотрел на меня и отодвинулся."
        hide pi with dspr
        "А затем и вовсе убежал."
        th "И чего он так беспокоится? Может стоило сказать ему, а то ещё чего сотворит?"
        "Я домела площадь и отправилась на поиски Семёна."
        window hide
        stop ambience fadeout 2
        scene black with dissolve
        pause 2
        "Но поиски ни к чему не привели."
        "Более того, он словно испарился вместе с Леной."
        "До ужина ещё было далеко {w}, и у меня впервые появилось свободное время."
        th "Никаких поручений {w}, никаких срочных дел{w}, ничего, что могло бы занять меня на весь солнечный день."
        th "Впервые я себя так почувствовала, наверное, с момента приезда в лагерь."
        th "Как я скучаю по родному дому, и как хорошо, что скоро увижусь со своими родственниками."
        window hide
        scene black with dissolve
        pause 2
        
        scene bg ext_boathouse_day with dissolve
        play ambience ambience_camp_center_day fadein 3 
        "Я решила прогуляться вдоль воды и насладиться последним деньком в лагере."
        "Находясь рядом с лодочной станцией, тихая обстановка навевает приятные ощущения единения с природой."
        "А звук постоянно колышашихся лодок от мимолётных колебаний воды словно уносит в тот момент, когда дедушка взял меня на рыбалку."
        th "Как странно, у меня остались воспоминания, но я не могу в точности воспроизвести как это всё было."
        "Я взошла на понтон, мой взгляд устремился вдаль, где над водной гладью возвышались два забавно названных острова."
        "Я разулась и спустила ноги с дебаркадера, краем ступней касаясь воды."
        "Приятная прохлада привела мысли в порядок."
        th "Лена и Семён и правда очень хорошая пара. Удивительно насколько точно они сошлись характерами."
        th "Конечно, у каждого свои тараканы в голове. Но уверена, что у них всё будет хорошо."
        th "А зная Лену, у них сложится прекрасный брак, если только не начнёт ревновать ко всем подряд."
        "Я хихикнула своей собственной мысли и уже собиралась уходить, как вдруг увидела, что в мою сторону направляется Шурик."
        show sh surprise pioner with dissolve
        sh "Славя {w}, ты что здесь делаешь?"
        sl "А я как раз собиралась уходить."
        "Он подошёл поближе и присел."
        sh "Что же это там всё-таки было в пещерах."
        "Я не сразу поняла про что он."
        sl "Ты это о чём?"
        show sh serious pioner with dspr
        sh "Я про старый лагерь."
        if go_to_sh:
            sh "Когда вы с Семёном помогли мне и вывели наружу."
        else:
            sh "Семён нашёл меня там, в шахте, я заблудился пока ходил по этому чёртовому лабиринту."
        show sh cry pioner with dspr
        sh "Я очень благодарен."
        sh "Если бы он тогда не пришёл..."
        "Он рефлекторно опустился лицом мне на плечо и я приобняла его."
        sl "Ну, всё же хорошо обошлось."
        sh "Но я даже сам не понимаю зачем туда пошёл."
        sh "Как будто не было места, где ещё пособирать транзисторов."
        sh "Хорошо, что хотя бы колонки под сценой есть."
        th "Я насторожилась."
        sh "Ну да. {w}Ими всё равно никто не пользуется."
        "Но в этот момент, видимо, он понял, что что-то сказал не то."
        show sh upset pioner with dspr
        sh "Забудь, что я сказал, мы всё равно ничего не успели."
        stop ambience fadeout 2
        play music music_list["awakening_power"] fadein 4
        sl "Так ты ещё и Серёжу в эту авантюру втянул?"
        show sh scared pioner with dspr
        sh "З-знаешь, я вспомнил, что у меня тут дела ещё есть какие."
        "Я резко остановила его."
        "Но он вдруг резко вскочил и куда-то побежал."
        "Я лишь успела привстать, как он уже оказался на суше и бежал так, что только пятки сверкали."
        "Мне не было смысла гнаться за ним, поэтому я просто обулась и решила сходить к сцене."
        window hide
        stop music fadeout 3
        hide sh
        scene black
        with dissolve
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        window show
        "Я добралась до сцены и уже хотела было проверить колонки на следы вскрытия."
        play sound sfx_dinner_horn_processed
        "Но тут вдруг раздался звук горна."
        "Время ужина."
        window hide
        pause 1

        stop sound fadeout 2
        scene bg int_dining_hall_sunset with dissolve
        play ambience ambience_dining_hall_full fadein 3
        window show
        "Зайдя внутрь столовой, я огляделась."
        "Пара столиков стояла абсолютно свободными. Остальные были уже заняты."
        "Я взяла свою порцию и села за один из них."
        "Неожиданно, со мной села Ульяна."
        show us normal pioneer with dissolve
        us "Привет, я подсяду?"
        sl "Конечно!"
        us "Спасибо."
        sl "А почему ты села со мной, а не со своей подругой?"
        show us laugh pioneer with dissolve
        us "Ну, просто мне так захотелось."
        "Ульянка замялась."
        show us normal pioneer with dspr
        us "Потому что ты вчера пришла ко мне и мне было не так одиноко."
        show us grin pioneer with dspr
        sl "Значит ты не будешь больше проказничать?"
        "Ульянка ехидно ухмыльнулась."
        us "Буду! Но не при тебе."
        sl "Ты неисправима."
        "Я погладила её по голове."
        show us normal pioneer with dspr
        sl "А если честно?"
        us "Что?"
        sl "Почему ты не села с Алисой?"
        us "Она решила не идти на ужин."
        sl "На неё не похоже."
        us "Во во! Сегодня все какие-то непохожие."
        us "Кстати, ты не видела Лену?"
        th "А вот за меня никто так не печётся, кроме Ольги Дмитриевны."
        sl "Не нашла больше кому пакостей устроить?"
        "Сказала я с насмешкой."
        show us angry pioneer with dspr
        us "Нуу!"
        sl "Вообще я её сегодня видела, но, я думаю, она вернётся вечером."
        show us normal pioneer with dspr
        us "Точно?"
        sl "Не станет же она ночевать в лесу."
        us "Ну, наверное."
        "Ульяна встала из-за стола."
        us "Ладно, я пойду тогда."
        th "Я и не заметила как она быстро поела."
        hide us with dspr
        "Уля выбежала пулей из столовой."
        stop ambience fadeout 1
        pause 1

        $ persistent.sprite_time = "night"
        $ night_time()
        play ambience ambience_forest_night fadein 3
        scene bg ext_path_night with dissolve
        "Я решила немного прогуляться напоследок."
        "Всё таки последний день завтра."
        th "Жаль конечно, что придётся уезжать из этого дивного места."
        th "Но как говорится, {i}В гостях хорошо, а дома лучше{/i}."
        "Походив ещё недолго и подышав свежим воздухом я пошла к себе."
        window hide
        stop ambience fadeout 2
        scene black with dissolve
        pause 2

        scene bg int_house_of_sl_night_light with dissolve
        play ambience ambience_int_cabin_night fadein 3
        window show
        "Я взяла свой дневник и принялась писать."
        window hide

    # Дневник
        $ set_mode_nvl()
        "Сегодня предпоследний день в «Совёнке», как жаль что смена вот-вот подойдёт к концу. Но я рада, что попала сюда, здесь я встретила много интересных людей."
        "С некоторыми даже подружилась."
        "Однако сегодня весь день не было Лены. В начале дня она куда-то ушла, не предупредив даже свою соседку. Всё это очень странно..."
        "Остальной день я была занята, помогая Оле и занимаясь уборкой по лагерю."
        "А обо всём что произойдёт завтра, дорогой дневник, я {s}расскажу{/s} напишу завтра."
        $ set_mode_adv()
    # Конец дневника

        window show
        "Я закрыла дневник, положила его под подушку и легла спать."
        show blink
        th "Утро вечера мудренее."
        "..."

    #Ульяна
    if sl_m_end_us:
        "Еще какое-то время Мику рассказывала о новой песне, что она придумала. Но она говорила так быстро, что я успевала понимать лишь отрывками."
        play sound sfx_dinner_horn_processed
        show mi normal pioneer with dissolve
        mi "Ой, как быстро я и не заметила."
        sl "Пойдём вместе?"
        mi "Конечно."
        "Я поставила метлу к стене и мы направились в столовую."
        window hide
        stop sound fadeout 1
        stop ambience fadeout 1
        scene bg ext_dining_hall_away_day with dissolve
        pause 1
        scene bg int_dining_hall_people_day with dissolve
        play ambience ambience_dining_hall_full fadein 3
        window show
        "Мы выбрали столик недалеко от входа и принялись за еду."
        "Точнее я, а Мику постоянно о чём-то говорила."
        "К нам подсел расстроенный электроник."
        show el normal pioneer at right
        show mi normal pioneer at left
        with dissolve
        sl "Привет! Что-то случилось?"
        el "Да нет, почему?"
        sl "Ты совсем раскис."
        el "Пустяки, просто настроение не очень."
        el "А вы, кстати, не видели Женю?"
        sl "Ну, сегодня я проснулась и сразу побежала на пробежку, а затем вернулась и мы вместе пошли с ней на линейку."
        sl "Должно быть в библиотеке сидит."
        el "Был, нет её там."
        sl "Попробуй ещё где-нибудь поискать, например здесь."
        el "Хорошо."
        "Мику встала из-за стола."
        mi "Ладно, я тогда пойду, мы в клубе с Алисочкой решили встретиться."
        sl "Да, пока."
        hide mi with dspr
        "Я тоже закончила трапезу и вышла из-за стола."
        window hide
        stop ambience fadeout 2
        scene black with dissolve
        pause 1

        scene bg ext_square_day with dissolve
        play ambience ambience_camp_center_day fadein 3
        window show
        "Я решила не тратить время даром, а подмести площадь, пока есть метла."
        scene bg ext_admins_day with dissolve
        "Я вернулась к зданию администрации и захватила метёлку."
        "День был солнечный, самое то для прогулки."
        scene bg ext_square_day with dissolve
        show sh normal pioneer with dissolve
        "Я встретилась взглядами с Шуриком."
        sl "Привет, куда-то идёшь?"
        sh "Да. {w}Не видела Электроника?"
        sl "Последний раз я его видела в столовой"
        sh "У меня ключ от клубов куда-то делся, а он дверь закрыл. Мне пришлось через окно вылезать."
        "Я рассмеялась."
        show sh upset pioneer with dspr
        sh "Что смешного?"
        sl "Может он какой-то розыгрыш тебе устроил, а ты недотерпел и вышел раньше времени?"
        sh "Ещё чего! Зачем ему это всё?"
        sl "Не знаю."
        "Честно ответила я."
        show sh normal pioneer with dspr
        sh "Вот и я о том же. {w}Значит не видела, говоришь?"
        sl "Нет."
        sh "Ладно, пойду ещё похожу."
        hide sh with dspr
        sl "Не потеряйся!"
        "Крикнула я ему вслед."
        stop ambience fadeout 3
        scene black with dissolve
        "..."
        window hide

        play ambience ambience_camp_center_day fadein 3
        scene bg ext_square_day with dissolve
        window show
        "Когда всё было закончено, я пошла отнести метлу на склад."
        scene bg ext_shed_day with dissolve
        show mt normal pioneer with dissolve
        "По пути мне снова встретилась Оля."
        mt "Работаешь, Славя?"
        sl "Да вот, метлу на склад отношу."
        mt "Ну, тогда думаю на сегодня ты свободна."
        sl "Правда?"
        mt "Скоро будет конец смены, поэтому, почему бы нам всем не отдохнуть лишний раз?"
        sl "Значит, и вчерашнее наказание Ульяне снимешь?"
        "С ехидством спросила я у неё."
        show mt laugh pioneer with dspr
        mt "Славя, ты лучше своими делами занимайся."
        "Ответила мне Оля с улыбкой, но это не звучало грубо, а скорее наоборот, почти по-дружески."
        hide mt with dspr
        "Я открыла склад и поставила метлу рядом с остальными инструментами."
        scene bg ext_square_day with dissolve
        show pi normal pioneer with dissolve
        "Я шла, чтобы отнести вёдра из администрации на склад, но по пути мне встретился Семён."
        "Он был очень напряжён."
        me "Не знаешь, где Алиса?"
        sl "Знаю, а что?"
        me "Так скажи!"
        "Я решила не спорить с ним."
        sl "В музыкальном кружке."
        hide pi with dspr
        "Семён пошёл дальше, даже не поблагодарил и не попрощался."
        "А я, взяв вёдра, отнесла их на склад и пошла на ужин, который должен был уже быть с минуты на минуту."
        window hide
        stop ambience fadeout 2
        scene black with dissolve
        pause 1

        $ persistent.sprite_time = "day"
        $ day_time()
        scene bg int_dining_hall_people_day with dissolve
        play ambience ambience_dining_hall_full fadein 3
        show mi normal pioneer with dissolve
        window show
        "Я решила занять место рядом с Мику."
        sl "Привет, не возражаешь?"
        mi "Нет, конечно, садись, конечно."
        "Меня немного позабавил лексический повтор от японки и я улыбнулась."
        show mi normal pioneer:
            linear 1.0 left
        show dv sad pioneer at right with dissolve
        "К нам подсела Алиса. Лицо у неё было как будто заплаканное, или мне так казалось."
        sl "Алиса, всё хорошо?"
        dv "Да, всё хорошо."
        mi "Мы же с тобой из клуба..."
        show dv angry pioneer at right with dspr
        dv "Мику, помолчи."
        "Грубо заткнула её Алиса."
        sl "Не хочешь говорить?"
        show dv sad pioneer at right with dspr
        dv "Не хочу."
        "Остаток обеда мы провели безмолвно, и даже Мику."
        window hide
        pause 1
        stop ambience fadeout 2
        scene black with dissolve
        pause 1

        $ persistent.sprite_time = "night"
        $ night_time()
        scene bg ext_square_night with dissolve
        play ambience ambience_camp_center_night fadein 3
        window show
        "Время клонилось к вечеру, делать было нечего."
        "Я решила немного прогуляться перед сном."
        "Я села на лавку."
        "Время было ещё не совсем позднее, поэтому то и дело проходили мимо пионеры. Кто-то шёл под руку, кто-то просто в компании друзей.{w} Но нигде не было видно Семёна."
        th "Конечно, Оля бывает иногда строга к Ульяне. Но ведь она ещё ребёнок, кому как ни ей это знать, ведь наверняка уже не первый год работает в «Совёнке»."
        "Кстати, об Ульяне.."
        show mt normal pioneer with dissolve
        mt "Славя, не заснула тут?"
        sl "Нет, Оля, а что такое?"
        mt "Семён пропал."
        mt "Кстати, а ты не видела Ульяну?"
        sl "Нет.."
        show mt sad pioneer with dspr
        mt "Началось в колхозе утро."
        sl "Может, объявятся скоро?"
        mt "На это нет времени, завтра уже уезжаем, надо срочно их найти!"
        "Я мигом встала и мы направились к складу."
        window hide
        stop ambience fadeout 2
        scene black with dissolve
        pause 1
        scene bg ext_square_night
        show mt normal pioneer
        with dissolve
        play ambience ambience_camp_center_night fadein 3
        window show
        "Мы забрали фонарики и встали на площади."
        mt "Так, мысленно подели лагерь пополам: ты обыщешь сцену, библиотеку, медпункт, столовую, спортплощадку и станцию, а я остальное."
        sl "Хорошо."
        window hide
        stop ambience fadeout 2
        scene black with dissolve
        pause 1
        scene ext_boathouse_night with dissolve
        play ambience ambience_camp_center_night fadein 3
        window show
        "Когда я уже заканчивала осмотр, прошло добрых полчаса, а может и больше."
        "Я вернулась на площадь с докладом Оле."
        scene bg ext_square_night
        show mt normal pioneer
        with dissolve
        sl "Их нигде нет."
        mt "Я тоже не нашла."
        mt "Ладно, сейчас не время поднимать весь лагерь на уши. Завтра разберёмся."
        window hide
        stop ambience fadeout 1

        $ persistent.sprite_time = "day"
        $ day_time()
        scene bg int_house_of_sl_night_light with dissolve
        play ambience ambience_int_cabin_night fadein 3
        window show
        "Я взяла свой дневник."
        window hide

    # Дневник
        $ set_mode_nvl()
        "Сегодня предпоследний день в «Совёнке», как жаль, что смена вот-вот подойдёт к концу. Но я рада, что попала сюда, здесь я встретила много интересных людей."
        "С некоторыми даже подружилась."
        "Например с такими замечательными ребятами, как Серёжа и Саша."
        "Я надеюсь, они обязательно помирятся, ведь они друзья не разлей вода."
        "Весь остальной день я заняла полезной работой по лагерю. Пожалуй, завтра я проведу весь день в отдыхе, если не появится каких-нибудь новых поручений."
        $ set_mode_adv()
    # Конец дневника

    if sl_m_end_us or sl_m_end_sl:
        play sound sfx_open_door_1
        show mz normal pioneer glasses with dissolve
        window show
        "В домик вошла Женя."
        mz "Спать ещё не собираешься?"
        sl "Да вот, уже застелилась."
        mz "Спокойной ночи."
        hide mz with dspr
        "Она разделась и легла с головой под одеяло."
        th "И как ей не жарко летом?"
        stop ambience fadeout 2
        show blink
        "Я тоже легла спать."
        "..."

    window hide
    stop ambience fadeout 1
    play ambience ambience_grasshoper_clean fadein 3
    scene bg ext_camp_entrance_fog
    show prologue_dream
    with dissolve
    pause 2
    window show
    voice "Время пришло."
    window hide
    pause 1
    scene black with dissolve
    stop ambience fadeout 1
    pause 1
    if sl_m_Full:
        jump slavyana_mod__day7_alt
    jump slavyana_mod__launcher0
