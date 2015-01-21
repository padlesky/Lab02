import socket
import sys

try:
    import thread
except ImportError:
    import _thread as thread

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

s.listen(5)
print 'Socket now listenin'

def clientthread(conn):
    conn.send('Welcome to the server. Type something and hit enter\n')

    while True:

        data = conn.recv(1024)
        reply = 'Hello ' + data
        if not data:
            break

        conn.sendall(reply)

    conn.close()

while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    thread.start_new_thread(clientthread ,(conn,))

s.close()
