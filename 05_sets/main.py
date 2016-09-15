empty_set = set() # {} would create an empty dictionary
print(empty_set)
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}

# convert other data types to set
print(set('letters'))
print(set(['a', 'b', 'c']))

# test existence
print(0 in even_numbers)
print(3 in even_numbers)

# intersection
my_favourite_numbers = {7, 3}
print(even_numbers & odd_numbers)
print(my_favourite_numbers & odd_numbers)

# union
print(even_numbers | odd_numbers)

# difference
print(odd_numbers - my_favourite_numbers)

# XOR: items in one set or the other, but not both
print(odd_numbers ^ my_favourite_numbers)

# is subset
print(my_favourite_numbers <= odd_numbers)

# is proper subset
print(my_favourite_numbers < odd_numbers)

# is superset
print(odd_numbers >= my_favourite_numbers)

# is proper superset
print(odd_numbers > my_favourite_numbers)
