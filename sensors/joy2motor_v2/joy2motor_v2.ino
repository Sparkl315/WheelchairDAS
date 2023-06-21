/* joy2motor v2
 * Updated on 16 June 2023
 */
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
  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);
  pinMode(A4, OUTPUT); 
  pinMode(A5, OUTPUT);
  Serial.begin(9600);

}

void ReportA(){
   var = analogRead(pinA);
if(var > averageA + 100){
  out1 = 700;
  Serial.print(out1);
  digitalWrite(A2,HIGH);
  digitalWrite(A3,HIGH);
}
else if(var < averageA - 100){
  out1 = 300;
  Serial.print(out1);
  digitalWrite(A2,LOW);
  digitalWrite(A3,LOW);
}
  else {
  out1 = 500;
  Serial.print(out1);
  digitalWrite(A2,LOW);
  digitalWrite(A3,HIGH);
  }
}

void ReportB(){
 
  var2 = analogRead(pinB);
if(var2 > averageB + 250){
  out2 = 700;
  Serial.println(out2);
  digitalWrite(A4,HIGH);
  digitalWrite(A5,HIGH);
}
else if(var2 < averageB - 250){
  out2 = 300;
  Serial.println(out2);
  digitalWrite(A4,LOW);
  digitalWrite(A5,LOW);
}
  else{
  out2 = 500;
  Serial.println(out2);
  digitalWrite(A4,LOW);
  digitalWrite(A5,HIGH);
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
  
