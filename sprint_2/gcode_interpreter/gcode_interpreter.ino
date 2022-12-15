/**
  * Principles of Integrated Engineering - PIE Final Project
  * Name: gcode_interpreter
  * Purpose: interpret gcode commands into arduino for mehendi bot

  * @author: Rucha Dave
  * @version: 1.1
  */

#include <Stepper.h>

// Define motors
Stepper stepperY1(200, 2, 3);
Stepper stepperX(200, 4, 5);
Stepper stepperY2(200, 6, 7);

int STEPS = 200;
int PICK_SPEED = 50;


String curr_line;
float feedrate = 0;
float step_delay = 1;

// Define current position of ink
float x_pos;
float y_pos;
float reset;
float x_change;
float y_change;

/**
  * Provide basic description of project and what each function does
  */  
void help() {
  // Serial.println("Mehendi Bot");
}

/**
  * Set feedrate and step_delay based on the value entered.
  * @param: fr float representing new feedrate
  */
void set_feedrate(float fr) {
  step_delay = 1000000.0/fr;
  feedrate = fr;
}

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  help();
  set_feedrate(5000);
  stepperX.setSpeed(PICK_SPEED);
  stepperY1.setSpeed(PICK_SPEED);
  stepperY2.setSpeed(PICK_SPEED);

  x_pos = 0;
  y_pos = 0;
  ready();
}

/**
  * Initiate serial
  */
void ready() {
  curr_line = "";
}

/**
  * Create a delay for time specified
  * @param: ms long representing the milliseconds of delay wanted
  */
void pause(long ms) {
  delay(ms/1000);
  delayMicroseconds(ms%1000);  // delayMicroseconds doesn't work for values > ~16k.
}

/**
  * Using ABSOLUTE positions, move to inputted x,y coordinates. 
  * This is done using Breseham's Line Algorithm.
  * @param: new_x String representing the new x-position
  * @param: new_y String representing the new y-position
  */
void moveLine(String new_x, String new_y) {
  float x_new = new_x.toFloat() * 7;
  float y_new = new_y.toFloat() * 7;

  // Find relative distance to move
  x_change = abs(x_new - x_pos);
  y_change = abs(y_new - y_pos);

  int x_dir;
  int y_dir; 
  
  // Set direction of x movement
  if (x_new > x_pos) {
    x_dir = -1;
  } else {
    x_dir = 1;
  }

  // Set direction of y movement
  if (y_new > y_pos) {
    y_dir = -1;
  } else {
    y_dir = 1;
  }

  // Implement Breseham's Algorithm
  if (x_change > y_change) {
    reset = x_change / 2;
    for (int i = 0; i < x_change; i++) {
      stepperX.step(x_dir);
      reset += y_change;
      if (reset >= x_change) {
        reset -= x_change;
        stepperY1.step(y_dir);
        stepperY2.step(y_dir);
      }
    }
  }
  else {
    // Serial.println(y_change);
    reset = y_change / 2;
    for (int i = 0; i < y_change; i++) {
      // Serial.print(step_delay);
      stepperY1.step(y_dir); 
      stepperY2.step(y_dir);  
      reset += x_change;
      if (reset >= y_change) {
        reset -= y_change;
        stepperX.step(x_dir);
      }
    }
  }
  set_feedrate(5000);

  // Set new positions
  x_pos = x_new;
  y_pos = y_new;
}

void loop() {
  if (Serial.available()) {
    char this_char = Serial.read();
    curr_line += this_char;

    // Run command per line
    if ((this_char == ';') && (curr_line.length() > 0)) {
      Serial.print(curr_line);
      runCommand();
      curr_line = "";

    }
  }
}

/**
  * Given commands in GCode, perform the actions required
  */
void runCommand() {
  int G_command;
  
  if (curr_line.indexOf(" ") != -1) {
    G_command = (curr_line.substring(curr_line.indexOf("G") + 1, curr_line.indexOf(" ") + 1)).toInt();
  }
  else {
    G_command = (curr_line.substring(curr_line.indexOf("G") + 1)).toInt();    
  }

  // Run G commands
  if (G_command != 0) {
    // If 01 or 1 command, move in a line to the position X, Y given at speed F given (absolute positions)  
    if (G_command == 1) {
      int F_speed_index = curr_line.indexOf("F");
      if (F_speed_index > -1) {
        set_feedrate(curr_line[F_speed_index]);
      }
      
      int X_index = curr_line.indexOf("X");
      int X_end = X_index + curr_line.substring(X_index).indexOf(" ");
      int Y_index = curr_line.indexOf("Y");
      moveLine(curr_line.substring(X_index + 1, X_end + 1), curr_line.substring(Y_index + 1)); 
    }

    // If 04, delay for the time P given
    if (G_command == 4) {
      int delay_period = curr_line.substring(curr_line.indexOf("P") + 1).toInt();
      delay(delay_period * 1000);
    }
    
  }
}
