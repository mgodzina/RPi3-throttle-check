#!/usr/bin/env python3
import subprocess

Command = 'vcgencmd get_throttled'

Alerts = {
    0: 'Under-voltage!',
    1: 'ARM frequency capped!',
    2: 'Currently throttled!',
    16: 'Under-voltage has occurred since last reboot.',
    17: 'Throttling has occurred since last reboot.',
    18: 'ARM frequency capped has occurred since last reboot.',
    19: 'Soft temperature limit has occurred'
}


output = subprocess.check_output(Command, shell=True)
print(output[:-1])
bits = bin(int(output.split('=')[1], 0))[2:].zfill(20)

warnings = 0
for pos, alert in Alerts.items():
    if bits[pos] == '1':
        print(alert)
