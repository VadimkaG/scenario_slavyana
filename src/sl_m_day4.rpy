init python:
  # Условие, если славя ходила за шуриком
  go_to_sh = False

label slavyana_mod__day4:
  stop music
  stop sound
  stop ambience
  $ backdrop = "days"
  $ new_chapter(4, u"Славя. День четвертый")
  $ save_name = (u'Славя. День четвертый')
  $ day_time()
  $ persistent.sprite_time = "day"
  $ renpy.pause(3, hard=True)

  play ambience ambience_int_cabin_day fadein 4
  scene bg int_house_of_sl_day with dissolve2
  "Это утро, как всегда, было добрым."
  "Я поднялась с кровати."
  "На часах было полседьмого."
  th "Как раз успею на утреннюю пробежку."
  "А моя соседка мирно спала, дожидаясь седьмого часа."
  th "Странно, что она частенько спит на своём посту."
  "Я надела спортивную форму и захватила пакетик с умывальными принадлежностями, после чего вышла на улицу."
  stop ambience fadeout 1
  scene black with dissolve
  pause 1
  play ambience ambience_camp_center_day fadein 3
  scene bg ext_houses_day with dissolve
  "Солнце уже появилось, но ещё не успело подняться высоко."
  "Пробежка просто обещала быть прекрасной!"
  "А лагерь спал.{w} Абсолютно весь, кроме меня."
  scene bg ext_washstand_day with dissolve
  "Я добежала до умывальников, которые, естественно, пустовали."
  "Подойдя к одному из них, я краем глаза заметила, как в музыкальный клуб забежала фигура в пионерской форме и циановыми волосами."
  th "С утра пораньше не на пробежку, а в клуб?"
  "Я быстро умылась холодной водой, которая мгновенно отогнала остатки сна, и побежала дальше."
  stop ambience fadeout 1
  scene black with dissolve
  "…"

  play ambience ambience_camp_center_day fadein 3
  scene bg ext_square_day with dissolve
  "Я решила вспомнить события минувшего дня."
  th "Случай в клубе кибернетиков…"
  th "Уборка на площади -{w} с Семёном."
  th "Уборка в библиотеке -{w} тоже с Семёном."
  th "Вечерняя дискотека. И, как ни странно, тоже с Семёном."
  th "А потом этот странный разговор на пляже…"
  th "Возможно, я действительно много времени провожу с Семёном? Но как так получается?" 
  th "Меня саму как будто тянет к нему: он дважды пытался скрыться, и я дважды его находила."
  th "Быть может, между нами действительно что-то есть? Но что? Странные вопросы, на которые нет ответа."
  stop ambience fadeout 1
  scene bg ext_beach_day with dissolve
  play ambience ambience_boat_station_day fadein 3
  "Незаметно я оказалась рядом с пляжем."
  th "А теперь – обратно!"
  stop ambience fadeout 1
  scene black with dissolve
  "…"
  play ambience ambience_camp_center_day fadein 3
  scene bg ext_house_of_sl_day with dissolve
  "Моя пробежка подходила к концу. Я стояла на пороге нашего с Женей домика."
  show mt normal pioneer with dspr
  "Как вдруг меня встретила вожатая."
  show mt sad pioneer with dspr
  mt "Славя, Шурик куда-то делся! Электроник сказал, что до сих пор его не видел."
  sl "Может быть, он в клубе?"
  show mt surprise pioneer with dspr
  mt "На входе висит замок, он его ещё не открывал."
  sl "Хорошо, я поищу его."
  hide mt with dspr
  "Я не успела договорить, вожатая уже стала отдаляться."
  th "Надо передать это Жене."
  stop ambience fadeout 1
  play sound sfx_open_door_1
  play ambience ambience_int_cabin_day fadein 3
  scene bg int_house_of_sl_day
  show mz normal glasses pioneer
  with dissolve
  "Я вошла в домик. Женя уже проснулась и читала свою книжку, название которой я не знала."
  sl "Привет, ты в курсе, что Шурик пропал?"
  mz "И что с того?"
  th "Её безразличие немного пугает."
  sl "Ольга Дмитриевна поручила нам это! Скорее всего, она сейчас поднимет на уши весь лагерь."
  show mz angry glasses pioneer with dspr
  mz "Славь, сейчас только раннее утро, не вижу смысла в разведении паники из-за одного ботана. Найдётся он!"
  sl "Надеюсь…"
  hide mz with dspr
  "Я положила пакет с умывальными принадлежностями и переоделась в пионерскую форму."
  "Первым делом я решила проверить лес."
  th "Может, он заблудился?"
  "Подумала я и побежала в сторону леса."
  stop ambience fadeout 1
  scene black with dissolve
  "…"
  play ambience ambience_forest_day fadein 3
  scene bg ext_path_day with dissolve
  "Осмотрев лес, я дошла даже до бани. Не знаю почему, но я решила посмотреть и там, однако его нигде не было."
  stop ambience fadeout 1
  scene black with dissolve
  pause 1
  play ambience ambience_camp_center_day fadein 3
  scene bg ext_washstand_day with dissolve
  show dv normal pioneer at cright
  show us normal sport at cleft
  with dspr
  "На выходе из леса, около умывальников, я встретила двух неразлучных рыжеволосых подружек, которые, похоже, только проснулись."
  sl "Доброе утро. Вы нигде не видели Шурика?"
  us "Нет."
  show dv surprise pioneer at cright with dspr
  dv "А что такое?"
  sl "Не знаю ещё…"
  hide dv
  hide us
  with dspr
  "Ответила я и побежала дальше."
  "Думаю, как и сказала Женя, не стоит устраивать панику из-за одного кибернетика. Найдётся, надо лишь лучше искать {w},или подождать!"
  stop ambience fadeout 1
  scene black with dissolve
  pause 1

  play ambience ambience_camp_center_day fadein 3
  scene bg ext_clubs_day with dissolve
  th "А куда дальше-то? Надо было уточнить у Ольги Дмитриевны, может что-то ещё известно?"
  "Я побежала в сторону обители вожатой."
  scene bg ext_house_of_mt_day with dissolve
  play sound sfx_knock_door2
  "Встав на пороге её домика, я постучалась.{w=0.5}{nw}"
  play sound sfx_open_door_2
  extend " Не дождавшись ответа, я открыла дверь."
  stop ambience fadeout 1
  play ambience ambience_int_cabin_day
  scene bg int_house_of_mt_day with dissolve
  show pi normal pioneer with dspr
  "Внутри домика оказался Семён."
  sl "Доброе утро!{w} А Ольга Дмитриевна?.."
  "Но он молчал.{w} Более того: он смотрел будто сквозь меня."
  th "Учитывая события прошлой ночи…"
  sl "Семён?"
  "Но он продолжал так стоять и даже бровью не повёл!"
  sl "Что-то не так?"
  "Наконец он ответил:"
  me "Да нет, всё как раз так…"
  sl "Ольга Дмитриевна?.."
  me "Не знаю, когда проснулся, её уже не было."
  "Наконец он поднял свой взгляд и посмотрел в глаза."
  sl "Ладно, я ещё в одно место заскочить должна, так что увидимся на завтраке."
  "Я улыбнулась и вышла из домика, прикрыв за собой дверь."
  stop ambience fadeout 1
  play sound sfx_close_door_1
  play ambience ambience_camp_center_day fadein 3
  scene bg ext_house_of_mt_day with dissolve
  th "Время уже позднее, так что, похоже, я пропущу линейку. Ну и пусть! Поиски Шурика всё же важнее. "
  scene bg ext_admins_day with dissolve
  th "Ну в администрации его бы точно нашли, а вот в душевых стоит посмотреть." 
  "Однако, его не оказалось и там."
  scene bg ext_square_day with dissolve
  show mt normal pioneer with dissolve
  play music music_list["silhouette_in_sunset"] fadein 3
  "Я собиралась идти дальше, но встретила Олю."
  sl "Оля, привет, насчёт Шурика ничего неизвестно? Может, я не там ищу?"
  show mt sad pioneer with dspr
  mt "Нет, Серёжа сам не знает, куда бы он мог пойти. Видимо, придётся звать на помощь ребят."
  show mt normal pioneer with dspr
  mt "И ещё, Славя, на складе бардак - сходи заодно туда и приберись."

  if not sl_m_day2_sp_keys:
    sl "Я бы с радостью, но я так и не нашла свои ключи."
    show mt surprise pioneer with dspr
    play sound sfx_keys_rattle
    mt "Ну что же ты так! Ладно, возьми мои, но потом верни. Позже решим вопрос с ключами."
    "Она отдала мне свои ключи."
    show mt normal pioneer with dspr

  "Мимо нас пронёсся оставшийся кибернетик."
  show mt normal pioneer:
    linear 1.0 cright
  show el normal pioneer at cleft with dspr
  "Ольга Дмитриевна окликнула его."
  mt "Никаких известий?"
  show el sad pioneer at cleft with dspr
  el "Нет, Ольга Дмитриевна."
  "На его лице явно читалось разочарование."
  mt "Идём в столовую, скоро завтрак."
  th "Надо же! Я и не заметила, как быстро пролетело время."
  scene bg ext_dining_hall_near_day with dissolve
  show mt normal pioneer at cright
  show el normal pioneer at cleft
  with dspr
  "Мы вскарабкались по ступенькам и встали недалеко от двери."
  mt "Как думаешь, куда мог деться Шурик?"
  "Обратилась она к Электронику."
  show el sad pioneer at cleft with dspr
  el "Честно - не знаю."
  show mt sad pioneer at cright with dspr
  mt "Ну, хотя бы вечером он вернулся в домик?"
  show el serious pioneer at cleft with dspr
  el "Да, но он просто лёг спать, ничего не сказав."
  show el normal pioneer at cleft with dspr
  "К столовой начали стекаться пионеры.{w} Ольга Дмитриевна тут же подошла к ним."
  mt "Доброе утро, девочки. Вы не видели Шурика?"
  show el normal pioneer:
    linear 1.0 fright
  pause 0.5
  show dv normal pioneer at fleft
  show us normal pioneer at cleft
  with dissolve
  dv "Не видели. А что случилось-то?"
  mt "Он исчез, мы не можем его найти."
  show dv laugh pioneer at fleft with dspr
  dv "В клуб-то не забыли зайти? Первым делом там надо искать."
  th "Шутка Алисы явно была неуместной. Если Шурик потерялся, значит, он мог попасть в беду!"
  sl "Да, смотрели уже… И в клубе, и в душевых, и в бане – везде, где можно!"
  show dv normal pioneer at fleft
  show el serious pioneer at fright
  with dspr
  el "Как будто бы его и не было."
  "Добавил Электроник."
  show el normal pioneer at fright with dspr
  mt "А где тогда он ещё может быть? В библиотеке?"
  show us laugh pioneer at cleft
  show dv laugh pioneer at fleft
  with dspr
  us "Может, лодку угнал?" 
  "Влезла в разговор Ульянка."
  sl "Наверное, стоит поискать в дальних уголках лагеря."
  mt "Тогда стоит ещё раз осмотреть лес."
  show us dontlike pioneer at cleft
  show dv normal pioneer at fleft
  with dspr
  us "Может он в старый лагерь пошёл?"
  mt "Исключено. Зачем ему туда?"
  show us normal pioneer at cleft with dspr
  "Наша дискуссия была довольно долгой, даже Семён пришёл."
  hide us
  hide dv with dspr
  show mt normal pioneer:
    linear 1.0 center
  show pi normal pioneer at fleft with dspr
  "Неспешным шагом он подошёл к столовой и тут же попал под пресс Ольги Дмитриевны."
  mt "О, Семён!{w} Ты не видел сегодня Шурика?"
  me "Нет, а что такое?"
  mt "Мы его с утра не можем найти!"
  show el normal pioneer at fright with dspr
  "Сказала Вожатая и снова переключилась на Электроника. "
  mt "Но вчера же он был с тобой?"
  el "Был…"
  mt "А утром ты проснулся, а его нет?"
  "Спросила она его ещё раз, так как не услышала от него ответа в прошлый раз."
  el "Нет…"
  mt "И почему ты сразу не пошёл ко мне?"
  show el upset pioneer at fright with dspr
  el "Ну, я подумал, что, может, он раньше проснулся и умываться пошёл или ещё куда…"
  show el normal pioneer at fright with dissolve
  sl "А он вчера ничего такого не говорил?"
  el "Например?" 
  sl "Что собирается куда-то, например?"
  el "Нет…"
  me "А что такого страшного-то произошло?"
  me "Время только девять утра. Может, он прогуляться решил."
  th "«Но тогда почему мы ещё нигде его не встретили?» - хотела я сказать, но сдержалась."
  "Ребята начали затихать." 
  sl "Ты не знаешь Шурика."
  me "Не знаю, да…"
  mt "Ладно, не будем паниковать. Наверняка найдётся!"
  "Видимо, дискуссия остановлена."
  hide pi with dspr
  show mt normal pioneer:
    linear 1.0 cright
  pause 0.5
  show us grin pioneer at cleft
  show dv normal pioneer at fleft
  with dspr
  us "Но чтобы он пропустил завтрак…"
  dv "Точно!"
  "Неожиданно встряла Алиса."
  dv "Пора уже и есть идти."
  stop music fadeout 3
  hide us
  hide dv
  hide el
  hide mt
  with dissolve
  "Что ж, пожалуй, нет необходимости морить себя голодом, если Шурик действительно пошёл прогуляться."
  stop ambience fadeout 2

  scene bg int_dining_hall_people_day with dissolve
  play ambience ambience_dining_hall_full fadein 3
  "Пионеры стали заходить внутрь."
  show un normal pioneer with dspr
  sl "Привет, не занято?"
  un "Привет, садись."
  "Я села за столик с Леной."
  "Завтрак был такой же, как вчера. С разнообразием можно было и повременить, я не привередливая."
  "Я заметила, что Семён сел вместе с Алисой и Ульяной, и они что-то бурно обсуждали."
  sl "Как думаешь, куда мог деться Шурик?"
  un "Не знаю…"
  "Лена как и всегда была немногословна, к этому я уже привыкла."
  show un normal pioneer:
    linear 1.0 cright
  show mi normal pioneer at cleft with dspr
  mi "Привет, не занято? А то если занято, я пойду, поищу другой столик. Сидеть же где-то надо, ведь есть стоя тяжело. А у нас в Японии…"
  sl "Нет, не занято, садись."
  "Я поспешила вежливо остановить её."
  show mi smile pioneer at cleft with dspr
  mi "Спасибо."
  show mi normal pioneer at cleft with dspr
  "Я быстро доела завтрак и вышла из столовой."
  stop ambience fadeout 2

  scene bg ext_dining_hall_near_day with dissolve
  play ambience ambience_camp_center_day fadein 3
  "Куда бы мне пойти?"

  $ slavyana_mod__day4_map_choise__mt_house = False
  $ slavyana_mod__day4_map_choise__store = False
  $ slavyana_mod__day4_map_choise__music_club = False
label slavyana_mod__day4_map_choise:
  $ disable_all_zones()
  if ( not slavyana_mod__day4_map_choise__mt_house and ( slavyana_mod__day4_map_choise__store or slavyana_mod__day4_map_choise__music_club ) ):
    $ set_zone("me_mt_house","slavyana_mod__day4_mt_house")
  if not slavyana_mod__day4_map_choise__music_club:
    $ set_zone("music_club","slavyana_mod__day4_music_club")
  if not slavyana_mod__day4_map_choise__store:
    $ set_zone("store_house","slavyana_mod__day4_store")
  if slavyana_mod__day4_map_choise__mt_house and slavyana_mod__day4_map_choise__store and slavyana_mod__day4_map_choise__music_club:
    jump slavyana_mod__day4_after_map_choise
  else:
    $ show_map()

label slavyana_mod__day4_store:
  if slavyana_mod__day4_map_choise__mt_house:
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_clubs_day with dissolve
  elif slavyana_mod__day4_map_choise__music_club:
    scene bg ext_musclub_day with dissolve
  else:
    scene bg ext_dining_hall_near_day with dissolve
  "Мне всё ещё надо было сходить на склад и прибраться там." 
  if not sl_m_day2_sp_keys:
    "Благо, Оля дала мне свои ключи."
  scene bg ext_shed_day with dissolve
  "Подойдя к складу, я легко открыла ключами хлипкий замочек."
  th "Это скорее защита от вежливых воров. Хотя какому вору понадобиться лезть на склад за хозинвентарём?" 
#*Сюда вот предлагаю какой-нибудь бг внутренностей склада угнать <пр. корр.>*
  th "Похоже, что кому-то нужно очень хорошо здесь прибраться."
  "Я поставила валявшиеся повсюду коробки у стены, подмела пол и протёрла окна."
  "Мётлы, лопаты и грабли стояли в ряд, облокотившись об стену."
  "Надписи на банках с краской куда-то затерялись, поэтому я просто поставила их как есть на полку."
  "Повыше перекочевало всё, что могло поместиться на полках и притом не загромождать вход."
  "Закрывая склад, я услышала, как что-то покосилось и упало, но не придала этому большого значения."
  "Осталось вернуть ключи вожатой и можно продолжать поиски. Найду-ка я Олю и продолжу поиски."
  $ slavyana_mod__day4_map_choise__store = True
  jump slavyana_mod__day4_map_choise

label slavyana_mod__day4_music_club:
  if slavyana_mod__day4_map_choise__mt_house:
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_clubs_day with dissolve
  elif slavyana_mod__day4_map_choise__store:
    scene bg ext_shed_day with dissolve
  else:
    scene bg ext_dining_hall_near_day with dissolve
  "Пожалуй, если Мику сейчас у себя, мы вместе осмотрим подсобку её клуба." 
  th "Неужели там мы сможем найдём Шурика? Вот будет забавно!"
  "…"
  scene bg ext_musclub_day with dissolve
  "Подойдя поближе, я услышала игру на гитаре и пение на неизвестном мне языке."
  "Сомнений не было – Мику сейчас занята.{w} Пожалуй, зайду попозже."
  $ slavyana_mod__day4_map_choise__music_club = True
  jump slavyana_mod__day4_map_choise

label slavyana_mod__day4_mt_house:
  scene bg ext_house_of_mt_day with dissolve
  play sound sfx_knock_door2
  "Я постучалась в дверь."
  voice "Войдите."
  stop ambience fadeout 1
  play sound sfx_open_door_1
  play ambience ambience_int_cabin_day fadein 3
  scene bg int_house_of_mt_day with dissolve
  show pi normal pioneer with dspr
  "Ольги Дмитриевны внутри не оказалось, зато на кровати лежал дремлющий Семён."
  sl "А Ольги Дмитриевны нет?"
  me "Нет."
  "Мне показалось, что Семён отлынивает от поисков товарища."
  sl "А ты что делаешь?"
  "Он оглядел себя и сказал:"
  me "Лежу…"
  sl "Это я вижу.{w} Но я слышала, что тебе Ольга Дмитриевна поручила искать Шурика."
  th "Вообще я придумала это на ходу."
  th "Да, врать конечно плохо. {w}Но бездельничать ещё хуже!"
  me "Ну, да…"
  sl "И?.."
  me "Какой смысл?"
  th "Во дела!"
  me "Она уже наверняка весь лагерь вверх дном перевернула."
  me "Да и прошло не так много времени.{w} Зачем панику на корабле разводить?"
  sl "Всякое бывает…"
  "Я решила действовать решительней."
  sl "Вставай."
  me "А это обязательно?"
  sl "Да!"
  "Он с трудом поднялся с кровати, и мы вместе с ним вышли из домика."
  stop ambience fadeout 1
  play sound sfx_close_door_1
  play ambience ambience_camp_center_day fadein 3
  scene bg ext_house_of_mt_day with dissolve
  show pi normal pioneer with dspr
  "Некоторое время мы просто стояли на пороге и грелись в лучах летнего солнца."
  me "Куда идём?"
  "Этот вопрос меня немного удивил."
  sl "Надо поискать везде."
  scene bg ext_library_day with dissolve
  "Первым делом я решила проверить библиотеку."
  stop ambience fadeout 1
  play sound sfx_open_door_2
  play ambience ambience_int_cabin_day fadein 3
  play music music_list["take_me_beautifully"] fadein 3
  scene bg int_library_day with dissolve
  show mz normal pioneer glasses
  with dspr
  "Я решила спросить у Жени. Семен остался стоять у выхода."
  sl "Как продвигаются поиски Шурика?"
  mz "Никак."
  sl "Почему?"
  mz "А почему ты думаешь, что он вообще потерялся?"
  sl "Ну как же! За всё это время он так и не появился."
  show mz rage pioneer glasses with dspr
  mz "Не появился - и прекрасно! Он мне давно ещё надоел."
  sl "Ну как ты так можешь? Весь лагерь ищет своего товарища..."
  show mz normal pioneer glasses with dspr
  mz "Ну ты и своего Семёнчика привлекла, я погляжу."
  "Я засмущалась."
  sl "Он не мой, просто я пришла в домик Ольги Дмитриевны, а там Семён отлынивает от поисков, вот я его и взяла, чтобы хоть как-то поучаствовал в жизни лагеря."
  "Это прозвучало так, будто я оправдываюсь."
  mz "Ладно, Шурика я не видела. Поищите в другом месте."
  hide mz
  show pi normal pioneer
  with dspr
  "Я подошла к выходу, где стоял семен."
  me "И как?"
  sl "Нет…"
  "…"
  stop ambience fadeout 3
  scene bg ext_dining_hall_near_day with dissolve
  "Столовая. Чудное зрелище, когда вокруг никого нет."
  scene bg int_dining_hall_day with dissolve
  play ambience ambience_dining_hall_empty fadein 3
  "Внутри она была так же пуста, как и снаружи."
  "От поваров ничего не удалось узнать. Меня бы очень даже поразило, если бы они мне сообщили точное местоположение Шурика."
  "…"
  scene bg ext_aidpost_day with dissolve
  play ambience ambience_camp_center_day fadein 3
  "Я зашла внутрь одна, надеясь на то, что Семён подождёт снаружи."
  "Но…"
  "Виола тоже не знает, где Шурик."
  "…"
  scene bg ext_playground_day with dissolve
  "На спортивной площадке пионеры играли в футбол."
  th "Может, хотя бы кто-то из них видел Шурика?"
  "…"
  th "Нет"
  "…"
  scene bg ext_clubs_day with dissolve
  show pi normal pioneer with dissolve
  me "Ты серьёзно считаешь, что он может быть тут?! Мне кажется, это первое место, где стоило искать…"
  th "Кажется, Семён начинает догадываться, что я не просто так мотала его по противоположным углам лагеря."
  sl "Зайдём."
  stop ambience fadeout 3
  play sound sfx_open_door_clubs_2
  $ persistent.sprite_time = "day"
  scene bg int_clubs_male_day with dissolve
  show pi normal pioneer with dissolve
  "Здесь не оказалось даже Электроника."
  "Я решила проверить соседнее помещение."
  "Семён проследовал за мной."
  $ persistent.sprite_time = "sunset"
  scene bg int_clubs_male2_night with dissolve
  show pi normal pioneer with dissolve
  "Что ж. И тут его нет."
  th "Ну и где ещё может быть Шурик?"
  th "Если он действительно решил играть в прятки, ему пора бы уже покинуть укрытие."
  sl "И здесь нет…"
  me "А чего ты ожидала?{w} Что он в шкафу сидит?"
  "Мне показалось это несколько грубым."
  sl "Ну!"
  me "Извини, извини… {w}Просто… серьёзно!"
  sl "Я понимаю… {w}Но надо ведь проверить все варианты."
  me "Слушай, а ты-то что думаешь?"
  sl "Насчёт исчезновения Шурика?"
  me "Да."
  th "Настала моя очередь придумывать шутки!"
  sl "Может быть, он гулял в лесу и его там поймал Леший."
  "Мне показалось это забавным, и я рассмеялась."
  me "Неправдоподобно как-то… Я думаю, в этих краях киднеппинг не очень распространённое явление."
  th "Откуда в нём теперь такая серьёзность?"
  sl "Да, наверное… {w}Сейчас не время для шуток!"
  me "Не грусти! {w}Найдётся он!"
  sl "Надеюсь…"
  "Я натянуто улыбнулась."
  "Теперь надо как-то выйти из этой неловкой ситуации в этом тесном помещении."
  sl "Ладно, у меня ещё кое-какие дела."
  me "Увидимся."
  stop music fadeout 3
  $ persistent.sprite_time = "day"
  scene bg ext_clubs_day with dissolve
  "Я выпорхнула и оставила дверь открытой."
  th "А, собственно, какие у меня ещё дела?"
  $ slavyana_mod__day4_map_choise__mt_house = True
  jump slavyana_mod__day4_map_choise

label slavyana_mod__day4_after_map_choise:
  "…"
  play sound sfx_dinner_horn_processed
  th "Как быстро пробежало время!"
  "Я отправилась в столовую."
  scene bg ext_square_day with dissolve
  show mt normal pioneer with dissolve
  "По пути на площади я встретила Олю."
  mt "Ну как поиски?"
  sl "Всё так же…"

  if not sl_m_day2_sp_keys:
    play sound sfx_keys_rattle
    "Я отдала ей ключи."

  show mt sad pioneer with dspr
  mt "Уже обед, а мы до сих пор не нашли его. Нужно звонить в милицию!"
  show mt sad pioneer:
    linear 1.0 cright
  show el normal pioneer at cleft with dissolve
  "Мы снова встретили Электроника, который, похоже, даже не собирался идти на обед."
  mt "А как же обед?"
  show el serious pioneer at cleft with dspr
  el "Я обязательно приду, но не сейчас!"
  show el sad pioneer at cleft with dspr
  mt "Нет, прямо сейчас ты пойдёшь с нами и нормально пообедаешь."
  "Электроник молча присоединился к нам."

  scene bg int_dining_hall_people_day with dissolve
  play ambience ambience_dining_hall_full fadein 3
  "В столовой было ещё не так много народу, и мы смогли найти свободный столик на четверых."
  "Еда сегодня практически ничем не отличалась от вчерашней."
  "Когда мы уже расселись, в столовую заглянул Семён."
  show mt normal pioneer at center
  show el normal pioneer at left
  with dissolve
  mt "Семён, иди к нам."
  "Он положительно кивнул и отправился за своей порцией."
  show pi normal pioneer at right with dissolve
  "Когда он, наконец, сел, Ольга Дмитриевна начала разговор:"
  mt "Ну и что вы думаете?"
  me "О чём?"
  mt "О Шурике!{w} Уже обед, а его всё нет."
  sl "Мы обыскали весь лагерь."
  th "Точнее я, а Семён просто ходил со мной."
  show el upset pioneer at left  with dspr
  el "Я обошёл весь окрестный лес."
  "Оля посмотреля на Семёна"
  me "И я… {w}помогал."
  show mt surprise pioneer at center  with dspr
  mt "Надо звонить в милицию!"
  me "Может, хотя бы до вечера подождём?"
  th "Семёна, похоже, это обстоятельство абсолютно не волновало."
  me "Домой он поехал, например…"
  mt "Не может быть!{w} Шурик живёт отсюда в тысячах километров."
  me "Ну так на поезде."
  mt "До ближайшей станции…"
  "Она смутилась."
  show mt normal pioneer at center with dspr
  mt "Далеко…"
  "На такой неполный ответ последовал логичный вопрос:"
  me "Далеко – это сколько?"
  mt "Это много."
  sl "Значит, нужно идти глубже в лес! Может, он заблудился!"
  el "У Шурика всегда с собой компас."
  "Вмешался Электроник."
  th "Не думаю, что Шурик настолько хорошо ориентируется в нашем лесу, что при помощи компаса смог бы выбраться из него. {w}Тем более, к компасу нужна карта…"
  show mt surprise pioneer at center  with dspr
  mt "И в милицию! {w}В милицию этим же вечером!"
  me "Ну до вечера…"
  th "Что он имел ввиду?"
  me "Ещё далеко до вечера, я в этом смысле."
  show mt sad pioneer at center  with dspr
  mt "Если он правда пропал, то нельзя медлить!"
  th "Дальнейшие поиски в черте лагеря ни к чему не приведут, мы обыскали его полностью."
  sl "Мы не можем пока этого знать."
  mt "Ну а где он тогда, где он?"
  th "Не знаю…"
  "Я почувствовала себя виноватой."
  me "В любом случае мы сделали всё от нас зависящее, теперь остаётся только ждать."
  "Я взглянула на Семёна."
  stop ambience fadeout 2
  scene black with dissolve
  "…"
  scene bg ext_dining_hall_near_day with dissolve
  "После обеда я решила зайти в домик."
  th "Я уже и так достаточно набегалась за день, да и новых заданий не прибавилось."
  scene bg int_house_of_sl_day with dissolve
  play ambience ambience_int_cabin_day fadein 3
  "Вернувшись в домик, я легла на кровать, но быстро встала."
  th "Я предпочитаю дневному сну активный отдых."
  th "А лучший отдых – смена деятельности."
  "Я вспомнила, что когда-то бабушка обучила меня вышиванию."
  th "Стоит вернуть утерянные навыки, заодно и время проскочит."
  th "Где-то у меня были нитки, иголка и бабушкин платочек, которые я привезла из дома…"
  stop ambience fadeout 2
  scene black with dissolve
  "…"
  scene bg int_house_of_sl_day with dissolve
  play ambience ambience_int_cabin_day fadein 3
  "Когда я закончила, на платочке красовались жёлтые, зелёные и красные цветочки."
  "Но было только пол пятого. Нужно было чем-то занять оставшиеся полтора часа."
  "Идеи решительно не хотели лезть в голову, и я решила пройтись по лагерю."
  scene bg ext_house_of_sl_day with dissolve
  play ambience ambience_camp_center_day fadein 3
  "Выйдя из домика, я вдохнула свежего воздуха с улицы."
  th "Прекрасная погода!"
  "Подумала я и направилась к площади."
  scene bg ext_square_day with dissolve
  show un normal pioneer with dissolve
  "На площади сидела Лена с книжкой в руках. Остальных же пионеров нигде не было видно."
  sl "Привет Лена, что читаешь?"
  un "Да так…"
  "Я взглянула на обложку"
  th "«Унесённые ветром»…"
  th "Я слышала когда-то, но ничего о ней не знаю."
  sl "Интересно?"
  un "Да."
  sl "Расскажешь о чём там?"
  un "Ну… О любви."
  sl "Надо будет тоже почитать."
  th "Не знаю, зачем это сказала, ведь свободного времени у меня бывает очень мало."
  sl "Тебе, наверное, скучно так каждый день сидеть с книжкой. Давай завтра сходим куда-нибудь вместе?"
  show un smile pioneer with dissolve
  un "Давай."
  "Она улыбнулась."
  hide un with dspr
  "Я уже собиралась уходить, как краем глаза заметила, что Алиса с Ульяной куда-то направлялись, но на полпути Ульяна остановилась и пошла в сторону медпункта."
  th "Наверняка пакость какую-нибудь замышляют."
  th "Хотя… Подозревать без веских причин нельзя."
  th "Стоит ли проследить? {w}А если заметят?"
  th "Нет, я не привыкла подсматривать. {w}Но если что-то случится, первые подозрения падут именно на них."
  "Я встала и вернулась в домик."
  scene bg int_house_of_sl_day with dissolve
  play ambience ambience_int_cabin_day fadein 3
  "До ужина был ещё час времени. Может, стоит поискать Ольгу Дмитриевну и спросить, не нужна ли ей моя помощь?"
  play sound sfx_open_door_1
  show mz normal pioneer glasses with dspr
  "Но вдруг дверь распахнулась и на пороге стояла Женя."
  "Она ринулась к своему шкафчику и принялась искать."
  "Из шкафчика полетели её личные вещи, одежда, книги."
  sl "Что ищешь?"
  show mz angry pioneer glasses with dspr
  mz "Не твоё дело."
  sl "Может, я помогу?"
  mz "Не поможешь."
  sl "А может моя помощь всё-таки пригодится?.."
  "Женя достала небольшую цилиндрическую коробку и, убедившись, что она пуста, бросила на пол и легла на кровать."
  show mz normal pioneer glasses with dspr
  mz "Ладно, если хочешь помочь… Можешь мне принести кое-что личное?"
  mz "Ты, наверное, уже и сама поняла. Поищи в медпункте, там они должны быть. {w}Принесёшь?"
  "Отказывать подруге нельзя."
  hide mz with dspr
  "…"
  scene bg ext_houses_day with dissolve
  play ambience ambience_camp_center_day fadein 1
  th "Как мне обратиться к медсестре, чтобы не навязчиво, и в то же время она меня поняла?"
  scene bg ext_aidpost_day with dissolve
  "Всю дорогу я продумывала грядущий диалог."
  th "Я, конечно, могла и отказаться, но подруга в тяжёлой ситуации."
  play sound sfx_open_door_2
  stop ambience fadeout 3
  scene bg int_aidpost_day with dissolve
  play music music_list["smooth_machine"] fadein 3
  show pi normal pioneer with dissolve
  "Когда я была готова и открыла дверь, внутри меня ждал только Семён."
  "Меня это смутило, но я старалась не подавать виду."
  sl "Ой, привет! А медсестры нет?"
  me "Привет. Нет. Я за неё."
  sl "Хорошо. {w}А мне бы…"
  th "Зачем? Зачем я это произнесла? Что я ему теперь скажу?"
  me "Что?"
  "Семён, похоже, заметил мои колебания."

  if sl_m_day2_go_with_sp:
    "Я решила временно отвести разговор в сторону, пока не придумаю выход из этой ситуации."
    sl "Кстати, Семён…"
    me "Что?"
    sl "Я тут недавно свои ключи, кажется, потеряла. Ты не видел?"
    me "Да, вот, я вчера их нашёл возле столовой, хотел тебе отдать, но забыл…"
    "Он засмущался и его глаза метались в разные стороны."
    me "Вот."
    th "Неужали он пролежали там так долго?"
    "Я серьёзно посмотрела на него: если он сделал что-то нехорошее, пусть признается."
    "Но он не проронил ни слова."
    sl "Спасибо."
    me "Так зачем приходила?"
    me "Что-то болит?"

  else:
    th "Чем быстрее кончится диалог – тем быстрее я уйду."

  sl "Да нет, ничего…"
  me "Если что - ты говори! {w}Меня сюда и посадили, чтобы всех лечить."
  "Он широко улыбнулся."
  sl "Да нет… {w}То есть да, но нет."
  th "Как бы правильнее попросить..."
  me "Ну, так чем могу помочь?"
  sl "Ты?.. {w}Думаю, ничем."
  th "Кажется это плохая идея."
  "Я уже собралась уходить, но прийти к подруге ни с чем было хуже позора перед Семёном, и тогда я решила:"
  sl "Хотя… {w}Можешь выйти на минутку?"
  me "Хорошо…"
  hide pi with dspr
  "Дождавшись, когда он выйдет, я проверила, не подсматривает ли он и прильнула к шкафу."
  "Я нашла ничем не примечательную коробку и взяла оттуда обычные гигиенические изделия."
  "Чтобы он ничего не увидел, я положила их в пакет и вышла."
  me "Удачи!"
  sl "Спасибо!"
  stop music fadeout 2
  scene black with dissolve
  "…"
  scene bg ext_houses_day with dissolve
  "Это даже хорошо, что там не было медсестры. {w}Конечно, это нужно не мне, а Жене, но не стану же я её подводить?"
  scene bg int_house_of_sl_day with dissolve
  play ambience ambience_int_cabin_day fadein 3
  show mz normal pioneer glasses with dissolve
  mz "Спасибо."
  "Я молча отдала ей пакет."
  hide mz with dspr
  "Я взглянула на часы."
  "Время уже приближалось к вечеру, и до ужина было недалеко."
  "Я решила вспомнить, где я ещё не была."
  th "За сегодняшний день я не была только на стоянке и сцене."
  th "В остальных местах искать было бессмысленно, так как, скорее всего, там уже искали."
  "Я решила пройтись до сцены, а затем заглянуть на стоянку."
  "…"
  scene bg ext_stage_big_sunset with dissolve
  play ambience ambience_camp_center_day fadein 3
  play music music_list["miku_song_flute"] fadein 3
  "Подходя к сцене, я услышала, как кто-то играет на гитаре и поёт на непонятном языке. {w}Я решила подойти поближе."
  "Конечно же это была Мику, а на лавочке сидела Лена и слушала её."
  th "Мику, похоже, вкладывалась полностью в музыку и слова произносимые в такт мелодии, поэтому я не стала им мешать и, посидев ещё какое-то время, пошла искать дальше. {w}Всё равно Шурик бы здесь не смог спрятаться."
  stop music fadeout 3
  scene bg ext_square_day with dissolve
  "На площади я снова встретила Ольгу Дмитриевну, которая, похоже, никуда не торопилась. {w}Время уже было близко к ужину, поэтому мы направились в столовую."
  scene bg int_dining_hall_people_day with dissolve
  play ambience ambience_dining_hall_full fadein 3
  "Когда звонок прозвенел, мы уже зашли внутрь."
  "Пионеры начали постепенно занимать места, поэтому я выстояла очередь за едой и села за столик с Олей."
  "Естественно, с Шуриком ничего не прояснилось, и весь ужин мы болтали о мелочах."
  "…"
  scene bg ext_path2_day with dissolve
  play ambience ambience_forest_day fadein 3
  "После ужина я решила напоследок ещё раз пройтись по лесу. {w}{nw}"
  play sound sfx_muffled_explosion
  extend "Но не успела, услышав взрыв со стороны площади."
  th "Ну и что они на этот раз учудили?"
  th "Сомнений нет, это точно Алиса с Ульяной."
  stop ambience fadeout 2
  scene bg ext_square_day with dissolve
  play music music_list["you_won_t_let_me_down"] fadein 3
  "На площади уже собралась приличная толпа пионеров во главе с Ольгой Дмитриевной, которая отчитывала Алису."
  show us surp2 pioneer at right 
  show dv smile pioneer at left
  show mt angry pioneer ar center
  with dissolve
  mt "Теперь понятно…{w} Из чего бомбу делала?!"
  show dv normal pioneer at left with dspr
  dv "Активированный уголь, селитра и сера!"
  th "Откуда она нашла селитру в лагере? {w}Небось на склад пробралась, но я же его закрыла, разве нет?"
  mt "И почему именно памятник?{w} Чем тебе помешал уважаемый, заслуженный человек? Борец за права…"
  "..."
  stop music fadeout 3
  "Ольга дмитриевна еще долго отчитывала Двачевскую{w}, как вдруг на площадь выбежал электроник, размахивая чемто в руке"
  hide dv
  hide mt
  hide us
  show el smile pioneer at center with dissolve
  el "Нашёл! Нашёл!"
  "Все повернулись к нему."
  el "Вот!"
  "Электроник победоносно потряс предметом над головой."
  play music music_list["into_the_unknown"] fadein 3
  el "Это ботинок Шурика!"
  show mt normal pioneer at right with dissolve
  mt "Так, успокойся! {w}Расскажи подробно, где ты его нашёл!"
  show el normal pioneer at center with dspr
  el "В лесу. {w}На тропинке в старый лагерь!"
  "По рядам прошёл какой-то шёпот."
  all "Старый лагерь… Старый лагерь…"
  th "Старый лагерь… {w}Об этом месте ходит много слухов."
  show mt surprise pioneer at right with dspr
  mt "Ты уверен?"
  el "Абсолютно!"
  me "А что такого в этом старом лагере?"
  "Неожиданно ворвался в разговор Семён."
  mt "Да ничего такого на самом деле…"
  "Она запнулась."
  el "Одна из легенд «Совёнка» гласит, что там живёт привидение молодой вожатой, которая влюбилась в пионера, но, не найдя взаимности, покончила с собой…"
  show us laugh pioneer at left with dissolve
  us "Сделала харакири кухонным ножом. {w}А мальчика этого на следующий день сбил автобус!"
  "Ульяна выбежала из толпы."
  me "Автобус?"
  el "Но наука не допускает существования привидений, поэтому опасаться там нечего!"
  show mt normal pioneer at right with dspr
  mt "Всё равно кто-то должен туда пойти!"
  "Количество пионеров заметно поубавилось. Явно никто не хотел быть добровольцем."
  sl "Ольга Дмитриевна, ночь уже почти! Может, завтра?"
  hide us
  hide el
  with dissolve
  show mt normal pioneer:
    linear 1.0 cright
  show pi normal pioneer at cleft with dissolve
  mt "А если ночью… {w}ночью с ним что-нибудь случится… {w}Нет! Сегодня! Сейчас!"
  me "Кстати, а где это?"
  "Электроник примерно объяснил дорогу и рассказал про историю старого лагеря."
  show mt normal pioneer at cright with dissolve
  "Вожатая пристально посмотрела на Семёна."
  me "Если вы думаете, что я…"
  mt "Ты один здесь остался из мужчин."
  th "Действительно… Электроник ведь уже ушёл!"
  "Похоже, Семёну теперь в любом случае придётся идти в старый лагерь." 
  th "А вдруг ему нужна будет помощь?"

  menu:
    "Не обращать внимания":
      "Семён не маленький, и сам сможет."
      me "Я же не пойду туда один?!"
      th "И впрямь как маленький! Чего там бояться-то?"
      "Оля призадумалась."
      stop music fadeout 3
      mt "Пожалуй, ты прав… {w}Тогда завтра с утра пойдём все вместе."
      "Похоже, это всё на сегодня."
      "…"
      scene bg int_house_of_sl_day with dissolve
      play ambience ambience_int_cabin_day fadein 3
      "Я зашла в домик. До сна ещё было время, поэтому я заскочила, чтобы записать мысли в дневник."

      # Дневник
      show bknt_clear at truecenter with dspr
      play sound_loop pen_write
      show bknt_w10 at truecenter with dissolve2
      $ persistent.sl_m_bknt10 = True
      th "Сегодня был очень необычный день. Буквально с утра пропал наш товарищ – Шурик." 
      th "Весь день я только и делала, что искала его. {w}Кроме меня активно в поисках участвовали и другие ребята, особенно Электроник. Ведь они вместе с Шуриком каждый день что-то конструируют в кружке кибернетики."

      th "Но также мне сегодня помогал и Семён, во всяком случае, мы вместе обошли лагерь." 
      
      th "После ужина Алиса и Ульянка хотели взорвать памятник Генде. До сих пор не могу вспомнить, кто он такой, но ведь это не повод его взрывать!"
      th "Потом на площадь неожиданно забежал Электроник с ботинком Шурика в руке. По его словам, он нашёл его на дороге в старый лагерь. Не знаю, чем бы это всё кончилось, но Семён отказался идти туда в одиночку. Хотя я его понимаю. Он здесь совсем недавно, а его уже посылают на такое рискованное задание. (остановка) Может, стоило отправиться вместе с ним?"
      th "Ольга Дмитриевна сказала, что завтра отправимся все вместе. Наверное, так даже лучше."
      stop sound_loop
      hide bknt_clear
      hide bknt_w10
      with dspr
      # Конец дневника

      $ persistent.sprite_time = "night"
      $ night_time()
      scene bg int_house_of_sl_night with dissolve
      play ambience ambience_int_cabin_night fadein 3
      "Я закончила писать и посмотрела на часы."
      "Время было 21:15."
      th "Раньше ляжешь – раньше встанешь."
      "Подумала я, разделась и легла в постель."
      "Я долгое время не могла уснуть, Женя успела прийти и лечь спать."
      "Но спустя какое-то время меня начало клонить в сон. {w}И я, наконец, заснула."
      jump slavyana_mod__day4__without_pi

    "Вызваться помочь":
      $ sl_m_lp += 2

  sl "Я пойду с ним!"

  th "Сегодня он помог мне осмотреть лагерь."
  if not sl_m_day2_sp_keys:
    th "Он нашёл мои ключи, кто знает, что бы могло произойти, если бы они попали в плохие руки? Так он хотя бы вернул их."
  else:
    th "Сегодня он помог мне осмотреть лагерь."
  th "Я сегодня заходила в медпункт, хорошо, что он там был. Даже и не знаю как бы мне было стыдно говорить это нашей медсестре с её постоянными намёками."

  mt "Вот и отлично! Вдвоём веселее."
  me "Ты уверена?"
  "Спросил он меня шёпотом. {w}Но я лишь улыбнулась."
  mt "Отлично! Тогда удачи вам."
  me "Она нам пригодится…"
  play ambience ambience_camp_center_day fadein 3
  stop music fadeout 3
  hide mt with dissolve
  show pi normal pioneer:
    linear 1.0 center
  "Вожатая и девочки попрощались и разошлись. {w}Мы остались с Семёном одни на площади."
  th "Уже темнеет, наверное стоит взять фонарик.{w} Да и в помещениях он явно пригодится"
  sl "Подожди минутку, я за фонариком сбегаю."
  scene bg ext_houses_day with dissolve
  th "Мы пойдем ночью...{w} В заброшенный лагерь...{w} Вдвоем...{w} Надеюсь Семён знает на что согласился."
  th "Вдвоем всяко лучше, чем отпускать его одного."
  $ persistent.sprite_time = "day"
  $ day_time()
  scene bg ext_square_day with dissolve
  "На лавочке меня ждал Семён."
  show pi normal pioneer with dissolve
  sl "Вот и я!"
  "Я улыбнулась и протянула ему фонарик."
  sl "Пойдём?"
  $ persistent.sprite_time = "night"
  scene bg ext_path2_night 
  with dissolve
  $ night_time()
  play ambience ambience_forest_night fadein 3
  play music music_list["door_to_nightmare"] fadein 3
  "Уже совсем стемнело."
  "Конечно, я ориентировалась в лесу достаточно хорошо. {w}Даже ночью."
  "Но сама мысль о том, что мы идём в старый лагерь, угнетала. {w}То и дело слышались странные шорохи, трещали упавшие ветки."
  "Где-то вдалеке изредка ухала сова."
  th "Но со мной шёл Семён, и казаться в его глазах трусливой блондинкой мне совсем не хотелось."
  "Мы шли дальше."
  show pi normal pioneer with dissolve
  me "А ты совсем не боишься?"
  sl "В смысле?"
  "Я еле заметно улыбнулась."
  me "Ну ночь, лес, старый лагерь…"
  th "Он хочет только сильнее запугать меня?"
  sl "Да, не по себе, конечно, немного."
  me "Немного?"
  sl "А ты что, боишься?"
  me "Нет… Ну, то есть да, конечно, это же естественная реакция человека в такой ситуации."
  "Семён тоже старался скрыть страх, и я его понимаю. Надеюсь, мы быстро найдём Шурика."
  sl "Понятно."
  hide pi with dspr
  "…"
  window hide
  with fade
  window show
  "Тропинка становилась всё у́же, теснимая по краям деревьями и кустарниками."
  "Чем дальше мы заходили в лес, тем темнее становилось."
  "В один момент луна совсем пропала из вида, и всё погрузилось в кромешный мрак, стало ещё страшнее."
  "Но вот луна вышла из-за туч. Лучше не стало, но теперь хотя бы чуточку светлее."
  th "Семёну, наверное не так страшно, поэтому и я не должна подавать виду."
  "Наконец вдалеке показался просвет, и через минуту мы вышли на поляну…"
  stop meusic fadeout 3
  stop ambience fadeout 2
  scene bg ext_old_building_night with dissolve
  play ambience ambience_old_camp_outside fadein 3
  play music music_list["sunny_day"] fadein 5
  "На ней стояло жуткое здание старого лагеря – ветхое, размытое дождями и изрядно потрёпанное временем."
  th "Наверное, раньше детишкам здесь нравилось. Не то, что сейчас!"
  "От него веяло призрачным холодом. Как будто призрак той вожатой до сих пор бродит там."
  "Но делать нечего, думать надо было раньше."
  "Я уверенно схватила Семёна за руку."
  show pi normal pioneer with dissolve
  sl "Чтобы не так страшно…"
  "Я попыталась изобразить улыбку."
  "Он сжал руку крепче."
  th "Зачем он вообще сюда отправился? И точно ли сюда? {w}Может, с ним действительно что-то случилось?"
  "Я решила уточнить у Семёна."
  sl "Пойдём?"
  me "Ну, да, наверное…"
  th "Пусть он первый пойдёт, раз не боится."
  "Но мы так и стояли."
  hide pi with dissolve
  scene bg ext_old_building_night_moonlight with dissolve2
  "Вдруг луна выглянула из-за туч, осветив здание старого лагеря."
  "И всё будто прояснилось. {w}Доски стали новее, крыша была снова покрашена, а в окне, как мне показалось, прошёл ребёнок."
  "От этого стало жутко. {w}Но теперь наш путь стал светлее."
  "Я решила нарушить тишину, чтобы отбросить все невесёлые мысли."
  show pi normal pioneer with dissolve
  sl "Наверное, тут раньше здорово было."
  "Семён внимательно посмотрел на меня."
  me "Наверное. Пойдём?"
  sl "Да…"
  hide pi with dissolve
  "Наконец Семён зашагал вперёд."
  "Мы шагали медленно, осторожно, выверяя каждый шажок, чтобы, не дай бог, не наступить на что-то и не пораниться."
  "Мы приблизились к старой горке, прошли мимо старой покосившейся карусели."
  "Трава в некоторых местах доходила до пояса, так что любое неверное движение могло привести к сломанным ногам или рукам."
  "Наконец мы добрались до входа, и Семён посветил фонарём внутрь."
  "Тьма, смотревшая на меня оттуда, была куда страшнее, чем замогильный вид снаружи – там хотя бы ярко светила луна."
  stop ambience fadeout 2
  "Семён шагнул через порог."
  scene bg int_old_building_night with dissolve
  "Внутри старый лагерь походил на детский сад."
  show pi normal pioneer with dissolve
  me "Да уж…"
  "Свет фонаря прошёлся по стене, вылавливая из темноты всё новые останки былой детской радости. Повсюду лежали старые игрушки, одна из них, как мне показалось, смотрела прямо на меня."
  sl "Жутковато."
  "Я не заметила, как буквально вжалась в Семёна."
  me "Может, не стоило сюда ночью идти?"
  th "Как ты вовремя!"
  "Подумала я."
  sl "Наверное."
  me "Вернёмся?"
  th "Шурик в беде, ему нужна наша помощь!"
  sl "Нет, ну как же! А Шурик?"
  me "Да уж, Шурик… И чего он вообще сюда полез? Может, его вообще тут нет?"
  sl "А где он ещё может быть?"
  me "Не знаю. Волки его съели, например."
  th "Ну волки тут уж точно не водятся."
  sl "Не говори так!"
  "Я отошла от Семёна на шаг, на большее я была неспособна."
  "Похоже это на него подействовало."
  me "Ладно-ладно, волков тут, допустим, не водится."
  me "Ну раз уж пришли, давай искать."
  hide pi with dspr
  "…"
  window hide
  with fade
  window show
  "Мы обыскали все помещения старого лагеря: игровые комнаты, спальни, столовую и кухню, туалеты; Семён даже заглянул в кладовку."
  "Когда я посмотрела себе под ноги, то обнаружила старую куклу."
  show pi normal pioneer with dissolve
  sl "Смотри."
  "Я подобрала её и протянула Семёну."
  "Вид у неё был ужасный. У неё не было руки и глаза, а отовсюду торчали нитки"
  me "Ну и?"
  sl "Жалко…"
  me "Что жалко? Куклу?"
  sl "Да."
  me "А что её жалеть?"
  sl "Кто-то когда-то с ней играл, а потом вот так вот бросил, забыл, и она столько лет здесь одна – и в дождь, и в холод."
  me "Да, наверное."
  "Он взял куклу и осмотрел её."
  me "Ульянке подаришь."
  "Я рассмеялась. {w=0.5}{nw}"
  play sound sfx_wind_gust
  extend "Но внезапно подул ветер, напевая какую-то неведомую ораторию."
  play sound sfx_bodyfall_1
  with vpunch
  show pi normal pioneer:
    linear 1.0 ypos 2.0
  "Семён отпрыгнул, оступился и с грохотом упал."
  "Я мигом бросилась к нему."
  show pi normal pioneer:
    linear 1.0 ypos 1.0
  sl "Живой?"
  me "Да, вроде…"
  "Он зацепился за крышку люка."
  me "Ведь мы туда не полезем, да?"
  th "Как бы нам не было сейчас страшно, Мы пришли сюда не просто так."
  me "Ну вот, ещё не хватало в диггеров играть…"
  "Я не совсем поняла его, но не стала переспрашивать."
  "Я осмотрела люк. {w}Вниз на пару метров спускалась ржавая металлическая лестница, упирающаяся в грязный бетонный пол."
  "Семён свесил ноги в люк и посветил внутрь."
  me "И что там?"
  sl "Кажется, я слышала, что под старым лагерем есть бомбоубежище."
  th "По крайней мере, эту легенду мне рассказала Ульянка, которая обладает каким-то чудесным даром узнавать секреты."
  me "Бомбоубежище? {w}И что Шурик там забыл?"
  sl "Не знаю."
  th "Может это и не он открывал, но вход к люку явно был расчищен, указывая на то, что кто-то был здесь очень недавно."
  me "Ладно, я лезу первым, если всё в порядке, ты – за мной."
  sl "А что может быть не в порядке?"
  me "Ну, не знаю… Крысы, например. Боишься крыс?"
  th "Это испугало меня ещё сильней."
  "Семён вздохнул и начал спускаться вниз."
  hide pi with dspr
  "…"
  window hide
  scene cg d4_catac_sl 
  with dissolve
  play ambience ambience_catacombs fadein 3
  window show
  "Мы медленно пробирались вперёд, держась за руки."
  "В кромешной темноте фонарь помогал не сильно, лишь изредка освещая куски старых газет и валяющийся тут и там металлолом."
  "Вся эта обстановка угнетала меня, и я вцепилась в его руку сильнее."
  sl "Далеко нам ещё?"
  "Грустно спросила я."
  me "Далеко от чего? Не имею ни малейшего представления."
  sl "Ладно…"
  "И тут же перед нами словно из ниоткуда выросла массивная металлическая дверь."
  $ persistent.sprite_time = "night"
  scene bg int_catacombs_door with dissolve
  sl "Ой…"
  "Он подёргал за ручку, но не смог открыть."
  me "Готова?"
  sl "Не знаю…"
  th "К чему я должна быть готова? Там сидит Шурик? Там портал в иной мир? Или просто комната?"
  "Колесо сделало несколько оборотов, ужасно скрипя при этом, и, наконец, замолкло, прокрутившись до конца."
  play sound sfx_open_metal_hatch
  "Он с силой дёрнул дверь и она открылась. За ней действительно была какая-то комната…"
  $ persistent.sprite_time = "sunset"
  scene bg int_catacombs_living with flash
  "Эта комната оказалась бомбоубежищем."
  "Когда мы вошли, внезапно включился свет, что изрядно напугало меня."
  th "Хотя вполне возможно, что здесь существуют какие-то источники автономного питания."
  th "Здесь было всё, чтобы поддерживать длительное существование людей во время войны: костюмы химзащиты, противогазы, сухпайки и канистры с водой."
  "В дальнем углу стоял стол с какими-то приборами. {w}Которыми, скорее всего, так и не воспользовались. Более того, даже никто не заходил сюда ни разу после постройки."
  "Я вспомнила про Шурика, но его здесь, к сожалению, не оказалось."
  show pi normal pioneer with dissolve
  me "Ну, тут Шурика точно нет."
  sl "А был?"
  me "Не знаю. Но если бы был, то не мог же он просто испариться."
  "Он окинул помещение взглядом и его взор остановился на ещё одной двери."
  me "Может быть там?"
  "Он попытался открыть её, но не получилось."
  th "Приехали."
  sl "А вдруг он её запер с той стороны?"
  me "Но зачем?"
  sl "Не знаю…"
  th "Если он её закрыл, значит, он не хочет чтобы его нашли. Но зачем ему это нужно?"
  play sound sfx_metal_door_handle_rattle
  "Он снова надавил на неё, но она лишь глухо скрипнула."
  "Я стала искать что-нибудь, что помогло бы нам открыть её."
  "Открыв один из ящиков, я нашла фомку."
  sl "На вот, может, этим?"
  "Он повертел её в руках и подцепил ею дверь."
  play sound sfx_insert_crowbar_door
  me "Давай попробуем."
  play sound sfx_fall_metal_door
  "Он навалился, и дверь начала поддаваться, после чего с громким шумом упала на пол."
  "Я посветила в проход фонарём. Там был коридор."
  sl "Там такой же коридор."
  me "Да уж… Тут прямо целый лабиринт."
  sl "Идём?"
  me "Подожди…"
  "Он сел на кровать и вытер пот со лба наволочкой."
  me "Сейчас, отдышусь немного."
  th "Похоже, этот трюк потребовал у него много сил."
  "Я села рядом. От нечего делать решила осмотреть узор плитки."
  me "Ты бы фонарь пока выключила…"
  sl "Ах, да…"
  "Рядом с Семёном я потихоньку забыла, где мы, и даже забыла выключить фонарь."
  "Румянец выступил у меня на щеках."
  th "О чём я думаю? Нам надо поскорее спасти Шурика."
  me "Жуть какая-то…"
  "Я ещё чуть подсела поближе. Всё же вместе было уже не так страшно."
  sl "Да…"
  me "А тебе не кажется это странным?"
  sl "Что именно?"
  me "Ну, что мы сидим тут, вдвоём, ночью. Не нормально ли в данной ситуации дождаться утра, вызвать милицию?"
  "Его слова звучали убедительно, и я согласилась с ним."
  sl "Да, наверное."
  me "Конечно, я практически сам вызвался. Не стоило."
  sl "Но ведь ты просто хотел помочь. Если Шурик там, то нужно найти его как можно скорее."
  me "Такими темпами скорее не мы Шурика найдём, а им потом придётся нас искать. Ведь он как-то смог заблудиться."
  th "А ведь и правда. Мы тоже можем заблудиться, и придётся просидеть здесь до утра."
  me "Ладно-ладно, я ничего такого не имел в виду. Может, его там нет и он давно вернулся в лагерь."
  sl "Да, может быть."
  me "Но проверить стоит?"
  sl "Конечно!"
  "Я встала и протянула ему руку. Нужно скорее всё проверить и вернуться в лагерь."
  "…"
  $ persistent.sprite_time = "night"
  scene bg int_catacombs_entrance 
  with dissolve
  play ambience ambience_catacombs fadein 3
  "Коридор был в точности таким же, как и тот, из которого мы вышли."
  "Мы шли какое-то время, пока я не обнаружила пролом в полу."
  sl "Смотри!"
  scene bg int_catacombs_hole with dissolve
  "Я крепче сжала его руку."
  show pi normal pioneer with dissolve
  sl "Может быть…"
  th "Он спустился туда?"
  "Он посветил вниз."
  me "Думаю, стоит проверить…"
  stop ambience fadeout 2
  "Глубина ямы позволяла потом выбраться оттуда, так что бояться на первый взгляд было нечего."
  scene bg int_mine with dissolve
  play ambience ambience_catacombs_stones fadein 3
  "Он спустился и следом помог спуститься мне."
  "Мы оказались в какой-то шахте."
  "Стены и потолок были укреплены деревянными балками, а вдаль уходили рельсы."
  "Я совершенно не была готова к такому повороту событий. Бродить по неизвестной шахте было худшим исходом в нашем походе."
  show pi normal pioneer with dissolve
  sl "Как думаешь, где мы?"
  me "Не знаю, шахта какая-то. Что здесь могли добывать?"
  sl "Может быть, уголь?"
  me "Может быть…"
  hide pi with dissolve
  "Мы начали медленно продвигаться вперёд."
  "Фонарь постоянно моргал, а вокруг образовывались страшные тени. Стоило посветить на них, и они исчезали. "
  "Не знаю, какой бы испуг я испытала, если бы одна из них осталась на месте."
  show pi normal pioneer with dissolve
  sl "Тут страшнее, чем наверху…"
  me "Да, пожалуй."
  hide pi with dissolve
  "В один момент мне уже даже хотелось бросить эту затею и вернуться сюда утром с ребятами. Оно того не стоило."
  "Мы вышли к развилке."
  scene bg int_mine_crossroad with dissolve
  show pi normal pioneer with dissolve
  sl "И куда нам теперь?"
  me "Не знаю."
  sl "А вдруг мы заблудимся?"
  me "Да, точно, давай сделаем пометку, что мы здесь уже были!"
  th "Похоже, Семён не совсем так меня понял."
  "Он взял с пола камень и начертил им подобие креста на балке."
  me "Вот, теперь точно будем знать, что здесь уже проходили."
  sl "Хорошо."
  "Я улыбнулась."
  sl "И куда?"
  hide pi with dspr
  "…"
  window hide
  with fade
  window show
  "Семён решил пойти направо. {w}Но мы лишь встретились с очередной развилкой."
  "Дальше я не особо запомнила путь, надеясь на память Семёна."
  "Бродили мы минут десять, может двадцать. {w}Стало казаться, что мы ходим по кругу."
  "Однако, всё ещё находились развилки, которые мы до этого не встречали."
  "Мы несколько раз возвращались к началу. Но Семён не терял энтузиазма."
  scene bg int_mine_door with fade
  "Наконец пейзаж сменился на большую деревянную дверь в стене."
  me "Ну, уже хоть что-то."
  sl "А что там?"
  stop ambience fadeout 3
  me "Вот сейчас и выясним."
  play sound sfx_open_door_mines
  pause(1)
  $ persistent.sprite_time = "night"
  scene bg int_mine_room with dissolve
  "За дверью скрывалась небольшая комната, похожая то ли на подсобку котельной, то ли на одно из помещений бомбоубежища."
  "Везде валялся мусор. Было больно смотреть на это зрелище. {w} Все стены были исписаны некультурными словами."
  "Здесь явно бывали люди, но как часто и как давно они здесь были в последний раз?"
  "Семён водил фонарём по всему помещению, как вдруг…"
  scene cg d4_sh_sit with dissolve
  "В углу мы увидели съёжившегося Шурика."
  sl "Шурик!"
  "Я сразу же позвала его."
  "Но он даже не отреагировал."
  me "Так вот ты где! А мы тебя всю ночь ищем! Что ты тут вообще забыл?"
  sh "А вы кто?"
  me "Что значит, «мы кто»? Давай уже вставай и пойдём."
  sh "Никуда я с вами не пойду."
  "Он отвернулся."
  sh "Вы опять хотите меня обмануть. Будете водить кругами по подземелью? Будете! Я вас знаю!"
  "Бедняга, похоже, он совсем заплутал в этом лабиринте и сошёл с ума. {w}С ним надо быть аккуратнее, неизвестно что он может выкинуть в следующую секунду."
  me "Хватит уже чушь нести."
  "Семён двинулся к нему, но я схватила его за руку и остановила."
  sl "Он не в себе."
  me "Ну и я не в себе! Целую ночь тут шляться – любой не в себе будет."
  "Я покачала головой и сама направилась к Шурику, оставаясь в свете фонаря, чтобы он мог меня отчётливо разглядеть."
  scene bg int_mine_room with dissolve
  show pi normal pioneer at cleft
  show sh scared pioneer at cright
  with dissolve
  sl "Всё в порядке, это я, Славя."
  sh "Правда?"
  show sh cry pioneer at cright with dspr
  "Он посмотрел на меня и тихо заплакал."
  sl "Конечно! Кто же ещё? И Семён со мной. Мы пришли за тобой. Теперь всё в порядке!"
  sh "Вы точно не {i}они{/i}?"
  sl "Нет конечно! Мы – это мы."
  "Он попытался встать, но, видимо, потерял ориентацию в пространстве и был уже готов упасть, если бы я вовремя не поймала его."
  sl "Вот так! Осторожнее!"
  show sh scared pioneer at cright with dspr
  me "Ладно, пора выбираться отсюда!"
  show sh upset pioneer at cright with dspr
  sh "Назад нельзя…"
  me "Назад – это куда? В шахту?"
  sh "Да."
  "Шурик говорил спокойно, но при этом его голос еле заметно дрожал."
  me "Почему?"
  show sh scared pioneer at cright with dspr
  sh "Там… они!"
  me "Кто они-то?"
  sh "Голоса."
  me "Какие ещё голоса?"
  "Семён только портил ситуацию тем, что выдавал нас. Шурик мог в любой момент перестать нам верить и вернуться в угол."
  sl "Успокойся, Шурик. И расскажи нам всё подробно."
  "Он сделал несколько глубоких вдохов и выдохов и начал:"
  show sh normal pioneer at cright with dspr
  sh "Мне нужны были кое-какие детали для робота, и я слышал, что в старом лагере есть бомбоубежище. А в бомбоубежищах обычно много всякой аппаратуры. Она, конечно, старая, но разобрать вполне можно – катушки, резисторы всегда найдутся."
  sh "Вот я с утра пораньше и пошёл, думал, всё быстро сделаю и к завтраку вернусь."
  sh "Всё, что нужно, я собрал."
  "Он достал из кармана и показал нам какие-то лампочки и проводочки."
  sh "Но потом из-за двери – там наверху, в бомбоубежище – услышал какие-то звуки. То ли стоны, то ли плач. Сначала стало страшно, но потом я подумал – а вдруг человек в опасности. И пошёл…"
  show sh scared pioneer at cright with dspr
  sh "А тут вот – шахта, лабиринт этот чёртов! Я совсем заблудился. И голоса, голоса повсюду что-то говорят мне – то кричат, то шепчут, а я никак разобрать не могу!"
  "Он уже был готов разрыдаться, но я погладила его по голове и попыталась успокоить. Он продолжил:"
  show sh normal pioneer at cright with dspr
  sh "В общем, нашёл я эту комнату, тут хотя бы не слышно их…"
  me "И решил сидеть и ждать, пока тебя спасут, как в фильмах уровня «Б»?"
  "Язва Семёна явно была не к месту и я бросила на него гневный взгляд."
  me "Ну, в любом случае пора выбираться отсюда! Если никто не против, конечно?"
  sh "Пойдёмте, я знаю короткий путь!"
  me "Короткий?"
  sh "Да, я же тут всё исходил."
  me "Ну ладно…"
  scene black 
  with dissolve
  "Шурик не соврал."
  scene bg int_mine_exit_night_light with dissolve
  "Действительно, поплутав по шахте всего пару минут, мы оказались возле решётки, за которой виднелось небо."
  me "И почему же ты не выбрался тогда сам?"
  sh "А ты попробуй."
  "Семён подтянулся и сильно дёрнул решётку несколько раз."
  "Но решётка не хотела поддаваться."
  "Он посмотрел на нас с Шуриком, ожидая предложений."
  sl "Может, фонарём?"
  me "Фонарём…"
  "Возможно это был неподходящий предмет. Но Семёну хватило и его."
  "Он с размаху ударил им по решётке."
  play sound sfx_break_grid
  "Вскоре послышался треск, и на землю посыпались болты, удерживающие её."
  stop music fadeout 3
  "…"
  scene bg ext_square_night with dissolve
  play ambience ambience_camp_center_night fadein 3
  "Через минуту мы все уже находились сверху, {w}у памятника Генде."
  show sh normal pioneer at center  with dissolve
  sh "Ну ладно, я пойду, спасибо вам…"
  "Шурик выглядел несколько растерянным."
  hide sh with dissolve
  "Семён ничего не ответил, лишь махнул рукой на прощание."
  play music music_list["forest_maiden"] fadein 3
  show pi normal pioneer with dissolve
  "Я села рядом с Семёном, развалившемся на траве."
  sl "Ну и ночка…"
  me "Да уж… Если бы мне кто ещё неделю назад сказал, что я попаду в пионерлагерь да и ещё придётся лазать по бомбоубежищам…"
  sl "Зато весело."
  me "В каком-то смысле."
  th "Когда-нибудь мы вспомним и вместе посмеёмся над всем этим."
  me "Как думаешь, он и правда там что-то слышал?"
  sl "Не знаю... Возможно, конечно, но, скорее всего, ему просто показалось. В такой ситуации любому может померещиться."
  me "А я вот думаю, ему стоит психиатру показаться…"
  sl "Наверное!"
  "Мне показалось это забавным, и я рассмеялась."
  th "На улице уже была поздняя ночь, учитывая что Семён в одном домике с Ольгой Дмитриевной, ему явно не поздоровиться."
  sl "Ну ладно, пора спать."
  me "Угу."
  "Чувствовалась какая-то недосказанность."
  me "Спасибо тебе!"
  sl "За что?"
  th "Вот так сюрприз!"
  me "Без тебя бы я не справился."
  sl "Да ничего…"
  "Семён меня засмущал."
  "Мне стало неловко, и, дождавшись пока он на меня не смотрит, я по-тихому ушла."
  hide pi with dissolve
  stop music fadeout 3
  th "Не хватало, чтобы он ещё что-то сказал, от чего я совсем засмущаюсь."
  th "Хотя чего тут такого? Я вызвалась помочь ему, он поблагодарил меня, почему я стесняюсь?"
  scene bg ext_houses_night with dissolve
  "Подходя к дому, я поняла, что повела себя некультурно не попрощавшись с ним."
  th "Он, наверное, обидится."
  th "Завтра извинюсь."
  stop ambience fadeout 3
  scene bg int_house_of_sl_night with dissolve
  "Когда я зашла внутрь, Женя уже спала, и я не стала её будить."
  "Я осторожно взяла свой дневник и вышла на крыльцо."
  scene bg ext_house_of_sl_night_light with dissolve
  play ambience ambience_camp_center_night fadein 3

  # Дневник
  show bknt_clear at truecenter with dspr
  play sound_loop pen_write
  show bknt_w11 at truecenter with dissolve2
  $ persistent.sl_m_bknt11 = True
  "Сегодня был очень необычный день. Буквально с утра пропал наш товарищ – Шурик."
  "Весь день я только и делала, что искала его. {w}Кроме меня активно в поисках участвовали и другие ребята, особенно Электроник. Ведь они вместе с Шуриком каждый день что-то конструируют в кружке кибернетики."
#Если она зашла в дом Семёна после того как сходила на склад/музклуб, иначе строчка пропускается
  "Но также мне сегодня помогал и Семён, во всяком случае, мы вместе с ним обошли лагерь. К сожалению, мы не смогли найти Шурика." 
  "После ужина Алиса и Ульянка хотели взорвать памятник Генде. До сих пор не могу вспомнить кто он такой, но ведь это не повод его взрывать! Я заподозрила что-то неладное ещё до ужина, когда они вместе куда-то пошли."
  "Потом на площадь неожиданно забежал Электроник, с ботинком Шурика в руке. По его словам, он нашёл его на дороге в старый лагерь." 
  "Семён добровольно вызвался помочь. И я не могла не вызваться пойти с ним. Хотя я до сих пор не могу понять, как Ольга Дмитриевна позволила нам отправиться ночью в такое жуткое место. Семён мог заблудиться, если бы я не пошла с ним, ведь я знаю дорогу."
  "Придя на место, я немного струхнула уже от самого вида лагеря. Но вот Семён пошёл вперёд и я за ним. Мы зашли внутрь и осмотрели здание. Всё это время я пыталась не отходить далеко от Семёна."
  "Потом мы нашли люк, вход к которому был расчищен. Когда мы спустились, стало ещё хуже: там был тоннель, по стенам которого тянулись провода. И в конце него находилось бомбоубежище, о котором я услышала от Ульяны."
  hide bknt_w11
  show bknt_w11_2 at truecenter with dspr
  "Семён предлагал несколько раз вернуться назад, однако я смогла его убедить продолжить поиски Шурика, потому что одна вряд ли бы отважилась идти дальше."
  "Нам пришлось спуститься в пролом в полу. Мы оказались в заброшенной шахте. К этому моменту я уже ни на минуту не отпускала руку Семёна, который неумолимо шёл вперёд. {w}Мы миновали развилки, несколько десятков минут плутали по этому лабиринту, но всё-таки нашли Шурика."
  "Бедняге слышались голоса, и мне пришлось его успокаивать, чтобы вернуть его в «Совёнок»."
  "Всё закончилось благополучно, и все вернулись домой. Когда Шурик ушёл, мы ещё некоторое время сидели вместе с Семёном."
  "Там, на площади, мне так не хотелось уходить, создавалось чувство какой-то недосказанности."
  "Семён поблагодарил меня, и почему-то мне стало неловко, поэтому я ушла, не попрощавшись, и мне до сих пор стыдно за этот поступок."
  "Завтра мы во второй раз идём в поход. Эта скукотища мне надоела, нужно будет как-нибудь сбежать оттуда."
  stop sound_loop
  hide bknt_clear
  hide bknt_w11_2
  with dspr
  #конец дневника

  "Закончив писать дневник, я посмотрела на небо."
  scene stars with dissolve
  th "Если Семён ещё не ушёл с площади, наверное он тоже сейчас любуется звёздами."
  th "Хотя о чём это я? Уже и спать пора."
  scene bg int_house_of_sl_night with dissolve
  play ambience ambience_int_cabin_night fadein 3
  "Я зашла в домик, переоделась и легла в кровать."
  "Усталость, вызванная поисками Шурика в экстремальной обстановке быстро дала о себе знать."
  "Силы моментально покинули меня и я уснула."
  $ go_to_sh = True

label slavyana_mod__day4__without_pi:
  stop ambience fadeout 3
  show blink
  "..."
  window hide

  if sl_m_Full:
      jump slavyana_mod__day5
  jump slavyana_mod__launcher0

label slavyana_mod__day4_fast_choice:
  scene bg ext_square_day
  show mt normal pioneer at cright
  show pi normal pioneer at cleft
  with dissolve
  "Четвертый день.{w} Поиски шурика"
  menu:
      "Вызваться помочь":
        $ go_to_sh = True
        $ sl_m_lp += 2
      "Не обращать внимания":
        $ go_to_sh = False
  return