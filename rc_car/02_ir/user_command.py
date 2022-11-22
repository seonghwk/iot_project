from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
from time import sleep

mh = Raspi_MotorHAT(addr=0x6f)
motor = mh.getMotor(2)

servo = PWM(0x6F)
servo.setPWMFreq(60)  # Set frequency to 60 Hz

speed = 0
motor.setSpeed(speed)

servoCH = 0 # servo pin
SERVO_PULSE_MAX = 450   # servo range
SERVO_PULSE_MIN = 280

def go():
    global speed
    if speed < 250:
        speed = speed + 10
    motor.setSpeed(speed)
    motor.run(Raspi_MotorHAT.FORWARD)

def back():
    global speed
    if speed < 250:
        speed = speed + 10
    motor.setSpeed(speed)
    motor.run(Raspi_MotorHAT.BACKWARD)

def stop():
    global speed
    while speed >10:
        speed = speed - 10
        motor.setSpeed(speed)
        sleep(0.5)
    speed = 0
    motor.setSpeed(speed)
    motor.run(Raspi_MotorHAT.RELEASE)

def speed_up():
    global speed
    speed = 255 if speed >= 235 else speed + 20 
    motor.setSpeed(speed)

def speed_down():
    global speed
    speed = 0 if speed <= 20 else speed - 20 
    motor.setSpeed(speed)

def steer(angle = 0):   
    if angle <= -60:
        angle = -60
    if angle >= 60:
        angle = 60
    pulse_time = SERVO_PULSE_MIN + (SERVO_PULSE_MAX - SERVO_PULSE_MIN) // 180 * (angle + 90) 

    servo.setPWM(servoCH, 0, pulse_time)

def steer_right():
    steer(30)

def steer_left():
    steer(-30)

def steer_center():
    steer(0)
