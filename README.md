# Motivation

LEGO MINDSTORMS Python is a lot fun to play with! However, I don't like to be limited by the Lego IDE, and would rather develop using PyCharm.

This project aims to implements [stubs](https://en.wikipedia.org/wiki/Method_stub) and documentation for all of the classes and functions of the `mindstorms` library. It does NOT implement the actual underlying code, and does not make it possible to directly run your programs on your LEGO robot. You will still need to copy your code over to the LEGO MINDSTORMS app. Helper functions will be included to make this process less painful.

# Resources

* Official Documentation: [MINDSTORMS-Robot-Inventor-hub-API](https://lego.github.io/MINDSTORMS-Robot-Inventor-hub-API/)
* Required Official App: [LEGO MINDSTORMS Robot Inventor](https://www.microsoft.com/en-us/p/lego-mindstorms-robot-inventor/9mtq0n7w1d6x?activetab=pivot:overviewtab)
* Similar Project: [Mindstorms / SPIKE Prime / SPIKE Essential](https://github.com/gpdaniels/spike-prime)

# Legal

I claim no rights to any of the documentation or API, of which all are probably owned by LEGO.

# Process

Originally I planned on using [robot-inventor-tools](https://github.com/ckumpe/robot-inventor-tools)
and simply sniff the packets going through. However, I was running on Windows and couldn't get it 
working properly.

Instead, I used the following process

* Install [wireshark](https://www.wireshark.org/#download)
* Install [btvs.exe](https://techcommunity.microsoft.com/t5/microsoft-bluetooth-blog/introducing-bluetooth-virtual-sniffer-btvs-exe/ba-p/2113478) from MS
* Start `btvs.exe -mode Wireshark`
* Enable full packet logging
* Connect to the Hub via the LEGO MINDSTORMS app
* Write code in the LEGO MINDSTORMS app which writes wanted output:

```python
import mindstorms
import os

print(dir(os))

MAX_DEPTH = 2

print('LEGO LOG', 'getcwd:    ', os.getcwd())
print('LEGO LOG', '__file__:    ', __file__)

def check_out_path(target_path, level=0):
    try:
        sub_files = os.listdir(target_path)
        print('LEGO LOG', 'directory', target_path)
        for sub_file in sub_files:
            sub_path = (target_path + '/' + sub_file).replace('//', '/')
            check_out_path(sub_path, level+1)
    except Exception as ex:
        print('LEGO LOG', 'file     ', target_path)

check_out_path('/')

def explore(obj, obj_type, obj_name, depth=0):
    print('LEGO LOG', '>' * depth, obj_type, obj_name)
    if obj_type in ('type', 'module', 'package') and depth <= MAX_DEPTH:
        for obj_elm_name in dir(obj):
            obj_elm = getattr(obj, obj_elm_name)
            obj_elm_type = type(obj_elm).__name__
            explore(obj_elm, obj_elm_type, obj_elm_name, depth+1)
    elif obj_type in ('function',):
        pass  # TODO: Try to print arguments.

explore(mindstorms, 'package', 'mindstorms')
```

(It is writen in a little odd fashion because some of the standard python OS library level tools are missing.) 

* Prefix log output with `LEGO LOG`
* Use the following filter `data.data matches "UserProgram" && data.data matches "TEVH"` in Wireshark. 
  The bit about `TEVH` is just the first part of the string `LEGO LOG` in base64 encoding, the full 
  string would have been `TEVHTyBMT0c=`.
* Run the program in the LEGO MINDSTORMS app.
* After the lego code has run Export Packet Dissections as JSON
* Fetch and decode the print statements using the following code:

```python
import json
import codecs
import base64

with open('packet_data.json', 'rt') as file:
    packets = json.load(file)

    for packet in packets:
        hex_str = packet['_source']['layers']['data']['data.data'].replace(':', '')
        payload_str = codecs.decode(hex_str, 'hex').decode('utf-8')
        try:
            payload = json.loads(payload_str)
            message = base64.b64decode(payload['p']['value']).decode('utf-8')[len('LEGO LOG'):].strip()
        except:
            message = payload_str.strip()
        print(message)
```

* Create stub files using file part of the data using this script:

```python
import os

files = """
file      /boot.py
file      /bt-lk1.dat
file      /bt-lk2.dat
file      /main.py
directory /util
directory /util/adjust_motor_offset
directory /util/adjust_motor_offset/lpf2
file      /util/adjust_motor_offset/lpf2/__init__.mpy
file      /util/adjust_motor_offset/lpf2/lpf2_logging.mpy
...
"""

for file_line in files.strip().split('\n'):
    file_path = file_line[len('directory') + 2:]
    if (file_line.startswith('file') and (file_path.endswith('.mpy') or file_path.endswith('.py'))):
        if file_path.endswith('.mpy'):
            file_path = file_path[:-len('.mpy')] + '.py'
        print('FILE', file_path)
        with open('src/' + file_path, 'wt') as file:
            file.write('')
    elif file_line.startswith('directory'):
        print('DIR', file_path)
        os.makedirs('src/' + file_path)
```

* Next manually populate the various modules with appropriate stubs.
