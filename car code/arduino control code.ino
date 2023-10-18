#include<Servo.h>

Servo duoji1;
Servo duoji2;


// 定义电机引脚
int ENA = 3;
int motorPin1 = 4;  // 连接到电机的引脚1
int motorPin2 = 5;  // 连接到电机的引脚2
int motorPin3 = 6;  // 连接到电机的引脚3
int motorPin4 = 7;  // 连接到电机的引脚4
int ENB = 8;

int trigPin1=39;//前
int echoPin1=38;

int trigPin2=30;//left
int echoPin2=31;

int trigPin3=53;
int echoPin3=52;//right

int trigPin4=26;
int echoPin4=28;//up

int pin=44;

 

long duration,cm1,right,left,cm4;

const int vibrationPin = 2;


void setup() {
  // 配置引脚模式
  Serial.begin(9600);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  pinMode(trigPin1,OUTPUT);  
  pinMode(trigPin2,OUTPUT);
  pinMode(trigPin3,OUTPUT);
  pinMode(trigPin4,OUTPUT);
  pinMode(13,OUTPUT);

  pinMode(vibrationPin, INPUT);

  duoji1.attach(48);
  duoji2.attach(50);
}

void loop() {
digitalWrite(13,LOW);
digitalWrite(trigPin1,LOW);
delayMicroseconds(20000);
digitalWrite(trigPin1,HIGH);
delayMicroseconds(40000);
digitalWrite(trigPin1,LOW);
duration=pulseIn(echoPin1,HIGH);
cm1=(duration/2)/29.1;
Serial.print(cm1);
Serial.print("前：\t");

digitalWrite(trigPin2,LOW);
delayMicroseconds(20000);
digitalWrite(trigPin2,HIGH);
delayMicroseconds(40000);
digitalWrite(trigPin2,LOW);
duration=pulseIn(echoPin2,HIGH);
left=(duration/2)/29.1;
Serial.print(right);
Serial.print("右：\t");//左

digitalWrite(trigPin3,LOW);
delayMicroseconds(20000);
digitalWrite(trigPin3,HIGH);
delayMicroseconds(40000);
digitalWrite(trigPin3,LOW);
duration=pulseIn(echoPin3,HIGH);
right=(duration/2)/29.1;
Serial.print(left);
Serial.print("左：\t");//右

digitalWrite(trigPin4,LOW);
delayMicroseconds(20000);
digitalWrite(trigPin4,HIGH);
delayMicroseconds(40000);
digitalWrite(trigPin4,LOW);
duration=pulseIn(echoPin4,HIGH);
cm4=(duration/2)/29.1;
Serial.print(cm4);
Serial.print("上：\t");//上



if(cm1<=80 && cm4 <= 80 && (cm4-cm1)>=13){
  digitalWrite(13,HIGH);
  setSpeed(0,0);
  delay(5000);
  if(left > right){
  setSpeed(-90, 90);
  delay(1500);
  }else if(left < right) {
  setSpeed(90, -90);
  delay(1500);
  }
}
if(cm1>27){
  
  setSpeed(70, 70);
  delay(250);
  if(left<right && left<35 && right<35){
    setSpeed(95, -95);
  }else if(left>right && left<35 && right<35){
    setSpeed(-95, 95);
  }  
}
else if(cm1<27){
  setSpeed(70,70);
  delay(100);
  if(right-left>20){
  setSpeed(100, -100);
  delay(900);
  setSpeed(70,70);
  delay(300);
  }else if(left-right>20){
  setSpeed(-95, 95);
  delay(900);
  setSpeed(70,70);
  delay(300);
  }else if(cm1<20 &&left <20 && right <20){
  if(left > right){
  setSpeed(-100, 100);
  delay(1500);
  }else if(left < right) {
   setSpeed(100, -100);
  delay(1500);

  }
  }
}

  Serial.println();
duoji2.write(0);
duoji1.write(90);

  // for(int i=0;i<180;i++)
  // {
  //   duoji2.write(i);
   
  //   delay(10);
  // }
  // for(int i=179;i>=0;i--)
  // {
  //   duoji2.write(i);
   
  //   delay(10);
  // }
  // for(int i=0;i<90;i++)
  // {
   
  //   duoji1.write(i);
  //   delay(8);
  // }
  // for(int i=89;i>=0;i--)
  // {
   
  //   duoji1.write(i);
  //   delay(8);
  // }

}

void setSpeed(int leftSpeed, int rightSpeed){
  if(leftSpeed >= 0){
    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, LOW);
  }else {
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
    leftSpeed= -leftSpeed;
  }
    analogWrite(ENA, leftSpeed);
  if(rightSpeed >= 0){
    digitalWrite(motorPin3, HIGH);
    digitalWrite(motorPin4, LOW);
  }else {
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, HIGH);
    rightSpeed= -rightSpeed;
  }
    analogWrite(ENB, rightSpeed);
}
