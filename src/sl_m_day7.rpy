label slavyana_mod__day7:
  stop music
  stop sound
  stop ambience
  $ backdrop = "days"
  $ new_chapter(7, u"Славя. День седьмой")
  $ save_name = (u'Славя. День седьмой')
  $ day_time()
  $ persistent.sprite_time = "day"
  $ renpy.pause(3, hard=True)

  play music music_list["forest_maiden"] fadein 3
  scene ext_polyana_day with dissolve
  "Когда я проснулась, на меня смотрел Семён."
  "Перед глазами пронеслись события прошлой но…"
  th "Так, стоп! Это было днём."
  if persistent.sl_m_hen_txt:
    scene cg d7_sl_morning_2 with dissolve
  else:
    show pi normal pioneer close at center with dissolve
  sl "Доброе утро!"
  me "Доброе! Хорошо спалось?"
  sl "Лучше, чем когда-либо."
  me "Мне тоже."
  "Я потянулась к нему и поцеловала."
  "Это был нежный поцелуй, какой делают каждый день все влюблённые."
  "Казалось, время остановилось."
  "Я отпустила его."
  sl "Надо бы позавтракать."
  me "Да, пожалуй."
  sl "Сколько сейчас времени, не знаешь?"
  me "Нет, но, думаю, ещё рано."
  sl "Надеюсь, столовую уже открыли, а то я есть ужас как хочу."
  me "И я."
  scene black with dissolve
  stop music fadeout 3
  "Мы собрали вещи и направились в сторону лагеря, взявшись за руки."
  scene bg int_dining_hall_day
  show pi normal pioneer at center
  with dissolve
  play ambience ambience_dining_hall_empty loop fadein 3
  "Мы оказались сегодня первыми посетителями столовой."
  "Завтрак был довольно простой, но что делать, если приходится кормить сразу несколько отрядов?"
  me "Знаешь, мне здесь еда никогда не нравилась."
  sl "Мне тоже, по правде говоря."
  "Я рассмеялась."
  me "Но поскольку выбора нет… {w} Да и с голодухи весьма неплохо идёт."
  sl "Да, это точно!"
  "Семён ел немного неосторожно, то и дело обливаясь чаем и роняя кашу."
  sl "Ты всегда так ешь?"
  me "А фто такое?"
  "Сказал он с набитым ртом."
  "Я снова рассмеялась."
  "Когда он прожевал, то всё-таки ответил."
  me "А… Нет, не всегда. Но когда очень голодный, то бывает. {w} Правда я могу и покультурнее."
  sl"Да ладно, ничего страшного."
  "Вскоре мы доели завтрак и направились к выходу."
  show pi normal pioneer:
    linear 1.0 xalign 0.255
  show mt normal pioneer at cright with dissolve
  "Но тут же встретились с Ольгой Дмитриевной."
  show mt surprise pioneer at cright with dspr
  mt "А, это вы… {w} Ну, я не буду спрашивать, где вы ночевали… {w} В общем, это…"
  show mt sad pioneer at cright with dspr
  "Вожатая была явно смущена."
  "Она с нами даже не поздоровалась, и я решила ей об этом напомнить."
  sl "И вам доброе утро, Ольга Дмитриевна."
  "И как можно невинней улыбнулась."
  mt "Да, утро… утро… {w} Ладно, вы, главное, не забудьте собраться."
  sl "Не забудем!"
  stop ambience fadeout 2
  scene bg ext_dining_hall_away_day
  show pi normal pioneer at center
  with dissolve
  play ambience ambience_ext_road_day loop fadein 3
  me "А что она имела в виду? Опять какой-то поход?"
  sl "Да нет же! {w} Сегодня последний день, ты разве забыл?"
  stop ambience
  play music music_list["meet_me_there"] fadein 3
  me "Последний день чего?"
  sl "Последний день смены!"
  show pi shocked pioneer at center with dspr
  "Его глаза заметались."
  me "Как? Почему?.."
  sl "А что ты удивляешься? Ты разве не знал? На линейке же объявляли."
  me "Нет…"
  sl "Теперь знаешь!"
  "Я улыбнулась."
  me "И что делать?.."
  sl "В смысле?"
  show pi normal pioneer at center with dspr
  me "Да ладно, ничего… {w} И когда отъезд?"
  sl "Вечером, часов в пять-шесть."
  show pi smile pioneer at center with dspr
  me "Ну, времени ещё полно!"
  sl "Да, но у меня дела кое-какие. {w} К тому же надо Женю найти, а то она, наверное, волновалась, что меня ночью не было."
  sl "На обеде увидимся!"
  "Я поцеловала его в щёчку и поспешила, чтобы всё успеть до обеда."
  stop music fadeout 3
  play ambience ambience_ext_road_day loop fadein 3
  scene bg ext_houses_day with dissolve
  pause 2
  scene bg ext_house_of_sl_day with dissolve
  pause 2
  stop ambience fadeout 1
  play sound sfx_open_door_1
  scene bg int_house_of_sl_day with dissolve
  play ambience ambience_int_cabin_day loop fadein 3
  "Внутри домика было пусто. Скорее всего, Женя ушла к себе в библиотеку."
  "Во-первых, надо бы сходить помыться."
  "Я взяла с собой полотенце и направилась в баню."
  scene black with dissolve
  stop ambience fadeout 1
  "…"
  play ambience ambience_int_cabin_day loop fadein 3
  scene bg int_house_of_sl_day with dissolve2
  "Вернувшись, я переоделась в новую форму, хоть до отъезда оставалось меньше 6 часов."
  "До обеда оставалось около 10 минут, так что я решила сделать заметку в своём дневнике, т.к. не успела за эти два дня."

#Дневник:
  th"Четырнадцатый день в «Совёнке». Последний. Не верится, что за эти прекрасные 14 дней произошло столько всего интересного. И как жаль, что уже пора покидать это чудное место, в котором я встретила новых друзей, отдохнула от домашних забот {w}, и, что самое главное, нашла своё счастье."
  th"Но время идёт, и я надеюсь, что мы с ним обязательно встретимся снова в этом лагере, а может быть и за его пределами. А этот дневник поможет мне вспомнить почти все самые яркие моменты."

  th"Конечно же, надо будет взять дневник с собой."
#Конец дневника

  play sound sfx_dinner_horn_processed
  "Пора на обед."
  stop ambience fadeout 1
  scene black with dissolve
  "…"
  scene bg ext_dining_hall_away_day with dissolve
  play ambience ambience_ext_road_day loop fadein 3
  show un normal pioneer at right with dissolve
  "Дойдя до столовой, я встретила Лену, которая сидела на лавочке."
  "Я поздоровалась с ней и зашла в столовую."
  stop ambience fadeout 1
  scene bg int_dining_hall_people_day
  show pi normal pioneer at cright
  show us normal pioneer at cleft
  with dissolve
  play music music_list["i_want_to_play"] fadein 1
  "За одним столом с Семёном сидела Ульяна."
  "Я взяла свой поднос с едой и подошла к ним."
  sl "Можно к вам?"
  us "Ладно, я уже ухожу."
  "Ульянка вскочила и убежала в другой конец столовой."
  stop music fadeout 3
  play ambience ambience_dining_hall_full loop fadein 3
  hide us with dissolve
  sl "О чём разговаривали?"
  me "Ну, ты же её знаешь, о чём с ней можно разговаривать?"
  "Я улыбнулась."
  me "Разобралась с делами?"
  sl "Да! Теперь я полностью свободна. Могу помочь тебе собраться."
  me "Да что мне собирать-то…"
  sl "Ну, тогда можешь помочь собраться мне."
  me "Хорошо."
  "Вскоре мы закончили и отправились к моему домику."
  stop ambience fadeout 1
  scene black with dissolve
  pause 1
  play sound sfx_open_door_1
  scene bg int_house_of_sl_day
  show pi normal pioneer at cright
  with dissolve
  play ambience ambience_int_cabin_day loop fadein 3
  "Я достала сумку."
  "У меня было очень много вещей с собой."
  "Я открыла шкаф и принялась собирать вещи в сумку."
  me "А какие у тебя планы после лагеря? Что делать собираешься?"
  sl "Ну как же…"
  "Я повернулась к нему и улыбнулась."
  sl "Пойду учиться."
  me "Ну… Да…"
  sl "А ты?"
  me "Я? Ну, наверное, тоже."
  me "Хотя… Мне не очень хочется возвращаться в родной город."
  sl "Почему?"
  stop ambience
  play music music_list["trapped_in_dreams"] fadein 3
  me "Потому что… Потому что там нечего делать, там ничего нет, и там меня никто не ждёт."
  sl "А родители?"
  me "Ну, родители… {w} Понимаешь ли… Их как бы сейчас нет."
  th "Из приюта что ли?"
  sl "А где они?"
  me "Работают за границей, так сказать."
  sl "Так тебе повезло!"
  "Я попыталась приободрить его."
  me "Почему?"
  sl "Заграничные вещи разные и всё такое."
  me "Ну в любом случае…"
  sl "Не расстраивайся!"
  me "По этому поводу я и не расстраиваюсь."
  sl "А что тогда?"
  me "Много всего…"
  sl "Например?"
  me "Ну, например…"
  play sound sfx_open_door_1
  show mz normal glasses pioneer at cleft with dissolve
  "Семён недоговорил, потому что в этот момент дверь распахнулась и в дом вошла Женя."
  mz "Ага, вот вы где."
  sl "Да, как раз собираемся."
  show mz laugh glasses pioneer at cleft with dspr
  mz "Вижу-вижу… Хорошо, что я не пришла минут на десять попозже, а то могла бы помешать… «сборам»."
  "Моя соседка поставила меня в очень неловкое положение."
  "Я попыталась отвлечься запихиванием вещей в сумку, но они не умещались."
  mz "Ну что, герой-любовник?"
  me "Что?"
  "Абсолютно равнодушным тоном ответил ей Семён."
  show mz normal glasses pioneer at cleft with dspr
  mz "Да ничего…"
  mz "Смотри! Теперь от твоего выбора зависишь не только ты."
  play sound sfx_close_door_1
  hide mz with dissolve
  "И Женя вышла."
  sl "Что она имела в виду?"
  me "По-моему, этого никогда точно знать нельзя."
  sl "Но всё же."
  me "Ну… Понимаешь, я сам хотел с тобой об этом поговорить."
  sl "О чём?"
  me "Просто вот сегодня мы уезжаем, так?"
  sl "Так."
  me "И разъедемся по своим городам."
  sl "Ну да."
  me "И когда я смогу тебя увидеть в следующий раз?"
  th "А ведь действительно. Мы разъедемся, и будем заняты своими делами. Возможно, мы даже больше никогда не увидимся после этого. И это печально."
  sl "Не знаю…"
  me "Вот и я не знаю…"
  sl "Но ты можешь писать мне письма!"
  "Я улыбнулась, чтобы снова приободрить его."
  me "Да, конечно, но это не то, ты сама понимаешь."
  sl "А что тогда?"
  me "Может быть, я поеду с тобой?"
  th "Такой вопрос поставил меня в тупик."
  sl "И что ты там будешь делать? {w} Учёба, родители… {w} Да и что люди скажут?"
  show pi angry pioneer at cright with dspr
  me "Ну, всегда можно найти выход!"
  sl "Какой же?"
  me "Придумаем!"
  sl "Семён, нам ещё мало лет для такого…"
  me "И что?"
  sl "Может быть, позже…"
  me "Через сколько? Через год? Два? Пять?"
  th "Похоже, я действительно обидела его."
  sl "Ты так говоришь… {w} Я не знаю…"
  me "То есть всё, что было,  - это так, курортный роман?"
  sl "Нет! Конечно, нет! Просто…"
  me "Что?"
  sl "Я сейчас не готова об этом говорить. Давай попозже."
  me "Когда попозже? У нас осталось пару часов до отъезда."
  "Я ничего не ответила и продолжала собирать вещи."

  if words_red:
    show pi normal pioneer at cright with dspr
    me "Слушай, я всё-таки не понимаю."
    sl "Чего?"
    me "Почему ты не хочешь…"
    sl "А как ты себе это представляешь?"
    me "Ну, я могу найти работу, снять квартиру."
    me "А что ты умеешь? У тебя хотя бы аттестат есть?"
    me "Это не самое главное!"
    sl "Почему же!"
    me "Если есть цель, то можно преодолеть любые препятствия! {w} Тем более, они не настолько серьёзные."
    sl "Это тебе так кажется."
    me "Может и так. Но я всё равно не понимаю, почему ты на всё это так реагируешь! {w} Ведь если мы просто разъедемся, то это всё, конец…"
    sl "Я этого не говорила."
    me "Но ведь и так понятно."
    sl "Да с чего ты это взял?!"
    "Уже закричала я."
    me "Хорошо, поставим вопрос по-другому -  я просто не хочу ехать к себе, где я там живу… {w} И общаться с тобой только письмами или по телефону, надеясь на случайную встречу."
    sl "Для меня это тоже будет тяжело."
    "И это правда."
    me "Ну, а в чём тогда проблема?"
    sl "Понимаешь, не всё зависит от нас…"
    me "А от кого же тогда?!"
    sl "Есть нормы общества, законы, мораль и этика, в конце концов."
    me "Да при чём тут это-то, я никак понять не могу?!"
    sl "Если для тебя это не так важно, то важно для меня."
    me "Хорошо. {w} Я готов даже вести себя так, как положено по этим твоим нормам, но ведь есть и что-то более важное."
    sl "Может быть… Но я не могу вот так сразу…"
    me "У тебя не так много времени для раздумий. {w} Могу предложить только себя… {w} Потому что больше у меня ничего нет."
    me "Более того, я не знаю, что будет со мной через час, но зато точно уверен, что, как бы там ни было, начинать с чистого листа я хочу именно с тобой!"
    sl "Ты всё так красиво говоришь, но, представь, каково мне! {w} Если для тебя всё так просто, то у меня есть и своя жизнь, к которой я привыкла, и вот так сразу всё менять…"
    "Семён сказал шёпотом что-то невнятное, но кажется это было…"
    me  "У меня тоже когда-то была…"
    sl "Что?"
    me "Я говорю, что это неизбежно. {w} Перемены – это часть жизни, без них никуда."
    th "А ведь он прав, как ни крути. Но сейчас передо мной стоит трудный выбор между моей личной жизнью и его."
    th "И раз он жертвует всем ради меня, то и я должна тоже, ради него."
    "Я подсела к нему."
    sl "Ладно, я тебе верю. Раз ты так говоришь, то так и будет!"
    "Мы просидели молча ещё какое-то время, но я взглянула на часы, на которых время поджимало."
    sl "Пора."
    "Прошептала я ему."
    me "Да, точно. {w} Ты иди на остановку, а я сейчас сбегаю в домик к вожатой, возьму свои вещи."
    sl "Какой ты неорганизованный! Надо было заранее собраться."
    "Рассмеялась я."
    me "Да мне собирать-то…"
    stop music fadeout 3
    play ambience ambience_int_cabin_day loop fadein 3
    play sound sfx_close_door_1
    hide pi with dissolve
    "Он выскочил из домика."
    "А я направилась к остановке."
    scene black with dissolve
    "…"

  if words_green or words_blue:
    me "Ты думаешь, только для тебя это всё сложно!"
    sl "Думаю, что и для тебя непросто, но ты так почему-то не считаешь."
    me "А если я тебе скажу, что мне совсем некуда возвращаться, что у меня, начиная с прошедшего понедельника, больше нет никакой жизни, и мне всё равно придётся начинать всё с начала?"
    sl "Не знаю… {w} Это не звучит правдоподобно."
    me "А и не должно! Но всё же это правда."
    sl "И что же… Ну, объясни тогда."
    me "Я попал в этот лагерь совершенно случайно! {w} Вообще, я из другого времени, может быть, из другого мира."
    me "Из начала XXI века."
    me "И лет мне несколько больше, чем кажется."
    me "Я совершенно не знаю, как здесь оказался."
    if words_blue:
      th "А ведь это всё может быть правдой. Но всё настолько бредово, что поверить в это почти невозможно, особенно без доказательств."
      th "Хотя окажись я в такой же ситуации, как говорит Семён, первым делом я бы пыталась выяснить у окружающих, что происходит и как я сюда попала."
    th "Мне кажется Семён пытается придумать такие обстоятельства, решение которых будет невозможно для нормальной жизни."
    sl "И зачем ты всё это говоришь?"
    me "Чтобы ты понимала моё положение."
    sl "Но это же… {w} Это звучит просто глупо…"
    me "Конечно! Я на твоём месте отреагировал бы точно так же."
    sl "И что ты от меня ждёшь?"
    show pi normal pioneer at cright with dspr
    me "Не знаю… {w} Я просто почувствовал необходимость признаться."
    sl "Я не говорю, что ты врёшь, и психом тебя не считаю, но пойми, я не могу в это вот так поверить."
    me "Да, понимаю… {w} Я думал просто, что это поможет тебе понять мою ситуацию и мотивацию моих поступков."
    sl "Не помогло, если честно."
    "Он вздохнул."
    sl "И мнение моё не изменилось."
    me "Но?.."
    sl "Тебе лучше собрать свои вещи, а то опоздаешь."
    me "Да там…"
    sl "Потом поговорим."
    play sound sfx_close_door_1 
    hide pi with dissolve
    "Он вышел, оставив меня наедине с моими мыслями."
    stop music fadeout 3
    play ambience ambience_int_cabin_day loop fadein 3

  if words_green:
    th "Семён ведёт себя как маленький ребёнок."
    "Да, мне тоже не хочется расставаться, и мне очень грустно, что смена заканчивается, но нельзя же в погоне за мной увязываться в другой город."
    "Тем более как он говорит, в родном городе его никто не ждёт . Ну как такое может быть?"
    "Он готов испортить свою жизнь ради… {i}меня{/i}?"
    "Но это же абсурдно! Просто глупо!"
    "Я ему не позволю. Пусть думает, что я пока что на него обиделась."

  if words_blue:
    th "Он поступает очень необдуманно и эгоистично."
    "В погоне за счастьем, он готов отречься от прошлого. {w} И всё ради… {i}меня{/i}?"
    th "Это очень мило с его стороны. Но нельзя так поступать! Даже ради меня."
    "Эх, надо уже что-то решать… {w} И я решила!"
    "Я собрала сумку, вышла из домика и направилась к остановке, предварительно заперев его."

  play ambience ambience_ext_road_day loop fadein 3
  scene ext_bus with dissolve
  "На остановке уже собрались пионеры и приехал автобус."
  "Но нигде не было видно вожатой, а Семён скоро должен был подойти."
  scene black with dissolve
  "…"
  "Наконец они пришли."
  scene cg d7_pioneers_leaving with dissolve
  stop ambience
  play music music_list["memories"] fadein 2
  mt "Все собрались?"
  "Начала Ольга Дмитриевна."
  mt "Сегодня вы покидаете наш лагерь, и на прощание мне хотелось бы вам кое-что сказать."
  "Она заметно нервничала и никак не могла подобрать нужные слова."
  mt "Надеюсь, что время, проведённое здесь, вам запомнится на всю жизнь, что у вас останутся только приятные воспоминания о «Совёнке»."
  mt "Также я надеюсь, что здесь вы стали чуточку лучше, смогли чему-то научиться, познакомились с новыми друзьями… {w} В общем, возвращайтесь в следующем году!"
  "Вожатая отвернулась."
  "Да, в такой момент было трудно сдержать слёзы."
  "Я буду очень скучать."
  stop music fadeout 3

  if words_green or words_blue:
    scene ext_bus
    show pi normal pioneer at cright
    with dissolve
    "Ко мне подошёл Семён."
    me "Давай сядем вместе."
    sl "Давай."

  play ambience sfx_bus_interior_moving loop fadein 2
  scene bg int_bus_people_night with dissolve
  "Автобус мчался вперёд. Пейзажи сменяли друг друга."

  if words_green:
    "Уже несколько часов мы сидели рядом, а попытки завязать разговор заканчивались односложными фразами."
    stop ambience
    play music music_list["a_promise_from_distant_days"] fadein 2
    me "Не бери в голову то, что я тогда сказал! Я не хочу оправдываться или говорить, что это неправда. {w} Просто для меня сейчас самое главное - это ты."
    sl "Я понимаю."
    me "Если я даже иногда веду себя не так, делаю и говорю глупости…{w} Всё равно для меня сейчас самое главное – быть с тобой! И всегда будет."
    me "Я понимаю, что вёл себя слишком опрометчиво, строил глупые прожекты. Но мы можем попробовать сделать всё по уму. Вместе! Ты и я!"
    sl "Ты понимаешь, что это будет непросто? И что нельзя вот так, очертя голову, бросаться в омут? Ведь проблем будет столько, что не разгребёшь."
    me "Да, теперь понимаю! {w} Но ради тебя я на всё готов."
    th "Помирились."
    "Я поцеловала его в щёчку и положила голову ему на плечо."

  if words_red or words_blue:
    "И всё у нас было хорошо."
    "От яркого лунного света было светло, как днём. Деревья принарядились в серые цвета."
    "Мы с Семёном сидели на последнем ряду и разглядывали впереди сидящих пионеров."
    "Ульянка бегала по салону и громко кричала. {w} Лена читала книжку, а Алиса спала."

  if words_red:
    "Я решила прервать наше с Семёном молчание."
    stop ambience
    play music music_list["farewell_to_the_past_edit"] fadein 2
    sl "О чём думаешь?"
    me "О жизни."
    sl "И как думается?"
    me "Замечательно!"
    "Я тихо рассмеялась."
    me "Знаешь…"
    "Автобус покачивало, и меня невольно клонило в сон."
    sl "Давай потом, что-то меня укачало. {w} Я посплю, если ты не возражаешь."
    me "Да, конечно!"
    "Я положила голову ему на плечо."
  
  if words_blue:
    stop ambience
    play music music_list["a_promise_from_distant_days"] fadein 2
    me "Не бери в голову то, что я тогда сказал! Я не хочу оправдываться или говорить, что это неправда. {w} Просто для меня сейчас самое главное - это ты."
    sl "Я понимаю."
    me "Если я даже иногда веду себя не так, делаю и говорю глупости…{w} Всё равно для меня сейчас самое главное – быть с тобой! И всегда будет."
    me "Я понимаю, что вёл себя слишком опрометчиво, строил глупые прожекты. Но мы можем попробовать сделать всё по уму. Вместе! Ты и я!"
    sl "Ты понимаешь, что это будет непросто? И что нельзя вот так, очертя голову, бросаться в омут? Ведь проблем будет столько, что не разгребёшь."
    me "Да, теперь понимаю! {w} Но ради тебя я на всё готов."
    "Я поцеловала его в щёчку и положила голову ему на плечо."
  
  show blink
  pause 1
  scene black
  "А потом я тихо заснула."
  stop ambience
  stop music fadeout 1
  "…"

  if sl_m_Full:
      jump slavyana_mod__epilogue
  jump slavyana_mod__launcher0