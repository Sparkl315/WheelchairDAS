/*
 * @name joy2motor v4
 * @note joystick input manipulation
 */

/* PINOUTS */
#define pinA      A0
#define pinB      A1
#define pinAout   5
#define pinBout   6

/* I/O Variables */
#define MAX_INPUT 50
int JoyInput[2];
int JoyOutput[2];

void processIncomingByte (const byte inByte) {
  static char input_line[MAX_INPUT];
  static unsigned int input_pos = 0;

  switch (inByte) {
    case '\n':                    // end of text
      input_line[input_pos] = 0;  // Terminate input
      process_data(input_line);   // Process input line
      input_pos = 0;              // reset buffer for next time
      break;

    case '\r':   // discard carriage return
      break;

    default:
      // Get inBytes
      if (input_pos < (MAX_INPUT - 1)) {
        input_line [input_pos++] = inByte;
      }        
      break;

  }  // end of switch
}

void Val_Get() {
  JoyInput[0] = analogRead(pinA);
  JoyInput[1] = analogRead(pinB);
}

void Val_Manipulate() {
  
}

void Val_Output() {
  JoyOutput[0] = JoyInput[0];
  JoyOutput[1] = JoyInput[1];
}

void setup() {
  // put your setup code here, to run once:
  pinMode(pinA, INPUT);
  pinMode(pinB, INPUT);
  pinMode(pinAout, OUTPUT);
  pinMode(pinBout, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    processIncomingByte(Serial.read());
  }
  
}
