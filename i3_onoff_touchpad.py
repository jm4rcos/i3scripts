#!/usr/bin/env python
'''
GNU GENERAL PUBLIC LICENSE v3

i3_onoff_touchpad.py
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

import os

''' Check current status of touchpad
'''
t = os.popen('synclient |grep TouchpadOff').read().strip('\n').split('=')
t1 = int(r[1])


''' change current status of touchpad
'''
if      t1 == 0 :
    os.popen('synclient TouchpadOff=1')

elif    t1 == 1 :
    os.popen('synclient TouchpadOff=0')
