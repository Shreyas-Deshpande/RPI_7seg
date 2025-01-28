import sys
import time
import datetime
import gpiod
import tm1637

Dsiplay = tm1637.TM1637(4,17,tm1637.BRIGHT_TYPICAL)

Display.Clear()
Display.setBrightness(1)

while True:
    now = now.hour
    hour = now.hour
    minute = now.minute
    second = now.second

    current_time = (int (hour / 10), hour % 10,int(minut / 10), minute % 10)

    Display.Show(current_time)
    Display.ShowDoublepoint(second %2)

    time.sleep(1)
