from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
from time import sleep

mh = Raspi_MotorHAT(addr=0x6f)
myMotor = mh.getMotor(2)  # 핀번호

servo = PWM(0x6F)
servo.setPWMFreq(60)  # Set frequency to 60 Hz


def MQTTGO():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.FORWARD)


def MQTTLEFT():
    servo.setPWM(0, 0, 280)


def MQTTRIGHT():
    servo.setPWM(0, 0, 450)


def MQTTBACK():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.BACKWARD)


def MQTTSTOP():
    myMotor.run(Raspi_MotorHAT.RELEASE)
    servo.setPWM(0, 0, 380)


def MQTTMIDDLE():
    servo.setPWM(0, 0, 380)


"""
try:
    while True:
        command = input('command : ')
        if command == '1':
            GO()
        if command == '2':
            LEFT()
        if command == '3':
            RIGHT()
        if command == '4':
            BACK()
        if command == '5':
            STOP()
        if command == '6':
            MIDDLE()
        if command == 'exit':
            break

finally:
    myMotor.run(Raspi_MotorHAT.RELEASE)
"""
