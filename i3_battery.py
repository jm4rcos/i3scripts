#!/usr/bin/env python3
#
# GNU GENERAL PUBLIC LICENSE v3
#
# Copyright (C) <2016> JOSE *MARCOS* <jm4rcos@gmail.com>
#
# This program  is free software: you can redistribute it and/or modify it under
# the  terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3  of  the License, or (at your option)  any  later
# version.
#
# This  program  is distributed in the hope that it will be useful,  but WITHOUT
# ANY WARRANTY; without even  the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.
#
# See <http://www.gnu.org/licenses/>  for more details of the GNU General Public
# License.
#
# comments/requirements:
# Script designed to work with i3blocks to return battery status to i3bar.
#
# This python  script  uses  acpi to get battery status and requires FontAwesome
# to be installed on your system.
#
# [*] see https://fortawesome.github.io/Font-Awesome/
# [*] key value  for "markup" has to be "pango" in  i3blocks config file.


import os

b_level = ''
batt_status = ''
ac_icon = ''

def batt_level():
    # this function returns battery level and relative level color

    acpi_battery = os.popen('acpi -b')
    b = acpi_battery.read().split(',')
    batt = b[1].strip().strip('%')

    # the battery level
    b_level = int(batt)

    return b_level

def ac_status():
    # this function returns battery cable status (on-line, off-line)

    acpi_ac_adap = os.popen('acpi -a')
    ac = acpi_ac_adap.read().split(':')
    ac_status = ac[1].strip()

    return ac_status

# get values from fuctions
b_level   = batt_level()
ac_status = ac_status()

# logic to define battery icon
if ac_status == 'on-line':
    ac_icon = "<span font='FontAwesome'>&#xf1e6;</span>"

elif b_level == 100 :
    ac_icon = "<span font='FontAwesome'>&#xf240;</span>"

elif b_level >= 75 and b_level < 100 :
    ac_icon = "<span font='FontAwesome'>&#xf241;</span>"

elif b_level >= 25 and b_level < 75  :
    ac_icon = "<span font='FontAwesome'>&#xf242;</span>"

elif b_level >= 1 and b_level < 25  :
    ac_icon = "<span font='FontAwesome'>&#xf243;</span>"
    color   = '#FF0000'

# Print 3 values as expected by i3blocks:
# full text, short text and color.

print (ac_icon + " " +  str(b_level) + '%')
print (ac_icon + " " +  str(b_level) + '%')

if b_level >= 1 and b_level < 25 and ac_status != 'on-line': print (color)
else: print ()
