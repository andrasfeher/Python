# named tuple
# + looks and acts like an immutable onject
# + more space and time-efficient than objects
# + you can access attributes by using dot notation instead of dictionary-style []
# + you can use it as dictionary key

from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')

print(duck)
print(duck.bill)
print(duck.tail)


# make a named tuple from a dictionary
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)
