"""
A file named hosts holds hostnames and IP addresses
in format: hostname=ip
Write a program that reads the file and takes
a list of hostnames in sys.argv
Program should print the IP addresses of the hosts requested
"""
import sys

host_ip_map = {}

with  open("d:\hosts",'r') as ff:
    for line in ff:
        key_value=str.split(line,'=')
        key = (key_value[0]).rstrip()
        value = key_value[1].rstrip() 
        if key in host_ip_map:
            host_ip_map[key] =  host_ip_map[key]  + ';' + value
        else:
            host_ip_map[key] = value

for k in sys.argv[1:]:
    if k not in host_ip_map:
        print 'host '+k+' is empty'
        continue
    print ('host:{} ips:{}').format(k,host_ip_map[k])