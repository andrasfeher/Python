import re

text = 'This is some text -- with punctuation.'

print(text)
print

patterns = [
    (r'^(\w+)', 'word at start of string'),
    (r'(\w+)\S*$', 'word at end, with optional punctuation'),
    (r'(\bt\w+)\W+(\w+)', 'word starting with t, another word'),
    (r'(\w+t)\b', 'word ending with t'),
]

for pattern, desc in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print('Pattern %r (%s)\n' % (pattern, desc))
    print('   ', match.groups())
    print()


# group(): in single; useful when grouping is being used to find parts of the
# string, but some parts matched by groups are not needed in the results

# word starting with 't' then another word
regex = re.compile(r'(\bt\w+)\W+(\w+)')
match = regex.search(text)
print('Entire match:', match.group(0))
print('Word starting with "t":', match.group(1))
print('Word after "t" word:', match.group(2))

# named groups; syntax: (?P<name>pattern)
for pattern in [
    r'^(?P<first_word>\w+)',
    r'(?P<last_word>\w+)\S*$',
    r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
    r'(?P<ends_with_t>\w+t)\b',
    ]:

    regex = re.compile(pattern)
    match = regex.search(text)
    print('Matching "%s"' % pattern)
    print('   ', match.groups())
    print('   ', match.groupdict()) # dictionary group names - substrings from the match
    print
