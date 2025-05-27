#include <Wire.h>
#include <VL53L1X.h>

VL53L1X sensor1;
VL53L1X sensor2;

String input;
bool send = false;
bool flag = false;

void setup() {
  Serial.begin(9600);

  Wire.begin();

  sensor1.setTimeout(500);
  if (!sensor1.init()) {
    Serial.println("Failed to detect and initialize sensor!");
    while (1)
      ;
  }

  sensor1.setAddress(0x30);
  Serial.println("Address set to 0x30");

  sensor1.setDistanceMode(VL53L1X::Medium);   // Options: Short, Medium, Long
  sensor1.setMeasurementTimingBudget(50000);  // in microseconds
  sensor1.startContinuous(50);                // Start continuous readings every 50 ms

  Serial.println("sensor1 initalized?");

  while (!flag) {
    if (Serial.available() > 0) {
      input = Serial.readString();
      if (input == "c\n") {
        flag = true;
      } else {
        Serial.println("Received " + input);
      }
    }
  }
  
  Serial.println("Now!");

  sensor2.setTimeout(500);

  if (!sensor2.init()) {
    Serial.println("Failed to detect and initialize sensor!");
    while (1)
      ;
  }

  sensor2.setDistanceMode(VL53L1X::Medium);   // Options: Short, Medium, Long
  sensor2.setMeasurementTimingBudget(50000);  // in microseconds
  sensor2.startContinuous(50);                // Start continuous readings every 50 ms

}

void loop() {


  if (Serial.available() > 0) {

    input = Serial.readString();

    if (input == "y\n") {
      send = true;
    } else if (input == "n\n") {
      send = false;
    }
  }


  // Sends '<sensor1_readings[mm]>, <sensor2_readings[mm]>', eg. '1023, 67'
  if (send) { 
    Serial.print(sensor1.read());
    Serial.print(", ");
    Serial.println(sensor2.read());
    delay(50);
  }
}