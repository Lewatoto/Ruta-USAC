

void setup(){
  Serial.begin(115200);
  Serial3.begin(115200);
  pinMode(BLUE_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
}

void loop(){
  digitalWrite(BLUE_LED, HIGH);
  while (Serial3.available()){
    digitalWrite(GREEN_LED, HIGH);
    int lectura = Serial3.read();
    Serial.println(lectura);
  }
}
