# create a file with open()
fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file = fout)
fout.close()


# test the existence with exists()
import os
print(os.path.exists('oops.txt'))

# check file type
name = 'oops.txt'
print(os.path.isfile(name))
print(os.path.isdir(name))

# check if path is absolute
print(os.path.isabs('/big/fake/name'))

# copy file
import shutil
shutil.copy('oops.txt', 'ohno.txt')

# rename
import os
os.rename('ohno.txt', 'ohwell.txt')


# create hard link
if os.path.exists('yikes.txt'):
    os.unlink('yikes.txt') # or remove(...)

if os.path.exists('jeepers.txt'):
    os.unlink('jeepers.txt') # or remove(...)

os.link('oops.txt', 'yikes.txt')
print(os.path.isfile('yikes.txt')) # true
print(os.path.islink('yikes.txt')) # false

os.symlink('oops.txt', 'jeepers.txt')
print(os.path.islink('jeepers.txt')) # true

# change permission
# os.chmod('oops.txt', 0o400)

# or you can use constants
# import stat
# os.chmod('oops.txt', stat.S_IRUSR)

# get path
print(os.path.abspath('oops.txt'))

# get symlink pathname with realpath
print(os.path.realpath('jeepers.txt'))

# directory manipulation
if os.path.exists('poems'):
    os.rmdir('poems')

os.mkdir('poems')
print(os.listdir('..'))

# change current directory
import os
os.chdir('/')
print(os.listdir('.'))

# list matching files/directories with glob()
import glob
print(glob.glob('m*'))
print(glob.glob('???')) # three letter files/directories
print(glob.glob('[klm]*a')) # begins with 'k', 'l', or 'm' and ends with 'a'

# get the process id and current directory
import os
print(os.getpid())
print(os.getcwd())

# get my user and group id
print(os.getuid())
print(os.getgid())

# start another program and get the output
import subprocess

ret = subprocess.getoutput('date') # you won't get back anything until the process ends
print(ret)

# show the exit status
ret = subprocess.getstatusoutput('date')
print(ret)
