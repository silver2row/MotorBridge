import MotorBridgeI
import time

MotorName        = 1
#MotorName        = 2 Only one motor attached for now, i.e. testing, testing, 1, 2, 3.
ClockWise        = 1
CounterClockWise = 2
PwmDuty          = 90
Frequency        = 1000

if __name__=="__main__":

    motor = MotorBridgeI.MotorBridgeCape()
    motor.DCMotorInit(1, 1000) # Initiate the motor
    #motor.DCMotorInit(2, 1000) just running one motor and not two!
    print("Getting Motors Ready!")
    time.sleep(4)

    for i in range(1, 3):
        motor.DCMotorMove(1, 2, 90) # 1 = Motor Number, 2 = CCW, 90 = PWM_duty.
        #motor.DCMotorMove(2, 1, 90) one motor, not two
        print("Making Things Happen!", 1)
        time.sleep(3)

    #motor = MotorBridgeI.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    #motor.DCMotorInit(2, 1000)
    for i in range(1, 3):
        motor.DCMotorMove(1, 1, 90)
        #motor.DCMotorMove(2, 2, 90)
        time.sleep(3)
    print("Making Things Happen Again!")

    motor = MotorBridgeI.MotorBridgeCape()
    motor.DCMotorInit(1, 0)
    for i in range(0, 1):
        motor.DCMotorMove(1, 2, 0)
        time.sleep(10)


