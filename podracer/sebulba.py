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
        mh.getMotor(motor).run(Adafruit_MotorHAT.direction)
        for i in range(10, speed):
            motor.setSpeed(i)
        mh.getMotor(motor).run(Adafruit_MotorHAT.RELEASE)

    time.sleep(distance)

    for motor in range(1, 5):
        mh.getMotor(motor).run(Adafruit_MotorHAT.direction)
        for i in reversed(range(0, speed)):
            motor.setSpeed(i)
        mh.getMotor(motor).run(Adafruit_MotorHAT.RELEASE)


def racer_turn(turn, direction, duration):
    if turn == 'LEFT':
        motor1 = mh.getMotor(1).run(Adafruit_MotorHAT.direction)
        motor2 = mh.getMotor(2).run(Adafruit_MotorHAT.direction)
        motor3 = mh.getMotor(3).run(Adafruit_MotorHAT.direction)
        motor4 = mh.getMotor(4).run(Adafruit_MotorHAT.direction)

        motor2.setSpeed(40)
        motor4.setSpeed(40)
        motor1.setSpeed(5)
        motor3.setSpeed(5)

        time.sleep(duration)

        motor1.run(Adafruit_MotorHAT.RELEASE)
        motor2.run(Adafruit_MotorHAT.RELEASE)
        motor3.run(Adafruit_MotorHAT.RELEASE)
        motor4.run(Adafruit_MotorHAT.RELEASE)

    if turn == 'RIGHT':
        motor1 = mh.getMotor(1).run(Adafruit_MotorHAT.direction)
        motor2 = mh.getMotor(2).run(Adafruit_MotorHAT.direction)
        motor3 = mh.getMotor(3).run(Adafruit_MotorHAT.direction)
        motor4 = mh.getMotor(4).run(Adafruit_MotorHAT.direction)

        motor2.setSpeed(5)
        motor4.setSpeed(5)
        motor1.setSpeed(40)
        motor3.setSpeed(40)

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
