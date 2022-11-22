import user_command as CAR_CMD
from time import sleep

from lirc import RawConnection

cnt = 0;
def ProcessIRRemote():

    # get IR command
    # keypress format = (hexcode, repeat_num, command_key, remote_id)
    try:
        keypress = conn.readline(.0001)
    except:
        keypress = ""

    if (keypress != "" and keypress != None):
        global cnt
        cnt += 1
        data = keypress.split()
        sequence = data[1]
        command = data[2]

        # ignore command repeats
        # if (sequence != "00"):
        #     return
        if (command == "KEY_UP"):
            CAR_CMD.go()
        if (command == "KEY_DOWN"):
            CAR_CMD.back()
        if (command == "KEY_LEFT"):
            CAR_CMD.steer_left()
        if (command == "KEY_RIGHT"):
            CAR_CMD.steer_right()
        if (command == "KEY_OK"):
            CAR_CMD.steer_center()
        if (command == "KEY_POWER"):
            CAR_CMD.stop()

        print(command)


# define Global
conn = RawConnection()
print("Starting Up...")
try:
    while True:
        if cnt > 1000:
            break
        ProcessIRRemote()

finally:
    CAR_CMD.STOP()
