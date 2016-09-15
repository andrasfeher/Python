import re

# Precompile the patterns
regexes = [ re.compile(p) for p in ['this', 'that'] ]

text = 'Does this text match the pattern?'

print('Text: %r\n' % text)

for regex in regexes:
    print('Seeking "%s" ->' % regex.pattern)

    if regex.search(text):
        print('match!')
    else:
        print('no match')

# findall function returns all substrings of the iput that match the pattern
# without overlapping

text = 'abbaaabbbbaaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
    print('Found "%s"' % match)


# finditer returns an iterator that produces Match instanaces instead of the
# strings returned by findall()

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))
