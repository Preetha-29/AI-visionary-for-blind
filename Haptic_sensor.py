import RPi.GPIO as GPIO
import time

# Set the GPIO mode and specify the servo control pin
servo_pin = 18  # Change this to the GPIO pin you are using
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance with a frequency of 50Hz
pwm = GPIO.PWM(servo_pin, 50)

def turn_left():
    pwm.start(2.5)  # Duty cycle for 90 degrees left position
    time.sleep(1)   # Add a delay to allow the servo to reach the left position

def turn_right():
    pwm.start(12.5)  # Duty cycle for 90 degrees right position
    time.sleep(1)    # Add a delay to allow the servo to reach the right position

def turn_center():
    pwm.start(7.5)   # Duty cycle for the center position
    time.sleep(1)    # Add a delay to allow the servo to reach the center position

try:
    while True:
        user_input = input("Enter 0 for left, 1 for right, or 2 to exit: ")

        if user_input == '0':
            for _ in range(5):
                turn_left()
                turn_center()
        elif user_input == '1':
            for _ in range(5):
                turn_right()
                turn_center()
        elif user_input == '2':
            break  # Exit the loop if '2' is pressed
        else:
            print("Invalid input. Please enter 0, 1, or 2.")

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
