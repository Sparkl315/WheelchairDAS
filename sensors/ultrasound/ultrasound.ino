/**
 * @name      Side Obstacle Detection Module
 * @brief     Detect Obstacle with 6 x HC-SR04 Ultrasound module 
 *            Requires:   NewPing Library (by Tim Eckel)
 */

#include <NewPing.h>
#include <string.h>

#define TOTAL_SONAR    6
/* Define All Necessary Pins */
#define ECHO_PIN_1     2
#define TRIGGER_PIN_1  3
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
#define SONAR_LIMIT    0.8                        // User Defined Maximum distance (in meters)
#define MAX_DISTANCE   200                        // Hardware Maximum distance (in centimeters) FOR REFERENCE
// Calibration
#define TEMP           25.5                       // Temperature calibration constant
#define CALI_FACTOR    sqrt(1+TEMP/273.15)/60.368 // Speed of sound calculation based on temperature

// Variables
float distance[TOTAL_SONAR];
float storePast[TOTAL_SONAR];
float storeCur[TOTAL_SONAR];

String distString = "";    // Distance String Output (via Serial Port)


/* Setup NewPing */
NewPing sonar_array[TOTAL_SONAR] = {
  NewPing(TRIGGER_PIN_1, ECHO_PIN_1, MAX_DISTANCE),
  NewPing(TRIGGER_PIN_2, ECHO_PIN_2, MAX_DISTANCE),
  NewPing(TRIGGER_PIN_3, ECHO_PIN_3, MAX_DISTANCE),
  NewPing(TRIGGER_PIN_4, ECHO_PIN_4, MAX_DISTANCE),
  NewPing(TRIGGER_PIN_5, ECHO_PIN_5, MAX_DISTANCE),
  NewPing(TRIGGER_PIN_6, ECHO_PIN_6, MAX_DISTANCE)
};

/* Functions */

void storage(float data, int data_id) {
  storePast[data_id] = data;
}

// Remove data higher than user defined maximum
// Remove unwanted 0
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
  if (storage_bool == true) { // Save the data if not 0
    storage(tmp, data_id);    
  }
  return tmp;
}

// Delay For Ultrasound to receive transmitted wave
void hold() { 
  delay(30);
}

float get_sonar_value(int sonar_handler_id) {
  return (float)(sonar_array[sonar_handler_id].ping_cm()) * CALI_FACTOR;
}

/* Main Workflow */
void setup() {
  Serial.begin(115200);
  for (int i = 0; i < TOTAL_SONAR; i++) { // Initialize Storage
    storePast[i] = 0;
  }
}

void loop() {
  for (int sid = 0; sid < 6; sid++) {
    distance[sid] = filter(get_sonar_value(sid), sid);
    distString += (String(distance[sid]) + " ");
    hold();
  }
  distString += "\n"; // End of Data

  // Send Distance data through serial port
  Serial.write(distString.c_str());
  distString = "";  // reset Output String
}
