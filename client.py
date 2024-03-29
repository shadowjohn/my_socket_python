# -*- coding: utf-8 -*-
import socket
import struct
def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

cS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cS.connect((socket.gethostname(), 1234, ))
while True:
  
  
  
  #data = "Hello World"
  
  #b_data = data.encode("utf-8")
  
  #cS.send(b_data)
  
  #data = cS.recv(1024)
  
  #s_data = data.decode("utf-8")
  
  #print("Recevice: ", s_data)


  #data = cS.recv(1024)
  #s_data = data.decode("utf-8")
  #print("Recevice: ", s_data + "\n")  
  data = input("Input: ")
  b_data = data.encode("utf-8")
  send_msg(cS,b_data)
  
  #data = cS.recv(1024)  
cS.close()  