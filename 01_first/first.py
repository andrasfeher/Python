print(61)

a=43
print(a)
print(type(a))
a //= 4
print(a)
print(a % 5)

print(0b10)
print(0x10)

print(int(True))
print(int(False))
print(int(86.4))
print(int('99'))

googol = 10 ** 100
print(googol)

print(float(True))
print(float(False))
print(float('98.4'))
print(float('-1.5'))


poem2 = '''I do not like thee, Doctor Fell.
The reason why, I cannot tell.
But this I know, and know full well:
I do not like thee, Doctor Fell.
'''
print(poem2)

print(99, 'bottles', 'would be enough')

bottles = 99
base = ''
base += 'current inventory: '
base += str(bottles)
print(base)

start = 'Na ' * 4 + '\n'
print(start)

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])
print(letters[2])
print(letters[3])
print(letters[20:])
print(letters[12:15])
print(letters[-3:])
print(letters[18:-3])
print(letters[-6:-2])
print(letters[::7])
print(letters[4:20:3])
print(len(letters))
print(letters.startswith('a'))
print(letters.endswith('a'))
print(letters.find('i'))
print(letters.rfind('i'))

name = 'Henny'
print(name.replace('H', 'P'))
print(name)
print('P' + name[1:])

todos = 'get gloves,get mask,give cat vitamins,call ambulance'
print(todos.split(','))

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)


poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem.startswith('All'))
print(poem.endswith('All'))

word = 'the'
print(poem.find(word))
print(poem.rfind(word))
print(poem.count(word))
print(poem.isalnum())

setup = 'a duck goes into a bar...'
print(setup.strip('.'))
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())
print('*****' + setup.center(30) + '******')
print('*****' + setup.ljust(30) + '******')
print('*****' + setup.rjust(30) + '******')
print(setup.replace('duck', 'marmoset'))
print(setup.replace('a', 'a famous ', 100))
