import user_command as CAR_CMD
from time import sleep

from lirc import RawConnection


def ProcessIRRemote():

    # get IR command
    # keypress format = (hexcode, repeat_num, command_key, remote_id)
    try:
        keypress = conn.readline(.0001)
    except:
        keypress = ""

    if (keypress != "" and keypress != None):

        data = keypress.split()
        sequence = data[1]
        command = data[2]

        # ignore command repeats
        # if (sequence != "00"):
        #     return
        if (command == "KEY_UP"):
            CAR_CMD.GO()
        if (command == "KEY_DOWN"):
            CAR_CMD.BACK()
        if (command == "KEY_LEFT"):
            CAR_CMD.LEFT()
        if (command == "KEY_RIGHT"):
            CAR_CMD.RIGHT()
        if (command == "KEY_OK"):
            CAR_CMD.MIDDLE()
        if (command == "KEY_POWER"):
            CAR_CMD.STOP()

        print(command)


# define Global
conn = RawConnection()
print("Starting Up...")
try:
    while True:
        ProcessIRRemote()

finally:
    CAR_CMD.STOP()
