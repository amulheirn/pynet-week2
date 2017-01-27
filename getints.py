#!/usr/bin/env python


import telnetlib
import time

IPADDR = '184.105.247.70'
PORT = 23
TIMEOUT = 5
username = 'pyclass'
password = '88newclass'


def send_command(connection, cmd):
    output = connection.write(cmd + '\n')
    time.sleep(1)
    return connection.read_very_eager()

def login(connection,username,password):
    connection.read_until('sername:', TIMEOUT)
    connection.write(username + '\n')
    connection.read_until('assword:', TIMEOUT)
    connection.write(password + '\n')
    time.sleep(1)

def disable_paging(connection, command='set term len 0'):
    return send_command(connection, command)



def telnet_connect(IPADDR):
    try:
        return telnetlib.Telnet(IPADDR,PORT,TIMEOUT)
    except socket.timeout:
        sys.exit('Connection timed out')


connection=telnet_connect(IPADDR)

login(connection,username,password)

output = send_command(connection, 'show ip int brief')

print output

connection.close()

