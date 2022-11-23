from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
from time import sleep

mh = Raspi_MotorHAT(addr=0x6f)
motor = mh.getMotor(2)

servo = PWM(0x6F)
servo.setPWMFreq(60)  # Set frequency to 60 Hz

speed = 0
motor.setSpeed(speed)

SERVO_PULSE_MAX = 450   # servo range
SERVO_PULSE_MIN = 280
SERVO_PULSE_CENTER = 380
steer = 380

def GO():
    global speed
    if (speed > 0):
        speed = min(250, speed + 25)
    else:
        speed = max(-250, speed + 25)
    motor.setSpeed(abs(speed))
    if (speed > 0):
        motor.run(Raspi_MotorHAT.FORWARD)
    if (speed < 0):
        motor.run(Raspi_MotorHAT.BACKWARD)

def BACK():
    global speed
    if (speed > 0):
        speed = min(250, speed - 25)
    else:
        speed = max(-250, speed - 25)
    motor.setSpeed(abs(speed))
    if (speed > 0):
        motor.run(Raspi_MotorHAT.FORWARD)
    if (speed < 0):
        motor.run(Raspi_MotorHAT.BACKWARD)

def STOP():
    global speed
    speed = 0
    motor.setSpeed(speed)
    motor.run(Raspi_MotorHAT.RELEASE)

def LEFT():
    global steer
    if (steer <= SERVO_PULSE_CENTER):
        steer = max(steer - 20, SERVO_PULSE_MIN)
    else:
        steer = steer - 14
    servo.setPWM(0, 0, steer)

def RIGHT():
    global steer
    if (steer >= SERVO_PULSE_CENTER):
        steer = min(steer + 14, SERVO_PULSE_MAX)
    else:
        steer += 20
    servo.setPWM(0, 0, steer)

def MIDDLE():
    global steer
    steer = 380
    servo.setPWM(0, 0, steer)