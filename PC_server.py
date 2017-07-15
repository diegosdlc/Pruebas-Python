import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
sys.stderr.write('starting up on %s port %s' % (server_address))
#print('starting up on %s port %s' % (server_address)) #>> sys.stderr
sock.bind(server_address)

while True:
    sys.stderr.write('\nwaiting to receive message')
    #print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)

    sys.stderr.write('received %s bytes from %s' % (len(data), address))
    time.sleep(6)
    #print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    sys.stderr.write(data)
    #print >>sys.stderr, data

    if data:
        sent = sock.sendto(data, address)
        sys.stderr.write('sent %s bytes back to %s' % (sent, address))
        #print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
