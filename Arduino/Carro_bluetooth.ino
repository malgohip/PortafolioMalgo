#include <SoftwareSerial.h>
SoftwareSerial bluetooth (A0,A1);
const int motor_l_p = 0;
const int motor_l_n = 1;
const int motor_r_p = 2;
const int motor_r_n = 3;
const int frontal_light = 4;
const int back_light = 5;
const int right_directional = 6;
const int left_directional = 7;
char dato;
void setup() {
  // put your setup code here, to run once:
  pinMode(motor_l_p, OUTPUT);
  pinMode(motor_l_n, OUTPUT);
  pinMode(motor_r_p, OUTPUT);
  pinMode(motor_r_n, OUTPUT);
  pinMode(frontal_light, OUTPUT);
  pinMode(back_light, OUTPUT);
  pinMode(right_directional, OUTPUT);
  pinMode(left_directional, OUTPUT);
  bluetooth.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  dato=bluetooth.read();
  delay(500);
  if(dato=='N')//parado
  {
    digitalWrite(motor_l_p, LOW);
    digitalWrite(motor_l_n, LOW);
    digitalWrite(motor_r_p, LOW);
    digitalWrite(motor_r_n, LOW);
    digitalWrite(frontal_light, LOW);
    digitalWrite(back_light, LOW);
    digitalWrite(right_directional, LOW);
    digitalWrite(left_directional, LOW);
  }
 if(dato=='D')//adelante
  {
    digitalWrite(motor_l_p, HIGH);
    digitalWrite(motor_l_n, LOW);
    digitalWrite(motor_r_p, HIGH);
    digitalWrite(motor_r_n, LOW);
  }
  if(dato=='d')//derecha
  {
    digitalWrite(motor_l_p,HIGH);
    digitalWrite(motor_l_n,LOW);
    digitalWrite(motor_r_p,LOW);
    digitalWrite(motor_r_n,HIGH);
  }
  if(dato=='A')//atras
  {
    digitalWrite(motor_l_p,LOW);
    digitalWrite(motor_l_n,HIGH);
    digitalWrite(motor_r_p,LOW);
    digitalWrite(motor_r_n,HIGH);
    digitalWrite(back_light, HIGH);
  }
  if(dato=='i')//izquierda
  {
    digitalWrite(motor_l_p,LOW);
    digitalWrite(motor_l_n,HIGH);
    digitalWrite(motor_r_p,HIGH);
    digitalWrite(motor_r_n,LOW);
  }
  while(dato=='L')//luces
  {
    digitalWrite(frontal_light, HIGH);
    digitalWrite(back_light, HIGH);
  }
  while(dato=='l')//direccionales_izquierdas
  {
    digitalWrite(left_directional, HIGH);
    delay(500);
    digitalWrite(left_directional, LOW);
    delay(500);
  }
  while(dato=='r')//direccionales_derechas
  {
    digitalWrite(right_directional, HIGH);
    delay(500);
    digitalWrite(right_directional, LOW);
    delay(500);
  }
}