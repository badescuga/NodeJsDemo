from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit

"""

 Sebulba's Podracer
    Motor layout

   1 O---*---O 2
         |
      [Lights]
         |
         |
       [Pi2]
         |
   3 O---+---O 4



Usage:
    from sebulba import *
    racer_turnleft('FORWARD', 3)

"""


# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    for motor in range(1, 5):
        mh.getMotor(motor).run(Adafruit_MotorHAT.RELEASE)

# hook SIGINT and stop all motors upon exit
atexit.register(turnOffMotors)

def racer_move(distance, speed, direction):
    for motor in range(1, 5):
        for i in range(10, speed):
            m = mh.getMotor(motor)
            m.setSpeed(i)
        if direction == 'FORWARD':
            m.run(Adafruit_MotorHAT.FORWARD)
	if direction == 'BACKWARD':
            m.run(Adafruit_MotorHAT.BACKWARD)

    time.sleep(distance)

    for motor in range(1, 5):
        for i in reversed(range(0, speed, 5)):
            m = mh.getMotor(motor)
            m.setSpeed(i)
        if direction == 'FORWARD':
            m.run(Adafruit_MotorHAT.FORWARD)
            m.run(Adafruit_MotorHAT.RELEASE)
	if direction == 'BACKWARD':
            m.run(Adafruit_MotorHAT.BACKWARD)
            m.run(Adafruit_MotorHAT.RELEASE)


def racer_turn(turn, direction, duration):
    motor1 = mh.getMotor(1)
    motor2 = mh.getMotor(2)
    motor3 = mh.getMotor(3)
    motor4 = mh.getMotor(4)

    if turn == 'RIGHT':
        motor2.setSpeed(65)
        motor4.setSpeed(90)
        motor1.setSpeed(230)
        motor3.setSpeed(170)

        if direction == 'FORWARD':
            motor2.run(Adafruit_MotorHAT.BACKWARD)
            motor4.run(Adafruit_MotorHAT.FORWARD)
            motor1.run(Adafruit_MotorHAT.FORWARD)
            motor3.run(Adafruit_MotorHAT.FORWARD)

        time.sleep(duration)

        motor1.run(Adafruit_MotorHAT.RELEASE)
        motor2.run(Adafruit_MotorHAT.RELEASE)
        motor3.run(Adafruit_MotorHAT.RELEASE)
        motor4.run(Adafruit_MotorHAT.RELEASE)

    if turn == 'LEFT':
        motor2.setSpeed(170)
        motor4.setSpeed(230)
        motor1.setSpeed(90)
        motor3.setSpeed(30)

        if direction == 'FORWARD':
            motor2.run(Adafruit_MotorHAT.FORWARD)
            motor4.run(Adafruit_MotorHAT.FORWARD)
            motor1.run(Adafruit_MotorHAT.BACKWARD)
            motor3.run(Adafruit_MotorHAT.FORWARD)

        time.sleep(duration)

        motor1.run(Adafruit_MotorHAT.RELEASE)
        motor2.run(Adafruit_MotorHAT.RELEASE)
        motor3.run(Adafruit_MotorHAT.RELEASE)
        motor4.run(Adafruit_MotorHAT.RELEASE)


def racer_forward(distance, speed):
    racer_move(distance, speed, 'FORWARD')

def racer_backward(distance, speed):
    racer_move(distance, speed, 'BACKWARD')

def racer_turnleft(direction, duration):
    racer_turn('LEFT', direction, duration)

def racer_turnright(direction, duration):
    racer_turn('RIGHT', direction, duration)
