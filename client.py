import socket

HEADERSIZE = 10

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 1234))

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
            print(full_message[HEADERSIZE:])
            new_message = True
            full_message = ""