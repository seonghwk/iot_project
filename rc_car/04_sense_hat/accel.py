from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    acc = sense.get_accelerometer_raw()
    print(f'[{acc["x"]:5.3f}] - ', end = '')
    print(f'[{acc["y"]:5.3f}] - ', end = '')
    print(f'[{acc["z"]:5.3f}]', end = '')
    print()
    sleep(0.1)
