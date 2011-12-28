#==============================================================================
# device_activation.py
# Python script that activates a device based on its serial number.  Device has
# to first be enabled for activation within the timeout period for the Client
# model.  Docs at exosite.com/api.  
#==============================================================================
## Tested with python 2.6.5
##
## Copyright (c) 2010, Exosite LLC
## All rights reserved.
##
## For License see LICENSE file

import socket

HOST = 'm2.exosite.com'
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('POST /provision/activate HTTP/1.1\r\n')
s.send('Host: m2.exosite.com\r\n')
s.send('Content-Type: application/x-www-form-urlencoded\r\n')
s.send('Content-Length: 34\r\n\r\n')
s.send('vendor=newco&model=Example&sn=0001')

data = s.recv(1024)
s.close()
print 'Received: \r\n', repr(data)

