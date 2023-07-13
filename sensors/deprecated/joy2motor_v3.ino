#include <Wire.h>

#define pinA A0
#define pinB A1

const int numReadings = 10;

int var;
int var2;
int readings[numReadings];
int total = 0;
int averageA = 0;
int averageB = 0;
int out1;
int out2;
bool calibrationA_bool = true;
bool calibrationB_bool = true;

void calibrationA() {
  for (int i=0;i<10;i++){
  readings[i] = analogRead(pinA);
  total = total + readings[i];
  } 
  averageA = total/10;
  Serial.print("average A: ");
  Serial.print(averageA);
  calibrationA_bool = false;
  total = 0;
}

void calibrationB() {
  for (int i=0;i<10;i++){
  readings[i] = analogRead(pinB);
  total = total + readings[i];
  } 
  averageB = total/10;
  Serial.print("average B: ");
  Serial.print(averageB);
  calibrationB_bool = false;
}

void setup() {
  // put your setup code here, to run once:
  
  pinMode(pinA, INPUT);
  pinMode(pinB, INPUT);
  Serial.begin(9600);

}

void ReportA(){
   var = analogRead(pinA);
if(var > averageA + 100){
  out1 = 700;
  Serial.print(out1);

}
else if(var < averageA - 100){
  out1 = 300;
  Serial.print(out1);

}
  else {
  out1 = 500;
  Serial.print(out1);

  }
}

void ReportB(){
 
  var2 = analogRead(pinB);
if(var2 > averageB + 250){
  out2 = 700;
  }

else if(var2 < averageB - 250){
  out2 = 300;
  }

  else{
  out2 = 500;
  }
  
if (RF == false && out2 == 700) {
   out2 = 500;
}
if (RM == false && out2 == 00) {
   out2 = 500;
}
if (RB == false && out2 == 00) {
   out2 = 500;
}
 Serial.println(out2);
}


void loop() {
  // put your main code here, to run repeatedly:
  if (calibrationA_bool == true) {
    calibrationA();
   }
    if (calibrationB_bool == true) {
    calibrationB();
    }  
    DetectObs();
    ReportA();
    Serial.print("   "); 
    ReportB();

}

void DetectObs(){
bool LF = true;
bool LM = true;
bool LB = true;
bool RF = true;
bool RM = true;
bool RB = true;
int value1 = value2 = value3 = value4 = value5 = value6 = 11

  if (value1 < 10) {
  LF = false;
  }

  if (value2 < 10) {
  LM = false;
  }

  if (value3 < 10) {
  LB = false;
  }

  if (value4< 10) {
  RF = false;
  }

  if (value5 < 10) {
  RM = false;
  }

  if (value6< 10) {
  RB = false;
  }
  
}
