

String curr_line;
int total_length;

void setup() {
  Serial.begin(9600);
  help();
  set_feedrate(200);
  ready();
}

void loop() {
  if Serial.available() {
    char this_char = Serial.read();
    Serial.print(c);

    // Get next character from Serial
    curr_line += c;
    if c == '\n':
      Serial.print(F("\r\n"));
      curr_line += "0";
      runCommand();
  }
}

void runCommand() {
  // Run command given
  int G_command = curr_line[strchr(curr_line, "G") + 1 : strchr(curr_line, "G") + 3];

  if G_index != -1 {
    // Run G commands

    if G_command == "1" {
      // If 01, move in a line to the position X, Y given at speed F given
      int F_speed_index = strchr(curr_line, "F");
      set_feedrate(curr_line[F_speed]);
      moveLine(curr_line[strchr(curr_line, "X")], curr_line[strchr(curr_line, "Y")]);  
    }

    if G_command == "2" {
      // If 02, move in circular arc to position X, Y given with radius R given at speed F given
      int F_speed = curr_line[strchr(curr_line, "F")];
      set_feedrate(F_speed]);
      
      int radius = curr_line[strchr(curr_line, "R")];
    }

    if G_command == "3" {
      // If 03, move in circular arc to position X, Y, given I, J as relative position at speed F
      int F_speed = curr_line[strchr(curr_line, "F")];
      set_feedrate(F_speed]);

      
    }

    if curr_line[G_index + 1 : G_index + 3] == "04" {
      // If 04, delay for the time P given
      int delay_period = curr_line[strchr(curr_line, "P")];
      delay(delay_period * 1000);
    }
    
  }
}

void moveLine(new_x, new_y) {
  // Move to new x and new y
}

void help() {
  Serial.println("Mehendi Bot");
}

void ready() {
  total_length = 0;
  curr_line = "";
  Serial.print(F("> "));
}