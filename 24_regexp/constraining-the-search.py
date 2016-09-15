import re

text = 'This is some text -- with punctuation.'
pattern = 'is'

print('Text   :', text)
print('Pattern:', pattern)

# not found as the pattern is not at the beginning of the text
# "match is a search with ^";
m = re.match(pattern, text)
print('Match   :', m)

s = re.search(pattern, text)
print('Search  :', s)

# Search the words containing 'is'
# less efficient than iterall()
# the search method of the compiled regular expression accepts optional start
# and end position parameters to limit the search to a substring of the input
pattern = re.compile(r'\b\w*is\w*\b')

print('Text:', text)
print()

pos = 0
while True:
    match = pattern.search(text, pos)
    if not match:
        break
    s = match.start()
    e = match.end()
    print('  %2d : %2d = "%s"' % (s, e-1, text[s:e]))

    # move forward in the text for the next search0
    pos = e
