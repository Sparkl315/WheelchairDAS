#include <NewPing.h>
#include <string.h>

#define TOTAL_SONAR 4
#define SONAR_LIMIT 0.8
#define ECHO_PIN     2
#define TRIGGER_PIN  3
#define ECHO_PIN_2     4
#define TRIGGER_PIN_2  5
#define ECHO_PIN_3     6
#define TRIGGER_PIN_3  7
#define ECHO_PIN_4     8
#define TRIGGER_PIN_4  9
#define MAX_DISTANCE 200 // Maximum distance we want to measure (in centimeters).


float storePast[TOTAL_SONAR];
float storeCur[TOTAL_SONAR];
float temp = 25.5; // Temperature in Celsius (this value would probably come from a temperature sensor).
float factor = sqrt(1 + temp / 273.15) / 60.368; // Speed of sound calculation based on temperature.

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.
NewPing sonar2(TRIGGER_PIN_2, ECHO_PIN_2, MAX_DISTANCE); // NewPing setup of pins and maximum distance.
NewPing sonar3(TRIGGER_PIN_3, ECHO_PIN_3, MAX_DISTANCE); // NewPing setup of pins and maximum distance.
NewPing sonar4(TRIGGER_PIN_4, ECHO_PIN_4, MAX_DISTANCE); // NewPing setup of pins and maximum distance.


void storage(float data, int data_id) {
  storePast[data_id] = data;
}

float filter(float data, int data_id) {
  float tmp = data;
  bool storage_bool = true;
  if (tmp > SONAR_LIMIT) {
    tmp = 0;
  }
  else if (tmp == 0) {
    tmp = storePast[data_id];
    storage_bool = false;
  }
  if (storage_bool == true) {
    storage(tmp, data_id);    
  }
  return tmp;
}

void hold() {
  delay(30);
}

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < TOTAL_SONAR; i++) {
    storePast[i] = 0;
  }
}

void loop() {
  hold();

  float distance = (float)sonar.ping_cm() * factor; // Send ping, get distance in cm and print result (0 = outside set distance range)
  distance = filter(distance, 0);
  // distance *= 0.01;

  hold();
  
  float distance2 = (float)sonar2.ping_cm() * factor; // Send ping, get distance in cm and print result (0 = outside set distance range)
  distance2 = filter(distance2, 1);
  // distance2 *= 0.01;

  hold();

  float distance3 = (float)sonar3.ping_cm() * factor; // Send ping, get distance in cm and print result (0 = outside set distance range)
  distance3 = filter(distance3, 2);
  // distance3 *= 0.01;

  hold();

  float distance4 = (float)sonar4.ping_cm() * factor; // Send ping, get distance in cm and print result (0 = outside set distance range)
  distance4 = filter(distance4, 3);
  // distance4 *= 0.01;
  
  String distString = String(distance) + " " + String(distance2) + " " + String(distance3) + " " + String(distance4) + "\n";

  Serial.write(distString.c_str());
  // Serial.print("Distance: ");
  // Serial.print(distance);
  // // Serial.print("m");
  // Serial.print(" ");
  // Serial.print(distance2);
  // // Serial.print("m");
  // Serial.print(" ");
  // Serial.print(distance3);
  // // Serial.print("m");
  // Serial.print(" ");
  // Serial.println(distance4);
  // // Serial.println("m");
}