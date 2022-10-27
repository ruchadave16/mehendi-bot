#include <Adafruit_MotorShield.h>

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *motorLeft = AFMS.getMotor(3);
Adafruit_DCMotor *motorRight = AFMS.getMotor(2);
Adafruit_DCMotor *motorCenter = AFMS.getMotor(1);

motorDirections = [] // motorLeft, motorRight, motorCenter

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  if (!AFMS.begin()) {
    Serial.println("Check wiring");
    while(1);
  }

  motorLeft->setSpeed(20);  
  motorRight->setSpeed(20);
  motorCenter->setSpeed(20);
  
  motorCommands = {{"forward", "forward", "forward"}, {"forward", "forward", "forward"}, {"backward", "backward", "backward"}, {"backward", "backward", "backward"}};
  int index = 0;

  setMotorDirection(motorLeft, motorCommands[0][0]);
  setMotorDirection(motorRight, motorCommands[0][1]);
  setMotorDirection(motorCenter, motorCommands[0][2]);

  motorLeft->run(RELEASE);
  motorRight->run(RELEASE);
  motorCenter->run(RELEASE);
}

void loop() {
  // put your main code here, to run repeatedly:
  setMotorDirection(motorLeft, motorCommands[i][0]);
  setMotorDirection(motorRight, motorCommands[i][1]);
  setMotorDirection(motorCenter, motorCommands[i][2]);

  delay(20);
  
  i++;
}

void setMotorDirection (this_motor, direction) {
  if direction == "forward" {
    this_motor->run(FORWARD);
  }
  if direction == "backward" {
    this_motor->run(BACKWARD);
  }
}


