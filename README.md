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
> str1 = "I\"m a string" # A backslash is required to escape the string
> str2 = "I am a string\n I am not an integer" #\n allows a newline
> str_a = "a" * 10 # this assigns 10 a to str_a

**Transforming Strings**
> str1.upper()
> str1.lower()
> str1.strip() # removes blanks
> str1.replace("!", "?") # replaces all ! with ?
> str1.replace("string","example").strip() #combines transformation
> str1.split() # splits string by space as delimiter
> str1.split(",") # splits by comma
> str1.encode() 
> str1.rjust(25,"X") # this justifies str1 by 25 space and fills in the space with XXXX

**Strings Conditional Checks**
> print( "string" in str2) # this checks if "string" is in str2 and returns True or False accordingly
> print(str1.startswith("I")) #checks if str1 starts with I
> print(str1.index("string")) #outputs the index of the "String" in str1

> len(str1) # outputs number of characters in str1

**Format**
> "string1 is {} characters long!".format(len(str1)) # this circumvents needing to cast len(str1) as a string and inputs format(len(str1)) as {}
> print("{} {} {}".format(len(str1), 5.0, 20)) #this will print in sequence 14, 5.0 and 20
> print("{1} {0} {2}".format(len(str1), 5.0, 20)) #this will print by index. i.e. 5.0, 14, 20

> length =len(str1)
> print(f"str1 is {length} characters long") #by defining a varable ahead of time, using the f in front of the string allows to input the varaiable without needing to type out format

> print("string1 is %d characters long!" % len(str1)")

**Lists**
> name_list = ["Tom", "Alice"]
> name1, name2 = name_list # this assigns Tom to name1 and Alice to name2

**tuple**
Can store multiple variables types and is immutable (cannot be changed)
Unlike lists, you cannot append to a tuple though you can combine tuples
> name_tuple = ("Tom", "Alice")
> tuple_repeat = ('Combined!',) * 4 # this outputs ('Combined!', 'Combined!')
> print("item2" in tuple_items) #check for item2 in the tuple_items
> print(tuple_items.index("item2"))( # returns the index of item2 in tuple_items)
> print(len(tuple_items)) # returns number of items inside tuple_items
> print(tuple_items[-1]) # returns final item
> print(tuple_items[0:2] # returns first two items)

**Dictionaries**
> name_dict = {"Tom": 30, "Alice": 25}

**Boolean**
> name_boolean = True
> valid, not_valid = True, False
    > print (valid == True) #evaluates to True
    > print (not_valid == True) # evaluates to False
    > print (valid != True) # evaluates to False

**Math Operations**
> print(10 // 10) #returns 1.0 as float
> print(10 ** 3) #returns 1000
> print(10 % 10) #returns modulus which is 0 in this case
> x += 1 # outputs +1 to last x value
> x *= 5 # outputs *5 to last x value
> print(bin(x)) #returns binary value of x

**Range**
>name_range = range(6)

**Bytes**
>name_bytes = b"Tom"

