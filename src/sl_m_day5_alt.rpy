label slavyana_mod__day5_alt:

# Рут Ульяны: sl_m_day1_help_od
# Рут Лены: sl_m_day5_berries_go_with
# Рут Алисы: sl_m_day6_alt_dv
# Одиночный рут: sl_m_day1_help_od and not sl_m_day5_berries_go_with and not sl_m_day6_alt_dv

  "Я вынула ключ из рубашки и отправилась к домику."
  stop ambience fadeout 1
  play ambience ambience_camp_center_night fadein 2
  scene bg ext_square_night with dissolve
  pause 1
  scene bg ext_house_of_sl_night with dissolve
  pause 1
  stop ambience fadeout 1
  play ambience ambience_int_cabin_night fadein 1
  play sound sfx_open_door_1
  scene bg int_house_of_sl_night with dissolve
  pause 2
  stop ambience fadeout 1
  play ambience ambience_camp_center_night fadein 2
  scene bg ext_square_night with dissolve
  pause 1
  play ambience ambience_boat_station_night fadein 3
  scene bg ext_beach_night with dissolve
  "По пути обтираясь сухим полотенцем я вернулась на пустеющий пляж, где меня ждала оставленная пионерская форма."
  "Я оделась."
  "Посидев ещё минут 10, глядя на Луну и дорожку, которую она оставила на воде, я собралась обратно."
  stop ambience fadeout 1
  play ambience ambience_camp_center_night fadein 2
  scene bg ext_square_night with dissolve
  "На полпути в домик я решила навестить Ульяну."
  "Занеся вещи в домик, я подошла к домику Алисы и Ульяны."
  $ persistent.sprite_time = "night"
  scene bg ext_house_of_dv_night with dissolve

  play sound sfx_knock_door7_polite
  if not sl_m_day1_help_od:
    "Я несколько раз постучалась."
    "Но никто не ответил."
    th "Наверное спит уже."

  else:
    "Я постучалась."
    us "Открыто."
    "Донёсся её звонкий голосочек с ноткой грусти."
    play sound sfx_open_door_2
    stop ambience fadeout 4
    $ persistent.sprite_time = "day"
    scene bg int_house_of_dv_night with dissolve
    show us sad pioneer with dissolve
    play music music_list["what_do_you_think_of_me"] fadein 3
    "Я зашла в гости к Ульяне."
    us "Чего надо?"
    "Так же грустно произнесла она."
    sl "Тебя вот решила навестить, наказанная же сидишь."
    us "Меня не надо навещать."
    sl "А одной не скучно?"
    show us angry pioneer with dspr
    us "Нисколечки!"
    show us sad pioneer with dspr
    us "Лучше скажи почему Алиса ещё не вернулась."
    sl "Поход ещё не закончился."
    show us smile pioneer with dspr
    us "А ты значит сбежала с него?"
    sl "Не сбежала, а отпросилась. {w=0.5} Кто то же должен следить чтобы ты не сбежала."
    show us dontlike pioneer with dspr
    us "Бе-бе-бе!"
    "Нахмурилась Ульянка."
    show us sad pioneer with dspr
    sl "Да шучу я!"
    "Я рассмеялась."
    sl "Давай тогда посижу с тобой недолго, спать уже скоро."
    us "Сейчас же только пол девятого!"
    sl "Раньше уснёшь - раньше выспишься и тем более молодому организму надо много сна."
    sl "Сказку тебе почитать?"
    "Шутливо сказала я."
    us "А давай! Страшную!"
    sl "Ну, насчёт страшной не знаю."
    us "Я тогда сразу лягу спать, чтобы не напридумывать себе ничего."
    sl "Ну... Хорошо, ложись тогда."
    "Я укрыла её одеялом и села на стул рядом."
    stop music fadeout 2
    hide us with dspr
    $ set_mode_nvl()
    window show
    pause 2
    play music music_list["memories"] fadein 5
    "Как то раз в лагерь приехал один мальчик."
    "Мальчик этот долго не хотел вступать в пионеры."
    "Никто точно не знал почему. {w}Может считал себя недостойтым, может быть настроения не было."
    "А может быть был просто вредным, или ещё какая-то причина."
    "В общем, не хотел мальчик вступать в пионеры и всё тут."
    nvl clear
    "Но однажды его всё-таки уговорили. Приняли всё-таки в пионеры и торжественно повязали пионерский галстук."
    "После этого мальчик довольный пошёл гулять по лагерю и решил ненадолго снять галстук, так как было жарко."
    "Но к его ужасу он не мог развязать галстук. {w}Наоборот, он затягивался всё туже и туже и начал душить мальчика."
    "Мальчик посинел, начал хрипеть и никак не мог избавиться от галстука."
    "На его удачу появилась вожатая и разрезала ножницами красный галстук."
    "Из него полилась чёрная... {w} субстанция."
    "И он исчез!"
    nvl clear
    $ set_mode_adv()
    stop music fadeout 3
    "Ульяна не дослушала истории до конца и уже дремала."
    play ambience ambience_camp_center_night fadein 2
    $ persistent.sprite_time = "night"
    scene bg ext_house_of_dv_night with dissolve
    "Я погасила свет и осторожно вышла."

  "Пора и мне идти спать."

  stop ambience fadeout 2
  scene black with dissolve
  "..."
  play ambience ambience_int_cabin_night fadein 3
  scene bg int_house_of_sl_night_light with dissolve
  "Судя по часам на будильнике, время подхода приближалось к концу. Я расстелила кровать, включила свет и уселась писать дневник."
  
# Дневник
  $ set_mode_nvl()
  "Дневник"
  "...На ужине в честь чудесного спасения Шурика испекли торт, из ингредиентов, которые пришлось носить Семёну."
  "Но пакостливая Ульянка сразу набросилась на него и нам ничего не досталось."
  "Затем мы пошли в поход. Поблуждав немного по уже истоптанным тропинкам в лесу, мы вышли на поляну,которую мы сегодня убирали с Леной."
  "Я отпросилась с похода, предпочтя провести время купанием в речке. Я надеюсь Леночка призналась Семёну в чувствах."
  "Насчёт наказания Ульяны я не уверена. Слишком уж строго вожатая к ней отнеслась. Она хоть и заслужила это, но всё-таки остаётся ребёнком."
  if not sl_m_day1_help_od:
    "Мы весело провели с ней время и я уложила её спать."
  nvl clear
  window hide
  $ set_mode_adv()
# Конец дневника
  
  th "Завтра будет новый день, завтра будут новые свершения!"
  "С этой мыслью я легла на кровать и заснула."
  
  stop ambience fadeout 3
  scene black with dissolve
  pause 3
  play music music_list["door_to_nightmare"] fadein 3
  scene anim prolog_2 with dissolve
  us "Как долго нам осталось?"
  dv "Мы все умрём."
  un "Я не знаю."
  sl "Почему всё так?"
  mt "Я не знаю, но похоже оно движется."
  me "А я знаю что это!"
  scene bg ext_square_day_city
  show prologue_dream
  with dissolve
  pause 2
  stop music fadeout 2
  scene black with dissolve

  if sl_m_Full:
    jump slavyana_mod__day6_alt
  jump slavyana_mod__launcher0