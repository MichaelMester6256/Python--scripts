import socket

target_host = www.google.com
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK.STREAM)


client.conect((target_host,target_port))


client.send ("GET /HTTP/1.1\r\nHost :google.com\r\n\r\n")

responce = client.recv(4096)

print responce