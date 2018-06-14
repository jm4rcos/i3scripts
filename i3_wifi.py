#!/usr/bin/env python3
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

# icon copied from fontAwesome cheatsheet, https://fontawesome.com/cheatsheet
# just copy/paste the icon here

wifi_icon = ""

DD = {}

def find_interface_instance():
    devices = os.popen("nmcli dev show").read().split("\n")
    for line in devices:
        if line.startswith("GENERAL.DEVICE")  :GD=line.split(":")[1].lstrip()
        if line.startswith("GENERAL.TYPE")    :GT=line.split(":")[1].lstrip()
        if line == "":
            if GT.startswith("wif"): DD[GT]=GD     # wifi if
            if GD.startswith("enp"): DD[GT]=GD     # ethernet if
    #returns value for wifi or ethernet
    instance = DD['wifi']
    return instance


def check_wifi_radio_status():
    r = ''
    r_status = os.popen("nmcli radio wifi").read().strip()
    if r_status == 'enabled':  r = True
    if r_status == 'disabled': r = False
    return r


instance     = find_interface_instance()
radio_status = check_wifi_radio_status()

if radio_status == True:
    icon = "<span fgcolor='#b0b0b0' font='FontAwesome'>&#xf1eb;</span>"
else:
    icon = "<span fgcolor='#404040' font='FontAwesome'>&#xf1eb;</span>"

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
    print (icon,         \
           wipaddr[0],   \
           signal        \
          )

except:
    # Print 3 values as expected by i3blocks - full text, short text and color.
    #
    print (icon, "<span font_style='italic'> no ip_addr</span>")
    print (icon, "<span font_style='italic'> no ip_addr</span>")
    print ('#595959')
