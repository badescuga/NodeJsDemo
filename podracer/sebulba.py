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
    racer_move('FORWARD', 3)

"""


# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    for motor in range(1, 5):
        mh.getMotor(motor).run(Adafruit_MotorHAT.RELEASE)

# hook SIGINT and stop all motors upon exit
atexit.register(turnOffMotors)

# SEBULBA
def racer_move(direction, distance):
    speed = 160

    motor1 = mh.getMotor(1)
    motor2 = mh.getMotor(2)
    motor3 = mh.getMotor(3)
    motor4 = mh.getMotor(4)

    for i in range(10, speed, 8):
        motor1.setSpeed(i)
        motor2.setSpeed(i)
        motor3.setSpeed(i)
        motor4.setSpeed(i)
        if direction == 'FORWARD':
            for m in range(1, 5):
            	mh.getMotor(m).run(Adafruit_MotorHAT.FORWARD)
	if direction == 'BACKWARD':
            for m in range(1, 5):
            	mh.getMotor(m).run(Adafruit_MotorHAT.BACKWARD)

    time.sleep(distance)

    for i in reversed(range(0, speed, 8)):
        motor1.setSpeed(i)
        motor2.setSpeed(i)
        motor3.setSpeed(i)
        motor4.setSpeed(i)
        if direction == 'FORWARD':
            for m in range(1, 5):
                mh.getMotor(m).run(Adafruit_MotorHAT.FORWARD)
            for m in range(1, 5):
                mh.getMotor(m).run(Adafruit_MotorHAT.RELEASE)
        if direction == 'BACKWARD':
            for m in range(1, 5):
                mh.getMotor(m).run(Adafruit_MotorHAT.BACKWARD)
            for m in range(1, 5):
                mh.getMotor(m).run(Adafruit_MotorHAT.RELEASE)


def racer_turn(direction, duration):
    motor1 = mh.getMotor(1)
    motor2 = mh.getMotor(2)
    motor3 = mh.getMotor(3)
    motor4 = mh.getMotor(4)

    if direction == 'RIGHT':
        motor2.setSpeed(65)
        motor4.setSpeed(90)
        motor1.setSpeed(230)
        motor3.setSpeed(170)
        # Floor it!
        motor2.run(Adafruit_MotorHAT.BACKWARD)
        motor4.run(Adafruit_MotorHAT.FORWARD)
        motor1.run(Adafruit_MotorHAT.FORWARD)
        motor3.run(Adafruit_MotorHAT.FORWARD)
        # Turn for (duration) seconds
        time.sleep(duration)
        # Brake!
        motor1.run(Adafruit_MotorHAT.RELEASE)
        motor2.run(Adafruit_MotorHAT.RELEASE)
        motor3.run(Adafruit_MotorHAT.RELEASE)
        motor4.run(Adafruit_MotorHAT.RELEASE)

    if direction == 'LEFT':
        motor2.setSpeed(170)
        motor4.setSpeed(230)
        motor1.setSpeed(90)
        motor3.setSpeed(30)
        # Floor it!
        motor2.run(Adafruit_MotorHAT.FORWARD)
        motor4.run(Adafruit_MotorHAT.FORWARD)
        motor1.run(Adafruit_MotorHAT.BACKWARD)
        motor3.run(Adafruit_MotorHAT.FORWARD)
        # Turn for (duration) seconds
        time.sleep(duration)
        # Brake!
        motor1.run(Adafruit_MotorHAT.RELEASE)
        motor2.run(Adafruit_MotorHAT.RELEASE)
        motor3.run(Adafruit_MotorHAT.RELEASE)
        motor4.run(Adafruit_MotorHAT.RELEASE)
