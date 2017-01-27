#!/usr/bin/env python
import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def login(remote_conn, username, password):
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    output = remote_conn.write(username + '\n')
    output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
    send_command(remote_conn, password)
    return output

def send_command(remote_conn, cmd):
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def main():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    try:
        remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed-out")

    output = login(remote_conn, username, password)
#    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
#    print output
#    output = remote_conn.write(username + '\n')
#    output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
#    send_command(remote_conn, password)
#    output = remote_conn.write(password + '\n')
#    time.sleep(1)
#    output = remote_conn.read_very_eager()
    print output
    remote_conn.write("terminal length 0" + '\n')
    output = send_command(remote_conn, "show version")
    print output
    remote_conn.close()

if __name__ == "__main__":
    main()
