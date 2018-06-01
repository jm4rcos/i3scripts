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
#
# usage: ./i3_brightness_ctrl.py <value>
#
# [*] allowed values for sys.argv[1] (first argument for script) are:
#    +/- 0.1
#    +/- 0.3
#    +/- 0.5

import os
import sys

# current brightness value as float type
#
b = os.popen("xrandr --verbose | grep -i brightness | cut -f2 -d ' ' | head -n1")
b = float(b.read().strip('\n'))

# read brightness new value
#
try:
    new_b = float(sys.argv[1])

except IndexError:
    exit()

# check if sys.argv[1] is one of the allowed values and add it to current
# brightness values
#
if any(x == new_b for x in [0.1, -0.1, 0.3, -0.3, 0.5, -0.5]):
    os.popen("xrandr --output LVDS-0 --brightness " + str(b + new_b))
