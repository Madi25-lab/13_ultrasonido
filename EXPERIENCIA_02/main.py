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

#Proceso
while(1==1):
    ma.run(75)
    md.run(75)
    ev3.light.on(Color.GREEN)
    if SonicSensor.distance()<=200:
        ev3.light.on(Color.RED)
        ev3.speaker.play_file(SoundFile.LASER)
        ma.brake()
        md.brake()
        ev3.light.on(Color.YELLOW)
        ev3.speaker.beep()
        wait(300)
        md.run(75)
        wait(3000)
        ma.run(75)

    




