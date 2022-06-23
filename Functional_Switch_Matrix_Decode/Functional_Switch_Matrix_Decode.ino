void setup() {
  Serial.begin(9600);
  pinMode(7, OUTPUT);
  digitalWrite(7, 0);
}

void readKeypad(String printVal, int inputPin, int outputPin){
//  Debounce
  pinMode(inputPin, INPUT_PULLUP);
  pinMode(outputPin, OUTPUT);
  digitalWrite(outputPin, 0);
  if(digitalRead(inputPin) == 0)
    Serial.print(printVal);

//    Cleanup
  pinMode(inputPin, INPUT);
  pinMode(outputPin, INPUT);

}


void loop() {
  
  readKeypad("#", 5, 8);
  readKeypad("6", 5, 3);
  readKeypad("9", 5, 2);
  readKeypad("0", 6, 8);
  readKeypad("*", 7, 8);
  readKeypad("7", 7, 2);
  readKeypad("4", 7, 3);
  readKeypad("1", 7, 4);
  readKeypad("2", 6, 4);
  readKeypad("3", 4, 5);
  readKeypad("5", 3, 6);
  readKeypad("8", 2, 6);
  
}
