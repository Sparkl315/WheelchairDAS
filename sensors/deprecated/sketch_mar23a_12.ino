#define pinA 3
#define pinB A2

int total;

void setup() {
  // put your setup code here, to run once:
  pinMode(pinA, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  total = 0;
  for (int i=0;i<5;i++) {
    int dataA = digitalRead(pinA);
    total += dataA;
    if (i==4) {
      total /= 5;
      Serial.println(total);
    }
  }; 
}
