#!/usr/bin/env python
'''
GNU - GENERAL PUBLIC LICENSE v3

get_extarnal_ip.py

Copyright (C) <2016> JOSE (J) MARCOS <jm4rcos@gmail.com>

The  GNU  General  Public  License is  a free, copyleft license  for
software and other kinds of works.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the  Free Software Foundation,  either  version 3 of the License, or
(at your option) any later version.

This  program  is distributed  in  the hope that it  will be useful,
but  WITHOUT  ANY  WARRANTY;  without even  the implied warranty  of
MERCHANTABILITY  or  FITNESS  FOR  A  PARTICULAR  PURPOSE.  See  the
GNU General Public License for more details.

You   should  see  a copy of  the  GNU  General  Public  License  @
<http://www.gnu.org/licenses/>.
'''


import urllib2

try:
    try:
        gurl = urllib2.urlopen('http://checkip.org/',timeout=5)
        for line in gurl:
            if line.startswith('<h1>Your IP'):
                ip_ = line.split('>')
                ip_ = ip_[2].split('<')
                ip1 = ip_[0]
        print ip1

        # gurl = urllib2.urlopen('https://myexternalip.com/raw')
        # ip2 = gurl.read().strip('\n')
        #
        # dig +short myip.opendns.com @resolver1.opendns.com



    except URLError:
        print "err: url.err"

    except socket.timeout:
        print "err: sock.to"

except:
    print 'NO EXT IP'
    print 'NO EXT IP'
    print '#FF0000'
