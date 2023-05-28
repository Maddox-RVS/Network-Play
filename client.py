import socket
import mouse

HEADERSIZE = 10

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("testPC1", 1234))

while True:
    full_message = ""
    new_message = True

    while True:
        message = sock.recv(16)

        if (new_message):
            # print(f"New message length: {message[:HEADERSIZE]}")
            messageLen = int(message[:HEADERSIZE])
            new_message = False
        
        full_message += message.decode("utf-8")

        if len(full_message)-HEADERSIZE == messageLen:
            # print("Full message recieved!")
            # print(full_message[HEADERSIZE:])

            try:
                xCoord = full_message[full_message.index("=") + 1:full_message.index(",")]
                yCoord = full_message[full_message.index(",") + 4:full_message.index(")")]
                time = full_message[full_message.index(")") + 2:]
                print(f"X: {xCoord}, Y: {yCoord}, Time: {time}")
                mouse.move(int(xCoord), int(yCoord))
            except Exception as e:
                print(e)

            new_message = True
            full_message = ""