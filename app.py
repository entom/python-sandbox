import random


def myFunc(name):
    print("Hello!" + name + "!")


msg = "Hello World"
print(msg)
print(msg.capitalize())
print(msg.upper())
arr = msg.split()
arrLength = len(arr)
print("Array length: " + str(arrLength))

if 5 > 1:
    print('5 > 1 - ok')

myFunc("Tom")
myFunc("Carl")
myFunc("John")

print(type(5.1))
print(type(5))
print(type("5"))
print(5 > 2)

listing = ["apple", "banana", "cherry"]
print(listing)
print("listing size is " + str(len(listing)))
print("listing, index 0 is: " + listing[0])
print("listing, index 1 is: " + listing[1])
print("listing, index 2 is: " + listing[2])

user = {"name": "Tom", "age": 40}

print("user type is", type(user))
print("user keys:", user.keys())
print("user name: " + user.get("name"))
print("user age: " + str(user.get("age")))
user["age"] = 50
print("user age: " + str(user.get("age")))
print("user:", user)
user['zip'] = 44300
print("user:", user)
user.update({"age": 60})
print("user:", user)

print("random from 1 to 100 is: " + str(random.randrange(1, 100)))
randomString = "random from 1 to 100 is: {}, {}, {}"
print(randomString.format(random.randrange(1, 100), random.randrange(1, 100), random.randrange(1, 100)))

print('''
multiline
text
example
''')

stringExample = "example string"
print(stringExample[0])
if "ex" in stringExample:
    print("'ex' is in stringExample value")
if "ex string" in stringExample:
    print("'ex string' is in stringExample value")
if "ex string" not in stringExample:
    print("'ex string' is not in stringExample value")

print("part of string 2-5: " + stringExample[2:5])
print("part of string from start: " + stringExample[:5])
print("part of string from end: " + stringExample[5:])
print("replace example: " + stringExample.replace("example", "Hello"))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for n in numbers:
    print("number: " + str(n))
for i in range(len(numbers)):
    print("number: " + str(numbers[i]))

j = 0
while j < len(numbers):
    print("while - number: " + str(numbers[j]))
    j += 1

print(numbers)
print(numbers[2:5])
print(numbers[8:])
print(numbers[:3])
print("5" in numbers)
print("15" not in numbers)
print("19" in numbers)
print(numbers)
numbers[1] = numbers[2]
print(numbers)
numbers.insert(13, 13);
numbers.insert(14, 14);
numbers.insert(15, 15);
print(numbers)
numbers.append(16)
numbers.append(17)
numbers.append(18)
print(numbers)
numbers.extend([19, 20, 21])
print(numbers)
numbers.append("number1")
numbers.append("number2")
print(numbers)
numbers.remove("number2")
print(numbers)
numbers.pop(len(numbers) - 1)
print(numbers)
numbers.pop()
print(numbers)

newNumbers = [x for x in numbers if x < 5]
print('newNumbers', newNumbers)

numbers.clear()
print(numbers)

colors = ["yellow", "red", "green", "orange", "blue", "black"]
print('colors', colors)
colors.reverse()
colorCopy = colors.copy()
colorCopySecond = list(colors)
print('colors - reverse', colors)
colors.sort()
print('colors', colors)
colors.sort(reverse=True)
print('colors', colors)
print('colors-copy-1', colorCopy)
print('colors-copy-2', colorCopySecond)
colorSum = colorCopy + colors
print('color-sum', colorSum)
colorCopy.extend(colorCopySecond)
print('colorCopy - extend with second list', colorCopy)

itemsTuple = ('square', 'triangle', 'circle')
print('itemsTuple', itemsTuple)
print('itemsTuple: index 0 is', itemsTuple[0])
print('itemsTuple: index 1 is', itemsTuple[1])
print('itemsTuple: index 2 is', itemsTuple[2])

listItems = list(itemsTuple)
listItems.append('other')
itemsTuple = tuple(listItems)
print('itemsTuple', type(itemsTuple), itemsTuple)
(item1, item2, item3, item4) = itemsTuple
print('items from tuple: ', item1, item2, item3, item4)
(itemA, *itemB) = itemsTuple
print('items from tuple: ', itemA, itemB)

setOfColors = {'yellow', 'orange', 'red'}
print('set-of-colors', type(setOfColors), setOfColors)
for x in setOfColors:
    print('item from set of colors: ' + x)
setOfColors.add('purple')
print('set-of-colors', setOfColors)
setOfColors.discard('orange')
print('set-of-colors', setOfColors)
setOfColorsLight = {'light1', 'light2', 'light3'}
setOfColors.update(setOfColorsLight)
print('set-of-colors', setOfColors)
