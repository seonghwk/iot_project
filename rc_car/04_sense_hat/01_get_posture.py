from sense_hat import SenseHat

sense = SenseHat()

while True:
    acceleration = sense.get_accelerometer_raw()
    orientation = sense.get_orientation()

    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    pitch = orientation['pitch']
    roll = orientation['roll']
    yaw = orientation['yaw']

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)

    #print("x={0}, y={1}, z={2}".format(x, y, z))
    print ("pitch {} roll {} yaw {}".format(pitch, roll, yaw))
