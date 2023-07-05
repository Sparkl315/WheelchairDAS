/**
 * @name     Joystick Input Manipulation Module
 * @brief    Retrieve Joystick Voltage Input from MLX90333 and Output Manipulated Voltage Output
 *            - Input & Output Voltage Range : 0 ~ 5V
 * @version  04
 */

/* PINOUTS */
#define pinA       A0
#define pinB       A1
#define pinAout    5
#define pinBout    6

/* I/O Variables */
#define MAX_INPUT  50   // Prevent Serial Input Overflow
int     JoyInput[2];
int     JoyOutput[2];

/* Obstacle Detector Variables */
#define POSIS      6    // Positions (LF, L, LB, RB, R, RF)
//  POSITIONS - ARRAY ID
#define LF         0
#define L          1
#define LB         2
#define RB         3
#define R          4
#define RF         5
bool    Obstacle_Exist[POSIS];    //  [LF, L, LB, RB, R, RF]

/* Process Serial Inputs */
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

void process_data(const char * input) {
  for (int i; i < POSIS; i++) {
    if(input[i] == "1") Obstacle_Exist[i] = true;
    if(input[i] == "0") Obstacle_Exist[i] = false;
  }
}

/* Joystick Value Manipulations */
// Retrieve joystick input values
void Val_Get() {
  JoyInput[0] = analogRead(pinA);
  JoyInput[1] = analogRead(pinB);
}

// Change joystick value if obstacle exists
void Val_Manipulate() {
  if(Obstacle_Exist[LF]) {

  }
  if(Obstacle_Exist[L]) {

  }
  if(Obstacle_Exist[LB]) {

  }
  if(Obstacle_Exist[RB]) {

  }
  if(Obstacle_Exist[R]) {

  }
  if(Obstacle_Exist[RF]) {

  }
}

void Val_Output() {
  // Convert Resolution of ADC Input to PWM Output  (1024 to 256)
  JoyOutput[0] = JoyInput[0]/4;
  JoyOutput[1] = JoyInput[1]/4;
  
  // AnalogWrite to Channel A & B PWM pinout
  AnalogWrite(pinAout, JoyOutput[0]);
  AnalogWrite(pinBout, JoyOutput[1]);
}

/* Main Workflow */
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
  Val_Get();
  Val_Manipulate();
  Val_Output();
}
