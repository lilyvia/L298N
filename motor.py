#!/usr/bin/env python

import RPi.GPIO as GPIO


class directio(object):
    def __init__(self, IN1, IN2, IN3, IN4, ENA, ENB, MODE):
        self.IN1 = IN1
        self.IN2 = IN2
        self.IN3 = IN3
        self.IN4 = IN4
        self.ENA = ENA
        self.ENB = ENB
        self.MODE = MODE
        GPIO.setmode(self.MODE)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        global PA
        global PB
        PA = GPIO.PWM(self.ENA, 1000)
        PB = GPIO.PWM(self.ENB, 1000)
        PA.start(100)
        PB.start(100)

    def stop(self, DCA=100, DCB=100):
        PA.ChangeDutyCycle(DCA)
        PB.ChangeDutyCycle(DCB)
        GPIO.output(self.IN1, 1)
        GPIO.output(self.IN2, 1)
        GPIO.output(self.IN3, 1)
        GPIO.output(self.IN4, 1)

    def turn_right(self, DCA=100, DCB=100):
        PA.ChangeDutyCycle(DCA)
        PB.ChangeDutyCycle(DCB)
        GPIO.output(self.IN1, 1)
        GPIO.output(self.IN2, 0)
        GPIO.output(self.IN3, 1)
        GPIO.output(self.IN4, 0)

    def turn_left(self, DCA=100, DCB=100):
        PA.ChangeDutyCycle(DCA)
        PB.ChangeDutyCycle(DCB)
        GPIO.output(self.IN1, 0)
        GPIO.output(self.IN2, 1)
        GPIO.output(self.IN3, 0)
        GPIO.output(self.IN4, 1)

    def forward(self, DCA=100, DCB=100):
        PA.ChangeDutyCycle(DCA)
        PB.ChangeDutyCycle(DCB)
        GPIO.output(self.IN1, 1)
        GPIO.output(self.IN2, 0)
        GPIO.output(self.IN3, 0)
        GPIO.output(self.IN4, 1)

    def backward(self, DCA=100, DCB=100):
        PA.ChangeDutyCycle(DCA)
        PB.ChangeDutyCycle(DCB)
        GPIO.output(self.IN1, 0)
        GPIO.output(self.IN2, 1)
        GPIO.output(self.IN3, 1)
        GPIO.output(self.IN4, 0)


L_IN1_ =
L_IN2_ =
L_IN3_ =
L_IN4_ =
L_ENA_ =
L_ENB_ =
R_IN1_ =
R_IN2_ =
R_IN3_ =
R_IN4_ =
R_ENA_ =
R_ENB_ =
MODE_ =
L_MOTOR = directio(L_IN1_, L_IN2_, L_IN3_, L_IN4_, L_ENA_, L_ENB_, MODE_)
R_MOTOR = directio(R_IN1_, R_IN2_, R_IN3_, R_IN4_, R_ENA_, R_ENB_, MODE_)
