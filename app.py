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