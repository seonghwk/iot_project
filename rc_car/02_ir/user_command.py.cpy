from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
from time import sleep

mh = Raspi_MotorHAT(addr=0x6f)
myMotor = mh.getMotor(2)  # 핀번호

servo = PWM(0x6F)
servo.setPWMFreq(60)  # Set frequency to 60 Hz


def GO():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.FORWARD)


def LEFT():
    servo.setPWM(0, 0, 280)


def RIGHT():
    servo.setPWM(0, 0, 450)


def BACK():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.BACKWARD)


def STOP():
    myMotor.run(Raspi_MotorHAT.RELEASE)
    servo.setPWM(0, 0, 380)


def MIDDLE():
    servo.setPWM(0, 0, 380)
    