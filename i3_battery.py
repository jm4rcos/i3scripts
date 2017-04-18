#!/usr/bin/env python
'''
GNU GENERAL PUBLIC LICENSE v3

i3_battery.py
Copyright (C) <2016> JOSE (J) MARCOS <jm4rcos@gmail.com>

This program  is free software:  you  can redistribute it and/or modify it under
the  terms  of the GNU General Public License  as published by the Free Software
Foundation, either version 3  of  the  License, or  (at your option)  any  later
version.

This program  is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY;  without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

See  <http://www.gnu.org/licenses/>  for  more details of the GNU General Public
License.
'''

'''
this  python  script  uses  acpi  to get battery status and requires FontAwesome
to be installed on your system.

https://fortawesome.github.io/Font-Awesome/

key  value  for "markup" has to be "pango" in  i3blocks config file.

'''

import os

b_level = ''
bat_status = ''
ac_is = ''
color = '#ffffff'
#color = '#000000'
plug =  "<span font='FontAwesome'>&#xf1e6;</span>"

def bat_level():
    acpi_battery = os.popen('acpi -b')
    b = acpi_battery.read().split(',')
    bat = b[1].strip().strip('%')
    b_level = int(bat)
    return b_level

def ac_status():
    acpi_ac_adap = os.popen('acpi -a')
    ac = acpi_ac_adap.read().split(':')
    ac_status = ac[1].strip()
    return ac_status


b_level   = bat_level()
ac_status = ac_status()


if ac_status == 'on-line':
    ac_is = "<span font='FontAwesome'>&#xf1e6;</span>"
    color = '#008a00'

elif b_level == 100 :
    ac_is = "<span font='FontAwesome'>&#xf240;</span>"
    color = '#008a00'

elif b_level >= 75 and b_level < 100 :
    ac_is = "<span font='FontAwesome'>&#xf241;</span>"
    color = '#008a00'

elif b_level >= 25 and b_level < 75  :
    ac_is = "<span font='FontAwesome'>&#xf242;</span>"
    color = '#008a00'

elif b_level >= 1 and b_level < 25  :
    ac_is = "<span font='FontAwesome'>&#xf243;</span>"
    color = '#FF0000'

''' Print 3 values as expected by i3blocks:
    full text, short text and color.
'''
print ac_is + " " +  str(b_level) + '%'
print ac_is + " " +  str(b_level) + '%'
print color


# jmarcos@mammuth:~$ acpi -b
# Battery 0: Charging, 99%, 00:00:01 until charged
# jmarcos@mammuth:~$ acpi -b
# Battery 0: Unknown, 99%
#
# jmarcos@mammuth:~$
# jmarcos@mammuth:~$ acpi -a
# Adapter 0: on-line
# jmarcos@mammuth:~$ acpi -a
# Adapter 0: off-line
