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

> Typing Python3 in Linux Command box opens up the Interpreter which allows for code to be run on the spot\
> python3 -c 'import pty; pty.spawn("/bin/bash");'

## Basic Syntax and Python 101

**Variables and Data Types**
> name = 'Tom' #Assigning the string Tom to variable name\
> name_length = 3 # assigning the integer 3 to name_length\
> name, name_length = "Tom" , 3 # assigning multiple values to multiple variables\

**Integers and Floats**
> num_int = 1\
> num_flt = 1.0\
> num_complex = 3.14j #complex numbers\
> num_hex = 0xa # this returns an integer of 10 as 0xa in hex is 10\
> num_octal = 0o10\

*Python allows combination of number types for calculation. For eg, 1 + 0x1 =2*

> abs(-4) #absolute functions\
> round (8.4) # rounds the float\

**Strings**
> str1 = "I\"m a string" # A backslash is required to escape the string\
> str2 = "I am a string\n I am not an integer" #\n allows a newline\
> str_a = "a" * 10 # this assigns 10 a to str_a\

**Transforming Strings**
> str1.upper()\
> str1.lower()\
> str1.strip() # removes blanks\
> str1.replace("!", "?") # replaces all ! with ?\
> str1.replace("string","example").strip() #combines transformation\
> str1.split() # splits string by space as delimiter\
> str1.split(",") # splits by comma\
> str1.encode() \
> str1.rjust(25,"X") # this justifies str1 by 25 space and fills in the space with XXXX\

**Strings Conditional Checks**
> print( "string" in str2) # this checks if "string" is in str2 and returns True or False accordingly\
> print(str1.startswith("I")) #checks if str1 starts with I\
> print(str1.index("string")) #outputs the index of the "String" in str1\

> len(str1) # outputs number of characters in str1

**Format**
> "string1 is {} characters long!".format(len(str1)) # this circumvents needing to cast len(str1) as a string and inputs format(len(str1)) as {}\
> print("{} {} {}".format(len(str1), 5.0, 20)) #this will print in sequence 14, 5.0 and 20\
> print("{1} {0} {2}".format(len(str1), 5.0, 20)) #this will print by index. i.e. 5.0, 14, 20\

> length =len(str1)\
> print(f"str1 is {length} characters long") #by defining a varable ahead of time, using the f in front of the string allows to input the varaiable without needing to type out format\

> print("string1 is %d characters long!" % len(str1)")

**Lists**
> name_list = ["Tom", "Alice"]\
> name1, name2 = name_list # this assigns Tom to name1 and Alice to name2\

You can put all kinds of data types inside a list including another list or a tuple

> list1[0] = "X" #assigns X to first item on the list\
> del list1[0] #removes the firs t item\
> list1 = ['A'] + list1 #adds A as the first item to list\
> list1.append("G")\
> list1.reverse() #reverse the order of the list\
> list1.count("A") #counts the number of A in the list\
> list1.pop() # eject the last item in the list\
> list1.extend(list3) # add list3 to the end of list1\
> list1.clear() # remove everything in the list\
> list1.sort() #sort from smaller to biggest\
> list1.sort(reverse=True) #sort from biggest to smallest\
> list1.copy() #copy a list\

**List Comprehension**
Another way to create new lists through iteriation\
> list1 = ['a', 'b', 'c']\
> list2 =[x for x in list1] # this create a list 2 with the same elements in list1\
> list3 =[x for x in list1 if x =='a'] \
> list4 = [x for x in range(5)]\
> list5 = [x*x for x in range(5)\ # this creates a list where each element is squared]\
> list10 =[[1,2,3], [4,5,6]]\
> list11 = [y for x in list10 for y in x] # this returns list 10 sublists as separate elements\
> list12 = [c for c in "string"]\


**tuple**

Can store multiple variables types and is immutable (cannot be changed)\
Unlike lists, you cannot append to a tuple though you can combine tuples\
> name_tuple = ("Tom", "Alice")\
> tuple_repeat = ('Combined!',) * 4 # this outputs ('Combined!', 'Combined!')\
> print("item2" in tuple_items) #check for item2 in the tuple_items\
> print(tuple_items.index("item2"))( # returns the index of item2 in tuple_items)\
> print(len(tuple_items)) # returns number of items inside tuple_items\
> print(tuple_items[-1]) # returns final item\
> print(tuple_items[0:2] # returns first two items)\

**Dictionaries**

Store Key:Value pairs. Cannot store duplicates. Good for performance\
> name_dict = {"Tom": 30, "Alice": 25}\
> dict1 = {'a':1, 'b':2, 'c':3}\
    > dict1.get('a)' #returns 1\
    > dict1.keys() # returns all Key values\
    > dict1.values() # returns all values\
    > dict1.items() # return all key-value pairs\
    > dict1['d'] = 4 # add the key of d and value of 4\
    > dict1.update({'a':2}) # updates 'a' to 2\
    > dict1['a'] = 2 #does the same thing as update\
    > dict1.pop('d') #pops d out\
    > del dict1['c'] # delete the key value pair of c:3\
    > dict1['c'] = {'a':1, 'b':2} #nested dictionaries \

**Sets**

Sets are unordered and you cant search something up with index\
Could be useful for union/intersect problem sets and you dont want to work with duplicates\
> set1 = {'a', 'b', 'c'} #when printed this randomly prints out combinations of a b c\
> set1.add('d') # adds d\
> set2 = {4,5,6}\
> set3 = set1.union(set2) \

**Boolean**
> name_boolean = True\
> valid, not_valid = True, False\
    > print (valid == True) #evaluates to True\
    > print (not_valid == True) # evaluates to False\
    > print (valid != True) # evaluates to False\

**Math Operations**
> print(10 // 10) #returns 1.0 as float\
> print(10 ** 3) #returns 1000\
> print(10 % 10) #returns modulus which is 0 in this case\
> x += 1 # outputs +1 to last x value\
> x *= 5 # outputs *5 to last x value\
> print(bin(x)) #returns binary value of x\

**Range**
>name_range = range(6)

**Bytes**
>name_bytes = b"Tom"

## Conditionals

if 1 < 1:/
    print('A')/
elif 1<=1:/
    print('B')/
else:/
    print('C')/

## Loops

a = 1\
while a < 5:\
    a += 1\
    print(a)\

for i in range(5):\
    print(i)\

for i in range(3):\
    for j in range(2):\
        print(i,j)\

for i in range (4):\
    if i == 2:\
        break\
    print (i)\

for i in range(5):\
    if i == 2:\
        continue\
    print(i) # this bypass 2\

for c in 'string':\
    print(c)\

for key, value in {'a':1, 'b':2}.items()

## Reading and Writing Files

f = open('xxx.txt', 'rt') # read text\
print(f.read()) #outputs the strings\

print(f.readlines()) # returns all lines as a list where each line is an item in the list\
f.seek(0) # this returns the pointer to the top of the file\

> for line in f:\
    print(line.strip())\

**Writing to file**

f = open('xxx.txt','w')\
f.write("test line two!")\ 
f.close() #these commands overwrite whatever text there is\

f = open('xxx.txt','a') # this opens the text file in append mode\
f.write("test line two!")\ 
f.close()\

For huge files

> with open('rockyou.txt', encoding='latin-1') as f\


## User Input
> test = input("Enter your name")\

> while True:\
    test = input ("Enter IP: ")\
    print(">>> {}".format(test))\
    if test == "exit":\
        break\
    else:\
        print ("Exploiting....")\
    
## Exceptions and Error Handling

try:
    f = open("sfvbavbiuas") # this file does not exist\
except Exception as e:\
    print(e) # this prints the error code and continues the file execution
except FileNotFoundError:\
    print("File does not exist")\

## Functions
Block of reusable code that runs only when it is called

> def function1():\
    > return "hello from function1!"\

return_from_function1 = function1() #assign a variable \

**Adding Parameters**

> def function2(s1,s2):\
    > print("{} {}".format(s1,s2))

function2("apple", "pear") # this returns apple pear\

To set a default parameter value\

def function3(s1="default response"):\
    print({}.format(s1))\

If the user does not input any parameters, default response would be printed\

Dictionary Arguments in Function\

def function7(**ks):\
    for a in ks:\
        print(a, ks[a])\

Variables declared within a function is a local variable and can only be used within the function\
If we wish to bring in global variables\

v=100\
def function9():\
    global var\
    v+=1\
    print(v)\


## Lambda
An anoymous function \

add = lambda x,y: x+y\
print(add(10,4) # returns 14\)


## Python Virtual Environments
Create isolated environments with specific libraries

> pip install virtualenv\
> python3 -m venv env\
> source env/bin/activate #this activates the virtual environment\

## Introduction to Sys
1. sys provides a bunch of functions and var related to the python runtime environment
2. A standard library that comes packaged with python

To use sys,\
> import sys\

Writing a Progress Bar\

> import time\
> for i in range(0, 51):\
    > time.sleep(0.1)\
    > sys.stdout.write("{} [{}{}]\r".format(i, '#'*i, "."*(51-i)))\
sys.stdout.write("\n")\

**sys.argv**
Gives a list of command line arguments that was passed when a script is run\

> python3 sys-demo.py 1 2 3 4 5 #passed five arguments into sys-demo.py \
To ensure that the user run the right number of arguments:\
> if len(sys.argv) !=3:
    > print("[X] To run {} enter a username and password".format(sys.argv[0])) #sys.argv[0] is the name of the script\
    > sys.exit(5) # returns error code of 5 \
> username = sys.argv[1]\
> password = sys.argv[2]\
> print("{} {}".format(username,password))\

## Introduction to Requests
Often used to interact with webapps\

> import requests\
> x = requests.get("http://httpbin.org/get") # httpbin is a test server that can be used\
> print(x.headers) #returns the website headers\
> if x.status_code == 200:\
    >print("Success!")\
> elif x.status_code == 404:\
    > print("Not Found")\
> print(x.elapsed)\
> print(x.cookies)\

> x = requests.get("http://httpbin.org/get", params={'id':1}) #this adds id=1 to the http request\
> print(x.url)\

> x = requests.delete("http://httpbin.org/delete")\

> x = requests.post("http://httpbin.org/post", data={'a':'b'})#sends data to the server\

> files = {'file': open('google.png', 'rb')}\
> x = requests.post('http://httpbin.org/post', files=file) #sends google.png to the server\

> x = requests.get("http://httpbin/org/get", auth=('username', 'password'))\

> x = requests.get("http://expired.badssl.com", verify=False) #bypass the SSL checks\

By default, requests follow redirects. To disable redirects:\

> x = requests.get("http://github.com", allow_redirects=False)\

For Timeouts\

>x = requests.get("Http://httpbin.org/get", timeout=0.01)\
> print(x.content)\

Getting Cookies to persist across session\

> x=requests.Session()\
> x.cookies.update({'a':'b'})\

## Intro to Pwntools (Library)
> from pwn import *\

Starting a local process\
> p = process("bin/sh")\
> p.sendline("echo hello!;")\
> p.interactive()\

Starting a remote process\
> r = remote("IP Address", Port)\
> r.sendline("hello")\
> r.interactive()\
> r.close()\

Set up a separate netcat\

> nc -lp <port>\

**Load files**

l = ELF('/bin/bash')\
print(hex(l.address)) #base address\
print(hex(l.entry))  #entry point\







