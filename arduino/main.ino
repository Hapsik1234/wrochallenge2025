#include <Wire.h>
#include <VL53L1X.h>

VL53L1X sensor;

String input;
bool send = false;

void setup() {
  Serial.begin(9600);
  
  Wire.begin();

  sensor.setTimeout(500);
  if (!sensor.init()) {
    Serial.println("Failed to detect and initialize sensor!");
    while (1);
  }

  sensor.setDistanceMode(VL53L1X::Medium);  // Options: Short, Medium, Long
  sensor.setMeasurementTimingBudget(50000);  // in microseconds
  sensor.startContinuous(50);  // Start continuous readings every 50 ms

}

void loop() {


  if (Serial.available() > 0) {

    input = Serial.readString();

    if (input=="y\n") {
      send = true;
    } else if (input=="n\n") {
      send = false;
    }

  }

  if (send) {
    Serial.println(sensor.read());
    delay(50);
  }

}