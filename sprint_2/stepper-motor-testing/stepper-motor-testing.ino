/**
    PIE Final Project Sprint 2
    Name: Mehendi Bot
    Purpose: Guide a marker into a square spiral using 3 stepper motors

    @author: Cherry Pham
    @version: 1.0 11/14/2022
 **/

// Define pin connections & motor's steps per revolution
const int motorLeft_dir = 5;
const int motorLeft_step = 6;
const int motorRight_dir = 3;
const int motorRight_step = 4;
const int stepsPerRev = 200;


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
  pinMode(motorLeft_step, OUTPUT);
  pinMode(motorLeft_dir, OUTPUT);
  pinMode(motorRight_step, OUTPUT);
  pinMode(motorRight_dir, OUTPUT);
}

void loop()
{
  digitalWrite(motorLeft_dir, HIGH);
  digitalWrite(motorRight_dir, HIGH);
  // Spin motor slowly
  for(int x = 0; x < stepsPerRev; x++)
  {
    digitalWrite(motorLeft_step, HIGH);
    digitalWrite(motorRight_step, HIGH);
    delayMicroseconds(1000);
    digitalWrite(motorLeft_step, LOW);
    digitalWrite(motorRight_step, LOW);
    delayMicroseconds(1000);
  }
  delay(1000); 
}
