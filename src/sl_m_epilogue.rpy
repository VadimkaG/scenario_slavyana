init python:
  words_red = False
  words_green = False
  words_blue = False
  # Плохая концовка
  def setEndRed():
    global words_red, words_green, words_blue
    words_red = True
    words_green = False
    words_blue = False
  # Альтернативная концовка
  def setEndBlue():
    global words_red, words_green, words_blue
    words_red = False
    words_green = False
    words_blue = True
  # Хорошая концовка
  def setEndGreen():
    global words_red, words_green, words_blue
    words_red = False
    words_green = True
    words_blue = False

label slavyana_mod__epilogue:
  stop music
  stop sound
  stop ambience
  $ backdrop = "epilogue"
  $ new_chapter(7, u"Славя. Эпилог")
  $ save_name = (u'Славя. "Эпилог"')
  $ day_time()
  $ persistent.sprite_time = "day"
  $ renpy.pause(3, hard=True)

  play music music_list["farewell_to_the_past_edit"] fadein 3
  show anim prolog_1 with dissolve
  "Наша история похожа на романтический рассказ."
  "Два пионера встретили друг друга в лагере и полюбили друг друга. Но вот, настал момент расставания, и им придётся что-то решать."
  "И какие бы препятствия не встретились на их пути, они всё преодолеют."

  if words_blue:
    call slavyana_mod__epilogue_alt

    #*Ачивка «Лучший Новый Год в жизни»*
    if not persistent.endings["sl_m_blue"]:
        $ persistent.endings["sl_m_blue"] = True
        if persistent.show_achievements:
            $ show_achievement("sl_m_blue")
            $ achievement.grant("ACH_SL_M_BLUE")
    #$ renpy.notify("Лучший Новый Год в жизни")

    pause 2

    call slavyana_mod__ending

    play music music_list["everlasting_summer"] fadein 4
    pause 1
    scene bg ext_camp_entrance_day behind credits with dissolve2
    jump slavyana_mod__credits

  if words_red:
    "Кроме одного…"

  #*Фон внутри зимнего автобуса*
  scene bg intro_xx with dissolve
  "Когда я проснулась, я вспомнила всё что было."
  "Я ехала со встречи однокурсников домой с пересадкой. На следующей остановке надо было сойти и пройти 2 квартала до следующей и потратить ещё час езды."
  "Я взглянула на часы."
  "Прошло не больше 20 минут."
  th "Как можно было заснуть в автобусе?!"
  th "Хорошо, что остановку не проспала."
  "Я стала вспоминать свой сон."

  if words_red:
    #*Фон поляна с Семёном*
    scene bg ext_polyana_day
    show pi normal pioneer
    show prologue_dream
    with dissolve
    "Семён…"
    #*Фон площадь с Леной с помехами*
    scene bg ext_square_day
    show un normal pioneer
    show prologue_dream
    with dissolve
    "Лена…"
    #*Фон домики с Алисой с помехами*
    scene bg ext_houses_day
    show dv normal pioneer
    show prologue_dream
    with dissolve
    "Алиса…"
    #*Фон внутри музклуба с Мику с помехами*
    scene bg int_musclub_day
    show mi normal pioneer
    show prologue_dream
    with dissolve
    "Мику…"
    #*Фон спортплощадка с Ульяной с помехами*
    scene bg ext_playground_day
    show us normal pioneer
    show prologue_dream
    with dissolve
    "Ульяна…"
    #*Фон внутри домика ОД*
    scene bg int_house_of_mt_day
    show mt normal pioneer
    show prologue_dream
    with dissolve
    "Ольга… Дмитриевна?.."
    scene bg intro_xx with dissolve
    "Ну точно! Пионерлагерь «Совёнок»!"
    "А я там была помощницей вожатой."

  if words_green:
    "Всплывали отдельные образы, не формирующие общей картины."
    #*Фон площадь с Леной с помехами*
    scene bg ext_square_day
    show un normal pioneer
    show prologue_dream
    with dissolve
    "Девочка с фиолетовыми волосами… {w} Один вопрос: почему?"
    #*Фон домики с Алисой с помехами*
    scene bg ext_houses_day
    show dv normal pioneer
    show prologue_dream
    with dissolve
    "Девочка с рыжими волосами и чудной причёской."
    #*Фон поляна с Семёном с помехами*
    scene bg ext_polyana_day
    show pi normal pioneer
    show prologue_dream
    with dissolve
    "Мальчик, который кажется знакомым."
    #*Иллюстрация линейки с помехами*
    scene cg d2_lineup
    show prologue_dream
    with dissolve
    "Толпа пионеров и их вожатая. {w} И я стою в их строю."
    #*Иллюстрация окно автобуса*
    scene bg intro_xx with dissolve
    th "Что же мне такое снилось?"

  "Но вот моя остановка. И теперь надо пройти небольшое расстояние в пару сотен метров."
  #*Фон зимний город*
  scene bg town_snow with dissolve
  "На улице шёл снег. Недавно все дружно отметили Новый Год."
  "По улице практически не ходили люди. Было уже очень позднее время."
  
  if words_red:
    "Но получается, что это всё было не больше чем сном?"
    "Целых 14 дней уместились в 20 минутах? Такого не может быть!"
    "Всё, что я ощущала, было реальным. Да, тело было 17-летней пионерки. Но это точно была я, потому что всё помню. Откуда то же я должна это помнить!"
    th "Но, блин, как же всё-таки жалко, что всё было не настоящим. Или было?"
    "Может быть, он тоже сейчас проснулся и где-нибудь мечтает наяву?.."
    "…"
  
  if words_green:
    "Надо было добраться до дома как можно скорее и я поторопилась."

  "Ветер усиливался, начиналась метель."

  #*Фон остановка*
  scene bg bus_stop with dissolve
  if words_red:
    "Когда я дошла до остановки, с неё уже уходил кто-то в тёмном пальто."
    th "Не дождался."
    "Я взглянула на расписание."
    "Как раз должен был подойти последний на сегодня 410-тый."
    "Я принялась ждать."
    "Прошло больше часа, а он всё не появлялся."
    "Пришлось ждать дольше, чем хотелось бы."
    #*Иллюстрация с автобусом с распахнутыми дверьми*
    show anim intro_11 with dissolve
    "К остановке начал подъезжать автобус. {w} Очень старый автобус. {w} ЛИаЗ."
    th "Такие наверное ещё при Сталине ездили. Или когда там их стали производить?"
    "Его двери распахнулись и я вошла внутрь."
    #*Иллюстрация с автобусом с горящей фарой*
    show anim intro_13 with dissolve
    th "Вези меня домой!"
    stop music fadeout 3
    scene black with dissolve2
    scene bg black with dissolve
    #*Фон тёмный экран*

    $ renpy.pause(2, hard=True)

    #*Ачивка «Домой!»*
    if not persistent.endings["sl_m_red"]:
      $ persistent.endings["sl_m_red"] = True
      if persistent.show_achievements:
        $ show_achievement("sl_m_red")
        $ achievement.grant("ACH_SL_M_RED")

    pause 2

    call slavyana_mod__ending
    #*Титры на фоне ночных ворот Совёнка под трек «410»*
    play music music_list["410"] fadein 4
    pause 1
    scene bg ext_camp_entrance_night with dissolve2
    jump slavyana_mod__credits

  if words_green:
    "Я дошла до остановки. На ней стоял мужчина в тёмном пальто."
    sl "А вы не знаете, последний автобус уже ушёл?"
    voice "Вроде бы после двенадцати должен быть ещё один."
    sl "Спасибо."
    "На этом разговор кончился."
    "Молчание затягивалось."
    sl "А вы почему так поздно?"
    voice "Гуляю…"
    "Задумчиво ответил он."
    voice "А вы… по делам?"
    sl "Ну, не то чтобы… Еду домой."
    voice "А где живёте?"
    sl "Далеко…"
    th "Ему действительно интересно, где я живу?"
    voice "А я вот рядом."
    sl "Хороший район."
    "Зачем-то сказала я."
    voice "Выбирать не приходится…"
    sl "Вам тут не нравится?"
    voice "Не знаю, уже привык."
    sl "А вот мне кажется, что человек везде может быть счастливым."
    voice "Наверное…"
    sl "Ну сами посудите! {w} Люди ведь и в Антарктиде живут… на станциях, я имею в виду. {w} И в пустыне Сахара! И много где ещё. Главное ведь – это люди!"
    voice "С вами сложно не согласиться."
    "В его голосе была слышна ирония."
    sl "Мне кажется, вы неискренни."
    voice "Нет, отчего же, сударыня…"
    "Я засмеялась в кулачок."
    sl "Я думаю, вы хороший человек!"
    "Я развернулась, чтобы посмотреть на своего собеседника."
    #*Иллюстрация Славя в капюшоне*
    scene cg epilogue_sl with dissolve
    pause(1)
    #*Иллюстрация Славя в капюшоне развернулась*
    scene cg epilogue_sl_2 with dissolve
    pause(2)
    #*Фон остановка и спрайт Семёна в куртке*
    scene bg bus_stop
    show pi normal coat
    with dissolve
    stranger "А мы с вами нигде раньше не встречались?"
    "Я внимательно посмотрела на него, пытаясь узнать его."
    sl "Вряд ли… {w} Но ваше лицо почему-то кажется знакомым."
    stranger "Вы… ты никогда не была в пионерлагере в детстве?"
    sl "Нет, конечно!"
    "Мне показалось это смешным."
    sl "Когда я родилась, их уже не было."
    sl "Хотя… Мне недавно снился сон…"
    th "Про пионерлагерь?"
    stranger "И мне тоже. {w} В смысле про пионерский лагерь."
    th "Я сказала это вслух?"
    sl "Может быть, там и виделись."
    stranger "Не исключено."
    sl "Кстати, меня Славя зовут. Вообще, полное имя – Славяна, но все меня Славей зовут. И ты тоже зови!"
    stranger "А меня Семён…"
    sl "Очень милое имя."
    me "Тоже на «с» начинается."
    sl "Да."
    me "Значит, ты далеко живёшь?"
    sl "Ну не так уж…"
    "Я назвала район."
    me "А я думал, что где-то на юге."
    sl "Почему?"
    me "Не знаю… {w} Может быть, потому что ты похожа на пионерку."
    sl "Да сдались тебе эти пионеры!"
    "Я рассмеялась."
    me "Если бы не они, возможно, мы бы и не познакомились."
    sl "Почему?"
    me "Да так… Шутка… {w} Скажи, а ты согласна, что мир существует, потому что мы в это верим?"
    sl "Это какой-то субъективный идеализм прямо…"
    "Я задумалась."
    me "Последнее время мне, наверное, близка эта философская школа."
    sl "Ну, не знаю… {w} Я в таких вещах не сильна."
    me "А в чём сильна?"
    "Я улыбнулась."
    sl "В чём-то другом."
    me "Не сомневаюсь ни секунды!"
    sl "Но ты же меня едва знаешь!"
    me "А кажется, что уже давно."
    sl "Да, и мне почему-то так кажется…"
    "Наступило неловкое молчание."
    "Снег несколько успокоился, но автобуса всё не было."
    "Было очень холодно, поэтому я растирала щёки."
    me "Похоже, 410-ый маршрут на сегодня закончил свои рейсы."
    sl "Похоже…"
    th "А до дома идти далеко."
    me "Если хочешь…"
    sl "Что?"
    me "Можешь остаться у меня…"
    sl "Но мы же только что познакомились."
    "Я рассмеялась."
    me "Да, я понимаю, но ночь на улице в такой холод…"
    sl "А не боишься?"
    "Я лукаво улыбнулась ему."
    me "Я? А надо?"
    sl "Кто знает… Кто знает…"
    me "Я просто предложил, ты не подумай ничего…"
    "Начал он оправдываться."
    sl "Да я всё прекрасно понимаю!"
    "Я рассмеялась."
    sl "Если ты не против, конечно…"
    "Я засмущалась."
    me "Пойдём?"
    sl "Давай всё же ещё немного подождём, вдруг приедет?"
    me "Хорошо."
    scene black with dissolve
    "…"
    #*Снова фон зимняя остановка*
    scene bg bus_stop
    show pi normal coat
    with dissolve
    sl "А чем ты занимаешься?"
    me "Я… Ну… {w} Работаю на дому, так скажем."
    "Мне показалось это лучшей работой на свете."
    sl "Здорово!"
    me "Что хорошего?"
    sl "Не знаю… {w} Много свободного времени, никуда ездить не надо! Ну и всё такое…"
    me "А ты?"
    sl "Я учусь."
    me "На краеведа?"
    sl "А кто это?"
    th "Однозначно глупый вопрос и поставила себя в глупое положение."
    me "Неважно…"
    sl "На эколога."
    me "Что же, достойная профессия…"
    "Мы продолжали болтать ни о чём, а автобус всё не ехал."
    "Был уже второй час ночи. {w} Время летело незаметно."
    "Смысла ждать на остановке больше не было."
    sl "Пойдём?"
    "Я улыбнулась."
    "Он встал и медленно направился в сторону дома."
    "Я аккуратно взяла его под руку и заглянула ему в глаза."
    sl "Знаешь, я уверена, что в этом году всё будет лучше, чем в предыдущем!"
    "…"
    #*Фон тёмный экран*
    stop music fadeout 3
    scene black with dissolve2

    $ renpy.pause(2, hard=True)

    #*Ачивка «Ты меня не потеряешь…»*
    if not persistent.endings["sl_m_green"]:
        $ persistent.endings["sl_m_green"] = True
        if persistent.show_achievements:
            $ show_achievement("sl_m_green")
            $ achievement.grant("ACH_SL_M_GREEN")

    pause 2
    call slavyana_mod__ending
    #*Титры на фоне заснеженного Совёнка под трек «Everlastingsummer»*
    play music music_list["everlasting_summer"] fadein 4
    pause 1
    scene bg ext_camp_upview_snow with dissolve2
    jump slavyana_mod__credits

label slavyana_mod__ending:
  "У каждой истории есть начало и конец."
  "У каждой истории есть своя канва, синопсис, содержание, ключевые моменты, прологи и эпилоги."
  "И нет такой книги, в которой при каждом новом прочтении не открывались бы вещи, на которые раньше не обращал внимания."
  "У каждой истории есть начало и конец."
  if words_red:
    "Почти у каждой…"
  else:
    "И даже у этой."
  return

label slavyana_mod__credits:
  $ renpy.show('credits_sl_m credits_sl_m_text', [sl_m_ending_transform], layer='widgetoverlay')
  $ renpy.pause(90, hard=True)
  $ renpy.hide('credits_sl_m credits_sl_m_text', layer='widgetoverlay')
  stop music fadeout 4
  scene black with dissolve2
  pause 3

  jump slavyana_mod__launcher0