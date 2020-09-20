init:
  python:
    colors['alis'] = {'night': "#fd7c6e", 'sunset': "#fd7c6e", 'day': "#fd7c6e", 'prolog': "#fd7c6e"}
    names['alis'] = u"Алиса"
    store.names_list.append('alis')

    colors['krist'] = {'night': "#a3505c", 'sunset': "#a3505c", 'day': "#a3505c", 'prolog': "#a3505c"}
    names['krist'] = u"Кристина"
    store.names_list.append('krist')
  image SlaviaRoom = "scenario_slavyana/res/slavy_alt/image/int_sl_room.jpg"
  image Hallway = "scenario_slavyana/res/slavy_alt/image/int_hallway.jpg"
  image Podz01 = "scenario_slavyana/res/slavy_alt/image/int_podz_01.jpg"
  image Podz02 = "scenario_slavyana/res/slavy_alt/image/int_podz_02.jpg"
  image Podz03 = "scenario_slavyana/res/slavy_alt/image/int_podz_03.jpg"
  image Street01 = "scenario_slavyana/res/slavy_alt/image/int_str_01.jpg"
  image Street02 = "scenario_slavyana/res/slavy_alt/image/int_str_02.jpg"
  image Street03 = "scenario_slavyana/res/slavy_alt/image/int_str_03.jpg"
  image Street04 = "scenario_slavyana/res/slavy_alt/image/int_str_04.jpg"
  image Street05 = "scenario_slavyana/res/slavy_alt/image/int_str_05.jpg"
  image Street06 = "scenario_slavyana/res/slavy_alt/image/int_str_06.jpg"
  image SlaviaRoomFocus = "scenario_slavyana/res/slavy_alt/image/int_sl_roomfoc1.jpg"
  image SlaviaRoomFocus2 = "scenario_slavyana/res/slavy_alt/image/int_sl_roomfoc2.jpg"
  image SlaviaRoomFocusKrist = "scenario_slavyana/res/slavy_alt/image/int_sl_roomfocusonkrist.jpg"
  image SlaviaRoomFocusAlisa = "scenario_slavyana/res/slavy_alt/image/int_sl_roomfocusonalis.jpg"
  image SemenUnknown = "scenario_slavyana/res/slavy_alt/image/sem_unk.jpg"

  $ Sound01 = "scenario_slavyana/res/slavy_alt/sound/Soundtrack_01.ogg"
  $ Sound02 = "scenario_slavyana/res/slavy_alt/sound/Soundtrack_02.ogg"
  $ DressFall = "scenario_slavyana/res/slavy_alt/sound/Sound_dressfall.ogg"
  $ Sound03 = "scenario_slavyana/res/slavy_alt/sound/Soundtrack03.ogg"
  $ Sound04 = "scenario_slavyana/res/slavy_alt/sound/Soundtrack04.ogg"
  $ Sound05 = "scenario_slavyana/res/slavy_alt/sound/Soundtrack05.ogg"

label slavyana_mod__epilogue_alt:
  window show
  $ renpy.pause (1)
  "Бывают сны, надолго закрепляющиеся в нашей памяти."
  "В которых, ты действительно хочешь оставаться и не проснуться вновь."
  "Целый новый мир и герои этой сказки."
  "И прошлое уже давно позади, а настоящее здесь и сейчас."
  "И наш век - это всего лишь миг для вселенной."
  "Но и вряд ли наберется один день."
  "Каждый человек не задумывается, как прожить ту или иную минуту, и столь ли необходимо и важно чем он занимается в целом мегаполисе?"
  window hide
  stop music fadeout 2
  $ renpy.pause (2)
  play music music_list["sparkles"] fadein 3
  scene SlaviaRoomFocusKrist  with dissolve
  $ renpy.pause (1)
  window show
  play sound sfx_bed_squeak1
  krist "Славя, просыпайся! Хватит спать!"
  "Нехотя, но мне пришлось проснуться."
  "Вставать не хотелось - будучи закатанной в одеяле, я чувствовала себя на вершине блаженства."
  "Идти мне сегодня никуда не надо, как ни как."
  "Да и планов, на сегодняшний вечер у меня не было."
  scene SlaviaRoomFocusAlisa  with dissolve
  alis "Славя, просыпайся. Иначе опять все проспишь как в прошлый раз."
  scene SlaviaRoomFocus  with dissolve
  "Эх, как же мне хотелось еще пару минут полежать одной, в спокойствии."
  play sound sfx_bed_squeak2
  "Я перевернулась с бока на бок и стала рассматривать белый потолок."
  "Спустя пару минут, у меня хватило сил сбросить одеяло и более менее отойти, от этого сказочного сна."
  "Пионерлагерь 'Совенок' и Семен, Лена, Мику, Алиса, Ольга Дмитриевна."
  scene SlaviaRoomFocus2  with dissolve
  "Эти персонажи были мне очень знакомы, но неужели мы виделись ранее?"
  "Но, что же тогда произошло той злополучной ночью? К сожалению, этот момент, крепко стерся у меня из памяти."
  "Семен{w}, да! Мы заснули в автобусе, а потом я заснула и уже очнулась здесь..."
  "У себя в квартире, той же холодной зимой, что была неделю или две назад."
  "Мне очень понравилось в этом сне. И что же мешает этому повториться вновь?"
  "Я попыталась закрыть глаза и уснуть, и сразу же оказаться там."
  $ renpy.pause (1)
  window hide
  scene black  with dissolve
  $ renpy.pause (1)
  window show 
  "Нет, видимо, то время уже не вернуть, и надо вновь вернуться к настоящей, реальной жизни."
  scene SlaviaRoom  with dissolve
  "Лучшим решением было просто забыть это как сон. Странный, пусть и лучший сон, который я видела."
  "Единственным элементом, мешающим мне забыть это. Был Семен... Что-то было в нем, что не могло отпустить его просто так."
  "Я вспомнила его улыбку, чувство юмора, время проведенное вместе."
  "С времени его приезда в лагерь до... {w} настоящего."
  "Как же хочется вернуть то время, хотя бы один день, проведенный вместе."
  "И как бы я хотела, чтобы он вернулся со мной из этого лагеря..."
  "Я постаралась забыть этот сон."
  "Нехотя, мне пришлось встать. Знаете, такое разбитое чувство, когда переспала, видимо сейчас оно и есть."
  sl "Девочки, какое сегодня число?"
  krist "28 Декабря."
  sl "А сколько сейчас время?"
  alis "Одиннадцать часов вечера."
  "Я вспомнила, что мне надо было срочно ехать за продуктами к новому году."
  "В одиннадцать часов вечера из всех работал только один знакомый мне магазин, но к нему можно было подъехать только на автобусе."
  sl "Мне надо в магазин..."
  krist "Ночью?"
  sl "Почему бы и нет?"
  alis "Может завтра? Уже ночь на дворе, вдруг, что случится."
  sl "Скоро новый год на дворе, а у нас так ничего и не готово."
  sl "Не волнуйтесь, все будет в порядке."
  play sound sfx_far_steps
  window hide
  $ renpy.pause (1)
  scene Hallway  with dissolve
  stop music fadeout 2
  $ renpy.pause (1)
  window show
  "Через несколько шагов, в полусонном состоянии я дошла до прихожей, ориентируясь на интуицию и память."
  stop sound 
  play music DressFall
  $ renpy.pause (1)
  stop music fadeout 2
  "Открыв гардероб, на меня посыпалась куча одежды."
  play music Sound05 fadein 4
  "Алиса и Кристина уже давно имели черные пояса, по загрязнению квартиры."
  "Расправившись с этой горой одежды, я нашла свою одежду, оделась, собралась, и пошла на улицу."
  sl "Не скучайте без меня."
  "Из комнаты донеслись их голоса."
  krist "Удачи, приходи поскорее."
  alis "Уже поздно, так что возвращайся поскорее."
  play sound sfx_open_door_1
  scene Podz01  with dissolve
  "Лифт не работает, придется спускаться по лестнице..."
  "Я попробовала еще несколько раз нажать на кнопку, но она не поддавалась."
  window hide
  $ renpy.pause (1)
  scene Podz02  with dissolve
  $ renpy.pause (1)
  window show
  "По пути мне никто и не встретился, в такое время, все сейчас сидят дома и отогреваются от столь холодной зимы."
  scene Street01  with dissolve
  play sound sfx_open_door_2
  "Как же холодно. Да и Согреть некому, так и приходится в пальто укутываться. Будь Семен рядом со мной..."
  "Сейчас градусов тридцать мороза не меньше. Более чем уверена."
  "Пальто очень согревало и холода можно было не бояться."
  "Яркий свет фонарей, озарял улицы ."
  "Метель и ветер очень хорошо виднелись при свете фонарей."
  "Никого на улице не было. Сомневаюсь, кто пошел бы сейчас на улицу, при такой погоде?"
  "Холод, метель и сильный ветер отбивали малейшее желание выйти погулять напрочь."
  "Я бы тоже сидела дома, но мне нужно по делам. Это было единственной причиной выйти на улицу."
  scene Street02  with dissolve
  "Морозы сковали землю. Замерзли реки и озера. Везде лежит белый пушистый снег."
  "Только животным тяжело в зимнюю стужу."
  "Улицы, вчера еще по-осеннему унылые, сплошь покрыты белым снегом, и солнце переливается в нем слепящим блеском."
  scene Street06 
  "Причудливый узор мороза лег на витрины магазинов и наглухо закрытые окна домов, иней покрыл ветви тополей."
  "Глянешь ли вдоль улицы, вытянувшейся ровной лентой, вблизи ли вокруг себя посмотришь, везде все то же: снег, снег, снег"
  scene Street03  with dissolve
  "Изредка поднимающийся ветерок пощипывает лицо и уши, зато как красиво все вокруг! Какие нежные, мягкие снежинки плавно кружатся в воздухе."
  "Как ни колюч морозец, он тоже приятен. Не за то ли все мы любим зиму, что она так же, как весна, наполняет грудь волнующим чувством. Все живо, все ярко в преобразившейся природе, все полно бодрящей свежести."
  "Так легко дышится и так хорошо на душе, что невольно улыбаешься и хочется сказать дружески этому чудесному зимнему утру: «Здравствуй, зима!»"
  scene Street04  with dissolve
  "По стволам и сучьям толстых деревьев постукивает мороз, хлопьями осыпается лёгкий серебряный иней. В темном высоком небе видимо-невидимо рассыпалось ярких зимних звезд..."
  window hide
  stop music fadeout 2
  $ renpy.pause (1)
  play music music_list["everlasting_summer"] fadein 2
  scene bus_stop  with dissolve
  $ renpy.pause (1)
  window show
  "Я и сама не заметила, как оказалась на автобусной остановке."
  "Ветер и метель уже стихли. И шел лишь небольшой снег."
  "Автобусная остановка пустела. Автобус тоже не подавал признаки существования."
  "Холодно, я старалась разогреться как могла, но и это не особо помогало."
  "Стоя, на небе я увидела очень красивую, яркую звезду."
  "Видимо, полярная. Только она светится столь ярко на ночном небе."
  "На часах показывало полуночь. И метель начала усиливаться."
  "Мысль вернуться домой была актуальнее с каждой минутой."
  "Как вдруг, ко мне подошел незнакомец."
  scene SemenUnknown  with dissolve
  "Я решила спросить у него про автобус, может он знает."
  sl "А вы не знаете, последний автобус уже ушел?"
  stranger "Вроде бы после двенадцати должен быть еще один."
  sl "Спасибо."
  sl "А вы почему так поздно?"
  stranger "Гуляю..."
  "Задумчиво ответил незнакомец."
  stranger "А вы... по делам?"
  "Неужели ему это так интересно?"
  sl "Ну,не то чтобы... {w} Еду домой."
  stranger "А где живете?"
  "Я решила ему соврать, в наше время много людей, которым нельзя доверять."
  sl "Далеко..."
  stranger "Я тут рядом."
  stranger "Выбирать не приходится."
  sl "Вам тут не нравится?"
  stranger "Не знаю, я уже привык."
  sl "А вот мне кажется, что человек везде может быть счастливым!"
  stranger "Наверное."
  sl "Ну вы сами посудите! {w} Люди ведь и в Антарктиде живут... на станциях, я имею в виду. {w} И в пустыне Сахара! И много где еще.Главное ведь- это люди!"
  stranger "С вами сложно не согласится."
  sl "Мне кажется, вы неискренни."
  stranger "Нет,отчего же,сударыня..."
  "Мне кажется он образованный человек, по крайней мере, хочет им казаться."
  "И конечно с юмором."
  sl "Я думаю, вы хороший человек."
  "Внезапно, незнакомец повернулся."
  window hide
  scene bus_stop  with dissolve
  show pi normal coat 
  window show
  "Теперь все сошлось по полочкам. Я поняла, почему его голос, фигура, и все показались мне знакомыми."
  "Передо мной стоял Семен. Именно тот Семен из лагеря, именно такой каким я помню, с такой же внешностью и характером, даже голос был похож. "
  sl "А мы с вами нигде не встречались?"
  me "Возможно, ваше лицо кажется я где-то видел."
  sl "Вы были в пионерлагере?"
  me "Один раз.{w} Во сне."
  sl "Мне недавно снился сон..."
  sl "В смысле? Тоже про пионерский лагерь."
  me "Может быть, возможно там и виделись."
  sl "Скорее всего, так и есть."
  sl "Кстати, меня зовут Славя. Полное имя – Славяна, но все меня Славей зовут."
  "Он немного промолчал, но чуть позже неловко ответил."
  me "А меня Семен..."
  sl "Очень милое имя."
  show pi smile coat  with dissolve_fast
  me "Тоже на «С» начинается."
  sl "Да."
  me "Значит, ты далеко живешь?"
  sl "Ну не так уж..."
  show pi normal coat 
  me "А я думал,что где-то на юге."
  sl "Почему?"
  me "Не знаю... {w} может быть, потому что ты похожа на пионерку."
  me "Если бы не они, возможно, мы бы и не познакомились."
  sl "Почему?"
  show pi smile coat 
  me "Да так... Шутка... {w} Скажи, а ты согласна,что мир существует, потому что мы в это верим?"
  sl "Это какой-то субъективный идеализм прямо..."
  me "Последнее время мне, наверное, близка эта философская школа."
  sl "Ну, не знаю... {w} Я в таких вещах не очень сильна."
  me "А в чем сильна?"
  $ renpy.pause (1)
  sl "В чем-то другом."
  me "Не сомневаюсь ни секунды!"
  sl "Но ты же меня едва знаешь!"
  me "А кажется, что уже давно."
  sl "Да, и мне почему-то так кажется..."
  "Между нами возникло неловкое молчание."
  "Автобус все еще не приезжал."
  $ renpy.pause (1)
  show pi normal coat 
  me "Похоже, 410-ый маршрут на сегодня закончил свои рейсы."
  sl "Похоже..."
  me "Если хочешь..."
  "Что он имеет ввиду?!"
  sl "Что?"
  show pi smile coat 
  me "Можешь остаться у меня..."
  sl "Но мы же недавно познакомились."
  me "Да, я понимаю,но ночь на улице в такой холод."
  "Конечно,я была не против переночевать у него.Дома лучше,но добираться до него в такой холод было безумием."
  sl "А не боишься?"
  me "Я? А надо?"
  sl "Кто знает... Кто знает..."
  show pi normal coat 
  me "Я просто предложил, ты не подумай ничего..."
  sl "Да я все прекрасно понимаю!"
  sl "Если ты не против, конечно..."
  me "Пойдем?"
  "Может быть автобус все-таки еще приедет. Просто опаздывает..."
  sl "Давай все же еще немного подождем, вдруг приедет?"
  me "Хорошо."
  $ renpy.pause (1)
  "Надо как-то поддержать разговор."
  sl "А чем ты занимаешься?"
  "Немного постояв и подумав он ответил мне."
  $ renpy.pause (1)
  me "Я... Ну... {w} Работаю на дому, так скажем."
  sl "Здорово!"
  me "Что хорошего?"
  sl "Не знаю... {w} Много свободного времени, никуда ездить не надо! Ну и все такое..."
  "Действительно... {w} Хорошая работа."
  show pi smile coat 
  me "А ты?"
  "Я нигде не работала и мне не понять людей, которые работают. И пока, я учусь в университете."
  sl "Я учусь."
  me "На краеведа?"
  "Почему именно на краеведа?"
  sl "А кто это?"
  me "Неважно..."
  sl "На эколога."
  me "Что же, достойная профессия..."
  "Уже шел 2 час ночи."
  "А автобус, все не приезжал..."
  sl "Пойдем?"
  "По его взгляду было понятно, что он тоже был не против."
  $ renpy.pause (1)
  me "Пошли."
  "Мы встали и медленно пошли в сторону его дома."
  "Он аккуратно взял меня под руку и заглянул в глаза."
  me "Знаешь, я уверен, что в этом году все будет лучше, чем в предыдущем!"
  hide me  with dissolve
  stop music fadeout 2
  $ renpy.pause (1)
  "..."
  $ renpy.pause (1)
  window hide
  scene black  with dissolve
  $ renpy.pause (1)
  return