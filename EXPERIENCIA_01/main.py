#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

ev3.speaker.beep()

#Declaracion de puertos
ma=Motor(Port.A)
md=Motor(Port.D)
SonicSensor=UltrasonicSensor(Port.S4)


#Prroceso
while(1==1):
    ma.run(75)
    md.run(75)
    if SonicSensor.distance()<200:
        ma.brake()
        md.brake()
        wait(300)
        ev3.speaker.beep()
        md.run(75)
        wait(2000)
        ma.run(75)



