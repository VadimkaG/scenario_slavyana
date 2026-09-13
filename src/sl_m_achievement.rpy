
# Трансформация появления достижения
transform slavyana_mod_achievement_slide:
    xanchor 0.0
    yanchor 1.0
    xpos 1.0
    ypos 0.85

    easein_cubic 0.5 xpos 0.75
    pause 4.0
    easeout_cubic 0.5 xpos 1.0

# Окно достижения
screen slavyana_mod_achievement(achievement_image):
  on "show" action Play("sound", sfx_achievement)
  timer 5.1 action Hide("slavyana_mod_achievement")
  add achievement_image at slavyana_mod_achievement_slide

init python:
  # Выдать достижение
  def sl_m_ach(mask,achievement):
    if ((persistent.slavyana_mod_progress or None) is None):
      persistent.slavyana_mod_progress = 0
    if persistent.slavyana_mod_progress & mask == 0:
      persistent.slavyana_mod_progress = persistent.slavyana_mod_progress | mask
      renpy.show_screen("slavyana_mod_achievement","scenario_slavyana/res/images/achievement/achievement_"+achievement+".png")
  # Зеленая концовка
  def sl_m_ach_green():
    sl_m_ach(1,"green")
  # Красная концовка
  def sl_m_ach_red():
    sl_m_ach(2,"red")
  # Получена ли красная концовка
  def sl_m_ach_red_has():
    return (persistent.slavyana_mod_progress or 0) & 2 != 0
  # Синяя концовка
  def sl_m_ach_blue():
    sl_m_ach(4,"blue")
  # Одиночная концовка
  def sl_m_ach_solo():
    sl_m_ach(8,"solo")
  # Одиночная концовка Алисы
  def sl_m_ach_solo_dv():
    sl_m_ach(16,"solo_dv")
  # Одиночная концовка Лены
  def sl_m_ach_solo_un():
    sl_m_ach(32,"solo_un")
  # Одиночная концовка Ульяны
  def sl_m_ach_solo_us():
    sl_m_ach(64,"solo_us")

  # Пройдена ли основная ветка
  def sl_m_ach_main_has():
    return (persistent.slavyana_mod_progress or 0) & 7 != 0