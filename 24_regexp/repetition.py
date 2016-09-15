from pattern_syntax import test_patterns

test_patterns(
    'abbaabbba',
    [('ab*', 'a followed by zero or more b'),
     ('ab+', 'a followed by one or more b'),
     ('ab?', 'a followed by zero or one b'),
     ('ab{3}', 'a followed by three b'),
     ('ab{2,3}', 'a followed by two to three b'),
     ]
)

# turn off greediness by following the repetition instruction with ?
test_patterns(
    'abbaabbba',
    [('ab*?', 'a followed by zero or more b'),
     ('ab+?', 'a followed by one or more b'),
     ('ab??', 'a followed by zero or one b'),
     ('ab{3}?', 'a followed by three b'),
     ('ab{2,3}?', 'a followed by two to three b'),
     ]
)

# character sets
test_patterns(
    'abbaabbba',
    [('[ab]', 'either a or b'),
     ('a[ab]+', 'a followed by one or more a or b'),
     ('a[ab]+?', 'a followed by one or more a or b not greedy')
     ]
)

# ^: loook for characters not in the set following
test_patterns(
    'This is some text -- with punctuation.',
    [('[^-. ]+', 'sequences without -, ., or space')
     ]
)

# character ranges
test_patterns(
    'This is some text -- with punctuation.',
    [('[a-z]+', 'sequences of lowercase letters'),
     ('[A-Z]+', 'sequences of uppercase letters'),
     ('[a-zA-Z]+', 'sequences of lowercase or uppercase letters'),
     ('[A-Z][a-z]+', 'one uppercase followed by lowercase')
     ]
)

# metacharacter dot (.): any single character in that position
test_patterns(
    'abbaabbba',
    [('a.', 'a followed by any one character'),
     ('b.', 'b followed by any one character'),
     ('a.*b', 'a followed by anything, ending in b, greedy'),
     ('a.*?b', 'a followed by anything, ending in b, non-greedy')
     ]
)

# escape codes
# r: raw string, \ is not an escape character
test_patterns(
    'A prime #1 example!',
    [(r'\d+', 'sequence of digits'),
     (r'\D+', 'sequence of nondigits'),
     (r'\s+', 'sequence of whitespace'),
     (r'\S+', 'sequence of nonwhitespace'),
     (r'\w+', 'alphanumeric characters'),
     (r'\W+', 'nonalphanumeric characters'),
     ]
)

# match the characters that are part of the regular expression syntax with
# backslash
test_patterns(
    '\d+ \D+ \s+',
    [(r'\\.\+', 'escape code'),
     ]
)

# anchoring
test_patterns(
    'This is some text -- with punctuation.',
    [(r'^\w+', 'word at start of string'),
     (r'\A\w+', 'word at start of string (same as caret)'),
     (r'\w+\S*$', 'word near end of string'),
     (r'\w+\S*\Z', 'word near end of string (same as $)'),
     (r'\w*t\w*', 'word containing t'),
     (r'\bt\w+', 't at start of word'), # \b: Empty string at the beginning or end of a word
     (r'\w+t\b', 't at end of word'),
     (r'\Bt\B', 't, not start or end of word'),# \B: Empty string not at the beginning or end of a word
     ]
)

# groups
test_patterns(
    'abbaaabbbbaaaaa',
    [('a(ab)', 'a followed by literal ab'),
     ('a(a*b*)', 'a followed by 0-n a and 0-n b'),
     ('a(ab)*', 'a followed by 0-n ab'),
     ('a(ab)+', 'a followd by 1-n ab'),
     ]
)
