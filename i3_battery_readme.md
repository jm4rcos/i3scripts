## Readme file for i3_battery.py

#### Battery status:

This python script outputs battery charge status (%) and AC adapter power plug status.

examples:

1. Battery 100% charged and AC adapter power cord plugged.

   ![alt text][bat100]

2. Battery 62% charged and AC adapter power cord unplugged.

   ![alt text][bat62]

3. Battery 15% charged and AC adapter power cord unplugged.

   ![alt text][bat15]

[bat100]: https://github.com/jm4rcos/i3scripts/blob/master/img/bat_100.png "battery indication 100%"
[bat62]: https://github.com/jm4rcos/i3scripts/blob/master/img/bat_62.png "battery indication 62%"
[bat15]: https://github.com/jm4rcos/i3scripts/blob/master/img/bat_15.png "battery indication 15%"


#### Requirements

Script designed to work with i3blocks to give battery status to i3bar.

This  python  script  uses  acpi  to get battery status and requires FontAwesome to be installed in your system.

https://fortawesome.github.io/Font-Awesome/

key value for "markup" has to be "pango" in i3blocks config file, see example below:

```
# battery status
[batt]
command=~/github/i3scripts/i3_battery.py
markup=pango
interval=10
```
