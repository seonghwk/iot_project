#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

servo = PWM(0x6f)
servo.setPWMFreq(60)

# recommended for auto-disabling motors on shutdown!


def turnOffMotors():
    mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)


atexit.register(turnOffMotors)

# DC motor test!
myMotor = mh.getMotor(2)


def GO():
    myMotor.setSpeed(100)
    myMotor.run(Raspi_MotorHAT.FORWARD)


def LEFT():
    servo.setPWM(0, 0, 280)


def RIGHT():
    servo.setPWM(0, 0, 400)


def BACK():
    myMotor.setSpeed(100)
    myMotor.run(Raspi_MotorHAT.BACKWARD)


def STOP():
    myMotor.run(Raspi_MotorHAT.RELEASE)
    servo.setPWM(0, 0, 340)


def MIDDLE():
    servo.setPWM(0, 0, 340)

# # set the speed to start, from 0 (off) to 255 (max speed)
# myMotor.setSpeed(150)
# myMotor.run(Raspi_MotorHAT.FORWARD)
# # turn on motor
# myMotor.run(Raspi_MotorHAT.RELEASE)


print("Turn Left! Move Forward!")
LEFT()
GO()
time.sleep(1)

print("Turn Right! Move Forward!")
RIGHT()
GO()
time.sleep(1)

print("Turn Left! Move Backward!")
LEFT()
BACK()
time.sleep(1)

print("Turn Left! Move Backward!")
RIGHT()
BACK()
time.sleep(1)

print("Stop")
MIDDLE()
STOP()
