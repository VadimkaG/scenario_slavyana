init python:
  # Условие, если славя ходила за шуриком
  go_to_sh = False
  # Славя сказала правду лене, когда они очищали костер
  sl_m_day5_cleaning_told_truth = False
  # В медпункте свалить вину на семена
  sl_m_day5_make_semen_guilty = False

label slavyana_mod__day5:
  stop music
  stop sound
  stop ambience
  $ backdrop = "days"
  $ new_chapter(5, u"Славя. День пятый")
  $ save_name = (u'Славя. День пятый')
  $ day_time()
  $ persistent.sprite_time = "day"
  $ renpy.pause(3, hard=True)
  
  scene black
  if go_to_sh:
    scene bg int_mine
    call pomehi
    with dissolve
    play music music_list["sunny_day"] fadein 3
    "Я шла вдоль шахты. {w} В одиночку."
    "У меня был фонарик, но он светил очень тускло, что я еле разбирала дорогу впереди."
    "Эта шахта была очень похожа на ту, в которую мы спустились с Семёном в поисках Шурика."
    "Разве что тоннель был длиннее."
    "В одиночку идти было очень страшно."
    "Вдруг что-то пробежало мимо меня, и я посветила в ту сторону {w} но никого не было."
    "Я шла дальше, и мне казалось, что я слышу голоса. Но никого рядом не было."
    scene bg int_mine_crossroad
    call pomehi
    with dissolve
    "Я дошла до развилок и пошла в левую сторону {w} но быстро дошла до тупика, заваленного камнями."
    scene cg d4_uv_1
    call pomehi
    with dissolve
    "Луч фонаря бегло пробежался по стене и мне показалось, что я видела девочку… С хвостом!"
    "Однако она быстро убежала."
    scene bg int_mine_halt
    call pomehi
    with dissolve
    "Я пошла назад."
    th"Это не может быть правдой! Похоже, что я сплю."
    "Но вдруг мои ноги подкосились, и я упала. Чьи-то руки подхватили меня и осторожно положили."
    stop music fadeout 2

  else:
    "Мне снился сон."
    "Очень яркий и насыщенный. Но хоть убей, не могу вспомнить."
    "Помню только, что было страшно и был огонь."
    "Я даже не помню, где это было."
    "От этого я резко проснулась."

  scene bg int_house_of_sl_day with dissolve
  play ambience ambience_int_cabin_day loop fadein 3
  "Так начался двенадцатый день моего пребывания в «Совёнке»."
  
  if go_to_sh:
    "Часы показывали половину восьмого."
    "Даже если бы я прямо сейчас вышла на пробежку, я бы, скорее всего, опоздала на линейку."
    "Поэтому я оделась в пионерскую в форму, завязала галстук на воротнике и пошла на площадь."

  else:
    "Время 6:30. Как раз хорошее время для пробежки!"
    "Я надела спортивный костюм и вышла из домика."

    play sound sfx_close_door_1

    scene bg ext_house_of_sl_day with dissolve
    "Мой маршрут проходил от домика по площади, {w} затем вдоль пляжа до пристани, {w} от неё к административному корпусу {w} и далее к клубам с крюком к моему домику."
    scene black with dissolve
    stop ambience fadeout 1
    "…"
    scene ext_washstand_day with dissolve
    play ambience ambience_camp_center_day loop fadein 3
    "Добежав до умывальников, я умылась и побежала дальше."
    scene bg ext_houses_day with dissolve
    pause 1
    scene bg int_house_of_sl_day
    show mz normal pioneer
    with dissolve
    play sound sfx_open_door_1
    play ambience ambience_int_cabin_day loop fadein 3
    "К этому моменту Женя уже проснулась, и надо было собираться на линейку."
    "Я быстро переоделась, и мы вместе направились к площади."

  stop ambience
  scene black with dissolve
  pause 1

  scene bg ext_square_day with dissolve
  play ambience ambience_camp_center_day loop fadein 3
  "Бо́льшая часть пионеров уже собралась, пока остальные ещё подтягивались."
  "И вот, когда все собрались, я окинула взглядом пришедших."

  if go_to_sh:
    "Пришла даже Двачевская! {w} Но нигде не было Семёна."
  else:
    "Пришла даже Двачевская и Шурик! {w} Но нигде не было Семёна."

  th "Видимо, отсыпается после похода."
  scene cg d2_lineup with dissolve
  stop ambience
  play music music_list["my_daily_life"] fadein 3
  "Линейка началась с традиционного приветствия вожатой и наставлений на правильный, коммунистический путь."
  "Сегодняшний план включал в себя: уборку помещений, дежурство Мику в столовой и уборку на поляне перед вечерним костром."
  "В прошлый четверг тоже был костёр и ничего выдающегося он из себя не представлял: небольшая прогулка по лесу с остановкой на поляне."
  "Также Ольга Дмитриевна упомянула в своей речи пропажу Шурика и то, как Семён храбро отправился на его поиски."
  if go_to_sh:
    "Я, конечно, тоже участвовала, но решила не напоминать ей об этом, тем более в присутствии других пионеров."
  mt "Линейка окончена."
  scene bg ext_square_day with dissolve
  stop music fadeout 2
  play ambience ambience_camp_center_day loop fadein 3
  "С этими словами пионеры направились в столовую."
  show mt normal pioneer with dissolve
  mt "Славя, можешь подойти на минуточку?"
  mt "В честь возвращения Шурика, запланировано испечь торт, и мне потребуется твоя помощь."
  mt "Надо будет собрать земляники и принести мешок с мукой из библиотеки, остальные ингредиенты я поручу кое-кому."
  mt "Можешь пойти с кем-нибудь вместе, чтобы тебе было удобней."
  th "Например с Семёном или Леной."
  sl "Хорошо."
  stop ambience fadeout 1
  scene black with dissolve
  pause 1

  scene bg ext_dining_hall_near_day
  show un normal pioneer
  with dissolve
  play ambience ambience_camp_center_day loop fadein 3
  "У столовой я встретила Лену."
  sl "Привет."
  un "Привет."

  menu:
    "Напомнить Лене":
      sl "Ольга Дмитриевна решила испечь торт в честь спасения Шурика и поручила мне собрать земляники. Мы можем сходить вместе, а по пути ещё кого-нибудь найдём."
      "Я решила быть честной."
    "Не напоминать":
      un "Тебе Ольга Дмитриевна что-нибудь говорила?"
      sl "Насчёт чего?"
      un "Ну, насчёт земляники."
      "Я никогда не умела врать, да и сейчас это выглядело бы очень явно."
      sl "Да, говорила."
      un "Тогда вместе пойдём, ты же не против?"
      sl "Конечно, я тебе вчера как раз предлагала погулять вместе."
  show un smile pioneer with dspr
  un "Хорошо."
  "Она улыбнулась, и мы вошли в столовую."

  stop ambience fadeout 1
  scene bg int_dining_hall_people_day
  show un normal pioneer
  with dissolve
  play ambience ambience_dining_hall_full loop fadein 3
  "Сегодняшний завтрак состоял из риса с мясом, пары булочек и чая."
  sl "Приятного аппетита."
  un "Спасибо."
  sl "Я тут подумала… Может, ещё позовём с собой Семёна?"
  show un surprise pioneer with dspr
  un "Куда?"
  "Похоже, она очень удивилась."
  sl "За земляникой, конечно же."
  show un shy pioneer with dspr
  un "А… Н-ну да, можно."
  "Она покраснела."
  sl "Ладно, я тогда пойду. У меня ещё дела есть, а за земляникой после обеда пойдём. Как раз за корзинками схожу."
  "Я попрощалась с Леной и вышла из столовой."

  stop ambience fadeout 2
  scene bg ext_dining_hall_near_day with dissolve
  play ambience ambience_camp_center_day loop fadein 3

  if go_to_sh:
    "Раз я не успела побегать до линейки, то займусь этим прямо сейчас."
    "По плану сейчас уборка в клубах, но если побегу сейчас, то не успею. Но если сократить маршрут, то успею помочь Мику."
    "Если, конечно, не появится новых поручений от вожатой."
    stop ambience fadeout 1
    scene black with dissolve
    pause 1
    scene bg ext_house_of_sl_day with dissolve
    play ambience ambience_camp_center_day loop fadein 3
    "Переодевшись, я набросала себе в уме примерный маршрут: от моего домика в лес, затем мимо умывальников. Заскочу к Мику, помогу ей и вернусь к себе."
    "Как раз к обеду управлюсь."
    stop ambience fadeout 1
    scene black with dissolve
    "…"
    scene bg ext_washstand_day with dissolve
    play ambience ambience_camp_center_day loop fadein 3
    "Выбегая из леса, у умывальников я заметила опоздавшего на завтрак пионера, но не сразу определила, кто это."
    "Подбежав поближе, он обернулся и я узнала в нём…"
    show tl pioneer far with dissolve
    th "Да это же Толик!"
    sl "Привет, а почему ты на завтрак опоздал? Я уж было подумала, ты там ночуешь."
    tl "Проспал. Есть хочу."
    sl "Пойдём, я тебе столовую открою, обжора."
    tl "Хорошо."
    stop ambience fadeout 1
    scene black with dissolve
    pause 1
    scene bg ext_dining_hall_near_day
    show tl pioneer far
    with dissolve
    play ambience ambience_camp_center_day loop fadein 3
    th "Обычно Толя никогда не пропускал приём пищи."
    stop ambience fadeout 1
    scene bg int_dining_hall_day
    show tl pioneer normal
    with dissolve
    play ambience ambience_dining_hall_empty loop fadein 3
    "Я открыла ему дверь и вошла в столовую вместе с ним."
    "Я зашла на кухню и принесла ему остатки от завтрака: пару булочек, треугольник кефира и что-то, напоминавшее творожную запеканку."
    sl "Вот, всё что осталось. Не опоздай на обед."
    sl "Тебя же и на линейке не было, ты в курсе, что сегодня опять будет костёр?"
    tl "Запеканка."
    sl "Точно."
    stop ambience fadeout 1
    scene black with dissolve
    pause 1
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day loop fadein 3
    "Возня с Толиком заняла у меня слишком много времени, поэтому я бегом направилась в музыкальный кружок."
    stop ambience fadeout 1
    scene black with dissolve
    pause 1
    play sound sfx_open_door_2
    play ambience ambience_music_club_day loop fadein 3
    scene bg int_musclub_day
    show mi normal pioneer
    with dissolve2
    sl "Привет Мику, помощь нужна?"
    show mi smile pioneer with dspr
    mi "Привет. Славечка! Да я, вот, уже заканчиваю, но можешь помочь. Осталось помыть полы в подсобке и протереть инструменты. Я уже начала протирать, так что тебе остались струнные, барабаны и рояль. Подсобкой я займусь сама."
    mi "В углу стоит ведро, там же и тряпки."
    hide mi with dissolve
    "Сказала Мику и зашла в подсобку."
    "Сначала я протёрла рояль и его клавиши, которые отозвались мелодичными звуками."
    "Дальше я приступила к остальным инструментам."
    "Где-то через 20 минут я закончила и, отчитавшись Мику, в темпе отправилась домой."

  else:
    "Сейчас по плану уборка в клубах, пойду помогу кибернетикам навести порядок в их «логове»."
    stop ambience fadeout 1
    scene black with dissolve
    pause 1
    scene bg ext_clubs_day with dspr
    play sound sfx_knock_door2
    play ambience ambience_camp_center_day loop fadein 3
    "Подойдя к зданию клубов, я постучалась."
    play sound sfx_open_door_clubs
    play ambience ambience_clubs_inside_day loop fadein 3
    scene bg int_clubs_male_day
    show sh normal pioneer at cleft
    show el normal pioneer at cright
    with dissolve
    "Зайдя внутрь, я заметила, что Саша и Серёжа даже не приступали к уборке."
    el "Привет, Славя, зачем пожаловала?"
    sl "Ольга Дмитриевна на линейке говорила вам про уборку."
    el "Ну да, ну ты разве не видишь, что мы немного другим заняты?"
    sh "Тем более, это непростой беспорядок… {w} Это творческий беспорядок. Так нам лучше думается."
    sl "Ребят, ну нельзя же работать в таком бардаке! Тем более - ваши же инструменты и детали разбросаны по всему столу. Вы их хотя бы рассортируйте. Да и полы бы не помешало помыть."
    sl "А уж что у вас на складе творится - это совсем кошмар."
    sl "Я и так пришла вам помочь."
    el "Ладно, Шурик, быстрее управимся – быстрее продолжим работу."
    sh "Согласен."
    "Шурик тут же отложил в сторону паяльник и стал сгребать детали в кучу."
    "Электроник взял из подсобки вёдра и отправился за водой, а я принесла швабры."
    "После этого Электроник принялся протирать полы в основном зале, а я в подсобке."
    scene bg int_clubs_male2_night with dissolve
    "Пришлось поднять довольно много разного хлама, и не только хлама, чтобы навести чистоту на всём «складе». Шурик помог расставить всё по местам."
    stop ambience fadeout 1
    scene black with dissolve
    pause 1
    play ambience ambience_camp_center_day loop fadein 3
    scene bg ext_clubs_day with dissolve
    "Наконец мы закончили и кибернетики снова вернулись к своему делу."
    scene bg ext_square_day
    show us normal pioneer far at left
    with dissolve
    "Навстречу мне шла Ульяна. Она, не поздоровавшись, двигалась к клубам."
    hide us with dspr
    "А я решила сходить на волейбольную площадку."
    "Обожаю волейбол, жаль что времени для него часто нет."
    stop ambience fadeout 1
    scene black with dissolve
    "…"
    scene bg int_house_of_sl_day with dissolve
    play ambience ambience_int_cabin_day loop fadein 3
    "Я забежала к себе домой и переоделась в спортивный костюм."
    stop ambience fadeout 1
    scene black with dissolve
    pause 3
    scene bg ext_square_day with dissolve
    play ambience ambience_int_cabin_day loop fadein 3
    scene bg ext_dining_hall_away_day with dissolve
    pause 1
    scene bg ext_playground_day with dissolve
    "На футбольном поле уже резвились малыши, а у волейбольной сетки какие-то неизвестные мне пионеры собирались для игры."
    "Я попала в команду к 2 мальчикам и 1 девочке."
    "Против нас играла команда, полностью состоящая из мальчиков."
    stop ambience fadeout 1
    scene black with dissolve
    "…"
    play ambience ambience_soccer_play_background loop fadein 3
    scene bg ext_playground_day with dissolve
    "Соперники играли довольно хорошо, но и наша команда старалась изо всех сил." 
    "Сыграв 1 раунд, мы, в конце концов, смогли свести игру практически в ничью, проигрывая всего на одно очко."
    show un normal sport far with dissolve
    "На площадке для бадминтона я увидела Лену, которая несколько раз старалась подбросить воланчик, но у неё никак не получалось."
    sl "Привет."
    un "Привет, а что, уже обед?"
    sl "Нет, но скоро будет. После него пойдём за земляникой."
    show un smile sport far with dspr
    un "Хорошо."
    "Она улыбнулась, и мы договорились встретиться на площади."
    stop ambience fadeout 1
    scene black with dissolve
    "…"

  scene bg int_house_of_sl_day with dissolve
  play ambience ambience_int_cabin_day loop fadein 3
  "Забежав домой, я уже достала форму и корзинки..."
  play sound sfx_knock_door3_dull
  "Как вдруг в дверь кто-то постучал."
  sl "Войдите."
  play sound sfx_open_door_1
  show dv normal pioneer2 with dissolve
  "Как ни странно, ко мне пожаловала сама Двачевская."
  sl "Привет. Что-то хотела?"
  show dv laugh pioneer2 with dspr
  dv "Да. Тут такое дело…"
  "Она указала на спину своей рубашки."
  dv "Мне бы форму новую, старая в стирке."
  sl "Сейчас."
  show dv normal pioneer2 with dspr
  "Я улыбнулась. Хоть на этот раз у неё никаких злых намерений ко мне!"
  "Я открыла шкаф и принялась искать форму для Алисы."
  "Здесь было всё необходимое: юбки, шорты, рубашки, кумачовые галстуки, плащи на случай дождя, палатка на случай длительного похода (который не предполагается в последние дни). {w} И даже военный камуфляж от папы."
  "Рубашку пришлось искать на глазок."
  "Пока я искала, Алиса заметила корзинки и решила начать беседу."
  dv "За грибами собираешься?"
  sl "За ягодами поплывём на остров. Ольга Дмитриевна поручила собрать."
  dv "Ты не одна поедешь?"
  sl "Мы с Леной договорились. Может, ещё кто присоединится."
  "Я улыбнулась и продолжила искать рубашку."
  dv "Давайте я помогу вам!"
  th "А вот этого в мои планы не входило!"
  sl "Да не надо, мы сами справимся."
  th "Наверняка очередную проделку задумала и нам помешает."
  "Подумала я."
  show dv smile pioneer2 with dspr
  dv "Всё равно мне делать нечего. Да и на остров посмотреть хочу."
  "Она продолжала настаивать."
  show dv normal pioneer2 with dspr
  sl "Да не стоит, спасибо. Мы как-нибудь сами."
  "Но мой голос выдавал меня."
  "Вот чего я точно не хотела, так это видеть Двачевскую с нами на одном острове."
  dv "Ну как знаешь."
  "Ответила она ехидно."
  sl "Вот."
  "Я протянула ей рубашку."
  "Она взяла её и направилась к выходу."
  sl "А старую форму?"
  dv "Потом занесу."
  hide dv with dspr
  play sound sfx_close_door_1
  "Сказала она и вышла на улицу."
  th "И не занесёт ведь…"
  stop ambience fadeout 1
  scene black with dissolve
  pause 1

  play ambience ambience_camp_center_day loop fadein 3
  scene bg ext_houses_day with dissolve
  "Переодевшись, я пошла в сторону площади. Скоро уже должен был начаться обед."

  scene bg ext_square_day
  show un normal pioneer far
  with dissolve
  if go_to_sh:
    "Я подошла к Лене, и мы вместе направились в столовую."
  else:
    "На площади, как мы и условились, я встретила Лену."

  stop ambience fadeout 1
  scene black with dissolve
  "…"
  play ambience ambience_dining_hall_full loop fadein 3
  scene bg int_dining_hall_people_day
  show un normal pioneer at cleft
  with dissolve
  "Зайдя в столовую, я обнаружила свободные места с Семёном."
  show pi normal pioneer at cright with dspr
  sl "Можно?"
  "Я улыбнулась."
  me "А? {w} Да, конечно!"
  "Он встал и выдвинул стул передо мной."
  "Я положила лукошки под стол."
  un "Приятного аппетита…"
  me "И тебе."
  "Сегодня на обед давали гороховый суп и рыбу с картофельным пюре."
  "Четверг же, рыбный день."
  sl "Семён, есть какие-нибудь планы на день?"
  me "Нет."
  sl "Тогда не хочешь с нами прокатиться на лодке до острова?"
  me "Зачем?"
  sl "Ольга Дмитриевна просила земляники собрать. Там её много, и она такая вкусная!"
  "Наверное, по моему лицу в этот момент можно было прочувствовать весь вкус земляники."
  me "Земляника… {w} А зачем?"
  sl "Не знаю, но, по-моему, идея отличная!"
  th "Знаю конечно, но пусть для Семёна это будет сюрпризом. {w} Был бы он на линейке, про всё бы знал."
  me "Да, пожалуй."
  "Я вытащила из под стола лукошки, и мы дружно отправились к пристани."
  play ambience ambience_camp_center_day loop fadein 3
  scene bg ext_dining_hall_away_day
  show un normal pioneer at cleft
  show pi normal pioneer far at right
  with dissolve
  "Я шла вместе с Леной, а Семён традиционно для него витал в облаках."
  "Болтать было особо не о чем, так что до пристани мы дошли практически в тишине."
  scene bg ext_square_day
  show un normal pioneer at cleft
  show pi normal pioneer far at right
  with dissolve
  pause 2
  play ambience ambience_boat_station_day loop fadein 3
  scene bg ext_boathouse_day
  show un normal pioneer at cleft
  show pi normal pioneer at right
  with dissolve
  "Через десять минут мы уже стояли на пристани."
  sl "Вот лодка. {w} Подожди, я сейчас за вёслами схожу."
  hide un
  hide pi
  with dspr
  "Я направилась к домику станции."
  show un normal pioneer at cleft
  show pi normal pioneer at right
  with dspr
  "Взяв вёсла, я вернулась  к ним."
  sl "Вот!"
  "Я протянула ему вёсла."
  me "Ага… Да…"
  stop ambience fadeout 1
  scene cg d5_boat with dissolve
  play music music_list["everyday_theme"]
  "Мы забрались в лодку, и, отвязав её, Семён забрался в неё, оттолкнул от берега и начал грести."
  me "А куда именно плыть?"
  sl "Вон туда!"
  "Я указала на остров Ближний."
  th "И кто, интересно, решил его так обозвать?"
  sl "Остров Ближний."
  me "Вас понял!"
  "Пока Семён грёб воду вёслами, я успела заметить, что лодку немного шатает из стороны в сторону."
  me "А что… {w} Земляника больше нигде не растёт? {w} Я имею в виду места более доступные."
  sl "Но там она самая вкусная."
  "Я попыталась изобразить удивление."
  un "Тебе, наверное, тяжело одному грести?"
  me "Да нет… {w} Нормально…"
  "Остаток пути мы перешёптывались с Ленкой о мелочах."
  stop music fadeout 3
  play ambience ambience_boat_station_day loop fadein 3
  "Наконец мы приплыли."
  scene bg ext_island_day
  show un normal pioneer at cleft
  show pi normal pioneer at right
  with dissolve
  "Отсюда открывался красивый вид на остров. Немудрено, что это излюбленное место Лены."
  sl "Держи."
  "Я протянула Семёну корзинку."
  sl "Нам бы надо разделиться, так быстрее управимся."
  me "Да, наверное."
  show un surprise pioneer with dspr
  un "Но корзинки-то только две."
  sl "Да, точно, это я недоглядела!"
  un "И как мы разделимся?"

  menu:
    "Пойти с Семёном":
      $ sl_m_lp += 1
      me "Одна корзинка у меня, одна - у вас; всё очевидно."
      sl "Нет, давай я с тобой пойду!"
      "Я улыбнулась."
      show pi smile pioneer at right with dspr
      me "Давай…"
      th "Мне показалось, или в его глазах мелькнула искра радости?"
      hide un with dspr
      "Лена не стала спорить и пошла одна."
      stop ambience fadeout 1
      scene black with dissolve
      "…"
      play music music_list["timid_girl"] fadein 3
      scene bg ext_island_day
      show pi normal pioneer
      with dissolve
      "Чтобы было удобнее, мы оба несли корзинку, по пути собирая ягоды."
      "Мы заглядывали под каждый кустик в поисках ягодок."
      "Правда Семён всё же часто их пропускал или втихую поедал."
      sl "Внимательнее!"
      me "А, да… Извини."
      sl "Ничего."
      "Я улыбнулась."
      me "Тебе, наверное, здесь нравится? {w} Ты ведь любишь природу."
      sl "Конечно!"
      "Я снова улыбнулась."
      sl "Напоминает о доме – у нас там такие же красивые берёзы."
      "Я посмотрела в сторону лагеря и представила себе пейзаж моей деревни. Вот стоят соседние дома. Во дворе нашего домика небольшой огород, а рядом резвятся мальчишки."
      "А недалеко от нас расположился лесок с берёзками. И солнышко светит."
      me "Слушай, давно хотел спросить – а чем ты вообще увлекаешься?"
      me "А то целыми днями занята – кажется, времени на отдых совсем не остаётся."
      sl "Ну…"
      th "Никогда об этом не задумывалась. Всегда находятся какие-нибудь задания или поручения."
      sl "Не знаю даже. {w} Для меня отдых – это смена вида деятельности."
      me "Нет, это понятно, но всё же?"
      "Я вспомнила, чем занималась вчера, чтобы скоротать время."
      sl "Я вышивать люблю и вязать! {w} Вот…"
      "Я достала платочек, на котором вышивала вчера перед приходом Жени."
      "Он был весь в разноцветных цветочках."
      me "Очень мило."
      sl "Спасибо! {w} Давай я его тебе подарю!"
      "Семён смутился."
      me "Да не стоит…"
      "Это предложение вызвало не такую реакцию, которую я ожидала."
      sl "Нет, бери!"
      "Он ещё раз посмотрел на платочек и положил его себе в карман."
      me "Спасибо…"
      stop music fadeout 1
      scene black with dissolve
      "…"
      play ambience ambience_boat_station_day loop fadein 3
      scene bg ext_island_day
      show pi normal pioneer
      with dissolve
      "Через полчаса корзинка наполнилась до краёв."
      me "Ну, видимо, всё…"
      sl "Да. {w} Набрали немало, этого с запасом хватит."
      "Когда мы вернулись к лодке, Лена ещё не подошла."
      sl "Ей одной больше времени надо, чтобы полную корзинку собрать."
      me "Да, наверное…"
      "Семён задумался и посмотрел в сторону реки."
      sl "О чём думаешь?"
      me "Ни о чём… {w} А ты?"
      sl "А я… {w} Что будет, когда закончатся каникулы? Придётся вернуться домой, покинуть лагерь…"
      sl "Увижусь ли я когда-нибудь со всеми, с кем сегодня познакомилась?"
      th "Вот он тот самый момент!"
      sl "Увижусь ли я когда-нибудь с тобой?.."
      show un normal pioneer at cright with dissolve
      show pi normal pioneer:
        linear 1.0 xalign 0.255
      "Неожиданно из леса вышла Лена."
      un "Ой, а вы уже тут… Вот."
      "В руках у неё была полная корзинка земляники."
      sl "Отлично! {w} Теперь можно отправляться назад."

    "Я и сама могу":
      me "Давай я пойду с тобой."
      "Он обратился к Лене."
      un "Давай…"
      sl "Вот и славно!"
      "Я взяла вторую корзинку и пошла в дальнюю часть острова, чтобы на середине встретиться и вместе вернуться к лодке."
      stop ambience fadeout 1
      scene black with dissolve
      "…"
      play ambience ambience_boat_station_day loop fadein 3
      scene bg ext_island_day with dissolve
      "Мне не составило труда собрать корзину земляники."
      th "Как там дела у Семёна и Лены?"
      "Я решила позвать их."
      sl "Семён! Лена!"  
      show un normal pioneer at cleft
      show pi normal pioneer at right
      with dissolve
      "Сквозь листву виднелись две фигуры в белом с красными галстуками. Я подошла к ним."
      sl "И как улов?"
      "Я посмотрела в корзинку и Семён вздохнул."
      sl "Что-то негусто…"
      sl "Ладно, нам и этого хватит! {w} Пора возвращаться!"
      "Мы направились к лодке."

  stop ambience fadeout 2
  scene black with dissolve
  pause 1
  play ambience ambience_boat_station_day loop fadein 3
  scene bg ext_boathouse_day
  show un normal pioneer at cleft
  show pi normal pioneer at right
  with dissolve
  "Путь обратно занял гораздо меньше времени."
  show pi normal pioneer at right:
    linear 1.0 ypos 1.0
  "Семён пришвартовал лодку и обессиленно рухнул на землю."
  "Мы склонились над ним."
  hide pi
  sl "Если тебе было так тяжело, то сказал бы!"
  "У меня был некоторый навык гребли на лодке."
  un "Да…"
  me "Да нет, ничего… {w} Сейчас полежу и всё пройдёт…"
  sl "Ладно, тогда отнеси корзинки, пожалуйста, Ольге Дмитриевне, а то у нас ещё дела есть."
  me "Да, конечно."
  "Я поставила корзинки рядом с ним, и мы отправились вместе с Леной дальше."
  un "А у нас есть ещё какие-то дела?"
  "Спросила она меня пройдя некоторое расстояние"
  sl "Да, надо принести мешок с мукой из библиотеки. Одна я не справлюсь, ты же поможешь?"
  un "Ну конечно!"  
  un "Но неужели мы сами потащим этот мешок?"
  sl "Можно прикатить тележку со склада."
  "И мы отправились на склад."
  stop ambience fadeout 1
  scene black with dissolve
  "…"
  play music music_list["sweet_darkness"] fadein 3
  scene bg ext_houses_day
  show un normal pioneer
  with dissolve
  "На полпути к библиотеке, Лена вдруг решила уточнить у меня, откуда взялась мука в библиотеке."
  sl "Не знаю, но ты можешь спросить это у Жени, если тебе так интересно." 
  show un laugh pioneer with dspr
  "Она рассмеялась."
  show un smile pioneer with dspr
  mt "Девочки!"
  show un smile pioneer:
    linear 1.0 xalign 0.255
  show mt normal pioneer panama at cright with dspr
  "Внезапно нас окликнула Ольга Дмитриевна."
  mt "Спасибо вам, что собрали землянику. Семён передавал вам благодарность, за то, что выполнили за него всю работу."
  "Видимо она так шутит."
  show mt smile pioneer panama at cright with dspr
  mt "Шучу конечно, но Семён действительно благодарил вас. {w} И ещё, чуть не забыла. Раз он не слишком устал после сбора ягод, я направила его собирать ингредиенты для…"
  show mt normal pioneer panama at cright with dspr
  un "Ольга Дмитриевна, Славя мне уже сказала, зачем."
  show mt grin pioneer panama at cright with dspr
  mt "А, ты уже вкурсе. Ну ладно, тебе можно. В общем, я снимаю с вас поручение и перекладываю на вас новое."
  mt "Скоро ужин, а после него костёр. Надо, чтобы кто-нибудь убрался на поляне."
  mt "Ещё какие-нибудь вопросы?"
  sl "Ольга Дмитриевна, Семён действительно устал после гребли, может всё же кто-то другой займётся?"
  show mt normal pioneer panama at cright with dspr
  mt "А кто? Все заняты. Тем более пионер ведь всегда готов."
  sl "Ладно…"
  mt "Вот и хорошо, а у меня ещё дела. Торопитесь!"
  stop music fadeout 3
  play ambience ambience_camp_center_day loop fadein 3
  hide mt with dspr
  "Ольга Дмитриевна куда-то убежала."
  sl "Надо вернуть тележку."
  un "Потом вернём, успеем."
  sl "Ну хорошо."
  "А меня вновь посетила мысль пропустить костёр и сходить на пляж."

  $ cclothes_after_cleaning = False;

  menu:
    "Переодеться до уборки костра":
      sl "Лен, ты тогда иди пока что, я тебя догоню. Мне сейчас надо в домик зайти и кое-что взять."
      un "Хорошо."
      hide un with dspr
      "Лена ушла, и я поспешила в свой домик."
      scene bg int_house_of_sl_day with dissolve
      pause 2
      call slavyana_mod__day5_change_clothes

    "После уборки костра":
      $ cclothes_after_cleaning = True;
  jump slavyana_mod__day5_change_clothes_after

label slavyana_mod__day5_change_clothes:
  scene bg ext_house_of_sl_day with dissolve
  if cclothes_after_cleaning:
    "Переодевшись, я вышла из домика."
  else:
    "Переодевшись, я вышла из домика и отправилась за своей подругой."
  scene bg ext_square_day
  show pi normal pioneer far
  with dissolve
  "На площади я встретила Семёна."
  "Он был ко мне спиной, так что я позвала его."
  show pi normal pioneer with dspr
  sl "Как продвигается?"
  me "Что?"
  sl "Поиски ингредиентов."
  me "А, ты уже знаешь…"
  sl "Да!"
  me "Нормально…"
  th "Я заметила какой-то выпирающий предмет у него под майкой."
  sl "А что у тебя там?"
  me "А это…"
  "Он засмущался."
  show pi smile pioneer with dspr
  me "Да так, ничего особенного…"
  "Он как-то странно захихикал."
  me "Мне пора…"
  hide pi with dspr
  "И он быстро куда-то улизнул в сторону домиков."
  th "Что это было?"
  return

label slavyana_mod__day5_change_clothes_after:
  scene black with dissolve
  "…"
  
  play ambience ambience_forest_day loop fadein 3
  scene bg ext_path_day
  show un normal pioneer
  with dissolve
  "По пути к костровой поляне, я встретила Лену, идущую туда."
  sl "Не успела?"
  un "Д-да."
  
  scene bg ext_polyana_day
  show un normal pioneer far
  with dissolve
  "Придя на место, мы принялись расчищать кострище и собирать мусор, который набросали пионеры в прошлый раз."
  th "Настоящие пионеры так себя не ведут!"
  "Несмотря на большое количество хлама, мы довольно быстро закончили."
  "Образовавшуюся тишину прервала Лена."
  show un normal pioneer with dspr
  un "Славя, давно хотела спросить: что ты думаешь о Семёне?"
  stop ambience
  play music music_list["you_lost_me"] fadein 3
  "Такой вопрос меня очень удивил."
  sl "В каком смысле думаю?"
  un "Ну вот в смысле твоего к него отношения.{w=0.5}{nw}"
  show un laugh pioneer with dspr
  play sound sfx_scary_sting
  extend "{i}Нравится{/i} ли он тебе?"
  sl "Лен, это личные вопросы…"
  un "А я так не думаю. {w=0.5}{nw}"
  show un evil_smile pioneer with dspr
  extend "Я же вижу как ты на него смотришь и не стесняешься."

  if sl_m_lp < 4:
    jump slavyana_mod__day5_lena_lie

  menu:
    "Соврать":
      jump slavyana_mod__day5_lena_lie
    "Сказать правду":
      pass

label slavyana_mod__day5_lena_true:
  $ sl_m_day5_cleaning_told_truth = True
  sl "Я ещё точно не знаю, не уверена, но… наверное. А почему ты интересуешься?"
  show un shy pioneer with dspr
  un "Да нет, просто…"
  "Она засмущалась.  Неожиданно."
  un "Просто я тоже люблю его и хотела узнать твоё к нему отношение."
  "Да, я конечно замечала, что Лена иногда ведёт себя необычно, но чтобы любовь..."
  un "Заметно, что Семён отвечает тебе взаимностью, поэтому не буду вам мешать. Мы же всё-таки подруги."
  play sound sfx_scary_sting
  show un evil_smile pioneer with dspr
  un "{i}Пока{/i}."
  show un normal pioneer with dspr
  
  "Дальше мы шли молча."
  scene bg ext_path_day
  show un normal pioneer
  with dissolve
  pause 1
  scene bg ext_square_day
  show un normal pioneer
  with dissolve
  un "Ладно, я пойду. Удачи тебе."
  show un smile pioneer with dspr
  un "Не бери себе в голову то, что я там наговорила. Давай останемся подругами."
  "Она улыбнулась."
  sl "Пустяки. Удачи тебе."
  hide un with dspr
  "Она ушла."
  jump slavyana_mod__day5_lena

label slavyana_mod__day5_lena_lie:
  sl "Никак я на него не смотрю. С чего ты взяла?"
  un "Ну да, ты ещё врать будешь."
  sl "Нет."
  show un rage pioneer with dspr
  un "После этого ещё подругой называешься. Даже мне правду в глаза не можешь сказать!"
  sl "Леночка, успокойся."
  un "Я спокойна. Но помни, что я за вами слежу."
  sl "Да, ты права, мне нравится Семён, но с чего ты это взяла?"
  un "Да потому что я вижу, как вы часто бываете вместе. Я уже давно обо всём догадалась."
  if persistent.slavyana_mod__day5_bad_end:
    sl "Не нужно ссориться из-за одного мальчика, пусть он сам решит, с кем он хочет быть. Я как раз после костра собиралась на пляж сбежать."
    "Она не отвечала."
    sl "Лена?"
  hide un with dspr

label slavyana_mod__day5_lena:
  stop music fadeout 2
  play ambience ambience_camp_center_day loop fadein 3

  if cclothes_after_cleaning:
    scene black with dissolve
    "…"
    call slavyana_mod__day5_change_clothes
  "До ужина оставалось ещё некоторое время. Поэтому я решила зайти к себе в домик, чтобы записать в свой дневник сегодняшние события."
  stop ambience fadeout 1
  scene black with dissolve
  pause 1
  play ambience ambience_int_cabin_day loop fadein 3
  play sound sfx_open_door_1
  scene bg int_house_of_sl_day with dissolve

#Дневник:
  if go_to_sh:
    "Двенадцатый день в Совёнке. Сегодня не произошло чего-то столь же масштабного, как поиски Шурика."
  else:
    "Двенадцатый день в Совёнке. Сегодня не произошло чего-то столь же масштабного, как пропажа Шурика." 
  
  "В честь его чудесного спасения Ольга Дмитриевна решила испечь торт (не сама, конечно же), для этого пришлось собрать земляники на острове Ближний, куда нас с Леной отвёз Семён. Остальные ингредиенты так же таскал Семён."
  "Ещё нам на линейке объявили об очередном костре. Я уже была на этом мероприятии в прошлый раз и ничего удивительного он из себя не представлял: пешая прогулка по лесу и остановка на заранее подготовленной поляне. Однако, каждый раз Оля говорила о взаимовыручке и о том, чему мы научимся в этом походе. В этот раз я постараюсь отпроситься, ну или, в крайнем случае, по-тихому исчезнуть. Осталось только собрать сумку." 
  "Также в лесу случился очень странный разговор с Леной. Как я поняла, она нашла во мне соперницу в отношениях с Семёном. Надеюсь, она не слишком обиделась. Её реакция поистине напугала меня."
#*Конец дневника*

  th "Когда вернусь, допишу."
  play sound sfx_dinner_horn_processed
  stop ambience fadeout 1
  scene black with dissolve
  "…"
  play ambience ambience_camp_center_day fadein 3
  scene bg ext_square_day
  show un normal pioneer
  with dissolve
  "На площади я встретила Лену, вместе с которой мы отправились на ужин."
  stop ambience fadeout 1
  play ambience ambience_dining_hall_full fadein 3
  scene bg int_dining_hall_people_day
  show pi normal pioneer at cleft
  show un normal pioneer at cright
  with dissolve
  "Зайдя в столовую, я заметила Семёна, сидящего одного и прикрывшего голову руками."
  sl "Что с тобой?"
  me "Ничего…"
  sl "Устал?"
  me "Да, есть немного…"
  th "Небось тяжёло ему было. Бедненький."
  sl "Это плохо."
  me "Ещё бы…"
  sl "Ты же помнишь, что после ужина мы все в поход идём? Уже собрался?"
  show pi shocked pioneer at cleft with dspr
  "Семён резко встрепенулся."
  me "Чего? Куда?"
  sl "Поход…"
  "Я удивилась его реакции."
  sl "Ты не знал?"
  show pi normal pioneer at cleft with dspr
  me "Нет…"
  "Он снова опустил голову и прикрыл её руками."
  "Мы приступили к еде."
  "На ужин давали ту же рыбу с пюре как и в обед."
  show pi normal pioneer:
    linear 1.0 xalign 0.5
  show un normal pioneer:
    linear 1.0 xalign 0.9
  show mt grin pioneer far at left with dissolve
  "Через некоторое время из дальнего угла столовой донёсся громкий голос Ольги Дмитриевны:"
  mt "Ребята! {w} В честь чудесного спасения нашего друга и товарища, Шурика, мы приготовили для вас этот торт!"
  "Я обернулась, но вокруг него уже столпились пионеры."
  mt "Сейчас… Сейчас…"
  sl "Пойдём! {w} А то без нас съедят!"
  "Я мотивировала свои слова улыбкой."
  un "Пойдём."
  me "Да, конечно…"
  "Когда мы подошли к толпе пионеров, Оля как раз поставила торт на середину стола."
  mt "А теперь…"
  stop ambience fadeout 2
  play music music_list["awakening_power"] fadein 3
  scene cg d5_cake_alt with dissolve
  "Вожатая не успела закончить, как через толпу пионеров проскочила Ульянка, которая обеими руками ухватилась за торт. {w} Она даже успела его кое-где надкусить."
  "Ольга Дмитриевна как могла оттащила её, пока на них глядела ехидная Алиска, а Лена слизывала крем с торта."
  "Ульянка упиралась и визжала."
  scene bg int_dining_hall_people_day with dissolve
  show mt rage pioneer at center 
  show us normal pioneer at right 
  with dissolve
  mt "Ульяна! Это уже переходит все границы!"
  show us sad pioneer at right  with dspr
  us "Я… {w} Я…"
  th "И как она вообще додумалась до такого?!"
  "Неожиданно в их разговор вмешался сам виновник торжества – Шурик."
  show sh normal pioneer at left  with dissolve
  sh "Да ладно вам, Ольга Дмитриевна! Раз уж торт в мою честь, то ничего страшного…"
  "Он замялся."
  show mt angry pioneer at center  with dspr
  mt "Неважно!"
  mt "А ты… {w} Тебя я сегодня накажу по-настоящему, чтобы в следующий раз знала!"
  show us dontlike pioneer at right  with dspr
  "Она обратилась к Ульяне."
  us "Ради бога!"
  "Она фыркнула и отвернулась."
  mt "Сегодня с нами в поход не идёшь!"
  us "Да больно надо было!"
  "Вполне заслуженное наказание. Хотя бы в этот раз поход пройдёт удачно, без Ульянкиных пакостей."
  stop music fadeout 3
  play ambience ambience_dining_hall_full fadein 3
  hide sh  with dissolve
  "Пионеры стали потихоньку расходиться."
  play ambience ambience_camp_center_day fadein 3
  scene bg ext_dining_hall_near_day with dissolve
  "Я вышла из столовой и пошла собираться."
  play sound sfx_open_door_1
  play ambience ambience_int_cabin_day fadein 3
  scene bg int_house_of_sl_day with dissolve
  "Собирать было ничего не нужно, но я оставила у себя в домике заранее заготовленную сумку с полотенцем, тапочками и прочим."
  
  if not sl_m_day2_go_with_sp:
    "Когда я собиралась закрыть домик, то взглянула на стол,{w} где лежали мои вожатские ключи."
    "Откуда они здесь взялись? Видимо принёс кто-то."
  
  play ambience ambience_camp_center_day fadein 3
  scene bg ext_house_of_sl_day with dissolve
  play sound sfx_close_door_1
  "Я закрыла домик и пошла на площадь."
  scene bg ext_square_day with dissolve
  "Вечерело."
  stop ambience fadeout 3
  play music music_list["lightness"] fadein 3
  "На площади уже собралась приличная толпа пионеров. Почти что все были здесь{w}, разве что Ульянка не пришла."
  show mt normal pioneer far with dspr
  mt "Вроде все на месте… Отлично!"
  "Ольга Дмитриевна начала стандартную речь про поход, настоящих пионеров и взаимовыручку."
  "В прошлый раз было то же самое, так что я уже запомнила её речь."
  mt "...Всему этому нам с вами предстоит научиться!"
  "По толпе пионеров прошёл недобрый шёпот."
  show mt normal pioneer far with dspr
  mt "Идти будем парами. {w} Так что если вы ещё не выбрали себе партнёра, сейчас самое время!"
  "Пионеры начали быстро группироваться по двое."
  show mt normal pioneer with dspr
  "Я подошла к вожатой, чтобы отпроситься."
  sl "Оля, я, пожалуй, в этот раз пропущу костёр. Можно?"
  show mt surprise pioneer with dspr
  mt "Но почему? Это же общелагерное мероприятие."
  sl "Мне надо побыть одной сегодня, что-то голова слегка побаливает. Просто знайте: если что - я пойду к себе в домик отлежаться."
  show mt normal pioneer with dspr
  mt "Ох, ну ладно. Я на тебя рассчитываю, как на образцового пионера."
  sl "Конечно, Ольга Дмитриевна."
  show mt normal pioneer far with dspr
  "Пионеры уже разбились по парам. Чтобы не смущать Лену, я встала в начале строя с Ольгой, а вот моей соседке напарника не досталось."
  "Но потом ей выделили Семёна."
  mt "Вперёд!"
  "Скомандовала вожатая."
  stop music fadeout 3
  play ambience ambience_forest_day fadein 3 
  scene bg ext_path_day with dissolve
  "Разговаривать было решительно не о чем. Но надо было хоть как-то скрасить прогулку до поляны."
  "Некоторое время мы просто прогуливались по кругу"
  "Через 10-20 минут мы всё-таки пришли в назначенное место."
  $ persistent.sprite_time = "sunset"
  scene bg ext_polyana_sunset 
  with dissolve
  #show mt normal pioneer at center with dissolve
  #hide mt with dissolve
  play music music_list["dance_of_fireflies"] fadein 3
  "И всё-таки не зря вожатая водит пионеров именно сюда. Вечером здесь невероятно красиво."
  "Мальчиков отправили искать дрова для костра."
  "Я решила порасспрашивать своих знакомых из отряда."
  show un normal pioneer with dissolve
  "Я подсела к Лене."
  sl "Привет. Нравится поход?"
  un "Да."
  sl "О чём поболтаем?"
  un "Ой, я, наверное, пойду, не до тебя сейчас. Ты только не обижайся."
  hide un with dspr
  th "Видимо, не в настроении."
  show mi normal pioneer with dissolve
  "Затем я подсела к Мику."
  sl "Привет. Как всё проходит?"
  show mi dontlike pioneer with dspr
  mi "Никак. Я забыла гитару, а Ольга Дмитриевна не дала за ней сходить… Может быть, если бы я попросила тебя, она разрешила, а так не разрешает."
  sl "Жалко. Я бы обязательно послушала, как ты играешь."
  show mi smile pioneer with dspr
  mi "Спасибо. {w}{nw}"
  show mi sad pioneer with dspr
  extend "Но это слабое утешение."
  show el normal pioneer at right with dspr
  "Ко мне подошёл Электроник."
  el "Славя, можешь у Алисы зажигалку попросить? Ольга Дмитриевна просила для костра, а мы спички не взяли."
  sl "Хорошо, сейчас."
  hide mi
  hide el
  with dspr
  scene black with dspr
  pause 0.5
  scene bg ext_polyana_sunset
  show dv normal pioneer
  with dspr
  sl "Слушай, у тебя зажигалки не будет?"
  show dv smile pioneer with dspr
  dv "Прикурить дать?"
  th "Спасибо, но я, в отличие от тебя, не курю."
  sl "Нет, костёр развести. Шурик с Электроником забыли взять спички."
  show dv normal pioneer with dspr
  dv "А почему она у меня должна быть?"
  "Она прищурилась."
  "Такой вопрос поставил меня в тупик."
  sl "Не знаю… Вдруг есть, я у всех спрашиваю!"
  dv "Нет, не курю."
  th "Вот это да!"
  el "Всё-всё, мы нашли."
  "Раздались сбоку голоса кибернетиков."
  sl "А, всё, не надо."
  hide dv with dspr
  "Я оставила её."  
  "Наконец, Ольга Дмитриевна разожгла костёр."
  "Огонь разгорался недолго: сначала вспыхнули газеты, а затем и брёвна, которые собрали мальчики."
  "Я подсела к Семёну."
  show pi normal pioneer with dspr
  sl "О чём думаешь?"
  me "Да так, ни о чём… {w} Наслаждаюсь походом."
  sl "Что-то не похоже."
  me "Ну, от радости прыгать не готов, ты уж извини."
  "Похоже, Семён не в настроении. Наверное, лучше оставить его в покое."
  sl "Ладно, не буду тебе мешать."
  stop music fadeout 2
  scene black with dissolve
  pause 2
  $ persistent.sprite_time = "night"
  $ night_time()
  play ambience ambience_forest_night fadein 3 
  scene bg ext_polyana_night with dissolve
  "Я ещё посидела недолго, но вскоре отправилась на пляж, осторожно скрывшись в кустах."
  scene bg ext_path_night with dissolve
  "Я уже отошла на приличное расстояние, но всё ещё могла расслышать радостные голоса пионеров."
  "Похоже, кто-то действительно наслаждается походом. Рада за них."
  "Этот лес был мне знаком, однако пришлось чуток поплутать, прежде чем я вышла к лагерю."
  show anim stars_1 with dissolve
  "Какое сегодня прекрасное и чистое небо… Кажется, обычно было слегка облачно, но сегодня на небе ни облачка. {w} Да и луна полная."
  th "Романтика да и только."
  stop ambience fadeout 1
  scene black with dissolve
  "…"
  play ambience ambience_boat_station_night fadein 3
  scene bg ext_beach_night with dissolve
  "Придя к пляжу, я сняла с себя форму и зашла в воду в купальнике, который заранее надела."
  "Люблю купаться."
  stop ambience fadeout 1
  scene black with dissolve
  "…"
  play ambience ambience_boat_station_night fadein 3
  scene bg ext_beach_night with dissolve
  "Когда я начала замерзать, пришлось выйти из воды."
  th "Кажется, я забыла взять из домика сумку, в которой лежало полотенце."
  "Прошло не больше 15 минут."
  th "Стоит ли ждать Семёна? Наверное, он остался там."
  th "Но может всё же подождать?"

  menu:
    "Подождать ещё":
      $ sl_m_lp += 1
      th "Ладно, подожду ещё, насмерть-то не замёрзну."
      th "У меня крепкое здоровье."
      stop ambience fadeout 1
      scene black with dissolve
      "…"
      play ambience ambience_boat_station_night fadein 3
      scene bg ext_beach_night with dissolve
      "Чья-то фигура в галстуке стала приближаться к пляжу."
      "Высокий, стройный, немного хилый, взъерошенный…"
      show pi normal pioneer far with dspr
      th "Семён!"

    "Сходить за сумкой":
      th "Скорее всего, Семён не придёт. Ну и ладно… Надеюсь, у них с Леной всё получится."
      "Я вынула ключ из рубашки и отправилась к домику."
      stop ambience fadeout 1
      play ambience ambience_camp_center_night fadein 2
      #*Фон площадь*
      scene bg ext_square_night with dissolve
      pause 1
      #*Фон напротив домика Слави*
      scene bg ext_house_of_sl_night with dissolve
      pause 1
      #*Фон внутри домика Слави*
      stop ambience fadeout 1
      play ambience ambience_int_cabin_night fadein 1
      play sound sfx_open_door_1
      scene bg int_house_of_sl_night with dissolve
      pause 2
      #*Фон напротив домика Слави*
      stop ambience fadeout 1
      play ambience ambience_camp_center_night fadein 2
      scene bg ext_house_of_sl_night with dissolve
      pause 1
      #*Фон площадь*
      scene bg ext_square_night with dissolve
      stop ambience fadeout 1
      pause 1
      #*Фон ночной пляж*
      play ambience ambience_boat_station_night fadein 3
      scene bg ext_beach_night with dissolve
      "Я уже подходила к пляжу, как заметила чью-то фигуру в белой рубашке с галстуком."
      show pi normal pioneer far with dspr
      th "Семён?"

  "Так получилось, что он был повёрнут ко мне спиной."
  "Я тихо подошла к нему."
  sl "Прогуливаешь поход?"
  me "…"
  sl "Я думала, что всё ещё в лесу."
  show pi normal pioneer with dspr
  "Он обернулся."
  me "Извини, я помешал, наверное?"
  sl "Да ничего, я уже заканчивала."
  "Я почувствовала, как мои щёки пылают."
  me "А чего это ты решила ночью искупаться?"
  sl "А что, нельзя?"
  "Я улыбнулась."
  me "Да нет… {w} Просто… {w} А Ольга Дмитриевна не будет против, что ты ушла раньше?.."
  sl "Ну так и ты тоже!"
  "Я ехидно взглянула на него."
  me "Да, и я тоже…"
  "Он сел на песок и посмотрел на реку."
  me "Не понравился поход?"
  sl "Нет, почему… {w} Просто захотелось немного побыть одной."
  me "А я тебе помешал."
  sl "Нет, всё нормально."
  me "Это на тебя не похоже."
  sl "Ты о чём?"
  me "Ну вот так уходить."
  "Я рассмеялась."
  sl "Я же не робот всё-таки, чтобы постоянно действовать по заведённой программе."
  me "Да, точно…"
  "Он замолчал на некоторое время."
  stop ambience fadeout 3
  play music music_list["forest_maiden"] fadein 3
  me "А тебе не кажется всё это странным?"
  sl "Странным?"
  me "Всё, что здесь происходит. {w} Идеальная модель пионерлагеря."
  me "Конечно, я о них знаю не много, но всё именно так, как я себе и представлял."
  th "Порой Семён говорит странные вещи."
  sl "Ты о чём?"
  me "Ты никогда не думала, что находишься не на своём месте?"
  sl "Не знаю."
  me "Точнее, совсем не там, где надо. {w} Как будто за тысячи километров от дома или вообще в другой галактике."
  th "Я и так живу довольно далеко отсюда, но, видимо, он имеет в виду что-то другое."
  sl "Я тебя не понимаю…"
  me "В этом мы с тобой похожи…"
  "Он улёгся на спину."
  me "А что, если я тебе скажу, что я пришелец из будущего?"
  sl "А ты пришелец из будущего?"
  me "Ну, допустим. {w} И как мне вернуться в своё время?"
  th "Ему так и не понравилось здесь?"
  sl "А ты этого хочешь?"
  th "Даже если подумать, что он говорит чистую правду, не хочет ли он всё-таки остаться?"
  me "Ну, допустим, я не знаю. {w} {i}Там{/i}, назовём это так, всё родное… {w} Нет, точнее, привычное."
  me "Практически всё знакомо и к любой ситуации ты готов."
  me "А тут наоборот: буквально каждая мелочь становится для тебя неожиданностью. И вообще всё… {w} другое."
  sl "Разве это плохо?"
  me "Я не говорил, что плохо… {w} Непривычно. Непонятно. {w} Иногда бывает сложно что-то менять. Особенно людям с моим характером."
  sl "А чего ты сам хочешь?"
  me "Начнём с того, что я не могу ответить на этот вопрос, пока точно не пойму, где это «тут»."
  sl "Так выясни!"
  me "Если бы всё было так просто…"
  sl "А что сложного?"
  me "Всё сложно! {w} Я даже не знаю, с какой стороны начать… {w} Да и меня постоянно отвлекают!"
  "Я не выдержала и прыснула."
  sl "Ты так серьёзно об этом рассуждаешь, как будто это всё на самом деле!"
  me "Кто знает…"
  "Мы снова замолчали."
  "…"

  "У меня защекотало в носу и…"
  sl "А-апчхи!"

  me "Будь здорова."
  sl "Спасибо!"
  me "Не надо было ночью-то купаться. Простудишься. Иди скорее в домик, а то холодно."
  sl "Да ничего, я лучше ещё с тобой посижу. Сейчас, только оденусь."
  me "Пойдём, я тебя провожу."
  "Я встала, но скоро мне поплохело, и пришлось облокотиться на Семёна."
  me "Что с тобой?"
  sl "Да что-то голова закружилась…"
  "Он протянул руку, чтобы пощупать лоб."
  me "Я же тебе говорил!"
  sl "Апчхи!"
  me "Пойдём скорее!"
  th "Вот ещё!"
  sl "Нет… Я Женю заражу… {w} Слушай, давай лучше в медпункт."
  me "И что ты будешь делать в медпункте ночью одна? Глупости!"
  sl "Нет, не глупости! Не хочешь – я сама пойду!"
  "Я демонстративно отшатнулась от него и пошла одна."
  th "Ну проводи же меня!"
  me "Не обижайся. {w} На, вот, накинь. Холодно ведь!"
  "Он предложил мне свой свитер."
  sl "Спасибо!"
  "Я просунула в него голову и расправила на плечах. Потом взглянула на Семёна взглядом благодарности."
  me "Медпункт, так медпункт. Как скажете!"
  stop music fadeout 2
  play ambience ambience_camp_center_night fadein 3
  scene bg ext_aidpost_night with dissolve
  "Через пару минут мы подошли к медпункту, и я уже открывала его дверь."
  stop ambience fadeout 2
  play sound sfx_open_door_2
  scene bg int_aidpost_night with dissolve
  play ambience ambience_int_cabin_night fadein 3
  "Наконец я открыла дверь и облокотилась на его руку."
  show pi normal pioneer with dspr
  sl "Голова немного кружится."
  "Я села на койку."
  me "Слушай, ну всё-таки! Ночью одной в медпункте…"
  sl "Всё нормально. {w} Не хочу никого стеснять. Тем более, завтра придёт медсестра."
  me "Слушай, может, я с тобой побуду…"
  sl "Зачем? {w} Всё в порядке будет. Спасибо, что проводил. Иди и ты спать."
  th "Это конечно было мило, но пора остановиться."
  me "Мне кажется, что всё же…"
  sl "Всё в порядке!"
  me "Я всё-таки…"
  sl "Не надо, говорю же!"
  show pi smile pioneer with dspr
  me "Ты же меня не выгонишь."
  "Он лукаво улыбнулся."
  sl "Ладно, но если заразишься, пеняй на себя!"
  th "Страшная угроза…"
  sl "И чем займёмся?"
  show pi normal pioneer with dspr
  "Он достал из ящика карты."
  me "В дурака?"
  th "Я не азартный игрок, но мы ведь только на интерес."
  sl "А давай."
  stop ambience fadeout 2
  scene black with dissolve
  "…"
  play ambience ambience_int_cabin_night fadein 3
  scene bg int_aidpost_night with dissolve
  "Играли мы долго."
  "Было уже много времени. Мы смеялись и болтали на разные темы."
  "Но мне уже не хотелось, чтобы он уходил."
  "В его компании мне и правда стало лучше."
  "Но вот на часах полночь…"
  show pi normal pioneer with dspr
  sl "Пора спать."
  me "Пожалуй…"
  "Здесь практически не было места."
  sl "А ты где собираешься?"
  sl "Иди всё же! {w} Не надо со мной тут сидеть."
  me "Да я и так…"
  "Я всё ждала, когда он уйдёт, но он так и продолжал стоять в задумчивости."
  th "Похоже, опять завис."
  sl "Спокойной ночи!"
  hide pi with dspr
  "Сказала я и задёрнула занавеску."
  me "Спокойной."
  "Похоже, Семён уселся на стул и уснул на столе."
  stop ambience fadeout 2
  scene black with dissolve
  "…"
  play ambience ambience_int_cabin_night fadein 3
  scene bg int_aidpost_night with dissolve
  "Никак не получалось заснуть. {w} То подушка слишком жёсткая, то в одеяле запуталась, то холодно, а в одежде вообще спать неудобно."
  "Похоже, этот везунчик уже заснул. {w} Но что-то кричал во сне…"
  me "Нет!.. Не бвам… овамусь, овамусь… она.."
  "И вдруг прекратил."
  show pi normal pioneer with dspr
  "Я одёрнула шторку."
  show pi smile pioneer with dspr
  me "Просто плохой сон…"
  "Он посмотрел на меня и глупо улыбнулся."
  sl "Ты кричал…"
  show pi normal pioneer with dspr
  me "И что я кричал?"
  sl "Не знаю… {w} Неразборчиво."
  me "…"
  sl "Семён."
  me "А?"
  sl "Мне холодно…"
  "Я попыталась сильнее укутаться в свитер."
  me "Сейчас, поищу одеяло."
  th "Да мне не одеяло…"
  "Я решила промолчать."
  "Он перерыл все шкафчики, но так ничего и не нашёл."
  me "Извини, ничего нет…"
  me "Подожди, сейчас сбегаю и принесу."
  sl "Не надо…"
  "Я решила его слегка подтолкнуть."
  sl "Может, ты ляжешь со мной? Так будет теплее."
  "Я произнесла это жалобным голосом."
  me "А ты уверена, что это… что… это нормально?"
  sl "Значит, нельзя?"
  me "Нет, почему…"
  stop ambience fadeout 2
  play music music_list["trapped_in_dreams"] fadein 3
  scene cg d5_sl_sleep with dissolve
  "Он снял ботинки и улёгся на краешке."
  "Я нежно обняла его и положила голову ему на грудь."
  "Я чувствовала его тепло."
  sl "Да, так лучше."
  me "Хорошо…"
  sl "Спасибо тебе."
  me "За что?"
  sl "За то, что ты здесь."
  me "Да нет, ничего такого…"
  "В его голосе чувствовалась фальшь."
  sl "Нет, правда."
  me "Ну, тогда – пожалуйста."
  "Я улыбнулась."
  me "Обращайтесь в любое время, так сказать!"
  sl "Ты такой заботливый, внимательный."
  th "Но намёки немножечко не для тебя, буду знать."
  me "Стараюсь."
  scene cg d5_sl_sleep_2 with dspr
  sl "Ты хороший друг."
  me "Друг? Ну, да, наверное…"
  "Я чем-то обидела его? {w} Его сердце забилось быстрее."
  me "Мне тоже…"
  "Я уже не обращала внимания на то, что он говорит {w}, я наконец-то могла спокойно заснуть."
  "Вдруг его сердце забилось ещё чаще."
  "И не видя его лица, мне казалось, там была грустная улыбка."
  sl "Ты чем-то расстроен?"
  me "Нет, всё в порядке."
  sl "Но я же вижу."
  me "Может быть…"
  th "Может быть, он не привык быть в такой компании с девушкой?"
  sl "Не хочешь об этом говорить?"
  me "Да не то, чтобы… Просто и не о чем говорить на самом деле."
  sl "Получается, ты не знаешь, чем расстроен?"
  me "Наверное так."
  sl "А зачем тогда расстраиваться?"
  "Я засмеялась."
  me "Выходит, что и незачем."
  "Наконец, его сердце перестало бешено биться."
  scene cg d5_sl_sleep with dspr
  sl "Вот и хорошо!"
  "Я ещё крепче прижалась к нему."
  me "Не холодно?"
  sl "Нет, спасибо, но если тебе неудобно, то ты скажи!"
  me "Ничего, нормально."
  sl "Как тогда, с лодкой?"
  me "Там совсем другое дело было же!"
  scene cg d5_sl_sleep_2 with dspr
  sl "Хорошо-хорошо."
  "Я лукаво улыбнулась и заглянула ему в глаза."
  sl "Значит, точно всё в порядке?"
  me "Да, в полном."
  th "Семён действительно не понимает намёков."
  th "Надо его ещё подтолкнуть."
  sl "Ты уверен?"
  me "Да… Наверное."
  th "Оставлю его с расспросами."
  sl "Ну хорошо. Тогда спокойной ночи!"
  me "И тебе."
  scene cg d5_sl_sleep with dspr
  "Наконец я стала засыпать."
  stop music fadeout 2
  scene black with dissolve
  "…"
  play music music_list["door_to_nightmare"] fadein 3
  scene bg ext_house_of_sl_day
  call pomehi
  with dissolve
#*Надо спрайт кота, любого, чтоб у него были 2 эмоции: пассивный и злой*
  show bor normal close with dspr
  dreamgirl "Приветствую, Славя."
  show bor serious close with dspr
  dreamgirl "Прости но лучше тебе молчать, пока я не разрешу, хорошо?"
  th "Что вообще происходит?"
  show bor normal close with dspr
  dreamgirl "Тебя наверное беспокоит, что происходит и как меня зовут. {w} Сейчас ты во сне, а меня зовут Борис."
  bor "Но позволь... Наверное, будет лучше, если мы не будем стоять на пороге."
  scene bg int_house_of_sl_day
  show bor normal close
  call pomehi
  with dissolve
  bor "Хотя, может, ты предпочитаешь вернуться туда, откуда ты сюда пришла?"
  scene bg int_aidpost_night
  show bor normal close
  call pomehi
  with dissolve
  bor "Я разрешаю тебе задать мне 3 вопроса, которые больше всего тебя беспокоят, а дальше ты меня больше никогда не встретишь."
  sl "Зачем ты всё это делаешь?"
  bor "М-да. Всё для тебя, я хочу тебе помочь."
  sl "С чем помочь?"
  bor "Пожалуй мне было лучше молчать про помощь… {w} Я хочу помочь вашим с Семёном отношениям, ты ведь не против? Ой!"
  bor "Ну давай уже, спрашивай последний и я ухожу."

  menu:
    "Как помочь?":
      bor "Чтобы вы воссоединились вместе. Ты и он."
      sl "А как нам воссоединиться?"
    "Любит ли меня Семён?":
      bor "По правде говоря, он ещё сам не уверен."
      sl "Что значит «не уверен»? У нас было так много запоминающихся моментов!"
    "Почему он хочет уйти из лагеря?":
      bor "Он тебе уже сказал почему."
      sl "Так почему?"
    "С нами всё будет в порядке?":
      bor "Всё зависит от его дальнейших действий. Я предвижу множество вариантов развития событий."
      sl "И во скольких всё сложится хорошо?"

  "Кот уже собирался уходить, но тут он резко обернулся и на лице его был звериный оскал."
  stop music fadeout 3
  "В комнате загорелся свет, а кот превратился в кого-то {w} знакомого…"
  play ambience ambience_int_cabin_day fadein 3
  scene bg int_aidpost_night
  show pi normal pioneer at cleft
  show mt angry pioneer at cright
  with dspr
  mt "Семён…"
  stop ambience fadeout 3
  play music music_list["awakening_power"] fadein 3
  show mt rage pioneer at cright with dspr
  mt "Я тебя везде ищу, а ты – смылся из леса раньше времени, не пришёл ночевать и развращаешь нашу лучшую пионерку!"
  sl "Ольга Дмитриевна! Это совсем не то, что вы думаете! Я просто заболела, и Семён проводил меня сюда."
  sl "А потом мне стало холодно и… {w} Я ему говорила, чтобы он шёл к себе!"
  mt "Да-да, конечно! Значит, заболела, говоришь?"
  sl "Да…"
  show mt angry pioneer at cright with dspr
  mt "Так вот и лечись!"
  show mt rage pioneer at cright with dspr
  mt "А ты! Быстро со мной!"
  "Она обратилась уже к Семёну."
  hide pi with dspr
  "Он встал и вышел, даже не взглянув и не попрощавшись."
  hide mt with dspr
  "За ним вышла и вожатая."
  stop music fadeout 3
  play ambience ambience_int_cabin_day fadein 3
  "Я осталась одна."
  "Ожидание тянулось бесконечность."
  "Каждая секунда длилась час."
  "А я сидела и ждала…"
  th "Надо срочно придумать оправдание!"

  menu:
    "Свалить вину на Семёна":
      $ sl_m_day5_make_semen_guilty = True
      $ sl_m_lp -= 3
    "Сказать правду":
      $ sl_m_day5_make_semen_guilty = False
      $ sl_m_lp += 2

  stop ambience fadeout 3
  scene black with dissolve
  "…"
  play ambience ambience_int_cabin_day fadein 3
  scene bg int_aidpost_night with dissolve
  "Прошло уже больше получаса. {w} Но никто не возвращался."
  "Я слишком устала и легла спать."
  stop ambience fadeout 4
  show blink
  if sl_m_Full:
      jump slavyana_mod__day6
  jump slavyana_mod__launcher0



#Ещё мы сделаем четвёртую, пасхальную концовку, для которой надо будет:
#1) Набрать меньше 3 очков привязанности к Семёну
#2) Во 2 дне пойти с Семёном за картами
#3) В 4 дне в выборе на карте первым делом пойти в клуб Мику.
#4) В 5 дне не напоминать Лене.
#Таким образом, сценка после приплывания на лодке:

#*Фон пристань*
  "Путь обратно затратил гораздо меньше времени."
  "Семён пришвартовал лодку и обессиленно рухнул на землю."
  "Мы склонились над ним."
  sl "Если тебе было так тяжело, то сказал бы!"
  "У меня был некоторый навык гребли на лодке."
  un "Да…"
  me "Да нет, ничего… {w} Сейчас полежу и всё пройдёт…"
  me "Ладно, тогда отнеси корзинки, пожалуйста, Ольге Дмитриевне, а то у нас ещё дела есть."
  me "Да, конечно."
  "Я поставила корзинки рядом с ним, и мы отправились вместе с Леной дальше."
  "Когда мы отошли, Лена спросила:"
  un "Славя, а у меня вообще-то свои дела ещё есть."
  sl "Эх, ладно."
#Фон тёмный экран
  "…"
#*Фон площадь*
  "По пути в библиотеку я встретила Ольгу, которая поручила мне уборку поляны."
  "После уборки я решила сходить к себе в домик переодеться."
#*Фон внутри домика Слави*
  th "Надо будет сказать Оле, чтобы она меня освободила от этого мероприятия. Мне надо побыть одной."
  "Я решила прогуляться перед ужином."
#*Фон площадь*
  "Я уже несколько дней не убиралась на площади, надо бы это исправить."
  "Но тут меня окликнула Лена."
  un "Славя, помоги мне пожалуйста."
  sl "Давай. {w} А что нужно?"
  un "Я… я вчера где-то в лесу книжку потеряла… не могу найти."
  sl "Ну, пойдём."
#*Фон тропинка в лесу (обязательно утренняя)*
  "Покинув площадь, мы шли через лесок."
  "На душе было очень радостно, несмотря на то что сегодня последний день."
  sl "А что за книжка? Небось, опять «Унесённые ветром»."
  un "Конечно же нет."
  un "Была в библиотеке и взяла первую попавшуюся. Даже названия не помню."
  sl "А Женя знает, что ты её потеряла?"
  un "Я ей не говорила, и надеюсь, что ты тоже не скажешь об этом."
  sl "Не скажу, конечно."
  "Мы шли довольно долго но вышли на какую-то полянку, к которой пришлось пробираться через кусты."
#*Фон полянка (обязательно утренняя)*
  "Славя: Да-а, далеко же мы отошли. Ты уверена, что она здесь?"
  th "Как странно, уже вечер а ещё светло."
  un "Думаю, надо чуть дальше. Нужно ведь поискать, уверена, вдвоём мы её точно найдём."
  "Она улыбнулась."
  "Мы искали под каждым деревом и кустиком, проверяя каждый уголок, где она могла по ошибке оставить книжку."
  "Вскоре перед нами возникло дерево."
  un "Вон, смотри!"
  "Она указала на него."
  un "Может быть, за ним?"
  sl "Ну, давай посмотрим."
#трек Orchid
  "Чувство самосохранения отозвалось в глубине."
  "Но я не предала этому значения. Тем не менее, ходить становилось тяжелее."
  "Я дважды обошла дерево, но нигде не было книги."
  sl "Нет, Лен, её здесь нет."
  "Я продолжала осматривать, но как бы в оправдание повторила."
#конец трека
  sl "Нет, Лен, её здесь точно нет."
#трек Pile
  un "{b}НЕТ?! КОНЕЧНО ЖЕ ЕЁ ЗДЕСЬ НЕТ, НАИВНАЯ ДУРА!{/b}"
  "Лена залилась каким-то нечеловеческим смехом."
  "Вдруг она подскочила ко мне, схватила за голову и сильно ударила об дерево."
#*Красный эффект удара*
  "Славя: Ааааа!"
  un "Э-э нет, спать ты не будешь."
  "Она вынула из-за спины нож."
  sl "Лена, что ты делаешь? Не надо, прошу, успокойся."
  "Я попыталась успокоить её."
  un "Что такое? Где твоя улыбка, Славя?!"
  "Она прокручивала нож в руке."
  un "Посмотри, какая хорошая погода, а какой красивый лес."
  un "Ты ведь любишь природу, так ведь?! Любишь побыть одной в тихом лесу?!"
#конец трека
  "Она зажала меня своими ногами. {w} Взмахнула ножом и…"
#*Красный эффект удара и звук удара как тогда во сне Семёна с кузнечиками*
#*иллюстрация с растерзанной Славей*
#Красный эффект удара
#*Фон тёмный экран*
  "А дальше всё было как в тумане…"
  "…"
#*Выскакивает ачивка «Game over, suka»*
  voice "Данная концовка основана на моде «Мику-рут глазами Лены»"
#*Титры на фоне иллюстрации расчленёнки под трек «Torture»*


#При втором прохождении выбор «Соврать»(в выборе с Леной на поляне) даёт выход на альтернативную концовку, но очков для её получения должно быть >=9 на 7 дне, иначе плохая

label slavyana_mod__day5_fast_choice:
  $ day_time()
  $ persistent.sprite_time = "day"
  scene bg ext_polyana_day with dissolve
  "Пятый день."
  scene bg ext_island_day
  show un normal pioneer at cleft
  show pi normal pioneer at right
  with dissolve

  "После обеда Славя с Леной отправились на остов за земляникой, прихватив с собой семена."
  "Корзинки оказалось две и встал выбор как разбиться на группы."
  menu:
    "Пойти с Семёном":
      $ sl_m_lp += 1
    "Я и сама могу":
      pass

  scene bg ext_polyana_day
  show un evil_smile pioneer far
  with dissolve
  "Во время уборки поляны перед костром, Лена заговорила об отношениях"
  if sl_m_lp < 4:
    $ sl_m_day5_cleaning_told_truth = False
  else:
    menu:
      "Соврать":
        $ sl_m_day5_cleaning_told_truth = False
      "Сказать правду":
        $ sl_m_day5_cleaning_told_truth = True

  $ night_time()
  $ persistent.sprite_time = "night"

  scene bg ext_beach_night with dissolve
  "После костра, Славя ушла купаться и забыла сумку. Славя Ждала Семёна, но он не появлялся."
  menu:
    "Подождать ещё":
      $ sl_m_lp += 1
    "Сходить за сумкой":
      pass

  scene bg int_aidpost_night with dissolve
  "В конце дня после того, как Ольга увела Семёна Славя решила придумать оправдание"
  menu:
    "Свалить вину на Семёна":
      $ sl_m_day5_make_semen_guilty = True
      $ sl_m_lp -= 3
    "Сказать правду":
      $ sl_m_day5_make_semen_guilty = False
      $ sl_m_lp += 2
  return