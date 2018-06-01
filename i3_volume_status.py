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

s = os.popen('amixer get Master | grep Mono:')
s = s.read().split(' ')

vol_level       = int(s[4])
mute_status     = s[7].strip('\n')

def get_vol_status():
    if mute_status == '[off]':
        vol_icon = "<span font='FontAwesome'>&#xf026;</span>"
    elif vol_level <= 50:
        vol_icon = "<span font='FontAwesome'>&#xf027;</span>"
    elif vol_level > 50:
        vol_icon = "<span font='FontAwesome'>&#xf028;</span>"
    return vol_icon

vol_icon = get_vol_status()

print(vol_icon)
print(vol_icon)
print()
