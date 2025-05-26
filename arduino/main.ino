#include <Wire.h>
#include <VL53L1X.h>

#define GATE_MOTEN 5
#define GATE_MOTO1 4
#define GATE_MOTO2 3

#define SENS_MOTEN 8
#define SENS_MOTO1 7
#define SENS_MOTO2 6

const String icode = "b4115erwin";


class LegoMotor {

  public:

  int port_1, port_2, port_en;

  LegoMotor(int _port_1, int _port_2, int _port_en) {
    pinMode(_port_en, OUTPUT);
    pinMode(_port_1, OUTPUT);
    pinMode(_port_2, OUTPUT);

    port_1 = _port_1;
    port_2 = _port_2;
    port_en = _port_en;
  }

  void move(int speed) {
    if (speed > 100)
      speed = 100;
    if (speed < -100)
      speed = -100;

    analogWrite(port_en, int(abs(speed) * 2.55));

    if (speed > 0)
    {
      digitalWrite(port_1, HIGH);
      digitalWrite(port_2, LOW);
    }
    else
    {
      digitalWrite(port_1, LOW);
      digitalWrite(port_2, HIGH);
    }
  }


  void stop() {
    digitalWrite(port_1, LOW);
    digitalWrite(port_2, LOW);
  }
  

};

VL53L1X sensor1;
VL53L1X sensor2;

LegoMotor gate = LegoMotor(GATE_MOTO1, GATE_MOTO2, GATE_MOTEN);
LegoMotor sensors_deployer = LegoMotor(SENS_MOTO1, SENS_MOTO2, SENS_MOTEN);

String input;
bool send = false;
bool flag = false;

int time = 150;

void setup()
{
  Serial.begin(9600);


  // Waiting for "c\n" command from brick
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
  input = "";
  flag = false;

  Serial.println("Setting up...");


  

  Wire.begin();

  sensor1.setTimeout(500);
  if (!sensor1.init()) {
    Serial.println("Failed to detect and initialize sensor!");
    Serial.print(icode);
    Serial.println("Es1init.");
    while (1)
      ;
  }

  sensor1.setAddress(0x30);
  Serial.println("Address set to 0x30");
  Serial.print(icode);
  Serial.println("Ss1addr.");

  sensor1.setDistanceMode(VL53L1X::Medium);   // Options: Short, Medium, Long
  sensor1.setMeasurementTimingBudget(50000);  // in microseconds
  sensor1.startContinuous(50);                // Start continuous readings every 50 ms

  Serial.println("Sensor 1 initialized, waiting for sensor insertion.");

  Serial.print(icode);
  Serial.println("Ss1wait.");

  while (!flag) {
    if (Serial.available() > 0) {
      input = Serial.readString();
      if (input == "c\n") {
        flag = true;
      } else {
        Serial.print("Received ");
        Serial.println(input);
      }
    }
  }

  input = "";
  flag = false;
  
  Serial.println("Initializing senor 2.");
  Serial.print(icode);
  Serial.println("Is2init.");

  sensor2.setTimeout(500);

  if (!sensor2.init()) {
    Serial.println("Failed to detect and initialize sensor!");
    Serial.print(icode);
    Serial.println("Es2.");
    while (1)
      ;
  }

  Serial.println("Successfully initialized senor 2!");
  Serial.print(icode);
  Serial.println("Ss2init.");

  sensor2.setDistanceMode(VL53L1X::Medium);   // Options: Short, Medium, Long
  sensor2.setMeasurementTimingBudget(50000);  // in microseconds
  sensor2.startContinuous(50);                // Start continuous readings every 50 ms
}

void loop()
{
  if (Serial.available() > 0) {

    input = Serial.readString();

    if (input=="startsensing\n") {
      send = true;
    } else if (input == "stopsensing\n") {
      send = false;
    } else if (input == "gatedown\n") {
      gate.move(-100);
      delay(time);
      sensors_deployer.stop();
    } else if (input == "gateup\n") {
      gate.move(100);
      delay(time);
      sensors_deployer.stop();
    } else if (input == "sensorsup\n") {
      gate.move(-100);
      delay(time);
      sensors_deployer.stop();
    } else if (input == "sensorsdown\n") {
      gate.move(100);
      delay(time);
      sensors_deployer.stop();
    }
    input = "";
  }


  // Sends '<sensor1_readings[mm]>, <sensor2_readings[mm]>', eg. '1023, 67'
  if (send) { 
    Serial.print(icode);
    Serial.print("Isens.");
    Serial.print(sensor1.read());
    Serial.print(", ");
    Serial.println(sensor2.read());
    delay(50);
  }


}