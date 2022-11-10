
String curr_line;
int total_length;


void help() {
  Serial.println("Mehendi Bot");
}

void setup() {
  Serial.begin(9600);
  help();
  // set_feedrate(200);
  ready();
}

void ready() {
  total_length = 0;
  curr_line = "";
  Serial.print(F("> "));
}

void moveLine(String new_x, String new_y) {
  // Move to new x and new y
  float x_pos = new_x.toFloat();
  float y_pos = new_y.toFloat();

  float dx=newx-px; // distance to move (delta)
  float dy=newy-py;
  int dirx=dx > 0?1:-1; // direction to move
  int diry=dy > 0?1:-1;
  dx=abs(dx); // absolute delta
  dy=abs(dy);  
  Serial.print("Move to X: ");
  Serial.print(new_x);
  Serial.print(" Y: ");
  Serial.println(new_y);
}

void loop() {
  if (Serial.available()) {
    char this_char = Serial.read();
    Serial.print("Found Character: ");
    Serial.println(this_char);

    // Get next character from Serial
    curr_line += this_char;
    if (this_char == '\n') {
      Serial.print(F("\r\n"));
      runCommand();
      curr_line = "";
    }
  }
}

void runCommand() {
  // Run command given
  int G_command = (curr_line.substring(curr_line.indexOf("G") + 1, curr_line.indexOf("G") + 3)).toInt();
  Serial.println(G_command);

  if (G_command != 0) {
    // Run G commands

    if (G_command == 1) {
      
      // If 01, move in a line to the position X, Y given at speed F given
      int F_speed_index = curr_line.indexOf("F");
      // set_feedrate(curr_line[F_speed_index]);
      int X_index = curr_line.indexOf("X");
      int X_end = X_index + curr_line.substring(X_index).indexOf(" ");
      int Y_index = curr_line.indexOf("Y");

      moveLine(curr_line.substring(X_index + 1, X_end + 1), curr_line.substring(Y_index + 1));  
    }

  //   if G_command == "2" {
  //     // If 02, move in circular arc to position X, Y given with radius R given at speed F given
  //     int F_speed = curr_line[strchr(curr_line, "F")];
  //     set_feedrate(F_speed]);
      
  //     int radius = curr_line[strchr(curr_line, "R")];
  //   }

  //   if G_command == "3" {
  //     // If 03, move in circular arc to position X, Y, given I, J as relative position at speed F
  //     int F_speed = curr_line[strchr(curr_line, "F")];
  //     set_feedrate(F_speed]);

      
  //   }

    if (G_command == 4) {
      // If 04, delay for the time P given
      int delay_period = curr_line.substring(curr_line.indexOf("P") + 1).toInt();
      delay(delay_period * 1000);
      Serial.println("Done");
    }
    
  }
  else {
    Serial.println("No G");
  }
}