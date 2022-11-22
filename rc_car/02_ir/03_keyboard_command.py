from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
from time import sleep
from pynput import keyboard

mh = Raspi_MotorHAT(addr=0x6f)
myMotor = mh.getMotor(2)  # 핀번호

servo = PWM(0x6F)
servo.setPWMFreq(60)  # Set frequency to 60 Hz


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


def on_press(key):
    try:
      if key.char == 'w':
          GO()
      if key.char == 'a':
          LEFT()
      if key.char == 's':
          BACK()
      if key.char == 'd':
          RIGHT()
    except AttributeError:
        pass
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))


def on_release(key):
    try:
      if key.char == 'w' or key.char == 's':
          STOP()
      if key.char == 'a' or key.char == 'd':
          MIDDLE()
      # print('{0} released'.format(
      #     key))
      if key == keyboard.Key.esc:
          # Stop listener
          return False
    except AttributeError:
        pass


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

try:
    while True:
        print(listener)
        # command = input('command : ')
        # if command == '1':
        #     GO()
        # if command == '2':
        #     LEFT()
        # if command == '3':
        #     RIGHT()
        # if command == '4':
        #     BACK()
        # if command == '5':
        #     STOP()
        # if command == '6':
        #     MIDDLE()
        # if command == 'exit':
        #     break

finally:
    myMotor.run(Raspi_MotorHAT.RELEASE)
