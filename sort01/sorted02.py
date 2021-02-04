#!/usr/bin/python3

iplist = ['10.8.2.1', '1.1.1.1', '255.255.255.255', '10.1.2.1', '10.2.1.2', \
'10.2.3.2', '10.7.2.1', '192.168.23.1', '192.168.66.1', '10.42.2.1', \
'10.11.10.2', '10.25.32.2', '10.27.21.1', '192.168.55.1']

print('Currently iplist looks like this:', iplist)

print()


iplistkeyed = sorted(iplist, key=len)

print('\nResults of sorted(iplist, key=len): ' + str(iplistkeyed))


bakiplistkeyed = sorted(iplist, key=len, reverse=True)

print('\nResults of sorted(iplist, key=len, reverse=True): ' + str(bakiplistkeyed))

