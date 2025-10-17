import xarm
import time

arm = xarm.Controller('USB')

servo1 = xarm.Servo(1)
servo2 = xarm.Servo(2)
servo3 = xarm.Servo(3)
servo4 = xarm.Servo(4)
servo5 = xarm.Servo(5)
servo6 = xarm.Servo(6)

servosList = [servo1, servo2, servo3, servo4, servo5, servo6]

def turn_off(servosList):
    for servo in servosList:
        arm.servoOff(servo)

def set_positions(servosList, position, wait=True):
    index = 0
    for servo in servosList:
        print(f"Setting position: {position[index]} for servo: {servo.servo_id}")
        arm.setPosition(servo.servo_id, position[index], wait)
        index += 1
        time.sleep(1)
    turn_off(servosList)

def get_position(servo):
    print(arm.getPosition(servo))

def set_state(state_name):
    states = {
        "home": [107, 533, 229, 785, 643, 69],
        "ready_to_grab": [105, 531, 162, 916, 658, 503],
        "ready_to_move": [45, 120, 135, 90, 90, 90]
    }

    if state_name in states:
        print(f"Set to {state_name}")
        set_positions(servosList, states[state_name], False)
        return states[state_name]
    else:
        print("Invalid state")

    return None

if __name__ == "__main__":
    print('Battery voltage in volts:', arm.getBatteryVoltage())
    state_position = set_state("ready_to_grab")




