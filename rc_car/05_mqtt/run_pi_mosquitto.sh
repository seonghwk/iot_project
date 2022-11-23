#!/bin/bash
sudo /etc/init.d/mosquitto stop
sudo mosquitto -c /etc/mosquitto/mosquitto.conf -v
