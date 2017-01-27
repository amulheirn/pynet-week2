#!/usr/bin/env python

# script to get name of router and description
# using snmp.

# Requires snmp_helper.py from Kirk

from  snmp_helper import snmp_get_oid, snmp_extract
import pysnmp

devices=['184.105.247.70','184.105.247.71']
username = 'pyclass'
password = '88newclass'
snmp_port = 161
community = 'galileo'

for d in devices:
    device=(d,community,snmp_port)
    print device
    snmp_data=snmp_get_oid(device,oid='.1.3.6.1.2.1.1.1.0',display_errors=True)
#    print snmp_data
    snmp_readable=snmp_extract(snmp_data)
    print snmp_readable
    snmp_ints=snmp_get_oid(device,oid='1.3.6.1.2.1.2.2.1.2.1',display_errors=True)
    snmp_readable=snmp_extract(snmp_ints)
    print snmp_readable,
    snmp_int_status=snmp_get_oid(device,oid='1.3.6.1.2.1.2.2.1.7.1',display_errors=True)
    snmp_readable=snmp_extract(snmp_int_status)
    if int(snmp_readable) == 1:
        print ' \033[94m [UP] \033[0m'
    else:
        print ' \033[91m [DOWN] \033[0m'
