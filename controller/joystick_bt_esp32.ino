#include "BluetoothSerial.h"
#include "esp_bt_device.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

int JoyStick_X = A0; // Analog Pin  X
int JoyStick_Y = A3; // // Analog Pin  Y
int JoyStick_button = 34; // IO Pin

void printDeviceAddress(){
  const uint8_t* point = esp_bt_dev_get_address();
  for (int i = 0; i < 6; i++){
    char str[3];
    sprintf(str, "%02X", (int)point[i]);
    Serial.print(str);

    if (i < 5){
      Serial.print(":");
    }
  }
}

void setup()
{
    pinMode(JoyStick_X, INPUT);
    pinMode(JoyStick_Y, INPUT);
    pinMode(JoyStick_button, INPUT_PULLUP);
    Serial.begin(115200);
    //Serial.begin(9600);
    SerialBT.begin("ESP32test"); //Bluetooth device name
    Serial.println("The device started, now you can pair it with bluetooth!");
    printDeviceAddress();
    Serial.println();
}
void loop()
{
    int x, y, button;
    x = analogRead(JoyStick_X); //  X
    y = analogRead(JoyStick_Y); //  Y
    button = digitalRead(JoyStick_button); // 
    x = map(x, 0, 4095, -255, 255);
    y = map(y, 0, 4095, 280, 450);
    
    Serial.print("X : ");
    Serial.print(x, DEC);
    Serial.print(" / Y : ");
    Serial.print(y, DEC);
    Serial.print(" , B : ");
    Serial.println(button, DEC);

    SerialBT.print("Vel:" + String(x) + "|Dir:" + String(y));
    delay(100);
}
