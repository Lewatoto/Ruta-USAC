int motor1 = PC_4;
int motor2 = PC_5;
int motor3 = PD_6;
int motor4 = PD_7;
int lectura = 0;

void setup(){
  Serial.begin(9600);
  Serial3.begin(9600);  
  pinMode(RED_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(motor1, OUTPUT);
  pinMode(motor2, OUTPUT);
  pinMode(motor3, OUTPUT);
  pinMode(motor4, OUTPUT);
}

void loop(){
  while (Serial3.available() > 0){
    lectura = Serial3.read();
    Serial.println(lectura);
    if (lectura == 'a'){ //Derecha (Rojo)
      digitalWrite(motor1, HIGH);
      digitalWrite(motor2, LOW);
      digitalWrite(motor3, LOW);
      digitalWrite(motor4, LOW);
      digitalWrite(RED_LED, HIGH);
      digitalWrite(BLUE_LED, LOW);
      digitalWrite(GREEN_LED, LOW);
    }else if (lectura == 'b'){  //Izquierda (Azul)
      digitalWrite(motor1, LOW);
      digitalWrite(motor2, LOW);
      digitalWrite(motor3, HIGH);
      digitalWrite(motor4, LOW);
      digitalWrite(RED_LED, LOW);
      digitalWrite(BLUE_LED, HIGH);
      digitalWrite(GREEN_LED, LOW);
    }else if (lectura == 'c'){  //Adelante (Verde)
      digitalWrite(motor1, HIGH);
      digitalWrite(motor2, LOW);
      digitalWrite(motor3, HIGH);
      digitalWrite(motor4, LOW);
      digitalWrite(RED_LED, LOW);
      digitalWrite(BLUE_LED, LOW);
      digitalWrite(GREEN_LED, HIGH);
    }else if (lectura == 'd'){  //Atras (Amarillo)
      digitalWrite(motor1, LOW);
      digitalWrite(motor2, HIGH);
      digitalWrite(motor3, LOW);
      digitalWrite(motor4, HIGH);
      digitalWrite(RED_LED, HIGH);
      digitalWrite(BLUE_LED, LOW);
      digitalWrite(GREEN_LED, HIGH);
    }else{
      digitalWrite(motor1, LOW);
      digitalWrite(motor2, LOW);
      digitalWrite(motor3, LOW);
      digitalWrite(motor4, LOW);
      digitalWrite(RED_LED, LOW);
      digitalWrite(BLUE_LED, LOW);
      digitalWrite(GREEN_LED, LOW);
    }
  }
}
