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
file      /util/adjust_motor_offset/lpf2/lpf2_motor_adjust.mpy
file      /util/adjust_motor_offset/lpf2/lpf2_motor_eeprom.mpy
file      /util/adjust_motor_offset/lpf2/lpf2_packet.mpy
file      /util/adjust_motor_offset/lpf2/lpf2_process.mpy
file      /util/adjust_motor_offset/AbsoluteMotorAdjust.mpy
file      /util/__init__.mpy
file      /util/animations.mpy
file      /util/color.mpy
file      /util/constants.mpy
file      /util/error_handler.mpy
file      /util/log.mpy
file      /util/motion.mpy
file      /util/motor.mpy
file      /util/movement.mpy
file      /util/print_override.mpy
file      /util/resetter.mpy
file      /util/schedule.mpy
file      /util/scratch.mpy
file      /util/sensors.mpy
file      /util/storage.mpy
file      /util/time.mpy
directory /projects
directory /projects/standalone_
file      /projects/standalone_/__init__.mpy
file      /projects/standalone_/animation.mpy
file      /projects/standalone_/device_helper.mpy
file      /projects/standalone_/devices.mpy
file      /projects/standalone_/display.mpy
file      /projects/standalone_/priority_mapping.mpy
file      /projects/standalone_/program.mpy
file      /projects/standalone_/row.mpy
file      /projects/standalone_/util.mpy
file      /projects/standalone.mpy
file      /projects/.slots
directory /projects/27192
file      /projects/27192/__init__.mpy
directory /projects/59615
file      /projects/59615/__init__.mpy
directory /projects/14694
file      /projects/14694/__init__.mpy
directory /runtime
directory /runtime/extensions
file      /runtime/extensions/__init__.mpy
file      /runtime/extensions/abstract_extension.mpy
file      /runtime/extensions/displaymonitor.mpy
file      /runtime/extensions/linegraphmonitor.mpy
file      /runtime/extensions/music.mpy
file      /runtime/extensions/radio_broadcast.mpy
file      /runtime/extensions/sensors.mpy
file      /runtime/extensions/sound.mpy
file      /runtime/extensions/weather.mpy
file      /runtime/__init__.mpy
file      /runtime/dirty_dict.mpy
file      /runtime/multimotor.mpy
file      /runtime/stack.mpy
file      /runtime/virtualmachine.mpy
file      /runtime/vm_store.mpy
directory /system
directory /system/callbacks
file      /system/callbacks/__init__.mpy
file      /system/callbacks/customcallbacks.mpy
file      /system/__init__.mpy
file      /system/abstractwrapper.mpy
file      /system/display.mpy
file      /system/motors.mpy
file      /system/motorwrapper.mpy
file      /system/move.mpy
file      /system/movewrapper.mpy
file      /system/simplemotorwrapper.mpy
file      /system/simplemovewrapper.mpy
file      /system/sound.mpy
directory /_api
file      /_api/__init__.mpy
file      /_api/app.mpy
file      /_api/button.mpy
file      /_api/colorsensor.mpy
file      /_api/control.mpy
file      /_api/distancesensor.mpy
file      /_api/forcesensor.mpy
file      /_api/large_technic_hub.mpy
file      /_api/lightmatrix.mpy
file      /_api/motionsensor.mpy
file      /_api/motor.mpy
file      /_api/motorpair.mpy
file      /_api/operator.mpy
file      /_api/speaker.mpy
file      /_api/statuslight.mpy
file      /_api/util.mpy
directory /commands
file      /commands/__init__.mpy
file      /commands/abstract_handler.mpy
file      /commands/device_methods.mpy
file      /commands/hub_methods.mpy
file      /commands/light_methods.mpy
file      /commands/linegraphmonitor_methods.mpy
file      /commands/motor_methods.mpy
file      /commands/move_methods.mpy
file      /commands/program_methods.mpy
file      /commands/radio_broadcast_methods.mpy
file      /commands/sound_methods.mpy
file      /commands/wait_methods.mpy
directory /event_loop
file      /event_loop/__init__.mpy
file      /event_loop/event_loop.mpy
directory /mindstorms
file      /mindstorms/__init__.mpy
file      /mindstorms/control.mpy
file      /mindstorms/operator.mpy
file      /mindstorms/util.mpy
directory /programrunner
file      /programrunner/__init__.mpy
directory /protocol
file      /protocol/__init__.mpy
file      /protocol/notifications.mpy
file      /protocol/rpc_protocol.mpy
file      /protocol/ujsonrpc.mpy
directory /sounds
file      /sounds/menu_click
file      /sounds/menu_fastback
file      /sounds/menu_program_start
file      /sounds/menu_program_stop
file      /sounds/menu_shutdown
file      /sounds/startup
directory /spike
file      /spike/__init__.mpy
file      /spike/control.mpy
file      /spike/operator.mpy
file      /spike/util.mpy
directory /ui
file      /ui/__init__.mpy
file      /ui/hubui.mpy
file      /hub_runtime.mpy
file      /version.py
file      /.runtime_hash
directory /etc
file      /etc/linkkeys
file      /etc/hostname
directory /extra_files
file      /extra_files/Affirmative
file      /extra_files/Damage
file      /extra_files/Exterminate
file      /extra_files/Fire
file      /extra_files/Grab
file      /extra_files/Hammer
file      /extra_files/Laser
file      /extra_files/Laugh
file      /extra_files/Mission Accomplished
file      /extra_files/Punch
file      /extra_files/Scanning
file      /extra_files/Seek and Destroy
file      /extra_files/Shut Down
file      /extra_files/Target Acquired
file      /extra_files/Target Destroyed
file      /extra_files/Whirl
file      /extra_files/1234
file      /extra_files/Delivery
file      /extra_files/Dizzy
file      /extra_files/Goodbye
file      /extra_files/Hello
file      /extra_files/Hi
file      /extra_files/Hi 5
file      /extra_files/Humming
file      /extra_files/Chuckle
file      /extra_files/Like
file      /extra_files/No
file      /extra_files/Ouch
file      /extra_files/Sad
file      /extra_files/Scared
file      /extra_files/Tadaa
file      /extra_files/Wow
file      /extra_files/Yes
file      /extra_files/Yipee
file      /extra_files/Yuck
file      /extra_files/Activate
file      /extra_files/Kick
file      /extra_files/Shake
file      /extra_files/Deactivate
file      /extra_files/Initialize
file      /extra_files/Brick Eating
file      /extra_files/Horn
file      /extra_files/Hydraulics Down
file      /extra_files/Hydraulics Up
file      /extra_files/Reverse
file      /extra_files/Revving
file      /extra_files/Shooting
file      /extra_files/Play
file      /extra_files/Countdown
file      /extra_files/Countdown Tick
file      /extra_files/Error
file      /extra_files/Ping
file      /extra_files/Success Chime
file      /extra_files/Bowling
file      /extra_files/Celebrate
file      /extra_files/Explosion
file      /extra_files/Goal
file      /extra_files/Hit
file      /extra_files/Slam Dunk
file      /extra_files/Strike
file      /.extra_files_hash
file      /runtime.log
file      /test.txt
file      /lego-test.txt
"""


if __name__ == '__main__':
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
