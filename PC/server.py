import socket, os
def write(text):
    file = open("command.txt","w")
    file.write(text)
    file.close()

def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))
    s.listen(5)
    c, addr = s.accept()
    print("Got connection from "+addr[0]+":"+str(addr[1]))
    c.send(b"Connected")
    words = []
    original = ""
    while True:
        message = c.recv(1).decode("utf-8")
        if message != "\n":
            words.append(message)
        else:
            message = "".join(words)
            words = []
            if message != original and len(message) != 0:
                original = message
                write(message)
                print(message)
main()
