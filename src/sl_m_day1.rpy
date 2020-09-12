#alpha v.0.1 (-)
#alpha v.0.3 (-)
#beta v.0.5 (-)
#beta v.0.7 (-)
#beta v.0.9 (-)
#release v.1.0

init:
    $ sl_m_day1_help_od = False
    $ sl_m_sp1 = None
    $ sl_m_al1 = None
    $ sl_m_mpr1 = None
    $ sl_m_day1_not_now = False
    $ sl_m_day1_map_od = False
    $ sl_m_day1_map_mh = False
    $ sl_m_day1_map_ul = False
    $ sl_m_day1_other = False
    $ sl_m_day1_al_que = False

label slavyana_mod__day1:
    pause(3)
    $ backdrop = "days"
    $ new_chapter(1, u"Славя. День первый")
    $ save_name = (u'Славя. День первый')
    $ day_time()
    $ persistent.sprite_time = "day"

#часть 1
    #домик
    scene black with dissolve
    pause (2)
    show unblink
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_sl_day with dissolve
    pause (3)
    window show
    th "Замечательное начало прекрасного нового дня!"
    "Подумала я, поднимаясь с кровати рано утром."
    th "Сколько ещё нужно сделать, сколько всего уже сделано!"
    "На соседней кровати лежала и посапывала Женя.{w} Часы показывали шесть тридцать утра, так что будить её не было смысла."
    th "Сама проснётся через полчаса. И как только ей удаётся каждый день вставать ровно в это время?"
    "Я оделась и вышла на крыльцо."
    stop ambience fadeout 3
    window hide
    play sound sfx_close_door_campus_1

    #улица-пробежка
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_house_of_sl_day with dissolve
    window show
    "Улица встретила меня прохладой и свежестью. На траве блестела роса, а в небе летели редкие птицы."
    th "Идеальная погода для утренней пробежки!{w} А заодно и лагерь осмотрю, как меня вчера Ольга Дмитриевна просила."
    scene bg ext_houses_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    "Лагерь был как всегда пуст."
    th "И почему никто не хочет выходить с утра из домиков? Ведь здесь так замечательно!"
    scene bg ext_house_of_mt_day with dissolve
    "Пробегая около дома Ольги Дмитриевны, я постучала к ней в дверь."
    window hide
    play sound sfx_knock_door2
    pause (2)
    window show
    "Никто не ответил."
    scene bg ext_houses_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    th "И она тоже спит! «Ну, а каков командир, таковы и солдаты!»"
    "Это фраза моего папы. Он военный и знает ещё много мудрых фраз.{w} А ещё из-за него мы часто переезжали, хотя последние пять лет живём в Якутске и никуда не переезжаем."
    scene bg ext_path_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    th "Вот бы так было подольше...{w} А то всегда так – только успеваю с кем-то подружиться и опять переезд...{w} Впрочем, не нужно думать о грустном! Я сейчас в лагере, вокруг замечательная природа, так что я могу просто наслаждаться происходящим!"
    th "Ой, а где это я?"
    "Я наконец-то стала следить за дорогой и обнаружила, что забежала в лес. К счастью, из-за деревьев показались умывальники, и я вышла к ним."
    scene bg ext_washstand_day with dissolve

    #Ульяна-забег
    "На знакомой площадке я увидела чьи-то ярко-рыжие, ближе к красным волосы."
    th "Ульяна тоже не спит по утрам?{w} Вот и замечательно, хотя бы кто-то понял, что нужно вставать пораньше!"
    stop ambience fadeout 2
    play music music_list["went_fishing_caught_a_girl"] fadein 3
    show us surp1 sport at center with dissolve
    sl "Физкульт-привет!"
    us "Физкульт-ура!{w} Как твоя утренняя пробежка?"
    sl "Отлично! Уже три круга проделала, последний остался..."
    show us smile sport at center with dspr
    us "Неплохо.{w} Но сколько бы ты не старалась, меня догнать все равно не сможешь!"
    sl "Ну, это ещё не факт."
    us "А давай поспорим, что этот круг я пробегу быстрее тебя!"
    sl "Нет, спорить я не буду."
    show us surp1 sport at center with dspr
    us "Ага, значит все таки не догонишь!"
    sl "А если догоню?"
    us "А вот и нет!"
    sl "А вот и да!"
    us "А ты докажи!"
    sl "Хорошо, но никакого спора не будет."
    show us dontlike sport at center with dspr
    us "Так не интересно!"
    "Ульяна скорчила обиженное лицо."
    sl "Так мы бежим или нет?"
    show us smile sport at center with dspr
    us "Ладно уж, побежали.{w} Но я всё равно буду быстрее тебя!"
    hide us with dspr
    "Я описала маршрут забега, и мы встали на старт."
    sl "Начинаем по моей команде."
    play music music_list["always_ready"] fadein 3
    sl "Три..."
    sl "Два..."
    sl "Один..."
    sl "Старт!"
    scene bg ext_houses_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve     
    "Мы резко рванулись с места.{w} Я бежала немного впереди Ульяны, которая явно была не готова к забегу."
    scene bg ext_clubs_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve
    "Мы бежали через клубы..."
    scene bg ext_houses_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve
    "Затем повернули к домикам..."
    scene bg ext_square_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve
    "На площади Ульяна всё же догнала меня, и даже начала обгонять."
    th "И откуда у неё только силы взялись?{w} Или это я уже устаю?.."
    scene bg ext_dining_hall_away_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve
    "Возле столовой между нами был уже ощутимый отрыв."
    scene bg ext_dining_hall_near_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve
    "Около крыльца был поворот обратно, на котором я словно получила второе дыхание и начала сокращать отрыв."
    scene bg ext_square_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve
    "Оказавшись снова на площади, я уже почти догнала Ульяну, но тут она резко ускорилась и я снова отстала."
    scene bg ext_washstand_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat
    with dissolve
    "Спустя пару секунд мы уже были около умывальников, где у нас был финиш."
    stop music fadeout 1
    show mt normal pioneer far at center with dissolve
    play music music_list["revenga"] fadein 3
    "Как назло, именно сейчас там была Ольга Дмитриевна.{w} И в неё на полном ходу влетела Ульяна!"
    hide mt with dspr
    play sound sfx_fall_grass
    "Я подбежала к ним."
    scene bg ext_washstand_day
    menu:
        "Помочь Ольге Дмитриевне":
            $ sl_m_day1_help_od = True
            sl "Ольга Дмитриевна, вам не больно? Вы не ушиблись? Давайте я вам помогу!"
            show mt angry pioneer:
                xalign 0.5 ypos 1.0
                linear 2.0 yalign 0.5
            with dspr
            "Я помогла вожатой встать, а Ульяна оставалась лежать на земле."
            th "Ей тоже нужно было бы помочь, но сейчас её отчитывает вожатая..."
        "Помочь Ульяне":
            show us shy sport:
                xalign 0.28 ypos 1.0
                linear 2.0 yalign 0.5
            show mt angry pioneer:
                xalign 0.72 ypos 1.0
                linear 2.0 yalign 0.5
            with dspr
            "Я подошла к Ульяне и помогла ей подняться. Ольга Дмитриевна поднялась сама."
            th "Ей тоже нужно было бы помочь, но ведь Ульяна ещё ребёнок, ей помощь требовалась больше..."
    mt "Ульяна! {w}Что все это значит?!"
    us "Мы бежали, затем поворот, потом вы, я не успела затормозить, и в общем..."
    mt "Тебя разве не учили смотреть по сторонам когда бежишь?{w} Не видишь что-ли, что человек идет?!"
    stop music fadeout 3
    play ambience ambience_camp_center_day fadein 2
    if not sl_m_day1_help_od:
        show us shy2 sport:
            xalign 0.28 ypos 1.0 yalign 0.5
        with dspr
    us "Простите... Я так больше не буду..."
    if not sl_m_day1_help_od:
        show mt normal pioneer:
            xalign 0.72 ypos 1.0 yalign 0.5
        with dspr
    else:
        show mt normal pioneer:
            xalign 0.5 ypos 1.0 yalign 0.5
        with dspr
    mt "Ладно, так и быть, прощаю."
    if sl_m_day1_help_od:
        show us shy sport:
            xalign 0.28 ypos 1.0
            linear 2.0 yalign 0.5
        show mt normal pioneer:
            yalign 0.5 xpos 0.5
            linear 2.0 xalign 0.72
        with dspr
        "Ульяна поднялась с земли и отряхнулась."
    mt "Девочки, вы же помните, что скоро у нас линейка?"
    sl "Конечно помним!"
    show mt smile pioneer:
        xalign 0.72 ypos 1.0 yalign 0.5
    with dspr
    mt "Ну вот и хорошо.{w} У вас есть время, чтобы вернуться в домики и надеть форму."
    show mt angry pioneer:
        xalign 0.72 ypos 1.0 yalign 0.5
    with dspr
    mt "Ульяна, а ты разбуди Двачевскую.{w} И пусть она только попробует снова не явиться!"
    show us normal sport:
        xalign 0.28 ypos 1.0 yalign 0.5
    with dspr
    us "Постараюсь..."
    show mt normal pioneer:
        xalign 0.72 ypos 1.0 yalign 0.5
    with dspr
    mt "Ладно, мне пора идти.{w} Через десять минут построение на площади, не опаздывайте!"
    hide mt with dspr
    sl "Я тоже уже ухожу.{w} До встречи на линейке!"

    #переход
    scene bg ext_square_day with dissolve
    th "И всё-таки зря я ввязалась во всё это..."
    stop ambience fadeout 2
    window hide
    scene black with dissolve
    pause (3)
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_house_of_sl_day with dissolve
    window show
    "По пути я встретила всего лишь нескольких пионеров, устало плетущихся к умывальникам."
    th "Как же так? Ведь скоро линейка, а они только идут умываться!{w} Да и где же все остальные? Неужели ещё спят?"
    "Я правда не понимала, как так можно поступать. Ведь мы же пионеры! {i}«Клич пионера: \"Всегда будь готов!\"»{/i}, как поётся в одной песне, а они..."
    stop ambience fadeout 2
    play sound sfx_open_dooor_campus_1
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_sl_day with dissolve
    "В моём домике было пусто.{w} Часы показывали 7:15."
    th "Женя как всегда в своём репертуаре.{w} Такая пунктуальная!"
    "Быстро переодевшись, я вышла и направилась в сторону площади."
    stop ambience fadeout 3
    window hide
    scene black with dissolve
    pause (2)

    #линейка
    play ambience ambience_medium_crowd_outdoors fadein 3
    play music music_list["everyday_theme"] fadein 3
    scene bg ext_square_day with dissolve
    window show
    "Когда я пришла, там уже собралось довольно много пионеров."
    show mt normal pioneer with dissolve
    mt "Вижу, все уже в сборе."
    stop ambience fadeout 1
    "При виде Ольги Дмитриевны наш отряд выстроился в одну шеренгу."
    mt "Все, кроме Алисы."
    show mt angry pioneer with dspr
    mt "Ульяна!{w} Я же просила тебя ее разбудить!"
    us "А она не может.{w} У нее это...{w} живот болит!"
    mt "А не врешь?"
    us "Честное пионерское!"
    show mt normal pioneer with dspr
    mt "Ладно, тогда пускай поправляется."
    mt "А теперь перейдем непосредственно к теме..."
    "Далее последовал монолог вожатой про важность нашей пионерской деятельности и про требования к нам. Несмотря на то, что я была помощницей вожатой, я её не особенно слушала.{w} Ольга Дмитриевна говорит одно и то же каждое утро, так что скоро и я смогу рассказывать этот текст без запинок. Да и остальные, наверное, тоже."
    window hide
    pause (2)
    stop music fadeout 3
    show mt normal pioneer with dspr
    play music music_list["i_want_to_play"] fadein 3
    window show
    mt "...И напоследок важная новость: сегодня к нам в лагерь приезжает новенький."
    th "Ах да, новенький...{w} Мне ведь его встречать после обеда!"
    us "А когда он приедет?"
    mt "После обеда."
    us "Здорово!{w} А как его зовут?{w} И сколько ему лет?"
    show mt grin pioneer with dspr
    mt "А ты подойди к нему и познакомься."
    us "Вот еще!{w} Пускай сам первый подходит!"
    stop music fadeout 3
    play ambience ambience_camp_center_day fadein 2
    play sound music_list["dinner_horn_processed"]
    "В этот момент прозвучал сигнал призыва на завтрак."
    show mt smile pioneer with dspr
    mt "Все, ребята, линейка окончена!{w} Можете расходиться."

    #Ольга Дмитриевна-завтрак
    "Площадь стала понемногу пустеть. Все направлялись в столовую.{w} Я же догнала Ольгу Дмитриевну."
    show mt normal pioneer at center with dspr
    mt "Славя! Как хорошо, что ты подошла! Ты ведь помнишь, что тебе встречать новенького после обеда?"
    sl "Конечно, Ольга Дмитриевна!"
    mt "Вот и хорошо.{w} И ещё... Раз уж после завтрака нет никаких важных поручений, то, может быть, сходим на пляж?"
    sl "Хорошо!"
    scene bg ext_dining_hall_near_day
    show mt normal pioneer at center
    with dissolve
    "Мы дошли до столовой."
    mt "А теперь иди и подкрепись. День обещает быть интересным."
    sl "Да, Ольга Дмитриевна, уже иду!"
    th "Хорошая всё-таки у нас вожатая!"
    stop ambience fadeout 2
    play sound sfx_open_door_1

    #завтрак-Женя
    play ambience ambience_dining_hall_full fadein 2
    scene bg int_dining_hall_people_day with dissolve
    "Внутри столовой, как всегда, было многолюдно. Но свободные места ещё были и я заняла одно из них, рядом с Женей."
    show mz normal glasses pioneer at center with dissolve
    sl "Привет! Со вчерашнего дня не виделись!"
    mz "Привет. Ну и каково оно, с Ульяной наперегонки?"
    sl "Ты-то откуда знаешь?"
    mz "Видела вас, пока к умывальникам ходила."
    sl "Да всё хорошо, только если бы она под конец вожатую не сшибла."
    mz "Эх, зря я ушла.{w} Ведь видела, как вы мчались обратно!"
    sl "Ну ничего, может ещё как-нибудь увидишь!"
    mz "Да, если ты опять согласишься на подобную глупость.{w} Ладно, пошла я в библиотеку, а то уже опаздывать начинаю."
    sl "Увидимся!"
    hide mz with dissolve
    th "Нет, всё же иногда она слишком пунктуальна.{w} Слишком."
    th "Но насчёт глупости Женя права. В следующий раз нужно будет всё получше обдумать."
    window hide
    pause (2)
    stop ambience fadeout 2
    play sound sfx_close_door_1
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_dining_hall_near_day with dissolve
    window show
    th "Отзавтракала, теперь можно и на пляж!{w} Вода должна быть в самый раз!"
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (3)

    #домик
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_sl_day with dissolve
    window show
    "Дома меня ждала пустота.{w} Неудивительно, ведь Женя сразу помчалась в библиотеку."
    "На одной из полок шкафа меня ждал купальник. Рядом с ним лежал блокнот."
    show bknt_clear at truecenter with dspr
    th "Пустой.{w} Может, стоит туда что-нибудь записывать?"
    play sound_loop pen_write
    show bknt_w1 at truecenter with dissolve2
    th "Итак, мой восьмой день пребывания в Совёнке. Погода замечательная..."
    stop sound_loop
    th "А что дальше?{w} Нет, лучше я этим займусь в конце дня."
    hide bknt_w1
    hide bknt_clear
    with dspr
    $ persistent.sl_m_bknt1 = True
    play sound sfx_knock_door2
    "Я переоделась, и тут в дверь домика постучали."
    mt "Славя! Ты там?"
    sl "Да, уже выхожу!"
    stop ambience fadeout 2
    play sound sfx_close_door_campus_1
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_house_of_sl_day
    show mt normal panama pioneer at center
    with dissolve
    "На улице меня ждала наша вожатая в своей любимой панаме.{w} По крайней мере, она часто её надевала, а на пляже я Ольгу Дмитриевну никогда и не видела без неё."
    mt "Что-то ты уж больно долго."
    sl "Да нет, это вы слишком быстро."
    "Когда ты любимица вожатой, можно позволять себе и такие высказывания."
    mt "Ну ладно, хватит пререкаться, пошли уже."
    "Cказала Ольга Дмитриевна и поманила меня за собой."

    #пустота
    scene bg ext_houses_day with dissolve
    "Лагерь был пуст."
    th "Нет, они даже сейчас не хотят выйти на улицу! Ну как так можно!.."
    th "Хотя... Может, хотя бы на пляже кто-то есть?"
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (3)

    #пляж
    play music music_list["sweet_darkness"] fadein 3
    scene bg ext_beach_day
    show mt normal panama pioneer at center
    with dissolve
    window show
    "Но на пляже было также немноголюдно.{w} Если говорить точнее, то совсем пусто."
    th "И здесь? Ну как можно быть такими лентяями?!"
    #пичаль-бида, некрасиво выглядит
    "Быстро скинув одежду, я забежала в воду. Ольга Дмитриевна зашла следом."
    show mt surprise swim at center with dspr
    sl "Замечательная тёплая вода!"
    mt "Тёплая? Как по мне, так очень даже и холодная!"
    sl "Ольга Дмитриевна, вы не забывайте, что я уже несколько лет живу на Севере, и ваше «холодно» для меня «почти тепло»."
    show mt normal swim at center with dspr
    mt "Да уж, и как я только могла...{w} Плыви за мной!"
    hide mt with dspr
    "Доплыв почти до самых буйков, Ольга Дмитриевна остановилась."
    show mt normal swim at center with dspr
    mt "Слушай, Славя...{w} Может, ну его, этот официоз? Называй меня просто Олей и обращайся на «ты». Но не при посторонних, конечно же."
    $ sl_m_meet('mt','Оля')
    sl "Хорошо, Ольга... Оля."
    show mt smile swim at center with dspr
    mt "Вот и замечательно!{w} Смотри, там ещё кто-то пришёл!"
    "Она показала в сторону берега.{w} Там были Ульяна и Алиса."
    sl "Ну хотя бы кто-то догадался выйти из домиков!"
    show mt normal swim at center with dspr
    mt "Да уж! А то весь лагерь пустует, несмотря на разгар рабочего дня!{w} Как ты думаешь, может стоит придумать что-нибудь, чтобы занять их?"
    sl "Было бы неплохо. Только не перетруждайте, хотелось бы, чтобы все уехали с хорошими воспоминаниями."
    mt "Ну, это само собой разумеется. Да и с тобой я буду советоваться, как же без этого?"
    sl "Судя по всему, никак!"
    "Я рассмеялась."
    if sl_m_day1_help_od:
        mt "Слушай...{w} Вообще, хорошо, что ты здесь! Мне есть с кем посоветоваться, всегда есть та, которая поможет мне..."
    else:
        mt "Слушай...{w} Вообще, хорошо, что ты здесь! Мне всегда есть с кем посоветоваться..."
    "Я покраснела."
    sl "Оля, ну не надо таких речей!"
    show mt smile swim at center with dspr
    mt "Ну ладно, больше не буду, стеснительная!"
    sl "Кто? Я?"
    mt "Да."
    play sound sfx_water_splash
    play sound sfx_water_emerge
    sl "Ну тогда получай!"
    "В воздух поднялся фонтан из брызг, красиво переливающихся на солнечном свету.{w} Уже через секунду вся эта красота опустилась на вожатую, чего она явно не ожидала."
    show mt surprise swim at center with dspr
    mt "Ах так..."
    show mt smile swim at center with dspr
    play sound sfx_water_splash
    play sound sfx_water_emerge
    "Теперь такая же красота полетела в мою сторону."
    window hide
    hide mt with dspr
    play sound sfx_water_splash
    play sound sfx_water_emerge
    pause (2)
    play sound sfx_water_splash
    play sound sfx_water_emerge
    pause (2)
    play sound sfx_water_splash
    play sound sfx_water_emerge
    pause (2)
    window show
    "Мы ещё недолго побрызгались, а потом обнаружили, что плаваем уже очень долго и решили выходить из воды."
    "За это время Ульяна уже успела задремать, да и Алиса была близка к этому состоянию."
    th "Не буду им мешать."
    stop music fadeout 3

    #площадь
    play music music_list["everyday_theme"] fadein 3
    scene bg ext_square_day
    show mt normal panama pioneer at center
    with dissolve
    "По пути с пляжа Ольга Дмитриевна рассказывала мне о списке дел на неделю:"
    mt "Итак, ещё раз напоминаю, после обеда приезжает новенький. Твоя задача – встретить его и направить ко мне."
    sl "Хорошо."
    mt "Потом, на третий день у нас дискотека."
    sl "Да?"
    show mt grin panama pioneer at center with dspr
    mt "Да, а ты, как я вижу, рада?"
    sl "Конечно! Как можно не любить дискотеки?"
    show mt normal panama pioneer at center with dspr
    mt "Полностью с тобой согласна.{w} Но не забывай об обязанностях. Ведь тебе же её и готовить."
    sl "Вот всегда вы нальёте ложку дегтя в бочку мёда!"
    show mt smile panama pioneer at center with dspr
    mt "Ну, ты же ведь будешь не одна. С тобой точно будут ещё кибернетики и... может даже и новенький.{w} Если он, конечно, не окажется дистрофиком, в чём я сильно сомневаюсь."
    stop music fadeout 1
    play music music_list["awakening_power"] fadein 1
    show mt normal panama pioneer at center with dspr
    mt "Кстати о кибернетиках... Это не Серёжа бежит?"
    "Я посмотрела в дальний конец площади. И точно, Электроник мчался во весь опор, как будто забыл выключить паяльник."
    stop music fadeout 1
    play ambience ambience_camp_center_day fadein 2
    sl "И что это с ним?"
    mt "Теперь твоя задача – это выяснить. Потом придёшь ко мне, расскажешь.{w} Мне ведь тоже интересно."
    hide mt with dissolve
    "С этими словами она пошла в сторону домиков, а я отправилась к кружкам, выяснять произошедшее с Электроником."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (2)

    #клуб-Электроник
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_clubs_day with dissolve
    window show
    "Когда я подошла, его уже не было около здания кружков."
    th "А он быстро бегает!"
    stop ambience fadeout 2
    play sound sfx_open_door_clubs
    scene bg int_clubs_male_day with dissolve
    "Внутри здания тоже никого не оказалось."
    play sound sfx_open_door_clubs_nextroom
    scene bg int_clubs_male2_night_nolight

    #додумывайте сами где и как он сидит
    play ambience ambience_medstation_inside_day fadein 2
    show el shocked pioneer at center
    with dissolve
    "Я зашла в кладовку и увидела Электроника, сидящего на полу и обвившего руками ноги."
    el "С-Славя? Ч-что ты здесь д-делаешь?"
    sl "Да вот узнать пришла, куда ты так бежал."
    "Он молчал."
    sl "Ну же, не бойся, говори, что произошло."
    el "А-Алис-с-са..."
    sl "Что Алиса?"
    el "На п-п-пляж-ж-же..."
    th "Уже интересно."
    sl "Говори целиком, хватит дрожать."
    show el upset pioneer close at center with dissolve
    "Я села рядом с ним и приобняла его.{w} Это сработало, и он перестал дрожать."
    el "Я пришёл на пляж, искупаться решил, а там эта чёртова Дваче!{w} Она с меня шорты стащила и... выкинула их к буйкам!"
    "Я даже не знала что сказать."
    th "Это конечно в духе Алисы, но не слишком ли?"
    sl "Ты не бойся, она с тобой больше ничего не сделает."
    el "Точно?"
    sl "Обещаю, я поговорю об этом с вожатой."
    show el upset pioneer at center with dissolve
    "Я встала и пошла к двери."
    el "Спасибо, Славя..."
    sl "Да не за что. Так бы на моём месте поступил каждый."
    th "Кроме Алисы."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (3)

    #давайте поможем Славе найти Ольгу Дмитриевну!
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_houses_day with dissolve
    window show
    "Я попыталась найти Ольгу Дмитриевну, но её нигде не было."
    play sound music_list["dinner_horn_processed"]
    th "Потом расскажу."
    "Подумала я под звуки обеденного горна."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (2)

    #обед
    play ambience ambience_dining_hall_empty fadein 2
    scene bg int_dining_hall_day with dissolve
    window show
    "К счастью, я пришла одной из первых и успела занять целый свободный стол.{w} Вскоре ко мне подсела Лена."
    show un normal pioneer at center with dissolve
    sl "Привет!"
    un "Привет..."
    th "Вот странный человек. Печалится всё время, непонятно из-за чего. Ведь всё вокруг так замечательно!"
    sl "Как дела?"
    un "Хорошо..."
    hide un with dspr
    "Судя по всему, Лена не была настроена на диалог, поэтому я предпочла быстрее доесть свою порцию и выйти на улицу."
    window hide
    pause (2)
    stop ambience fadeout 2
    play sound sfx_close_door_1

    #на пути к воротам
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_dining_hall_near_day with dissolve
    window show
    th "Так, что у нас дальше?{w} Встречать новенького, точно!"
    window hide
    scene bg ext_square_day with dissolve
    window show
    "По пути к воротам, я вспомнила, что Ольга Дмитриевна просила меня как-нибудь заглянуть на пристань, проверить всё ли там в порядке."
    th "Вот сейчас встречу новенького и туда забегу."
    window hide
    scene black with dissolve
    pause (3)
    scene bg ext_clubs_day with dissolve
    window show
    "И вот, я уже у ворот. Остаётся только выйти за них и подождать новенького."
    stop ambience fadeout 2

    #и тут появляется Семён, весь такой офигевший!
    play ambience ambience_ext_road_day fadein 3
    scene bg ext_camp_entrance_day
    show pi shocked coat at center
    with dissolve
    "К счастью, ждать его не пришлось. Он уже собирался сам войти в лагерь, но застыл на месте при виде меня.{w} Я подошла поближе и улыбнулась."
    sl "Привет, ты, наверное, только что приехал?"
    $ sl_m_meet('me','Новенький')
    $ sl_m_sp1 = renpy.random.choice(['talk', 'mute'])
    if sl_m_sp1 == 'mute':
        "Но он не отвечал."
        sl "Я что-то не то сказала?"
        "Он продолжал стоять и смотреть на меня, как будто онемел, но наконец заговорил:"
        me "Ну… да…"
        sl "Что?"
        show pi normal coat at center with dspr
        me "А, нет, я в смысле, что {i}только что приехал{/i}."
        "Теперь же он говорил очень быстро, словно стараясь наверстать упущенное."
    elif sl_m_sp1 == 'talk':
        me "Ну… да…"
    sl "Что же, добро пожаловать!"
    th "Интересно, почему он в пальто и зимних ботинках? Может, тоже с севера?"
    show pi smile coat at center with dspr
    "Он усмехнулся."
    sl "Что смешного?"
    show pi surprise coat at center with dspr
    me "Н... ничего..."
    sl "Ну и славно."
    me "А ты, наверное, знаешь…"
    sl "Тебе к вожатой надо, она всё расскажет!"
    th "Надеюсь, Оля вернулась, а то я человека к ней пошлю, почём зря..."
    sl "Смотри. Сейчас идёшь прямо-прямо, доходишь до площади, затем налево, дальше будут домики."
    "Я показала ему примерное направление."
    sl "Ну спросишь у кого-нибудь, где домик Ольги Дмитриевны!"
    me "Я… эээ…"
    sl "Всё понял?"
    th "Он ведь кивнул, да?"
    sl "А мне пора."
    "Я помахала ему рукой и ушла за ворота."
    stop ambience fadeout 2
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_clubs_day with dissolve
    th "Он не выглядит глупым, так что дорогу сам найдёт."
    th "А ещё я забыла спросить, как его зовут. Ну ничего, ещё успею."
    stop ambience fadeout 2
    window hide
    scene black with dissolve
    pause (3)

    #пристань
    play ambience ambience_boat_station_day fadein 3
    scene bg ext_boathouse_day with dissolve
    window show
    th "Пристань. Как же давно я здесь не была."
    "Здесь почти всегда было пусто, разве что Лена могла прийти сюда, взять лодку и уплыть на остров.{w} Там что-то вроде её тайного места, где она может оставаться весь день, читая очередную книжку из библиотеки."
    "А в остальное время здесь тихо и хорошо."
    th "А может сплавать на остров? Я и одета подходяще."
    th "Но сначала - немного размяться, а то ещё утону на полпути!"
    window hide
    pause (3)

    #провожать Семёна
    window show
    "Но как только я решила, что уже можно плыть, на мостике показался новенький."
    th "Нет, всё же он смог ошибиться."
    "Я вышла из воды и сказала:"
    sl "Ой, так тебе не сюда!"
    stop ambience fadeout 2
    play music music_list["take_me_beautifully"] fadein 5
    show pi normal coat at center with dspr
    "Он обернулся."
    sl "Я же тебе сказала повернуть налево на площади, а ты куда пошёл?"
    sl "Ой, я же так и не представилась!{w} Меня Славя зовут!"
    sl "Вообще, полное имя Славяна, но все меня Славей зовут.{w} И ты тоже зови!"
    show pi surprise coat at center with dspr
    me "А… да…"
    sl "А тебя?"
    me "А… я… да… Семён…"
    $ sl_m_meet('me','Семён')
    "Казалось, что он всё время витает в облаках.{w} Либо очень шокирован чем-то, но чем? Вроде как и нечем, чего уж здесь-то может быть необычного?"
    sl "Очень приятно, Семён."
    th "Эх, ладно, как-нибудь потом постараюсь сплавать. А пока помогу Семёну, сейчас это важнее."
    sl "Ладно, я уже заканчиваю.{w} Ты подожди меня тут минутку, сейчас переоденусь, и вместе пойдём к Ольге Дмитриевне, хорошо?"
    show pi normal coat at center with dspr
    me "Хорошо…"
    hide pi with dspr
    "Я побежала в ту сторону, где я оставила форму."
    window hide
    pause (2)
    show pi normal coat at center with dissolve
    window show
    "Переодевшись, я вернулась к Семёну. Он сел и свесил ноги в воду."
    sl "Пошли?"
    me "Пошли…"
    th "Чем-то он мне Лену напоминает. Такой же грустный.{w} Ну ничего, может, он ещё развеселится!"
    window hide
    scene black with dissolve
    pause (2)
    scene bg ext_square_day
    show dv smile pioneer2 far at left  
    show us grin sport far at right
    show pi normal coat at center
    with dissolve
    window show
    "Мы вышли на площадь. По ней друг за другом бегали Алиса и Ульяна."
    th "Нет, Ульяну хлебом не корми, только дай побегать!"
    sl "Ульяна, хватит бегать! Я всё Ольге Дмитриевне расскажу!"
    us "Есть, гржнинначаник!"
    hide dv 
    hide us 
    with dissolve
    "Они убежали, а мы пошли дальше, в сторону домика вожатой."
    window hide
    stop music fadeout 3
    scene black with dissolve
    pause (2)
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_house_of_mt_day
    show pi normal coat at center
    with dissolve
    window show
    "Уже через пару минут мы были на месте.{w} Семён стоял и рассматривал окрестности."
    sl "Что стоишь? Пойдём!"
    mt "… и хватит издеваться над Леной…"
    th "Кажется, в домике кто-то есть, помимо нашей вожатой."
    play sound sfx_open_dooor_campus_1
    show us grin sport far at left behind pi with dissolve 
    "И точно, через мгновение дверь распахнулась, оттуда выбежала Ульяна и пронеслась мимо, всё так же хитро улыбаясь."
    th "И как она только успела?"
    hide us with dissolve
    show un normal pioneer far at left behind pi with dissolve
    "За ней вышла Лена.{w} Кажется, Ульяна успела ещё и с Леной поссориться."
    sl "Лена, не обижайся ты на неё!"
    show un shy pioneer at left behind pi with dissolve
    un "Да я не…"
    hide un with dspr
    "Она не закончила фразу, покраснела и быстрыми шагами направилась в сторону площади."
    th "Семёна испугалась?{w} Вполне в её духе."
    th "Хотя, Семён вроде не страшный, а вполне даже хороший.{w} И с Леной он как раз таки неплохо бы сошёлся..."
    sl "Пойдём."
    stop ambience fadeout 2
    play sound sfx_open_dooor_campus_1

    #дом ОД
    play music music_list["smooth_machine"] fadein 3
    scene bg int_house_of_mt_day
    show pi normal coat at cleft
    with dissolve
    "Мы зашли в домик."
    th "И всё-таки, как же здесь грязно! Неужели нельзя прибраться?"
    show mt normal pioneer far at cright with dissolve
    "Хозяйка домика стояла у окна."
    mt "Пришёл-таки!{w} Отлично!{w} Меня Ольга Дмитриевна зовут, я вожатая."
    me "Очень приятно, Семён."
    th "Кажется, он прекратил витать в облаках."
    show mt normal pioneer at cright with dissolve
    "Вожатая подошла к Семёну."
    mt "Мы тебя с утра ждём."
    show pi surprise coat at cleft with dspr
    me "Ждёте? Меня?.."
    show mt smile pioneer at cright with dspr
    th "Или нет."
    mt "Да, конечно!"
    show pi normal coat at cleft with dspr
    me "А когда автобус следующий будет, а то я…"
    show mt surprise pioneer at cright with dspr
    mt "А тебе зачем?"
    me "Нет, просто интересно…"
    th "Он что, правда не знает?"
    me "А кстати, где мы точно находимся?{w} Ну, адрес там?"
    me "Я родителям хотел письмо написать, что удачно добрался."
    show mt normal pioneer at cright with dspr
    mt "Так мне твои родители полчаса назад звонили! Тебе привет передавали."
    me "Значит, можно им позвонить, а то я перед отъездом забыл сказать кое-что?"
    show mt smile pioneer at cright with dspr
    mt "Нет."
    "Ольга Дмитриевна улыбнулась."
    me "И почему?"
    mt "А у нас телефона нет."
    "Это была ложь.{w} Телефон был, но только в админ. корпусе, а туда никого из пионеров не пускали. Но я один раз прошла, вместе с Ольгой Дмитриевной."
    "Она там разбирала какие-то бумаги, а я убирала уже отсортированные."
    me "Так как же они сюда позвонили?"
    mt "Я только из райцентра вернулась, там с ними и поговорила."
    "И снова. До райцентра нельзя доехать за полчаса, там как минимум час."
    "Но, иногда работники лагеря называли админ. корпус {i}райцентром{/i}, чтобы хотя бы как то объяснять своё отсутствие. Это я узнала от Ольги Дмитриевны тогда же, в администрации."
    "Я никогда не понимала, почему именно так, и зачем им это вообще нужно.{w} Впрочем, это не моё дело."
    th "Зато теперь я знаю, где она была всё это время."
    me "А мне можно как-нибудь в этот райцентр?"
    mt "Нет."
    me "Почему?"
    th "И всё же он странный. Как можно не понимать простых правил пребывания в лагере?{w} Пионерам во время смены нельзя в город, если это не предусмотрено в плане."
    mt "Потому что следующий автобус будет только через неделю."
    th "А ведь отъезд уже через неделю!{w} Как же мне не хочется, чтобы смена заканчивалась!"
    show pi serious coat at cleft with dspr
    "Семён, до этого не показывавший каких-либо эмоций, теперь явно задумался."
    show mt surprise pioneer at cright with dspr
    mt "Ой, надо тебе форму подобрать!"
    "Опомнилась Ольга Дмитриевна."
    show pi normal coat at cleft with dspr
    me "Да, спасибо…"
    show mt smile pioneer at cright with dspr
    mt "Ладненько, я побежала тогда, а ты пока можешь познакомиться с лагерем!{w} Вечером приходи на ужин, не забудь!"
    hide mt with dissolve
    "С этими словами она вышла из домика."
    sl "Мне тоже пора – дела."
    sl "Ты походи, осмотрись.{w} Вечером увидимся."
    "Произнесла я и пошла за Ольгой Дмитриевной."
    stop music fadeout 3
    play sound sfx_close_door_campus_1
    window hide
    
#часть 2
    #улица
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_house_of_mt_day with dissolve
    window show
    th "Нужно распросить вожатую про Семёна. Хотя бы узнать, куда она его поселит."
    scene bg ext_houses_day with dissolve
    "К счастью, она не успела уйти далеко, и я с лёгкостью догнала её."
    show mt normal pioneer at center with dissolve
    mt "Славя, как хорошо, что ты подошла. Сходи на склад и возьми форму для Семёна. Рост у него, кажется, 175 см.{w} Сможешь?"
    sl "Конечно! А где он будет жить?"
    show mt sad pioneer at center with dspr
    mt "Тут такая ситуация...{w} Свободных мест нет."
    sl "И?"
    show mt normal pioneer at center with dspr
    mt "Он будет жить у меня."
    "Произнесла Ольга Дмитриевна, и, подумав, добавила:"
    mt "Только никому не слова!"
    sl "Обещаю!"
    "Ответила я, а про себя подумала:"
    th "И зачем такая секретность?.. Всё равно рано или поздно все узнают..."
    #Тут же в каждом кусте может сидеть Ульяна, а уж она растреплет..."
    show mt smile pioneer at center with dspr
    mt "Вот и славно, а теперь иди и займись делом."
    hide mt with dissolve
    "Ольга Дмитриевна направилась в сторону медпункта, а я пошла к складу."
    window hide
    
    #склад
    scene bg ext_shed_day with dissolve
    window show
    "У склада было пустынно."
    th "Где как, а здесь всегда стабильность."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (3)
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_house_of_mt_day with dissolve
    window show
    "Процесс поиска формы не занял и пяти минут, и, вскоре я уже подошла к домику вожатой."
    play sound sfx_open_dooor_campus_1
    scene bg int_house_of_mt_day with dissolve
    "Войдя внутрь, я положила форму в шкаф и со спокойной душой вышла наружу."
    play sound sfx_close_door_campus_1
    scene bg ext_house_of_mt_day with dissolve
    th "Вроде, до ужина никаких дел не намечается. Можно и к себе заглянуть на несколько минут."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (2)
    
    #дом_Слави
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_sl_day with dissolve
    window show
    "Дом был пуст, так как Женя, вероятно, была в библиотеке."
    "Я подошла к шкафу и взяла блокнот. На первой странице красовались надписи, оставленные мною утром. Я решила продолжить:"
    show bknt_w1 at truecenter with dspr
    th "...Погода замечательная."
    play sound_loop pen_write
    show bknt_w2 at truecenter with dissolve2
    th "Сегодня к нам заехал ещё один пионер (Семён), прямо посреди смены. Странно. Да и сам он какой-то... необычный, что ли. В зимней одежде, замкнутый, хотя, видно, не дурак. Поначалу был то ли напуган, то ли шокирован чем-то, но сейчас уже вроде понял, что вне опасности."
    th "Да и какая опасность может быть в пионерском лагере? Правильно, никакая. Здесь не зона военных действий, не граница с капиталистами, а всего лишь тихая глушь, затерянная среди лесов..."
    stop sound_loop
    hide bknt_w2
    hide bknt_w1
    with dspr
    $ persistent.sl_m_bknt2 = True
    "Я посмотрела на часы."
    th "Ой, мне же ещё малышей в столовую проводить нужно, а до ужина всего 10 минут!"
    "Положив блокнот обратно, я побежала к домикам, где проживали самые младшие из пионеров."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (3)
    
    #малыши-столовая
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_houses_day with dissolve
    window show
    "Процесс сбора не занял много времени, и теперь мы небольшой группкой шли к столовой. Дети шумели у меня за спиной, но меня это абсолютно не раздражало, а скорее наоборот, умиляло."
    scene bg ext_dining_hall_near_day with dissolve
    "Наконец, мы пришли. У дверей нас уже ждала Оля."
    show mt smile pioneer at center with dissolve
    mt "И снова вы до горна!"
    sl "Уж как получается! И притом, это лучше, чем опаздывать!"
    show mt normal pioneer at center with dspr
    mt "С тобой не поспоришь."
    play sound music_list["dinner_horn_processed"]
    "После этих слов прозвучала музыка, сообщающая пионерам, что настала пора ужина."
    play sound sfx_open_door_1
    mt "Заходите!"
    "Cкомандовала Ольга Дмитриевна и открыла дверь.{w} Жестом поблагодарив её, я вместе с малышами зашла в столовую."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (3)
    play ambience ambience_dining_hall_full fadein 2
    scene bg int_dining_hall_people_day with dissolve
    window show
    "Потихоньку столовая наполнялась людьми. Я видела многих знакомых, но, сколько не искала, не могла найти Мику, Алису и Семёна."
    th "Наверное, позже подойдут."
    window hide
    pause (3)
    
    #Алиса-Семён
    window show
    "Через несколько минут я услышала, как вожатая кого-то ругает."
    show dv normal pioneer2 far at left
    show pi normal shirt far at right
    show mt rage pioneer far at center
    with dissolve
    "Это оказалась Алиса, которая опять неправильно надела форму.{w} Рядом также стоял Семён, наблюдая за Алисой."
    th "Кажется, Семёну понравилась Алиса, точнее её...{w} Впрочем, какое мне до этого дело?"
    window hide
    hide mt
    hide dv
    hide pi
    with dissolve
    pause (2)
    show dv normal pioneer at center with dissolve
    window show
    "Свободных мест оставалось не так уж и много, и, наверное, поэтому, Алиса решила сесть рядом со мной:"
    dv "Не против?"
    sl "Не против, садись."
    "Я слегка улыбнулась. Она в ответ лишь немного поморщилась."
    th "Алиса как всегда в своём репертуаре."
    sl "А ты случайно не видела Мику? Она почему-то не пришла на ужин…"
    dv "Нет. В клубе работает, небось. Фанат своего дела."
    sl "Это точно."
    "Алиса начала есть, я также решила не продолжать разговор."
    window hide
    hide dv with dissolve
    pause(1)
    
    #что-то упало
    stop ambience fadeout 2
    play sound sfx_broken_dish
    play sound2 sfx_dropped_chair
    play music music_list["doomed_to_be_defeated"] fadein 3
    window show
    "Вдруг раздался страшный грохот."
    window hide
    with dissolve
    pause(1)
    show pi shocked shirt far at left
    show us laugh2 pioneer far at right
    with dissolve
    window show
    "Я посмотрела вперёд, за Алису."
    "Там Семён свалился со стула и расколотил тарелку.{w} В дверях стояла Ульяна и громко смеялась."
    th "Понятно, Ульяне захотелось повеселиться."
    me "Ах ты, маленькая…"
    hide pi
    hide us
    with dissolve
    play sound sfx_slam_door_campus
    stop music fadeout 3
    play ambience ambience_dining_hall_full fadein 2
    "Ульяна выбежала из столовой, Семён бросился за ней вдогонку."
    
    #Алиса-расспросы
    show dv normal pioneer at center with dissolve
    sl "Опять Ульяна хулиганит."
    "Алиса промолчала, но потом спросила:"
    dv "Что это за парень был?"
    sl "Семён?"
    sl "Новенький. Только сегодня приехал."
    sl "Хороший парень, наверняка не виноват. От Ульяны не спасёшься."
    dv "Он что, с Северного полюса? В шубе тут ходил."
    sl "Может быть."
    $ sl_m_al1 = renpy.random.choice(['more', 'that_s_all'])
    if sl_m_al1 == 'more':
        $ sl_m_day1_al_que = True
        dv "А почему он так поздно?"
        sl "Не знаю, я не спрашивала."
        dv "А как он добрался сюда?"
        sl "Автобус приезжал."
        dv "И куда его поселят?"
        "Я, хитро улыбаясь, ответила:"
        sl "Это как Ольга Дмитриевна решит."
        "Алиса смерила меня презрительным взглядом и вернулась к еде."
        th "Фух, кажется, она не догадалась."
    elif sl_m_al1 == 'that_s_all':
        "На этом поток вопросов у Алисы иссяк, и она вернулась к еде."
    window hide
    hide dv with dissolve
    pause (2)
    
    #конец_ужина
    window show
    "Алиса справилась с порцией быстрее меня и ушла. Я решила не засиживаться дальше и тоже вышла из столовой."
    window hide
    stop ambience fadeout 2
    play sound sfx_close_door_1
    play ambience ambience_camp_center_evening fadein 2
    scene bg ext_dining_hall_near_sunset with dissolve
    
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    
    window show
    "За дверями меня встретил посвежевший воздух. Наступал вечер, принося с собой темноту и прохладу. Но пока ещё не было совсем темно и можно было наблюдать, как солнце постепенно приближается к горизонту, унося с собой остатки этого дня."
    th "Вот и день заканчивается. А завтра новый, и снова дела, заботы и всё такое прочее. А пока что можно со спокойной душой идти к себе."
    window hide
    scene bg ext_square_sunset with dissolve
    
    #время_поисков
    window show
    "На площади я остановилась и посмотрела в сторону леса."
    th "Как бы там никого ночью не оказалось. А то ведь там и заблудиться можно!.."
    stop ambience fadeout 2
    play music music_list["orchid"] fadein 3
    th "А куда Ульяна увела Семёна?{w} Не в лес ли часом?"
    "Мысль о том, что Семён может заблудиться в лесу, напугала меня."
    th "Мне нужно его найти.{w} Где же он может быть?.."
    window hide
    
    #карта
    $ disable_all_zones()
    $ set_zone("forest","slavyana_mod__day1_forest")
    $ set_zone("me_mt_house","slavyana_mod__day1_od")
    $ set_zone("medic_house","slavyana_mod__day1_mh")
    $ set_zone("dv_us_house","slavyana_mod__day1_ul")
    
    $ set_zone("old_house","slavyana_mod__day1_oh")
    
    $ set_zone("camp_entrance","slavyana_mod__day1_other")
    $ set_zone("library","slavyana_mod__day1_other")
    $ set_zone("estrade","slavyana_mod__day1_other")
    $ set_zone("clubs","slavyana_mod__day1_other")
    $ set_zone("boat_station","slavyana_mod__day1_other")
    $ set_zone("beach","slavyana_mod__day1_other")
    $ set_zone("music_club","slavyana_mod__day1_other")
    $ set_zone("sport_area","slavyana_mod__day1_other")
    $ set_zone("valleyball","slavyana_mod__day1_other")

label slavyana_mod__day1_map:
    $ show_map()

#лесочек
label slavyana_mod__day1_forest:
    stop music fadeout 2
    $ persistent.sprite_time = "night"

    if sl_m_day1_map_od:
        scene bg ext_houses_sunset with dissolve
    elif sl_m_day1_map_mh:
        if not sl_m_day1_other:
            stop ambience fadeout 2
            play ambience ambience_camp_center_evening fadein 2
        scene bg ext_aidpost_sunset with dissolve
    elif sl_m_day1_map_ul:
        if not sl_m_day1_other:
            stop ambience fadeout 2
            play ambience ambience_camp_center_evening fadein 2
        scene bg ext_house_of_dv_day with dissolve
    else:
        play ambience ambience_camp_center_evening fadein 2
        scene bg ext_square_sunset with dissolve
    window show
    th "Я уверена, Ульянка его куда-то в лес заманила.{w} Заблудился, наверное..."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (4)
    play ambience ambience_forest_evening fadein 2
    scene bg ext_path_sunset with dissolve
    window show
    "Я долго ходила по лесу, пока не поняла, что Семёна здесь не найду.{w} А ещё, что я, кажется, сама заблудилась."
    th "Вот тебе и поиски...{w} Но не надо сдаваться, я найду выход!"
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (5)
    $ night_time()
    play ambience ambience_forest_night fadein 2
    play music music_list["door_to_nightmare"] fadein 3
    scene bg ext_path_night with dissolve
    window show
    "Ночной лес поразительно отличался от дневного. На месте жизнерадостного зелёного цвета теперь находился светло-синий, близкий к голубому цвет. Животные затихли, и было слышно лишь тихий шелест листьев, да потрескивание сверчков."
    "Да и само ощущение менялось: если днём в лесу было спокойно и хотелось гулять как можно дольше, то ночью, наоборот, за каждым деревом как будто таилась опасность (которой там вовсе и не было, ведь хищных животных в этих местах почти не водится), а случайные звуки нагоняли ещё большую тревогу."
    "Впрочем, я почти не боялась леса, так как знала, что бояться здесь нечего.{w} Однако всегда нужно быть наготове."
    window hide
    stop music fadeout 3
    stop ambience fadeout 2
    scene black with dissolve
    pause (3)
    
    #объект_найден_и_захвачен
    play ambience ambience_camp_center_night fadein 2
    scene bg ext_camp_entrance_night
    show pi normal shirt far at center
    with dissolve
    window show
    "Минут через 10 ходьбы, я увидела впереди ворота лагеря, а рядом с ними...{w} Семёна."
    th "Так вот куда он пришёл."
    show pi normal shirt at center with dissolve
    "Когда я к нему приблизилась, он уже вставал и собирался уходить."
    sl "Привет, что тут так поздно делаешь?"
    show pi shocked shirt at center with dspr
    me "…"
    "Увидев меня, он вздрогнул, кажется, от неожиданности."
    th "{i}...а в ответ - тишина...{/i}"
    sl "Не догнал Ульяну?"
    "Я улыбнулась, заранее догадываясь об ответе."
    show pi upset shirt at center with dspr
    "Семён расстроенно помотал головой и вздохнул."
    sl "Неудивительно.{w} Никто не может."
    "Тут я спохватилась:"
    sl "Ты, наверное, есть хочешь, поужинать-то не получилось…"
    play sound sfx_stomach_growl #channel 7
    "За Семёна ответил его желудок, негромко заурчав."
    sl "Ну, тогда пойдём."
    show pi surprise shirt at center with dspr
    me "А разве столовая ещё открыта?"
    sl "Да ничего, у меня ключи есть."
    me "Ключи?"
    sl "Да, у меня от всех помещений лагеря есть ключи."
    me "А откуда?"
    sl "Ну, я здесь кто-то вроде помощницы вожатой."
    show pi normal shirt at center with dspr
    me "Понятно.{w} Ну пойдём."
    scene bg ext_square_night 
    show pi normal shirt at center
    with dissolve
    "Когда мы дошли до площади, я остановилась, вспомнив, что нужно предупредить Женю, что я буду немного позднее."
    sl "Извини, мне надо соседку предупредить, что я попозже приду, а то она сама такая пунктуальная – будет волноваться."
    sl "Ты иди пока к столовой, а я через минутку, хорошо?"
    me "Ладно…"
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (1)
    
    #ночной_дом-Женя
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    play ambience ambience_int_cabin_night fadein 2
    #поищите тени на картинке
    scene bg int_house_of_sl_night_light
    #не нашли?
    #это всё потому что я криворукий идиот
    show mz bukal glasses pioneer at center
    with dissolve
    window show
    "Когда я вошла, Женя лежала на кровати и читала книгу."
    sl "Женя, я сейчас немного задержусь, ты меня не дожидайся, хорошо?"
    show mz normal glasses pioneer at center with dspr
    mz "Хорошо.{w} А в честь чего задержка?"
    sl "Новенькому помочь хочу, он ведь не ужинал..."
    show mz smile glasses pioneer at center with dspr
    mz "А, ну понятно. Удачи тебе."
    "Сказала Женя и подмигнула."
    sl "Спасибо."
    window hide
    $ persistent.sprite_time = "night"
    $ night_time()
    stop ambience fadeout 2
    play sound sfx_close_door_campus_1
    play ambience ambience_camp_center_night fadein 2
    scene bg ext_house_of_sl_night_light with dissolve
    window show
    "Я вышла из домика и направилась к столовой."
    th "Необычно для неё.{w} И вообще, что она имеет в виду?{w} Она явно не о том подумала.{w} Я просто хочу помочь, вот и всё."
    
    #столовая_снаружи
    scene bg ext_dining_hall_away_night with dissolve
    "Подходя к столовой, я увидела, как что-то белое спрыгнуло с крыльца и скрылось в лесу."
    th "Надо спросить у Семёна, он должен знать."
    scene bg ext_dining_hall_near_night
    show pi normal shirt at center
    with dissolve
    sl "Всё в порядке?"
    me "Да, а почему ты спрашиваешь?"
    sl "Да нет, просто так."
    th "Он не хочет рассказывать.{w} Тогда, скорее всего, это была либо Ульяна, либо Алиса.{w} Запугали его чем-то, вот он и не говорит."
    me "Всё в порядке."
    "Повторил Семён."
    "Он говорил излишне уверенно, даже фальшиво."
    th "Точно что-то скрывает."
    sl "Ну что, пойдём?"
    "Я решила не подавать виду, что он попался на лжи."
    th "Ладно уж, первый день в лагере, не буду приставать к человеку.{w} Плюс, он ещё и голодный."
    stop ambience fadeout 2
    
    #столовая_внутри
    scene bg int_dining_hall_night
    show pi normal shirt at center
    with dissolve
    play music music_list["a_promise_from_distant_days"] fadein 5
    "Мы зашли в столовую."
    sl "Подожди, я сейчас что-нибудь принесу."
    window hide
    scene black with dissolve
    pause (2)
    scene bg int_dining_hall_night with dissolve
    window show
    "Я пошла на кухню и нашла там несколько булочек, а в холодильнике – немного кефира. Взяв всё это с собой, я вернулась к Семёну."
    scene cg d1_sl_dinner with dissolve
    "Семён стал есть, а я невольно стала изучать его внешность."
    th "Обычный парень, только выглядит слабоватым.{w} А может, мне только так кажется?"
    "Голос Семёна оторвал меня от размышлений:"
    me "Что, у меня что-то на лице?"
    show cg d1_sl_dinner_0 with dspr
    sl "Нет, просто…"
    "Я улыбнулась, чтобы скрыть смущение."
    th "Нужно переменить тему."
    sl "И как тебе первый день в лагере?"
    me "Ну, я даже не знаю..."
    "Он задумался."
    th "Вспоминая, то, как он пугался всего днём, мне кажется, что ему здесь пока что непривычно.{w} Но это дело поправимое."
    sl "Ничего, скоро привыкнешь!"
    show cg d1_sl_dinner with dspr
    "Я стала смотреть в окно, дабы больше не попадать в неприятные ситуации с объяснениями.{w} Потихоньку слипались глаза, но я старалась не заснуть."
    "Вскоре Семён снова заговорил:"
    me "Ну а так, вообще, здесь мило."
    sl "Да?"
    "Спросила я у него сквозь полудрёму.{w} Организм всё-таки давал о себе знать."
    me "Да. Здесь так..."
    "Он остановился."
    sl "Как?"
    "Я оживилась и внимательно посмотрела на него, ожидая ответа."
    th "Давай же, скажи что-нибудь, например, хорошо или ещё что-нибудь такого!"
    "Внутри меня копошились непонятные даже мне мысли."
    #и мне тоже
    me "Ну, я не знаю... мило. Да! Тут мило."
    show cg d1_sl_dinner_0 with dspr
    sl "Пожалуй."
    "Я успокоилась и улыбнулась."
    sl "Очень хорошо, что ты так думаешь."
    me "Почему?"
    sl "Ну, не всем здесь нравится..."
    th "Например, Алисе."
    me "А тебе?"
    "Я не ожидала такого вопроса."
    sl "Мне?"
    me "Да."
    sl "Нравится, тут здорово."
    me "Тогда и не стоит обращать внимание на других."
    sl "А я и не обращаю особо."
    th "Почти."
    "Я внезапно рассмеялась, заметив, как напряжён Семён."
    th "Интересно, это у него всегда так при разговоре?"
    sl "А вот ты волнуешься..."
    me "Да? Почему?"
    sl "Ну, когда кто-то так сосредоточенно жуёт..."
    me "Извини."
    sl "Ничего."
    th "И всё-таки, он странный.{w} Извиняется просто так, постоянно ожидает какого-то подвоха...{w} Может, ему следовало бы больше доверять людям?"
    window hide
    pause (2)
    window show
    th "А ещё Семён очень не похож на других. Взять, например, характер. Ни разу ещё не встречалась с настолько замкнутым человеком. А внешность? Ну тут всё обычно, кроме глаз, которые почти не видать за волосами."
    #th "С уверенностью могу заявить, что Семён – самое странное в этом лагере. Приехал посредине смены, да ещё и в зимней одежде. Да и на других он очень не похож. Взять, например, характер. Ни разу ещё не встречалась с настолько замкнутым человеком."
    th "А в целом... В целом он очень хороший.{w} Интересно, сколько раз за день я это себе всё это повторила?"
    window hide
    pause (2)
    window show
    "Я почувствовала, что на меня кто-то смотрит. Кроме Семёна и меня здесь никого больше не было, поэтому это мог быть только он."
    "Краем глаза я заметила, что это действительно был Семён, но смотрел он не прямо, а только немного подняв глаза, словно стеснялся меня."
    "Нужно было прерывать затянувшееся молчание:"
    show cg d1_sl_dinner with dspr
    sl "Прости, хотела показать тебе лагерь, но совсем забегалась сегодня."
    me "Да я сам... Вроде ничего не пропустил."
    show cg d1_sl_dinner_0 with dspr
    sl "Прям-таки ничего-ничего?"
    "Cказала я, улыбнувшись. Семён отвёл глаза, и даже слегка покраснел."
    me "Ну, откуда я знаю – я же здесь первый день."
    sl "Ну хорошо, и что видел уже?"
    me "Площадь, столовую вот видел, футбольную площадку..."
    sl "А пляж?"
    me "Только издалека."
    sl "Обязательно сходи! Или давай вместе сходим!"
    me "Ну ладно... сходим..."
    
    #что?
    "Я ещё раз посмотрела за окно. На улице уже была глубокая ночь."
    th "Неужели уже так поздно? Режим нарушать нельзя!"
    "Мысль была настолько внезапной, что, где-то в глубине себя, я удивилась."
    me "А можно задать глупый вопрос?"
    sl "Нет."
    stop music fadeout 5
    scene bg int_dining_hall_night
    show pi normal shirt at center
    with dissolve
    "Произнесла я с лёгкой улыбкой и встала из-за стола."
    th "Как-нибудь в следующий раз, сейчас пора спать."
    sl "Уже поздно... Сам дорогу до Ольги Дмитриевны найдёшь?"
    me "Найду, конечно, но зачем мне к ней?"
    sl "Поселит тебя к кому-нибудь."
    me "Зачем?"
    th "Так это и был его глупый вопрос?"
    "Подумала я про себя, а вслух лишь рассмеялась."
    sl "Ну так спать тебе где-то надо!"
    me "Логично..."
    sl "Ладно, я побежала тогда.{w} Спокойной ночи!"
    me "Спокойной..."
    window hide
    
    #ночь-дневник-спать
    play ambience ambience_camp_center_night fadein 2
    scene bg ext_square_night with dissolve
    window show
    th "Неудобно получилось...{w} И зачем только я убежала?{w} Сама не знаю..."
    th "Так или иначе, но всё уже сделано, назад не вернёшь."
    scene bg ext_house_of_sl_night with dissolve
    "Я дошла до домика. Света внутри уже не было, поэтому действовать нужно было как можно тише."
    stop ambience fadeout 2
    $ volume(0.1, "sound")
    play sound sfx_open_door_clubs
    scene bg int_house_of_sl_night with dissolve
    "Я зашла внутрь, взяла блокнот и вышла обратно на крыльцо."
    play sound sfx_close_door_clubs_nextroom
    play ambience ambience_camp_center_night fadein 2
    scene bg ext_house_of_sl_night with dissolve
    "Устроившись поудобнее, я стала дописывать:"
    show bknt_w2 at truecenter with dspr
    th "...затерянная среди лесов."
    play sound_loop pen_write
    show bknt_w3 at truecenter with dissolve2
    th "На ужине Ульяна его разыграла (не знаю как) и Семён упал со стула, заодно разбив тарелку. Я пошла его искать, и чуть не заблудилась ночью в лесу. Хотя, там в это время так же красиво, как и днём, можно было бы ещё немного побродить..."
    th "Найдя Семёна, я проводила его в столовую, лишний раз убедившись, в том, что он немного странный. Впрочем, может это только поначалу?"
    stop sound_loop
    "Я перечитала всё, что написала в блокнотике."
    th "Да, сегодняшний день прошёл просто замечательно!"
    hide bknt_w3
    hide bknt_w2
    with dspr
    $ persistent.sl_m_bknt3 = True
    "После этого, я закрыла блокнот и отложила его в сторону. Хотелось немного посидеть, ни о чём не думая и ничего не делая."
    window hide
    pause (3)
    #stop ambience fadeout 2
    play music music_list["raindrops"] fadein 3
    window show
    "Вокруг стояла тишина, и, если бы не свет фонарей, то я бы сейчас ощущала себя где-то в лесу.{w} Ночной лагерь действительно похож на ночной лес: те же деревья, те же сверчки и та же темнота. Разве что опасности совершенно не чувствуется, напротив, ощущаются покой и умиротворение."
    scene stars with dissolve
    "Я подняла голову к небу. Надо мной были тысячи, нет миллионы звёзд. И все они мерцали и переливались, каждая по своему, по особенному.{w} Некоторые – быстрее, другие – медленнее, а третьи почти незаметно, слегка, словно покачиваясь на воде."
    "Чуть вдалеке светила луна, а рядом с ней...{w} падающая звезда?"
    th "Нужно загадать желание! Я хочу... чтобы эта смена закончилась замечательно."
    window hide
    pause (3)
    stop music fadeout 3
    stop ambience fadeout 2
    scene bg ext_house_of_sl_night with dissolve
    window show
    "Ещё некоторое время я просто сидела и смотрела по сторонам.{w} Однако я вспомнила, что очень уж бежала соблюдать режим, чем сейчас совершенно не занималась."
    "Поднявшись, я вошла в домик."
    play sound sfx_open_door_clubs
    scene bg int_house_of_sl_night with dissolve
    "Там, положив блокнот и раздевшись, я легла в кровать, и, уже через пару минут, спокойно заснула."
    window hide
    hide unblink
    show blink
    $ volume(1.0, "sound")
    jump slavyana_mod__day1_end

#опять_ОД
label slavyana_mod__day1_od:
    stop music fadeout 2
    $ sl_m_day1_not_now = True
    $ sl_m_day1_map_od = True
    
    $ persistent.sprite_time = "sunset"
    
    if not sl_m_day1_other:
        stop ambience fadeout 2
        play ambience ambience_camp_center_evening fadein 2

    if sl_m_day1_map_mh:
        scene bg ext_aidpost_sunset with dissolve
    elif sl_m_day1_map_ul:
        scene bg ext_house_of_dv_day with dissolve
    else:
        scene bg ext_square_sunset with dissolve
    window show
    th "Думаю, они уже закончили свою беготню и разошлись по домам."
    "Решила я и направилась к домику вожатой."
    scene bg ext_house_of_mt_sunset 
    show mt normal pioneer at center
    with dissolve
    "Около домика в лежаке читала Ольга Дмитриевна."
    sl "Ты не видела Семёна?"
    show mt surprise pioneer at center with dspr
    mt "Нет, он разве ещё не вернулся?"
    sl "Нет, я его сейчас ищу."
    show mt grin pioneer at center with dspr
    mt "Молодец! Продолжай в том же духе."
    show mt normal pioneer at center with dspr
    mt "Может, тебе кого-то на помощь позвать?"
    sl "Нет, спасибо, не надо, я как-нибудь сама..."
    mt "Хорошо, но если не найдёшь, приходи ко мне, будем искать его более организованно."
    sl "Ладно, я тогда побежала!"
    mt "Удачи!"
    hide mt with dissolve
    th "Куда же теперь?.."
    window hide
    $ disable_current_zone()
    $ sl_m_day1_map_mh = False
    $ sl_m_day1_map_ul = False
    $ sl_m_day1_other = False
    jump slavyana_mod__day1_map

#медпункт
label slavyana_mod__day1_mh:
    stop music fadeout 2
    $ sl_m_day1_not_now = True
    $ sl_m_day1_map_mh = True
    if sl_m_day1_map_od:
        scene bg ext_houses_sunset with dissolve
    elif sl_m_day1_map_ul:
        if not sl_m_day1_other:
            stop ambience fadeout 2
            play ambience ambience_camp_center_evening fadein 2
        scene bg ext_house_of_dv_day with dissolve
    else:
        play ambience ambience_camp_center_evening fadein 2
        scene bg ext_square_sunset with dissolve
    window show
    th "Может, кто-то из них поранился? Нужно сходить в медпункт, проверить."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (1)
    play ambience ambience_medstation_inside_day fadein 2
    scene bg int_aidpost_day with dissolve
    window show
    "Внутри медпункта меня ждала только лишь пустота."
    th "Значит, Виола опять куда-то ушла, не закрыв дверь.{w} Ну как так можно!"
    th "А мне нужно поискать в другом месте."
    window hide
    $ disable_current_zone()
    $ sl_m_day1_map_od = False
    $ sl_m_day1_map_ul = False
    $ sl_m_day1_other = False
    jump slavyana_mod__day1_map

#поиски_Ульяны
label slavyana_mod__day1_ul:
    stop music fadeout 2
    $ sl_m_day1_not_now = True
    $ sl_m_day1_map_ul = True
    if sl_m_day1_map_od:
        scene bg ext_houses_sunset with dissolve
    elif sl_m_day1_map_mh:
        if not sl_m_day1_other:
            stop ambience fadeout 2
            play ambience ambience_camp_center_evening fadein 2
        scene bg ext_aidpost_sunset with dissolve
    else:
        play ambience ambience_camp_center_evening fadein 2
        scene bg ext_square_sunset with dissolve
    window show
    th "Нужно найти Ульяну. Уж она-то должна знать, куда бежала."
    scene bg ext_house_of_dv_day with dissolve
    "Дойдя до их с Алисой домика, я постучалась."
    window hide
    play sound sfx_knock_door2
    pause (2)
    window show
    "Ответа не последовало."
    play sound sfx_open_dooor_campus_1
    "Я приоткрыла дверь и вошла внутрь."
    stop ambience fadeout 2
    play ambience ambience_int_cabin_evening fadein 3
    scene bg int_house_of_dv_day with dissolve
    "В домике было пусто."
    th "Нет, здесь никто не прячется.{w} Тогда пойду искать Семёна.{w} Но где?.."
    window hide
    $ disable_current_zone()
    $ sl_m_day1_map_od = False
    $ sl_m_day1_map_mh = False
    $ sl_m_day1_other = False
    jump slavyana_mod__day1_map
    
#старый_корпус
label slavyana_mod__day1_oh:
    if sl_m_day1_map_od:
        scene bg ext_houses_sunset with dissolve
    elif sl_m_day1_map_mh:
        $ sl_m_day1_other = True
        stop ambience fadeout 2
        play ambience ambience_camp_center_evening fadein 2
        scene bg ext_aidpost_sunset with dissolve
    elif sl_m_day1_map_ul:
        $ sl_m_day1_other = True
        stop ambience fadeout 2
        play ambience ambience_camp_center_evening fadein 2
        scene bg ext_house_of_dv_day with dissolve
    else:
        scene bg ext_square_sunset with dissolve
    window show
    "Туда я не пойду."
    window hide
    $ disable_current_zone()
    jump slavyana_mod__day1_map

#остальные_места
label slavyana_mod__day1_other:
    if sl_m_day1_map_od:
        scene bg ext_houses_sunset with dissolve
    elif sl_m_day1_map_mh:
        $ sl_m_day1_other = True
        stop ambience fadeout 2
        play ambience ambience_camp_center_evening fadein 2
        scene bg ext_aidpost_sunset with dissolve
    elif sl_m_day1_map_ul:
        $ sl_m_day1_other = True
        stop ambience fadeout 2
        play ambience ambience_camp_center_evening fadein 2
        scene bg ext_house_of_dv_day with dissolve
    else:
        scene bg ext_square_sunset with dissolve
    $ sl_m_mpr1 = renpy.random.choice(['d1_mr1', 'd1_mr2', 'd1_mr3'])
    window show
    if sl_m_mpr1 == 'd1_mr1':
        "Там его быть не может."
    elif sl_m_mpr1 == 'd1_mr2':
        "Откуда ему там взяться?"
    elif sl_m_mpr1 == 'd1_mr3':
        "Не думаю, что найду его там."
    window hide
    $ disable_current_zone()
    jump slavyana_mod__day1_map

    #временная концовка
    #window show
    #fbt "Продолжение следует..."
    #window hide

#кодо-концовка
label slavyana_mod__day1_end:
    scene black with dissolve
    hide blink
    pause (3)
    $ persistent.sl_m_day1 = True
    if sl_m_Full:
        jump slavyana_mod__day2
    jump slavyana_mod__launcher0

#Сделано FireBoTer'ом

#Быстрый выбор
label slavyana_mod__day1_fast_choice:
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