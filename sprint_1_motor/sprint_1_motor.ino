/**
    PIE Final Project Sprint 1
    Name: Mehendi Bot
    Purpose: Guide a marker into a square spiral using 3 DC motors

    @author: Rucha Dave
    @version: 1.0 10/31/2022
 **/
 
#include <Adafruit_MotorShield.h>

// Designate motors and motor shield
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *motorLeft = AFMS.getMotor(2);
Adafruit_DCMotor *motorRight = AFMS.getMotor(1);
Adafruit_DCMotor *motorCenter = AFMS.getMotor(3);


// Set motor commands to loop over
// motorLeft, motorRight, motorCenter
String motorCommands[4][3] = {
  {"backward", "forward", "forward"}, 
  {"backward", "forward", "forward"}, 
  {"forward", "backward", "backward"}, 
  {"forward", "backward", "backward"}
};

int motorSpeed = 100;

int motorSpeeds[4][3] = {
  {motorSpeed, motorSpeed, 0},
  {0, 0, motorSpeed},
  {motorSpeed, motorSpeed, 0},
  {0, 0, motorSpeed}
};

// Time to let marker move for
float time_length = 2000;
int index;

void setup() {
  // Start serial
  Serial.begin(9600);
  AFMS.begin();  // create with the default frequency 1.6KHz
  index = 0;
  
  // Set initial speeds
  motorLeft->setSpeed(70);  
  motorRight->setSpeed(70);
  motorCenter->setSpeed(70);

  // Set initial motor direections
  setMotorDirection(motorLeft, motorCommands[0][0]);
  setMotorDirection(motorRight, motorCommands[0][1]);
  setMotorDirection(motorCenter, motorCommands[0][2]);

  // Run release on motors
  motorLeft->run(RELEASE);
  motorRight->run(RELEASE);
  motorCenter->run(RELEASE);
}

void loop() {
  // Reset index to 0 (only 4 motor commands in list)
  if(index == 4) {
    index = 0;
  }
  
  setMotorDirection(motorLeft, motorCommands[index][0]);
  setMotorDirection(motorRight, motorCommands[index][1]);
  setMotorDirection(motorCenter, motorCommands[index][2]);
  
  // Stop marker if end of design reached
  if(time_length <= 0) {
    setMotorSpeed(motorLeft, 0);
    setMotorSpeed(motorRight, 0);
    setMotorSpeed(motorCenter, 0);
  }

  else {
    // Set speeds if not end
    setMotorSpeed(motorLeft, motorSpeeds[index][0]);
    setMotorSpeed(motorRight, motorSpeeds[index][1]);
    setMotorSpeed(motorCenter, motorSpeeds[index][2]);
  }

  // Decrease time interval by 3 whenever new iteration is started to create spiral effect
  if((index - 2) % 4 == 0) {
    time_length -= 200;
    
  }

  delay(time_length);
  index++;

  Serial.println(time_length);
}


/**
 * Set the motor specified to the direction specified
 * 
 * @param this_motor: the motor to change direction for
 * @param direction: a string representing the direction to set the motor to (forward or backward)
 **/
void setMotorDirection (Adafruit_DCMotor *this_motor, String direction) {
  if (direction == "forward") {
    this_motor->run(FORWARD);
  }
  
  if (direction == "backward") {
    this_motor->run(BACKWARD);
  }
}

/**
 * Set the motor specified to the speed specified
 * 
 * @param this_motor: the motor to change speed for
 * @param speed: an int representing the speed to set the motor to
 **/
void setMotorSpeed (Adafruit_DCMotor *this_motor, int speed) {
  this_motor->setSpeed(speed);
}
