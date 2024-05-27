# python4Hacking

This is my notes from TCMSecurity's Python 101 and 201 for Hackers

## Python 101

**What is Python?**
1. Dynamic, interpreted, object-oriented, high-level language
2. Versatile with a mature standard library
3. Actively used with a large community

**Why learn Python as a hacker?**
1. Understand how PoCs work
2. Debug, modify and run scripts or PoCs
3. Create your own scripts
4. Understanding how an app works could also lead to understanding how it could break

### Python Interpreter

> Typing Python3 in Linux Command box opens up the Interpreter which allows for code to be run on the spot
> python3 -c 'import pty; pty.spawn("/bin/bash");'

## Basic Syntax and Python 101

**Variables and Data Types**
> name = 'Tom' #Assigning the string Tom to variable name
> name_length = 3 # assigning the integer 3 to name_length
> name, name_length = "Tom" , 3 # assigning multiple values to multiple variables

**Integers and Floats**
> num_int = 1
> num_flt = 1.0
> num_complex = 3.14j #complex numbers
> num_hex = 0xa # this returns an integer of 10 as 0xa in hex is 10
> num_octal = 0o10

*Python allows combination of number types for calculation. For eg, 1 + 0x1 =2*

> abs(-4) #absolute functions
> round (8.4) # rounds the float

**Strings**


**Lists**
> name_list = ["Tom", "Alice"]
> name1, name2 = name_list # this assigns Tom to name1 and Alice to name2

**tuple**
>name_tuple = ("Tom", "Alice")

**Dictionaries**
>name_dict = {"Tom": 30, "Alice": 25}

**Boolean**
>name_boolean = True

**Range**
>name_range = range(6)

**Bytes**
>name_bytes = b"Tom"

