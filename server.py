# -*- coding: utf-8 -*-
import socket
import threading
import struct
from datetime import datetime
# AF_INET = ipv4
# AF_INET6 = ipv6
# SOCK_STREAM = tcp
# SOCK_DGRAM = udp
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((socket.gethostname(), 1234, ))

sock.listen(5)
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
def handle_client(client_socket,addr):
  while True:  
    request = recv_msg(client_socket)
    now = datetime.now()
    dt = now.strftime("%Y/%m/%d %H:%M:%S")
    print("[%s] [%s] Received: %s" % (dt,addr[0], request.decode("utf-8")))

        
def handle_send():
  while True:
    #content = raw_input()
    #sock.send(content);
    #阻塞在這裡，等待接收客戶端的資料
    client_socket,addr = sock.accept()
    print("[*] Accept connection from:%s:%s" % (addr[0],addr[1]))
    #建立一個執行緒
    client_handler = threading.Thread(target=handle_client,args=(client_socket,addr,))
    client_handler.start()
    
            
send_handler = threading.Thread(target=handle_send,args=())
send_handler.start()

  
