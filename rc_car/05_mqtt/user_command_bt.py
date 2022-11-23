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

