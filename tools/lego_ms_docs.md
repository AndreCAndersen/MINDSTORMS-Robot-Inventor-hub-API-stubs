Python Basics
-------------


# Getting Started
# Introduction
Python is an intuitive text-based coding language, renowned worldwide and used in different sectors from web development to software development and scientific applications. It’s an excellent programming language for beginners because it’s concise and easy-to-read.

Here is a place you can start to learn coding with MINDSTORMS Python. In the following sections of the “Python Help Center” you will find a lot of information to help you explore the Python functionalities of MINDSTORMS.

**Using this Python Help Center**

This Python Help Center has been organized into these 3 sections:

 - A step-by-step Getting Started section that will guide you through the exploration of the most common functions used to control the MINDSTORMS Hub, motors, and sensors.
 - The Word Block Translator will show you some of the well known Word Blocks translated into Python Code.
 - The Libraries section is where you’ll find descriptions of all the functions in the different libraries as well as code examples that are available to experiment with. To explore and play around with these examples, copy them to your project, then modify and customize them to fit with the rest of your program.


**Alright, here we go!**
# Writing a MINDSTORMS Python Program
There are only a few rules that you have to keep in mind when writing your program with Python.
Importing Libraries
-------------------

When creating a Python project, you often have to import one or more libraries. In terms of programming, a library is a set of useful functions that you can use to perform specific actions. These functions are pre-made so that you don't have to spend time creating them yourself in your own program. 
When creating your MINDSTORMS Python program you must always import the libraries that correspond to the different hardware your model is using like the hub, motors and sensors.
### Writing a MINDSTORMS Python Program

```python
from mindstorms import MSHub, Motor, ColorSensor, DistanceSensor
```

The import of libraries must be made at the beginning of the program, and must be done only once.
If you’re unsure of which libraries you should import, you can always import everything possible using this code example:
### Writing a MINDSTORMS Python Program 1

```python
from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
```

By default all the available libraries are imported in the template program automatically loaded when you start a new Python project. 

Creation of Objects
-------------------

After you’ve imported the right libraries, you need to “create objects" to be able to use the functions of some libraries. This is how to create objects for the hub, motor, and sensors:
### Writing a MINDSTORMS Python Program 2

```python
# Initialize the hub.
hub = MSHub()
# Initialize the motors connected to Ports A and B.
motor_a = Motor('A')
motor_b = Motor('B')
# Initialize the Color Sensor connected to Port C.
color_sensor = ColorSensor('C')
# Initialize the Distance Sensor connected to Port D.
distance_sensor = DistanceSensor('D')
```

You can create as many objects as you want, but it is advisable to create only one per hardware component on your model. Try to give a meaningful name to the objects you create, like: `hub`, `color_sensor`, `motor_a`, `motor_left_arm`, `motor_right_wheel` etc. This will make your code easier to read and understand. 
Note that not all libraries need an object.
Function call

To use the functions the libraries contain, you need to call them in your program by writing the function name followed by a pair of parenthesis like so:
### Writing a MINDSTORMS Python Program 3

```python
distance_sensor.light_up_all()
motor_a.start()
wait_for_seconds(2)
distance_sensor.wait_for_distance_closer_than(10, 'cm')
motor_a.stop()
```

Some of these functions have parameters that you need to specify. Parameter as the name implies help you change the parameters of a function to help you define even more precisely what the function should do or how it should do it.
### foo()1

```python
from mindstorms import MSHub

hub = MSHub

# the function shows an image on the light matrix
# the 2 parameters define precisely which image: 'GO_RIGHT' and what brightness: 100%
hub.light_matrix.show_image('GO_RIGHT', 100)
```

The values you have to provide (called arguments) can be a constant value that you write directly in your program, variables or function's return value.
### foo()2

```python
from mindstorms import MSHub
from random import randint

hub = MSHub()

# Values specified directly in the code.
hub.speaker.beep(60, 0.2)

# Values specified as variables.
tone = randint(44, 123)
seconds = 0.2
hub.speaker.beep(tone, seconds)

# Values specified from a function return value.
hub.speaker.beep(randint(44, 123), randint(0.1, 0.5))
```

The values (arguments) have to be provided in the same order the parameters are defined in the Help Center function description. You can however disregard the order if you affect the value directly to the parameter using its name.
### foo()3

```python
from mindstorms import MSHub

hub = MSHub()

# Values specified in the same order as the function description: x, y and brightness.
hub.light_matrix.set_pixel(3, 3, 100)
# Values specified in a different order using the parameter's name
hub.light_matrix.set_pixel(brightness = 100, y = 1, x = 1)


```

Some parameters do not need to have a specified value because they have a default value that the function will use instead.
### foo()4

```python
from mindstorms import MSHub

hub = MSHub()

# Values are specified.
hub.speaker.beep(90, 0.5)
# Values are not specified, the function uses the default tone: 60 and seconds: 0.2
hub.speaker.beep()
```

Writing Convention
------------------

Python is sensitive to capitalization, line breaks, spaces and indentation (the spaces at the beginning of a code line). This makes Python easier to code and read, once you are familiar with the rules.
One important rule is that each command is written on a new line:
### Writing a MINDSTORMS Python Program 5

```python
# This is a command:
hub = MSHub()
# This is another command on a new line:
hub.light_matrix.write('MINDSTORMS')
```

Another important rule is the indentation.
Indentation represents the body (block of code) of loops, conditions and functions.
In other words, indentation represent where a loop, a condition or a function starts and stops.
For example there is a difference between:
### Writing a MINDSTORMS Python Program 6

```python
if 1 > 0:
print('MINDSTORMS')
```

and
### Writing a MINDSTORMS Python Program 7

```python
if 1 > 0:
    print('MINDSTORMS')
```

The first example will generate a Syntax Error due to the missing indentation before `print('MINDSTORMS')`, while the second example will display “MINDSTORMS” in the console. You can try each of these examples, one at a time, to see for yourself.

Comments in Python
------------------

Every line starting with a “#” is considered a comment. Therefore, it is not executed as a statement. Comments are helpful to explain and remember what your code and commands do and also for code readability.
### Writing a MINDSTORMS Python Program 8

```python
# This is a comment.
# This is another comment.
```

The Console
-----------

The console is located at the bottom of the coding canvas. You can access it by clicking this icon:
In the console you can see if there are any errors when running your code. You can also use the console as a debugging tool to display your own text by using the `print()` command, for example:
### Writing a MINDSTORMS Python Program 4

```python
my_variable = 0
print('This text will be displayed in the console.')
print('my_variable:', my_variable)
```

An error in your code will be represented like this in the console:
There are several types of errors. These are the most common errors you can encounter: 
- SyntaxError
- TypeError
- ValueError
- RuntimeError
- NameError 

The console will inform you where the error happened in your code so that you can refer to the line number and correct it.
You can look into the section **More Python Basics** to find more info about errors.
# Function Description
Functions available in the MINDSTORMS Python Library have been divided into multiple sections that will be explained here:

 - Description
 - Code example
 - Parameters
 - Return
 - Errors


**Description**

Every function article start with the name of the function followed by a short description of what the function does.

**Code Example**

A code example of how this function can be used is provided. You can copy the example to your canvas by using the copy button at the top right of the code example and then paste it to your canvas.

**Parameters**

If the function takes one or multiple parameters, these will be listed and explained in this section.

Each Parameter is described by its name, type, value and default value.

In your program, it is important  that you respect the parameter's type (integer, float, boolean, string, etc.) otherwise your program will generate an error.

The value field indicates if the parameter has a specific range of values it can accept. There are two types of value ranges:

 - Fixed range
 - Limited range


Fixed range means that the value you specify has to be within the range of the lower and upper limits described, otherwise the program will generate an error. You can see if the range is limited by checking if there is a ValueError mentioned in the error field of the function description.

Limited range means that if the value you specify in your program is outside the range, the function will use the lower or upper limit instead, depending on which limit your value is closer to. For example on a limited value range -100 - 100, a value of -400 will be limited to -100.

If no value range is mentioned the value can be anything as long as the type is respected (i.e. any number for float or any text for string, etc.)

A parameter can either be required or optional. When a parameter is required, it must be specified in your program. When a parameter is optional, it can be omitted in your program, in this case, the function uses the default value of that parameter.

**Return**

If the function returns a value, it will be described in that section. Returned values have a type, a description and a value range. The value returned by the function will be within that range.

**Errors**

In this section all possible errors a function can generate are listed.
# Programming Simple Outputs
What You Will Need
------------------

You're going to create some short programs for your Hub.

Make sure that you have:  

- Installed the battery.
- Turned it on by pressing the Center Button.
- Connected it to your device via Bluetooth or USB.
Controlling the Light Matrix
----------------------------

Create your first program using Python. 

Copy the code below by pressing the copy icon.
Paste the code to the Programming Canvas.

Purple lines are comments, they will not influence the actions. The other lines are your program. Can you figure out what this first program is all about?

Then, play the program!
### Programming Simple Outputs

```python
# Import the MSHub class.
from mindstorms import MSHub
from mindstorms.control import wait_for_seconds
# Initialize the Hub.
hub = MSHub()
# Show a smiley face for five seconds.
hub.light_matrix.show_image('HAPPY')
wait_for_seconds(5)
hub.light_matrix.off()
```

You should see a happy face on the Hub.
To change the image that’s displayed on the Light Matrix.

Either change the parameter `'HAPPY'` to `'GO_RIGHT'` in the code you already have. This will light up the play icon instead of the happy face on the Hub.

Or copy in the code in the box bellow and paste it after the last line of your program. This will light up the happy face for 5 seconds, and then it will light up a play icon for 5 seconds.
### Programming Simple Outputs 1

```python
# Show another image for five seconds.
hub.light_matrix.show_image('GO_RIGHT')
wait_for_seconds(5)
hub.light_matrix.off()
```

**Congratulations!** 

You have written your first program using Python. Keep going to learn more.

Playing Small Beeps and Time
----------------------------

Let’s make the Hub play some beeps.

- If you have a program on the Programming Canvas, it is a good idea to delete it or start a new project to continue.
- Then, copy the code below to the Programming Canvas.
- Make sure you have only one line of code that starts with: `from mindstorms import`.
- Play the program!
### Programming Simple Outputs 2

```python
# Import the MSHub class.
from mindstorms import MSHub
from mindstorms.control import wait_for_seconds
# Initialize the Hub.
hub = MSHub()
# Beep beep beep!
hub.speaker.beep(60, 1)
```

Change the beat and the tone. Here is one way to do it.
### Programming Simple Outputs 3

```python
# Here’s a new song:
hub.speaker.beep(60, 0.5)
hub.speaker.beep(67, 1.0)
wait_for_seconds(0.5)
hub.speaker.beep(60, 0.5)
```

Playing Sounds
--------------

You can also add some sounds to be played from your device.

Copy the code below to the Programming Canvas. Play the program!
### Programming Simple Outputs 4

```python
# Import the App class.
from mindstorms import App
# Initialize the app.
app = App()
# Play a sound.
app.play_sound('Applause 1')
```

Pick another sound to play, or use this program.
### Programming Simple Outputs 5

```python
app.play_sound('Triumph')
```

Challenge
---------

Use the functions you’ve learned so far.
Create a short countdown program, something like 3, 2, 1, BOOM!
# Controlling the Motors
What You’ll Need
----------------

Now we’ll connect a motor and turn it on. Connect a motor to one of the Ports with a letter (e.g., Port A). 

Run Single Motor for Time
-------------------------

Let’s run the motor for 2 seconds.

- Copy this code to the Programming Canvas.
- Play the program and watch the motor.
### Controlling the Motors

```python
# Import the Motor class.
from mindstorms import Motor
# Initialize the motor connected to Port A.
motor = Motor('A')
# Rotate clockwise for 2 seconds at 75% speed.
motor.run_for_seconds(2.0, 75)
```

Modify your code to change the speed of the motor and the duration of its motion. For example:
### Controlling the Motors 1

```python
# Rotate counterclockwise for 6.5 seconds at 30% speed.
motor.run_for_seconds(6.5, -30)
```

Run Single Motor for Degrees
----------------------------

Let’s run the motor 360 degrees.

- Copy the code below to the Programming Canvas
- Play the program and watch the motor.
### Controlling the Motors 2

```python
# Import the Motor class.
from mindstorms import Motor
# Initialize the motor connected to Port A.
motor = Motor('A')
# Rotate the motor 360 degrees clockwise.
motor.run_for_degrees(360)
```

Modify your code to change the direction of the motor, using degrees of rotation. For example:
### Controlling the Motors 3

```python
# Run the motor 360 degrees clockwise, at 30% speed.
motor.run_for_degrees(-360, 30)
```

Run Single Motor to Position
----------------------------

Let’s bring the motor to the 0-degree position from whichever position it’s currently in. Its position is indicated by the marker on the motor.

- Copy this code to the Programming Canvas.
- Play the program and watch the motor.
### Controlling the Motors 4

```python
# Import the Motor class.
from mindstorms import Motor
from mindstorms.control import wait_for_seconds
# Initialize the motor connected to Port A.
motor = Motor('A')
# Run the motor to position “0,” aligning the markers.
motor.run_to_position(0, 'shortest path', 75)
```

Change your code to make the motor stop in different positions.
### Controlling the Motors 5

```python
# Run the motor to different positions, at different speeds.
wait_for_seconds(1)
motor.run_to_position(0, 'shortest path', 30)
wait_for_seconds(1)
motor.run_to_position(90, 'clockwise', 100)
```

Challenge
---------

Create a short program to run two motors according to a beat, something like both motors in one direction, both in the other direction, one motor in opposite direction of the other, and more!
Use the functions you’ve learned so far.
# Using the Color Sensor
What You Will Need
------------------

Connect a Color Sensor to Port C and two motors to Ports A and B. 

Yellow or Red?
--------------

Let’s use the Color Sensor to control the motors.

- Copy this code to the Programming Canvas.
- Play the program. Present a red beam or a yellow beam to the Color Sensor, then watch the motors.
### Using the Color Sensor

```python
from mindstorms import ColorSensor, Motor
from mindstorms.control import Timer
# Initialize the Color Sensor, two motors, and a timer.
color_sensor = ColorSensor('C')
motor_a = Motor('A')
motor_b = Motor('B')
timer = Timer()
# Present each colored beam to the Color Sensor and observe what happens.
# It will detect colors for 30 seconds.
while timer.now() < 30:
    color = color_sensor.wait_for_new_color()
    if color == 'red':
        motor_a.run_for_rotations(1)
    elif color == 'yellow':
        motor_b.run_for_rotations(1)
```

Change your code to explore another interaction with the sensor.
### Using the Color Sensor 1

```python
# This will use the reflected value of the colors to set the power of the motors.
# Yellow is approximately 80% and red approximately 60%.
while True:
    color = color_sensor.get_color()
    percentage = color_sensor.get_reflected_light()
    if color == 'red':
        motor_a.start_at_power(percentage)
    elif color == 'yellow':
        motor_b.start_at_power(percentage)
    else:
        motor_a.stop()
        motor_b.stop()
```

# Using the Distance Sensor
What You Will Need
------------------

Connect a Distance Sensor to Port D and a motor to Port A. 

Closer or Farther
-----------------

Let’s use the Distance Sensor to control the motor.

- Copy this code to the Programming Canvas.
- Play the program and wave your hand over the Distance Sensor.
### Using the Distance Sensor

```python
from mindstorms import DistanceSensor, Motor
# Initialize the Distance Sensor and motor.
distance_sensor = DistanceSensor('D')
motor = Motor('A')
# Move your hand slowly toward and away from the Distance Sensor.
while True:
    distance_sensor.wait_for_distance_farther_than(20, 'cm')
    motor.start()
    distance_sensor.wait_for_distance_closer_than(20, 'cm')
    motor.stop()
```

Change your code to explore another interaction with the sensor.
### Using the Distance Sensor 1

```python
# Move your hand slowly toward and away from the Distance Sensor.
# The motor speed will change based on the distance detected.
while True:
    percentage = distance_sensor.get_distance_percentage()
    if percentage is not None:
        motor.start(100 - percentage)
    else:
        motor.stop()
```

# Using the Motion Sensor
What You Will Need
------------------

You will only need the Hub, which you will hold and tilt. 

Detect the Position
-------------------

Let us control the Light Matrix using the Hub’s Motion Sensor.

- Copy this code to the Programming Canvas.
- Play the program and tilt the Hub up and down.
### Using the Motion Sensor

```python
# Import the MSHub and App classes.
from mindstorms import MSHub, App
# Initialize the MSHub and the App.
hub = MSHub()
app = App()
while True:
    orientation = hub.motion_sensor.wait_for_new_orientation()
    if orientation == 'front':
        hub.light_matrix.show_image('ASLEEP')
        app.start_sound('Snoring')
    elif orientation == 'up':
        hub.light_matrix.show_image('HAPPY')
        app.start_sound('Triumph')
```

Change your code to explore another interaction with the sensor. Tilt your Hub in the pitch axis to see what is happening.
### Using the Motion Sensor 1

```python
while True:
    angle = abs(hub.motion_sensor.get_pitch_angle()) * 2
    hub.light_matrix.show_image('HAPPY', angle)
```

Challenge
---------

Use the Motion Sensor to create a musical instrument that can modulate different sounds.
# Driving
What You Will Need
------------------

You can use Tricky or build a simple Driving Base by attaching two motors to the Hub, facing in opposite directions. Connect some wheels, and you’re ready to go! 

Move Forward-Backward
---------------------

Let’s program your Driving Base to move in straight lines.

- Copy this code to the Programming Canvas.
- Play the program! Make sure you have enough space for your Driving Base to move.
### Driving

```python
from mindstorms import MotorPair
# Initialize the motor pair.
motor_pair = MotorPair('A', 'B')
# Initialize the default speed.
motor_pair.set_default_speed(50)
# Move in one direction for 2 seconds.
motor_pair.move(2, 'seconds')
```

Use this code to change your Driving Base’s movement.
### Driving 1

```python
# Move in the other direction for 2 seconds.
motor_pair.set_default_speed(-50)
motor_pair.move(2, 'seconds')
```

Rotate a Driving Base (Point Turn)
----------------------------------
You can't just drive your Driving Base straight forever! You need to learn how to turn. Let us try what is called a “point turn”. It will turn the Driving Base on a single point.

- Copy this code to the Programming Canvas.
- Play the program! Make sure you have enough space for your Driving Base to move.
### Driving 2

```python
from mindstorms import MotorPair
# Initialize the motor pair.
motor_pair = MotorPair('A', 'B')
# Turn in one direction for 10 centimeters.
motor_pair.move_tank(10, 'cm', left_speed=75, right_speed=-75)
```

Use this code to change your Driving Base’s movement.
### Driving 3

```python
# Move in the other direction for one rotation.
motor_pair.move_tank(1, 'rotations', left_speed=-50, right_speed=50)
```

Challenge
---------

Here is a classic! Program your Driving Base to drive in a square using the functions you have just learned.
# More Python Basics
As a text-based programming language, Python relies on some principles that are worth further explanation.

- Flow Execution
- Data Types
- Errors

## Flow Execution
Remember that Python code is executed line-by-line. This is called the “flow of the execution.” 
There are different ways to modify that flow. For example, you can pause the execution of the program by using the different wait functions of the libraries. The program will be on pause until the event the function is waiting for happen.

## If/Elif/Else
“if/elif/else” allows you to modify the program’s flow of execution. The "if/elif/else" are conditional statements which can make the program execute or not a specified set of code based on a particular condition. Effective use of the “if/elif/else” statements is dependent on the ability to write and use good conditional statements.
"If/elif/else" statements can only have one if statement, multiple or none elif statement and one or none else statement. The program will first check whether the specified if condition is True or False. If True, it will execute the set of code placed within the if statement, otherwise the program can do 3 different things based on how your "if/elif/else" statement is made:

- Check the next elif statement if present
- Execute the set of code of the else statement, if present and all other elif condition were False or no elif statement is present.
- Continue its execution 

To indicate what goes in the body of the statement, you must indent the text.
### ifelse

```python
from mindstorms import MSHub, ColorSensor
from random import randint

hub = MSHub()

# Create a random number between 1 and 10
random_number = randint(1, 10)
# Check if the random number is greater than 5, less than 5 or equal to 5
if random_number > 5 :
    hub.light_matrix.write( 'Random number > 5')
elif random_number < 5:
    hub.light_matrix.write( 'Random number < 5')
else :
    hub.light_matrix.write( 'Random number = 5')


```

## While Loop
The while loop is used to repeat a set of code. It is used with a condition. The loop will repeat itself until the condition is False. 
In Python, we often use the <code>while True:</code> loop, which means that the loop repeat indefinitely because the condition is always True.
To indicate what goes in the body of the loop, you must indent the text.
### while

```python
from mindstorms import MSHub

hub = MSHub()

# The while loop update the light matrix brightness for as long as the code run
while True:
    pitch = hub.motion_sensor.get_pitch_angle() + 10
    hub.light_matrix.show_image('TARGET', pitch)
```

## For Loop
The for loop is used to repeat a set of code. The for loop repeats itself for a fixed number of times. For loops are used to go through a sequence of value in order. For example you can have the for loop repeat for a fix number by using the `range() function or can go through all the items of a list or all the character of a text.
To indicate what goes in the body of the loop, you must indent the text.
### for

```python
from mindstorms import MSHub
from mindstorms.control import wait_for_seconds

hub = MSHub()

# the For loop goes through all the character of the Mindstorms text
for character in 'Mindstorms' :
    hub.light_matrix.write(character)
    wait_for_seconds(0.8)
```

## Data Types
When using a text-based programming language, you’ll have to experiment with different types of values. In the beginning, you’ll mostly use integer, float, string, boolean and lists.
- Integer : positive or negative whole number, including 0.
### More Python Basics

```python
my_integer = 7
print(my_integer)
```

- Float: A positive or negative number with decimals.
### More Python Basics 1

```python
my_float = 7.0
print(my_float)
```

- String: A text composed of at least one character. the text must be surrounded by single quote ' or double quote " to be recognized as such by your program.
### More Python Basics 2

```python
my_string = 'Hello World'
print(my_string)
```

- Lists: Multiple values bundled together, with each value accessible via an index. The index starts at 0 and needs to be specified in between brackets [ ].
### More Python Basics 3

```python
my_list = [1,2,3]
print(my_list[1])
```

Boolean: Boolean can only take one of two possible values: True or False.
## Class, Objects, Methods, Proprieties
Python is an object-oriented programming language.

Here’s how it works:
- In the MINDSTORMS library, we’ve defined the electronic components that you’re able to program. These have been grouped into **classes**. An example of this is the MSHub Class, which defines everything you can do with the MINDSTORMS Hub.
<code>from mindstorms import MSHub</code>
- To use a class, you have to make a copy of it. The action of making a copy is referred to as “making an Object.” It’s done by initializing a component:
<code>my_own_hub_object = MSHub()</code>
- Now that you’ve made a copy (i.e., object ) of a class, you can do lots of “things “with it. These “things” are referred to as methods, and sometimes as functions. Methods sometimes have parameters, and sometimes they don’t. For example:
### More Python Basics 4

```python
# The method show_image() has a parameter called 'HAPPY.'
my_own_hub_object.light_matrix.show_image('HAPPY')
# The method stop() has no parameter.
motor.stop()
```

## Errors

You can sometimes makes some mistakes when writing your program, do not worry, this happens even to the best programmers!

Python can recognize these errors and will indicate where and what kind of error it has detected.
The detected errors and their location will be shown to you in the console when you play your program.
Here is a list of the most common errors you can make:

SyntaxError:
A SyntaxError occurs when you did not follow the Python language syntax in your program. For example it can be that you forgot a colon : in an while loop or a if statement.

ValueError:
A ValueError happens when you specify a value that is not allowed by a function parameter. For example, if a function parameter only accepts a value between a range 0-100 and you specify a value of 101.

TypeError:
A TypeError occurs when you specify a different type of value than the one of a function parameter. For example, if a function parameter is of integer type and you specify a string or float or boolean. 

NameError:
A NameError occurs when Python does not recognize the name of a function or a variable. For example, you might have written the name of a function or a variable wrong, or forgot to create a variable before using it in a function call or forgot to include the quote around a string.

IndexError:
An IndexError occurs when you specify an index for a list that is out of the list range. For example, if you have a list with 3 items the index goes from 0 to 2, any number you specify outside that range generates the IndexError.

IndentationError:
An IndentationError occurs when you do not respect the indentation in your program. For example, you forgot to indent the set of code of an if statement, a while or for loop or a function declaration.

ImportError:
An ImportError occurs when you import a module that is not recognized by Python. For example, if you import a module with the wrong name.

RuntimeError:
A RuntimeError occurs when you don't attribute the right port for a motor or sensor or they are not connected to that specified port. For example, if you attribute the port A to a motor but this motor is physically attached to another port or it is a sensor connected to the port B instead of a motor.
# Word Block Translator
These are the most common Word Blocks translated into MINDSTORMS Python. 

**Beep Sound**
### Word Block Translator

```python
hub.speaker.beep(60, 0.2)
```

**Play Sound**
### Word Block Translator 1

```python
app.play_sound('Cat Meow 1')
```

**Light Matrix**
### Word Block Translator 2

```python
hub.light_matrix.show_image('HAPPY')
wait_for_seconds(2)
hub.light_matrix.off()
```

**Single Motor On for Seconds**
### Word Block Translator 3

```python
motor = Motor('A')
motor.run_for_seconds(1, 75)
```

**Multiple Motor On for Rotations**
### Word Block Translator 4

```python
motor_pair = MotorPair('A', 'E')
motor_pair.move_tank(1, 'rotations', -75, 75)
```

**Drive In Straight Line (Driving Base)**
### Word Block Translator 5

```python
motor_pair = MotorPair('A', 'B')
motor_pair.set_default_speed(50)
motor_pair.move(10, 'cm')
```

**Wait for 2 Seconds**
### Word Block Translator 6

```python
wait_for_seconds(2)
```

**Wait for Distance Sensor**
### Word Block Translator 7

```python
distance_sensor = DistanceSensor('D')
distance_sensor.wait_for_distance_closer_than(15, 'cm')
```

**Repeat 10 Times**
### Word Block Translator 8

```python
for count in range(10):
    hub.light_matrix.write(count)
    wait_for_seconds(1)
```

**If... Else**
### Word Block Translator 9

```python
color_sensor = ColorSensor('A')
color = color_sensor.wait_for_new_color()
if color == 'yellow':
    print('Yellow')
else:
    print('Not Yellow')
```

**A Program**
### Word Block Translator 10

```python
from mindstorms import MSHub, MotorPair, DistanceSensor
from mindstorms.control import wait_for_seconds

hub = MSHub()
motor_pair = MotorPair('A', 'B')
distance_sensor = DistanceSensor('D')

distance_sensor.light_up_all()
motor_pair.set_default_speed(80)
hub.light_matrix.show_image('GO_RIGHT')
wait_for_seconds(2)
hub.light_matrix.off()
motor_pair.move(10, 'cm')
```

Libraries
---------


App
# App
This is the App Library, you can use this library to command the Mindstorms App to play sounds through your device (ie. Smartphone, Tablet and computer). This is how you initialize it:
### App

```python
from mindstorms import App
# Initialize the app.
app = App()
```

## Actions
Plays a sound from your device (i.e., smartphone, tablet or computer). The program will not continue until the specified sound has finished playing. If the specified sound name is not found, no sound is played and the program continue immediately to the next line.
### play_sound()

```python
from mindstorms import App

app = App()

app.play_sound('Cat Meow 1')
```

```python
    def play_sound(self, name: str, volume: int = 100):
        """Plays a sound from your device (i.e., smartphone, tablet or computer). The program will not continue until the specified sound has finished playing. If the specified sound name is not found, no sound is played and the program continue immediately to the next line.Plays a sound from your device (i.e., smartphone, tablet or computer). The program will not continue until the specified sound has finished playing. If the specified sound name is not found, no sound is played and the program continue immediately to the next line.

        :param name: The name of the sound to be played.
        :param volume: The volume at which the sound will be played.
        """
        assert name in ['Alert', 'Applause 1', 'Applause 2', 'Applause 3', 'Baa', 'Bang 1', 'Bang 2', 'Basketball Bounce', 'Big Boing', 'Bird', 'Bite', 'Boat Horn 1', 'Boat Horn 2', 'Bonk', 'Boom Cloud', 'Boop Bing Bop', 'Bowling Strike', 'Burp 1', 'Burp 2', 'Burp 3', 'Car Accelerate 1', 'Car Accelerating 2', 'Car Horn', 'Car Idle', 'Car Reverse', 'Car Skid 1', 'Car Skid 2', 'Car Vroom', 'Cat Angry', 'Cat Happy', 'Cat Hiss', 'Cat Meow 1', 'Cat Meow 2', 'Cat Meow 3', 'Cat Purring', 'Cat Whining', 'Chatter', 'Chirp', 'Clang', 'Clock Ticking', 'Clown Honk 1', 'Clown Honk 2', 'Clown Honk 3', 'Coin', 'Collect', ' Connect', ' Crank', ' Crazy Laugh', ' Croak', ' Crowd Gasp', ' Crunch', ' Cuckoo', ' Cymbal Crash', ' Disconnect', ' Dog Bark 1', ' Dog Bark 2', ' Dog Bark 3', ' Dog Whining 1', ' Dog Whining 2', ' Doorbell 1', ' Doorbell 2', ' Doorbell 3', ' Door Closing', ' Door Creek 1', ' Door Creek 2', ' Door Handle', ' Door Knock', ' Door Slam 1', ' Door Slam 2', ' Drum Roll', ' Dun Dun Dunnn', ' Emotional Piano', ' Fart 1', ' Fart 2', ' Fart 3', ' Footsteps', ' Gallop', ' Glass Breaking', ' Glug', ' Goal Cheer', ' Gong', ' Growl', ' Grunt', ' Hammer Hit', ' Head Shake', ' High Whoosh', ' Jump', ' Jungle Frogs', ' Laser 1', ' Laser 2', ' Laser 3', ' Laughing Baby 1', ' Laughing Baby 2', ' Laughing Boy', ' Laughing Crowd 1', ' Laughing Crowd 2', ' Laughing Girl', ' Laughing Male', ' Lose', ' Low Boing', ' Low Squeak', ' Low Whoosh', ' Magic Spell', ' Male Jump 1', ' Male Jump 2', ' Moo', ' Ocean Wave', ' Oops', ' Orchestra Tuning', ' Party Blower', ' Pew', ' Ping Pong Hit', ' Plane Flying By', ' Plane Motor Running', ' Plane Starting', ' Pluck', ' Police Siren 1', ' Police Siren 2', ' Police Siren 3', ' Punch', ' Rain', ' Ricochet', ' Rimshot', ' Ring Tone', ' Rip', ' Robot 1', ' Robot 2', ' Robot 3', ' Rocket Explosion Rumble', ' Rooster', ' Scrambling Feet', ' Screech', ' Seagulls', ' Service Announcement', ' Sewing Machine', ' Ship Bell', ' Siren Whistle', ' Skid', ' Slide Whistle 1', ' Slide Whistle 2', ' Sneaker Squeak', ' Snoring', ' Snort', ' Space Ambience', ' Space Flyby', ' Space Noise', ' Splash', ' Sport Whistle 1', ' Sport Whistle 2', ' Squeaky Toy', ' Squish Pop', ' Suction Cup', ' Tada', ' Telephone Ring 2', ' Telephone Ring', ' Teleport 2', ' Teleport 3', ' Teleport', ' Tennis Hit', ' Thunder Storm', ' Toliet Flush', ' Toy Honk', ' Toy Zing', ' Traffic', ' Train Breaks', ' Train Horn 1', ' Train Horn 2', ' Train Horn 3', ' Train On Tracks', ' Train Signal 1', ' Train Signal 2', ' Train Start', ' Train Whistle', ' Triumph', ' Tropical Birds', ' Wand', ' Water Drop', ' Whistle Thump', ' Whiz 1', ' Whiz 2', ' Window Breaks', ' Win', ' Wobble', ' Wood Tap', ' Zip']
        assert 0 <= volume <= 100
```


Starts playing a sound from your device (i.e., tablet or computer). The program will not wait for the sound to finish playing before proceeding to the next command. If a sound with the specified name is not found, nothing will happen.
### start_sound()

```python
from mindstorms import App

app = App()

app.start_sound('Cat Meow 1')
```

```python
    def start_sound(self, name: str, volume: int = 100):
        """Starts playing a sound from your device (i.e., tablet or computer). The program will not wait for the sound to finish playing before proceeding to the next command. If a sound with the specified name is not found, nothing will happen.Starts playing a sound from your device (i.e., tablet or computer). The program will not wait for the sound to finish playing before proceeding to the next command. If a sound with the specified name is not found, nothing will happen.

        :param name: The name of the sound to be played.
        :param volume: The volume at which the sound will be played
        """
        assert name in ['Alert', 'Applause 1', 'Applause 2', 'Applause 3', 'Baa', 'Bang 1', 'Bang 2', 'Basketball Bounce', 'Big Boing', 'Bird', 'Bite', 'Boat Horn 1', 'Boat Horn 2', 'Bonk', 'Boom Cloud', 'Boop Bing Bop', 'Bowling Strike', 'Burp 1', 'Burp 2', 'Burp 3', 'Car Accelerate 1', 'Car Accelerating 2', 'Car Horn', 'Car Idle', 'Car Reverse', 'Car Skid 1', 'Car Skid 2', 'Car Vroom', 'Cat Angry', 'Cat Happy', 'Cat Hiss', 'Cat Meow 1', 'Cat Meow 2', 'Cat Meow 3', 'Cat Purring', 'Cat Whining', 'Chatter', 'Chirp', 'Clang', 'Clock Ticking', 'Clown Honk 1', 'Clown Honk 2', 'Clown Honk 3', 'Coin', 'Collect', ' Connect', ' Crank', ' Crazy Laugh', ' Croak', ' Crowd Gasp', ' Crunch', ' Cuckoo', ' Cymbal Crash', ' Disconnect', ' Dog Bark 1', ' Dog Bark 2', ' Dog Bark 3', ' Dog Whining 1', ' Dog Whining 2', ' Doorbell 1', ' Doorbell 2', ' Doorbell 3', ' Door Closing', ' Door Creek 1', ' Door Creek 2', ' Door Handle', ' Door Knock', ' Door Slam 1', ' Door Slam 2', ' Drum Roll', ' Dun Dun Dunnn', ' Emotional Piano', ' Fart 1', ' Fart 2', ' Fart 3', ' Footsteps', ' Gallop', ' Glass Breaking', ' Glug', ' Goal Cheer', ' Gong', ' Growl', ' Grunt', ' Hammer Hit', ' Head Shake', ' High Whoosh', ' Jump', ' Jungle Frogs', ' Laser 1', ' Laser 2', ' Laser 3', ' Laughing Baby 1', ' Laughing Baby 2', ' Laughing Boy', ' Laughing Crowd 1', ' Laughing Crowd 2', ' Laughing Girl', ' Laughing Male', ' Lose', ' Low Boing', ' Low Squeak', ' Low Whoosh', ' Magic Spell', ' Male Jump 1', ' Male Jump 2', ' Moo', ' Ocean Wave', ' Oops', ' Orchestra Tuning', ' Party Blower', ' Pew', ' Ping Pong Hit', ' Plane Flying By', ' Plane Motor Running', ' Plane Starting', ' Pluck', ' Police Siren 1', ' Police Siren 2', ' Police Siren 3', ' Punch', ' Rain', ' Ricochet', ' Rimshot', ' Ring Tone', ' Rip', ' Robot 1', ' Robot 2', ' Robot 3', ' Rocket Explosion Rumble', ' Rooster', ' Scrambling Feet', ' Screech', ' Seagulls', ' Service Announcement', ' Sewing Machine', ' Ship Bell', ' Siren Whistle', ' Skid', ' Slide Whistle 1', ' Slide Whistle 2', ' Sneaker Squeak', ' Snoring', ' Snort', ' Space Ambience', ' Space Flyby', ' Space Noise', ' Splash', ' Sport Whistle 1', ' Sport Whistle 2', ' Squeaky Toy', ' Squish Pop', ' Suction Cup', ' Tada', ' Telephone Ring 2', ' Telephone Ring', ' Teleport 2', ' Teleport 3', ' Teleport', ' Tennis Hit', ' Thunder Storm', ' Toliet Flush', ' Toy Honk', ' Toy Zing', ' Traffic', ' Train Breaks', ' Train Horn 1', ' Train Horn 2', ' Train Horn 3', ' Train On Tracks', ' Train Signal 1', ' Train Signal 2', ' Train Start', ' Train Whistle', ' Triumph', ' Tropical Birds', ' Wand', ' Water Drop', ' Whistle Thump', ' Whiz 1', ' Whiz 2', ' Window Breaks', ' Win', ' Wobble', ' Wood Tap', ' Zip']
        assert 0 <= volume <= 100
```


Stops any sound that is playing in the App.
### stop_sound()

```python
from mindstorms import App

app = App()

app.start_sound('Cat Meow 1')
wait_for_seconds(0.5)
app.stop_sound()
```

```python
    def stop_sound(self):
        """Stops any sound that is playing in the App.
        """
        pass
```


Hub
# MSHub
This is the MSHub library. The Hub is divided into six components, each with its specific functionalities. To use the Hub and its components, you must first initialize it.
### MSHub

```python
from mindstorms import MSHub

# Initialize the Hub.
hub = MSHub()
```

## Constants

# Constants
## MSHub.left_button
The Left Button on the Hub.
### Constants

```python
from mindstorms import MSHub

hub = MSHub()

hub.left_button.wait_until_pressed()
```

## MSHub.right_button
The Right Button on the Hub.
### Constants 1

```python
from mindstorms import MSHub

hub = MSHub()

hub.right_button.wait_until_pressed()
```

## MSHub.speaker
The speaker inside the Hub.
### Constants 2

```python
from mindstorms import MSHub

hub = MSHub()

hub.speaker.beep()
```

## MSHub.light_matrix
The Light Matrix on the Hub.
### Constants 3

```python
from mindstorms import MSHub

hub = MSHub()

hub.light_matrix.off()
```

## MSHub.status_light
The Brick Status Light on the Hub’s Center Button.
### Constants 4

```python
from mindstorms import MSHub

hub = MSHub()

hub.status_light.on('blue')
```

## MSHub.motion_sensor
The Motion Sensor inside the Hub.
### Constants 5

```python
from mindstorms import MSHub

hub = MSHub()

yaw = hub.motion_sensor.get_yaw_angle()
```

## MSHub.PORT_A
The Port that is labeled "A" on the Hub. 
## MSHub.PORT_B
The Port that is labeled "B" on the Hub. 
## MSHub.PORT_C
The Port that is labeled "C" on the Hub. 
## MSHub.PORT_D
The Port that is labeled "D" on the Hub. 
## MSHub.PORT_E
The Port that is labeled "E" on the Hub. 
## MSHub.PORT_F
The Port that is labeled "F" on the Hub.
# Buttons
This is the buttons components part of the Hub. The functions below use the state of the left or right button, meaning whether they are pressed or not. You can use these functions to control the flow of your program. To select one button or the other you have to use the attribute `.left_button` or `.right_button`.

## Events
Waits until the button is pressed.
### wait_until_pressed()

```python
from mindstorms import MSHub

hub = MSHub()
# Beep every time the Left Button is pressed.
while True:
    hub.left_button.wait_until_pressed()
    hub.speaker.start_beep()
    hub.left_button.wait_until_released()
    hub.speaker.stop()
```

```python
    def wait_until_pressed(self):
        """Waits until the button is pressed.
        """
        pass
```


Waits until the button is released.
### wait_until_released()

```python
from mindstorms import MSHub

hub = MSHub()
# Beep every time the Left Button is pressed.
while True:
    hub.left_button.wait_until_pressed()
    hub.speaker.start_beep()
    hub.left_button.wait_until_released()
    hub.speaker.stop()
```

```python
    def wait_until_released(self):
        """Waits until the button is released.
        """
        pass
```


Checks if the button was pressed.
### was_pressed()

```python
from mindstorms import MSHub
from mindstorms.control import wait_for_seconds

hub = MSHub()

while True:
    wait_for_seconds(3)
    if hub.left_button.was_pressed():
        # Put your own code here
        hub.speaker.beep()
```

```python
    def was_pressed(self):
        """Checks if the button was pressed.
        """
        pass
```


## Measurements
Checks if the button is pressed.
### is_pressed()

```python
from mindstorms import MSHub

hub = MSHub()

if hub.left_button.is_pressed():
    # Do something.
        hub.speaker.beep()
```

```python
    def is_pressed(self):
        """Checks if the button is pressed.
        """
        pass
```


Checks if the button is released.
### is_released()

```python
from mindstorms import MSHub

hub = MSHub()

if hub.left_button.is_released():
   # Beep if left button is released
   hub.speaker.beep()
```

```python
    def is_released(self):
        """Checks if the button is released.
        """
        pass
```


# Status Light
This is the status light component part of the hub, the following functions let you change the color of the status light (central button light ring).

## Actions
Sets the color of the status light.
### on()

```python
from mindstorms import MSHub

hub = MSHub()

hub.status_light.on('blue')
```

```python
    def on(self, color: str = 'white'):
        """Sets the color of the status light.Sets the color of the status light.

        :param color: Illuminates the Hub’s Status Light in the specified color.
        """
        assert color in ['azure', 'black', 'blue', 'cyan', 'green', 'orange', 'pink', 'red', 'violet', 'white', 'yellow']
```


Turns off the light.
### off()

```python
from mindstorms import MSHub

hub = MSHub()

hub.status_light.off()
```

```python
    def off(self):
        """Turns off the light.
        """
        pass
```


# Light Matrix
This is the Light Matrix component part of the Hub, you can use the following functions to display pixels, images, numbers or text on the Light Matrix.

## Actions
Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.
### set_pixel()

```python
from mindstorms import MSHub

hub = MSHub()

hub.light_matrix.set_pixel(1, 4, 90)
```

```python
    def set_pixel(self, x: int, y: int, brightness: int = 100):
        """Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.

        :param x: Pixel position of the Light Matrix 5 columns, counting from the left.
        :param y: Pixel position of the Light Matrix 5 rows, counting from the top.
        :param brightness: Brightness of the specified pixel in percent
        """
        assert 0 <= x <= 4
        assert 0 <= y <= 4
        assert 0 <= brightness <= 100
```


Shows an image on the Light Matrix.
### show_image()

```python
from mindstorms import MSHub
from mindstorms.control import wait_for_seconds

hub = MSHub()

hub.light_matrix.show_image('HAPPY')
wait_for_seconds(5)
hub.light_matrix.show_image('ASLEEP')
```

```python
    def show_image(self, image: str, brightness: int = 100):
        """Shows an image on the Light Matrix.Shows an image on the Light Matrix.

        :param image: Name of the image.
        :param brightness: Brightness of the image in percent
        """
        assert image in ['ANGRY', 'ARROW_E', 'ARROW_N', 'ARROW_NE', 'ARROW_NW', 'ARROW_S', 'ARROW_SE', 'ARROW_SW', 'ARROW_W', 'ASLEEP', 'BUTTERFLY', 'CHESSBOARD', 'CLOCK1', 'CLOCK10', 'CLOCK11', 'CLOCK12', 'CLOCK2', 'CLOCK3', 'CLOCK4', 'CLOCK5', 'CLOCK6', 'CLOCK7', 'CLOCK8', 'CLOCK9', 'CONFUSED', 'COW', 'DIAMOND', 'DIAMOND_SMALL', 'DUCK', 'FABULOUS', 'GHOST', 'GIRAFFE', 'GO_RIGHT', 'GO_LEFT', 'GO_UP', 'GO_DOWN', 'HAPPY', 'HEART', 'HEART_SMALL', 'HOUSE', 'MEH', 'MUSIC_CROTCHET', 'MUSIC_QUAVER', 'MUSIC_QUAVERS', 'NO', 'PACMAN', 'PITCHFORK', 'RABBIT', 'ROLLERSKATE', 'SAD', 'SILLY', 'SKULL', 'SMILE', 'SNAKE', 'SQUARE', 'SQUARE_SMALL', 'STICKFIGURE', 'SURPRISED', 'SWORD', 'TARGET', 'TORTOISE', 'TRIANGLE', 'TRIANGLE_LEFT', 'TSHIRT', 'UMBRELLA', 'XMAS', 'YES']
        assert 0 <= brightness <= 100
```


Displays text on the Light Matrix, one letter at a time, scrolling from right to left. The program will not continue until all of the specified text have been displayed.
### write()

```python
from mindstorms import MSHub

hub = MSHub()

hub.light_matrix.write('Hello!')
# Show the number "1" on the Light Matrix.
hub.light_matrix.write('1')
```

```python
    def write(self, text: str):
        """Displays text on the Light Matrix, one letter at a time, scrolling from right to left. The program will not continue until all of the specified text have been displayed.Displays text on the Light Matrix, one letter at a time, scrolling from right to left. The program will not continue until all of the specified text have been displayed.

        :param text: Text to display. If a character is unknown, ? will be displayed instead.
        """
        pass
```


Turns off all the pixels (LEDs) of the Light Matrix.
### off()

```python
from mindstorms import MSHub
from mindstorms.control import wait_for_seconds

hub = MSHub()

hub.light_matrix.show_image('TARGET')
wait_for_seconds(3)
hub.light_matrix.off()
```

```python
    def off(self):
        """Turns off all the pixels (LEDs) of the Light Matrix.
        """
        pass
```


Show an array of pixels on the light matrix.
### show()

```python
from mindstorms import MSHub

hub = MSHub()

pixels = '99999:77777:55555:33333:11111'
hub.light_matrix.show(pixels)
```

```python
    def show(self, pixels: str):
        """Show an array of pixels on the light matrix.Show an array of pixels on the light matrix.

        :param pixels: Array of pixels to display on the light matrix.
        """
        assert 0 <= pixels <= 9
```


Plays an animation on the light matrix.

The program will not continue until the animation has finished playing.
### play_animation()

```python
from mindstorms import MSHub

hub = MSHub()

anim_countdown = [
   '09990:09000:09990:00090:09990',
   '09090:09090:09990:00090:00090',
   '09990:00090:09990:00090:09990',
   '09990:00090:09990:09000:09990',
   '00900:09900:00900:00900:09990',
   '99999:99999:99999:99999:99999'
]
hub.light_matrix.play_animation(anim_countdown, 10, 'fade out', True)
```

```python
    def play_animation(self, animation: str, fps: int = 2.5, effect: str = 'direct', clear: bool = False):
        """Plays an animation on the light matrix.
        
        The program will not continue until the animation has finished playing.Plays an animation on the light matrix.
        
        The program will not continue until the animation has finished playing.

        :param animation: The animation to be played. Animation should be composed of multiple strings separated by commas. Each string consists of 5 groups of 5 numbers from 0 to 9 separated by ':'. Each group of 5 numbers represents a line of pixels of the light matrix with the first number of the first group representing the first left pixel of the first top line and the value representing the brightness 0 being off and 9 being 100% brightness.
        :param fps: The speed at which the animation is played, i.e. animation frames displayed per second.
        :param effect: The effect that is applied to the animation.
        :param clear: Whether or not the animation should clear the display upon completion.
        """
        assert 1 <= fps <= 20
        assert effect in ['direct', 'overlay', 'slide right', 'slide left', 'fade in', 'fade out']
        assert isinstance(clear, bool)
```


Starts an animation on the light matrix.

The program will not wait for the animation to finish playing before proceeding to the next command.
### start_animation()

```python
from mindstorms import MSHub

hub = MSHub()

anim_countdown = [
   '09990:09000:09990:00090:09990',
   '09090:09090:09990:00090:00090',
   '09990:00090:09990:00090:09990',
   '09990:00090:09990:09000:09990',
   '00900:09900:00900:00900:09990',
   '99999:99999:99999:99999:99999'
]
hub.light_matrix.start_animation(anim_countdown, 10, False, 'fade out', True)
```

```python
    def start_animation(self, animation: str, fps: int = 2.5, loop: bool = False, effect: str = 'direct', clear: bool = False):
        """Starts an animation on the light matrix.
        
        The program will not wait for the animation to finish playing before proceeding to the next command.Starts an animation on the light matrix.
        
        The program will not wait for the animation to finish playing before proceeding to the next command.

        :param animation: The animation to be played. Animation should be composed of multiple strings separated by commas. Each string consists of 5 groups of 5 numbers from 0 to 9 separated by ':'. Each group of 5 numbers represents a line of pixels of the light matrix with the first number of the first group representing the first left pixel of the first top line and the value representing the brightness 0 being off and 9 being 100% brightness.
        :param fps: The speed at which the animation is played, i.e. animation frames displayed per second.
        :param loop: Whether or not the animation should loop.
        :param effect: The effect that is applied to the animation.
        :param clear: Whether or not the animation should clear the display upon completion.
        """
        assert 1 <= fps <= 20
        assert isinstance(loop, bool)
        assert effect in ['direct', 'overlay', 'slide right', 'slide left', 'fade in', 'fade out']
        assert isinstance(clear, bool)
```


Sets the orientation of the light matrix.
### set_orientation()

```python
from mindstorms import MSHub

hub = MSHub()

hub.light_matrix.write('LEGO')
hub.light_matrix.set_orientation('upside down')
hub.light_matrix.write('MINDSTORMS')
```

```python
    def set_orientation(self, orientation: str = 'upright'):
        """Sets the orientation of the light matrix.Sets the orientation of the light matrix.

        :param orientation: The orientation the light matrix will be oriented towards.
        """
        assert orientation in ['upright', 'left', 'upside down', 'right']
```


Rotates the light matrix to the select direction
### rotate()

```python
from mindstorms import MSHub

hub = MSHub()

hub.light_matrix.write('LEGO')
hub.light_matrix.rotate('counterclockwise')
hub.light_matrix.write('MINDSTORMS')
```

```python
    def rotate(self, direction: str = 'clockwise'):
        """Rotates the light matrix to the select directionRotates the light matrix to the select direction

        :param direction: The direction set light matrix will be rotated. Rotating four times will put the light matrix in the same orientation it was before the rotations.
        """
        assert direction in ['clockwise', 'counterclockwise']
```


## Measurements
Gets the orientation of the light matrix.
### get_orientation()

```python
from mindstorms import MSHub

hub = MSHub()

hub.light_matrix.set_orientation("right")
orientation = hub.light_matrix.get_orientation()
print(orientation)
```

```python
    def get_orientation(self):
        """Gets the orientation of the light matrix.
        """
        pass
```


# Speaker
This is the Speaker component part of the Hub, you can use the functions below to play beeps on the speaker and adjust the volume.

## Actions
Plays a beep on the Hub's speaker at the specified note. Your program will not continue until the specified number of seconds has elapsed.
### beep()

```python
from mindstorms import MSHub

hub = MSHub()

# beep beep beep!

hub.speaker.beep(60, 0.5)
hub.speaker.beep(44, 0.5, 50)
hub.speaker.beep(123, 0.5, 100)
```

```python
    def beep(self, note: int = 60 (middle C note), seconds: float = 0.2, volume: int):
        """Plays a beep on the Hub's speaker at the specified note. Your program will not continue until the specified number of seconds has elapsed.Plays a beep on the Hub's speaker at the specified note. Your program will not continue until the specified number of seconds has elapsed.

        :param note: The MIDI note number.
        :param seconds: The duration of the beep in seconds.
        :param volume: The volume at which the sound will be played. Type: integer or float (positive or negative number, including 0) Values: 0 to 100% or None Default: None (indicating that current volume is used)
        """
        assert 44 <= note <= 123
        assert 0 <= volume <= 100
```


Starts playing a beep on the Hub's Speaker at the specified note. The beep will play until stop() is called or another beep is played on the Speaker.
### start_beep()

```python
from mindstorms import MSHub

hub = MSHub()

#Beep high-pitched for 3 seconds 
hub.speaker.start_beep(123, 100)
wait_for_seconds(3)
hub.speaker.stop()
```

```python
    def start_beep(self, note: int = 60 (middle C note), volume: int):
        """Starts playing a beep on the Hub's Speaker at the specified note. The beep will play until stop() is called or another beep is played on the Speaker.Starts playing a beep on the Hub's Speaker at the specified note. The beep will play until stop() is called or another beep is played on the Speaker.

        :param note: The MIDI note number.
        :param volume: The volume at which the sound will be played.
        """
        assert 44 <= note <= 123
        assert 0 <= volume <= 100
```


Stops any sound that is playing on the Hub's Speaker.
### stop()

```python
from mindstorms import MSHub

hub = MSHub()

hub.speaker.start_beep()
# Put your own code here
hub.speaker.stop()
```

```python
    def stop(self):
        """Stops any sound that is playing on the Hub's Speaker.
        """
        pass
```


Plays a sound from the hub speaker.
The program will not continue until the sound has finished playing.
### play_sound()

```python
from mindstorms import MSHub

hub = MSHub()

# Play the 'Damage' sound and wait for it to finish
hub.speaker.play_sound('Damage')
```

```python
    def play_sound(self, name: str, volume: int):
        """Plays a sound from the hub speaker.
        The program will not continue until the sound has finished playing.Plays a sound from the hub speaker.
        The program will not continue until the sound has finished playing.

        :param name: Name of the sound to play on Hub.
        :param volume: The volume at which the sound will be played.
        """
        assert name in ['1234', 'Activate', 'Affirmative', 'Bowling', 'Brick Eating', 'Celebrate', 'Chuckle', 'Countdown', 'Countdown Tick', 'Damage', 'Deactivate', 'Delivery', 'Dizzy', 'Error', 'Explosion', 'Exterminate', 'Fire', 'Goal', 'Goodbye', 'Grab', 'Hammer', 'Hello', 'Hi', 'Hi 5', 'Hit', 'Horn', 'Humming', 'Hydraulics Down', 'Hydraulics Up', 'Initialize', 'Kick', 'Laser', 'Laugh', 'Like', 'Mission Accomplished', 'No', 'Ouch', 'Ping', 'Play', 'Punch', 'Reverse', 'Revving', 'Sad', 'Scanning', 'Scared', 'Seek and Destroy', 'Shake', 'Shooting', 'Shut Down', 'Slam Dunk', 'Strike', 'Success Chime', 'Tadaa', 'Target Acquired', 'Target Destroyed', 'Whirl', 'Wow', 'Yes', 'Yipee', 'Yuck']
        assert 0 <= volume <= 100
```


Starts playing a sound from the Hub speaker.

The program will not wait for the sound to finish playing before proceeding to the next command.
### play_sound()

```python
from mindstorms import MSHub

hub = MSHub()

# Play the 'Damage' sound and wait for it to finish
hub.speaker.play_sound('Damage')
```

```python
    def start_sound(self, name: str, volume: int):
        """Starts playing a sound from the Hub speaker.
        
        The program will not wait for the sound to finish playing before proceeding to the next command.Starts playing a sound from the Hub speaker.
        
        The program will not wait for the sound to finish playing before proceeding to the next command.

        :param name: Name of the sound to play on Hub.
        :param volume: The volume at which the sound will be played.
        """
        assert name in ['1234', 'Activate', 'Affirmative', 'Bowling', 'Brick Eating', 'Celebrate', 'Chuckle', 'Countdown', 'Countdown Tick', 'Damage', 'Deactivate', 'Delivery', 'Dizzy', 'Error', 'Explosion', 'Exterminate', 'Fire', 'Goal', 'Goodbye', 'Grab', 'Hammer', 'Hello', 'Hi', 'Hi 5', 'Hit', 'Horn', 'Humming', 'Hydraulics Down', 'Hydraulics Up', 'Initialize', 'Kick', 'Laser', 'Laugh', 'Like', 'Mission Accomplished', 'No', 'Ouch', 'Ping', 'Play', 'Punch', 'Reverse', 'Revving', 'Sad', 'Scanning', 'Scared', 'Seek and Destroy', 'Shake', 'Shooting', 'Shut Down', 'Slam Dunk', 'Strike', 'Success Chime', 'Tadaa', 'Target Acquired', 'Target Destroyed', 'Whirl', 'Wow', 'Yes', 'Yipee', 'Yuck']
        assert 0 <= volume <= 100
```


## Measurements

Returns the value of the hub's Speaker volume.
### get_volume()

```python
from mindstorms import MSHub

hub = MSHub()
# Increase the volume of the Hub speaker by 10%.
hub.speaker.set_volume(hub.speaker.get_volume() + 10)
```

```python
    def get_volume(self):
        """Returns the value of the hub's Speaker volume.
        """
        pass
```


## Settings

Sets the Hub's Speaker volume. Not your device volume
### set_volume()

```python
from mindstorms import MSHub

hub = MSHub()
# Set the Hub speaker volume to 50%.
hub.speaker.set_volume(50)
```

```python
    def set_volume(self, volume: int = 100):
        """Sets the Hub's Speaker volume. Not your device volumeSets the Hub's Speaker volume. Not your device volume

        :param volume: The new volume in percent. If the specified volume is out of range, the nearest volume (i.e., 0 or 100) will be used instead.
        """
        assert 0 <= volume <= 100
```


# Motion Sensor
This is the Motion sensor component part of the Hub, the functions below helps you determine the Hub orientation as well as detect gestures.

## Events
Checks if the specified gesture has been detected by the Hub's Motion Sensor.
### was_gesture()

```python
from mindstorms import MSHub
from mindstorms.control import wait_for_seconds

hub = MSHub()

wait_for_seconds(5)
if hub.motion_sensor.was_gesture('shaken'):
    # The Hub has been shaken at least once within the last 5 seconds.
    hub.speaker.beep()
```

```python
    def was_gesture(self, gesture: str):
        """Checks if the specified gesture has been detected by the Hub's Motion Sensor.Checks if the specified gesture has been detected by the Hub's Motion Sensor.

        :param gesture: The name of the gesture.
        """
        assert gesture in ['shaken', 'tapped', 'doubletapped', 'falling']
```


Waits until a new gesture is detected.
### wait_for_new_gesture()

```python
from mindstorms import MSHub

hub = MSHub()

new_gesture = hub.motion_sensor.wait_for_new_gesture()
# comment1
hub.light_matrix.write(new_gesture)
```

```python
    def wait_for_new_gesture(self):
        """Waits until a new gesture is detected.
        """
        pass
```


Waits until the Hub’s orientation changes.
### wait_for_new_orientation()

```python
from mindstorms import MSHub

hub = MSHub()

new_orientation = hub.motion_sensor.wait_for_new_orientation()
# Write the new orientation on the hub's Light Matrix
hub.light_matrix.write(new_orientation)
```

```python
    def wait_for_new_orientation(self):
        """Waits until the Hub’s orientation changes.
        """
        pass
```


## Measurements
Returns the Hub's current orientation.
### get_orientation()

```python
from mindstorms import MSHub

hub = MSHub()

orientation = hub.motion_sensor.get_orientation()
# Write the orientation on the hub's Light Matrix
hub.light_matrix.write(orientation)
```

```python
    def get_orientation(self):
        """Returns the Hub's current orientation.
        """
        pass
```


Returns the most recently detected gesture.
### get_gesture()

```python
from mindstorms import MSHub

hub = MSHub()

wait_for_seconds(5)
gesture = hub.motion_sensor.get_gesture()
# Write the most recently detected gesture on the hub's Light Matrix
hub.light_matrix.write(gesture)
```

```python
    def get_gesture(self):
        """Returns the most recently detected gesture.
        """
        pass
```


Returns the Hub’s Pitch angle.
### get_pitch_angle()

```python
from mindstorms import MSHub

hub = MSHub()

while True:
    # Rotate your hub around the Pitch axis to see what happen
    pitch = hub.motion_sensor.get_pitch_angle()
    hub.speaker.set_volume(abs(pitch))
    hub.speaker.start_beep(70)
```

```python
    def get_pitch_angle(self):
        """Returns the Hub’s Pitch angle.
        """
        pass
```


Returns the Hub’s Roll angle.
### get_roll_angle()

```python
from mindstorms import MSHub

hub = MSHub()

while True:
    # Rotate your hub around the Roll axis to see what happen
    roll = hub.motion_sensor.get_roll_angle()
    hub.speaker.set_volume(abs(roll))
    hub.speaker.start_beep(80)
```

```python
    def get_roll_angle(self):
        """Returns the Hub’s Roll angle.
        """
        pass
```


Returns the Hub’s Yaw angle.
### get_yaw_angle()

```python
from mindstorms import MSHub

hub = MSHub()

hub.motion_sensor.reset_yaw_angle()
while True:
    # Do something.
    yaw = hub.motion_sensor.get_yaw_angle()
    hub.speaker.set_volume(abs(yaw))
    hub.speaker.start_beep(90)
```

```python
    def get_yaw_angle(self):
        """Returns the Hub’s Yaw angle.
        """
        pass
```


## Settings

Sets the Yaw angle to 0.
### reset_yaw_angle()

```python
from mindstorms import MSHub

hub = MSHub()

while True:
    # Rotate your hub around the Yaw axis to see what happen
    hub.motion_sensor.reset_yaw_angle()
    angle = hub.motion_sensor.get_yaw_angle()
    hub.ligth_matrix.write(angle)

```

```python
    def reset_yaw_angle(self):
        """Sets the Yaw angle to 0.
        """
        pass
```


Motors
# Single Motors
This is the Single Motor Library, you can use the following functions to rotate your motors or move them to a specific position. To use the motors, you must first initialize them.
### Single Motors

```python
from mindstorms import Motor
# Initialize the motor on port A
motor_a = Motor('A')
```

## Actions
Runs the motor to an absolute position.
### run_to_position()

```python
from mindstorms import Motor

motor_a = Motor('A')

# Run the motor to position 0 degrees, aligning the markers.

motor_a.run_to_position(175, 'clockwise', 75)
# Run the motor to position 0 degrees, aligning the markers.
motor_a.run_to_position(0)
```

```python
    def run_to_position(self, degrees: int, direction: str = 'shortest path', speed: int = None):
        """Runs the motor to an absolute position.Runs the motor to an absolute position.

        :param degrees: The new desired position.
        :param direction: The direction the motor should run. You can choose to rotate the motor in one direction or the other, or let the motor decide which direction makes its rotation shorter by choosing 'shortest path'
        :param speed: The desired motor's speed. If no value is specified, the speed set by `set_default_speed()` is used.
        """
        assert 0 <= degrees <= 359
        assert direction in ['shortest path', 'clockwise', 'counterclockwise']
        assert 0 <= speed <= 100
```


Runs the motor to a relative position of degrees counted. You can set the degrees count by using `set_degrees_counted()`.
### run_to_degrees_counted()

```python
from mindstorms import Motor
from mindstorms.control import wait_for_seconds

motor_a = Motor('A')

# Run the motor to 400 degrees counted at 50% speed.
motor_a.run_to_degrees_counted(400, 50)
# Run the motor to -600 degrees counted at maximum (100%) speed.
motor_a.run_to_degrees_counted(-600, 100)
# Comment 3
motor_a.run_to_degrees_counted(0)
```

```python
    def run_to_degrees_counted(self, degrees: int, speed: int = None):
        """Runs the motor to a relative position of degrees counted. You can set the degrees count by using `set_degrees_counted()`.Runs the motor to a relative position of degrees counted. You can set the degrees count by using `set_degrees_counted()`.

        :param degrees: The new desired degrees counted position.
        :param speed: The desired motor's speed. If no value is specified, the speed set by set_default_speed() is used.
        """
        assert 0 <= speed <= 100
```


Runs the motor for a specified number of degrees.
### run_for_degrees()

```python
from mindstorms import Motor

motor_a = Motor('A')

# Run the motor 90 degrees clockwise at 30% speed.
motor_a.run_for_degrees(90, 30)
# Run the motor 90 degrees counterclockwise at maximum (100%) speed.
motor_a.run_for_degrees(-90, 100)
# Run the motor 360 degrees clockwise at default speed.
motor_a.run_for_degrees(360)
```

```python
    def run_for_degrees(self, degrees: int, speed: int):
        """Runs the motor for a specified number of degrees.Runs the motor for a specified number of degrees.

        :param degrees: The number of degrees the motor should run. F.ex 360 degrees makes the motor run a full rotation
        :param speed: The desired motor’s speed. If no value is specified, the speed set by `set_default_speed()` is used.
        """
        assert -100 <= speed <= 100
```


Runs the motor for a specified number of rotations.
### run_for_rotations()

```python
from mindstorms import Motor

motor_a = Motor('A')
# Run the motor 0.25 rotations clockwise (90 degrees).
motor_a.run_for_rotations(0.25, 90)
# Run the motor 0.25 rotations counterclockwise (-90 degrees).
motor_a.run_for_rotations(-0.25, 10)
```

```python
    def run_for_rotations(self, rotations: float, speed: int = None):
        """Runs the motor for a specified number of rotations.Runs the motor for a specified number of rotations.

        :param rotations: The number of rotations the motor should run.
        :param speed: The desired motor’s speed. If no value is specified, the speed set by set_default_speed() is used.
        """
        assert -100 <= speed <= 100
```


Runs the motor for a specified number of seconds.
### run_for_seconds()

```python
from mindstorms import Motor

motor_a = Motor('A')
# Run the motor clockwise for half a second at 75% speed.
motor_a.run_for_seconds(0.5, 75)
# Run the motor counterclockwise for 3 seconds at 30% speed.
motor_a.run_for_seconds(3, -30)
```

```python
    def run_for_seconds(self, seconds: float, speed: int):
        """Runs the motor for a specified number of seconds.Runs the motor for a specified number of seconds.

        :param seconds: The number of seconds the motor should run.
        :param speed: The desired motor’s speed. If no value is specified, the speed set by `set_default_speed()` is used.
        """
        assert -100 <= speed <= 100
```


Starts running the motor at the specified speed. The motor will keep on running until you give it another motor command or your program ends.
### start()

```python
from mindstorms import MSHub, Motor

hub = MSHub()
motor_a = Motor('A')

motor_a.start(60)
# Press on the hub's left button when you want to stop the motor
hub.left_button.wait_until_pressed()
motor_a.stop()
```

```python
    def start(self, speed: int = None):
        """Starts running the motor at the specified speed. The motor will keep on running until you give it another motor command or your program ends.Starts running the motor at the specified speed. The motor will keep on running until you give it another motor command or your program ends.

        :param speed: The desired motor’s speed. If no value is specified, the speed set by `set_default_speed()` is used.
        """
        assert -100 <= speed <= 100
```


Starts running the motor at the specified power level. The motor will keep on running until you give it another motor command or your program ends.
### start_at_power

```python
from mindstorms import MSHub, Motor

hub = MSHub()
motor_a = Motor('A')

motor_a.start_at_power(50)
# Press on the Hub's left button when you want the motor to stop.
hub.left_button.wait_until_pressed()
motor_a.stop()
```

```python
    def start_at_power(self, power: int):
        """Starts running the motor at the specified power level. The motor will keep on running until you give it another motor command or your program ends.Starts running the motor at the specified power level. The motor will keep on running until you give it another motor command or your program ends.

        :param power: The desired motor's power.
        """
        assert -100 <= power <= 100
```


Stops the motor.
What the motor does after it stops depends on the action sets in `set_stop_action()`.
### stop()

```python
from mindstorms import MSHub, Motor

hub = MSHub()
motor = Motor('A')

motor.start()
# Press on the Hub's left button when you want the motor to stop.
hub.left_button.wait_until_pressed()
motor.stop()
```

```python
    def stop(self):
        """Stops the motor.
        What the motor does after it stops depends on the action sets in `set_stop_action()`.
        """
        pass
```


## Measurements

Returns the actual speed of the motor.
### get_speed()

```python
from mindstorms import MSHub, Motor

hub = MSHub()
motor_a = Motor('A')

motor_a.start()
hub.light_matrix.write('Speed =')
hub.light_matrix.write(motor_a.get_speed())
motor_a.stop()
```

```python
    def get_speed(self):
        """Returns the actual speed of the motor.
        """
        pass
```


Returns the actual absolute position of the motor.
### get_position()

```python
from mindstorms import MSHub, Motor

hub = MSHub()
motor_a = Motor('A')

motor_a.run_for_seconds(1, 100)
hub.light_matrix.write('Position =') 
hub.light_matrix.write(motor_a.get_position())
motor_a.stop()
```

```python
    def get_position(self):
        """Returns the actual absolute position of the motor.
        """
        pass
```


Returns the motor's relative position of degrees counted.
You can set the degrees count by using set_degrees_counted().
### get_degrees_counted()

```python
from mindstorms import MSHub, Motor

hub = MSHub()
motor_a = Motor('A')

motor_a.run_for_seconds(1, 100)
hub.light_matrix.write('degrees counted =') 
hub.light_matrix.write(motor_a.get_degrees_counted())
motor_a.stop()
```

```python
    def get_degrees_counted(self):
        """Returns the motor's relative position of degrees counted.
        You can set the degrees count by using set_degrees_counted().
        """
        pass
```


Returns the default motor speed.
### get_default_speed()

```python
from mindstorms import MSHub, Motor

hub = MSHub()
motor_a = Motor('A')

motor_a.set_default_speed(50)
motor_a.run_for_rotations(1, 100)
hub.light_matrix.write('default speed =') 
hub.light_matrix.write(motor_a.get_default_speed())
```

```python
    def get_default_speed(self):
        """Returns the default motor speed.
        """
        pass
```


## Events

Checks if the last motor command was interrupted.
### was_interrupted()

```python
from mindstorms import Motor

motor = Motor('A')

motor.run_for_rotations(2)
if motor.was_interrupted():
    # The motor did not complete two rotations.
    print('interrupted')
```

```python
    def was_interrupted(self):
        """Checks if the last motor command was interrupted.
        """
        pass
```


Checks if the motor was stalled.
### was_stalled()

```python
from mindstorms import MSHub, Motor

hub = MSHub()
motor_a = Motor('A')

motor_a.set_stall_detection(True)
motor_a.run_for_rotations(2)
if motor_a.was_stalled():
    # The motor did not complete two rotations.
    hub.light_matrix.write('stalled')
```

```python
    def was_stalled(self):
        """Checks if the motor was stalled.
        """
        pass
```


## Settings

Sets the degrees counted to the desired count.
```python
    def set_degrees_counted(self, degrees_counted: int):
        """Sets the degrees counted to the desired count.Sets the degrees counted to the desired count.

        :param degrees_counted: The new degrees counted count.
        """
        pass
```


Sets the default motor speed.
This is the default speed value used by the other motor functions when you do not specify a speed value. Setting the default speed does not affect the actual motor speed. This function should be used before another function that runs motors.
### set_default_speed()

```python
from mindstorms import Motor
from mindstorms.control import wait_for_seconds

motor_a = Motor('A')


motor_a.set_default_speed(30)
# The motor start running for 2 seconds at the default speed (30%)
motor_a.run_for_seconds(2)
# The motor start running at 85 speed
motor_a.start(85)
# The default speed is changed to 20%, not the actual motor speed
motor_a.set_default_speed(20)
wait_for_seconds(2)
motor_a.stop()
```

```python
    def set_default_speed(self, default_speed: int):
        """Sets the default motor speed.
        This is the default speed value used by the other motor functions when you do not specify a speed value. Setting the default speed does not affect the actual motor speed. This function should be used before another function that runs motors.Sets the default motor speed.
        This is the default speed value used by the other motor functions when you do not specify a speed value. Setting the default speed does not affect the actual motor speed. This function should be used before another function that runs motors.

        :param default_speed: The desired default speed.
        """
        assert -100 <= default_speed <= 100
```


Sets the default stop action the motor performs when it stops running.
Setting the default stop action does not affect the actual motor stop action. This functions should be used before another functions that run or stop motors.
### set_stop_action()

```python
from mindstorms import Motor

motor_a = Motor('A')

# The motor is free after it completely stops.
motor_a.set_stop_action('coast')
motor_a.run_for_seconds(1, 100)
# The motor keeps braking after it completely stops.
motor_a.set_stop_action('brake')
motor_a.run_for_seconds(1, 100)
# The motor holds its position after it completely stops.
motor_a.set_stop_action('hold')
motor_a.run_for_seconds(1, 100)
```

```python
    def set_stop_action(self, action: str = 'coast'):
        """Sets the default stop action the motor performs when it stops running.
        Setting the default stop action does not affect the actual motor stop action. This functions should be used before another functions that run or stop motors.Sets the default stop action the motor performs when it stops running.
        Setting the default stop action does not affect the actual motor stop action. This functions should be used before another functions that run or stop motors.

        :param action: The desired stop action.
        """
        assert action in ['coast', 'brake', 'hold']
```


Turns stall detection on or off. Stall detection senses when a motor has been blocked and can’t move. If stall detection has been enabled and a motor is blocked, the motor will be powered off after two seconds and the current motor command will be interrupted. If stall detection has been disabled, the motor will keep trying to run and programs will "get stuck" until the motor is no longer blocked. Stall detection is enabled by default.
### set_stall_detection()

```python
from mindstorms import Motor

motor = Motor('A')

motor.set_stall_detection(False)
motor.run_for_rotations(2)
# The program will never proceed to here if the motor is stalled.
```

```python
    def set_stall_detection(self, stop_when_stalled: bool = True):
        """Turns stall detection on or off. Stall detection senses when a motor has been blocked and can’t move. If stall detection has been enabled and a motor is blocked, the motor will be powered off after two seconds and the current motor command will be interrupted. If stall detection has been disabled, the motor will keep trying to run and programs will "get stuck" until the motor is no longer blocked. Stall detection is enabled by default.Turns stall detection on or off. Stall detection senses when a motor has been blocked and can’t move. If stall detection has been enabled and a motor is blocked, the motor will be powered off after two seconds and the current motor command will be interrupted. If stall detection has been disabled, the motor will keep trying to run and programs will "get stuck" until the motor is no longer blocked. Stall detection is enabled by default.

        :param stop_when_stalled: Choose "True" to enable stall detection or "False" to disable it.
        """
        pass
```


# Motor Pairs
This is the Motor Pair Library, you can use the functions here to control 2 motors simultaneously in opposite directions. To be able to use a Motor Pair, you must initialize both motors.
### Motor Pairs

```python
from mindstorms import MotorPair

# Switch the motors Port sequence to change the motor's direction
motor_pair_ba = MotorPair('B', 'A')
```

## Actions

Runs both motors simultaneously to move a Driving Base.
### move()

```python
from mindstorms import MotorPair

motor_pair = MotorPair('B', 'A')

motor_pair.move(4, 'cm', 0, 50)
motor_pair.move(2, 'rotations', steering=100)
motor_pair.move(3, 'seconds', steering=-100, 100)
```

```python
    def move(self, amount: float, unit: str = 'cm', steering: int = 0, speed: int = None):
        """Runs both motors simultaneously to move a Driving Base.Runs both motors simultaneously to move a Driving Base.

        :param amount: The amount of movement in relation to the specified unit. Negative value moves the Driving Base backward instead of forward.
        :param unit: The unit of measurement. When unit is specified as 'cm' or 'in', the amount parameter represents the horizontal distance the Driving Base must travel. The relationship between the motor rotations and distance traveled can be adjusted using the function `set_motor_rotation()`. When unit is specified as 'rotations" or 'degrees', the amount parameter represents how many rotations or degrees the motor must rotate. When unit is specified as 'seconds', the amount parameter represents the duration the motors must run.
        :param steering: The direction the Driving Base is steering. The default 0 value steers the Driving Base straight. Negative value steers the Driving Base to the left and positive value to the right. Minimum and maximum value makes the Driving Base spin on itself.
        :param speed: The desired motors speed. Negative value moves the Driving Base backward instead of forward. If no value is specified, the speed set by set_default_speed() is used.
        """
        assert unit in ['cm', 'in', 'rotations', 'degrees', 'seconds']
        assert -100 <= steering <= 100
        assert -100 <= speed <= 100
```


Starts both motors simultaneously to move a Driving Base.
The motors will keep moving at the specified speed until you give them another command or when your programs ends.
### start()

```python
from mindstorms import MSHub, MotorPair

motor_pair = MotorPair('B', 'A')

motor_pair.start(-100, 30)
# Press on the Hub's right button when you want the motors to stop.
hub.right_button.wait_until_pressed()
motor_pair.stop()
```

```python
    def start(self, steering: int = 0, speed: int = None):
        """Starts both motors simultaneously to move a Driving Base.
        The motors will keep moving at the specified speed until you give them another command or when your programs ends.Starts both motors simultaneously to move a Driving Base.
        The motors will keep moving at the specified speed until you give them another command or when your programs ends.

        :param steering: The direction the Driving Base is steering. The default 0 value steers the Driving Base straight. Negative value steers the Driving Base to the left and positive value to the right. minimum and maximum value makes the Driving base spin on itself.
        :param speed: The desired motors speed. If speed is negative, the Driving Base will move backward. If no value is specified, the default speed set by set_default_speed() is used.
        """
        assert -100 <= steering <= 100
        assert -100 <= speed <= 100
```


Stops both motors simultaneously, which will stop a Driving Base. What the motors do after they stop depends on the action sets in set_stop_action().
### stop()

```python
from mindstorms import MSHub, MotorPair

motor_pair = MotorPair('B', 'A')

motor_pair.start(-100, 30)
# Press on the Hub's right button when you want the motors to stop.
hub.right_button.wait_until_pressed()
motor_pair.stop()
```

```python
    def stop(self):
        """Stops both motors simultaneously, which will stop a Driving Base. What the motors do after they stop depends on the action sets in set_stop_action().
        """
        pass
```


Moves the Driving Base using differential (tank) steering. The speed of each motor can be controlled independently.
### move_tank()

```python
from mindstorms import MotorPair

motor_pair = MotorPair('B', 'A')
motor_pair.move_tank(10, 'cm', 25, 75)
```

```python
    def move_tank(self, amount: float, unit: str = 'cm', left_speed: int = None, right_speed: int = None):
        """Moves the Driving Base using differential (tank) steering. The speed of each motor can be controlled independently.Moves the Driving Base using differential (tank) steering. The speed of each motor can be controlled independently.

        :param amount: The amount of movement in relation to the specified unit. Negative value moves the Driving Base backward instead of forward.
        :param unit: The unit of measurement. When unit is specified as 'cm' or 'in', the amount parameter represents the horizontal distance the Driving Base must travel. The relationship between the motor rotations and distance traveled can be adjusted using the function set_motor_rotation(). When unit is specified as 'rotations" or 'degrees', the amount parameter represents how many rotations or degrees the motor must rotate. When unit is specified as 'seconds', the amount parameter represents the duration the motors must run.
        :param left_speed: The left motor's desired speed. Negative value makes the left motor run backward. If no value is specified, the default speed set by set_default_speed() is used.
        :param right_speed: The right motor's desired speed. Negative value makes the right motor run backward. If not value is specified, the default speed set by set_default_speed() is used.
        """
        assert unit in ['cm', 'in', 'rotations', 'degrees', 'seconds']
        assert -100 <= left_speed <= 100
        assert -100 <= right_speed <= 100
```


Starts moving a Driving Base using differential (tank) steering. The speed of each motor can be controlled independently. The motors will keep moving at the specified speed until you give them another command or when your programs ends.
### start_tank()

```python
from mindstorms import MSHub, MotorPair

motor_pair = MotorPair('B', 'A')

motor_pair.start_tank(100, -100)
# Press on the Hub's right button when you want the motors to stop.
hub.right_button.wait_until_pressed()
motor_pair.stop()
```

```python
    def start_tank(self, left_speed: int, right_speed: int):
        """Starts moving a Driving Base using differential (tank) steering. The speed of each motor can be controlled independently. The motors will keep moving at the specified speed until you give them another command or when your programs ends.Starts moving a Driving Base using differential (tank) steering. The speed of each motor can be controlled independently. The motors will keep moving at the specified speed until you give them another command or when your programs ends.

        :param left_speed: The left motor's desired speed.
        :param right_speed: The right motor's desired speed.
        """
        assert -100 <= left_speed <= 100
        assert -100 <= right_speed <= 100
```


Starts moving the Driving Base without speed control. This is useful when using your own control algorithm (e.g. a line-follower). The motors will keep moving at the specified power until you give them another command or when your programs ends.
### start_at_power()

```python
from mindstorms import MotorPair, ColorSensor

motor_pair = MotorPair('B', 'A')
color_sensor = ColorSensor('F')

while True:
    steering = color_sensor.get_reflected_light() - 50
    motor_pair.start_at_power(50, steering)
```

```python
    def start_at_power(self, power: int, steering: int = 0):
        """Starts moving the Driving Base without speed control. This is useful when using your own control algorithm (e.g. a line-follower). The motors will keep moving at the specified power until you give them another command or when your programs ends.Starts moving the Driving Base without speed control. This is useful when using your own control algorithm (e.g. a line-follower). The motors will keep moving at the specified power until you give them another command or when your programs ends.

        :param power: The desired amount of power for the motors. Negative value makes the motors rotate backward.
        :param steering: The direction the Driving Base is steering. The default 0 value steers the Driving Base straight. Negative value steers the Driving Base to the left and positive value to the right. Minimum and maximum value makes the Driving Base spin on itself.
        """
        assert -100 <= power <= 100
        assert -100 <= steering <= 100
```


Starts moving the Driving Base using differential (tank) steering without speed control.
This is useful when using your own control algorithm (e.g., a line-follower). The motors will keep moving at the specified power until you give them another command or when your programs ends.
### start_tank_at_power()

```python
from mindstorms import MSHub, MotorPair

hub = MSHub()
motor_pair = MotorPair('B', 'A')

motor_pair.start_tank_at_power(80, -80)
# Press on the Hub's right button when you want the motors to stop.
hub.right_button.wait_until_pressed()
motor_pair.stop()
```

```python
    def start_tank_at_power(self, left_power: int, right_power: int):
        """Starts moving the Driving Base using differential (tank) steering without speed control.
        This is useful when using your own control algorithm (e.g., a line-follower). The motors will keep moving at the specified power until you give them another command or when your programs ends.Starts moving the Driving Base using differential (tank) steering without speed control.
        This is useful when using your own control algorithm (e.g., a line-follower). The motors will keep moving at the specified power until you give them another command or when your programs ends.

        :param left_power: The desired amount of power for the left motor. Negative value makes the motors rotate backward.
        :param right_power: The desired amount of power for the right motor. Negative value makes the motors rotate backward.
        """
        assert -100 <= left_power <= 100
        assert -100 <= right_power <= 100
```


## Measurements

Returns the default motor pair speed.
### get_default_speed()

```python
from mindstorms import MSHub, Motor

hub = MSHub()
motor_pair_ba = MotorPair('B', 'A')

motor_pair_ba.set_default_speed(50)
motor_pair_ba.move(1, 'rotations', 0, 100)
hub.light_matrix.write('default speed =') 
hub.light_matrix.write(motor_pair_ba.get_default_speed())
```

```python
    def get_default_speed(self):
        """Returns the default motor pair speed.
        """
        pass
```


## Settings

Sets the distance ratio that a Driving Base travels when both motors run simultaneously one full rotation.
Setting the default speed does not affect the actual distance ratio. This function should be used before another function that runs motors.
### set_motor_rotation()

```python
from mindstorms import MotorPair
import math

motor_pair = MotorPair('B', 'A')
# The MINDSTORMS wheels have a diameter of 5,6 cm, multiplying by "π" gives the circumference.
motor_pair.set_motor_rotation(5,6 * math.pi, 'cm')
motor_pair.move(2, 'cm')
```

```python
    def set_motor_rotation(self, amount: float = 17.6, unit: str = 'cm'):
        """Sets the distance ratio that a Driving Base travels when both motors run simultaneously one full rotation.
        Setting the default speed does not affect the actual distance ratio. This function should be used before another function that runs motors.Sets the distance ratio that a Driving Base travels when both motors run simultaneously one full rotation.
        Setting the default speed does not affect the actual distance ratio. This function should be used before another function that runs motors.

        :param amount: The distance the Driving Base travels when both motors run simultaneously one full rotation. When the wheels are attached directly to the motors axle, the circumference of one wheel should be specified. When using gearing between the wheels and the motors axle, the gearing ratio must be multiplied by one wheel circumference.
        :param unit: The unit of measurement.
        """
        assert unit in ['cm', 'in']
```


Sets the default motor pair speed.
this is the default speed value used by the other motor pair functions when you do not specify a speed value. Setting the default speed does not affect the actual motors speed. This function should be used before another function that runs motors.
### set_default_speed()

```python
from mindstorms import MotorPair
from mindstorms.control import wait_for_seconds

motor_pair = MotorPair('B', 'A')

motor_pair.set_default_speed(30)
# The motor pair rotates for 2 seconds at the default speed (30%).
motor_pair.move(2, 'seconds')
# The motor pair start rotating at 60% speed.
motor_pair.start(0, 60)
# The default motor pair speed is set to 20% but the actual motor pair speed remains unchanged.
motor_pair.set_default_speed(20)
wait_for_seconds(2)
motor_pair.stop()
```

```python
    def set_default_speed(self, default_speed: int):
        """Sets the default motor pair speed.
        this is the default speed value used by the other motor pair functions when you do not specify a speed value. Setting the default speed does not affect the actual motors speed. This function should be used before another function that runs motors.Sets the default motor pair speed.
        this is the default speed value used by the other motor pair functions when you do not specify a speed value. Setting the default speed does not affect the actual motors speed. This function should be used before another function that runs motors.

        :param default_speed: The desired default motor pair speed.
        """
        assert -100 <= default_speed <= 100
```


Sets the default stop action the motor pair performs when motors stop running.
Setting the default stop action does not affect the actual motor pair stop action. This function should be used before another function that run or stop motor pair.
### set_stop_action()

```python
rom mindstorms import MotorPair

motor_pair = MotorPair('B', 'A')

# The motors are free after their complete stop.
motor_pair.set_stop_action('coast')
motor_pair.move(1, 'seconds', 0, 100)
# The motors keep braking after their complete stop.
motor_pair.set_stop_action('brake')
motor_pair.move(1, 'seconds', 0, 100)
# The motors hold their respective position after their complete stop.
motor_pair.set_stop_action('hold')
motor_pair.move(1, 'seconds', 0, 100)
```

```python
    def set_stop_action(self, action: str = 'coast'):
        """Sets the default stop action the motor pair performs when motors stop running.
        Setting the default stop action does not affect the actual motor pair stop action. This function should be used before another function that run or stop motor pair.Sets the default stop action the motor pair performs when motors stop running.
        Setting the default stop action does not affect the actual motor pair stop action. This function should be used before another function that run or stop motor pair.

        :param action: The desired stop action.
        """
        assert action in ['coast', 'brake', 'hold']
```


Sensors
# Color Sensor
This is the Color sensor Library, you can use the functions here to detect colors, ambient light and light reflection.
To use the Color Sensor, you must first initialize it.
### Color Sensor

```python
from mindstorms import ColorSensor
# Initialize the Color Sensor.
color = ColorSensor('E')
```

## Measurements
Returns the color the color sensor sees.
### get_color()

```python
from mindstorms import MSHub, ColorSensor
from mindstorms.operator import not_equal_to


hub = MSHub()
paper_scanner = ColorSensor('E')

color = paper_scanner.get_color()
if not_equal_to(color, None):
    hub.status_light.on(color)
    hub.light_matrix.write('Color ' + color + ' detected')
else :
    hub.light_matrix.write('No color detected')

```

```python
    def get_color(self):
        """Returns the color the color sensor sees.
        """
        pass
```


Returns the intensity of the ambient light. The Color Sensor changes mode to detected the ambient light, this can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it is in ambient light mode.
```python
    def get_ambient_light(self):
        """Returns the intensity of the ambient light. The Color Sensor changes mode to detected the ambient light, this can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it is in ambient light mode.
        """
        pass
```


Returns the intensity of the reflected light.
```python
    def get_reflected_light(self):
        """Returns the intensity of the reflected light.
        """
        pass
```


Returns the intensity of the red, green and blue color and the overall color intensity.
### get_rgb_intensity()

```python
from mindstorms import MSHub, ColorSensor
from mindstorms.control import wait_for_seconds

# Display the red intensity, tuple [0].
hub = MSHub()
paper_scanner = ColorSensor('E')

wait_for_seconds(1)
rgb_intensity = paper_scanner.get_rgb_intensity()
hub.light_matrix.write('red = ')
# Display the red intensity, tuple [0].
hub.light_matrix.write(rgb_intensity[0])
wait_for_seconds(1)
hub.light_matrix.write('overall = ')
# Display the overall intensity, tuple [3].
hub.light_matrix.write(rgb_intensity[3])
```

```python
    def get_rgb_intensity(self):
        """Returns the intensity of the red, green and blue color and the overall color intensity.
        """
        pass
```


Returns the red color intensity detected by the Color Sensor.
```python
    def get_red(self):
        """Returns the red color intensity detected by the Color Sensor.
        """
        pass
```


Returns the green color intensity detected by the Color Sensor.
```python
    def get_green(self):
        """Returns the green color intensity detected by the Color Sensor.
        """
        pass
```


Returns the blue color intensity detected by the Color Sensor.
```python
    def get_blue(self):
        """Returns the blue color intensity detected by the Color Sensor.
        """
        pass
```


## Events

Waits until the Color Sensor detects the specified color.
### wait_until_color()

```python
from mindstorms import ColorSensor

color_sensor = ColorSensor('A')

color_sensor.wait_until_color('blue')
# Put your own code here
```

```python
    def wait_until_color(self, color: str):
        """Waits until the Color Sensor detects the specified color.Waits until the Color Sensor detects the specified color.

        :param color: The name of the color.
        """
        assert color in ['black', 'blue', 'cyan', 'green', 'red', 'violet', 'white', 'yellow' or None]
```


Waits until the Color Sensor detects a new color. The first time this method is called, it immediately returns the detected color. After that, it waits until the Color Sensor detects a color that’s different from the color that was detected the last time this method was used.
### wait_for_new_color()

```python
from mindstorms import ColorSensor

color_sensor = ColorSensor('A')

while True:
    color = color_sensor.wait_for_new_color()
    if color == 'black':
        # Put your own code here
        print('black')
    elif color == 'white':
        # Put your own code here
        print('white')
```

```python
    def wait_for_new_color(self):
        """Waits until the Color Sensor detects a new color. The first time this method is called, it immediately returns the detected color. After that, it waits until the Color Sensor detects a color that’s different from the color that was detected the last time this method was used.
        """
        pass
```


## Actions

Lights up all of the lights on the Color Sensor at the specified brightness. The Color Sensor changes mode to light up, this can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in light up mode.
### light_up_all()

```python
from mindstorms import ColorSensor

color_sensor = ColorSensor('A')
# Turns on the Color Sensor's lights at 100% (default) brightness.
color_sensor.light_up_all()
# Turns on the Color Sensor's lights at 10% brightness..
color_sensor.light_up_all(10)
```

```python
    def light_up_all(self, brightness: int = 100):
        """Lights up all of the lights on the Color Sensor at the specified brightness. The Color Sensor changes mode to light up, this can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in light up mode.Lights up all of the lights on the Color Sensor at the specified brightness. The Color Sensor changes mode to light up, this can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in light up mode.

        :param brightness: The desired brightness in percent of the Color Sensor lights.
        """
        assert 0 <= brightness <= 100
```


Sets the brightness of each individual lights on the Color Sensor.
The Color Sensor changes mode to light up, this can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in light up mode.
### light_up()

```python
from mindstorms import ColorSensor

color_sensor = ColorSensor('A')
# Turn on one light (light_2) on the Color Sensor at full brightness.
color_sensor.light_up(0, 100, 0)
```

```python
    def light_up(self, light_1: int = 100, light_2: int = 100, light_3: int = 100):
        """Sets the brightness of each individual lights on the Color Sensor.
        The Color Sensor changes mode to light up, this can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in light up mode.Sets the brightness of each individual lights on the Color Sensor.
        The Color Sensor changes mode to light up, this can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in light up mode.

        :param light_1: The desired brightness of the first light in percent.
        :param light_2: The desired brightness of the second light in percent.
        :param light_3: The desired brightness of the third light in percent.
        """
        assert 0 <= light_1 <= 100
        assert 0 <= light_2 <= 100
        assert 0 <= light_3 <= 100
```


# Distance Sensor
This is the Distance Sensor Library, you can use the functions here to detect objects within the sensor range and measure distances. To use the Distance Sensor, you must first initialize it.
### Distance Sensor

```python
from mindstorms import DistanceSensor
# Initialize the Distance Sensor.
distance = DistanceSensor('A')
```

## Measurements

Returns the measured distance in centimeters.
### get_distance_cm()

```python
from mindstorms import DistanceSensor

# Initialize the Distance Sensor.
wall_detector = DistanceSensor('F')

# Measure the distance between the Distance Sensor and object in centimeters and inches.
dist_cm = wall_detector.get_distance_cm()
dist_inches = wall_detector.get_distance_inches()
# Print both results on the console.
print('cm:', dist_cm, 'inches:', dist_inches)
```

```python
    def get_distance_cm(self, short_range: bool = False):
        """Returns the measured distance in centimeters.Returns the measured distance in centimeters.

        :param short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
        """
        assert isinstance(short_range, bool)
```


Returns the measured distance in inches.
### get_distance_cm()

```python
from mindstorms import DistanceSensor

# Initialize the Distance Sensor.
wall_detector = DistanceSensor('F')

# Measure the distance between the Distance Sensor and object in centimeters and inches.
dist_cm = wall_detector.get_distance_cm()
dist_inches = wall_detector.get_distance_inches()
# Print both results on the console.
print('cm:', dist_cm, 'inches:', dist_inches)
```

```python
    def get_distance_inches(self, short_range: bool = False):
        """Returns the measured distance in inches.Returns the measured distance in inches.

        :param short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
        """
        assert isinstance(short_range, bool)
```


Returns the measured distance as a percentage of the Distance Sensor detection range.
```python
    def get_distance_percentage(self, short_range: bool = False):
        """Returns the measured distance as a percentage of the Distance Sensor detection range.Returns the measured distance as a percentage of the Distance Sensor detection range.

        :param short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
        """
        assert isinstance(short_range, bool)
```


## Events

Waits until the measured distance is greater than the specified distance.
### wait_for_distance_farther_than()

```python
from mindstorms import MSHub, DistanceSensor

hub = MSHub()
distance_sensor = DistanceSensor('F')

while True:
    distance_sensor.wait_for_distance_farther_than(20, 'cm')
    hub.light_matrix.write('>')
    distance_sensor.wait_for_distance_closer_than(20, 'cm')
    hub.light_matrix.write('<')
```

```python
    def wait_for_distance_farther_than(self, distance: float, unit: str = 'cm', short_range: bool = False):
        """Waits until the measured distance is greater than the specified distance.Waits until the measured distance is greater than the specified distance.

        :param distance: The target distance to be detected from the sensor to an object.
        :param unit: The unit in which the distance is measured.
        :param short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
        """
        assert unit in ['cm', 'in', '%']
        assert isinstance(short_range, bool)
```


Waits until the measured distance is less than the specified distance.
### wait_for_distance_farther_than()

```python
from mindstorms import MSHub, DistanceSensor

hub = MSHub()
distance_sensor = DistanceSensor('F')

while True:
    distance_sensor.wait_for_distance_farther_than(20, 'cm')
    hub.light_matrix.write('>')
    distance_sensor.wait_for_distance_closer_than(20, 'cm')
    hub.light_matrix.write('<')
```

```python
    def wait_for_distance_closer_than(self, distance: float, unit: str = 'cm', short_range: bool = False):
        """Waits until the measured distance is less than the specified distance.Waits until the measured distance is less than the specified distance.

        :param distance: The target distance to be detected from the sensor to an object.
        :param unit: The unit in which the distance is measured.
        :param short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
        """
        assert unit in ['cm', 'in', '%']
        assert isinstance(short_range, bool)
```


## Actions
Lights up all of the lights on the Distance Sensor at the specified brightness.
### light_up_all()

```python
from mindstorms import DistanceSensor

distance_sensor = DistanceSensor('F')

# Turn on the lights at maximum brightness (100%).
distance_sensor.light_up_all(100)
# Turn off the lights.
distance_sensor.light_up_all(0)
```

```python
    def light_up_all(self, brightness: int = 100):
        """Lights up all of the lights on the Distance Sensor at the specified brightness.Lights up all of the lights on the Distance Sensor at the specified brightness.

        :param brightness: The desired brightness in percent of all the distance sensor lights.
        """
        assert 0 <= brightness <= 100
```


Light up each individual lights of the Distance Sensor at the specified brightness.
### light_up()

```python
from mindstorms import DistanceSensor

distance_sensor = DistanceSensor('A')
# Switch on the top light of the Distance Sensor.
distance_sensor.light_up(100, 20, 0, 0)
```

```python
    def light_up(self, right_top: int = 100, left_top: int = 100, right_bottom: int = 100, left_bottom: int = 100):
        """Light up each individual lights of the Distance Sensor at the specified brightness.Light up each individual lights of the Distance Sensor at the specified brightness.

        :param right_top: The brightness in percent of the right top light of the Distance Sensor.
        :param left_top: The brightness in percent of the left top light of the Distance Sensor.
        :param right_bottom: The brightness in percent of the right bottom light of the Distance Sensor.
        :param left_bottom: The brightness in percent of the left bottom light of the Distance Sensor.
        """
        assert 0  <= right_top <= 100
        assert 0 <= left_top <= 100
        assert 0 <= right_bottom <= 100
        assert 0 <= left_bottom <= 100
```


# Force Sensor
This is the Force Sensor library, you can use the functions here to detect pression on the Force Sensor and measure the force applied. To use the Force Sensor, you must first initialize it.
### Force Sensor

```python
from mindstorms import ForceSensor
# Initialize the Force Sensor.
force = ForceSensor('E')
```

## Measurements
Checks if the Force Sensor is pressed.
### is_pressed()

```python
from mindstorms import MSHub, ForceSensor

hub = MSHub
door_bell = ForceSensor('E')

# Check if the Force Sensor is pressed.
while True:
    if door_bell.is_pressed():
        hub.speaker.beep()
```

```python
    def is_pressed(self):
        """Checks if the Force Sensor is pressed.
        """
        pass
```


Returns the measured force in newtons.
### get_force_newton()

```python
from mindstorms import ForceSensor

# Initialize the Force Sensor.
door_bell = ForceSensor('E')

# Measure the force in newtons and as a percentage.
newtons = door_bell.get_force_newton()
percentage = door_bell.get_force_percentage()
# Print both results on the console.
print('N:', newtons, '=', percentage, '%')

```

```python
    def get_force_newton(self):
        """Returns the measured force in newtons.
        """
        pass
```


Returns the measured force as a percentage of the Force sensor detection range.
### get_force_newton()

```python
from mindstorms import ForceSensor

# Initialize the Force Sensor.
door_bell = ForceSensor('E')

# Measure the force in newtons and as a percentage.
newtons = door_bell.get_force_newton()
percentage = door_bell.get_force_percentage()
# Print both results on the console.
print('N:', newtons, '=', percentage, '%')

```

```python
    def get_force_percentage(self):
        """Returns the measured force as a percentage of the Force sensor detection range.
        """
        pass
```


## Events

Waits until the Force Sensor is pressed.
### wait_until_pressed()

```python
from mindstorms import MSHub, ForceSensor

hub = MSHub()
force_sensor = ForceSensor('E')

while True:
    force_sensor.wait_until_pressed()
    hub.light_matrix.show_image('GO_DOWN')
    force_sensor.wait_until_released()
    hub.light_matrix.show_image('GO_UP')
```

```python
    def wait_until_pressed(self):
        """Waits until the Force Sensor is pressed.
        """
        pass
```


Waits until the Force Sensor is released.
### wait_until_pressed()

```python
from mindstorms import MSHub, ForceSensor

hub = MSHub()
force_sensor = ForceSensor('E')

while True:
    force_sensor.wait_until_pressed()
    hub.light_matrix.show_image('GO_DOWN')
    force_sensor.wait_until_released()
    hub.light_matrix.show_image('GO_UP')
```

```python
    def wait_until_released(self):
        """Waits until the Force Sensor is released.
        """
        pass
```


Math & Logic
# Mathematical Functions
This is the Mathematical functions library, you can use the functions here to do some advance mathematical operations.
Returns the result of the inverse cosine function.
```python
    def acos(self, x: float):
        """Returns the result of the inverse cosine function.Returns the result of the inverse cosine function.

        :param x: 
        """
        pass
```


Returns the result of the inverse hyperbolic cosine function.
```python
    def acosh(self, x: float):
        """Returns the result of the inverse hyperbolic cosine function.Returns the result of the inverse hyperbolic cosine function.

        :param x: 
        """
        pass
```


Returns the result of the inverse sine function.
```python
    def asin(self, x: float):
        """Returns the result of the inverse sine function.Returns the result of the inverse sine function.

        :param x: 
        """
        pass
```


Returns the result of the inverse hyperbolic sine function.
```python
    def asinh(self, x: float):
        """Returns the result of the inverse hyperbolic sine function.Returns the result of the inverse hyperbolic sine function.

        :param x: 
        """
        pass
```


Returns the result of the inverse tangent function.
```python
    def atan(self, x: float):
        """Returns the result of the inverse tangent function.Returns the result of the inverse tangent function.

        :param x: 
        """
        pass
```


Returns the result of the arc tangent function of y/x.
```python
    def atan2(self, x: float, y: float):
        """Returns the result of the arc tangent function of y/x.Returns the result of the arc tangent function of y/x.

        :param x: 
        :param y: 
        """
        pass
```


Returns the result of the inverse hyperbolic tangent function.
```python
    def atanh(self, x: float):
        """Returns the result of the inverse hyperbolic tangent function.Returns the result of the inverse hyperbolic tangent function.

        :param x: 
        """
        pass
```


Returns a ceiling value of x i.e., the largest integer not greater than x.
```python
    def ceil(self, x: float):
        """Returns a ceiling value of x i.e., the largest integer not greater than x.Returns a ceiling value of x i.e., the largest integer not greater than x.

        :param x: 
        """
        pass
```


Returns the value of x with the sign of y.
```python
    def copysign(self, x: float, y: float):
        """Returns the value of x with the sign of y.Returns the value of x with the sign of y.

        :param x: 
        :param y: 
        """
        pass
```


Returns the result of the cosine function.
```python
    def cos(self, x: float):
        """Returns the result of the cosine function.Returns the result of the cosine function.

        :param x: 
        """
        pass
```


Returns the result of the hyperbolic cosine function.
```python
    def cosh(self, x: float):
        """Returns the result of the hyperbolic cosine function.Returns the result of the hyperbolic cosine function.

        :param x: 
        """
        pass
```


Returns the result of the conversion from radians to degrees.
```python
    def degrees(self, x: float):
        """Returns the result of the conversion from radians to degrees.Returns the result of the conversion from radians to degrees.

        :param x: 
        """
        pass
```


Returns the result of the error function.
```python
    def erf(self, x: float):
        """Returns the result of the error function.Returns the result of the error function.

        :param x: 
        """
        pass
```


Returns the result of the complementary error function.
```python
    def erfc(self, x: float):
        """Returns the result of the complementary error function.Returns the result of the complementary error function.

        :param x: 
        """
        pass
```


Returns the result of the exponential function.
```python
    def exp(self, x: float):
        """Returns the result of the exponential function.Returns the result of the exponential function.

        :param x: 
        """
        pass
```


Returns the result of the exponential function of x,  - 1. This function provides greater precision than exp(x) - 1 for small values of x.
```python
    def expm1(self, x: float):
        """Returns the result of the exponential function of x,  - 1. This function provides greater precision than exp(x) - 1 for small values of x.Returns the result of the exponential function of x,  - 1. This function provides greater precision than exp(x) - 1 for small values of x.

        :param x: 
        """
        pass
```


Returns the absolute value of x.
```python
    def fabs(self, x: float):
        """Returns the absolute value of x.Returns the absolute value of x.

        :param x: 
        """
        pass
```


Returns the floor of x i.e., the smallest integer not lesser than x.
```python
    def floor(self, x: float):
        """Returns the floor of x i.e., the smallest integer not lesser than x.Returns the floor of x i.e., the smallest integer not lesser than x.

        :param x: 
        """
        pass
```


Returns the remainder of x divided by y.
```python
    def fmod(self, x: float, y: float):
        """Returns the remainder of x divided by y.Returns the remainder of x divided by y.

        :param x: 
        :param y: 
        """
        pass
```


Returns the mantissa and the exponent of x, as a pair (m,e).
The mathematical formula is: x = m * 2^e.
```python
    def frexp(self, x: float):
        """Returns the mantissa and the exponent of x, as a pair (m,e).
        The mathematical formula is: x = m * 2^e.Returns the mantissa and the exponent of x, as a pair (m,e).
        The mathematical formula is: x = m * 2^e.

        :param x: 
        """
        pass
```


Returns the result of the gamma function.
```python
    def gamma(self, x: float):
        """Returns the result of the gamma function.Returns the result of the gamma function.

        :param x: 
        """
        pass
```


Checks if x is finite.
```python
    def isfinite(self, x: float):
        """Checks if x is finite.Checks if x is finite.

        :param x: 
        """
        pass
```


Checks if x is infinite.
```python
    def isinf(self, x: float):
        """Checks if x is infinite.Checks if x is infinite.

        :param x: 
        """
        pass
```


Checks if x is a NaN. NaN stands for Not a Number.
```python
    def isnan(self, x: Any):
        """Checks if x is a NaN. NaN stands for Not a Number.Checks if x is a NaN. NaN stands for Not a Number.

        :param x: 
        """
        pass
```


Returns the results of x * 2^exp.
```python
    def ldexp(self, x: float):
        """Returns the results of x * 2^exp.Returns the results of x * 2^exp.

        :param x: 
        """
        pass
```


Returns the result of the natural logarithm of the gamma function.
```python
    def lgamma(self, x: float):
        """Returns the result of the natural logarithm of the gamma function.Returns the result of the natural logarithm of the gamma function.

        :param x: 
        """
        pass
```


Returns the result of the natural logarithm function.
```python
    def log(self, x: float):
        """Returns the result of the natural logarithm function.Returns the result of the natural logarithm function.

        :param x: 
        """
        pass
```


Returns the result of the base-10 logarithm function.
```python
    def log10(self, x: float):
        """Returns the result of the base-10 logarithm function.Returns the result of the base-10 logarithm function.

        :param x: 
        """
        pass
```


Returns the result of the base-2 logarithm function.
```python
    def log2(self, x: float):
        """Returns the result of the base-2 logarithm function.Returns the result of the base-2 logarithm function.

        :param x: 
        """
        pass
```


Returns the fractional and integral parts of x.
```python
    def modf(self, x: float):
        """Returns the fractional and integral parts of x.Returns the fractional and integral parts of x.

        :param x: 
        """
        pass
```


Returns the result of the power function.
```python
    def pow(self, x: int, y: int):
        """Returns the result of the power function.Returns the result of the power function.

        :param x: 
        :param y: 
        """
        pass
```


Returns the result of the conversion from degrees to radians.
```python
    def radians(self, x: float):
        """Returns the result of the conversion from degrees to radians.Returns the result of the conversion from degrees to radians.

        :param x: 
        """
        pass
```


Returns the result of the sine function.
```python
    def sin(self, x: float):
        """Returns the result of the sine function.Returns the result of the sine function.

        :param x: 
        """
        pass
```


Returns the result of the hyperbolic sine function.
```python
    def sinh(self, x: float):
        """Returns the result of the hyperbolic sine function.Returns the result of the hyperbolic sine function.

        :param x: 
        """
        pass
```


Returns the result of the square root function.
```python
    def sqrt(self, x: float):
        """Returns the result of the square root function.Returns the result of the square root function.

        :param x: 
        """
        pass
```


Returns the result of the tangent function.
```python
    def tan(self, x: float):
        """Returns the result of the tangent function.Returns the result of the tangent function.

        :param x: 
        """
        pass
```


Returns the result of the hyperbolic tangent function.
```python
    def tanh(self, x: float):
        """Returns the result of the hyperbolic tangent function.Returns the result of the hyperbolic tangent function.

        :param x: 
        """
        pass
```


Returns the truncated integer part of a number.
```python
    def trunc(self, x: float):
        """Returns the truncated integer part of a number.Returns the truncated integer part of a number.

        :param x: value to be rounded toward 0
        """
        pass
```


## Constants

# e
## e
The mathematical constant e = 2.718281…  with the maximum precision the Mindstorms hub can provide.
# pi
## pi
The mathematical constant π = 3.141592… with the maximum precision the Mindstorms hub can provide.
# Operators
This is the Operators library, you can use the functions here to do logical (boolean) operations.
Checks if the specified value a is greater than the specified value b. This is the same as a > b.
### greater_than()

```python
from mindstorms import ColorSensor
from mindstorms.control import wait_until
from mindstorms.operator import greater_than

color_sensor = ColorSensor('A')

wait_until(color_sensor.get_reflected_light, greater_than, 50)
```

```python
    def greater_than(self, a: Any, b: Any):
        """Checks if the specified value a is greater than the specified value b. This is the same as a > b.Checks if the specified value a is greater than the specified value b. This is the same as a > b.

        :param a: Any value that can be compared to b.
        :param b: Any value that can be compared to a.
        """
        pass
```


Checks if the specified value a is greater than or equal to the specified value b. This is the same as a >= b.
### greater_than_or_equal_to()

```python
from mindstorms import ColorSensor
from mindstorms.control import wait_until
from mindstorms.operator import greater_than_or_equal_to

color_sensor = ColorSensor('A')

wait_until(color_sensor.get_reflected_light, greater_than_or_equal_to, 50)
```

```python
    def greater_than_or_equal_to(self, a: Any, b: Any):
        """Checks if the specified value a is greater than or equal to the specified value b. This is the same as a >= b.Checks if the specified value a is greater than or equal to the specified value b. This is the same as a >= b.

        :param a: Any value that can be compared to b.
        :param b: Any value that can be compared to a.
        """
        pass
```


Checks if the specified value a is less than the specified value b. This is the same as a < b.
### less_than()

```python
from mindstorms import ColorSensor
from mindstorms.control import wait_until
from mindstorms.operator import less_than

color_sensor = ColorSensor('A')

wait_until(color_sensor.get_reflected_light, less_than, 50)
```

```python
    def less_than(self, a: Any, b: Any):
        """Checks if the specified value a is less than the specified value b. This is the same as a < b.Checks if the specified value a is less than the specified value b. This is the same as a < b.

        :param a: Any value that can be compared to b.
        :param b: Any value that can be compared to a.
        """
        pass
```


Checks if the specified value a is less than or equal to the specified value b. This is the same as a <= b.
### less_than_or_equal_to()

```python
from mindstorms import ColorSensor
from mindstorms.control import wait_until
from mindstorms.operator import less_than_or_equal_to

color_sensor = ColorSensor('A')

wait_until(color_sensor.get_reflected_light, less_than_or_equal_to, 50)
```

```python
    def less_than_or_equal_to(self, a: Any, b: Any):
        """Checks if the specified value a is less than or equal to the specified value b. This is the same as a <= b.Checks if the specified value a is less than or equal to the specified value b. This is the same as a <= b.

        :param a: Any value that can be compared to b.
        :param b: Any value that can be compared to a.
        """
        pass
```


Checks if the specified value a is equal to the specified value b. This is the same as a == b.
### equal_to()

```python
from mindstorms import ColorSensor
from mindstorms.control import wait_until
from mindstorms.operator import equal_to

color_sensor = ColorSensor('A')

wait_until(color_sensor.get_color, equal_to, 'red')
```

```python
    def equal_to(self, a: Any, b: Any):
        """Checks if the specified value a is equal to the specified value b. This is the same as a == b.Checks if the specified value a is equal to the specified value b. This is the same as a == b.

        :param a: Any value that can be compared to b.
        :param b: Any value that can be compared to a.
        """
        pass
```


Checks if the specified value a is not equal to the specified value b. This is the same as a != b.
### not_equal_to()

```python
from mindstorms import ColorSensor
from mindstorms.control import wait_until
from mindstorms.operator import not_equal_to

color_sensor = ColorSensor('A')

wait_until(color_sensor.get_color, not_equal_to, None)
```

```python
    def not_equal_to(self, a: Any, b: Any):
        """Checks if the specified value a is not equal to the specified value b. This is the same as a != b.Checks if the specified value a is not equal to the specified value b. This is the same as a != b.

        :param a: Any value that can be compared to b.
        :param b: Any value that can be compared to a.
        """
        pass
```


Timing
# Wait Functions
This is the Wait Function library, you can use the functions here to pause your program while you are waiting for an event to happen or for a certain period of time.
Waits for a specified number of seconds before continuing the program.
### wait_for_seconds()

```python
from mindstorms import MSHub
from mindstorms.control import wait_for_seconds

hub = MSHub()

# Wait for 3 seconds (pause the program flow).
wait_for_seconds(3)
hub.speaker.beep(60, 0.2)
```

```python
    def wait_for_seconds(self, seconds: float):
        """Waits for a specified number of seconds before continuing the program.Waits for a specified number of seconds before continuing the program.

        :param seconds: The time to wait, specified in seconds.
        """
        pass
```


Waits until the specified condition is True before continuing with the program.
### wait_until() 3

```python
from mindstorms import MSHub, ColorSensor
from mindstorms.control import wait_until
from mindstorms.operator import equal_to

hub = MSHub()
color_sensor = ColorSensor('E')

# Wait until the color sensor sees a red color
wait_until(color_sensor.get_color, equal_to, 'red')
hub.status_light.on('red')
```

```python
    def wait_until(self, get_value_function: Callable, operator_function: Callable, target_value: Any):
        """Waits until the specified condition is True before continuing with the program.Waits until the specified condition is True before continuing with the program.

        :param get_value_function: The name of a function, without parenthesis, that returns a value you want to compare to the specified target value.
        :param operator_function: The name of a logical operator function, without the parenthesis, that compares two arguments. Check the Mindstorms operator library for the available operator functions.
        :param target_value: Any value that can be compared to get_value_function by operator_function.
        """
        pass
```


# Timer
This is the Timer library, you can use the functions here to set up a timer and measure time.
To use the Timer, you must first initialize it.
### Timer

```python
from mindstorms.control import Timer
# Initialize the Timer.
timer = Timer()
```

## Actions
Resets the Timer to 0.
### reset()

```python
from mindstorms import MSHub
from mindstorms.control import Timer

hub = MSHub()
timer = Timer()

# Reset the timer.
timer.reset()

# Display on the light matrix the timer count.
hub.light_matrix.write('timer =')
hub.light_matrix.write(timer.now())
```

```python
    def reset(self):
        """Resets the Timer to 0.
        """
        pass
```


## Measurements
Returns the timer count in seconds.
### reset()

```python
from mindstorms import MSHub
from mindstorms.control import Timer

hub = MSHub()
timer = Timer()

# Reset the timer.
timer.reset()

# Display on the light matrix the timer count.
hub.light_matrix.write('timer =')
hub.light_matrix.write(timer.now())
```

```python
    def now(self):
        """Returns the timer count in seconds.
        """
        pass
```


