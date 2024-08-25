import ifcfg
import json

def is_en(pair):
    key, value = pair
    if key.startswith('en'):
        return True
    else:
        return False

# Filtering for en devices    
en_devices = dict(filter(is_en, ifcfg.interfaces().items()))

# Sorting for en devices
en_devices = {key:en_devices[key] for key in sorted(en_devices)}

en_ip = dict()

# Filtering ip and mask
for device in en_devices.keys():
    en_ip[device] = dict()
    for param in en_devices[device].keys():
        if param == 'inet':
            en_ip[device][param] = en_devices[device][param]
        elif param == 'netmask':
            en_ip[device][param] = en_devices[device][param]




out = json.dumps(en_ip, indent=4)
print(out)