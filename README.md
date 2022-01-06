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

# Extract File Structure 

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

* Create stub files using file part of the data using this script: `build_src_files.py`

## Extract Documentation

* Use [Search Everything](https://www.voidtools.com/) to find Lego Mindstorms executable.
  * Found `MINDSTORMS-win-10.3.0-latest.289689-0.0.0.4015.exe`
* Installing [HxD](https://mh-nexus.de/en/hxd/) searching for a long string from the documentation, 
  "Python is an intuitive text-based coding language".
  * Found it stored as a json file.
* Installing the [dotPeek](https://www.jetbrains.com/decompiler) decompiler, opening the executable.
  * Found files `LEGO MINDSTORMS (10.3.0.0, x64)/Resources/Com.Lego.Flipper.variant.{GUID}`.
* Used the "Export to project" functionality.
* Uses [Sublime Text 3](https://www.sublimetext.com/3) and searched for long string from the documentation, 
  "Python is an intuitive text-based coding language".
  * Found it in `variant.5fd0c5fe69ba4ac093c0ca6e4b14d972`
* Used a formatting tool to get readable JSON.
* Manually extracted the english python documentation from the json file.
* Write the following parsing script to pre-render JSON docs: `build_docs.py`
