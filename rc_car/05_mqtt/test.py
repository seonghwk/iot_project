import paho.mqtt.client as mqtt
from time import sleep
from lirc import RawConnection
from user_command import *
from bluetooth import *
from user_command_bt import *
from user_command_mqtt import *

def input_and_send():
    print("\nType something\n")
    while True:
        data = input()
        if len(data) == 0: break
        sock.send(data)
        sock.send("\n")

def rx_and_echo():
    sock.send("\nsend anything\n")
    data = sock.recv(buf_size)
    if data:
        command_src = data.decode('utf-8')
        if (command_src[0] != 'V'):
            return
        if not (command_src[-1].isnumeric()):
            return
        command = command_src.split("|")
        print(command)
        velVal = int(command[0].split(":")[1])
        dirVal = int(command[1].split(":")[1])
        #print(velVal, dirVal)
        if (velVal < -14):
            velVal = (velVal + 14) / 241 * 255
            motor.run(Raspi_MotorHAT.BACKWARD)
        else:
            velVal = (velVal + 14) / 269 * 255
            motor.run(Raspi_MotorHAT.FORWARD)
        motor.setSpeed(abs(int(velVal)))
        if (dirVal < 358):
            dirVal = (dirVal - 358) / 78 * 100 + 380
        else:
            dirVal = (dirVal - 358) / 92 * 70 + 380
        servo.setPWM(0,0,int(dirVal))
        print(f"Vel:{velVal}, Dir:{dirVal}")
        sock.send(data)

#MAC address of ESP32
addr = "8C:CE:4E:99:4E:72"
#uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
#service_matches = find_service( uuid = uuid, address = addr )
service_matches = find_service( address = addr )

#buf_size = 1024;
buf_size = 16

if len(service_matches) == 0:
    print("couldn't find the SampleServer service =(")
    sys.exit(0)

for s in range(len(service_matches)):
    print("\nservice_matches: [" + str(s) + "]:")
    print(service_matches[s])

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

#port=1
print("connecting to \"%s\" on %s, port %s" % (name, host, port))

# Create the client socket
sock=BluetoothSocket(RFCOMM)
sock.connect((host, port))

print("connected")

#input_and_send()

print("\n--- bye ---\n")

mode = 0
conn = RawConnection()

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
            GO()
        if (command == "KEY_DOWN"):
            BACK()
        if (command == "KEY_LEFT"):
            LEFT()
        if (command == "KEY_RIGHT"):
            RIGHT()
        if (command == "KEY_OK"):
            MIDDLE()
        if (command == "KEY_POWER"):
            STOP()

# subscriber callback
def on_message(client, userdata, message):
    global mode
    mode = int(message.payload.decode("utf-8"))
    #print(mode)

def on_message_2(client, userdata, message):
    control_cmd = str(message.payload.decode("utf-8"))
    if (mode != 3):
        return
    if (control_cmd == "KEY_UP"):
        MQTTGO()
    if (control_cmd == "KEY_DOWN"):
        MQTTBACK()
    if (control_cmd == "KEY_LEFT"):
        MQTTLEFT()
    if (control_cmd == "KEY_RIGHT"):
        MQTTRIGHT()
    if (control_cmd == "KEY_OK"):
        MQTTMIDDLE()
    if (control_cmd == "KEY_POWER"):
        MQTTSTOP()


broker_address = "70.12.225.207"
client1 = mqtt.Client("client1")
client2 = mqtt.Client("client2")
client1.connect(broker_address)
client2.connect(broker_address)
client1.subscribe("car/mode")
client2.subscribe("car/control")
client1.on_message = on_message
client2.on_message = on_message_2
client1.loop_start()
client2.loop_start()
print("HI")

while True:
    while mode == 1:
        ProcessIRRemote()
    myMotor.setSpeed(0)
    servo.setPWM(0,0,380)
    while mode == 2:
        rx_and_echo()
    myMotor.setSpeed(0)
    servo.setPWM(0,0,380)
    while mode == 3:
        pass
    myMotor.setSpeed(0)
    servo.setPWM(0,0,380)

client1.loop_stop()
client2.loop_stop()
STOP()
sock.close()
