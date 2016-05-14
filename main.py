import time

import pyupm_grove as grove
import pyupm_i2clcd as lcd


temperatura = grove.GroveTemp(0)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)

celsius = temperatura.value()

display.setCursor(0,0)
display.setColor(255, 0, 0)

del temperatura
