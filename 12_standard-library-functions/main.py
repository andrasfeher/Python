# OrderedDict() remembers the order of key addition and returns them in the same
# order from an iterator
from collections import OrderedDict
from pprint import pprint

quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])

for stooge in quotes:
    print(stooge)

pprint(quotes)
