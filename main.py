import time

import pyupm_grove as grove
import pyupm_i2clcd as lcd

temperatura = grove.GroveTemp(0)
luz = grove.GroveLight(1)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)


while True:

    grados = temperatura.value()
    luxes = luz.value()

    display.setColor(255, 0, 0)

    display.setCursor(0,0)
    display.write('Temperatura ' + str(grados))

    display.setCursor(1,0)
    display.write('Luz ' + str(luxes))

    time.sleep(5)

del temperatura
