/**
  * Principles of Integrated Engineering - PIE Final Project
  * Name: gcode_interpreter
  * Purpose: interpret gcode commands into arduino for mehendi bot

  * @author: Cherry Pham, Emma Mascillaro, and Rucha Dave 
  * @version: 1.1
  */
#include <Stepper.h>

// Define motors
Stepper stepperY1(200, 2, 3);
Stepper stepperX(200, 4, 5);
Stepper stepperY2(200, 6, 7);

String curr_line;
float feedrate = 0;
float step_delay = 0;

// Define current position of ink
float x_pos;
float y_pos;
float reset;

void setup() {
  Serial.begin(9600);

  stepperY1.setSpeed(60);
  stepperY2.setSpeed(60);
  stepperX.setSpeed(30);
}


void loop() {
  // Move motors in direction specified
   stepperY1.step(1);
   stepperY2.step(1);
//   stepperX.step(1);
}
