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
# no commnets/requirements

import os

# Check current status of touchpad
t = os.popen('synclient |grep TouchpadOff').read().strip('\n').split('=')
touch = int(t[1])

# change current status of touchpad
if      touch == 0 :
    os.popen('synclient TouchpadOff=1')

elif    touch == 1 :
    os.popen('synclient TouchpadOff=0')
