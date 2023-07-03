#include <NewPing.h>
#include <string.h>

/* Define All Necessary Pins */
#define TOTAL_SONAR 6
#define ECHO_PIN     2
#define TRIGGER_PIN  3
#define ECHO_PIN_2     4
#define TRIGGER_PIN_2  5
#define ECHO_PIN_3     6
#define TRIGGER_PIN_3  7
#define ECHO_PIN_4     8
#define TRIGGER_PIN_4  9
#define ECHO_PIN_5     10
#define TRIGGER_PIN_5  11
#define ECHO_PIN_6     12
#define TRIGGER_PIN_6  13

/* Ultrasound Constants */
// Range
#define SONAR_LIMIT    0.8                        // Minimum distance (in centimeters)
#define MAX_DISTANCE   200                        // Maximum distance (in centimeters)
// Calibration
#define TEMP           25.5                       // Temperature calibration constant
#define CALI_FACTOR    sqrt(1+TEMP/273.15)/60.368 // Speed of sound calculation based on temperature


float storePast[TOTAL_SONAR];
float storeCur[TOTAL_SONAR];

/* Setup NewPing */
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
NewPing sonar2(TRIGGER_PIN_2, ECHO_PIN_2, MAX_DISTANCE);
NewPing sonar3(TRIGGER_PIN_3, ECHO_PIN_3, MAX_DISTANCE);
NewPing sonar4(TRIGGER_PIN_4, ECHO_PIN_4, MAX_DISTANCE); 


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

  float distance = (float)sonar.ping_cm() * CALI_FACTOR; // Send ping, get distance in cm and print result (0 = outside set distance range)
  distance = filter(distance, 0);
  // distance *= 0.01;

  hold();
  
  float distance2 = (float)sonar2.ping_cm() * CALI_FACTOR; // Send ping, get distance in cm and print result (0 = outside set distance range)
  distance2 = filter(distance2, 1);
  // distance2 *= 0.01;

  hold();

  float distance3 = (float)sonar3.ping_cm() * CALI_FACTOR; // Send ping, get distance in cm and print result (0 = outside set distance range)
  distance3 = filter(distance3, 2);
  // distance3 *= 0.01;

  hold();

  float distance4 = (float)sonar4.ping_cm() * CALI_FACTOR; // Send ping, get distance in cm and print result (0 = outside set distance range)
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
