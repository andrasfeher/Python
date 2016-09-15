# lists
empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
another_empty_list = list()

# convert string to list
print(list('cat'))

# convert a tuple to a list
print(list(('ready', 'fire', 'aim')))

# split string to list
birthday = '2/1/1967'
print(birthday.split('/'))

# get an item using offset
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])


# lists of lists
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]

print(all_birds)
print(all_birds[0])
print(all_birds[1][0])


# change an item
marxes[2] = 'Wanda'
print(marxes)

# get a slice
print(marxes[0:2])

# step is also valid here like strings
print(marxes[::2])
print(marxes[::-2]) # from right to left
print(marxes[::-1]) # reverse the list

# append
marxes.append('Zeppo')
print(marxes)

# merge one list into another
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

# alternative extend
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

# append does not extend: it adds the list as a single list item
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo', ['Gummo', 'Karl']]

# insert into the list
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.insert(3, 'Gummo') # inserts to the 4th place
print(marxes)

# delete by offset from list
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
del marxes[-1] # deletes 'Harpo'
print(marxes)

# delete by name from list
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.remove('Gummo')
print(marxes)

# implement pop
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop()) # removes Zeppo
print(marxes)
print(marxes.pop(1)) # removes Chico
print(marxes)

# find offset by name
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico')) # prints 1

# test if value is element of list
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes) # prints True

# count occurrences of value
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.count('Harpo'))

# convert to string with join
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(', '.join(marxes))

# sort list items
# sort() sorts in place
# sorted() returns sorted copy
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.sort()
print(marxes)

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse = True)
print(numbers)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(sorted(marxes))

# number of items in a list
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(len(marxes))

# assign with =, copy with copy()
a = [1,2,3]
b = a
a[0] = 'Suprise!'
print(b)

a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]
print(b)
print(c)
print(d)
