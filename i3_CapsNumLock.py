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
# Script designed to work with i3blocks to return CAPS and NUM status to i3bar.
#
# [*] key value  for "markup" has to be "pango" in  i3blocks config file.


import os

caps_onOff = ''
num_onOff  = ''
color_on   = ''

def is_caps_onOff():
    # this function returns on/off status for Caps

    caps_onOff = os.popen('xset q | grep -i caps | cut -c 22-24').read().strip()
    return caps_onOff

def is_num_onOff():
    # this function returns on/off status for Num

    num_onOff  = os.popen('xset q | grep -i caps | cut -c 46-48').read().strip()
    return num_onOff

caps_onOff = is_caps_onOff()
num_onOff  = is_num_onOff()

if caps_onOff == 'on':
    C = "<span foreground=\"white\" background=\"gray\" \
                              font_weight=\"bold\"> C </span>"
else:
    C = "<span font_weight=\"bold\"> C </span>"

if num_onOff  == 'on':
    N = "<span foreground=\"white\" background=\"gray\" \
                              font_weight=\"bold\"> N </span>"
else:
    N = "<span font_weight=\"bold\"> N </span>"


# Print values as expected by i3blocks:
#
print (C + " | " +  N)
print (C + " | " +  N)
