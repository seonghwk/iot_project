#!/bin/bash
# Identify RPi device
# https://sleeplessbeastie.eu/2022/04/22/how-identify-raspberry-pi-device-using-built-in-leds/ 

# sysfs leds directory
leds_path="/sys/class/leds"

# default led trigger
led_trigger_def="default-on"

# temporary led trigger (heartbeat, timer)
led_trigger_tmp="heartbeat"

# script timeout
timeout="10"

# get leds (led0, led1, ..., led9)
get_leds(){
  find ${leds_path} -maxdepth 1 -follow -type d -name "led[0-9]" -printf '%f\n'
}

# get current trigger for specific led 
get_trigger(){
  if [ -n "${1}" ]; then
    cat ${leds_path}/${1}/trigger | awk -F "[][]" "{print \$2}"
  fi
}

# set trigger (second param) for specific led (first param)
set_trigger(){
  if [ -n "${1}" ] && [ -n "${2}" ]; then
    echo ${2} | tee ${leds_path}/${1}/trigger >/dev/null
  fi
}

# cleanup in case of exit or emergency
cleanup() {
  for led in $(get_leds); do
    if [ "$(get_trigger ${led})" == "${led_trigger_tmp}" ]; then
      set_trigger "${led}" "${led_trigger_def}"
    fi
  done
}
trap cleanup SIGINT EXIT

# main
for led in $(get_leds); do
  if [ "$(get_trigger ${led})" == "${led_trigger_def}" ]; then
    set_trigger "${led}" "${led_trigger_tmp}"
    sleep ${timeout}
  fi
done
