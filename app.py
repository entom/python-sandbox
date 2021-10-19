import random

def myFunc(name):
    print("Hello!" + name + "!")

msg = "Hello World"
print(msg)
print(msg.capitalize())
print(msg.upper())
arr = msg.split()
arrLength = len(arr)
print("Array lenth: " + str(arrLength))

if 5 > 1:
    print('5 > 1 - ok')    

myFunc("Tom")
myFunc("Carl")
myFunc("John")

print(type(5.1))
print(type(5))
print(type("5"))

listing = ["apple", "banana", "cherry"]
print("listing size is " + str(len(listing)))
print("listing, index 0 is: " + listing[0])
print("listing, index 1 is: " + listing[1])
print("listing, index 2 is: " + listing[2])

user = {"name": "Tom", "age": 40}

print("user name: " + user.get("name"))
print("user age: " + str(user.get("age")))

print("random from 1 to 100 is: " + str(random.randrange(1, 100)))

print('''
multiline
text
example
''')

stringExample = "example string"
print(stringExample[0])
if ("ex" in stringExample):
    print("'ex' is in stringExample value")
if ("ex string" in stringExample):
    print("'ex string' is in stringExample value")
if ("ex string" not in stringExample):
    print("'ex string' is not in stringExample value")

print("part of string 2-5: " + stringExample[2:5])
print("part of string from start: " + stringExample[:5])
print("part of string from end: " + stringExample[5:])
print("replace example: " + stringExample.replace("example", "Hello"))