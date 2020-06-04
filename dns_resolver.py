#!/usr/bin/env python
import socket
import sys

if len(sys.argv) <= 1:
    print('USE: {} target.com'.format(sys.argv[0]))
    print('OUTPUT: target.com  ->  192.168.0.1')
else:
    host = sys.argv[1]
    get_host = socket.gethostbyname(host)

    print('{}  ->  {}'.format(host, get_host))
