#!/usr/bin/python
#https://physicsopenlab.org/2020/01/21/raspberry-pi-sense-hat/

from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from datetime import datetime
from csv import writer
import time
import sys

sense = SenseHat()
sense.set_imu_config(True, True, True)  # accelerometer, magnetometer , gyroscope
sense.clear()

logging = False

def get_sense_data():
  sense_data = []
  temperature = round(sense.get_temperature(),2)
  pressure = round(sense.get_pressure(),2)
  humidity = round(sense.get_humidity(),2)
  sense_data.append(temperature)
  sense_data.append(pressure)
  sense_data.append(humidity)
  
  mag = sense.get_compass_raw()
  mag_x = round(mag["x"],2)
  mag_y = round(mag["y"],2)
  mag_z = round(mag["z"],2)
  sense_data.append(mag_x)
  sense_data.append(mag_y)
  sense_data.append(mag_z)

  acc = sense.get_accelerometer_raw()
  acc_x = round(acc["x"],3)
  acc_y = round(acc["y"],3)
  acc_z = round(acc["z"],3)
  sense_data.append(acc_x)
  sense_data.append(acc_y)
  sense_data.append(acc_z)
  
  gyro = sense.get_orientation()
  pitch = round(gyro["pitch"],2)
  roll = round(gyro["roll"],2)
  yaw = round(gyro["yaw"],2)
  sense_data.append(pitch)
  sense_data.append(roll)
  sense_data.append(yaw)  
  
  sense_data.append(datetime.now())
  
  return sense_data

def pushed_up(event):
  global logging, timestart
  if event.action == ACTION_PRESSED:
    print("START")
    logging = True

def pushed_down(event):
  global logging
  if event.action != ACTION_PRESSED:
    print("STOP")
    logging = False

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down

timestamp = datetime.now()
timestart = datetime.now()
delay = 100 #milliseconds

with open('data.csv', 'w', newline='') as f:
  data_writer = writer(f)
  data_writer.writerow(['temp','pres','hum',
                        'mag_x','mag_y','mag_z',
                        'acc_x','acc_y','acc_z',
                        'pitch','roll','yaw',
                        'datetime','elapsed'])    
    
  while True:
    if logging:  
      data = get_sense_data()
      dt = data[-1] - timestamp
      elapsed = data[-1] - timestart
      if int(dt.total_seconds()*1000) > delay:
        #print(round(elapsed.total_seconds()*1000))
        data.append(round(elapsed.total_seconds()*1000))
        data_writer.writerow(data)
        timestamp = datetime.now()

