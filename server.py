import socket
import pyautogui
import time

HEADERSIZE = 10

lastCoordinates = (0, 0)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Hostname: " + socket.gethostname())
sock.bind((socket.gethostname(), 1234))
sock.listen(5)

while True:
    clientsocket, address = sock.accept()
    print(f"Connection from {address} has been established!\n")

    message = "Welcome to the server!"
    message = f"{len(message):<{HEADERSIZE}}" + message

    clientsocket.send(bytes(message, "utf-8"))

    while True:
        time.sleep(0.01)
        message = str(pyautogui.position())
        xCoord = message[message.index("=") + 1:message.index(",")]
        yCoord = message[message.index(",") + 4:-1]

        if ((xCoord, yCoord) != lastCoordinates):
            message = f"{len(message):<{HEADERSIZE}}" + message
            clientsocket.send(bytes(message, "utf-8"))
            lastCoordinates = (xCoord, yCoord)