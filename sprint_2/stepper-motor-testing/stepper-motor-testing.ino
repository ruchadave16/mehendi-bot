/**
    PIE Final Project Sprint 2
    Name: Mehendi Bot
    Purpose: Guide a marker into a square spiral using 3 stepper motors

    @author: Cherry Pham
    @version: 1.0 11/14/2022
 **/

// Define pin connections & motor's steps per revolution
const int motorCenter_dir = 2;
const int motorCenter_step = 3;
const int motorLeft_dir = 4;
const int motorLeft_step = 5;
const int motorRight_dir = 6;
const int motorRight_step = 7;
const int stepsPerRev = 24000;


// Set motor commands to loop over
// motorLeft, motorRight, motorCenter
String motorCommands[4][3] = {
  {"LOW", "HIGH", "HIGH"},
  {"LOW", "HIGH", "HIGH"},
  {"HIGH", "LOW", "LOW"},
  {"HIGH", "LOW", "LOW"}
};

void setup()
{
  // Start serial
  Serial.begin(9600);

  // Declare pins as Outputs
  pinMode(motorCenter_step, OUTPUT);
  pinMode(motorCenter_dir, OUTPUT);
  pinMode(motorLeft_step, OUTPUT);
  pinMode(motorLeft_dir, OUTPUT);
  pinMode(motorRight_step, OUTPUT);
  pinMode(motorRight_dir, OUTPUT);
}
// HIGH - CLOCKWISE - toward motor
// LOW - ANTICLOCKWISE - away fr motor
void loop()
{
  digitalWrite(motorCenter_dir, LOW);
  digitalWrite(motorLeft_dir, LOW);
  digitalWrite(motorRight_dir, LOW);
  // Spin motor slowly
  for(int x = 0; x < stepsPerRev; x++)
  {
    digitalWrite(motorLeft_step, HIGH);
    digitalWrite(motorRight_step, HIGH);
    digitalWrite(motorCenter_step, HIGH);
    delayMicroseconds(1000);
    digitalWrite(motorCenter_step, LOW);
    digitalWrite(motorLeft_step, LOW);
    digitalWrite(motorRight_step, LOW);
    delayMicroseconds(1000);
  }
  delay(1000); 
}
