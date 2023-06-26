#define pinA A1
#define pinB A2
#define pinOutA 3
#define pinOutB 6

void output(int pin, int data) {
  analogWrite(pin, data);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(pinA, INPUT);
  pinMode(pinB, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int dataA = analogRead(pinA);
//  Serial.print(" ");
//  Serial.println(analogRead(pinB));
  Serial.print(dataA);
  Serial.print(" ");
  Serial.println(analogRead(pinA));
  output(pinOutA, dataA);
}
