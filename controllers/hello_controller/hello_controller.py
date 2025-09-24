# hello_controller.py
from controller import Robot

robot = Robot()
TIME_STEP = 64

while robot.step(TIME_STEP) != -1:
    print("🤖 Robot is running...")
