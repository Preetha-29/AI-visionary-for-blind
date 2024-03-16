import RPi.GPIO as GPIO
from time import sleep
from mpu6050 import mpu6050
import time

mpu = mpu6050(0x68)

led= 11
but = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(but,GPIO.IN,pull_up_down=GPIO.PUD_UP)


def buzz():
        button_state=GPIO.input(but)
        if button_state==False:
            GPIO.output(led,0)
        else:
            GPIO.output(led,1)
        sleep(1)
def gyro():
    print("Temp : "+str(mpu.get_temp()))
    print()

    accel_data = mpu.get_accel_data()
    print("Acc X : "+str(accel_data['x']))
    print("Acc Y : "+str(accel_data['y']))
    print("Acc Z : "+str(accel_data['z']))
    print()

    gyro_data = mpu.get_gyro_data()
    print("Gyro X : "+str(gyro_data['x']))
    print("Gyro Y : "+str(gyro_data['y']))
    print("Gyro Z : "+str(gyro_data['z']))
    print()
    print("-------------------------------")
    time.sleep(1)
    if(gyro_data['x'] >= 100 or gyro_data['y'] >= 100 or gyro_data['z'] >= 235 or gyro_data['x'] <= -235 or gyro_data['y'] <= -235 or gyro_data['z'] <= -235):
        buzz()
    if(accel_data['x'] <= -18 or accel_data['y'] <= -18 or accel_data['z'] <= -18 or accel_data['x'] >= 18 or accel_data['y'] >= 18 or accel_data['z'] >= 18):
        buzz()
try:
    while True:
        gyro()

except KeyboardInterrupt:
    pass

#buzz()
finally:
    GPIO.cleanup()



