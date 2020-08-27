init:
    $ sl_m_day2_find_keys = False
    $ sl_m_day2_sp_keys = False
    $ sl_m_day2_go_with_sp = False
    $ sl_m_day2_you_win = False
    
label slavyana_mod__day2:
    pause (3)
    $ backdrop = "days"
    $ new_chapter(2, u"Славя. День второй")
    $ save_name = (u'Славя. День второй')
    $ day_time()
    $ persistent.sprite_time = "day"
    
    #сон
    play music music_list["sparkles"] fadein 3
    scene black with dissolve
    window show
    dreamgirl "{i}«Вставай!»{/i}"
    "Донеслось откуда-то из глубин сознания."
    window hide
    pause (1.5)
    window show
    dreamgirl "{i}«Славя, вставай!»{/i}"
    th "Что бы это ни было, оно было весьма настырно."
    window hide
    pause (1.5)
    window show
    dreamgirl "{i}«Славя, Ольга Дмитриевна зовёт!»{/i}"
    window hide
    stop music fadeout 1
    show unblink
    
    #домик
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_sl_day 
    show mz normal pioneer close at center
    with dissolve
    window show
    "Я резко открыла глаза.{w} Надо мной нависла Женя."
    mz "Наконец-то, проснулась! Вставай быстрее и иди умываться, а то завтрак пропустишь."
    sl "Да, я сейчас..."
    hide mz with dissolve
    "Сон оставил за собой ощущение разбитости, словно за ночь я подмела несколько десятков лагерных площадей."
    show mz normal pioneer at center with dissolve
    mz "И что это тебя так угораздило? Обычно же вскакиваешь, ни свет ни заря."
    sl "Да засиделась я немного ночью... Вот и..."
    "Женя перешла на нравоучительный тон:"
    mz "Советую впредь соблюдать режим, а то вдруг я тебя не добужусь?{w} Что будет-то..."
    sl "Даже и не говори."
    hide mz with dissolve
    "Наконец-то оторвавшись от кровати, я встала перед шкафом в нерешительности."
    th "А как же пробежка?{w} Придётся отменить?{w} Или всё-таки сбегать, но после завтрака?{w} А не вредно ли?{w} А хотя, ладно, сейчас надену спортивный костюм, а там разберусь."
    "Я подошла к столу, чтобы взять умывальные принадлежности. Они лежали на своём месте, а вот ключи..."
    play music music_list["awakening_power"] fadein 1
    extend " они пропали!{w} Я обсмотрела всё вокруг, но так и не нашла их."
    show mz normal pioneer at center with dissolve
    sl "Женя, ты не видела мои ключи?"
    mz "Больно они мне надо. Нет, не видела."
    stop ambience fadeout 3
    play sound sfx_close_door_campus_1
    scene bg ext_house_of_sl_day with dissolve
    "Я вышла за дверь. На ступеньках их не было."
    th "Значит либо я их где-то до этого забыла, либо... либо их кто-то взял.{w} Если это был человек, надеюсь, он отдал их вожатой."
    stop music fadeout 2
    "Вздохнув, я отправилась к умывальникам."
    window hide
    scene black with dissolve
    pause (2)
    
    #улица
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_houses_day with dissolve
    window show
    "Несмотря на то, что я немного проспала, в лагере всё равно было немноголюдно."
    th "Изо дня в день, одно и то же, одно и то же. Когда же здесь все перестанут лениться?"
    scene bg ext_washstand_day with dissolve
    "Однако, подойдя к умывальникам, я всё-таки отстояла небольшую очередь."
    window hide
    pause (1)
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 2 
    scene bg ext_washstand2_day with dissolve
    window show
    "Холодная вода из крана смыла последние остатки сна, и я вновь почувствовала привычное ощущение свежести и лёгкости. Быстро (но тщательно) почистив зубы и ещё раз умывшись, я отправилась обратно."
    stop sound_loop
    play sound sfx_close_water_sink
    stop ambience fadeout 2
    window hide
    scene black with dissolve
    pause (2)
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_houses_day with dissolve
    window show
    "Лагерь постепенно оживал. Неудивительно, ведь скоро завтрак, и все стремятся занять местечко получше и взять кусок повкуснее."
    "Я никогда этого не понимала, ведь все места по-своему хороши, а еду варят одни и те же повара из одной и той же посуды и по одному и тому же рецепту."
    "Столовая – эдакий уголок постоянства в «Совёнке», место, где почти ничего не меняется, что мне очень даже нравится."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (2)
    
    #домик
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_sl_day
    show mz bukal glasses pioneer at center
    with dissolve
    window show
    "Наконец, я вернулась в домик. Женя ждала меня там же, в её руках снова была книга."
    "Каждую свободную минуту она посвящала чтению, и, судя по всему, именно поэтому вызвалась на столь непопулярную должность заведующей библиотекой практически мгновенно. Возражений, естественно, не было."
    mz "Горн уже звучал?"
    "Сказала она слегка ворчливо. Женя не любила отвлекаться от чтения, даже если на то были серьёзные причины."
    sl "Нет, но я думаю, что уже скоро."
    show mz normal glasses pioneer at center with dissolve
    mz "Хорошо, тогда подождём, пока прозвучит и пойдём."
    "Крайняя Женина пунктуальность опять показывала себя во всей красе."
    window hide
    hide mz with dissolve
    pause (1.5)
    play sound music_list["dinner_horn_processed"]
    window show
    "Менее чем через минуту раздались знакомые каждому пионеру звуки."
    show mz normal glasses pioneer at center with dissolve
    mz "Эх, чуть-чуть попозже бы... Ну да ладно, пошли."
    hide mz with dissolve
    "Сказала Женя и направилась к выходу."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (2)
    
    #столовая-завтрак
    play ambience ambience_dining_hall_full fadein 2
    scene bg int_dining_hall_people_day with dissolve
    window show
    "Столовая была наполовину заполнена людьми. Ну, или наполовину пуста, тут как посмотреть. Этот спор стар, как мир и не мне его разрешать."
    "Взяв еду, мы с Женей сели за первый попавшийся свободный стол. Сегодня давали манную кашу и бутерброды с колбасой."
    "И если первое было уже обыденно, так как появлялось на тарелках пионеров почти каждый завтрак, то бутерброды с колбасой были редкостью, даже шиком, ведь достать колбасу было сложно даже в обычном магазине, а чтобы в пионерлагере... В общем, сегодня это явно было блюдом дня."
    "У всей этой еды был только один минус – мне теперь придётся ещё как минимум на час отложить свою пробежку."
    window hide
    pause (2)
    show mz normal glasses pioneer at right
    show mt normal pioneer at left
    with dissolve
    window show
    "Через пару минут к нам подошла Ольга Дмитриевна."
    mt "Здравствуйте, девочки."
    sl "Здравствуйте!"
    mz "Здравствуйте."
    "Нехотя ответила Женя."
    mt "Женя, ты ведь помнишь, что сегодня твоя очередь убираться в столовой?"
    show mz bukal glasses pioneer at right with dspr
    mz "Да, Ольга Дмитриевна."
    "Женя была недовольна напоминанием, ведь она всегда помнила, что и когда ей нужно сделать.{w} Ольга Дмитриевна же не обратила на это никакого внимания и продолжила раздачу ценных указаний:"
    mt "А от тебя, Славя, мне нужно, чтобы ты принесла на линейку обходной лист. Они ведь у тебя остались?"
    sl "Да, было ещё несколько. Вам для Семёна?"
    mt "Да."
    sl "А где он?"
    mt "Спит ещё. У него сегодня первый день, так что я решила его не будить. Ничего страшного, если он сегодня пропустит завтрак."
    sl "Но ведь он останется голодным!"
    mt "Я возьму для него бутерброды, можешь не беспокоиться."
    sl "А ещё, Ольга Дмитриевна...{w} Вы не видели моих ключей?"
    "Было очень неприятно признаваться вожатой в своей рассеянности, но это могло помочь найти ключи."
    show mt surprise pioneer at left with dspr
    mt "Ты их потеряла?!"
    sl "Да..."
    "Я почувствовала, что моё лицо покраснело."
    show mt normal pioneer at left with dspr
    mt "Нет, не видела... Но попробую поискать.{w} И ты давай ищи."
    sl "Хорошо, я постараюсь!"
    mt "И не забудьте про линейку!"
    hide mt with dissolve
    show mz bukal glasses pioneer at right:
        linear 0.5 xalign 0.5
    "Сказала вожатая и отошла от «нашего» столика."
    "Женя, последнюю пару минут молчавшая, снова заговорила:"
    show mz smile glasses pioneer at center with dspr
    mz "Что, опять печёшься о новеньком?"
    "Произнесла она немного ехидным голосом."
    sl "Да нет, что ты! Просто пытаюсь образумить вожатую."
    show mz normal glasses pioneer at center with dspr
    mz "Тогда лучше скажи ей, чтобы больше лезла ко мне со своими напоминаниями."
    "Я рассмеялась."
    sl "И как ты себе это представляешь? Подхожу я к Ольге Дмитриевне и говорю: «Ольга Дмитриевна, вы можете больше не напоминать Жене ни о чём?»"
    mz "Да, согласна, глупая идея..."
    sl "Я тебе вот что посоветую: не обращай на это внимания и жить станет намного проще!"
    mz "Хорошо, попробую. А теперь я ухожу, итак засиделась тут, библиотеку уже открывать надо."
    sl "Хорошо, пока."
    hide mz with dissolve
    "И хотя в библиотеку мало кто шёл {i}по своей воле{/i}, Женя всё равно сидела там каждый день. Возможно, это было единственное место, где она чувствовала себя в своей тарелке."
    "Практика набирания пионеров в библиотеку появилась только в этой смене, потому что штатный сотрудник уволился, а нового не нашли.{w} По крайней мере, это всё, что рассказала мне вожатая."
    "К этому моменту с кашей в моей тарелке уже было покончено. Я отнесла её и вышла из столовой."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (2)
    
    #домик-выбор
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_sl_day with dissolve
    window show
    "Дома я открыла шкаф и достала нужную бумажку. Положив её рядом со своей формой, я решила подумать, что мне делать сейчас."
    th "Нужно потратить ещё полчаса на что-нибудь неактивное.{w} Но просто так их пролежать я тоже не могу.{w} Что же делать?.."
    window hide
    menu:
        "Искать ключи":
            $ sl_m_day2_find_keys = True
            window show
            "Ответ пришёл сам собой. Нужно искать ключи."
            th "Пойду поброжу по лагерю, может найду где-нибудь..."
            window hide
            stop ambience fadeout 2
            scene black with dissolve
            pause (4)
            play ambience ambience_int_cabin_day fadein 3
            scene bg int_house_of_sl_day with dissolve
            window show
            "Около часа я искала по всему лагерю, но так и не нашла своих ключей. В конце концов, я вернулась в домик."
            jump slavyana_mod__day2_cnt1
        "Поискать занятие в домике":
            window show
            "Я осмотрела домик и задержалась на половине, принадлежащей Жене. У неё всегда в домике было несколько книг, и я решила взять одну из них."
            th "Конечно, я лучше бы пошла и занялась чем-нибудь общественно-полезным, но своё единственное задание я уже почти выполнила и в ближайшее время мне нечем заняться, а это лучше чем ничего."
            "Взятой мною книгой оказались «Русские народные сказки», одна из тех книг, которые я до сих пор уважала и могла перечитывать множество раз. Даже издание оказалось в точности такое же, как и у меня дома. Я углубилась в чтение..."
            window hide
            stop ambience fadeout 2
            scene black with dissolve
            pause (2)
            play music music_list["forest_maiden"] fadein 3
            scene bg int_house_of_sl_day with dissolve
            window show
            "Час прошёл незаметно. Я словно вернулась в детство, когда слушала, как мне рассказывает мама, а потом я и сама научилась читать и зачитывала эти сказки «до дыр»."
            "Потом я стала взрослеть и так много времени на чтение подобной литературы выделять больше не получалось, но, иногда, как сейчас, я всё таки выкраивала несколько минут на свою любимую книгу."
            window hide
            stop music fadeout 3
            play ambience ambience_int_cabin_day fadein 3
            pause (1)
            window show
            jump slavyana_mod__day2_cnt1

    #побежали
label slavyana_mod__day2_cnt1:
    "Часы показывали ровно 10 часов утра."
    th "В самый раз, как раз успею и побегать и переодеться, чтобы пойти на линейку."
    if sl_m_day2_find_keys:
        "Бегать я решила даже несмотря на то, что уже исходила весь лагерь вдоль и поперёк."
        th "Думаю, нет ничего плохо в ещё одной прогулке по лагерю, только уже в более быстром темпе.{w} Да и я совсем не устала после предыдущего раза."
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_house_of_sl_day with dissolve
    "Я вышла на крыльцо, вдохнула свежего воздуха и побежала."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (5)
    play music music_list["everyday_theme"] fadein 5
    scene bg ext_washstand_day
    show pi normal pioneer far at center
    with dissolve
    window show
    "Мой маршрут пролегал через умывальники. В это время там оказался Семён, судя по виду, недавно проснувшийся."
    sl "Физкульт-привет!"
    show pi surprise pioneer at center with dspr
    me "Охай… То есть, бобр… Доброе утро! Вот…"
    "Семён сначала говорил что-то странное, но потом всё же перешёл на разборчивую речь."
    th "Видимо, он ещё не до конца проснулся."
    sl "Почему на завтрак не пришёл?"
    show pi smile pioneer at center with dspr
    me "Проспал."
    "Сказал он, будто был очень доволен своим поступком."
    show pi normal pioneer at center with dspr
    me "Но мне Ольга Дмитриевна бутерброды принесла."
    sl "А, ну отлично тогда! Не забудь про линейку!"
    me "Да, конечно."
    sl "Ладно, я побежала, не скучай!"
    hide pi with dissolve
    "Я помахала ему на прощание и побежала дальше."
    window hide
    stop music fadeout 3
    scene black with dissolve
    pause (3)
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_house_of_sl_day with dissolve
    window show
    "Ещё минут через 10 я решила закругляться и прибежала домой."
    stop ambience fadeout 2
    play sound sfx_open_dooor_campus_1
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_sl_day with dissolve
    "Немного отдышавшись и переодевшись, я взяла обходной для Семёна, положила себе в карман и пошла на линейку."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (1)
    
    #линейка
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_square_day with dissolve
    window show
    "На площади уже собралась большая часть пионеров, но вот вожатой нигде не было видно. Впрочем, до линейки ещё было несколько минут, поэтому в этом не было ничего страшного."
    window hide
    pause (1)
    show dv normal pioneer far:
        xalign 0.0 yalign 0.5
        linear 0.5 xalign 2.0
    with dspr
    pause (1)
    show pi normal pioneer far at left
    show mt normal panama pioneer far at right
    hide dv
    with dissolve
    window show
    "Вскоре пионеры начали выстраиваться в одну шеренгу, ещё чуть позже прибежала Алиса, а потом на площадь пришли Ольга Дмитриевна с Семёном."
    me "А что, ещё не все пришли?"
    mt "Да вроде все."
    "Оля посмотрела в нашу сторону, бегло подсчитывая нас."
    mt "Ладно, иди становись."
    hide pi with dissolve
    show mt normal panama pioneer far:
        linear 0.5 xalign 0.5
    "Она вышла на центр площади. Семён встал в шеренгу."
    play music music_list["get_to_know_me_better"] fadein 5
    scene cg d2_lineup_an with dissolve
    mt "Доброе утро, отряд! Сегодня я расскажу вам о плане мероприятий на неделю…"
    "В целом, Ольга Дмитриевна рассказывала то же самое, что рассказала мне вчера, после пляжа. К сожалению, на сегодня никаких особо важных дел не оказалось, а вот на завтра была запланирована масштабная уборка территории, прямо перед дискотекой."
    window hide
    pause (2)
    window show
    "В самом конце Ольга Дмитриевна произнесла:"
    mt "Славя, подойди ко мне, Семён – останься на площади. Для остальных линейка окончена!"
    scene bg ext_square_day
    show pi normal pioneer at cright 
    show mt normal panama pioneer at cleft 
    with dissolve
    "Пионеры начали расходиться, мы же с вожатой подошли к Семёну. Он стоял и задумчиво рассматривал памятник."
    sl "О чём мечтаешь?"
    "Семён перевёл взгляд в нашу сторону."
    mt "Ты запомнил план на неделю?"
    "От Ольги Дмитриевны задумчивость Семёна тоже не укрылась."
    me "План?{w} План я никогда не забуду!"
    "Выпалил он, но мне почему-то показалось, что не знает он никакого плана..."
    show mt smile panama pioneer at cleft with dspr
    mt "Вот и отлично!"
    "А вот Ольге Дмитриевне так не казалось.{w} Она перевела взгляд на меня и спросила:"
    show mt normal panama pioneer at cleft with dspr
    mt "Принесла?"
    sl "Да."
    "Я отдала Семёну обходной."
    "Ольга Дмитриевна принялась объяснять, что нужно делать с этой бумагой (которую она не проверяет), а затем последовало стандартное:"
    mt "Всё понял?"
    me "Да."
    "На этот раз Семён действительно слушал, стараясь запомнить все «бесценные» указания."
    mt "Тогда давай, начинай прямо сейчас."
    me "А как же обед?"
    mt "Ничего страшного! Я тебе ещё бутербродов принесу. Обходной лист важнее!"
    th "По крайней мере, все должны так думать."
    sl "Удачи тебе."
    stop music fadeout 3
    hide mt
    hide pi 
    with dissolve
    "Сказала я на прощание и пошла за Ольгой Дмитриевной, рукой поманившей меня за собой."
    scene bg ext_houses_day
    show mt normal panama pioneer at center
    with dissolve
    sl "Что вы хотели?"
    "Спросила я у вожатой, когда поравнялась с ней."
    show mt surprise panama pioneer at center with dspr
    mt "Славя! Мы же договорились!"
    "Воскликнула Оля.{w} Я вспомнила о нашей вчерашней договорённости."
    sl "Прости, я ещё никак не привыкну."
    show mt smile panama pioneer at center with dspr
    mt "Ничего."
    show mt normal panama pioneer at center with dspr
    mt "Я совершенно забыла об этом на линейке, но сейчас вспомнила: тебе нужно зайти к кибернетикам, попросить их проверить аппаратуру к завтрашней дискотеке. Мало ли, сломалась, чтобы завтра аврал им не устраивать."
    mt "А потом, после обеда, сходи на пляж и последи там за порядком."
    sl "Хорошо, уже иду!"
    "Сказала я и завернула к своему домику."
    stop ambience fadeout 2
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_sl_day with dissolve
    "В домике я надела купальник (чтобы после столовой сразу пойти на пляж) и отправилась к клубам."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (2)
    
    #электроники
    play ambience ambience_clubs_inside_day fadein 3
    scene bg int_clubs_male_day
    show pi normal pioneer at center
    show el normal pioneer at left 
    show sh normal pioneer at right   
    with dissolve
    window show
    "В клубе кроме обычных его обитателей я встретила ещё и Семёна с обходным."
    sl "А, Семён! Надеюсь, они тебя тут не достают?"
    "Я строго посмотрела на будущих светил отечественного роботостроения. Они уже были замечены в попытке увеличения количества членов своего клуба путём обмана и шантажа. А кружки – дело добровольное."
    sl "А то я их знаю – они могут!"
    me "Да, понимаешь, на самом деле мне бы просто обходной подписать…"
    sl "Так это не проблема, давай сюда."
    hide pi
    hide el
    with dissolve
    show sh normal pioneer close:
        linear 0.5 xalign 0.5
    "Я взяла листок и подошла к Шурику, главе кружка кибернетики."
    sl "Подписывай!"
    show sh upset pioneer close at center with dspr
    sh "Ну подожди, мы ещё не закончили…"
    "Пролепетал он."
    th "Ах они опять..."
    sl "Закончили! Подписывай!"
    show el normal pioneer at left 
    show sh upset pioneer at right
    show pi normal pioneer at center
    with dissolve
    "Шурик решил не возражать мне и подписал обходной."
    hide pi with dissolve
    "Семён поблагодарил меня и вышел из здания."
    show el normal pioneer:
        linear 1.0 xalign 0.16 xanchor 0.5
    with dspr
    sl "А вас я попрошу остаться!"
    "Начала я, заметив, что Электроник пытается уйти «по-тихому»."
    sl "Это что ещё такое? С вами же уже был разговор, не так ли?"
    sh "Да, был, но понимаешь, у нас нехватка рук..."
    sl "Решайте эту проблему другим путём, а эти свои методы забудьте!"
    sl "А теперь перейдём к делу: вожатая просила вас проверить звукоаппаратуру для завтрашней дискотеки. Пойдёмте."
    "Кибернетики вздохнули и пошли за мной."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (2)
    
    #сцена
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_stage_normal_day with dissolve
    window show
    "Оборудование хранилось под сценой и состояло из нескольких колонок, пары пультов и огроменной груды проводов."
    "И если проводов было настолько много, что на один испорченный можно было найти ещё с десяток других (но неизвестно, рабочих ли), то вот те же колонки или пульты любили ломаться, и их приходилось постоянно чинить."
    window hide
    scene black with dissolve
    pause (1)
    scene bg ext_stage_normal_day with dissolve
    window show
    "..."
    window hide
    scene black with dissolve
    pause (2)
    scene bg ext_stage_normal_day with dissolve
    play sound music_list["dinner_horn_processed"]
    window show
    "Шурик с Электроником залезли под сцену и копошились там около получаса, пока не прозвучал сигнал начала обеда."
    show el normal pioneer:
        xalign 0.16 ypos 1.0
        linear 2.0 yalign 0.5
    with dissolve
    "Сначала показалась голова Электроника, потом и сам кибернетик, выволакивающий груду проводов."
    show sh normal pioneer at right with dissolve
    extend " Следом вылез Шурик, потирая руки."
    sh "Эти провода мы заберём для дальнейшего разбирательства, а ещё...{w} Ещё нам понадобится спирт для протирки контактов."
    sl "Хорошо, я поговорю с Ольгой Дмитриевной на эту тему."
    hide el
    hide sh
    with dissolve
    "Удовлетворившись таким ответом, они ушли в сторону здания клубов, я же пошла в столовую."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (2)
    
    #столовая-обед
    play ambience ambience_dining_hall_full fadein 2
    scene bg int_dining_hall_people_day with dissolve
    window show
    "Несмотря на то, что обед объявили только пять минут назад, столовая уже была битком. За одним столом сидели Лена и Женя. Я подошла к ним."
    show un smile pioneer at left
    show mz normal glasses pioneer at right
    with dissolve
    sl "У вас тут не занято?"
    un "Нет, садись."
    hide un
    hide mz
    with dissolve
    "Я сходила за едой и вернулась обратно."
    show un smile pioneer at left
    show mz normal glasses pioneer at right
    with dissolve
    sl "Как у вас дела?"
    show un grin pioneer at left with dspr
    un "А ты у Жени спроси, она ведь спит посреди дня."
    show mz angry glasses pioneer at right with dspr
    mz "И ничего я не спала! Только прилегла на пару минут и всё!"
    un "А как же ты новенького проморгала?"
    mz "А может я за ним наблюдала?"
    show un smile2 pioneer at left with dspr
    un "Ага, как же."
    "Сказала Лена и усмехнулась."
    mz "В конце-то концов, даже если я и спала, там всё равно никого не бывает!"
    sl "А если Ольга Дмитриевна зайдёт?"
    show mz bukal glasses pioneer at right with dspr
    mz "Ой, всё, сдаюсь!"
    "Женя уткнулась взглядом в тарелку."
    show un smile pioneer at left with dspr
    "Мы с Леной дружно рассмеялась."
    th "И всё-таки Лена не такая уж замкнутая и унылая, иногда она может быть даже весёлой."
    hide un
    hide mz
    with dissolve
    window hide
    pause (2)
    window show
    "Минут через десять я доела обед и вышла."
    stop ambience fadeout 2
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_dining_hall_near_day with dissolve
    "Мне предстояло отправиться на пляж и присматривать там за порядком. Благо, купальник уже был на мне, и не нужно было идти до дома.{w} Даже несмотря на то, что прогулки на свежем воздухе полезны, исполнять указания руководства нужно как можно быстрее."
    stop ambience fadeout 2

    #пляж
    play ambience ambience_lake_shore_day fadein 2
    scene bg ext_beach_day with dissolve
    "На пляже никого не было.{w} Пока никого не было, но через 10-15 минут сюда нахлынет толпа пионеров, ищущих спасения от полуденного зноя в воде или же желающих позагорать под палящим солнцем.{w} А сейчас пусто и спокойно."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (2)
    play ambience ambience_lake_shore_day fadein 2
    scene bg ext_beach_day with dissolve
    window show
    "И действительно, в положенный срок появились первые пионеры, потом ещё немного и вскоре весь пляж был битком."
    "Но это не прибавляло мне работы: проблем здесь почти никогда не возникало. Отгороженная для купания зона не отличалась особой глубиной, а за буйки никто старался не плавать, хотя и там утонуть было сложно: озеро почти всегда было спокойным, поэтому, если умеешь плавать, можно было хоть до островов плавать."
    "В целом, работа на пляже таковой не являлась: нужно было лишь смотреть по сторонам и всё время ждать неприятностей. Но разрешалось плавать и загорать, то есть всё то, зачем люди и ходят на пляж."
    "Однако за несколько часов всё это утомляло и хотелось уйти отсюда как можно быстрее."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (4)
    play ambience ambience_lake_shore_day fadein 2
    scene bg ext_beach_day with dissolve
    window show
    "Примерно за полчаса до ужина, когда солнце уже начало приближаться к горизонту, пионеры разошлись."
    "Немного подождав, я убедилась, что никого больше не будет и со спокойной душой отправилась к столовой."
    stop ambience fadeout 2
    
    #столовая-спор
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_dining_hall_near_day
    show el upset pioneer at center
    with dissolve
    "На крыльце столовой сидел Электроник и держался за глаз."
    sl "Привет, что у тебя с глазом?"
    "Спросила я и присела рядом."
    show el angry pioneer close at center with dspr
    el "Алиса, что же ещё!"
    th "Значит, как людей обманывать, так он первый, а как от Алисы получать, так нам страшно!"
    "Подумала я, но виду не подала. Всё-таки драка – неподобающее занятие для пионера, а уж тем более для пионерки."
    show us normal pioneer at right behind el
    show dv smile pioneer at left behind el
    with dissolve
    "К столовой подошли улыбающаяся Алиса и Ульяна."
    th "Легка на помине."
    dv "Ну, как глаз поживает?"
    show el upset pioneer close at center with dspr
    el "Знаешь, как болит!"
    "Ответил Электроник жалобным голосом."
    show dv laugh pioneer at left behind el with dspr
    dv "Чему болеть-то, прошло всё!"
    "Сказала Алиса и рассмеялась."
    "Я нахмурилась и произнесла:"
    sl "Алиса, это ты виновата?"
    dv "Почему сразу я-то?"
    show el scared pioneer close at center with dspr
    stop ambience fadeout 2
    play music music_list["awakening_power"] fadein 5
    el "Конечно она, а кто ж ещё!"
    "Встрял в разговор Электроник. Алиса зло посмотрела на него."
    dv "Если уж на то пошло, ты сам напросился."
    show el surprise pioneer close at center with dspr
    el "Да почему? Я ж ничего не делал!"
    dv "А вчера на этом месте кто обзывался? Сказал – получил, всё справедливо."
    el "Я просто представлял тебя!"
    dv "Ну и всё тогда. И больше не называй меня ДваЧе, а то ещё получишь!"
    show dv laugh pioneer behind el:
        linear 0.5 xalign 0.16
    show pi normal pioneer behind dv:
        xalign 0.14 xanchor 0.5
    show mt normal pioneer at fright behind us
    with dissolve
    "К нам подошли Семён и Ольга Дмитриевна и стали наблюдать за происходящим."
    el "Да не называл я тебя так! Тебе показалось!"
    show us grin pioneer at right behind el with dspr
    us "Называл, называл, я всё слышала!"
    show el angry pioneer close at center with dspr
    el "Да тебя вообще там не было!"
    us "А вот и была! Я в кустах сидела!"
    "Мне начинал надоедать этот бесполезный спор."
    sl "Хватит вам! Прекратите!"
    "Ольга Дмитриевна попыталась выяснить, что происходит:"
    mt "Что вы тут ругаетесь?"
    sl "Алиса Сыроежкину в глаз…"
    dv "Ничего я не делала!"
    hide dv with dissolve
    "Обиженно фыркнула Алиса и вошла в оказавшуюся открытой столовую."
    stop music fadeout 3
    mt "Ладно, пора ужинать."
    "Подытожила Ольга Дмитриевна. Все потянулись ко входу."
    
    #столовая-ужин
    play ambience ambience_dining_hall_full fadein 2
    scene bg int_dining_hall_people_day with dissolve
    "Несмотря на то, что перепалка началась ещё до ужина, и, казалось, быстро закончилась, в столовой уже было мало свободных мест. Несколько незанятых оказалось рядом с Шуриком и Электроником, куда я и направилась."
    "Они не стали возражать и вскоре я уже приступила к ужину, который включал в себя гречку с курицей и чай."
    show el normal pioneer at left
    show sh normal pioneer at right
    with dissolve
    el "Да, Славя... Спасибо, за то, что помогала."
    "Завёл разговор Электроник."
    sl "Да не за что!"
    "Сказала я и улыбнулась."
    sh "Слушай, Славя, ты уже говорила с вожатой насчёт нашей просьбы?"
    sl "Нет, после ужина собиралась. А что?"
    sh "Да нет, просто чем раньше мы сможем это сделать, тем лучше."
    sl "Я тебе обязательно расскажу, когда спрошу."
    sh "Хорошо."
    hide el
    hide sh
    with dissolve
    window hide
    pause (1)
    show el normal pioneer at left
    show sh normal pioneer at right
    with dissolve
    window show
    el "Славя, а у вожатой карты есть?"
    sl "Да должны быть...{w} Зачем они тебе?"
    el "Я пока что не могу рассказать. Чуть попозже, хорошо?"
    th "Что-то он темнит почём зря, как мне кажется..."
    sl "Надеюсь, ничего плохого?"
    el "Нет, что ты, что ты! Ну ладно, я тогда пойду вожатую поищу."
    hide el with dissolve
    show sh normal pioneer at right:
        linear 0.5 xalign 0.5
    "Сказал он, встал и ушёл."
    sl "А ты не знаешь, о чём он говорит?"
    sh "Нет, мне он тоже не рассказывает. Говорит только что ему нужны карты и что у него есть замечательная идея."
    hide sh with dissolve
    window hide
    pause (2)
    show sh normal pioneer at center with dissolve
    window show
    sl "Я пойду Ольгу Дмитриевну найду, спрошу у неё про твою просьбу. Пока."
    "Сказала я и встала из-за стола."
    sh "Пока."
    hide sh with dissolve
    "Вожатая как раз собиралась выходить на улицу. Я пошла за ней."
    stop ambience fadeout 2
    
    #столовая-задание
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["lightness"] fadein 5
    scene bg ext_dining_hall_near_sunset
    show el normal pioneer at left 
    show mt normal pioneer at center 
    show pi normal pioneer at right 
    with dissolve
    "На крыльце стояли Семён и Электроник."
    el "Ольга Дмитриевна! А Семён как раз хотел у вас карты попросить!"
    show pi surprise pioneer at right with dspr
    me "Я вообще-то…"
    "Попытался что-то высказать Семён, но Ольга Дмитриевна не дала ему договорить:"
    mt "Зачем?"
    show el smile pioneer at left with dspr
    el "Мы игру новую придумали!"
    "Гордо сказал светловолосый кибернетик."
    show mt surprise pioneer at center with dspr
    mt "Что за игра?"
    el "Будут карты – я покажу."
    show mt sad pioneer at center with dspr
    mt "Ох, не нравится мне эта идея…{w} Но раз и Семён за, то, наверное, ничего страшного…"
    me "Да я вообще-то…"
    sl "Давайте я с ним схожу принесу!"
    window hide
    menu:
        "Пойти с Семёном":
            $ sl_m_lp += 2
            $ sl_m_day2_go_with_sp = True
            jump slavyana_mod__day2_go_with_sp
        "Остаться":
            jump slavyana_mod__day2_stay

    #поиск с Семёном
label slavyana_mod__day2_go_with_sp:
    window show
    th "Всё-таки он новенький, надо ему помочь ориентироваться.{w} Да и неуверенна я, что карты у Оли в домике..."
    me "Если ты не против…"
    "Неуверенно начал Семён."
    stop ambience fadeout 2
    sl "Конечно! Пошли."
    scene bg ext_houses_sunset with dissolve
    "Мы отправились к домику Ольги Дмитриевны."
    "Где-то на полпути я вдруг остановилась, вспомнив, что карты не там, куда мы направляемся:"
    show pi normal pioneer at center with dissolve
    sl "Ой, я же совсем забыла, что карты у меня!"
    me "А где твой домик?"
    sl "Да тут рядом, пойдём!"
    "Отсюда как раз было недалеко до меня."
    scene bg ext_house_of_sl_day 
    show pi normal pioneer at center 
    with dissolve
    sl "Подожди тут минутку, я сейчас!"
    play ambience ambience_int_cabin_evening fadein 2
    scene bg int_house_of_sl_day with dissolve
    "Я забежала внутрь. Карты лежали на одной из полок шкафа. Схватив их, я вернулась на улицу."
    stop ambience fadeout 2
    scene bg ext_house_of_sl_day 
    show pi normal pioneer at center 
    with dissolve
    sl "Вот!"
    "Я показала Семёну предмет поисков – слегка потрёпанную колоду карт."
    me "Краплёные небось?"
    sl "Жульничать не спортивно!"
    sl "Пойдём?"
    me "Пойдём."
    scene bg ext_houses_sunset with dissolve
    "На обратном пути Семён стал расспрашивать меня:"
    show pi normal pioneer at center with dissolve
    me "А ты давно приехала?"
    sl "Уже неделю здесь."
    me "Понятно… А сама откуда?"
    sl "Я с севера."
    me "А поточнее?"
    sl "Холодного севера."
    "Я посмотрела на Семёна и улыбнулась."
    th "Не думаю, что ему нужно знать мой точный адрес."
    me "А что тебе нравится?"
    sl "В смысле?"
    me "Ну, твои увлечения?"
    sl "Ааа… Я природу люблю."
    me "Природу?.. Ясно.{w} Хочешь стать натуралистом?"
    sl "Скорее краеведом. Всегда интересовалась историей родной страны."
    me "А почему ты именно в этот лагерь поехала?"
    sl "Родителям путёвку на работе дали."
    th "Точнее, папе. Более того, даже несколько – на выбор."
    me "Ну, предположим, если бы у тебя был выбор?"
    "Семён, кажется, читал мои мысли."
    sl "Здесь хорошо.{w} Не думаю, что выбрала бы какое-нибудь другое место – здесь кажется, что ты становишься каким-то другим человеком!"
    me "В смысле «другим»?"
    sl "Ну, столько возможностей, столькому можно научиться, стольких людей узнать!"
    "Внезапно моя речь стала похожа на какие-то лозунги. Внутри себя я рассмеялась."
    th "Вот и общайся после этого с Олей!"
    stop music fadeout 3
    "На этом вопросы у Семёна закончились."
    play ambience ambience_camp_center_evening fadein 3
    scene bg ext_dining_hall_near_sunset 
    show pi normal pioneer at cleft 
    show mt normal pioneer at cright 
    with dissolve
    "Когда мы вернулись, Ольга Дмитриевна сказала мне:"
    mt "Я же вспомнила, что карты у тебя!"
    sl "Да ничего, мы принесли."
    show mt smile pioneer at cright with dspr
    mt "Ну и отлично!"
    stop ambience fadeout 2
    jump slavyana_mod__day2_cnt2

    #постоять, подумать
label slavyana_mod__day2_stay:
    window show
    th "А может, я и зря это сказала. Семён ведь не маленький, и сам сходить может..."
    show pi normal pioneer at right with dspr
    me "Да я и один могу сходить…"
    show mt normal pioneer at center with dspr
    mt "Ладно. Возьмёшь у меня в домике в ящике стола."
    hide pi 
    hide mt
    hide el
    with dissolve
    stop music fadeout 3
    "Семён ушёл в направлении своего с вожатой домика, а я всё никак не могла успокоиться. Я пыталась что-то вспомнить, но у меня никак не получалось..."
    th "А карты точно там, куда пошёл Семён?{w} Может, мне сходить за ним?"
    window hide
    menu:
        "Пойти за Семёном":
            $ sl_m_lp += 1
            $ sl_m_day2_sp_keys = True
            jump slavyana_mod__day2_go_for_sp
        "Остаться":
            jump slavyana_mod__day2_only_stay

    #поиск Семёна
label slavyana_mod__day2_go_for_sp:
    show mt normal pioneer at center with dissolve
    window show
    "Я подошла к вожатой и сказала:"
    sl "Ольга Дмитриевна, давайте я схожу за Семёном, а то он что-то долго."
    mt "Хорошо, иди."
    scene bg ext_houses_sunset with dissolve
    "Посреди дороги я вдруг встала как вкопанная."
    th "Карты же у меня остались!"
    "Я побежала к себе в домик."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (1)
    play ambience ambience_int_cabin_evening fadein 2
    scene bg int_house_of_sl_day with dissolve
    window show
    "Внутри никого не было."
    "Я открыла шкаф. Карты лежали на одной из полок."
    "Взяв их и сняв уже бесполезный купальник, я пошла в сторону домика вожатой."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (1)
    play ambience ambience_int_cabin_evening fadein 2
    scene bg int_house_of_mt_sunset with dissolve
    window show
    "Семён стоял и смотрел в шкаф."
    sl "Семён, что ты тут так долго?"
    show pi shocked pioneer with dissolve
    me "А... я... да..."
    "Он закопошился. В его руке что-то заблестело. Я подошла ближе и увидела... свои ключи!"
    sl "Ой, мои ключи! А я их обыскалась! Где ты..."
    "Я была несказанно рада."
    me "Да вот по дороге... В кустах валялись..."
    me "Пойдём?"
    window hide
    scene black with dissolve
    pause (1)
    stop ambience fadeout 2
    play ambience ambience_camp_center_evening fadein 3
    scene bg ext_dining_hall_near_sunset 
    show mt normal pioneer at right 
    show pi normal pioneer at left 
    with dissolve
    window show
    "Когда мы вернулись к столовой, Ольга Дмитриевна с невозмутимым видом сказала Семёну:"
    mt "Ой, извини, а карты у Слави были в домике.{w} Пока ты ходил, она сбегала."
    th "Видимо, это и Ольга Дмитриевна вспомнила."
    "Семён посмотрел на меня, я виновато улыбнулась в ответ."
    stop ambience fadeout 2
    jump slavyana_mod__day2_cnt2

    #постоять, ещё подумать
label slavyana_mod__day2_only_stay:
    window show
    th "Думаю, что он и сам скоро вернётся."
    window hide
    pause (1)
    window show
    "Я стояла, силясь вспомнить что-то...{w} Что-то, несомненно, важное и именно сейчас. Но мне никак не удавалось."
    "И вдруг... Я вспомнила, что карты оставались у меня."
    "Я их попросила у вожатой как-то раз для гадания. Нам с Женей выпали «скорые свидания», на что Женя с умным видом заявила, что всё это бред и что из всех возможных результатов именно этот может выпасть с такой-то вероятностью."
    "Но я видела, как она заинтересовалась, сразу же после оглашения результатов! Впрочем, сейчас это не важно, нужно сходить за картами."
    show mt normal pioneer at center with dissolve
    sl "Ольга Дмитриевна, карты тогда у меня остались, давайте я за ними схожу."
    mt "Хорошо, иди."
    hide mt with dissolve
    "Я побежала к себе в домик."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (2)
    play ambience ambience_int_cabin_evening fadein 2
    scene bg int_house_of_sl_day with dissolve
    window show
    "Внутри никого не было."
    "Я открыла шкаф. Карты лежали на одной из полок."
    "Взяв их и сняв уже бесполезный купальник, я пошла обратно к столовой."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (3)
    play ambience ambience_camp_center_evening fadein 3
    scene bg ext_dining_hall_near_sunset
    show pi normal pioneer at cleft 
    show mt normal pioneer at cright 
    with dissolve
    window show
    "Через минуту после меня пришёл Семён. Ольга Дмитриевна с невозмутимым видом сказала ему:"
    mt "Ой, извини, а карты у Слави были в домике.{w} Пока ты ходил, она сбегала."
    "Семён посмотрел на меня, я виновато улыбнулась в ответ."
    stop ambience fadeout 2
    jump slavyana_mod__day2_cnt2

    #перед игрой
label slavyana_mod__day2_cnt2:
    play ambience ambience_medium_crowd_indoors_1 fadein 3
    scene bg int_dining_hall_sunset with dissolve
    "Мы с Ольгой Дмитриевной зашли внутрь столовой. Я вспомнила про просьбу Шурика:"
    show mt normal pioneer at center with dissolve
    sl "Оль, там кибернетики просят спирта на протирку контактов."
    mt "Да? Хорошо, завтра зайди к Виоле, у неё должен быть спирт.{w} Только ты проконтролируй, чтобы исключительно на протирку."
    sl "Оля! Они порядочные!"
    mt "Доверяй, но проверяй. Особенно в таких делах. И не забудь вернуть остатки в медпункт!"
    sl "Хорошо."
    hide mt with dissolve
    "Я осмотрела столовую. Внутри всё уже было готово."
    "Тут и там толпились пионеры, весело разговаривая о своём. Столы сдвинули поближе к стенам, чтобы освободить место для игроков и зрителей."
    show cg lvl_1 with dissolve
    "В одном из углов стоял лист ватмана со схемой игроков."
    th "Значит, мне в первом туре играть с Женей. Но где она?"
    hide cg lvl_1 with dissolve
    "Жени нигде не было."
    th "Думаю, она скоро придёт."
    "Я отошла от схемы и присела за один из столов, предназначенных для участников."
    "Около схемы о чём-то спорили Семён и Электроник. Рядом прыгала Ульяна и что-то кричала про призы. Потом подошла Оля, и Семён куда-то убежал."
    th "Надеюсь, начало уже скоро."
    window hide
    scene black with dissolve
    pause (2)
    scene bg int_dining_hall_sunset with dissolve
    window show
    "Через несколько минут вернулся Семён, за ним вошла Женя."
    th "Начинается."
    show el normal pioneer at center with dissolve
    "Все внимательно посмотрели на Электроника."
    el "Итак..."
    "Прокашлялся он."
    el "Каждый тур состоит из одной игры."
    el "В случае ничьей будет переигровка."
    el "После этого проигравший выбывает, и начинается следующий тур."
    el "Поскольку добровольцев..."
    "Он посмотрел куда-то в сторону и исправился:"
    el "Поскольку участников – восемь, то и туров будет три."
    el "Всё понятно?"
    "Толпа пионеров весело загалдела."
    show us laugh pioneer at left with dissolve
    us "А призы какие, призы?"
    "Вновь завелась Ульяна."
    sl "Ульяна, хватит!"
    "Я подалась вперёд, пытаясь остановить её."
    show us laugh pioneer at right with dissolve
    us "Пока не выиграю приз, не успокоюсь!"
    th "И откуда в ней столько энергии?"
    show us laugh pioneer at left with dissolve
    us "Призы-призы!"
    "Как заведённая кричала Ульяна."
    sl "Прекрати."
    "Мне надоело ловить ее, и я перешла на уговоры."
    show el shocked pioneer at center with dspr
    "А у Электроника, похоже, от всей этой беготни вокруг него уже закружилась голова."
    show us laugh pioneer at right
    show pi normal pioneer at left
    with dissolve
    me "Давайте начинать."
    "Спокойно сказал Семён и добавил, обращаясь к Ульяне:"
    me "А то никаких призов не получишь."
    "Такой аргумент, похоже, подействовал, и она вернулась на своё место."
    hide us with dissolve
    "Я последовала за ней, благодарно улыбнувшись Семёну."
    hide pi with dissolve
    show el normal pioneer at center with dspr
    "Пионеры наконец угомонились."
    "Электроник начал объяснять правила. Они оказались предельно просты: ты берёшь карту – у тебя берут карту. При желании можно немного попутать соперника. Ничего запредельно сложного."
    hide el with dissolve
    show mz bukal glasses pioneer at center with dissolve
    sl "Ну как тебе игра?"
    mz "Ничего интересного. Туфта, одним словом."
    "Я не стала отвечать."
    "Турнир начался."
    window hide

    #картишки
    menu:
        "Играть в карты":
            jump slavyana_mod__cards_mz_play
        "Указывать исходы":
            pass
    #читы
    menu:
        "Победить":
            jump slavyana_mod__cards_mz_win
        "Проиграть":
            jump slavyana_mod__cards_mz_lose

    #игра
label slavyana_mod__cards_mz_play:
    python:
        dialogs = {
                        (0,"win","jump"):  "slavyana_mod__cards_mz_win",
                        (0,"fail","jump"): "slavyana_mod__cards_mz_lose",
                        (0,"draw","jump"): "slavyana_mod__cards_mz_draw",
                    }
        generate_cards("bg hall",dialogs)
        rival = CardGameRivalDv(sl_m_mz_avatar_set,"Женя")
    jump cards_gameloop

    #победа
label slavyana_mod__cards_mz_win:
    scene bg int_dining_hall_sunset
    show mz bukal glasses pioneer at center 
    with dissolve
    $ sl_m_day2_you_win = True
    window show
    "Это оказалось даже проще, чем я думала.{w} А вот Женя выглядела слегка... расстроенной?"
    sl "Жень, ты что расстроилась?"
    mz "Я? Нет, ты что."
    sl "А может, я тебе свою победу отдам?"
    show mz shy glasses pioneer at center with dissolve
    mz "Ну, если ты не хочешь больше играть..."
    sl "Нет."
    show mz smile glasses pioneer at center with dissolve
    mz "Ну тогда... Спасибо."
    sl "Всегда пожалуйста!"
    hide mz with dissolve
    "Я улыбнулась, затем встала и вышла на улицу."
    stop ambience fadeout 2
    jump slavyana_mod__day2_cnt3

    #ничья
label slavyana_mod__cards_mz_draw:
    scene bg int_dining_hall_sunset
    show mz normal glasses pioneer at left
    show el normal pioneer far at right
    with dissolve
    window show
    "К нам подошёл Электроник."
    el "Ничья! Играйте ещё раз."
    window hide
    hide el
    hide mz 
    with dissolve
    jump slavyana_mod__cards_mz_play

    #поражение
label slavyana_mod__cards_mz_lose:
    scene bg int_dining_hall_sunset
    show mz normal glasses pioneer at center 
    with dissolve
    window show
    "И всё-таки Женя оказалась сильнее."
    sl "Удачи!"
    show mz smile glasses pioneer at center with dissolve
    mz "Спасибо, Славя."
    hide mz with dissolve
    "Я встала и вышла на улицу."
    stop ambience fadeout 2
    jump slavyana_mod__day2_cnt3

    #ночные прогулки
label slavyana_mod__day2_cnt3:
    $ persistent.sprite_time = "night"
    $ night_time()
    play ambience ambience_camp_center_night fadein 2
    scene bg ext_dining_hall_away_night with dissolve
    "Снаружи уже было темно. Ночь вступила в свои права, принося с собой прохладу, которой так не хватает долгими летними днями. И, хотя летнее солнцестояние уже прошло, не было заметно, чтобы дни существенно сокращались."
    "В домик в такую замечательную летнюю ночь идти совершенно не хотелось, и я решила посидеть на площади, на скамейке."
    if sl_m_day2_go_with_sp:
        "Но для начала нужно было пойти и снять уже бесполезный купальник."
        window hide
        scene black with dissolve
        stop ambience fadeout 2
        pause (1)
        play ambience ambience_int_cabin_night fadein 2
        scene bg int_house_of_sl_night_light with dissolve
        window show
        "Дойдя до дома, и переодевшись, я вернулась на площадь."
        window hide
        stop ambience fadeout 2
        scene black with dissolve
        pause (1)
        window show
        play ambience ambience_camp_center_night fadein 2
    scene bg ext_square_night with dissolve
    "Вокруг было тихо, только редкие птицы на деревьях и сверчки в траве создавали неповторимую звуковую гамму."
    "Других пионеров в округе не наблюдалось: большинство сейчас находилось в столовой, остальные же сидели по домам, подтверждением чему служил свет в окнах некоторых домов."
    window hide
    pause (3)
    window show
    "Через несколько минут я вспомнила о небольшом озере в лесу, моём тайном месте, где меня никто не мог найти или случайно заметить."
    th "Такая чудесная ночь! Сейчас там должно быть просто замечательно!"
    if sl_m_day2_go_with_sp:
        th "Только зря я, получается, купальник снимала... Но ничего, меня же никто не увидит."
    else:
        th "Правда купаться там придётся вот так, без всего... Но ничего, меня же никто не увидит."
    "Я встала со скамейки и двинулась в направлении тропинки в лес, начинавшейся рядом со зданиями общих клубов, как вдруг... застряла."
    "Посмотрев себе под ноги, я поняла, что каблук одной из моих туфель попал в решётку ливневой канализации. Забавным было то, что обычно я обходила её стороной, а сейчас не заметила под непонятно откуда взявшейся листвой."
    th "Вот что бывает, когда площадь не подметают целый день! Надо будет завтра попроситься сюда, лично размету этот и другие сливы!"
    "Но сейчас размышления о прошлом и будущем были явно лишними. Нужно было выбираться из западни, если я ещё хочу пойти в лес."
    window hide
    scene black with dissolve
    pause (1)
    scene bg ext_square_night with dissolve
    window show
    "К несчастью, каблук умудрился застрять очень прочно. Сколько бы я не пыталась его вытащить, он не собирался поддаваться."
    "Вдруг, я заметила, как кто-то идёт по площади в мою сторону."
    play music music_list["gentle_predator"] fadein 3
    show dv normal pioneer far at center with dissolve
    "Это оказалась Алиса. Увидев её, я быстро вскочила на ноги."
    show dv normal pioneer at center with dissolve
    dv "Привет. Ты что тут делаешь?"
    sl "Привет. Да вот…"
    "Я показала вниз."
    sl "Дурацкая решётка. Не могу теперь вытащить."
    "Я дёрнула ногой, что никак не повлияло на ситуацию. Алиса засмеялась."
    show dv laugh pioneer at center with dspr
    dv "Ты б хоть сняла его вначале! Давай помогу."
    sl "А как я…"
    "«...пойду без обуви?» - хотела сказать я, но Алиса прервала меня:"
    show dv normal pioneer at center with dissolve
    dv "Снимай давай."
    th "Ладно, может у неё лучше выйдет..."
    "Я сняла туфлю и замерла на одной ноге, кое-как сохраняя равновесие."
    "Алиса немного покрутила каблук, и он с лёгкостью вышел из решётки."
    dv "Держи, пионер. Летом надо в сандалиях ходить."
    sl "Спасибо большое!"
    "Я быстро надела туфлю обратно."
    stop music fadeout 3
    sl "А ты что не спишь?"
    "Было уже достаточно поздно, поэтому встреча с кем-либо сама по себе была удивительна."
    show dv shy pioneer at center with dissolve
    dv "Да так…"
    dv "Слушай, ты это, не видела Семёна?"
    if sl_m_day1_al_que:
        "Я быстро улыбнулась."
        th "И вчера вечером она спрашивала про Семёна...{w} Кажется, она им заинтересовалась."
    else:
        th "Кажется, кто-то заинтересовался Семёном..."
    sl "Нет."
    "Невозмутимо ответила я."
    show dv normal pioneer at center with dissolve
    dv "Ладно, неважно, я пойду."
    sl "Спокойной ночи!"
    hide dv with dissolve
    "Ответа не последовало, Алиса развернулась и пошла в сторону домов. Я же продолжила свой маршрут, только на этот раз более внимательно."
    window hide
    scene black with dissolve
    pause (2)
    
    #лес
    play ambience ambience_forest_night fadein 3
    scene bg ext_path_night with dissolve
    window show
    "В лесу было тихо. Тропинки сменяли друг друга, и вскоре я оказалась в чаще. До озера оставалось всего несколько шагов..."
    play music music_list["forest_maiden"] fadein 5
    scene cg d2_slavya_forest with dissolve
    "Деревья расступились, и передо мной открылся чудесный вид на небольшое лесное озеро. Я побежала по берегу вприпрыжку, на ходу стягивая пионерский галстук и расправляя рубашку. Рубашка отправилась на землю, за ней юбка, а потом и всё остальное... "
    if persistent.hentai:
        scene cg d2_sl_swim with dissolve
    else:
        scene bg ext_path_night with dissolve
    "Я наконец-то зашла в воду. Вокруг было тихо и прекрасно, я стояла посередине озера и смотрела вверх, на небо... Вокруг меня была природа, я сама была частью природы... Покой и умиротворение охватывали меня со всех сторон..."
    "Стоять так можно было бы ещё очень долго, но вдруг сзади послышался треск дерева, как будто кто-то наступил на ветку."
    if persistent.hentai:
        scene bg ext_path_night with dissolve
    "Я обернулась, но никого не увидела...{w} Хотя...{w} Среди деревьев мелькнуло что-то белое... но был ли это человек или что-нибудь другое?..{w} А может, мне просто показалось?..{w} В любом случае, мне нужно было собираться и идти обратно, в лагерь."
    window hide
    pause (1)
    window show
    "Я шла по лесу немного другой дорогой, более запутанной, но и более необитаемой. Однако... я постоянно чувствовала на себе чей-то взгляд. Этот кто-то явно шёл за мной по пятам. Честно говоря, я была слегка напугана."
    
    #площадь
    stop ambience fadeout 2
    scene bg ext_square_night with dissolve
    "Но, наконец-то я вышла на площадь."
    show pi surprise pioneer at center with dissolve
    extend " Обернувшись, я заметила Семёна."
    th "Ещё один любитель ночных прогулок по лесу."
    sl "Думаешь, я тебя не заметила?"
    "Семён старался выглядеть спокойным, но бегающие зрачки выдавали его беспокойство."
    me "И давно?"
    sl "Не знаю..."
    "Я подошла чуть поближе."
    sl "Может быть, минут пять."
    me "То есть и там, на озере?.."
    th "Что?!"
    sl "На каком озере?"
    "Я решила притвориться, что ничего не понимаю, но на самом деле я уже всё поняла – Семён прошёл за мной до самого озера..."
    me "Ну..."
    show pi normal pioneer at center with dspr
    me "Ладно, проехали."
    sl "Хорошо."
    th "Хотя бы он не стал ничего говорить по этому поводу..."
    "Всё-таки мне было немного стыдно."
    "Но нужно было как можно быстрее перевести тему:"
    sl "Какая сегодня ночь замечательная!"
    "Я села на скамейку и подняла глаза на небо. Любоваться природой в чьей-то компании было приятнее, чем одной."
    me "Наверное, тут часто бывают такие ночи."
    "Задумчиво сказал Семён."
    sl "Ну, наверное..."
    "Ответила я, а сама пыталась осмыслить всё произошедшее за последние 15 минут."
    me "Почему так неуверенно?"
    "Прервал ход моих мыслей Семён."
    sl "Нет, просто задумалась."
    me "О чём?"
    "Я внимательно посмотрела на него: глаза, спрятанные под волосами, как обычно ничего не выражали."
    th "Значит, он не видит в произошедшем ничего особенного. Тогда и я буду вести себя спокойнее."
    "Я вернулась к созерцанию звёзд.{w} Внезапно захотелось поговорить о чём-то немного более личном, чем со всеми."
    sl "Просто иногда по ночам такое настроение бывает...{w} Днём – вся в делах, даже отдохнуть порой некогда, а ночью тут так тихо."
    sl "Если бы не сверчки и ночные птицы, то кажется, как будто остался наедине с космосом."
    me "Да для меня тут даже слишком спокойно."
    sl "Правда?"
    th "А я-то думала, что он наоборот любит спокойствие и уединение."
    show pi surprise pioneer at center with dspr
    me "Да, правда, а что такого?"
    sl "Ничего..."
    show pi normal pioneer at center with dspr
    "Мы замолчали."
    stop music fadeout 3
    play ambience ambience_camp_center_night fadein 2
    sl "Ладно!"
    "Я резко встала и поправила слегка смявшуюся юбку."
    sl "Уже и спать пора!"
    hide pi with dissolve
    "Я пошла в сторону своего домика."
    me "Спокойной ночи!"
    "Донеслось мне вслед."
    
    #домик
    scene bg ext_houses_night with dissolve
    th "И опять я сбегаю от Семёна...{w} Что же с ним не так?{w} Или это со мной не всё в порядке?.."
    "Мне казалось, что сегодня произошло что-то такое, что не должно было произойти...{w} Но всё равно произошло."
    "И я совершенно не знала, что теперь делать, как теперь вести себя при разговоре с Семёном: избегать его или нет, стесняться его или нет..."
    "Я чувствовала, что произошло что-то такое, что изменит дальнейшее... но в какую сторону?"
    scene bg ext_house_of_sl_night with dissolve
    "Дойдя до домика, я успокоилась и решила, что не нужно ничего менять, проще вести себя так, как обычно, будто ничего не произошло. А там и узнаю, что делать дальше."
    stop ambience fadeout 3
    $ volume(0.1, "sound")
    play sound sfx_open_door_clubs
    scene bg int_house_of_sl_night with dissolve
    "Женя, само собой разумеется, уже спала. Я аккуратно взяла блокнот и вышла на улицу, чтобы не мешать ей."
    play sound sfx_close_door_clubs_nextroom
    
    #блокнот
    play ambience ambience_camp_center_night fadein 2
    scene bg ext_house_of_sl_night with dissolve
    "Открыв блокнот на чистой странице, я продолжила свои записи:"
    show bknt_clear at truecenter with dspr
    play sound_loop pen_write
    show bknt_w4 at truecenter with dissolve2
    $ persistent.sl_m_bknt4 = True
    th "Сегодня, в свой девятый день в этом замечательном лагере я почти проспала завтрак. Спасибо Жене, что разбудила. Но день всё равно не задался с самого утра. Сначала я потеряла ключи."

    if sl_m_day2_find_keys:
        show bknt_w4_1 at truecenter with dissolve2
        $ persistent.sl_m_bknt4_1 = True
        extend " Я искала их по всему лагерю, но так и не нашла."

    if sl_m_day2_sp_keys:
        if sl_m_day2_find_keys:
            show bknt_w4_2_1 at truecenter with dissolve2
            $ persistent.sl_m_bknt4_2_1 = True
        else:
            show bknt_w4_2_2 at truecenter with dissolve2
            $ persistent.sl_m_bknt4_2_2 = True
        extend " Благо, Семён мне их вечером отдал."

    if sl_m_day2_sp_keys:
        if sl_m_day2_find_keys:
            show bknt_w5_1_1 at truecenter with dissolve2
            $ persistent.sl_m_bknt5_1_1 = True
        else:
            show bknt_w5_1_2 at truecenter with dissolve2
            $ persistent.sl_m_bknt5_1_2 = True
    elif sl_m_day2_find_keys:
        show bknt_w5_2 at truecenter with dissolve2
        $ persistent.sl_m_bknt5_2 = True
    else:
        show bknt_w5 at truecenter with dissolve2
        $ persistent.sl_m_bknt5 = True
    th "Под вечер Оля послала меня дежурить на пляже (не самое интересное занятие, честно говоря)."

    if sl_m_day2_you_win:
        if sl_m_day2_sp_keys:
            if sl_m_day2_find_keys:
                show bknt_w6_1_1_1 at truecenter with dissolve2
                $ persistent.sl_m_bknt6_1_1_1 = True
            else:
                show bknt_w6_1_1_2 at truecenter with dissolve2
                $ persistent.sl_m_bknt6_1_1_2 = True
        elif sl_m_day2_find_keys:
            show bknt_w6_1_2 at truecenter with dissolve2
            $ persistent.sl_m_bknt6_1_2 = True
        else:
            show bknt_w6_1 at truecenter with dissolve2
            $ persistent.sl_m_bknt6_1 = True
        extend " А после ужина, на карточном турнире, я выиграла у Жени. Но отдала ей свою победу, ведь она, кажется, расстроилась из-за проигрыша."
    else:
        if sl_m_day2_sp_keys:
            if sl_m_day2_find_keys:
                show bknt_w6_2_1_1 at truecenter with dissolve2
                $ persistent.sl_m_bknt6_2_1_1 = True
            else:
                show bknt_w6_2_1_2 at truecenter with dissolve2
                $ persistent.sl_m_bknt6_2_1_2 = True
        elif sl_m_day2_find_keys:
            show bknt_w6_2_2 at truecenter with dissolve2
            $ persistent.sl_m_bknt6_2_2 = True
        else:
            show bknt_w6_2 at truecenter with dissolve2
            $ persistent.sl_m_bknt6_2 = True
        extend " А после ужина, на карточном турнире, я проиграла Жене. Ну что ж, не только же мне выигрывать."

    if sl_m_day2_you_win:
        if sl_m_day2_sp_keys:
            if sl_m_day2_find_keys:
                show bknt_w7_1_1_1 at truecenter with dissolve2
                $ persistent.sl_m_bknt7_1_1_1 = True
            else:
                show bknt_w7_1_1_2 at truecenter with dissolve2
                $ persistent.sl_m_bknt7_1_1_2 = True
        elif sl_m_day2_sp_keys:
            show bknt_w7_1_2 at truecenter with dissolve2
            $ persistent.sl_m_bknt7_1_2 = True
        else:
            show bknt_w7_1 at truecenter with dissolve2
            $ persistent.sl_m_bknt7_1 = True
    else:
        if sl_m_day2_sp_keys:
            if sl_m_day2_find_keys:
                show bknt_w7_2_1_1 at truecenter with dissolve2
                $ persistent.sl_m_bknt7_2_1_1 = True
            else:
                show bknt_w7_2_1_2 at truecenter with dissolve2
                $ persistent.sl_m_bknt7_2_1_2 = True
        elif sl_m_day2_sp_keys:
            show bknt_w7_2_2 at truecenter with dissolve2
            $ persistent.sl_m_bknt7_2_2 = True
        else:
            show bknt_w7_2 at truecenter with dissolve2
            $ persistent.sl_m_bknt7_2 = True
    th "После турнира я пошла в своё тайное место в лесу. Но... я привела с собой Семёна, который увидел... то, что не должен был. Я не знаю, что мне теперь делать и просто буду ждать."
    stop sound_loop
    
    hide bknt_clear
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
    with dspr
    
    #сон
    "К моменту написания последней строки, моя голова уже весила несколько тонн, и мне казалось, что я могу заснуть прямо здесь, на ступеньках. Но, собрав последние силы, я всё же вошла в дом."
    stop ambience fadeout 3
    play sound sfx_open_door_clubs
    scene bg int_house_of_sl_night with dissolve
    "Часы подсказали мне, что сейчас уже 11 вечера."
    th "Как бы ещё и завтра не проспать."
    "Сняв с себя форму, я улеглась в кровать, но сон никак не шёл. Складывалось впечатление, что мой мозг решил поработать сверх меры, даже не спросив у меня."
    "В голове возникали какие-то образы, какие-то слова и фразы, но из-за сильной усталости у меня не получалось усваивать вырабатываемую информацию."
    window hide
    pause (2)
    window show
    "Ещё немного поворочавшись, я провалилась в сон..."
    window hide
    hide unblink
    show blink
    pause (1)
    scene black with dissolve
    hide blink
    pause (3)
    $ volume(1.0, "sound")
    $ persistent.sl_m_day2 = True
    if sl_m_Full:
        jump slavyana_mod__day3
    jump slavyana_mod__launcher0

#Сделано FireBoTer'ом
    
#Быстрый выбор
label slavyana_mod__day2_fast_choice:

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