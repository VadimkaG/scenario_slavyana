label slavyana_mod__day7_alt:
  $ renpy.pause(2, hard=True)
  stop music
  stop sound
  stop ambience
  $ backdrop = "days"
  $ new_chapter(7, u"Славя. День седьмой")
  $ save_name = (u'Славя. День седьмой')
  $ day_time()
  $ persistent.sprite_time = "day"
  $ renpy.pause(3, hard=True)

  #рут Алисы
  if sl_m_end_dv:
    # play ambience ambience_int_cabin_day fadein 5
    play music music_list["everyday_theme"] fadein 5
    scene bg int_house_of_sl_day
    show unblink
    "Я проснулась как всегда вовремя."
    "Утро было солнечным и за окном тихо пели птички."
    "Я собралась на пробежку, пока моя соседка спит."
    window hide
    pause 1
    scene bg ext_path_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    window show
    th "Сегодня бы только не наткнуться на ту кастрюлю!"
    "Поэтому я специально бежала в обратную сторону. {w}В сторону клуба Мику."
    scene bg ext_musclub_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    "Никого внутри не было. Скорее всего, Мику ещё спала."
    th "Конечно же, как и все остальные. Вот лентяи!"
    scene bg ext_clubs_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    "И кибернетики тоже ещё не проснулись."
    scene bg ext_clubs_day with dissolve
    th "Думаю, они не сильно расстроятся, если я открою клуб заранее."
    stop music fadeout 1
    stop ambience fadeout 3
    scene black with dissolve
    window hide
    pause 1

    play ambience ambience_camp_center_day fadein 3
    scene bg ext_clubs_day with dissolve
    "Я сбегала в домик и взяла свои ключи."
    stop ambience fadeout 2
    play sound sfx_open_door_clubs
    play ambience ambience_clubs_inside_day fadein 3
    scene bg int_clubs_male_day with dissolve
    window show
    "Открыв дверь, я осмотрела помещение."
    "Проверила ящики и зашла в подсобку."
    "Детальный осмотр не привёл ни к чему."
    "Я уже собиралась уходить..."
    play music music_list["two_glasses_of_melancholy"] fadein 2
    el "Ты забыл закрыть клуб?"
    sh "Нет, я точно закрывал. Может ты заходил и забыл?"
    el "Нет."
    sh "Странно."
    play sound sfx_open_door_clubs
    show el normal pioneer at right
    show sh normal pioneer at left
    with dissolve
    "Они зашли внутрь."
    show el surprise pioneer at right with dspr
    el "Славя?.. {w}А что ты тут делаешь?"
    show el normal pioneer at right with dspr
    "Электроник преградил рукой выход из клуба."
    th "Ну не стану же я им говорить что я их подозреваю?"
    sl "Мальчики, вы {b}точно{/b} никуда не прятали содержимое бутылки?"
    el "Нет."
    el "Так а зачем ты зашла?"
    sl "Я подумала, может вы перелили в другую тару, а залить обратно забыли, поэтому и зашла посмотреть."
    th "Да-а.. Не очень-то правдоподобно."
    el "Ключ бы попросила, мы бы дали."
    sl "А если вы нарочно слили и заранее бы спрятали содержимое?"
    sh "Логично. {w}А ты сама случайно ничего у нас не брала?"
    show sh normal pioneer close at left with dspr
    "Шурик подошёл поближе."
    sl "Нет."
    sh "А то у меня отвёртка пропала, не знаешь кто?"
    sl "Не догадываюсь."
    el "А тебе она ни за чем не могла понадобиться?"
    sl "Нет."
    sh "Ладно."
    show sh normal pioneer at left with dspr
    "Шурик прошёл дальше, мимо меня."
    "Электроник отошёл от двери."
    el "Ладно, проходи."
    th "Мне стало необычайно стыдно, за то что я так попалась."
    th "Но всё прошло благополучно."
    stop music fadeout 3
    stop ambience fadeout 3
    scene black with dissolve
    window hide
    pause 1

    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_sl_day with dissolve
    window show
    th "Кибернетики вне подозрений."
    th "Думаю Оля и сама разберётся с этим."
    "Я переоделась и пошла на линейку."
    stop ambience fadeout 1
    window hide
    pause 1

    play ambience ambience_camp_center_day fadein 3
    scene bg ext_square_day with dissolve
    window show
    "На площади уже собрались пионеры и наша вожатая."
    show mt normal pioneer far with dissolve
    mt "Сегодня в 6 часов вечера отъезд. Обязательно соберите свои вещи и застелите кровати заранее."
    mt "Ужина не будет."
    mt "Если у кого-то ещё остались дела здесь, доделайте или отпрашивайтесь."
    mt "По уважительной причине я могу продлить."
    mt "Линейка окончена. Строй! Разойдись!"
    "На линейке я не заметила Семёна и Алису, хотя обычно они главные прогульщики."
    "Я не стала с этим ничего делать, а направилась к столовой."
    window hide

    scene bg ext_dining_hall_away_day with dissolve
    pause 2
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_day with dissolve
    window show
    "Как всегда, столики были забиты пионерами."
    "Я села в компанию Лены и Ульяны."
    show us smile pioneer with dissolve
    us "Присаживайся!"
    sl "Спасибо!"
    sl "Не знала, что вы с Леной уже помирились."
    us "А мы и не мирились. Зачем нам?"
    sl "Ты же часто проказничаешь над ней."
    show us calml pioneer with dspr
    us "Я же любя."
    sl "Мне так не казалось."
    show us dontlike pioneer with dspr
    us "Тебе много чего кажется и не кажется."
    sl "Не начинай. Ешь скорей."
    un "Приятного аппетита."
    sl "Приятного!"
    hide us with dspr
    "Ульяна быстро успокоилась и больше не докучала."
    "Остаток завтрака мы разговаривали с Ленкой о мелочах. {w}Однако, она не была настроена на продолжение разговора, поэтому отвечала кратко."
    window hide
    pause 1

    stop ambience fadeout 1
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    window show
    "Походив недолго по площади, я решила снова спросить Семёна."
    th "Не даёт мне покоя эта потеря!"
    window hide
    pause 1

    scene bg ext_house_of_mt_day with dissolve
    play sound sfx_knock_door2
    window show
    "Я постучалась."
    "Никто мне не открыл. Ни Оля, ни Семён."
    stop sound
    "Видимо, никого нет."
    window hide
    pause 1

    scene bg ext_houses_day with dissolve
    show mi normal pioneer with dissolve
    window show
    "Буквально все мои мысли сейчас были вокруг этой проклятой бутылки."
    th "Ну куда могла деться эта водка? Ведь в самом деле, кому из пионеров взбредёт в голову красть такое?"
    th "Да за такое его тут же выпнули бы из пионеров, а похититель как будто и вовсе этого не боится."
    "Прогуливаясь по лагерю, я встретила Мику."
    show mi smile pioneer with dspr
    mi "Привет! А я тебя как раз искала."
    sl "Зачем?"
    "Я улыбнулась."
    show mi normal pioneer with dspr
    mi "Я новую песню написала и у меня наконец-то получилось её исполнять одновременно с игрой на гитаре!"
    mi "Хочешь послушать?"
    th "Впринципе, у меня сейчас не было дел."
    show mi smile pioneer with dspr
    sl "Хорошо, пошли. В клуб же?"
    mi "Да."
    "Неожиданно кратко ответила моя знакомая, что я даже вначале не поверила."
    window hide
    pause 1

    stop ambience fadeout 1
    scene bg int_musclub_day with dissolve
    play ambience ambience_music_club_day fadein 3
    show mi normal pioneer with dissolve
    window show
    "Мику уселась на стул и начала настраивать гитару, перебирая струнами."
    "Затем она выдохнула и начала."
    stop ambience fadeout 2
    window hide
    scene cg d4_mi_guitar with dissolve
    play music music_list["miku_song_voice"] fadein 1
    pause 3
    window show
    "Песня оказалась на японском языке."
    "Что-то похожее я слышала на сцене, когда там сидела Лена."
    "Я интуитивно напевала звуки, похожие на те слова, которые пела Мику."
    "Наверное если бы меня послушали без музыки, получилась бы белиберда."
    "Но в этот момент я была больше сконцентрирована на тех чувствах, которые во мне будила эта мелодия."
    "Порой она казалась мне знакомой, словно из детства."
    "А песнь так и лилась потоком."
    th "Какая Мику всё-таки молодец! А какой талант сокрыт в этой юной японке!"
    "Мне стоило познакомиться с ней получше. Жаль, что смена так быстро подошла к концу."
    "Когда она закончила, я ощутила, будто вернулась из другого мира."
    stop music fadeout 2
    scene bg int_musclub_day with dissolve
    play ambience ambience_music_club_day fadein 3
    show mi normal pioneer with dissolve
    mi "Ну как?"
    sl "Очень красиво. Но мне казалось, что ты уже показывала это исполнение Лене."
    show mi smile pioneer with dissolve
    mi "Да, Славечка, ты права, но тогда я в середине партии сбилась и пришлось начинать заново. А теперь у меня получается без запинки. И играю хорошо, и слова не забываю."
    sl "Здорово!"
    show mi normal pioneer with dissolve
    mi "Ну, если ты хочешь, можешь идти, или остаться. Я тогда пойду ещё насочиняю или ещё могу тебе что-нибудь спеть, хочешь?"
    sl "Я бы с радостью, но у меня ещё дела остались."
    "Я попрощалась с ней и вышла из клуба."
    hide mi with dspr
    window hide
    stop ambience fadeout 2

    play sound sfx_close_door_1
    scene bg ext_clubs_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    window show
    th "Как же прекрасна музыка!"
    th "Существует много вещей, без которых человек не может существовать."
    th "И культурные потребности тоже сюда входят."
    th "Как же я завидую людям, которые умеют творить музыку!"
    window hide
    scene black with dissolve
    stop music fadeout 2
    pause 2

    window show
    play sound sfx_dinner_horn_processed
    "Пока я думала о вечном и прекрасном, начался обед."
    scene bg ext_square_day with dissolve
    "По пути я встретила Ульяну, которая шла со стороны ворот."
    play music music_list["i_want_to_play"] fadein 2
    show us normal sport at center with dissolve
    sl "Что делала?"
    us "Что?"
    sl "Ты же только что от ворот шла."
    show us laugh sport at center with dspr
    us "Ну да."
    "Она замялась."
    sl "Так что?"
    "В это время я заметила, что её ладони в чём-то были перепачканы."
    sl "Что опять учудила?"
    show us calml sport at center with dspr
    us "Ничего я не делала! Там за лагерем куст с ягодами растёт, вот я и набрала."
    sl "Ты же знаешь, что нельзя есть дикие плоды."
    us "Но ведь ничего не произошло."
    sl "Пока что. Иди пока руки мой и к медсестре."
    show us dontlike sport at center with dspr
    us "Ну хорошо."
    hide us with dspr
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    window show
    "Я отвела её к умывальникам, а затем сама пошла на обед."
    stop music fadeout 2
    window hide
    pause 1

    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 3
    window show
    "Столовая к этому времени немного опустела, и уже не была так набита битком как на завтраке. Похоже некоторые пионеры уже успели поесть."
    "Я заняла свободный столик и принялась за еду. {w}Но меня прервал Электроник, который подсел ко мне."
    show el normal pioneer at center with dissolve
    el "Славя, ты что-нибудь брала, когда утром заходила?"
    sl "Нет, зачем мне?"
    show el upset pioneer at center with dspr
    el "У нас молоток ещё пропал. Вроде больше ничего."
    show el laugh pioneer at center with dspr
    el "Ты ничего случаем не строишь частного на территории лагеря?"
    sl "Нет же, у меня своих хлопот полно. Мне ещё с Ульяной надо разобраться."
    show el normal pioneer at center with dspr
    el "Ладно."
    hide el with dspr
    "Он покинул меня."
    "А я принялась уплетать вкуснейший суп."
    window hide
    pause 1

    stop ambience fadeout 2
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    window show
    "Первым делом я решила зайти к Виоле поинтересоваться насчёт Ульяны."
    stop ambience fadeout 2
    window hide
    pause 1

    scene bg int_aidpost_day with dissolve
    play ambience ambience_medstation_inside_day fadein 3
    window show
    show cs normal pioneer at center
    cs "Привет Славя, Ульяна сказала, что ты её сюда направила."
    sl "Да, я. Она диких ягод объелась."
    cs "А ты видела где-то в округе дикие ягоды?"
    th "И правда. Сколько я бегаю, никогда не видела плодовых кустов."
    cs "Я её отправила обратно. Никакого отравления у неё нет."
    sl "Спасибо Виола."
    hide cs with dspr
    window hide
    stop ambience fadeout 2
    play sound sfx_close_door_1
    scene bg ext_aidpost_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    window show
    sl "Что же тогда Ульяна делала за воротами?.."
    show un normal pioneer at center with dissolve
    un "О чём думаешь?"
    "Неожиданно вывела меня из размышлений подошедшая Лена."
    sl "Привет, Лена, да вот, Ульяна где-то руки перепачкала за забором."
    un "Понятно. Ну, думаю ты узнаешь."
    hide un with dspr
    "Она ушла в сторону библиотеки. В руках у неё была книга."
    window hide
    pause 1

    scene bg ext_house_of_dv_day with dissolve
    window show
    "Я уже собиралась постучаться, как меня окликнула Ульяна."
    show us normal sport at center with dissolve
    play music music_list["timid_girl"] fadein 2
    us "Привет, а тебе зачем?"
    sl "Тебя найти хотела."
    show us smile sport at center with dissolve
    us "Вот она я, что тебе нужно?"
    sl "Скажи мне, где ты нашла эти ягоды."
    show us grin sport at center with dissolve
    us "А тебе зачем?"
    sl "Ольге Дмитриевне доложу, чтобы выкопали его."
    show us sad sport at center with dspr
    us "Нет никакого куста..."
    sl "Ульяна не надо врать!"
    show us calml sport at center with dspr
    us "Я и не вру! Хочешь, сама всё покажу."
    sl "Ну давай тогда, пошли."
    "Она взяла меня за руку и повела к воротам."
    hide us with dissolve
    window hide
    scene bg ext_no_bus with dissolve
    window show
    "Из-за большого куста она вытащила... {w}Деревянный домик!"
    sl "И что это?"
    show us upset sport at center with dissolve
    us "Я птенчика нашла и его маму. Им жить негде. Я решила домик построить."
    th "Благородно, хвалю тебя!"
    sl "Подожди, а зачем ты делаешь это в тайне?"
    us "Я попросила у кибернетиков проволоку, но они мне её не дали. Поэтому я взяла её сама."
    us "А ещё инструменты и доски."
    th "Так вот куда всё пропало."
    sl "Ульяна! Ну так нельзя. Это же воровство социалистической собственности!"
    show us shy2 sport at center with dspr
    us "Но мне действительно нужно было."
    "Она так посмотрела на меня, что мне стало даже жалко эту маленькую девочку, которая пытается сделать что-то хорошее."
    sl "Ну.. Хорошо, давай я тогда помогу тебе?"
    show us surp1 sport at center with dspr
    us "Спасибо большое!"
    "Она обняла меня."
    hide us with dspr
    "Мы принялись за работу."
    stop music fadeout 2
    window hide
    pause 2

    scene bg ext_camp_entrance_day with dissolve
    window show
    "Это дело заняло несколько часов."
    th "Боюсь, что Оля уже обыскалась меня."
    "Когда всё было готово, Ульяна решила прикрепить к ней ленточки с разноцветными бантиками."
    show us normal sport at center with dspr
    us "Так красивее."
    sl "Кстати, Ульяна. А в чём же ты перепачкалась?"
    us "А, да это я краски хотела взять, но потом решила что покрасить времени не будет, вот и перепачкалась."
    hide us with dissolve
    "Мы понесли скворечник, идя параллельно забору, с внешней его стороны."
    window hide
    scene bg ext_polyana_day with dissolve
    window show
    "Ульяна захотела повесить его подальше от лагеря, чтобы пионеры не вспугнули птичек."
    show us normal sport at center with dspr
    us "Думаю, это всё. Сейчас я принесу их из домика."
    sl "Кстати, а где Алиса? Я её сегодня на завтраке не видела."
    us "Не знаю... "
    show us surp2 sport at center with dspr
    play music music_list["always_ready"] fadein 1
    extend "Ой! Скоро же автобус!"
    sl "Точно! Как же я могла забыть!"
    hide us with dissolve
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    window show
    "Мы скорее побежали к лагерю и разбежались на площади."
    window hide
    scene bg int_house_of_sl_day with dissolve
    play ambience ambience_int_cabin_day fadein 3
    window show
    "Я начала собираться."
    "Вынула подушку из наволочки. {w}Свернула простыню и положила на матрас."
    "Затем стала сворачивать матрас."
    stop music fadeout 3
    extend " Но моё внимание привлёкло что-то застрявшее в панцерной сетке."
    "Это был клочок бумаги. Немного порваный. {w}Я решила достать его."
    play music music_list["mystery_girl_v2"] fadein 2
  #картинка записки
    "{i}Надеюсь, Вам понравилась эта смена в Совёнке!{/i}"
    "{i}Обязательно сохраните все впечатления о ней, ведь другой такой же больше никогда не будет...{/i}"
    "Оставил(а) записку некий(ая) «{b}С{/b}»"
  #убрать картинку записки
    th "Не могу не отметить, что почерк красивый, однако вероятнее всего писалось это в спешке."
    th "Надо будет и мне такой же памятник следующей смене оставить."
    th "Маленький листок никому не повредит. Зато какие приятные эмоции может доставить следующей смене."
    "Убрав записку в карман, я продолжила собираться."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause 1
    scene bg int_house_of_sl_day with dissolve
    play ambience ambience_int_cabin_day fadein 2
    window show
    "Большинство моих вещей так и продолжали лежать в сумке, поэтому я лишь собрала то немногое, что успела вынуть."
    "Все это время записка никак не выходила из моей головы."
    "Я решила написать свою записку для будущей смены."
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause 2
    scene bg int_house_of_sl_day with dissolve
    play ambience ambience_int_cabin_day fadein 2
    window show
    "Почему-то было очень сложно что-нибудь придумать, поэтому я решила просто оставить эту же записку."
    stop music fadeout 3
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause 1
    scene bg int_house_of_sl_day with dissolve
    play ambience ambience_int_cabin_day fadein 3
    window show
    "Я в последний раз посмотрела на свой домик и мысленно попрощалась с ним."
    th "Ты нёс мне верную службу, я не забуду тебя {w}домик!"
    window hide
    stop ambience fadeout 2
    scene bg ext_bus with dissolve
    play ambience ambience_camp_center_day fadein 3
    window show
    "Пришлось немножко постоять."
    sl "Лен, скажи, тебе понравилось?"
    show un normal pioneer at center with dissolve
    un "Да, не то что я себе представляла, но тоже неплохо."
    show un smile pioneer at center with dissolve
    "Она улыбнулась."
    "Я встала рядом с ней."
    hide un with dissolve
    "Наконец, Ольга Дмитриевна пришла вместе с Ульяной."
    show mt normal pioneer at cleft
    show us normal pioneer at cright
    with dissolve
    sl "А где же Алиса и Семён?"
    mt "Ульяна сказала, что Алисе стало плохо и Семён останется с ней. Их заберут следующим автобусом."
    hide mt
    hide us
    with dissolve
    stop ambience fadeout 2
    window hide
    scene cg d7_pioneers_leaving with dissolve
    play music music_list["memories"] fadein 2
    window show
    mt "Все собрались?"
    "Начала Ольга Дмитриевна."
    mt "Сегодня вы покидаете наш лагерь, и, на прощание, мне хотелось бы вам кое-что сказать."
    "Она заметно нервничала и никак не могла подобрать нужные слова."
    mt "Надеюсь, что время, проведённое здесь, вам запомнится на всю жизнь, что у вас останутся только приятные воспоминания о «Совёнке»."
    mt "Также я надеюсь, что здесь вы стали чуточку лучше, смогли чему-то научиться, познакомились с новыми друзьями… {w} В общем, возвращайтесь в следующем году!"
    "Вожатая отвернулась."
    "Да, в такой момент было трудно сдержать слёзы."
    th "Я буду очень скучать." 
    stop music fadeout 1
    window hide
    scene bg int_bus_people_day with dissolve
    play ambience ambience_medium_crowd_outdoors fadein 3
    window show
    "Мы взяли свои сумки и заносили их в салон, кладя их на колени или под кресла."
    "Я заняла место рядом с Олей."
    mt "Поездка займёт несколько часов."
    "Сказала она мне."
    "Я молча уставилась в окно."
    stop ambience fadeout 2
    window hide
    scene bg int_bus_people_night with dissolve
    play sound_loop sfx_bus_interior_moving fadein 3 loop
    window show
    "Проехав уже достаточное расстояние, автобус включил фары. В свои права вступала ночь."
    "И меня начало клонить в сон..."
    stop sound_loop fadeout 2
    show blink
    "..."

  #Рут Лены
  elif sl_m_end_un:
    scene black
    "Утро этого дня явно не задалось."
    "Вначале я проснулась не выспавшейся."
    "А во вторых я проспала..."
    play music music_list["awakening_power"] fadein 1
    scene bg int_house_of_sl_day
    with hpunch
    extend " ЛИНЕЙКУ!!!"
    th "Этого не может быть! Время уже без десяти одиннадцать, а я только проснулась!"
    "Я мигом собрала все силы в кулак, вскочила с постели и надела форму."
    scene bg ext_house_of_sl_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    "На ходу я застёгивала нижние пуговицы и завязывала галстук."
    window hide
    scene bg ext_house_of_sl_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    pause 1.5
    scene bg ext_square_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    window show
    "Когда я добежала, площадь была {w}конечно же пуста."
    "С чувством вины я направилась в столовую."
    window hide
    pause 1.5
    scene bg ext_dining_hall_away_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    pause 1.5
    scene bg ext_dining_hall_near_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    stop music fadeout 2
    scene bg int_dining_hall_people_day
    play ambience ambience_dining_hall_full fadein 2
    window show
    "Столовая всё ещё была заполнена пионерами."
    "Я встала в очередь за своей порцией, издалека заприметив свободное место."
    "Получив порцию и дойдя до него, ко мне подсела Женя."
    show mz normal glasses pioneer with dspr
    mz "Что-то ты сегодня поздно. Ольга Дмитриевна была недовольна."
    sl "Странно что она не подняла весь лагерь на уши в моих поисках, я ведь никогда не пропускаю линейки."
    mz "Она всё списала на то, что у тебя была какая-то уважительная причина."
    sl "Надо будет извиниться перед ней."
    show mz bukal glasses pioneer with dspr
    mz "Да не стоит, лишний раз ей напоминать, лишняя болтовня. Разве тебе не хочется провести последний день с пользой или что-то вроде того?"
    mz "Ты хочешь чтобы он тебе запомнился ссорой с вожатой?"
    sl "Нет, конечно."
    show mz normal glasses pioneer with dspr
    mz "Так что просто забудь. {w}Ладно, я пойду в библиотеку."
    "Я решила не напоминать ей про случай с Электроником."
    hide mz with dspr
    "А просто доела свою порцию и вышла из-за стола."
    stop ambience fadeout 2
    pause 2

    scene bg ext_house_of_sl_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "Я решила не терять времени зря, утренняя «пробежка» быстро привела мысли в порядок."
    "Поэтому, я решила разобраться в наметившемся вопросе. {w}Касательно колонок, которые Шурик собирался разобрать."
    window hide
    scene bg ext_square_day with dissolve
    pause 1
    scene bg ext_clubs_day with dissolve
    window show
    "Я прошла площадь и подошла к клубам."
    show el sad pioneer with dissolve
    "На ступеньках сидел Электроник с поникшей головой."
    sl "А почему ты не со своим другом, и кстати, где он?"
    "Он указал в сторону дверей здания."
    stop ambience fadeout 1
    play music music_list["you_won_t_let_me_down"] fadein 1
    el "Мы немного... поссорились."
    th "Вот это да! Друзья не разлей вода поссорились!"
    el "Лучше не спрашивай почему. Всё уляжется само собой."
    th "А вот мне бы как раз прямо с ним и переговорить тет-а-тет."
    "Я молча направилась к дверям, как лохматый блондин меня остановил."
    show el surprise pioneer with dspr
    el "Стой, ты это куда?"
    sl "Мне надо с ним поговорить."
    show el upset pioneer with dspr
    el "Он сейчас явно не в духе, не надо сейчас его беспокоить."
    sl "Чего ты меня останавливаешь?"
    "Грозно осадила я его, но Электроник не сдавался."
    show el serious pioneer with dspr
    el "Прошу. {w}Сейчас правда не время для этого."
    "Я вздохнула, и, наконец, пошла на уступку."
    sl "Ладно."
    sl "Но мне всё равно с ним нужно будет серьёзно поговорить."
    hide el with dspr
    "Он с благодарностью посмотрел на меня, после чего я отошла от клубов и направилась в противоположную сторону."
    window hide
    stop music fadeout 3
    scene black with dissolve
    pause 1
    window show
    "Ноги привели меня к реке."
    scene bg ext_beach_day with dissolve
    play ambience ambience_boat_station_day fadein 3
    "На пляже было людно."
    th "Я поступила очень нерационально, не надев купальник под низ. Правда идея искупаться пришла ко мне только сейчас."
    "Поэтому, раз уж сегодня был последний день, я решила сходить к тому самому озеру, ведь там никогда никого не бывает."
    window hide
    stop ambience fadeout 1
    play ambience ambience_forest_day fadein 2
    scene ext_path_day with dissolve
    window show
    "Но, как только я начала заходить глубже в лес{w}"
    play sound sfx_dinner_horn_processed
    extend ", неожиданно на весь лагерь был объявлен обед."
    th "Делать нечего. А жаль, так сейчас хотелось немного освежиться."
    "Но прежде чем идти в сотолую, думаю стоит попытаться выловить Шурика"
    stop sound fadeout 2
    "Зайду к кибернетикам, всеравно по пути"
    scene ext_clubs_day with dissolve
    "Но судя по всему, он уже ушёл в столовую."
    window hide
    stop ambience fadeout 1
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 2
    window show
    "Обед, ровно как и завтрак, не представлял из себя ничего необычного."
    "Уже после того как я поела, я ещё некоторое время сидела, рассматривая заходящих у уходящих пионеров."
    "Я встала из-за стола, но нечаянно задела стакан с почти выпитым компотом."
    "Немного пролилось и на одежду."
    "Я быстро сбегала за тряпочкой, чтобы протереть стол, и побежала в сторону умывальников."
    stop ambience fadeout 2
    scene black with dspr
    "..."
    scene bg ext_washstand_day with dissolve
    play ambience ambience_camp_center_day fadein 2
    "Добежав до умывальников, я поняла что мне бы стоило сначала переодеться во что-то сухое."
    "Хоть рядом и не было никого..."
    "Но всё что могло мне подойти было сейчас в моём домике."
    stop ambience fadeout 2
    scene black with dspr
    "Поэтому мне пришлось вернуться к себе."
    scene bg ext_washstand_day with dissolve
    play ambience ambience_camp_center_day fadein 2
    "Переодевшись, я вернулась к умывальникам."
    "Я положила спортивную форму под воду и стала её замачивать."
    "Кое-как оттерев пятно руками, я направилась в домик."
    stop ambience fadeout 2
    scene bg int_house_of_sl_day with dissolve
    play ambience ambience_int_cabin_day fadein 3
    "Нужно было куда-то повесить форму, но верёвок не было."
    th "Благо капать перестало."
    "Поэтому я перекинула через форточку и повесила сушиться там. Тем более, что светило солнце."
    "Я взглянула на часы. {w}Времени было около 2 часов дня."
    "Я решила собраться заранее."
    "Вынула подушку из наволочки. {w}Свернула простыню и положила на матрас."
    "Затем стала сворачивать матрас. {w}Но моё внимание привлёк клочок бумаги застрявший в панцерной сетке и немного порванный."
    play music music_list["mystery_girl_v2"] fadein 1
    "Я решила достать его."
    play sound sfx_paper_bag
    show note at truecenter with dspr
    "{i}Надеюсь, Вам понравилась эта смена в Совёнке!{/i}"
    "{i}Обязательно сохраните все впечатления о ней, ведь другой такой же больше никогда не будет...{/i}"
    "Оставил(а) записку некий(ая) «{b}С{/b}»"
    hide note
    th "Не могу не отметить, что почерк красивый, однако вероятнее всего писалось это в спешке."
    th "Надо будет и мне такой же памятник следующей смене оставить."
    th "И я не считаю это вандализмом."
    "Убрав записку в карман, я продолжила собираться."
    window hide
    stop music fadeout 1.5
    stop ambience fadeout 1
    scene black with dspr
    pause 1
    scene bg int_house_of_sl_day with dissolve
    play ambience ambience_int_cabin_day fadein 2
    window show
    "Большинство моих вещей так и продолжали лежать в сумке, поэтому я лишь собрала то немногое, что успела вынуть."
    th "Я же решила в последний день отдохнуть. Значит этим я сегодня и буду заниматься."
    "Я надела под низ купальник и вышла с двумя полотенцами."
    stop ambience fadeout 1
    scene bg ext_beach_day with dissolve
    play ambience ambience_boat_station_day fadein 3
    "К тому моменту, как я подошла, многие уже разошлись и было не так многолюдно."
    show un normal pioneer far with dissolve
    "Вдали показалась и Лена, которой вчера не было весь день."
    sl "Привет!"
    show un normal pioneer with dspr
    un "Привет."
    sl "Тебя Семён вчера разыскался, весь день спрашивал, и Ульяне тоже стало интересно."
    un "Да?"
    show un shy pioneer with dspr
    "Она засмущалась."
    sl "А ты знаешь почему он тебя искал?"
    un "Н-наверное..."
    th "Мне кажется разговор в лесу как-то связан с этим."
    sl "Ладно."
    "Я улыбнулась."
    sl "Лен, мы ведь сегодня уже уезжаем..."
    show un normal pioneer with dspr
    un "И?"
    sl "Тебе понравилась эта смена?"
    un "Да."
    th "Видимо она уже не настроена на продолжение диалога."
    sl "Ладно, я пойду тогда искупнусь."
    show un smile pioneer with dspr
    "Она улыбнулась мне напоследок."
    hide un with dspr
    "Я расстелила большое полотенце на песке и, раздевшись, зашла в воду."
    th "Тёпленькая!"
    "..."
    window hide
    stop ambience fadeout 1
    scene black with dspr
    pause 1
    scene bg ext_beach_day with dissolve
    play ambience ambience_boat_station_day fadein 2
    window show
    "Не знаю сколько времени прошло, но я успела замёрзнуть, пока купалась и играла с малышами, которые были здесь."
    "Я вышла из воды и присела на полотенце."
    "Солнце уже давно было не в зените."
    th "Кстати, а где же Шурик?"
    "Отдалось у меня в голове, и я почувствовала чей-то взгляд."
    "Обернувшись, я увидела, как Шурик уже направился в обратную сторону{w}, словно пытался сбежать!"
    stop ambience fadeout 3
    play music music_list["revenga"] fadein 2
    "Я даже не успела одеться, лишь просунула ноги в ботиночки."
    "И стремительно направилась в его сторону, пытаясь догнать."
    "Через листву я отчётливо видела его светлую шевелюру, и то, что он направлялся в сторону лодочной станции."
    "Я решила сократить путь и прорываться прямо через кусты."
    play sound sfx_hiding_in_bush
    "Я стралась пролезть как можно быстрее, поэтому получалось у меня это очень шумно."
    window hide
    scene bg ext_boathouse_day with dissolve
    show sh normal pioneer:
        xpos 1.1 yalign 1.0 xanchor 0.5 yanchor 1.0
    show sh normal pioneer:
        linear 0.3 xpos 0.5
    pause 0.5
    hide sh
    show sh scared pioneer at center
    with hpunch
    pause 0.2
    play sound sfx_fall_grass
    show sh scared pioneer:
        linear 0.3 ypos 2.0
    pause 0.4
    hide sh
    window show
    "Но когда я наконец раздвинула листву и вышла к лодочной станции, то внезапно врезалась в Шурика."
    show sh scared pioneer close with dissolve
    sh "Славя! {w}А я {w}Как раз искал тебя."
    "Он не сразу сориентировался, поэтому я крепко схватила его за локоть."
    sl "Конечно, найти он меня пытался!"
    sl "Давай говори, что вы сделали с колонками?"
    show sh surprise pioneer close with dspr
    sh "Да ничего мы не делали."
    sl "Так я и поверила, что же ты тогда сразу запаниковал, когда вдруг проболтался"
    stop music fadeout 2
    show sh normal pioneer with dspr
    "Он поднялся и отошёл от меня на шаг, он дал понять, что никуда не сбегает и я отпустила его."
    play music music_list["meet_me_there"] fadein 4
    show sh upset pioneer with dspr
    sh "Я просто все транзисторы, которые нашёл в старом лагере, растерял."
    sh "И мне стало так стыдно, что я от отчаяния предложил Электронику колонки разобрать."
    sh "Ну он меня слишком буквально понял."
    "Я недоумённо посмотрела на него."
    show sh serious pioneer with dspr
    sh "Даже не подумал о последствиях. Ну я и накричал на него за это."
    sh "Мол, нам потом влетит. Так и случилось в итоге."
    sl "Как тебе вообще в голову пришло такое ему предложить?"
    sh "Ну а что? {w}Всё равно последний день смены, никто про эти колонки и не вспомнит. Хоть я и понимал, что если кто заметит, понятно будет кто виноват."
    show sh normal pioneer with dspr
    "Он вздохнул."
    sh "Ладно, признаю, что был не прав."
    sl "Мне придётся доложить об этом Ольге Дмитриевне."
    "Услышав это, кибернетика словно током пробило."
    show sh scared pioneer with dspr
    sh "Н-не надо Ольге Дмитриевне."
    sl "Но вы же испортили колонки."
    sh "Ничего мы не портили, достали из них просто компоненты и всё! Сейчас обратно поставим."
    sl "Ну, если обратно поставите.."
    stop music fadeout 2
    "Я грозно посмотрела на него, давая понять, что я обязательно проверю."
    sl "Тогда не буду ничего говорить, и впредь больше таким не занимайтесь."
    th "Всё равно бы Ольга Дмитриевна никак сейчас не наказала его."
    show sh smile pioneer with dspr
    sh "Спасибо тебе большое, Славя!"
    "Он посмотрел на меня взглядом, полным благодарности {w}и как-будто даже.. засмущался?"
    sl "Мне ещё переодеться надо."
    "Сказала я, нарушив тишину."
    sl "Потом приду проверю у сцены."
    th "Конечно же, ничего я проверять и не думала, просто бы не успела."
    sh "Обязательно! {w}И.. Спасибо, Славя."
    stop music fadeout 3
    play ambience ambience_boat_station_day fadein 2
    scene black with dspr
    "Живо ответил мне Саша и я вернулась на пляж, чтобы одеться."
    scene bg ext_beach_day with dissolve
    "Времени уже прошло достаточно, поэтому я оделась и направилась в домик."
    stop ambience fadeout 2
    scene bg int_house_of_sl_day with dissolve
    play ambience ambience_int_cabin_day fadein 2
    "Зайдя обратно, я сняла купальник и отжала его уже снаружи."
    "До автобуса оставалось примерно полчаса, я решила написать соответствующую записку для будущей смены."
    "Почему то было очень сложно что-нибудь придумать, поэтому я решила просто написать похожую записку."
    "..."
    "Когда было готово, я перечитала. {w}И обнаружила что шрифты были очень похожи."
    "Даже не так... {w}Они были идентичными!"
    th "Я что, настолько сильно перекопировала, что даже шрифт похожий? Да нет, бред какой-то!"
    th "Видимо просто совпадение."
    "Я сложила бумажку и подложила её под матрас."
    th "Её обязательно найдут!"
    "..."
    stop ambience fadeout 2
    scene bg ext_bus with dissolve
    play ambience ambience_camp_center_day fadein 2
    "Собрав вещи, я пришла на остановку, там уже стояла Оля и остальные пионеры."
    show mt normal pioneer far with dissolve
    mt "Я сейчас схожу за остальными, не разбегайтесь!"
    hide mt with dspr
    "И она зашла за ворота."
    "Пришлось немножко постоять."
    show dv sad pioneer with dissolve
    sl "Алиса, чего такая грустная?"
    dv "Да так, ничего..."
    sl "Тоже грустно уезжать?"
    dv "Ну и это тоже, в меньшей степени."
    hide dv with dspr
    "Мимо нас пробежала Ульяна."
    sl "Стоять! Куда бежим? Скоро Ольга Дмитриевна придёт."
    us "Да никуда я не бегу! Делать просто нечего пока ждём опаздывающих."
    show mt normal pioneer with dissolve
    "Наконец Ольга Дмитриевна пришла {w}одна."
    pi "А где же «остальные»?"
    mt "У Лены остались... дела здесь. Семён ей поможет."
    mt "Завтра за ними приедет автобус."
    mt "Остальные едут сейчас."
    scene cg d7_pioneers_leaving with dissolve
    play music music_list["memories"]
    mt "Все собрались?"
    "Начала Ольга Дмитриевна."
    mt "Сегодня вы покидаете наш лагерь, и на прощание мне хотелось бы вам кое-что сказать."
    "Она заметно нервничала и никак не могла подобрать нужные слова."
    mt "Надеюсь, что время, проведённое здесь, вам запомнится на всю жизнь, что у вас останутся только приятные воспоминания о «Совёнке»."
    mt "Также я надеюсь, что здесь вы стали чуточку лучше, смогли чему-то научиться, познакомились с новыми друзьями… {w} В общем, возвращайтесь в следующем году!"
    "Вожатая отвернулась."
    "Да, в такой момент было трудно сдержать слёзы."
    th "Я буду очень скучать." 
    stop music fadeout 1
    window hide
    scene bg int_bus_people_day with dissolve
    play ambience ambience_medium_crowd_outdoors fadein 3
    window show
    "Мы взяли свои сумки и заносили их в салон, кладя их на колени или под кресла."
    "Я заняла место рядом с Олей."
    mt "Поездка займёт несколько часов."
    "Сказала она мне."
    "Я молча уставилась в окно."
    stop ambience fadeout 2
    window hide
    scene bg int_bus_people_night with dissolve
    play sound_loop sfx_bus_interior_moving fadein 3 loop
    window show
    "Проехав уже достаточное расстояние, автобус включил фары. В свои права вступала ночь."
    "И меня начало клонить в сон..."
    stop sound_loop fadeout 2
    show blink
    "..."

  #рут Ульяны
  #Если выбрали "Ульяна"
  elif sl_m_end_us:
    play ambience ambience_int_cabin_day fadein 5
    scene bg int_house_of_sl_day
    show unblink
    "Я проснулась как всегда вовремя."
    "Утро было солнечным и за окном тихо пели птички."
    "Я собралась на пробежку, пока моя соседка спит."
    stop ambience fadeout 1
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_house_of_sl_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    with dissolve
    "Я немного постояла на месте и размялась перед пробежкой."
    "День обещал быть насыщенным."
    window hide
    scene bg ext_path_day:
        zoom 1.1
        yalign 0.01
        block:
            linear 0.2 pos (0,5)
            linear 0.2 pos (0,0)
        repeat
    with dissolve
    window show
    "Я пробежалась вдоль домиков и завернула в лес."
    "Минут десять я просто бежала вперёд, пока не оказалась достаточно глубоко в лесу, где ничто не могло нарушить природную тишину."
    "Бегая по лесу, я свернула на неизвестную мне тропинку."
    th "Только бы не заблудиться!"
    scene bg ext_polyana_day with dissolve
    "Я бежала дальше и вышла на какую-то неизвестную мне полянку."
    th "Странно, я почти везде в этом лесу была."
    "Особенно моё внимание привлёк небольшой комочек, валяющийся на земле."
    "Подойдя поближе и взяв его на руки, я поняла что это птенец какой-то птицы."
    th "Бедняжка, вывалился из гнезда."
    scene cg d7_feeding_trough with dissolve
    "Я подняла голову повыше и заметила неприметный скворечник с разноцветными верёвочками."
    "У него отломилось дно."
    scene bg ext_polyana_day with dissolve
    th "Я обязательно спасу тебя!"
    window hide
    scene ext_houses_day with dissolve
    "Ещё немного поплутав по лесу, я наконец вышла к лагерю."
    "Быстрым шагом я направилась к себе."
    stop ambience fadeout 1
    scene bg int_house_of_sl_day with dissolve
    play ambience ambience_int_cabin_day fadein 2
    "Время было ещё раннее и линейка не скоро."
    "Я положила птенца в небольшую коробочку и оставила в шкафу."
    stop ambience fadeout 1
    scene bg ext_clubs_day with dissolve
    play ambience ambience_camp_center_day fadein 2
    "Я решила зайти к кибернетикам поинтересоваться насчёт изоленты или чего-нибудь скрепляющего."
    scene bg ext_square_day with dissolve
    "На линейку я отправилась вместе с Женей."
    "Ольга Дмитриевна как раз собирала ребят."
    show mt normal pioneer far with dissolve
    mt "Сегодня в 6 часов вечера отъезд. Обязательно соберите свои вещи и застелите кровати заранее."
    mt "Ужина не будет."
    mt "Если у кого-то ещё остались дела здесь, доделайте или отпрашивайтесь."
    mt "По уважительной причине я могу продлить."
    mt "Линейка окончена. Строй! Разойдись!"
  #фон напротив клубов
    "Я сразу же направилась к кибернетикам, появилась у меня кое-какая идея."
    "Дверь оказалась открытой."
  #фон внутри клуба
    "Оба товарища были тут."
    sl "Доброе утро, ребята!"
    el "Доброе!"
    sh "И тебе!"
    sl "Я вот спросить хотела - а у вас случайно клейкой ленты нет?"
    sh "Была где-то..."
    "Задумчиво ответил Шурик."
    el "А посмотри в кладовке!"
  #звук неоткрывающейся двери посреди фразы
    "Я подошла к двери и {w}не смогла её открыть."
    sl "У вас тут заперто."
    el "Не может такого быть - мы никогда эту комнату не закрываем!"
    sh "Дай-ка я попробую."
    "Шурик дёрнул ручку, но дверь не поддалась."
    sh "Похоже, заело. Помоги-ка!"
    "Я отошла в сторону и Электроник тоже взялся за ручку."
    th "Тянут-потянут вытащить не могут."
  #эффект удара
    "Они дёрнули ещё раз и наконец дверь распахнулась."
  #тёмный фон
    "Там было темно, я нащупала выключатель и включила свет."
  #белая вспышка
  #фон внутри кладовки со светом
  #спрайты Шурика и Электроника по бокам, а по центру Семён, позади которого Ульяна
    el "Эээ... Доброе утро!"
    us "Доброе..."
    sh "А что вы тут делаете?"
    me "Ну, вообще... {w}Если честно, мы фильм смотрели. Ульянка принесла кассету, а ведь у вас тут магнитофон."
    el "И что за фильм?"
    me "Обычный самый фильм! Боевик! Новинка!"
  #Один из электроников отодвигается в сторону, чтобы Ульяну(которая вылезает из-за спрайта Семёна) было видно
    "Ульяна вышла из-за его спины и показала кассету Шурику."
    me "Если вы думаете... Да мы ничего такого!"
    "Он на мгновение смолк."
    me "Это всё моя вина..."
  #пропадает спрайт Шурика
    sl "Вас никто ни в чём не обвиняет..."
    me "Вот хоть один разумный человек из здесь присутствующих!"
    sl "Пока что..."
    "Добавила я шёпотом."
    me "Что?"
    us "На самом деле всё так и было, как он говорит."
    us "Мы просто смотрели кино, а потом захотели спать... Поздно ведь уже было..."
    el "Мы ничего такого и не думали... {w}Глупая ситуация, с кем не бывает..."
    sl "Думаю Ольга Дмитриевна во всём разберётся."
    me "Э, нет! Подожди-ка! Зачем до вожатой доводить?!"
    sl "А как же ещё?"
    me "Ну, ты же видишь, что мы говорим правду!"
    sl "Это не мне судить..."
    me "А кому тогда, чёрт возьми?! Ты сама всё видела своими глазами!"
    sl "Вожатая разберётся."
    "Разговор был окончен."
  #фон внутри клуба
    me "Да подожди ты!"
  #близкий спрайт злого Семёна 
    "Семён встал между мной и дверью, не давая мне пройти."
    me "Послушай!"
    sl "Это не моё дело..."
    "Я смотрела в сторону от него, давая понять что игнорирую его."
    sl "Просто я должна..."
    me "Кому ты должна-то? Зачем всё это нужно?"
    sl "Потому что..."
    "Я осеклась, ведь я и сама не знала почему ОБЯЗАНА."
    me "Вот и не стоит никуда ходить и ничего никому рассказывать!"
    sl "Нет..."
    "Я подняла голову и посмотрела ему в глаза."
    sl "Извини, Семён."
    us "Да оставь ты её, пусть идёт."
  #спрайт Семёна резко пролетает влево
    "Семён отвлёкся и я с лёгкостью проскочила мимо него."
  #фон напротив клубов
    me "Да подожди ты!"
    "Услышала я из-за двери."
    "Я твёрдо намеревалась дойти до вожатой."
  #фон площадь
  #фон домики
  #фон напротив домика ОД
    "Уже стоя на крыльце меня одолевало какое-то неприятное чувство."
    "Какое-то чувство вины."
    "Я постучалась в дверь."
    mt "Войдите!"
  #фон внутри домика ОД
    mt "Славя? Зачем пожаловала?"
    sl "Оля... Там сейчас в клубах произошёл инцидент."
    mt "Какой?"
    "Спокойно спросила она."
    sl "В общем, прошлой ночью Семён и Ульяна пробрались в клубы и заперлись в кладовке."
    sl "Ульяна принесла кассету. Ночь провели там же."
    sl "А на утро мальчики их там нашли. {w}Думаю ничего страшного, я видела что там ничего серьёзного не произошло."
    mt "Спасибо что сказала, можешь идти."
  #фон напротив домика ОД
  #фон напротив столовой
  #фон внутри столовой
    "Семён сидел за одним столиком с Ульяной, поэтому я не решилась к ним подсесть."
    "Вместо этого я села рядом с кибернетиками."
    el "Рассказала?"
    sl "Да."
    sh "Что ответила?"
    sl "Не понятно ещё, будет разбираться."
    sl "Я постаралась объяснить, что там ничего серьёзного."
    sh "Понятно."
    "Мы принялись за еду."
    el "Ты, кажется, за клейкой лентой заходила?"
    sl "Да."
    el "Хорошо, мы её дадим."
    "После всего произошедшего, кусок в горло не лез, поэтому я так и оставила свой поднос, даже не притронувшись к еде."
  #фон напротив столовой
    "Мы вместе вышли из столовой."
  #фон напротив клубов
  #фон внутри клуба
    "И так же вместе дошли до клубов."
    sh "Вот."
    "Он передал мне изоленту."
    sh "Можешь не возвращать даже, не обеднеем."
    sl "Спасибо!"
  #фон внутри домика Слави
    "Я вынула птенца из коробки, в которой он просидел всё время и забрала птенчика с собой."
    th "Надо было его накормить. Но я даже не знаю чем."
    "Поэтому я отправилась в библиотеку."
  #фон площадь
    "Но по пути в библиотеку меня встретила Оля."
    mt "Славя, помоги ребятам из младшего отряда на пристани убраться, а то у меня ещё дел много."
    sl "Хорошо, пару минут буквально и я буду."
    mt "Это желательно прямо сейчас сделать."
    "Повелительным тоном обратилась ко мне вожатая."
    "У меня не было иного выбора."
    sl "Да, Оля."
  #фон пристань
    th "Бедный птенчик ещё поголодает."
    th "Надо будет поскорее убраться."
    "Я помогала ребятам собирать и указывала куда отнести, работа продвигалась быстро."
    me "Убираетесь?"
    "Неожиданно пришёл Семён."
    sl "Да."
    "Сказала я не оборачиваясь."
    me "Слушай, я тут это..."
    sl "Хотел поговорить насчёт Ульянки?"
    me "Ну, да..."
    sl "И что же ты хотел сказать?"
    me "Ну, Ульянку наказали. {w}Может быть, она даже не уедет вместе со всеми."
    sl "Неудивительно."
    me "Просто я хотел тебе объяснить, что ничего там такого не было."
    sl "Я не знаю, честно. Просто я должна была рассказать."
    me "Рассказала, и кому от этого лучше стало?"
    "Произнёс он слишком угрюмо."
    sl "Я не уверена, конечно, что это было правильно..."
    me "Ну, что было, того уже не вернёшь... {w}Как думаешь, что сделать, чтобы Ульянку выпустили из-род домашнего ареста?"
    sl "Ты так за неё переживаешь."
    "Я посмотрела на него и улыбнулась."
    "Семён смутился."
    me "Не за неё... За справедливость!"
    sl "Ты же знаешь нашу вожатую."
    me "Знаю, это точно."
    sl "Подожди. Со временем она отойдёт."
    me "Да, ты права."
    "Всё это время я продолжала подметать."
    "Похоже, Семён хотел ещё что-то сказать, но молчал."
    "Постояв так ещё немного, он попрощался и ушёл."
    me "Ладно, я пойду."
    sl "Увидимся."
    "..."
  #тёмный фон и снова фон пристань
    "Мы закончили уборку на пристани."
    "Однако, вскоре прозвучал горн."
    th "О нет, уже обед! Я уже не успею в библиотеку." 
    th "Женю встречу в столовой, но что же делать с птенцом? Я же могу его так просто бросить..." 
    th "Но и в столовую с ним вот так не пойдёшь. Может положить его в карман? Или всё же отнести в укромное местечко?"
    
  #Выбор без очков(Отнести птенца домой/Положить в карман рубашки)

  #Если выбрали "Отнести птенца домой"
  #фон напротив столовой(веранда)
    th "Надеюсь вторая пробежка за день стоила того и в столовой будет вкусный обед."
  #фон внутри столовой
    "Сегодня на обед давали котлеты с пюрешкой из картофеля."
    th "Неплохо."
    "Я подсела к Жене, с ней всё равно практически никто не садился."
    "Я рассказала ей про мою находку."
    mz "Ты где птенца откопала?"
    sl "Не откопала, он сам из скворечника выпал."
    mz "Какого скворечника?"
    sl "Ну, в лесу нашла."
    mz "И что ты собираешься дальше делать?"
    sl "Починю скворечник."
    mz "Ну хорошо, а я тебе зачем в этом деле?"
    sl "Ты знаешь, чем его накормить?"
    mz "А ты всё это время его голодным держала?"
    sl "Ну, инцидент произошёл, я и забыла."
    mz "Ладно, посмотрим что в библиотеке есть. Приятного аппетита."
    sl "Тебе тоже!"
  #фон напротив библиотеки
    "Я попрощалась с Женей и побежала к домику."
  #фон напротив домика Слави
    "У меня было какое-то плохое предчувствие."
  #фон внутри домика Слави
    "Я зашла внутрь."
    "Открыв дверь, я сразу взглянула на свою кровать."
    th "Этого быть не может. Там нет птенца!"
    th "Где же я могла оставить его? Возможно я положила его где-то в другом месте?"
  #тёмный фон и снова фон внутри домика Слави
  #посреди фразы трек Eau de vie (Я скинул, постараюсь скачать из ВК)
    th "Без толку. {w}*трек Eau de vie*Обыскав весь дом, я ничего не нашла."
    "«Птенчик пропал!» эти слова эхом повторялись в моих мыслях."
    th "Теперь весь мой труд сегодня и весь день насмарку."
    th "Но страшнее даже не это..."
    th "Я не смогла защитить его и теперь он наверное потерялся."
    th "А я... Отнесла его далеко от мамы."
    th "Он же теперь не выживет {w}и всё из-за меня."
    th "Он такой маленький и незаметный, его просто раздавят."
    th "Господи, за что же это горе мне?"
    th "Почему я такая дура и не следила за ним?! Сытый желудок того не стоил."
    th "Я не хотела! Клянусь не хотела!"
    "Я не заметила, как отворилась дверь. Мне было абсолютно всё равно." 
    "Вся подушка была в солёных каплях, вытекающих из моих глаз."
    voice "Славя, что ты делаешь?"
    "Я ничего ей не ответила."
    mz "Выходя из столовой, ты была куда более в лучшем настроении. Что случилось?"
    sl "П... пппп... Птенчик пропал!!"
    "Как только я произнесла эти слова дрожащим голосом, из меня сразу хлынули слёзы с новой силой. Я не могла так просто смириться с пропажей маленького беззащитного птенца!"
    "Женя с силой посадила меня на кровать. Я всё так же продолжала плакать без устали..."
  #конец трека
    mz "Чего ты ревёшь? {w}Ты его на лавке у себя не заметила?"
    sl "Ч-что?"
    "Наконец я взглянула на неё."
  #трек Timid girl
    "В руках у неё был тот самый птенец!"
    "Я вмиг перестала плакать."
    sl "Женя, спасибо тебе огромное! Я так торопилась, что даже забыла, что не зашла в домик."
    mz "Ладно, пошли в библиотеку."
  #конец трека
    "..."
  #фон внутри библиотеки
    "Мы зашли в библиотеку и Женя принялась искать пособие по выведению птенцов."
    mz "Так... {w}Насекомые, овощи... {w}Крупа!"
    mz "Крупу будет легче всего достать, однако предпочтительнее мелкая живность."
    sl "Схожу в столовую, думаю мне одолжат немного."
    mz "Давай уж своего птенца, а то снова потеряешь."
    mz "Посижу с ним."
    sl "Спасибо."
    "Я посадила птенца ей на столик."
  #внутри столовой
    "Мне уже приходилось несколько раз обращаться к поварихе, так что меня она уже запомнила."
    "Я вежливо попросила у неё немного манки, объяснив ситуацию."
  #фон внутри библиотеки
    mz "Хилый он у тебя какой-то."
    sl "Знаю, но, к сожалению, я не смогу здесь остаться с ним. Меня ждут дома."
    sl "Мне придётся отнести его обратно в скворечник. {w}Кстати, пойду скорее, а то уже автобус скоро будет."
    mz "Давай, я пока что соберу свои вещи."
  #фон поляна
    "Я захватила с собой клейкую ленту и ножницы. Отрезав несколько кусочков, я залепила дно в несколько слоёв."
    sl "Сюда бы Шурика и Электроника, но они заняты сейчас."
    "Я положила птенчика обратно в скворечник, где его ждала мама."
    th "Наверное беспокоилась сильно..."
  #фон внутри домика Слави
    "Я побежала поскорее домой, потому что надо было успеть ещё на автобус."
    "Я вынула подушку из наволочки. {w}Свернула простыню и положила на матрас."
    "Затем стала сворачивать матрас. {w}Но моё внимание привлёк клочок бумаги застрявший в панцерной сетке и немного порванный."
  #трек Mystery girl
    "Я решила достать его."
  #картинка записки
    "{i}Надеюсь, Вам понравилась эта смена в Совёнке!{/i}"
    "{i}Обязательно сохраните все впечатления о ней, ведь другой такой же больше никогда не будет...{/i}"
    "Оставил(а) записку некий(ая) «{b}С{/b}»"
  #конец трека
  #убрать картинку записки
    th "Не могу не отметить, что почерк красивый, однако вероятнее всего писалось это в спешке."
    th "Надо будет и мне такой же памятник следующей смене оставить."
    th "И я не считаю это вандализмом."
    "Убрав записку в карман, я продолжила собираться."
  #тёмный фон и снова фон внутри домика слави
    "Большинство моих вещей так и продолжали лежать в сумке, поэтому я лишь собрала то немногое, что успела вынуть."
    "Я решила написать соответствующую записку для будущей смены."
  #тёмный фон и снова фон внутри домика Слави
    "Почему то было очень сложно что-нибудь придумать, поэтому я решила просто оставить эту же записку."
    "А затем я направилась к стоянке."
    "..."
  #фон автобус на стоянке
    "Пришлось немножко постоять."
    sl "Лен, скажи, тебе понравилось?"
    un "Да, не то что я себе представляла, но тоже неплохо."
    "Она улыбнулась."
    "Я встала рядом с ней."
    sl "Алиса, чего такая грустная?"
    dv "Да так, ничего..."
    sl "Тоже грустно уезжать?"
    dv "Ну и это тоже, в меньшей степени."
    "Наконец пришла Ольга Дмитриевна."
    pi "А где же «остальные»?"
    "Сказал один из пионеров, как вдруг..."
    "Из за ворот вышли Ульяна и Семён с сумками наперевес."
    "Он быстро закинул их в автобус и сбегал, видимо за своими, обратно в лагерь."
    "Все были в сборе."
  #трек memories
  #иллюстрация сборы перед отъездом
    mt "Все собрались?"
    "Начала Ольга Дмитриевна."
    mt "Сегодня вы покидаете наш лагерь, и на прощание мне хотелось бы вам кое-что сказать."
    "Она заметно нервничала и никак не могла подобрать нужные слова."
    mt "Надеюсь, что время, проведённое здесь, вам запомнится на всю жизнь, что у вас останутся только приятные воспоминания о «Совёнке»."
    mt "Также я надеюсь, что здесь вы стали чуточку лучше, смогли чему-то научиться, познакомились с новыми друзьями… {w} В общем, возвращайтесь в следующем году!"
    "Вожатая отвернулась."
    "Да, в такой момент было трудно сдержать слёзы."
    th "Я буду очень скучать." 
  #конец трека
  #фон внутри автобуса с пионерами
    "Мы взяли свои сумки и заносили их в салон, кладя их на колени или под кресла."
    "Я заняла место рядом с Олей."
    mt "Поездка займёт несколько часов."
    "Сказала она мне."
    "Я молча уставилась в окно."
  #фон внутри ночного автобуса с пионерами
    "Проехав уже достаточное расстояние, автобус включил фары. В свои права вступала ночь."
    "И меня начало клонить в сон..."
  #эффект закрывания глаз
    "..."
    
  #Если выбрали "Положить в карман рубашки"
    "Я как можно аккуратнее положила птенчика в наружный карман рубашки."
    th " Надеюсь он не наделает мне хлопот в столовой."
    "Я спокойно и аккуратно пошла к столовой."
  #фон далеко от столовой    
    th "Ходить с птенчиком в кармане оказалось не очень то и удобно. Но ничего, это всё ради его блага."
  #фон внутри столовой
    "В скором времени я отыскала Женю среди других пионеров. Она сидела одна за столиком в глубине столовой."
    "Я тихо подсела к Жене за столик."
    sl "Женя, мне нужна твоя помощь."
    mz "Да? Ну и в чём же состоит твоя просьба?"
    sl "Женя, ты же сможешь мне помочь накормить птенца?"
    mz "Зачем?"
    "Я показала ей его."
    mz "Ты где этого птенца откопала?"
    sl "Не откопала, он сам из скворечника выпал."
    mz "Какого скворечника?"
    sl "Ну, в лесу нашла."
    mz "И что ты собираешься дальше делать?"
    sl "Накормлю, починю скворечник и верну обратно."
    mz "А ты всё это время его голодным держала?"
    sl "Ну, инцидент произошёл я и забыла."
    mz "Ладно, посмотрим что в библиотеке есть. Приятного аппетита."
    sl "Тебе тоже!"
  #фон напротив библиотеки
    "На душе было приятно от совершения очередного хорошего дела."
  #фон внутри библиотеки
    "Мы зашли в библиотеку и Женя принялась искать пособие по выведению птенцов."
    mz "Так... {w}Насекомые, овощи... {w}Крупа!"
    mz "Крупу будет легче всего достать, однако предпочтительнее мелкая живность."
    sl "Схожу в столовую, думаю мне одолжат немного."
    mz "Оставь ты своего птенца, ничего с ним не произойдёт."
    mz "Могу даже на ключ закрыть, если не веришь."
    sl "Спасибо."
    "Я посадила птенца в коробку и поставила её на стол."
  #внутри столовой
    "Мне уже приходилось несколько раз обращаться к поварихе, так что меня она уже запомнила."
    "Мы вежливо попросила у неё немного манки, объяснив ситуацию."
  #фон напротив библиотеки
    mz "Хилый он у тебя какой-то. {w}Да и тем более, вот ты положишь его обратно. А дальше что?"
    sl "Не знаю, к сожалению, я не смогу здесь остаться с ним. Меня ждут дома."
    sl "Может быть поварихам сказать или с собой забрать. {w}Кстати, я что-то не видела его мамы."
    th "Наверное всё же возьму его с собой."
    "Женя открыла дверь."
  #фон внутри библиотеки
    "Я с радостью зашла внутрь. {w}Но всё моё настроение вмиг улетучилось, когда я посмотрела на стол."
  #трек Meet me there
    "Коробка лежала перевёрнутая рядом с ним."
    "И рядом валялся птенец. {w}Вернее... {w}Всё что от него осталось."
    th "Кому только могло прийти к голову растерзать такое беззащитное создание?"
    "Я не могла больше на этом смотреть и бросилась на грудь Жени."
    "Я громко разрыдалась"
  #пауза 3 секунды, очень плавный переход на следующий фон
  #фон внутри домика Слави
    "Я захватила изоленту из домика и отнесла её кибернетикам."
  #фон внутри клуба
  #спрайт удивлённого Электроника
    el "Славя, что случилось?"
    "Я не ответила."
  #фон внутри домика Слави
    "Все эмоции просто исчезли."
    "Я даже не заметила как на автомате собирала свои пожитки и постельное бельё."
  #очень плавное выключение трека
    "Но что-то всё же притянуло мой взгляд..."
    th "Записка."
  #картинка записки
    "{i}Надеюсь, Вам понравилась эта смена в Совёнке!{/i}"
    "{i}Обязательно сохраните все впечатления о ней, ведь другой такой же больше никогда не будет...{/i}"
    th "Оставил(а) записку некий(ая) «{b}С{/b}»"
  #убрать картинку записки
    "Я ещё некоторое время вглядывалась в неё, пытаясь понять суть."
    th "Надо мной будто издеваются!"
    "Я скомкала её. Я скомкала эту записку и выбросила в окно, чтобы никто, никогда на целом свете не нашёл эту чёртову записку!"
    "Я села на кровать и просто просидела так несколько минут, пытаясь сдержать слёзы."
    "Затем решила достать дневник и всё же написать в него."
    
  #Дневник(Ульяна)
    "{i}Я не справилась.{/i}"

    "Я положила его в сумку и направилась к остановке."
  #фон остановка
    "Пришлось немного постоять."
    "Наконец пришла Ольга Дмитриевна."
    pi "А где же «остальные»?"
    "Сказал один из пионеров, как вдруг..."
    "Из за ворот вышли Ульяна и Семён с сумками наперевес."
    "Он быстро закинул их в автобус и сбегал, видимо за своими, обратно в лагерь."
    "Все были в сборе."
  #трек memories
  #иллюстрация сборы перед отъездом
    mt "Все собрались?"
    "Начала Ольга Дмитриевна."
    mt "Сегодня вы покидаете наш лагерь, и на прощание мне хотелось бы вам кое-что сказать."
    "Она заметно нервничала и никак не могла подобрать нужные слова."
    mt "Надеюсь, что время, проведённое здесь, вам запомнится на всю жизнь, что у вас останутся только приятные воспоминания о «Совёнке»."
    mt "Также я надеюсь, что здесь вы стали чуточку лучше, смогли чему-то научиться, познакомились с новыми друзьями… {w} В общем, возвращайтесь в следующем году!"
    "Вожатая отвернулась."
    "Да, в такой момент было трудно сдержать слёзы."
    th "Прости меня птенчик..."
  #конец трека
  #фон внутри автобуса с пионерами
    "Мы взяли свои сумки и заносили их в салон, кладя их на колени или под кресла."
    "Я заняла место рядом с Олей."
    mt "Поездка займёт несколько часов."
    "Сказала она мне."
    "Я молча уставилась в окно."
  #фон внутри ночного автобуса с пионерами
    "Проехав уже достаточное расстояние, автобус включил фары. В свои права вступала ночь."
    "И меня начало клонить в сон..."
  #эффект закрывания глаз
    "..."

  #Рут одиночки
  #Если выбрали "Одиночка"
  else:
    "Утро этого дня явно не задалось."
    "Вначале я проснулась не выспавшейся."
  #посреди фразы эффект удара и трек Awakening power
    "А во вторых я проспала... {w}ЛИНЕЙКУ!!!"
    th "Этого не может быть! Время уже без десяти одиннадцать, а я только проснулась!"
    "Я мигом собрала все силы в кулак, вскочила с постели и надела форму."
  #фон домики
  #эффект бега
    "На ходу я застёгивала нижние пуговицы и завязывала галстук."
  #фон площадь
  #фон далеко от столовой
  #фон напротив столовой
  #конец эффекта
  #конец трека
    "Когда я добежала, площадь была {w}конечно же пуста."
    "С чувством вины я направилась в столовую."
  #фон внутри столовой
    "Столовая всё ещё была заполнена пионерами."
    "Я встала в очередь за своей порцией, издалека заприметив свободное место."
    "Получив порцию и дойдя до него, ко мне подсела Женя."
    mz "Что-то ты сегодня поздно. Ольга Дмитриевна была недовольна."
    sl "Странно что она не подняла весь лагерь на уши в моих поисках, я ведь никогда не пропускаю линейки."
    mz "Она всё списала на то, что у тебя была какая-то уважительная причина."
    sl "Надо будет извиниться перед ней."
    mz "Да не стоит, лишний раз ей напоминать, лишняя болтовня. Разве тебе не хочется провести последний день с пользой или что-то вроде того?"
    mz "Ты хочешь чтобы он тебе запомнился ссорой с вожатой?"
    sl "Нет конечно."
    mz "Так что просто забудь. {w}Ладно, я пойду в библиотеку."
    "Я решила не напоминать ей про случай с Электроником."
    "А просто доела свою порцию и вышла из-за стола."
  #фон напротив домика Слави
    "Я решила не терять времени зря и собрать свои вещи заранее."
  #фон площадь
    "Но когда я уже вышла на площадь, меня остановила Оля."
    mt "Славя, привет, я знаю, сегодня последний день смены, но мне как нельзя кстати пригодилась бы твоя помощь в «райцентре»."
    sl "Да ничего, а что надо сделать?"
    mt "Просто бумажная работа."
    #спрайт улыбающейся ОД
    mt "Но тебе по секрету скажу."
    mt "Нам определённые преференции капают, поэтому нужно собирать побольше достижений и рекомендаций."
    mt "И тебе, как помощнице вожатой, тоже причитается, просто отнеси некоторые документы."
    mt "Я бы и Семёна попросила, но как подумаю, сразу представляю себе бесконечные вопросы от него, поэтому, справишься?"
    sl "Конечно, Оля."
    "Я улыбнулась ей и мы направились в административный корпус."
    #тёмный экран
    "..."
    #фон внутри административного корпуса
    "Когда мы пришли, Оля принялась перебирать среди бумажек и разных папок, доставать какие-то, листки и перекладывать в свою папку."
    "Мне показалось это какой-то закулисной бюрократией, о той, которую не показывают по телевизору."
    "Хоть я и хорошо познакомилась с Олей за эти две недели, но всё равно казалось это чем-то странным."
    sl "А это точно законно?"
    mt "Славя!"
    #спрайт ОД
    "Она обернулась."
    mt "Я разве похожа на Семёна?"
    sl "А почему именно Семёна?"
    "Она какое-то время помолчала и, наконец, ответила."
    mt "А он разве не такой?"
    sl "Конечно не такой, он хороший, просто несмекалистый."
    mt "Только не говори мне, что у вас с ним что-то намечается."
    sl "Да нет, Оля, ты что, просто он никогда мне не казался таким."
    mt "Это каким?"
    "Спросила она меня, хоть и сама явно догадывалась."
    sl "Нестабильным элементом. Вот Алиса какая-нибудь.."
    mt "Ладно, я поняла."
    "Она улыбнулась."
    #звук горна
    "Прошло уже достаточно времени, работа была непыльная, но монотонная."
    mt "Я тут почти закончила, спасибо, что помогла, беги на обед."
    sl "Уже всё?"
    mt "Да, уже всё."
  #фон внутри столовой
    "Обед, ровно как и завтрак, не представлял из себя ничего необычного."
    "Больше всего меня волновал Семён."
    "За весь прошедший день я так его ни разу и не встретила."
    "Уже после того как я поела, я ещё некоторое время сидела, рассматривая заходящих у уходящих пионеров."
    "Но среди них не было того, кого я искала."
    th "Либо он успел первым войти и первым поесть, либо он всё ещё спит."
    "Поэтому я решила вначале узнать у Ольги Дмитриевны. Очевидно он ночевал у себя в домике, просто потому что больше негде."
    "Я встала из-за стола, но нечаянно задела стакан с почти выпитым компотом."
    "Немного пролилось и на одежду."
    "Я быстро сбегала за тряпочкой, чтобы протереть стол, и побежала в домик."
  #фон тёмный экран
    "..."
  #фон внутри домика Слави
    "Выбирать было не из чего, поэтому я надела первое, что попалось на глаза."
    "А первой мне попалась на глаза моя спортивная форма."
    "Поэтому, я надела её, а грязную одежду быстро понесла к умывальникам."
  #фон умывальники
    "У умывальников нашёлся пропавший."
    me "Не знаю... Но мне тоже хочется в это верить."
  #трек Afterword
    sl "Семён!"
    "Он обернулся."
    sl "Ты с кем это разговариваешь?"
    me "Да... Ни с кем... {w}Так, сам с собой."
    th "Я не стала совать свой нос не в своё дело."
    sl "Ты уже собрался?"
    th "Или я тебе могу помочь?"
    me "Собрался? Опять какой-то поход?"
    sl "Нет же! {w}Сегодня последний день смены."
    me "Чего?.."
    "Он расплылся в глуповатой улыбке."
    sl "Вечером автобус. Уезжаем."
    me "Ах, вот так даже..."
    me "Пока не собрался..."
  #конец трека
    "Я смотрела на него и слишком отвлеклась."
  #трек What do you think of me?
    me "Да у меня вещей-то особо нет."
    sl "Ладно..."
    "Семён смотрел на меня и мне было сложно собраться с мыслями." 
    "Я застеснялась и отвела взгляд."
    "Но вдруг я вспомнила, что облилась компотом, стыдно было показаться перед ним с горстью грязной одежды, поэтому поспешила ретироваться."
    sl "Тогда увидимся ещё!"
    me "Ага..."
  #конец трека
    th "Надо было смотреть когда руками махала, растяпа, но кто ж знал." 
    th "Надеюсь он не подумает, что я грязнуля."
  #фон тёмный экран
    "..."
  #фон домики
  #фон умывальники
    "Переждав немного, я вернулась к умывальникам."
    "Я положила грязную форму под воду и стала её замачивать."
    "Кое-как оттерев пятно руками, я направилась в домик."
  #фон внутри домика Слави
    "Нужно было куда-то повесить форму, но верёвок не было."
    "Благо капать перестала."
    "Поэтому я перекинула через форточку и повесила сушиться там. Тем более что светило солнце."
    "Я взглянула на часы. {w}Времени было около 2 часов дня."
    "Я решила собраться заранее."
    "Вынула подушку из наволочки. {w}Свернула простыню и положила на матрас."
    "Затем стала сворачивать матрас. {w}Но моё внимание привлёк клочок бумаги застрявший в панцерной сетке и немного порванный."
  #трек Mystery girl
    "Я решила достать его."
  #картинка записки
    "{i}Надеюсь, Вам понравилась эта смена в Совёнке!{/i}"
    "{i}Обязательно сохраните все впечатления о ней, ведь другой такой же больше никогда не будет...{/i}"
    "Оставил(а) записку некий(ая) «{b}С{/b}»"
  #конец трека
  #убрать картинку записки
    th "Не могу не отметить, что почерк красивый, однако вероятнее всего писалось это в спешке."
    th "Надо будет и мне такой же памятник следующей смене оставить."
    th "И я не считаю это вандализмом."
    "Убрав записку в карман, я продолжила собираться."
  #тёмный фон и снова фон внутри домика слави
    "Большинство моих вещей так и продолжали лежать в сумке, поэтому я лишь собрала то немногое, что успела вынуть."
    "И вышла из домика."
  #фон домики
    "Мне нужно было найти Семёна и самым вероятным местом где он мог быть, был конечно же домик Ольги Дмитриевны."
  #фон напротив Домика ОД
    "Я постучалась, надо же было убедиться, что кто-нибудь есть."
    "Дверь открыл Семён."
  #фон внутри домика ОД
    me "Ты к Ольге Дмитриевне?"
    sl "Нет..."
    me "Входи тогда."
    "Семён оглянулся за спину, но потом снова повернулся ко мне."
    "Я уселась на кровать слева."
    "Семён же облокотился спиной к шкафу."
  #трек Confession
    "И тут у меня началась паника, потому что я не знала с чего бы мне начать."
    me "Что-то случилось?"
    "Семён как не вовремя был сконцентрирован и не витал в облаках, как он это делает обычно."
    th "Не знаю почему, но чувствую себя как-то обмануто."
    sl "Нет... Просто сегодня же последний день..."
    me "Да я уже в курсе. Лучше поздно, чем никогда."
    "Подобрать правильные слова было очень тяжело, я решила всё же сделать первый шаг."
    sl "Ну, я и думала... {w}В смысле... {w}Мы же больше не увидимся, наверное."
    me "Мир тесен, как говорится."
    "Его слова пролетели мимо."
    sl "Может быть, ты мне свой адрес оставишь куда писать."
  #конец трека
  #трек из ссылки с которой я скинул файл, ес чо называется трек Mind The Gap TRAIN TRACKS 2014
    "Семён немного удивился."
    me "Понимаешь... Давай лучше ты мне свой. Я тебе обязательно напишу по приезду."
    th "Так вот почему, подсознание мне намекало всё это время.."
    sl "А почему ты не хочешь?"
    me "Ну... Мы просто переезжать совсем скоро собирались, поэтому мало ли что... {w}Лучше я тебе писать буду."
    "Семён улыбнулся."
    "Всё моё приподнятое настроение как рукой смахнуло."
    th "Лучше бы не врал, а честно сказал, что не хочешь общаться, я ведь действительно бы ждала твоего письма, а ты и не напишешь…"
    "Но вместо всего этого, я просто сказала:"
    sl "А, хорошо, понятно... Тогда ладно."
    "Я встала и направилась к двери. Уточнений не требовалось."
    me "Подожди, а адрес?"
    "Сказал он, наверное, больше из вежливости."
    sl "Давай потом."
    "Но никакого потом не будет. Семён явно ничего не испытывает ко мне."
  #фон напротив домика ОД
    "В разбитых чувствах я направилась обратно."
    "Чем занять остальной день было решительно непонятно."
  #конец трека
  #фон внутри домика Слави
    "Я решила искупаться. В последний-то день."
    th "А почему нет? Люблю купаться."
    "Я надела купальник и взяла с собой полотенца."
  #фон домики
  #фон площадь
  #фон пляж
    "К моему удивлению, на пляже почти что никого не было."
  #трек Take me beautifully
    th "Тем лучше."
    "Расстелив большое полотенце на песке, я сняла форму и забежала в воду."
    "..."
  #снова фон пляж
    "Однако, это скоро мне наскучило."
    "Поэтому я вышла на берег, обтёрлась и просто глядела на воду. Прошло, наверное, ещё не так много времени."
    "Через примерно полчаса ожидания, я пошла обратно."
  #конец трека
    "Я буквально не находила себе места, мне нужно было себя чем-то занять, но меня постоянно погружало в размышления."
    "При чём не самые приятные."
    th "Почему Семён так поступил со мной?"
    th "Он за всё это время ни разу не подметил мои намёки?"
    "Я посмотрела на небо, первое, что мне пришло в голову, чтобы отвлечься."
    "День начал близиться к вечеру."
    "К этому моменту я уже полностью высохла, поэтому просто надела форму."
  #фон домики
  #фон внутри домика Слави
    "До автобуса оставался примерно час времени, я решила написать соответствующую записку для будущей смены."
  #снова фон внутри домика Слави
    "Почему то было очень сложно что-нибудь придумать, поэтому я решила просто скопировать эту записку."
    "..."
    "Когда было готово, я перечитала. {w}И обнаружила что шрифты были очень похожи."
    "Даже не так... {w}Они были идентичными!"
    th "Я что, настолько сильно перекопировала, что даже шрифт похожий? Да нет, бред какой-то!"
    th "Видимо просто совпадение."
    "Я сложила бумажку и подложила её под матрас."
    th "Её обязательно найдут!"
    "Я в последний раз посмотрела на стены домика."
    th "Прощай!"
  #фон площадь
    "На площади собирались пионеры и их вожатая."
    mt "Все кто собрался молодцы, а мне придётся собирать остальных. Идите, пока что, к остановке."
    "Удивительно, но у нас удалось быстро организоваться идти колонной."
  #фон напротив клубов
  #фон остановка
    "Пришлось немножко постоять."
    sl "Лен, скажи, тебе понравилось?"
    un "Да, не то, что я себе представляла, но тоже неплохо."
    "Она улыбнулась."
    "Я встала рядом с ней."
    sl "Алиса, чего такая грустная?"
    dv "Да так, ничего..."
    sl "Тоже грустно уезжать?"
    dv "Ну и это тоже, в меньшей степени."
    "Мимо нас пробежала Ульяна."
    sl "Стоять! Куда бежим? Скоро Ольга Дмитриевна придёт."
    us "Да никуда я не бегу! Делать просто нечего пока ждём опаздывающих."
    "Последней показалась Мику со своим волоком вещей."
    th "И зачей ей столько здесь?"
    mi "Ой, а я рано пришла? Автобус ещё не пришёл? Я наверное зря тащила все свои вещи сюда, да?"
    "Наконец Ольга Дмитриевна пришла {w}одна."
    pi "А где же «остальные»?"
    mt "Только Семён остался. Он через пару минут придёт."
    "И действительно, через минуту из-за ворот показался Семён."
  #трек memories
  #иллюстрация сборы перед отъездом
    mt "Все собрались?"
    "Начала Ольга Дмитриевна."
    mt "Сегодня вы покидаете наш лагерь, и на прощание мне хотелось бы вам кое-что сказать."
    "Она заметно нервничала и никак не могла подобрать нужные слова."
    mt "Надеюсь, что время, проведённое здесь, вам запомнится на всю жизнь, что у вас останутся только приятные воспоминания о «Совёнке»."
    mt "Также я надеюсь, что здесь вы стали чуточку лучше, смогли чему-то научиться, познакомились с новыми друзьями… {w} В общем, возвращайтесь в следующем году!"
    "Вожатая отвернулась."
    "Да, в такой момент было трудно сдержать слёзы."
    th "Я буду очень скучать." 
  #конец трека
  #фон внутри автобуса с пионерами
    "Мы взяли свои сумки и заносили их в салон, кладя их на колени или под кресла."
    "Я заняла место рядом с Олей."
    mt "Поездка займёт несколько часов."
    "Сказала она мне."
    "Я молча уставилась в окно."
  #фон внутри ночного автобуса с пионерами
    "Проехав уже достаточное расстояние, автобус включил фары. В свои права вступала ночь."
    "И меня начало клонить в сон..."
  #эффект закрывания глаз
    "..."

label slavyana_mod__day7_epilogue_alt:
  window hide
  stop music
  stop sound
  stop ambience
  $ backdrop = "epilogue"
  $ new_chapter(7, u"Славя. День ...")
  $ save_name = (u'Славя. День ...')
  $ day_time()
  $ persistent.sprite_time = "day"
  $ renpy.pause(3, hard=True)
  play sound_loop sfx_bus_interior_moving fadein 3 loop
  scene bg int_bus_people_day
  show unblink
  window show
  "Автобус слегка потрясывало и подбрасывало на небольших кочках."
  th "Как это у меня удалось уснуть в автобусе?"
  "Я огляделась, все остальные только просыпались, кто то и не спал вовсе."
  "Рядом со мной по-прежнему сидела Ольга Дмитриевна."
  "Мы уже подъезжали к месту. Это было видно из окна."
  window hide
  pause 2
  stop sound_loop fadeout 1
  play sound sfx_bus_stop fadein 1
  scene black with dissolve
  window show
  "Наконец автобус заехал на стоянку и остановился, раскрыв свои двери."
  window hide
  scene bg ext_camp_entrance_day with dissolve2
  window show
  th "Ну здравствуй, «Совёнок»! Эта смена будет самой незабываемой и самой неповторимой!"
  window hide
  pause 2
  scene black with dissolve2

  # TODO: ачивка "Сохранить девственность"

  $ words_red = True
  call slavyana_mod__ending
  play music music_list["memories"]
  pause 1
  scene cg titles_sl_with_image with dissolve
  jump slavyana_mod__credits
