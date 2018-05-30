import time
import serial
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def write(words):
    file = open("command.txt","w")
    file.write(words)
    file.close()
def main():      
    ser = serial.Serial(port='/dev/ttyS0', baudrate = 9600, timeout=1)
    words = []
    while True:
        x = ser.read(1).decode("utf-8")
        #print(x)
        if x != "\n":
            words.append(x)
        else:
            t = GPIO.input(12)
            l = GPIO.input(16)
            message = "".join(words)+" t="+str(t)+" l="+str(l)
            words = []
            write(message)
            print(message)

main()
