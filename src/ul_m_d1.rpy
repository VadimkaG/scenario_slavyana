init:
    image underwater = "scenario_slavyana/res/images/uliana/underwater.jpg"
    
    image d1_grasshopper_1_orika = "scenario_slavyana/res/images/uliana/d1_grasshopper_1_orika.jpg"
    image d1_grasshopper_2_orika = "scenario_slavyana/res/images/uliana/d1_grasshopper_2_orika.jpg"
    image d1_grasshopper_3_orika = "scenario_slavyana/res/images/uliana/d1_grasshopper_3_orika.jpg"
    
    image dv angry swim = ConditionSwitch(True, im.Composite((900,1080), (0,0), "scenario_slavyana/res/images/uliana/dv/normal/dv_5_swim.png", (0,0), "scenario_slavyana/res/images/uliana/dv/normal/dv_5_angry.png"))
    
    $ bell = "scenario_slavyana/res/sound/uliana/zvuk_-_zvonok_na_urok.mp3"
    $ dv_snoring = "scenario_slavyana/res/sound/uliana/dv_snoring.wav"
    $ dv_scream = "scenario_slavyana/res/sound/uliana/dv_scream.wav"
    
label uliana_mod_day1:
    scene black with dissolve
    $ sl_m_try = "makenkn"
    call sl_m_try
    $ sl_m_try = None
    pause(3)
    $ backdrop = "days"
    $ sl_m_try = "savenameul"
    call sl_m_try
    $ sl_m_try = None

    $ day_time()
    $ persistent.sprite_time = "day"
    
    $ dv_good_end = 0
    $ semen_good_end = 0
    
    #В домике
    hide unblink
    show blink
    scene bg int_house_of_dv_day with dissolve
    play ambience ambience_int_cabin_day fadein 3
    play music music_list["smooth_machine"] fadein 3
    $ renpy.pause(1)
    window show
    "Яркий солнечный свет бил прямо в лицо."
    "Я лениво поежилась на кровати, протирая глаза ото сна."
    th"Что, уже утро?"
    th"Интересно, сколько сейчас времени?"
    "Я приподнялась и посмотрела на часы. {w}Стрелки на циферблате показывали 7 утра."
    th"Что-то я сегодня рано..."
    "Спать дальше почему-то совсем не хотелось."
    th"Чем бы заняться?"
    window hide
    play sound dv_snoring
    pause(1.5)
    window show
    "С соседней кровати доносилось легкое сопение." 
    "Его источником была мирно спавшая Алиса, моя соседка.{w} Солнечные лучи падали прямо на ее постель, но она даже не думала просыпаться."
    "Хоть мне и наскучило сидеть одной, будить ее в такую рань я не решилась."
    th"Все равно ведь не поднимется!"
    th"Раз уж тут делать нечего, пойду прогуляюсь до умывальников. Может даже встречу кого-нибудь."
    stop music fadeout 3
    stop sound fadeout 1
    "Я бесшумно встала, надела шорты и свою любимую футболку с надписью \"СССР\" и, захватив умывальные принадлежности, вышла из домика."
    window hide
    stop ambience fadeout 1
    
    play sound sfx_open_door_1
    scene black with dissolve
    pause(1)
    
    #У домика
    scene bg ext_house_of_dv_day with fade
    play ambience ambience_camp_center_day fadein 1
    play music music_list["my_daily_life"] fadein 3
    pause(1)
    window show
    "Утром на улице было довольно прохладно и свежо. {w}Воздух еще не успел до конца нагреться, даже несмотря на палящее солнце."
    window hide
    
    #Дорожка
    scene bg ext_houses_day with dissolve
    pause(1)
    window show
    "Лагерь пустовал. {w}Вокруг не было ни души."
    th"Ну естественно, мало кто по своей воле поднимется в такую рань!"
    window hide
    
    #Умывальники
    scene bg ext_washstand_day with dissolve
    pause(1)
    window show
    "Спустя несколько минут я уже стояла возле умывальников."
    window hide
    
    #Раковина
    play sound sfx_open_water_sink
    scene bg ext_washstand2_day with dissolve
    pause(1)
    play sound_loop sfx_water_sink_stream
    pause(1)
    window show
    "Вода из крана ярко переливалась в лучах утреннего солнца и отражалась на стенках раковины, создавая множество светлых пятен."
    "Сполоснув руки и лицо, я достала из кармана небольшой пакетик, где лежали все мои умывальные принадлежности, и начала извлекать содержимое."
    th"Так, что тут у нас? {w}Щетка, мыло, зубной порошок..."
    th"Сразу же вспомнилась понравившаяся мне шутка, которую я когда-то давно услышала:"
    th"Если мальчик любит мыло и зубной порошок, \n То у этого кретина будет заворот кишок!"
    #th"Сразу же вспомнился стишок, который мне часто читали в детстве:"
    #th"Если мальчик любит мыло и зубной порошок, \n Этот мальчик очень милый, поступает хорошо."
    "На этой минорной ноте я принялась чистить зубы."
    window hide
    
    pause(2)
    stop sound_loop
    
    #Умывальники
    play sound sfx_close_water_sink
    scene bg ext_washstand_day with dissolve
    pause(1)
    stop music fadeout 4
    window show
    th"Все таки хорошо с утра умываться на свежем воздухе. После этого чувствуешь себя взбодрившейся и полной сил."
    "Окончив свои утренние водные процедуры, я уже направилась обратно в домик, как вдруг услышала чьи-то приближающиеся шаги."
    window hide
    play music music_list["went_fishing_caught_a_girl"] fadein 3
    play sound sfx_slavya_run
    pause(3)
    show sl normal sport far:
        xalign 1.5 yalign 1.0
        linear 3.0 xalign 0.5
    pause(3)
    window show
    "Навстречу мне выбежала Славя в спортивном костюме."
    th"Значит все таки не я одна сегодня рано встала."
    show sl smile sport far with dspr
    sl"Физкульт-привет!"
    us"Физкульт-ура! {w}Как твоя утренняя пробежка?"
    show sl smile2 sport far with dissolve
    sl"Отлично! Уже три круга проделала, последний остался..."
    us"Неплохо. {w}Но сколько бы ты не старалась, меня догнать все равно не сможешь!"
    th"Я бегаю быстрее всех в лагере. Куда уж ей до меня!"
    show sl surprise sport far with dissolve
    sl"Ну это мы еще посмотрим!" 
    th"Тут мне пришла в голову интересная идея."
    us"А давай поспорим, что этот круг я пробегу быстрее тебя!"
    show sl serious sport far with dissolve
    sl"Нет, спорить я не буду."
    th"Вот всегда так! Наверняка ведь знает, что проиграет, поэтому и отнекивается!"
    us"Ага, значит все таки не догонишь!"
    show sl serious sport far with dspr
    sl"А вот и догоню!"
    us"А вот и нет!"
    sl"А вот и да!"
    us"А ты докажи!"
    sl"Хорошо.{w} На что спорим?"
    th"Как быстро она согласилась!{w} Хотя неудивительно, в спорах мне равных не было, это уж точно."
    us"Если я выиграю, то ты должна будешь мне мешок конфет."
    show sl surprise sport far with dissolve
    sl"Но откуда я достану мешок конфет?"
    th"А сама как-будто не знает, где тут у нас конфеты хранятся?"
    us"В столовке, где же еще! У тебя и ключ от шкафчика есть."
    show sl serious sport far with dissolve
    sl"Но ведь это же воровство!"
    us"Ничего не знаю, у нас спор."
    sl"Тогда, если я выиграю, ты весь день будешь вместо меня убираться в лагере!"
    th"И сдалась же ей эта уборка!"
    us"По рукам!"
    window hide
    stop music fadeout 3
    
    #Забег
    scene bg ext_houses_day with dissolve
    pause(1)
    window show
    "Славя описала мне маршрут забега, и мы встали на старт."
    sl"Начинаем по моей команде."
    play music music_list["always_ready"] fadein 3
    sl"Три..."
    sl"Два..."
    sl"Один..."
    sl"Старт!"
    scene bg ext_houses_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve     
    "Мы резко рванулись с места.{w} Через несколько секунд Славя уже бежала впереди меня с небольшим отрывом."
    th"Видимо, регулярные пробежки пошли ей на пользу. {w}Ну ничего, сейчас я ей продемонстрирую настоящую скорость!"
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
    scene bg ext_house_of_sl_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve
    "Затем повернули к домикам..."
    scene bg ext_house_of_dv_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve
    "Пробежали мимо моего..."
    scene bg ext_square_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve
    "Минуя площадь, я успела поравняться со Славей и слегка обогнать ее."
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
    th"Неужели выдохлась? Слижком уж быстро!"
    scene bg ext_dining_hall_near_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve
    "Подбежав к крыльцу, я развернулась и продолжила бег по назначенному маршруту."
    scene bg ext_square_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve
    "Оказавшись снова на площади, я обнаружила, что Славя уже дышит мне в затылок."
    th"Нужно срочно ускориться! {w}До финиша осталось совсем немного! {w}Я не позволю ей украсть у меня победу!"
    "Я изо всех сил постаралась увеличить скорость, и это дало результат: Славя немного отстала."
    scene bg ext_washstand_day:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat 
    with dissolve
    "Спустя пару секунд мы уже были на финишной прямой."
    th"Ну вот, теперь осталось только..."
    stop music fadeout 3
    show mt normal pioneer far with dissolve
    th"Только не это!"
    show mt normal pioneer with dissolve
    th"Только не сейчас, пожалуйста!"
    show mt surprise pioneer close with dissolve
    play music music_list["revenga"] fadein 3
    th"НЕЕЕЕТ!!!"
    window hide
    
    scene black with dissolve
    play sound sfx_fall_grass
    pause(1) 
    window show
    "Из-за сильного разгона я не успела вовремя затормозить и на большой скорости влетела прямиком в вожатую, сбив ее с ног."
    window hide
    
    #Умывальники
    scene bg ext_washstand_day
    show sl scared sport close behind unblink
    show unblink
    pause(1)
    window show
    "Мы очутились на земле, и к нам тут же подбежала Славя."
    sl"Ольга Дмитриевна, вам не больно? Вы не ушиблись?{w} Давайте я вам помогу!"
    th"Ну конечно! {w}Чуть что, так сразу Ольга Дмитриевна!{w} А обо мне кто-нибудь подумает?"
    window hide
    show sl scared sport at cleft with dissolve
    show mt angry pioneer:
        xalign 0.75 ypos 1.0
        linear 2.0 yalign 0.5
    pause(2) 
    window show
    "Тем временем Славя уже успела помочь вожатой подняться."
    mt"Ульяна!{w} Что все это значит?!"
    us"Мы бежали, затем поворот, потом вы, я не успела затормозить, и в общем..."
    mt"Тебя разве не учили смотреть по сторонам когда бежишь? {w}Не видишь что-ли, что человек идет?!"
    stop music fadeout 3
    us"Простите... Я так больше не буду..."
    show mt normal pioneer:
        xpos 0.75 
    with dissolve
    mt"Ладно, так и быть, прощаю."
    show sl normal sport at cleft with dissolve
    th"И на том спасибо..."
    "Я, наконец, встала с земли и отряхнулась."
    mt"Девочки, вы же помните, что скоро у нас линейка?"
    show sl smile sport at cleft with dspr
    sl"Конечно помним!"
    th"Точно, еще и линейка эта сегодня..."
    show mt smile pioneer:
        xpos 0.75 
    with dspr
    mt"Ну вот и хорошо. {w}У вас есть время, чтобы вернуться в домики и надеть форму."
    show mt angry pioneer:
        xpos 0.75 
    with dissolve
    mt"Ульяна, а ты разбуди Двачевскую. {w}И пусть она только попробует снова не явиться!"
    us"Постараюсь...."
    th"Думаю, Алиса не сильно обрадуется."
    show mt normal pioneer:
        xpos 0.75 
    with dissolve
    mt"Ладно, мне пора идти.{w}Через десять минут построение на площади, не опаздывайте!"
    hide mt with dissolve
    sl"Я тоже уже ухожу. {w}До встречи на линейке!"
    window hide
    hide sl with dissolve
    pause(1)
    window show
    th"Ну вот, не видать мне теперь мешка с конфетами...{w} А победа была так близка!{w} Это все вожатая виновата!"
    window hide
    
    #Дорожка
    scene bg ext_houses_day with dissolve
    pause(1)
    window show
    "Я молча поплелась к себе в домик."
    "Нога слегка болела после падения. {w}Только сейчас я заметила, что на ней появился небольшой синяк."
    th"Ничего, пройдет. Мне не привыкать!"
    "Идти на линейку, откровенно говоря, не хотелось, но получать второй по счету за день нагоняй от Ольги Дмитриевны хотелось еще меньше."
    window hide
    
    stop ambience fadeout 1
    scene black with dissolve
    pause(1)
    play sound sfx_open_door_1
    
    #В домике
    scene bg int_house_of_dv_day with fade
    play ambience ambience_int_cabin_day fadein 1
    play sound dv_snoring
    pause(1)
    window show
    "Зайдя в дом, я вдруг подумала:"
    th"А стоит ли мне вообще будить Алису?{w} Пускай спит дальше, все равно на линейке ничего полезного не скажут."
    th"С другой стороны, нам ведь потом обеим влетит от вожатой."
    th"И как же мне поступить?"
    window hide
    menu:
        "Разбудить Алису":
            $ dv_good_end = dv_good_end - 1 
            window show
            "Еще раз подумав о возможном наказании, я все-таки решила ее разбудить."
            stop sound fadeout 1
            th"Мало ли, что Ольга Дмитриевна может нам устроить!"
            play music music_list["gentle_predator"] fadein 3
            "Я подошла к Алисе и начала трясти ее за плечо."
            us"Подъем, спящая красавица, а то на линейку опоздаешь!"
            window hide
            show dv surprise swim with dissolve
            pause(1)
            window show
            dv"А?{w} Что?{w} Какую линейку?"
            show dv angry swim with dissolve
            dv"Ульяна, ты же знаешь, я не хожу на линейки!"
            us"А ведь тебя и наказать за это могут!"
            dv"Тоже мне угроза!{w} Пускай наказывают, мне все равно!"
            dv"А сейчас я спать. {w}И больше не вздумай будить меня так рано, поняла?{w} Иначе сама тебя накажу!"
            us"И как же ты собралась меня наказывать?"
            show dv normal swim with dissolve
            dv"Не волнуйся, что-нибудь обязательно придумаю."
            hide dv with dissolve
            "С этими словами Алиса легла обратно на кровать и закрыла глаза."
            stop music fadeout 3
            th"Видимо, все-таки не стоило ее будить."
            window hide
        "Не будить Алису":
            $ dv_good_end = dv_good_end + 1 
            stop sound fadeout 1
            th"Ладно, не буду ее тревожить, пускай отсыпается.{w} Все равно на линейку она вряд ли пошла бы."
            window hide
    stop ambience fadeout 1
    play sound sfx_open_door_1
    
    scene black with dissolve
    pause(1)
    
    #У домика
    scene bg ext_house_of_dv_day with fade
    play ambience ambience_camp_center_day fadein 1
    window show
    "Переодевшись в пионерскую форму, я вышла из домика и направилась к площади."
    window hide
    
    #Дорожка
    scene bg ext_houses_day with dissolve
    pause(1)
    window show
    th"А что я скажу вожатой?{w} Алисы ведь на линейке не будет."
    th"Придется соврать что-нибудь."
    "К счастью, с этим у меня никогда проблем не возникало."
    window hide
    
    scene black with dissolve
    pause(1)
    
    #Площадь
    scene bg ext_square_day with fade
    play ambience ambience_medium_crowd_outdoors fadein 3
    play music music_list["everyday_theme"] fadein 3
    window show
    "На площади уже собралось довольно много пионеров, в том числе из нашего отряда."
    show sl smile2 pioneer:
        xpos -0.1
    with dissolve
    "Славя..."
    show un surprise pioneer at cleft with dissolve 
    "Лена..."
    show mz shy pioneer at cright with dissolve
    "Женя..."
    show el smile pioneer:
        xpos 0.6
    with dissolve
    "... и Электроник."
    window hide
    show mt normal pioneer with dissolve
    pause(1)
    window show
    mt"Вижу, все уже в сборе."
    stop ambience fadeout 3
    show sl normal pioneer:
        xpos -0.1
    show un normal pioneer at cleft 
    show mz normal pioneer at cright 
    show el normal pioneer:
        xpos 0.6
    with dissolve
    hide sl
    hide un
    hide mz
    hide el
    with dissolve
    "При виде Ольги Дмитриевны наш отряд выстроился в одну шеренгу."
    mt"Все, кроме Алисы."
    show mt angry pioneer with dissolve
    mt"Ульяна!{w} Я же просила тебя ее разбудить!"
    us"А она не может.{w} У нее это... {w}живот болит!"
    mt"А не врешь?"
    us"Честное пионерское!"
    show mt normal pioneer with dissolve
    mt"Ладно, тогда пускай поправляется."
    mt"А теперь перейдем непосредственно к теме..."
    th"Ну вот, сейчас опять начнется... {w}Порядочный пионер должен то, порядочный пионер должен это, и все в таком духе... {w}Как же надоело!"
    th"Еще с ранних лет мне внушают, чего я должна делать, а чего не должна."
    mt"...и главное, что от вас требуется - дисциплина!"
    th "Вот опять это слово! Всюду только его и слышу! {w}Хотя ко мне, конечно же, оно ни имеет никакого отношения."
    mt"...ведь мы стоим на пороге светлого будущего, и каждый из вас должен внести свой вклад..."
    th"Ну и как тут забыть упомянуть про светлое будущее, строить которое должны почему-то всегда мы - пионеры."
    window hide
    stop music fadeout 3
    pause (2)
    window show
    "Вожатая все никак не могла закончить свой долгий и бессмысленный монолог."
    show mt normal pioneer with dissolve
    play music music_list["i_want_to_play"] fadein 3
    mt"...И напоследок важная новость: сегодня к нам в лагерь приезжает новенький."
    th "О, а вот это уже что-то интересненькое!"
    us"А когда он приедет?"
    mt"После обеда."
    us"Здорово!{w} А как его зовут?{w} И сколько ему лет?"
    show mt grin pioneer with dissolve
    mt"А ты подойди к нему и познакомься."
    us"Вот еще!{w} Пускай сам первый подходит!"
    th"Ну раз не хотите говорить - как хотите.{w} Я сама все узнаю!"
    window hide
    stop music fadeout 3
    play music music_list["dinner_horn_processed"]
    pause(3)
    window show
    "Прозвучал сигнал, призывающий пионеров на завтрак."
    show mt smile pioneer with dissolve
    mt"Все, ребята, линейка окончена!{w} Можете расходиться."
    window hide
    play ambience ambience_medium_crowd_outdoors fadein 3
    hide sl
    hide un
    hide mt
    hide mz
    hide el
    with dissolve
    pause(2)
    window show
    "Площадь стала понемногу пустеть. {w}Все пионеры направлялись в столовую."
    th"Пойду и я тоже.{w} Молодому растущему организму необходима энергия!"
    "Я развернулась и последовала за толпой пионеров, стараясь не отставать."
    window hide
    stop ambience fadeout 3
    scene black with dissolve
    pause(3)
            
    #Столовая 
    scene bg int_dining_hall_people_day with fade
    play ambience ambience_dining_hall_full fadein 1
    pause(1)
    window show
    "К тому моменту, как я пришла, столовая была уже почти полностью забита."
    "Свободное место нашлось далеко не сразу.{w} Присев, я тут же набросилась на еду."
    "Жадно поглощая манную кашу, я осматривала присутствующих."
    "За одним из столов сидели Лена и Мику."
    th"Не самая удачная компания.{w} Постоянно молчаливая Лена и не в меру болтливая Мику.{w} Как они вообще в одном домике уживаются?"
    "В другом конце столовой я заметила Шурика и Электроника."
    th"Ну эти как обычно!{w} Постоянно их вдвоем вижу.{w} Интересно, а спят они тоже вместе?"
    window hide
    pause (2)
    window show
    "Покончив со своей утренней трапезой, я вышла на крыльцо столовой."
    window hide
    
    scene black with dissolve
    stop ambience fadeout 2
    pause(1)
    
    #Крыльцо столовой
    scene bg ext_dining_hall_near_day with fade
    play ambience ambience_camp_center_day fadein 1
    pause(1)
    window show
    th"Чем бы заняться?"
    th"Точно! Сегодня же самая подходящая погода для купания!{w} Время будить Алису и идти на пляж. Она и так уже проспала все утро."
    "С этой мыслью я побежала к себе в домик."
    window hide
                
    scene black with dissolve
    stop ambience fadeout 2
    pause(1)
    play sound sfx_open_door_1
    
    #В домике
    scene bg int_house_of_dv_day with fade
    play ambience ambience_int_cabin_day fadein 1
    play sound dv_snoring
    pause(1)
    window show
    "Алиса по прежнему лежала на кровати и не думала просыпаться."
    stop sound fadeout 1
    th"Ну сколько можно спать?!"
    "Я подошла и резко хлопнула ее по спине."
    play music music_list["gentle_predator"] fadein 3
    us"Просыпайся! {w}Весь день тут лежать собралась?"
    window hide
    show dv surprise swim with dissolve
    pause(1)
    window show
    us"Нас ждут великие дела!"
    show dv angry swim with dissolve
    dv"Какие ещё великие? {w}Субботник что ли?"
    us"Сегодня воскресенье, тогда уж воскресник."
    show dv normal swim with dissolve
    dv"Ну хорошо, командир, с чего начнём?"
    us"На пляж можно сходить."
    dv"Вчера же там весь день проторчала, не хватило?"
    th"Ну что за глупый вопрос!"
    us"Конечно же нет!"
    dv"Ладно. {w}Дай хоть умыться схожу."
    us"Давай, через десять минут жду здесь."
    stop music fadeout 3
    show dv smile swim with dspr
    dv"Сама не опоздай."
    window hide
    stop ambience fadeout 1
    play sound sfx_open_door_1
            
    scene black with dissolve
    pause(1)
            
    #Дорожка
    scene bg ext_houses_day with fade
    play ambience ambience_camp_center_day fadein 1
    play music music_list["my_daily_life"] fadein 3
    pause(1)
    window show 
    "Чтобы скоротать время перед тем, как Алиса вернется, я решила немного прогуляться."
    th"Странно, что с утра по лагерю ходит очень мало людей.{w} Интересно, где они все пропадают?"
    th"Ну с кибернетиками все ясно - сидят в своем клубе, как затворники какие-то, и мастерят неведомо что. {w}Еще при этом говорят: \"Мы продвигаем вперед науку!\"."
    th"Лучше бы сами хоть куда-нибудь из своей \"обители\" продвинулись, на пляж вот сходили бы..."
    window hide
    
    #Площадь
    scene bg ext_square_day with dissolve
    window show
    th"Слави тоже нигде не видно.{w} Неужели уборка в конце концов ей наскучила?{w} Честно говоря, в это мне верится с трудом."
    th"А все остальные где?{w} Наверняка по домикам сидят. {w}Ну и дурачки! {w}И не скучно им в такую погоду торчать в четырех стенах?"
    th"Впрочем, это их дело.{w} Ладно, пойду назад к домику. {w}Алиса вот-вот должна прийти."
    window hide
    
    #У домика
    scene bg ext_house_of_dv_day with dissolve
    window show
    "Возле домика Алисы не было."
    th"И где она? {w}Десять минут уже прошло!"
    th"Ничего не поделаешь, придется ждать."
    window hide
    pause(1)
    show dv normal pioneer2 far with dissolve
    pause(1)
    window show
    "В скором времени Алиса показалась на дорожке."
    us"Опаздываем, значит?"
    show dv smile pioneer2 with dissolve
    dv"Мне можно."
    us"С чего это?"
    dv"Я же старше тебя буду."
    us"Ох, старушка, значит?"
    show dv smile pioneer2 with dspr
    dv"Старушка и по шее может съездить."
    us"Если догонит."
    "Я рассмеялась и побежала в сторону пляжа."
    window hide
    stop music fadeout 3
    stop ambience fadeout 3
    
    scene black with dissolve
    pause(2)
    
    #Пляж
    scene bg ext_beach_day with fade2
    play ambience ambience_lake_shore_day fadein 3
    play music music_list["reflection_on_water"] fadein 3
    pause(2)
    window show
    "На пляже было довольно тихо.{w} Вдалеке я заметила купающихся Ольгу Дмитриевну и Славю."
    th"Что-то старушка не сильно торопится. {w}Ну ладно, пока что переоденусь."
    window hide
    pause(1)
    show dv normal pioneer2 far with dissolve
    pause(1)
    window show
    "Через несколько минут подошла Алиса." 
    us"И что так медленно?"
    show dv smile pioneer2 with dissolve
    dv"А какая разница? Ведь догнала же."
    us"Всегда у тебя найдётся ответ."
    window hide
    show dv smile swim with dissolve2
    pause(2)
    window show
    "За пару секунд Алиса сбросила с себя пионерский наряд."
    dv"Пойдём лучше купаться!"
    th"Это с радостью!"
    window hide
    
    scene black with dissolve
    play sound sfx_water_emerge
    pause(1)
    
    #В воде
    scene underwater with fade
    pause(1)
    window show
    "Недолго думая, мы с Алисой забежали в воду."
    us"Ныряй за мной!"
    window hide
    play sound sfx_underwater_dive
    pause(2)
    window show
    "Проведя под водой несколько секунд, я вынырнула и легким кролем поплыла дальше.{w} Затем, перейдя на брасс, неспешно продолжила движение параллельно берегу."
    "Не знаю, сколько времени я провела в воде, но об этом времени определенно жалеть не буду."
    "Справа от меня показался остров, именуемый как \"Ближний\"."
    th"Как-нибудь обязательно нужно будет добраться туда вплавь. {w}Но не сейчас. {w}Сейчас, пожалуй, пора бы и на берег."
    play sound sfx_water_emerge
    window hide
    
    #Пляж
    scene bg ext_beach_day with fade
    pause(1)
    window show
    "Через пару минут я вышла из воды и присела на песок, планируя отдохнуть и обсохнуть в лучах солнца."
    "Водяные капли на теле высохли почти сразу, а уже скоро стали сухими и волосы."
    "Освежающая прохлада реки вновь сменилась солнечным зноем, и я решила отправиться в тень одинокого дерева, растущего на берегу."
    "Подойдя к нему, я прилегла, прислонившись головой к стволу и заложив руки за голову."
    th"Обожаю купание!{w} Особенно в такую жаркую погоду, как сейчас."
    "Еще с детства я привыкла проводить лето в деревне, где всегда жара и солнце. {w}Каждый день мы с друзьями ходили на речку, купались, грелись на солнышке, придумывали разные веселые игры."
    "Время тогда летело незаметно, и мы могли часами торчать возле реки до тех пор, пока не наступит ночь."
    th"Да, вот это было круто!{w} Не то, что сейчас!{w} Тут мне, кроме Алисы, и поиграть не с кем.{w} Все какие-то скучные, постоянно заняты чем-то...{w} Но вы же, в конце концов, сюда отдыхать приехали!"
    th"Одна надежда - тот новенький, который должен прибыть сегодня.{w} Вот бы он был не таким занудой, как остальные!"
    th"Ничего, это мы скоро узнаем.{w} До обеда немного осталось."
    window hide
    stop music fadeout 3
    pause(2)
    window show
    "Шум воды клонил в сон."
    "Оборвав все размышления, я на секунду закрыла глаза..."
    window hide
    
    show blink
    pause(3)
    play music music_list["dinner_horn_processed"]
    pause(3)
    window show
    "Меня разбудил звук из динамика."
    th"Как быстро летит время. Я ведь только на мгновение расслабилась, и вот уже раздался сигнал к обеду. {w}Сама не заметила, как уснула."
    window hide
    hide blink
    
    show unblink
    pause(1)
    window show
    "Я открыла глаза и огляделась. {w}Алисы на пляже не было."
    th"Скорее всего, уже ушла вместе со всеми. {w}Ну вот, а меня даже не позвала!"
    "Я быстро переоделась и поспешила в сторону столовой."
    window hide
    scene black with dissolve
    stop ambience fadeout 2
    pause(2)
            
    #Столовая
    scene bg int_dining_hall_people_day with fade
    play ambience ambience_dining_hall_full fadein 1
    pause(1)
    window show
    "Внутри было как всегда полно народу." 
    th"Похоже, я пришла последней."
    "Алиса и Мику о чем-то болтали, сидя за дальним столом."
    th"Ага, вот ты где! {w}Променяла меня на свою синеволосую подружку!"
    th"Ну ничего, я ей еще отомщу. {w}А сейчас мне нужно как следует подкрепиться."
    "Осматривая столовую на предмет незанятых мест, я обнаружила таковое рядом с Электроником."
    show el sad pioneer far  with dissolve
    th"Странно, а где же Шурик? {w}Впрочем, сейчас это не имеет значения, главное - побыстрее занять свободное место."
    show el sad pioneer at center with dissolve
    us"Привет, Сыроежка! {w}Не возражаешь, если я присяду?"
    el"Ну садись, раз уж пришла..."
    "Только сейчас я заметила печальное выражение его лица."
    us"Эй, ты чего грустный такой?"
    show el angry pioneer with dissolve
    el"Во всем виновата твоя подруга ДваЧе!"
    us"Тсс, ты что! {w}Она ведь и услышать может! {w}Ты ведь знаешь, она не любит, когда ее так зовут!"
    show el sad pioneer with dissolve
    el"Знаю я, знаю..."
    us"И что тебе сделала Алиса?"
    el"Я мирно купался в озере, никого не трогал. Тут внезапно ко мне сзади подплыла Двачевская и стащила с меня плавки!"
    "Казалось, Электроник вот-вот расплачется."
    show el upset pioneer with dspr
    el"А потом она выкинула их на буек, представляешь! {w}И мне пришлось добираться за ними вплавь!"
    "Я с трудом сдерживала себя, чтобы в голос не рассмеяться."
    th"Да, такая выходка вполне в духе Алисы. {w}Жалко, что я в тот момент спала, могли бы вместе вдоволь поразвлечься."
    th"Но Электроник, похоже, не разделял моего веселья. {w}Кажется, он здорово обиделся."
    th"Надо бы его как-нибудь подбодрить."
    us"Да ладно тебе! {w}Ну подумаешь один раз над тобой слегка подшутили, ты же ведь не умер! {w}Не стоит строить из этого трагедию."
    show el angry pioneer with dissolve
    el"Слегка?! {w}Подшутили?! {w}Да я... {w}Да мне... {w}Знаешь что! {w}Я с вами больше не разговариваю!"
    hide el with dissolve
    "С этими словами он резко встал и вышел из-за стола."
    th"Какой же он все-таки ранимый! {w}Ну посмотрим, надолго ли его хватит."
    window hide
    pause(2)
    window show
    "Через некотрое время с обедом было покончено, и я покинула столовую."
    window hide
    scene black with dissolve
    stop ambience fadeout 2
    pause(1)
            
    #Крыльцо столовой 
    scene bg ext_dining_hall_away_day with fade
    play ambience ambience_camp_center_day fadein 1
    play music music_list["everyday_theme"] fadein 3
    pause(1)
    window show
    th"Что-то новенького нигде не видать. {w}Наверное, опаздывает."
    th"Кстати, а на чем он вообще приедет?"
    "Собственно, вариант был всего один - на рейсовом автобусе, как и все пионеры."
    "Прийдя к такому заключению, я решила пойти ближе к воротам лагеря и покараулить его там."
    window hide
    
            
    scene black with dissolve
    pause(1)
    
    #Клубы
    scene bg ext_clubs_day with fade
    pause(1)
    window show
    th"Так, теперь нужно найти место, где можно спрятаться и незаметно за ним проследить."
    th"Кусты, ну конечно же!"
    window hide
    play sound sfx_bush_leaves
    pause(2)
    window show
    "Я аккуратно пролезла между ветками, устроилась поудобнее и принялась ждать."
    "На мгновение я представила себя в роли шпиона, посланного на миссию государственной важности."
    th"Итак, моя задача - выследить вражеского диверсанта, намеревающегося проникнуть на территорию базы \"Совенок\"."
    th"Секретный агент Ульяна готова к выполнению операции!"
    th"Главное - не упустить момент!"
    window hide
    show sl normal pioneer far with dissolve
    pause(1)
    window show
    "На дороге показалась Славя. {w}Позади нее виднелись ворота в лагерь. Одна из створок была чуть приоткрыта."
    th"И что она там забыла?.{w} В любом случае будет лучше, если она меня здесь не увидит."
    show sl normal pioneer with dissolve
    "Славя подошла почти вплотную к моему \"укрытию\"."
    th"Только бы не заметила!"
    hide sl with dissolve
    "К счастью все обошлось: пионерка прошла мимо, не обратив ни малейшего внимания."
    window hide
    stop music fadeout 3
    pause(2)
    window show
    "Время шло предательски медленно, и скоро мне наскучило сидеть в ожидании."
    "Посмотрев на землю, я обнаружила в траве огромного зеленого кузнечика.{w} Недолго думая, я накрыла его обеими руками, и через несколько секунд насекомое уже было поймано."
    th"Ага, попался!"
    "Кузнечик бесмомощно прыгал у меня между ладонями и пытался выбраться."
    th"Ну все, теперь никуда не убежишь!"
    window hide
    play sound sfx_open_door_clubs
    show un normal pioneer far with dissolve
    pause(1)
    window show
    "Дверь клубов внезапно открылась, и оттуда вышла Лена.{w} Тут же сама собой родилась идея."
    play sound sfx_bush_leaves
    play music music_list["eat_some_trouble"] fadein 3
    show un normal pioneer with dissolve 
    "Я выскочила из кустов и подбежала к Лене."
    scene d1_grasshopper_1_orika with dissolve
    us"Смотри, что у меня есть!"
    window hide
    scene d1_grasshopper_2_orika with dspr
    pause(0.5)
    scene d1_grasshopper_3_orika with dissolve
    pause(1)
    window show
    "Я взяла кузнечика и начала трясти им прямо у Лены перед лицом."
    un"Ииииии-иии-иииииии!"
    window hide
    scene bg ext_clubs_day
    show un shocked pioneer:
        xalign 0.5 yalign 1.0
        linear 2.0 xalign 2.0
    with dissolve
    pause(1)
    window show
    "Увидев насекомое, Лена в ужасе завопила и убежала в сторону площади."
    th"Ну и лицо же у нее было, такое редко когда увидишь!{w} Надо бы почаще ее пугать!"
    stop music fadeout 3
    "Я уже хотела прятаться обратно в кусты, как вдруг заметила, что со стороны ворот в нескольких шагах от меня стоит какой-то незнакомый парень и наблюдает за мной."
    show pi default coat far with dissolve
    th"Должно быть, это и есть тот самый новенький! Неужели он стоял тут все это время? Как я могла не заметить!"
    "Первое, на что я обратила внимание, это была его одежда, которая явно не соответствовала летней погоде: зимние ботинки, пальто и джинсы."
    th"Он что, на северном полюсе живет?"
    th"Все таки остаться незамеченной мне так и не удалось. {w}Видимо, не выйдет из меня шпиона..."
    th"Миссия провалена, переходим к плану Б!"
    window hide
       
    scene black with dissolve
    pause(1)
    window show
    "Недолго думая, я побежала в сторону площади, оставив незнакомца позади."
    th"Нужно срочно рассказать обо всем Алисе! Думаю, она не меньше меня заинтересуется появлением в нашем лагере нового пионера."
    window hide
    
    #У домика
    scene bg ext_house_of_dv_day with dissolve
    pause(1)
    window show
    "Добежав до нашего домика, я обнаружила, что по прежнему держу в руках того несчастного кузнечика."
    th"Думаю, сейчас самое время отомстить моей соседке за то, что сегодня она ушла на обед без меня."
    window hide
    play sound sfx_knock_door3_dull
    pause(2)
    window show
    "Я постучала в дверь."
    dv"Войдите!"
    th"Нет уж, давай сама выходи!"
    play music music_list["always_ready"] fadein 3
    "Внутри дома послышались шаги, и я уже приготовилась совершить задуманное."
    window hide
    play sound sfx_open_door_1
    show dv normal pioneer with dissolve
    pause(1)
    window show
    "Стоило Алисе открыть дверь, как я тут же раскрыла ладонь с кузнечиком прямо перед ней."
    window hide
    show dv scared pioneer far with dissolve
    play sound dv_scream
    pause(2)
    window show
    "От неожиданности она взвизгнула и отпрыгнула."
    show dv angry pioneer with dissolve
    dv "Ах, чтоб тебя!.."
    "Алиса попыталась схватить меня за руку, но я вырвалась и начала убегать."
    window hide
    
    
    #Площадь
    scene bg ext_square_day
    with dissolve
    show dv angry pioneer far:
        xalign 2.0 yalign 1.0
        linear 3.0 xalign -1.0
    pause(3)
    window show
    "Скоро мы очутились на площади, где я начала бегать по кругу, пытаясь уйти от преследовавшей меня Алисы."
    window hide
    show dv angry pioneer far:
        xalign -2.0 yalign 1.0
        linear 2.0 xalign 0.3
    pause(2)
    window show
    "Вдруг она резко сменила траекторию, бросилась наперерез и ущипнула меня за плечо."
    show dv smile pioneer far 
    with dissolve
    us "Ой! Ну я тебя сейчас…"
    window hide
    show dv smile pioneer far:
        xalign 0.3 yalign 1.0
        linear 2.5 xalign -2.0
    pause(2)
    window show
    "Я развернулась и погналась вслед за убегающей."
    window hide
    pause(2)
    hide dv
    window show
    "Раздался строгий голос со стороны лодочной…"
    sl "Ульяна, хватит бегать!"
    window hide
    show dv grin pioneer far at cleft
    show pi default coat far at right
    show sl angry pioneer far at cright
    with dissolve
    pause(1)
    window show
    "Вдалеке на тропике стояла Славя и тот незнакомец, которого я встретила у клубов."
    sl "Я всё Ольге Дмитриевне расскажу!"
    th"Ну почему чуть что, так сразу я?"
    th"Хотя, пусть рассказывает что хочет. Мы все равно ничего плохого не сделали. {w}Пока."
    us "Есть, гржнинначаник!"
    hide dv with dissolve
    "Тут я заметила, что Алисе под шумок удалось улизнуть."
    th"Вот ведь хитрюга!"
    stop music fadeout 3
    "Недолго думая, я ринулась за ней вдогонку."
    window hide
    
    scene black with dissolve
    pause(1)
    
    #Столовая
    scene bg ext_dining_hall_near_day with fade2
    pause(2)
    show dv normal pioneer with dissolve
    window show
    "Возле столовой я догнала Алису."
    dv "Ну всё-всё, хватит."
    us "Выдохлась что ли? Мало ты спортом занимаешься."
    dv "Хорошо, ты победила."
    us "И выиграла на ужин твой стакан с кефиром!"
    show dv smile pioneer with dspr
    dv "Ага, за шиворот."
    "Я рассмеялась и уселась на крыльцо."
    show dv normal pioneer with dspr
    dv "Что это за парень на площади?"
    us "Новенький. Видела его у клуба."
    dv "Ты его не знаешь?"
    us "Неа."
    dv "А чего он тут со Славей бродит?"
    us "Ольгу Дмитриевну ищут, похоже."
    dv "Наверное…"
    us "Хочешь, сбегаю на разведку?"
    dv "Зачем?"
    us "Интересно же. Странный гражданин. Смотри, как нарядился."
    dv "Давай. Успеешь за ними?"
    us "А то! Скоро буду."
    window hide
    
    #Дорожка
    scene black with dissolve
    pause(2)
    window show
    th"Если этот новоиспеченный пионер собирается к домику вожатой, мне необходимо его опередить, чтобы успеть подслушать их разговор."
    "Не раздумывая, я тут же направилась туда."
    window hide
   
    #Домик ОД снаружи
    scene bg ext_house_of_mt_day with fade
    pause(1)
    window show
    "Поначалу все шло хорошо, как вдруг..."
    show mt angry pioneer with dissolve
    mt"Ульяна! А ну ка стой!"
    "Я послушно остановилась."
    th"Ну что на этот раз?{w} Почему почти каждая моя встреча с вожатой начинается с того, что меня за что-то отчитывают?"
    us"Да, Ольга Дмитриевна?"
    mt"И только не надо делать вид, что ты ни в чем не виновата!"
    us"Но что я сделала?"
    th"Действительно, а что я такого сделала?"
    mt"Ты Лену чуть до слез не довела этим своим насекомым!"
    th"Ах, это... {w}Ты смотри, уже пожаловаться успела! Ну я ее..."
    show mt angry pioneer close with dissolve
    mt"Идем ка со мной в домик!"
    "Ольга Дмитриевна взяла меня за руку и потащила за собой."
    th"Похоже, сопротивление бесполезно."
    window hide
   
    #В домике ОД
    play sound sfx_open_door_1
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_mt_day with fade
    show un normal pioneer far at left
    pause(1)
    window show
    "В домике нас уже ждала эта вечно унылая девочка."
    "Пожалуй, с ней мне было ладить труднее, чем с кем-либо другим из нашего отряда. {w}Мы с ней как две противоположности."
    window hide
    show mt normal pioneer with dissolve
    pause(1)
    window show
    mt"А теперь, Ульяна, извинись перед Леной за свою выходку."
    us"Но я лишь показала ей кузнечика, только и всего!{w} Ее проблемы, что она насекомых боится."
    th"Не понимаю, как можно вообще их бояться. {w}Они ведь нисколечки не опасны."
    show mt angry pioneer  with dissolve
    mt"Не все в этом лагере любят насекомых, и ты это прекрасно знаешь. {w}Не выпущу тебя на улицу, пока не попросишь прощения!"
    show un shy pioneer far at left with dspr
    un"Ольга Дмитриевна, может, не стоит?"
    show un surprise pioneer far at left with dissolve
    mt"Еще как стоит!"
    show un normal pioneer far at left with dissolve
    th"Похоже, другого выхода у меня нет. Придется побороть себя."
    us"Лена, извини... {w}Я так больше не буду."
    show un smile pioneer far at left with dspr
    un"Хорошо, я прощаю тебя."
    show mt smile pioneer with dissolve
    mt"Вот видишь, Ульяна, какие у нас добрые девочки в отряде.{w} Не то что ты со своими шалостями."
    th"Ну как всегда, Ульяна во всем виновата, Ульяна - главная злодейка. {w}Не удивлюсь, если на наш лагерь вдруг упадет метеорит, в этом сразу же начнут обвинять меня."
    mt"Ладно, девочки, вы свободны, идите отдыхайте."
    show mt normal pioneer with dspr
    mt"И хватит издеваться над Леной."
    th"Да-да-да..."
    window hide 
    stop ambience fadeout 1
    
    play sound sfx_open_door_1
    scene black with dissolve
    pause(1)
    
    #У домика ОД
    scene bg ext_house_of_mt_day with fade
    play ambience ambience_camp_center_day fadein 1
    pause(1)
    window show
    "Я поспешила поскорее уйти из домика, Лена вышла вслед за мной."
    
    "..."
    fbt "Ну вот и всё!"
    window hide
    stop ambience fadeout 2
    scene black with dissolve
    pause (2)
    jump slavyana_mod__launcher0

#Сделано Андреем Хромовым и FireBoTer'ом