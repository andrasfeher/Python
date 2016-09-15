# one element
one_marx = 'Groucho',
print(one_marx)

marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)

# parenthesis is not mandatory, you can use it to make tuple more visible
marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

# tuples let you assign multiple variables at once
# tuple unpacking
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a)
print(b)
print(c)

# you can use tuples to exchange values in one statement without
# using a temporary variable
a = 1
b = 2
a, b = b, a
print(a)
print(b)

# tuple() conversion makes tuples from other things
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))
