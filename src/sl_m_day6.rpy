label slavyana_mod__day6:
  stop music
  stop sound
  stop ambience
  $ backdrop = "days"
  $ new_chapter(6, u"Славя. День шестой")
  $ day_time()
  $ persistent.sprite_time = "day"
  $ renpy.pause(3, hard=True)

  call slavyana_mod__day6_end_choise

  if words_red:
    play ambience sfx_head_heartbeat loop fadein 2
    scene bg ext_polyana_mere_day
    show prologue_dream
    with dissolve
    "Я купалась в озере. Том самом, рядом с поляной."
    "Не знаю, как я до него добралась, и почему я пошла именно сюда {w}, но мне здесь нравится."
    "Вода была чистой, а в её отражении было видно небо."
    play sound sfx_bush_leaves
    "Я услышала шелест рядом с одним из деревьев, но никого не увидела."
    "Лишь белая рубашка промелькнула на секунду."
    "Я хотела выбраться, чтобы посмотреть, кто это {w}{nw}"
    stop ambience fadeout 4
    play music music_list["faceless"] fadein 4
    extend ", но что-то схватило меня за ноги и не пускало."
    "Я гребла изо всех сил, пытаясь выпутаться. Но меня затягивало только сильнее."
    "Силы начали кончаться."
    scene cg under_water
    show prologue_dream
    with dissolve
    play sound sfx_shoulder_dive_water
    "А потом оно утянуло меня вниз и я стала тонуть. Но никакой возможности выплыть не было."
    "Я пыталась выпутаться, но ничего не могла разглядеть."
    "Собрав последние силы, я снова стала пробираться к поверхности…"
    "Я стала задыхаться."
    "И в последний момент я взглянула наверх{w} и увидела лицо Виолы!"

  elif words_green:
    play music music_list["sparkles"] fadein 1
    scene cg d6_sl_forest
    show prologue_dream
    with dissolve
    me "Как отдохнула?"
    sl "Хорошо, спасибо."
    me "Ну, чем займёмся?"
    sl "Не знаю, а зачем мы пришли?"
    me "Ну как же, забыла?"
    th "Вообще не помню."
    me "Мы пришли сюда, потому что ты хотела показать своё любимое место в лесу. Ты говорила, тут красиво и не ошиблась."
    sl "А… да."
    scene bg ext_polyana_day
    show pi normal pioneer
    show prologue_dream
    with dissolve
    sl "Ладно, ты сиди пока что, я пойду и скоро вернусь."
    sl "Куда ты?"
    me "Сказал же, что вернусь. А если нет… {w} {i}Ты меня не потеряешь{/i}."
    me "Ты же мне веришь?"
    sl "Я… верю. Конечно верю. Иди."
    hide pi with dspr
    "И он ушёл."
    "А потом…"

  elif words_blue:
    play music music_list["sparkles"] fadein 1
    #*Иллюстрация с 2 девками сидящими в комнате вечером с помехами* из альтернативной концовки надо пикчу вынуть
    # TODO: Заменить на правильное изображение
    scene bg SlaviaRoom
    show prologue_dream
    with dissolve
    "Мне снилось одно место…"
    "Одно очень знакомое место…"
    "Но почему, если я здесь не живу?.."
    "Две мои сестры (или не сестры) уже проснулись."
    "Умывшись, я оделась и вышла на улицу."
    scene bg town_snow
    show prologue_dream
    with dissolve
    "На дворе была зима. Но я почему-то не удивилась этому."

  stop music fadeout 2
  scene black with dissolve
  pause 2
  play ambience ambience_int_cabin_day fadein 3
  scene bg int_aidpost_day
  show cs normal
  show prologue_dream
  with dissolve
  cs "Проснулась… пионерка?"
  scene bg int_aidpost_day
  show cs normal
  with dspr
  cs "Ты уже проспала линейку, но я не стала тебя будить.{w} Тебе нужно отоспаться, чтобы организм быстрее справился с болезнью.{w} Я принесла тебе завтрак из столовой, но обед ещё не готов.{w} Так что я отойду потом на некоторое время."
  sl "Доктор, а сколько времени?"
  cs "Около 9 часов."
  show cs smile with dspr
  cs "Кстати, а расскажешь, почему Ольга заперла тебя и строго-настрого запретила видеться с Семёном?"
  "Она ехидно улыбнулась."
  "Мне было очень неловко."
  sl "Да там… Был один момент глупый. И вот…"
  cs "Какой же?"
  "Её улыбка мгновенно вгоняла меня в краску."
  sl "Ничего особенного… Если вы о чём-то не том подумали…"
  cs "А откуда ты знаешь, что я могу о чём-то не том думать."
  th "Оставлять меня одну с ней была не лучшая идея."
  cs "Ладно, можешь не говорить… пионерка."
  cs "Да, сейчас…"
  show cs normal with dspr
  "Она открыла ящик стола и стала что-то искать. Достав какую-то таблетку, она протянула мне её и стакан воды, чтобы запить."
  cs "Это чтобы голова не болела."
  "Медсестра подмигнула мне."
  play sound sfx_dinner_horn_processed
  stop ambience fadeout 1
  scene black with dissolve
  pause 2
  play ambience ambience_int_cabin_day fadein 2
  scene bg int_aidpost_day
  show cs normal
  with dspr
  "Уже прозвенел горн на завтрак."
  cs "Сегодня на завтрак каша, так что я не придумала для тебя ничего лучше, чем принести из запасов бутерброды, кусок омлета и чай."
  sl "Спасибо."
  play sound sfx_knock_door2
  "Через некоторое время в дверь постучали."
  cs "Сейчас-сейчас!"
  hide cs with dspr
  "Медсестра подошла к двери и начала с кем-то разговаривать."
  stop ambience fadeout 1
  scene black with dissolve
  pause 2
  play ambience ambience_int_cabin_day fadein 2
  play sound sfx_lock_close
  scene bg int_aidpost_day
  show cs normal
  with dspr
  "Медсестра вернулась и заперла дверь."
  cs "Герой-любовник твой пришёл."
  th "Доктор Виола, вы опять?"
  sl "Он не мой …"
  show cs smile with dspr
  cs "Да? А вроде всё слышит и понимает, даже общается."
  show cs normal with dspr
  cs "Славь, если честно, то лично я не нахожу ничего запретного в вашем поведении. Это природа. Но так мне наказала Ольга Дмитриевна. {w}Если хочешь поскорее освободиться, советую прилечь и расслабиться, если к ужину температура будет нормальной - отпущу. Договорились?"
  sl "Хорошо."
  "Я послушалась её совета и легла в кровать."
  show blink
  stop ambience fadeout 1
  pause 2
  "Заснуть никак не получалось."
  scene bg int_aidpost_day
  show cs normal with dspr
  play ambience ambience_int_cabin_day fadein 3
  show unblink
  pause 2
  hide unblink
  pause 1
  play sound sfx_open_door_2
  show cs normal:
    linear 1.0 xalign 0.255
  show mt normal panama pioneer at cright with dissolve
  "Вскоре пришла вожатая."
  mt "Славя, болеешь?"
  sl "Да, но мне уже лучше."
  mt "Это хорошо, но стоит подождать до завтра. {w}Лучше всего до вечера."
  sl "Но мне же хотя бы ещё вещи собрать надо."
  show mt smile panama pioneer at cright with dspr
  mt "Успеешь. Ладно, я пойду, а то за этим товарищем не уследишь."
  "Она уже собиралась уходить, но вдруг что-то вспомнила."
  show mt normal panama pioneer at cright with dspr
  mt "Ключи."
  sl "Какие ключи?"
  mt "Твои ключи. Как вы медпункт иначе бы открыли?"
  sl "Да..."
  "Я отдала ей ключи."
  show mt smile panama pioneer at cright with dspr
  mt "Не расстраивайся. Завтра всё равно пришлось бы их сдавать и всё равно они тебе больше не понадобятся."
  hide mt with dspr
  cs "Прости Славя, сама всё видишь."
  sl "Дa."
  show blink
  stop ambience fadeout 1
  pause 2
  scene bg int_aidpost_day
  play ambience ambience_int_cabin_day fadein 2
  play sound sfx_dinner_horn_processed
  show unblink
  "Меня разбудил горн, но я продолжала лежать в постели."
  "Вскоре Виола ушла."
  play sound2 sfx_knock_glass
  "Но тут кто-то постучал в окно. Я поднялась и, приоткрыв его, увидела...{w=0.5}{nw}"
  hide unblink
  show pi normal pioneer with dissolve
  pause 0.5
  extend " Семёна."
  sl "Семён, ты что здесь делаешь?{w} Тебе же нельзя…"
  me "Как себя чувствуешь?"
  sl "Хорошо…{w} Но Ольга Дмитриевна сказала мне, что ещё день надо здесь побыть…"
  me "Вылезай."
  "Уверенно сказал он."
  sl "Ты что? Зачем?"
  "Испуганно спросила я."
  me "Вылезай! Потом всё расскажу!"
  th "Похоже у него есть какой-то план, а раз так, Семёну, я думаю, можно довериться. Всё равно отговаривать его буду дольше."
  play sound sfx_slavya_gets_out
  stop ambience
  scene bg ext_aidpost_day
  show pi normal pioneer
  with dissolve
  play ambience ambience_camp_center_day fadein 3
  "Я распахнула окно и вылезла через него. Семён помог мне."
  sl "И что дальше?"
  me "Пойдём!"
  "Он взял меня за руку, и мы пошли в сторону леса."
  stop ambience fadeout 1
  play ambience ambience_forest_day fadein 3
  scene bg ext_polyana_day
  show pi normal pioneer
  with dissolve
  "Через несколько минут ходьбы, я остановилась и всё же решила спросить его."
  sl "Семён, что мы делаем?"
  me "А что такого? Ты считаешь, что всё это правильно?"
  sl "Нет, но так будет только хуже."
  me "Почему же? Мы имеем право поступать, как считаем нужным!"
  sl "Хорошо, но что дальше?"
  me "Смотри!"
  "Он показал мне сумку, которую тащил весь путь от медпункта до леса."
  sl "И?"
  me "Не знаю…{w} Отсидимся в лесу пока что… {w}Покажем, что с нами тоже надо считаться!"
  sl "Но ведь это глупо! По-детски."
  me "Если не хочешь…"
  th "Ну уж нет! Я с тобой до конца!"
  sl "Я сделаю, как ты скажешь…"
  me "В любом случае… {w}Думаю, сейчас это самое лучшее решение!"
  sl "Ладно…"
  scene cg d6_sl_forest
  with dissolve
  "Семён расстелил спальный мешок и мы расселись на нём. "
  sl "И что будем делать?"
  me "Не знаю…"
  me "А что ты хочешь?"
  play sound sfx_stomach_growl
  "После этих слов голод внезапно напомнил о себе."
  sl "Поесть было бы неплохо… "
  sl "Ты ничего с собой не захватил?"
  "Когда он показывал мне сумку, там ничего не было."
  me "Нет…"
  sl "Ладно..."
  "Мы продолжали сидеть молча."
  th "Интересно, о чём он думает? Может он в спешке дорабатывает план? Или он боится сделать первый шаг? {w}Хотя, скорее всего, он просто наслаждается моментом"
  me "Ладно, ты сиди здесь, я скоро вернусь."
  sl "Куда ты?"

  if words_green:
    th "Сказал же, что вернусь. А если нет... {i}Ты меня не потеряешь{/i}."

  me "За едой я!"
  sl "Может, вместе пойдём?"
  me "Не стоит… Я мигом!"
  hide pi
  if words_green:
    th "Никогда не верила в вещие сны."
  scene bg ext_polyana_day with dissolve
  "Семён встал и уверенным шагом ушёл с поляны, оставив меня одну."
  th "Зачем же всё-таки Семён это делает?"
  th "Может быть он просто за справедливость? Или я ему не безразлична."
  th "Всё, что сделал Семён очень мило. Но что же всё-таки думаю о нём я? Он симпатичный мальчик, смелый {w}, добрый {w}, заботливый."
  th "Но абсолютно некомпетентный!"
  if words_red:
    th "А я, дура, доверилась ему."

  if sl_m_lp < 8:
    jump slavyana_mod__day6_not_worth_it

  menu:
    "Не стоило идти с ним":
      pass
    "Он милый, но не смекалистый":
      $ sl_m_lp += 1
      "Но всё-таки он хороший. И я не жалею ни о чём."
      "Всё что он делает сейчас, это ради меня."
      stop ambience fadeout 2
      play music music_list["forest_maiden"] fadein 3
      "Я готова идти с ним, потому что я верю ему... {w}И... {w}Я... {w}Да {w}, я люблю его. {w}Очень сильно. Я наконец-то это поняла."
      if go_to_sh:
        "Именно поэтому я пошла с ним в старый лагерь."
      if not sl_m_day5_make_semen_guilty:
        "Именно поэтому я не прогнала его в медпункте."
      "Именно {b}поэтому{/b} я сейчас нахожусь здесь и жду его. Ведь я не могу иначе. И он тоже не может."
      stop music fadeout 3
      jump slavyana_mod__day6_not_worth_after

label slavyana_mod__day6_not_worth_it:
  "В любом случае, я уже пошла с ним, это будет бестактно: уйти, ничего не сказав."
  "Может, он всё-таки исправится."
  "Я хочу дать ему шанс."
  stop ambience fadeout 1

label slavyana_mod__day6_not_worth_after:

  scene bg black with dissolve

  if words_blue:
    "История, достойная фильма, или хотя бы книги. О любви двух пионеров, слишком поздно понявших это."
  else:
    pause 2

  play ambience ambience_forest_day fadein 2
  scene bg ext_polyana_day with dissolve
  show pi normal pioneer with dissolve
  "Наконец, он вернулся."
  me "Вот..."
  sl "Как у тебя ловко получилось!"
  me "Ну, мне помогали..."
  th "Значит теперь кто-то точно знает о нас"
  "Мы сосредоточенно ели, не говоря ни слова."
  me "Неплохо, весьма неплохо."
  sl "Да."
  sl "Что теперь будем делать?"
  me "Может, у тебя есть какие-то предложения?"

  if words_red:
    th "Придётся всё самой придумывать и устраивать."
    
  "Я решила уточнить."
  sl "Насчёт чего?"
  me "Ну, хотя бы как договориться с вожатой."
  sl "Не знаю... {w}А ты уверен..."
  me "Уверен!"

  th "Что стоило это всё затевать..."
  
  me "В конце концов, это акт протеста! {w}Пусть она знает, что нельзя мной... {w}нами помыкать!"
  th "Значит Семён у нас благородный рыцарь, который спасает принцессу из замка с драконом."
  sl "Ты смешной!"
  "Я улыбнулась."
  sl "Можно же было просто подойти к ней и поговорить. {w}Но раз ты хочешь сидеть здесь и ждать, то я согласна."
  me "Я пытался говорить..."
  sl "Именно так, как надо?"
  me "Не знаю..."
  th "Нет, скорее с колдуньей, с Ольгой."
  "Я рассмеялась своей мысли."
  me "Что?!"
  sl "Ничего... {w}Просто я сейчас похожа на принцессу, которую прекрасный принц похитил из замка злой колдуньи."
  "Семён серьёзно посмотрел на меня."
  show pi smile pioneer with dspr
  "И улыбнулся."
  me "Да... Аналогия {w}прослеживается."
  sl "И у принцесс обычно не бывает выбора в таких ситуациях."
  th "И она выходит замуж за своего похитителя."

  if words_green:
    "Хотела сказать я, но посчитала это слишком странным."

  elif words_red:
    "Хотела сказать я, но посчитала это слишком глупым."

  elif words_blue:
    "Хотела сказать я, но посчитала это слишком криповым."
    th "Криповым? Какое-то странное, выдуманное мной слово."
  
  show pi normal pioneer with dspr
  me "Знаешь, возможно, я был неправ."
  "Я удивлённо посмотрела на него."
  me "Мы действительно ничего не добьёмся, сидя здесь. {w}Даже не так! Это просто глупо и по-детски, тут ты права."
  sl "И что же тогда делать?"
  "Я серьёзно посмотрела на него."
  me "Пойдём!"
  "Мы встали, Семён взял меня за руку, и пошли обратно в лагерь."
  stop ambience fadeout 2
  scene black with dissolve
  pause 2
  $ persistent.sprite_time = "sunset"
  $ sunset_time()
  play music music_list["afterword"] fadein 3
  scene bg ext_square_day with dissolve
  show pi normal pioneer at cright
  show mt angry pioneer at cleft
  with dissolve
  "Через некоторое время мы вышли на площадь, где уже стояла вожатая."
  mt "Явились не запылились!"
  "Сказала она злобно."
  mt "И есть тебе, что сказать в своё оправдание?"
  "Обратилась она к Семёну"
  show pi serious pioneer at cright with dspr

  # Если ЛП больше или равно 9 и не свалили вину на семена
  if sl_m_lp >= 9 and not sl_m_day5_make_semen_guilty:
    # Если сказали лене правду
    if sl_m_day5_cleaning_told_truth:
      $ setEndGreen();
      me "Мне не в чем оправдываться."
    # Если солгали лене и плохая концовка получена
    elif persistent.endings["sl_m_red"]:
      $ setEndBlue();
      me "Мне не в чем оправдываться."
    # Если солгали лене, но плохая концовка не получена
    else:
      $ setEndRed();
      me "Мы ничего такого не делали, чтобы перед вами оправдываться!"
  # Если очков меньше 9 или свалили вину на семена
  else:
    me "Мы ничего такого не делали, чтобы перед вами оправдываться!"
    $ setEndRed();

  show mt surprise pioneer at cleft with dspr
  mt "Да? {w}Ну ладно. То есть ты считаешь это всё нормальным? Хорошо..."
  "Сейчас она глядела прямо на меня."
  mt "Иди к себе. {w}Я понимаю, что ты ни в чём не виновата."
  "Я опустила глаза и сжала руку Семёна."
  show mt angry pioneer at cleft with dspr
  mt "Славя!"
  me "Как видите, она не хочет."
  mt "Чем ты её так охмурил?"
  me "Да ничем, боже мой!"
  "Семён явно начал заводиться."
  me "Почему вы считаете, что мы сделали что-то неправильное? {w}И вообще! Ничего мы не делали."
  show mt grin pioneer at cleft with dspr
  mt "То-то я не видела!"
  th "А что она могла увидеть? Не выдумывает ли наша Оленька?"
  me "И что же вы видели?"
  show mt normal pioneer at cleft with dspr
  "Она замялась, но почти сразу же ответила тем же тоном:"
  mt "Достаточно."
  me "Хорошо же вы выводы делаете. Вам бы в НКВД работать."
  show mt rage pioneer at cleft with dspr
  mt "Не хами мне!"
  me "И не собирался даже."
  show mt angry pioneer at cleft with dspr
  mt "В общем, я не желаю дальше вести бессмысленные споры. Ты наказан до конца смены."
  me "О, правда? И как же?"
  mt "Будешь сидеть под замком!"
  me "А если не соглашусь?"
  show mt surprise pioneer at cleft with dspr
  "Оля удивленно посмотрела на Семёна"
  show mt angry pioneer at cleft with dspr
  mt "Что значит «не соглашусь»?"
  "Медленно произнесла вожатая."
  "Похоже, она не ожидала такого ответа."
  me "То и значит."
  mt "Но ты не можешь! Настоящий пионер..."
  me "Значит, я фальшивый!"
  "Ольга замолчала, словно собираясь с мыслями."
  show mt surprise pioneer at cleft with dspr
  mt "Думаешь, я не смогу тебя заставить?"
  th "Это начинает потихоньку надоедать."
  show pi smile pioneer at cright with dspr
  me "И каким же образом?"
  "Он рассмеялся."
  show mt angry pioneer at cleft with dspr
  mt "Знаешь что!"
  show pi normal pioneer at cright with dspr
  me "Что?"
  mt "Я... {w}Я... {w}По месту учёбы на тебя характеристику пошлю! Да тебя в комсомол не примут! В партию не возьмут!"
  mt "Короче говоря, у тебя всё равно выбора нет!"
  th "Ну это уж слишком! Тем более ни за что!"
  sl "А почему вы изначально правы, Ольга Дмитриевна? Что, Семён всегда во всём виноват? Что такого произошло? Что он... что мы сделали не так? Вы хоть сами знаете, в чём нас обвиняете?"
  sl "А если бы на моём месте была другая, вы бы вели себя точно так же?"
  show mt surprise pioneer at cleft with dspr
  mt "Славя, ты же знаешь..."
  sl "В том-то и дело, что я знаю! Знаю вас, знаю, что Семён ни в чём не виноват. Знаю, что у вас к нему предвзятое отношение. Не понятно почему, кстати. А ведь он старается!"
  sl "Да, это иногда выглядит немного неуклюже, но я знаю, что он вкладывает все силы и всю душу. Что же тогда, вы будете его винить просто за то, что он такой?"
  sl "А почему вы вообще сразу решили, что я не виновата? Я что, вся такая правильная, а может быть вы чего-то не знаете обо мне?"
  sl "Ни один человек не идеален, но Семён хотя бы пытается исправиться, а вы только мешаете и наказываете его за глупые случайности. Он жертва обстоятельств. Как вы не понимаете?"
  "Наконец этот поток гнева прекратился."
  show mt normal pioneer at cleft with dspr
  mt "Ладно, не знаю, что уж с вами и делать..."
  mt "Но не думайте, что я одобряю ваше поведение!"
  hide mt with dissolve
  "Она развернулась и, пройдя сквозь толпу, удалилась."
  stop music fadeout 3
  play ambience ambience_camp_center_day fadein 3
  "Только сейчас я заметила, что вокруг нас собрались пионеры."
  "А затем они стали расходиться."
  show pi normal pioneer at cright with dspr
  sl "Знаешь, по-моему, мы несколько переборщили."
  "Я улыбнулась"
  me "Нет, ты что! {w}Сам бы я с ней спорил и спорил до глубокой ночи, а ты так чётко и ясно всё расписала... {w}Я бы и за неделю таких слов не подобрал!"
  sl "Да ладно тебе..."
  me "Что ладно? Это чистая правда, ни капли лжи, ни капли комплиментов!"
  "Я рассмеялась."
  sl "А я сказала просто первое, что в голову пришло, а вышло вот так."
  me "Первая мысль - самая правильная, как говорят."
  sl "Наверное."
  "Внезапно Семён покраснел и попытался вынуть свою руку из моей."
  "Но я не пустила и взялась даже чуть крепче."
  sl "Куда пойдём?"
  me "А что если я предложу вернуться в лес?"
  th "Смысла в этом уже нет, но я не против."
  me "Ну понимаешь, просто иногда..."
  show pi smile pioneer at cright with dspr
  sl "Хорошо, пойдём!"
  "Семён усмехнулся"
  sl "Что?"
  me "Ничего, просто я тут вспоминал... {w}Ну да неважно! Пойдём!"
  stop ambience fadeout 2
  "Держась за руки, мы направились в лес."
  scene bg ext_polyana_day 
  with dissolve
  play ambience ambience_forest_day fadein 3
  scene bg ext_polyana_day
  "Вскоре мы вышли на ту же полянку."
  show pi normal pioneer with dissolve
  sl "Сюда?"
  me "Нет, давай пойдём дальше."
  sl "Хорошо."
  "Мы пошли дальше."
  scene bg ext_polyana_mere_day with dissolve
  "И вышли к небольшому озеру."
  show pi normal pioneer with dissolve
  me "Отличное место!"
  "В первый раз, когда мы здесь «встретились», Семён, как я уже догадалась, подсматривал за мной."
  sl "Это точно..."
  me "Значит, привал предлагаю сделать здесь!"
  sl "Отличное место."
  "Семён разложил тот самый спальник и уселся на него."
  "Я подсела к нему."
  me "И что будем делать?"
  sl "Не знаю... Ты же хотел в лес..."
  me "Да, хотел..."
  "Семён очень напрягся и задумался."
  sl "Да ладно, не напрягайся ты так!"
  "Я рассмеялась."
  me "Я совсем не..."
  sl "Я же вижу!"
  me "Ну просто потому что..."
  sl "Всё в порядке."
  me "Как скажешь."
  "Семён вздохнул."
  sl "Лучше расскажи мне про себя."
  me "Да и нечего в общем."
  sl "Не может такого быть, чтобы у человека совсем ничего интересного не было!"
  me "Почему же? Вот я, например..."
  sl "Просто ты..."
  th "...замкнутый."
  sl "А может, ты что-то не договариваешь?"
  me "Что же?"
  sl "Не знаю... {w}Скрываешь от меня что-нибудь?"
  me "Но зачем?"
  sl "Откуда мне знать? Тебе виднее."
  me "Ну... {w}Нет..."
  sl "Как-то ты это сказал..."
  me "Как?"
  "Семён заволновался."
  sl "Не так!"
  "Я вновь рассмеялась."
  me "Хорошо, а что тебя интересует?"
  sl "Ну, расскажи про себя. Какие-нибудь интересные случаи из жизни!"
  me "Ладно, дай подумать..."
  "Он задумался."
  me "Когда я был маленький - лет 5-6, наверное, - у меня на даче был шалашик."
  me "Крепкий такой, из досок, на крыше рубероид, в общем, в случае войны послужил бы бомбоубежищем."
  me "И вот как-то я сидел с кем-то на этом шалаше и... {w}внезапно упал."
  me "А за ним были грядки с клубникой."
  me "И все те доли секунды, что я летел до них, думал, что всё – вот она, костлявая с клюкой пришла, а перед глазами пронеслась вся жизнь, всего за 6 лет, но всё же…"
  me "Упал на грядку и ничего не почувствовал - понятное дело, земля рыхлая, её там целая гора."
  me "Вот такая история..."
  "Я рассмеялась."
  sl "Но это же глупо!"
  me "Мне в то время так не казалось."
  sl "А сейчас?"
  me "Не знаю... {w}Наверное..."
  sl "Ладно. {w}Ещё что-нибудь расскажи!"
  me "Опять скажешь, что глупость..."
  sl "Не скажу!"
  me "Эх..."
  "Он вновь задумался."
  me "Ещё я как-то с мостика упал в пруд и чуть не утонул."
  sl "У тебя все истории какие-то..."
  me "Ну, я же говорил - вспомнить особо нечего, вот и рассказываю первое, что в голову придёт."
  sl "Кстати, насчёт озера!"
  "Я обратила свой взгляд в сторону воды."
  sl "Может искупаемся?"
  th "Я как раз купальник ещё не сняла."
  me "Да я не любитель особо. {w}Да и не в чем."
  th "Ах, вот в чём дело!"
  sl "Да ладно тебе!"
  "Я ехидно улыбнулась."
  me "Ну, я даже не знаю."
  sl "Давай-давай!"
  hide pi with dissolve
  "Я побежала к озеру, по пути стаскивая рубашку."
  "Сначала было немного неловко, но когда верх полностью освободился, я почувствовала лёгкость и уже не так стеснялась."
  th "Хотя чего стесняться? Такими уж родились."
  me "Ну... эээ..."
  "К этому времени я уже стянула с себя всю одежду и запрыгнула в воду, зазывая Семёна."

  if persistent.sl_m_hen_txt:
    scene cg d6_sl_swim_alt with dissolve
  else:
    scene bg black with dissolve

  play sound_loop sfx_swimming fadein 3
  sl "Давай сюда!"
  me "Да я не... {w} Как-то не хочется..."
  sl "Да ладно тебе! Весело!"
  me "Я плавки не взял..."
  sl "Ну так и я..."
  sl "Не бойся."
  me "Я и не боюсь! Чего тут бояться..."
  sl "Тогда залезай."
  "Семён явно был смущён."
  sl "Ну и не надо!"
  sl "Иди тогда костёр разведи."
  me "Зачем?"
  sl "Затем! {w}Вот я выйду - надо будет высохнуть!"
  me "А, да... Хорошо..."
  stop sound_loop fadeout 2
  "И он быстро ушёл."
  "..."
  scene bg ext_polyana_mere_day with dissolve
  stop sound_loop fadeout 3
  play sound_loop2 sfx_forest_fireplace fadein 2
  "Пока я купалась, Семён уже успел развести огонь, как я поняла по характерному трескающемуся звуку."

  "Я поспешила к нему."
  if persistent.sl_m_hen_txt:
    scene cg d6_sl_after_swim with dissolve
  else:
    scene bg ext_polyana_day with dissolve
  "Я накинула на себя рубашку и расправила её."
  "Семён сидел ко мне спиной, повёрнутый к костру."
  "Я отправилась к нему."
  "Я нависла над ним и посмотрела на костёр."
  "Он вышел весьма неплохим."
  sl "Какой ты молодец."
  "Он поднял голову и, засмущавшись, отвернулся."
  sl "С тобой не пропадёшь."
  scene cg d6_sl_forest_2_alt with dissolve
  "Я решила больше его не смущать пока что и уселась к нему спиной."
  sl "Надеюсь, всё быстро высохнет."
  "Я чувствовала, что его спина была в напряжении."
  sl "Ну так что?"
  me "Что?"
  "Его голос дрогнул."
  sl "Расскажи ещё что-нибудь!"
  me "Да я даже не знаю..."
  "Его дыхание стало сбивчивым. С ним явно что-то не так."
  sl "Ты вдруг какой-то скованный стал."
  me "Да нет, просто..."
  "Он говорил прерывисто."
  me "А ты думаешь... это нормально?"
  sl "Что?"
  me "Ну, вот так сидеть."
  sl "А что такого?"
  th "Бедный, совсем застесняла его."
  th "Надо помочь ему расслабиться."
  me "Ну ты же... {w} Неужели не понимаешь..."
  "Он глубоко вздохнул."
  sl "Не знаю даже..."
  "А про себя усмехнулась."
  th "Надо ему намекнуть."
  sl "А ты что думаешь?"
  me "Ну, я... {w} Ну, мне..."
  sl "Может, и не стоит сдерживаться?"
  "Семён резко выгнулся и развернулся."

  scene black with dissolve
  stop sound_loop2 fadeout 2
  stop ambience fadeout 2
  stop sound_loop2 fadeout 2
  pause 2
  play music music_list["i_dont_blame_you"] fadein 1
  if persistent.sl_m_hen_txt:
    scene cg d6_sl_hentai_2 with dissolve

  "А потом, {w}рывком прижал меня к земле так, что я лежала на спине, в одной лишь майке. А он навис надо мной, сжимая руки."
  th "Как тогда в библиотеке."
  sl "Ай!"
  me "Больно?"
  sl "Нет, просто неожиданно..."
  me "Если ты..."
  sl "Нет, всё в порядке."
  "Он смотрел на меня, а я улыбалась, прикрыв глаза. Ясно давая понять, что теперь я его."
  "Он жадно впился в мои губы."

  if persistent.sl_m_hen_txt:
    "Я не умела целоваться, но в этот момент просунула язык в его рот."
    "Его хватка резко ослабла. И он принялся трогать меня за грудь."
    "Ток прошёлся по моей спине, и я прижалась к нему ещё сильнее."
    "Соски стали очень чувствительными. Один он облизывал языком, а второй массировал пальцами."
    "Я застонала от удовольствия, но главное должно было быть впереди."
    "Я стала гладить его по голове, перебирая волосы."
    "Он прекратил и посмотрел на меня."
    "Казалось, он хотел что-то сказать, но потом продолжил."
    "Он спустился ниже, провёл языком по животу и просунул его в пупок, и я вскрикнула."
    "Он продолжал свои непотребства и просунул пальцы в трусики."
    "А я уже стала влажной, и ни о чём больше не думала."
    "Он стянул их с меня."

  me "Можно?"
  sl "Можно…"
  "С трудом произнесла я."

  if persistent.sl_m_hen_txt:
    scene cg d6_sl_hentai_1_alt with dissolve
    "И вот, рыцарь уже готов проникнуть в принцессу…"
  else:
    scene bg black with dissolve

  me "Наверное, будет немножко больно…"
  sl "Ничего…"

  if persistent.sl_m_hen_txt:
    "Он вздохнул, схватил меня за плечи и глубоко вошёл внутрь."
    "Этот главный момент был непередаваем. Длился всего секунду {w}, но за этот миг я успела испытать и боль и блаженство одновременно."
    "Его член оборвал меня."
    "Я закатила глаза от возбуждения и принялась подмахивать."
    "Этот первый раз мне уже нравился."
    "Я практически ничего не умела, но похоже Семён знал, как надо доставлять удовольствие девушке."
    "Мне было так прекрасно в этот момент, и я хотела, чтобы он продолжал дольше."
    "Но он двигался так сильно, что уже скоро достиг предела."
    "Он снова вошёл максимально глубоко и кончил, заполнив меня внутри."
    "Его горячая струя обволакивала мои внутренности."
    "Он обессиленно свалился на меня."
    "Надо было предохраниться, но уже поздно."
    "Да и не важно это уже."

  stop music fadeout 4
  scene bg black with dissolve
  "..."
  "Между нами случилось нечто прекрасное. И я рада, что моим человеком оказался именно Семён."
  scene bg ext_polyana_day with dissolve
  play ambience ambience_forest_day fadein 3
  sl "Это было чудесно!"
  me "Да..."
  "Мы ещё некоторое время лежали рядом."
  sl "Что-то холодно."
  me "Сейчас."
  play sound sfx_unzip_sleepbag
  "Он расстегнул спальник, и мы забрались внутрь."
  "Я положила свою голову ему на плечо."
  sl "Не возражаешь, если я посплю немного, а то что-то устала?"
  me "Да, конечно..."
  show blink
  pause 1
  scene bg black
  stop ambience fadeout 2
  "Моё дыхание восстановилось. И я заснула."
  "Вокруг ветер тихо шелестел листьями, а рядом колыхалась трава."
  "..."

  if (sl_m_lp < 9):
    $ setEndRed();

  if sl_m_Full:
      jump slavyana_mod__day7
  jump slavyana_mod__launcher0

# Выбор концовки в начале дня
label slavyana_mod__day6_end_choise:
  # Если ЛП больше или рано 8 и в медпункте сказали правду
  if sl_m_lp >= 8 and not sl_m_day5_make_semen_guilty:
    # Если лене сказали правду
    if sl_m_day5_cleaning_told_truth:
      $ setEndGreen()

    # Если соврали, и уже получили плохую концовку
    elif persistent.endings["sl_m_red"]:
      $ setEndBlue();

    # Если лене соврали или не получали плохую концовку
    else:
      $ setEndRed()
  # Если ЛП меньше 8 или в медпункте солгали
  else:
    $ setEndRed()
  return

# Быстрый выбор
label slavyana_mod__day6_fast_choise:
  call slavyana_mod__day6_end_choise
  if sl_m_lp >= 8:
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg ext_polyana_day with dissolve
    "День шестой."
    "На поляне семен ушел за едой. Славя осталась одна и размышляла."
    menu:
      "Не стоило идти с ним":
        pass
      "Он милый, но не смекалистый":
        $ sl_m_lp += 1

  if (sl_m_lp < 9):
    $ setEndRed();
  return