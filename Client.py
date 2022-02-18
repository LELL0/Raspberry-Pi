import socket
import time

port = 4444
server= "192.168.0.100"

print("starting")
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket successfully created")

s.connect((server,port))
print("socket connected")
print("sending Data")
s.sendall(input("write a message: ").encode('utf-8'))
print("Data sent, waiting")
time.sleep(1)
response = str(s.recv(9999999).decode('utf-8'))
s.close()
print("respoonse:",response)