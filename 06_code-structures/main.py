# continue long line
alphabet = 'a' + \
'b' + \
'c'
print(alphabet)

# if; don't need parenthesis for test
# recommended style is PEP-8 (Python Enhancement Proposals)
trafficLight = 'red'
if trafficLight == 'red':
    print("Don't go")
elif trafficLight == 'yellow':
    print("Wait a while")
else:
    print("Go!")

# considered false:
# boolean False
# null None
# zero integer 0
# zero float 0.0
# empty string ''
# empty list
# []
# empty tuple ()
# empty dict {}
# empty set set()
aList = []
if aList:
    print('Not empty')
else:
    print('Empty')

# while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# cancel with break
# while True:
#    stuff = input("String to capitalize [type q to quit]: ")
#    if stuff == "q":
#        break
#    print(stuff.capitalize())

# skip ahead with continue
# while True:
#     value = input("Integer, please [q to quit]: ")
#     if value == 'q':
#         break
#     number = int(value)
#     if number % 2 == 0:
#         continue
#     print(number, 'squared is', number * number)

# check break use
numbers = [1, 3, 5, 6]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else: # break not called
    print('No even number found')

# iterate with for
numbers = [1, 3, 5, 6]
for number in numbers:
    print(number)

phonebook = {
    'Tercsi': '1234',
    'Fercsi': '233445',
    'Kata': '384576',
    'Klára' : '459983745'
}

for name in phonebook.keys():
    print(name)

for phoneNumber in phonebook.values():
    print(phoneNumber)

for item in phonebook.items():
    print(item)

# check break use with else
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else: # no break means no cheese
    print('This is not much of a cheese shop, is it?')

# iterate multiple sequences with zip() in parallel
# stops when the shortest sequence ends
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding'] # pudding is not printed
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

# build English - Frech dictionary
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(dict(zip(english, french)))


# range
for x in range(0, 3):
    print(x)

# range from 2 down to 0
for x in range(2, -1, -1):
    print(x)

# even numbers
print(list(range(0, 11, 2)))

# comprehension
number_list = [number for number in range(1,6)]
print(number_list)

# comprehension to create odd number list
oddNumberList = [number for number in range(1,6) if number % 2 == 1]
print(oddNumberList)

# comprehension using nested loop
# for row .., and for col... can also have their own test
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

# dictionary comprehensions
# set is used to avoid the multiple counting of the same letter
# the result is the same, but it is more 'pythonic'
text = 'letters'
letterCounts = {letter: text.count(letter) for letter in set(text)}
print(letterCounts)

# set comprehension
# set of odd numbers
oddSet = {number for number in range(1, 6) if number % 2 == 1}
print(oddSet)
