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

import urllib.request, urllib.error, urllib.parse
import itertools

def check_url_for_ipaddr(url):
    # fuction to return ip address informed by url

    ip = urllib.request.urlopen(url, timeout=5).read().strip()
    return ip

# list with sites to check my local ip address
url_list =  \
        [
        'http://plain-text-ip.com/'     ,
        'https://api.ipify.org/'        ,
        'http://ipecho.net/plain'
        ]

# list to hold ip addresses
ipa_result = []

# url error count
e = 0

# check each url in url list, save ip addresses in a list and count errors
for l in url_list:
    try:
        ipa = check_url_for_ipaddr(l)
        ipa_result.append(ipa)

    # counting check errors
    except urllib.error.HTTPError as err:
        e += 1
    except urllib.error.URLError as err:
        e += 1

# Print ip address list result, for debuging pourpose
#
#print(ipa_result)

# evaluate ip addresses in ip address list, errors and ip mismatch
try:
    if len(ipa_result) == 0: raise ValueError()
    m = 0

    # compare items in ip address list to find discrepancies (check if ip add
    # are equal, they should be!) and count them
    for a, b in itertools.combinations(ipa_result,2):
        if a != b: m += 1

    # print them all!
    print (ipa_result[0].decode(), 'E[{}]'.format(e), 'M[{}]'.format(m))

except:
    print ('no ext ip.addr ' 'E[{}]'.format(e))
    print ('no ext ip.addr ' 'E[{}]'.format(e))
    print ('#FF0000')
