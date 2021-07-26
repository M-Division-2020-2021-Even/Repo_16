// C++ code
//
#include <Servo.h>

Servo servo;
int servoPin = 11;
int degrees = 60;
int forcePin = A0;
int forceValue = 0;

void setup()
{
    pinMode(forcePin, INPUT);
    pinMode(servoPin, OUTPUT);
    servo.attach(servoPin);
    Serial.begin(9600);
}

void loop()
{
    forceValue = analogRead(forcePin);
    Serial.println(forceValue);
    if (forceValue < 1023)
    {
        servo.write(degrees);
    }
    else
    {
        servo.write(0);
    }
}