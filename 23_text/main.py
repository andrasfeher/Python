import string

s = 'The quick brown fox jumped over the lazy dog.'

print(s)

# capitalize words
print(string.capwords(s))

# replace characters, just more efficient than replace()
leet = str.maketrans('abegiloprstz', '463611082562')
print(s.translate(leet))
