# Экран блокнота
screen sl_m_nb():
  frame:
    xalign 0.5
    yalign 0.5
    xminimum 716
    yminimum 490
    xmaximum 716
    ymaximum 490
    padding (0, 0, 0, 0)

    background "scenario_slavyana/res/images/notebook/notebook.png"

    fixed:
      xsize 676
      ysize 490
      xpos 20
      ypos 0

      text "[sl_m_notebook_history_left]":
        xpos 0
        ypos 0
        xsize 340
        style "notebook_text_style"

      text "[sl_m_notebook_history_right]":
        xpos 355
        ypos 0
        xsize 301
        style "notebook_text_style"

# Стиль текста блокнота
style notebook_text_style:
  font "scenario_slavyana/res/Fonts/ofont.ru_Sacramento.ttf"
  size 20
  color "#0400ff"
  line_spacing -10
  xanchor 0.0
  yanchor 0.0
  xpos 0
  ypos 0
  layout "greedy"

style notebook_page_text_style:
  size 20
  color "#000000"

# Блокнот-меню
screen slavyana_mod__notebook_history_sc():
  tag menu
  modal True

  key "dismiss" action [ Play("sound", "sound/sfx/cardgame/new/choose_card_1.ogg"), Return() ]

  frame:
    xalign 0.5
    yalign 0.5
    xminimum 716
    yminimum 490
    xmaximum 716
    ymaximum 490
    padding (0, 0, 0, 0)

    background "scenario_slavyana/res/images/notebook/notebook.png"

    fixed:
      xsize 676
      ysize 490
      xpos 20
      ypos 0

      text "[sl_m_notebook_history_left]":
        xpos 0
        ypos 0
        xsize 340
        style "notebook_text_style"

      text "[sl_m_notebook_history_right]":
        xpos 355
        ypos 0
        xsize 301
        style "notebook_text_style"

  hbox:
    xalign 0.5
    yalign 0.5
    xanchor 1.0
    yanchor 1.0
    xoffset 340
    yoffset 240
    spacing 30

    imagebutton:
      idle "scenario_slavyana/res/images/notebook/arrow_left.png"
      hover "scenario_slavyana/res/images/notebook/arrow_left_hover.png"
      sensitive (sl_m_notebook_history_page > 1)
      action Function(slavyana_mod__notebook_page_prev)
    text "[sl_m_notebook_history_page]/[sl_m_notebook_history_count]":
      style "notebook_page_text_style"
    imagebutton:
      idle "scenario_slavyana/res/images/notebook/arrow_right.png"
      hover "scenario_slavyana/res/images/notebook/arrow_right_hover.png"
      sensitive (sl_m_notebook_history_page < sl_m_notebook_history_count)
      action Function(slavyana_mod__notebook_page_next)


# Иконка блокнота
screen slavyana_mod__notebook_interface():
  imagebutton:
    idle "scenario_slavyana/res/images/notebook/notebook_ico.png"
    hover "scenario_slavyana/res/images/notebook/notebook_ico_hover.png"
    xpos 20
    ypos 700
    action [ Play("sound", "sound/sfx/cardgame/new/choose_card_1.ogg"), ShowMenu("slavyana_mod__notebook_history_sc") ]

init python:
  # Левый текущий текст в журнале
  sl_m_notebook_history_left = ""
  # Правый текущий текст в журнале
  sl_m_notebook_history_right = ""
  # Все страницы журнала
  sl_m_notebook_history = []
  # Текущая страница журнала
  sl_m_notebook_history_page = 0
  # Последняя страница журнала
  sl_m_notebook_history_count = 0

  # Очистить блокнот
  def sl_m_nb_clear():
    global sl_m_notebook_history_page, sl_m_notebook_history_left, sl_m_notebook_history_right, sl_m_notebook_history, sl_m_notebook_history_count
    sl_m_notebook_history_left = ""
    sl_m_notebook_history_right = ""
    sl_m_notebook_history = []
    sl_m_notebook_history_page = 0
    sl_m_notebook_history_count = 0

  # Принудительно установить последнюю страницу
  def sl_m_nb_lastpage():
    global sl_m_notebook_history_page, sl_m_notebook_history_count
    sl_m_notebook_history_page  = sl_m_notebook_history_count

  # Добавить новую страницу в блокнот
  def sl_m_nb_addpage(new_text):
    global sl_m_notebook_history_page, sl_m_notebook_history_left, sl_m_notebook_history_right, sl_m_notebook_history, sl_m_notebook_history_count
    sl_m_notebook_history.append([new_text,""])
    sl_m_notebook_history_count = len(sl_m_notebook_history)
    sl_m_notebook_history_page  = sl_m_notebook_history_count
    sl_m_notebook_history_left  = new_text
    sl_m_notebook_history_right = ""

  # Добавить текст на последнюю страницу
  def sl_m_nb_add(new_text):
    global sl_m_notebook_history_page, sl_m_notebook_history_left, sl_m_notebook_history, sl_m_notebook_history_count
    sl_m_notebook_history_page  = sl_m_notebook_history_count
    i = sl_m_notebook_history_count-1
    sl_m_notebook_history[i][0] += new_text
    sl_m_notebook_history_left = sl_m_notebook_history[i][0]

  # Добавить текст справа на последнюю страницу
  def sl_m_nb_add2(new_text):
    global sl_m_notebook_history_page, sl_m_notebook_history_right, sl_m_notebook_history, sl_m_notebook_history_count
    sl_m_notebook_history_page  = sl_m_notebook_history_count
    i = sl_m_notebook_history_count-1
    sl_m_notebook_history[i][1] += new_text
    sl_m_notebook_history_right = sl_m_notebook_history[i][1]

  # Изменить последнюю страницу в блокноте
  def sl_m_nb_set(text_left,text_right = ""):
    global sl_m_notebook_history_page, sl_m_notebook_history_left, sl_m_notebook_history_right, sl_m_notebook_history, sl_m_notebook_history_count
    sl_m_notebook_history_page  = sl_m_notebook_history_count
    sl_m_notebook_history_left = text_left
    sl_m_notebook_history_right = text_right
    i = sl_m_notebook_history_count-1
    sl_m_notebook_history[i][0] = text_left
    sl_m_notebook_history[i][1] = text_right

  # Следующая страница блокнота
  def slavyana_mod__notebook_page_next():
    global sl_m_notebook_history_page, sl_m_notebook_history_left, sl_m_notebook_history_right, sl_m_notebook_history, sl_m_notebook_history_count
    if sl_m_notebook_history_count > 0 and sl_m_notebook_history_page < sl_m_notebook_history_count:
      sl_m_notebook_history_page += 1
      i = sl_m_notebook_history_page-1
      sl_m_notebook_history_left = sl_m_notebook_history[i][0]
      sl_m_notebook_history_right = sl_m_notebook_history[i][1]
      renpy.music.play("sound/sfx/cardgame/new/choose_card_1.ogg", channel="sound")

  # Предыдущая страница блокнота
  def slavyana_mod__notebook_page_prev():
    global sl_m_notebook_history_page, sl_m_notebook_history_left, sl_m_notebook_history_right, sl_m_notebook_history
    if sl_m_notebook_history_page > 1:
      sl_m_notebook_history_page -= 1
      i = sl_m_notebook_history_page-1
      sl_m_notebook_history_left = sl_m_notebook_history[i][0]
      sl_m_notebook_history_right = sl_m_notebook_history[i][1]
      renpy.music.play("sound/sfx/cardgame/new/choose_card_1.ogg", channel="sound")