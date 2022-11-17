/**
  * Principles of Integrated Engineering - PIE Final Project
  * Name: gcode_interpreter
  * Purpose: interpret gcode commands into arduino for mehendi bot

  * @author: Cherry Pham, Emma Mascillaro, and Rucha Dave 
  * @version: 1.1
  */
#include <Stepper.h>

// Define motors
Stepper stepperY1(200, 4, 5);
Stepper stepperX(200, 6, 7);
Stepper stepperY2(200, 2, 3);

String curr_line;
float feedrate = 0;
float step_delay = 0;

// Define current position of ink
float x_pos;
float y_pos;
float reset;

/**
  * Provide basic description of project and what each function does
  */  
void help() {
  Serial.println("Mehendi Bot");
}

void setup() {
  Serial.begin(9600);
  
  stepperY1.setSpeed(0);
  stepperY2.setSpeed(0);

  help();
}


void loop() {
  // Move motors in direction specified
  stepperY1.step(1);
  stepperY2.step(1);
}
