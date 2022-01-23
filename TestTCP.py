import socket

target_host = "www.google.com"
target_port = 80

# Create a socket object 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to client
client.connect((target_host,target_port))

# send some data
msg = "GET /HTTP/1.1\r\Host: google.com\r\n\r\n"
client.send(msg.encode())

# rececive some data 
respone = client.recv(4096)

print(respone)
