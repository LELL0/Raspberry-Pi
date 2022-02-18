import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.0.100",4444))
s.listen(10)
print("Server listener started")

while True:
    conn , addr = s.accept()
    print("Connected by : 25", addr)
    data = conn.recv(10240)
    if data:
        data = data.decode("utf-8")
        print("data",data)

