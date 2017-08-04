#!/usr/bin/env python
#
# GNU GENERAL PUBLIC LICENSE v3
#
# Copyright (C) <2017> JOSE MARCOS <jm4rcos@gmail.com>
#
# This program  is free software: you can redistribute it and/or modify it under
# the  terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3  of  the License, or (at your option)  any  later
# version.
#
# This  program  is distributed in the hope that it will be useful,  but WITHOUT
# ANY WARRANTY;  without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.
#
# See <http://www.gnu.org/licenses/>  for more details of the GNU General Public
# License.
#
# comments/requirements:
# no commnets/requirements

import os

# Set interface instance here. It must match your wireless interface name.

instance = 'wlp2s0'


try:
    # Get interface ip address.

    wipa = os.popen("nmcli device show " + instance + \
                                    "|grep IP4.ADDRESS |awk -F' ' '{print $2}'")
    wipaddr = wipa.read().split('/')

    # Get wireless signal, quit if none.

    q = os.popen("grep " + instance + \
                     " /proc/net/wireless | awk '{ print int($3 * 100 / 70) }'")
    signal = q.read().rstrip()

    if signal == '' : quit()

    # Print them all
    #
    signal = signal+'%'
    print wipaddr[0], signal

except:
    # Print 3 values as expected by i3blocks - full text, short text and color.
    #
    print 'down'
    print 'down'
    print '#FF0000'
