phonebook = {
    'Tercsi': '1234',
    'Fercsi': '233445',
    'Kata': '384576',
    'Klára' : '459983745'
}

# add new item
phonebook['Izolda'] = '384756'

# test if key exists in dictionary
print('Tercsi' in phonebook)
print('Béla' in phonebook)

# get value
print(phonebook['Tercsi'])

# runtime error:
# print(phonebook['Béla'])

# .get() method returns second parameter if key does not exist
print(phonebook.get('Béla', 'Not in the phonebook!'))
print(phonebook.get('Tercsi', 'Not in the phonebook!'))

# get all keys in iteratable dict_keys format
print(phonebook.keys())

# get all the values from the dictionary
print(phonebook.values())
print(list(phonebook.values())) # converted to list

# get all key-value pairs
print(phonebook.items())
print(list(phonebook.items())) # converted to list

# assign with =, copy with copy()
# ...

# combine dictionaries
newFriends = {
    'qqqq': '723645',
    'kdfhg': '348576'
}

phonebook.update(newFriends)
print(phonebook)

# delete item
del phonebook['qqqq']
print(phonebook)

# delete all items
phonebook.clear()
print(phonebook)
