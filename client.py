import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 1234))

message = sock.recv(1024)
print(message.decode("utf-8"))