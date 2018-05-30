import socket
import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
def read():
    file = open("command.txt")
    result = file.read()
    file.close()
    return result
def main():
    s = socket.socket()
    host = "192.168.1.6"
    port = 12345
    s.connect((host, port))
    print(1)
    print(s.recv(1024))
    original = ""
    while True:
        t = str(GPIO.input(12))
        message = read()+" t="+t+" l=0 r=0\n"
        if message != original:
            print(message)
            original = message
        message = message.encode('utf-8')
        s.send(message)
    s.close()
main()
