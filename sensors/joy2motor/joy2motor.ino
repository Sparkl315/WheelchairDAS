#include <Wire.h>

#define pinA A1
#define pinB A2

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
  pinMode(A3, OUTPUT);
  pinMode(A4, OUTPUT); 
  Serial.begin(9600);

}

void ReportA(){
  var = analogRead(pinA);
  
  if(var > averageA + 100){
    out1 = 700;
    analogWrite(A3, out1/4);
    Serial.print(out1);
  }
  else if(var < averageA - 100){
    out1 = 300;
    analogWrite(A3, out1/4);
    Serial.print(out1);
  }
  else {
    out1 = 500;
    analogWrite(A3, out1/4);
    Serial.print(out1);
  }
}

void ReportB(){
 
  var2 = analogRead(pinB);
  
  if(var2 > averageB + 250){
    out2 = 700;
    analogWrite(A4, out2/4);
    Serial.println(out2);
  }
  else if(var2 < averageB - 250){
    out2 = 300;
    analogWrite(A4, out2/4);
    Serial.println(out2);
  }
  else{
    out2 = 500;
    analogWrite(A4, out2/4);
    Serial.println(out2);
  }

}


void loop() {
  // put your main code here, to run repeatedly:
  if (calibrationA_bool == true) {
    calibrationA();
   }
    if (calibrationB_bool == true) {
    calibrationB();
    }  
    ReportA();
    Serial.print("   "); 
    ReportB();
  }
  
