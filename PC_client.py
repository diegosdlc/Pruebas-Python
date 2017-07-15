import socket
import sys
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'This is the message.  It will be repeated.'

try:

    # Send data
    sys.stderr.write('sending "%s"' % message)
    #print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message.encode('utf-8'), server_address)
    time.sleep(6)

    # Receive response
    sys.stderr.write("waiting to receive")
    #print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    sys.stderr.write('received "%s"' % data)
    #print >>sys.stderr, 'received "%s"' % data

finally:
    sys.stderr.write('closing socket')
    #print >>sys.stderr, 'closing socket'
    sock.close()
