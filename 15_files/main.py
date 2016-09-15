# write text
message = 'Hello world'

fout = open('mytextfile.txt', 'wt') # t: text file; optional
fout.write('from fout:' + message + '\n')
print('from print:' + message, file=fout)
fout.close()

# using exception handler
try:
    fout = open('mytextfile.txt', 'xt')
    fout.write('anytext')
except FileExistsError:
    print('file already exists')


# read the whole file into memory at once
fin = open('mytextfile.txt', 'rt')
message = fin.read()
fin.close()
print(message)

# read the whole file in chunks
message = ''
fin = open('mytextfile.txt', 'rt')
chunk = 5

while True:
    fragment = fin.read(chunk) # read count characters at a time
    if not fragment:
        break
    message += fragment

fin.close()
print(message)


# read the file line by line
message = ''
fin = open('mytextfile.txt', 'rt')

while True:
    line = fin.readline()
    if not line:
        break
    message += line

fin.close()
print(message)

# the easiest way to read a text file: using an iterator
message = ''
fin = open('mytextfile.txt', 'rt')

for line in fin:
    message += line

fin.close()
print(message)

# readlines() returns a list of lines
fin = open('mytextfile.txt', 'rt')
lines = fin.readlines()
fin.close()
print(lines)

# read binary file
fin = open('logo.png', 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()

# write binary file
fin = open('logo.png', 'rb')
bdata = fin.read()
fin.close()

fout = open('logo2.png', 'wb')
fout.write(bdata)
fout.close()

# write binary file in chunks
fin = open('logo.png', 'rb')
bdata = fin.read()
fin.close()

fout = open('logo3.png', 'wb')
size = len(bdata)
offset = 0
chunk = 100

while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk

fout.close()


# close file automatically when the block of code finishes; normally or exception
with open('mytextfile.txt', 'wt') as fout:
    fout.write(message)

# write CSV files
import csv
phonebook = [
    ['Tercsi', '348756'],
    ['Fercsi', '349857'],
    ['Kata', '394857']
]

with open('phonebook.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(phonebook)

# read csv files
import csv

with open('phonebook.csv', 'rt') as fin: # context manager
    cin = csv.reader(fin)
    phonebook = [row for row in cin] # list comprehension

print(phonebook)

# read csv content as list of dictionaries
import csv

with open('phonebook.csv', 'rt') as fin: # context manager
    cin = csv.DictReader(fin, fieldnames = ['name', 'phone'])
    phonebook = [row for row in cin] # list comprehension

print(phonebook)

# write csv files with header
import csv
phonebook = [
    {'name':'Tercsi', 'phone':'348756'},
    {'name':'Fercsi', 'phone':'349857'},
    {'name':'Kata',   'phone':'394857'}
]

with open('phonebook.csv', 'wt') as fout:
    cout = csv.DictWriter(fout, ['name', 'phone'])
    cout.writeheader()
    cout.writerows(phonebook)

# read back the csv file
import csv

with open('phonebook.csv', 'rt') as fin: # context manager
    cin = csv.DictReader(fin)
    phonebook = [row for row in cin] # list comprehension

print(phonebook)


# json
phonebook = \
{
    'private': {
        'P Tercsi': '348756',
        'P Fercsi': '349857',
        'P Kata': '394857'
    },
    'official':{
        'O Tercsi': '348756',
        'O Fercsi': '349857',
        'O Kata': '394857'
    }
}

import json

# serialize to string
phonebookJSON = json.dumps(phonebook)
print(phonebookJSON)

# JSON string to data structure
ph = json.loads(phonebookJSON)
print(ph)


# configuration files
import configparser
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')
print(cfg['french']['greeting'])
print(cfg['files']['bin'])

# pickle module saves and restores and object in a special binary format
import pickle
import datetime

now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)

print(now1)
print(now2)

class Tiny():
    def __str__(self):
        return 'tiny'

obj1 = Tiny()
print(str(obj1))
pickled = pickle.dumps(obj1)
obj2 = pickle.loads(pickled)
print(str(obj2))
