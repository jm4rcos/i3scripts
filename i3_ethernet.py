#!/usr/bin/env python3
#
# GNU GENERAL PUBLIC LICENSE v3
#
# Copyright (C) <2016> JOSE MARCOS <jm4rcos@gmail.com>
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
# Script requires network manager installed

import os

# Set interface instance here. It must match your ethernet interface name.
instance = 'enp5s0'

try:
    # Get interface status, if unavailable, quit.

    show_i = os.popen("nmcli device show " + instance )
    status = show_i.read().split('\n')
    for item in status:
        if item.startswith('GENERAL.STATE'):
            item = item.split(':')
            item = item[1].lstrip(' ').split(' ')
            if item[0] == '20' : quit()

    # Get interface ip address.

    eth_ipa = os.popen("nmcli device show " + instance + \
                                    "|grep IP4.ADDRESS |awk -F' ' '{print $2}'")
    eth_ipa = eth_ipa.read().split('/')

    # Get interface speed and duplex.

    int_s = os.popen("ethtool " + instance)

    for line in int_s.read().split('\n\t'):
        if line.startswith('Speed'): s = line
        if line.startswith('Duplex'): d = line

    s = s.split(':')
    d = d.split(':')

    # Change speed/duplex output format.

    if s[1] == ' 1000Mb/s': s = '1Gb/s'
    if s[1] == ' 100Mb/s' : s = '100Mb/s'
    if s[1] == ' 10Mb/s'  : s = '10Mb/s'

    if d[1] == ' Full':     d[1] = 'FD'
    if d[1] == ' Half':     d[1] = 'HD'

    # Get interface "wired-properties.carrier" status.
    # "wired-properties.carrier" shows if cable is connected.

    #eth_w_status = os.popen("nmcli device show " + instance + \
    #                   "|grep WIRED-PROPERTIES.CARRIER |awk -F' ' '{print $2}'")

    #eth_wire_status = eth_w_status.read().strip('\n')

    # Print them
    #print (eth_ipa[0], s, d[1], '[', eth_wire_status, ']')
    print (eth_ipa[0], s, d[1])

except:
    # Print 3 values as expected by i3blocks:
    # full text, short text and color.

    print ('down')
    print ('down')
    print ('#FF0000')
