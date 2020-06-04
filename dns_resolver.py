#!/usr/bin/env python
import socket
import sys

host = sys.argv[1]
get_host = socket.gethostbyname(host)

print('{}  ->  {}'.format(host, get_host))
