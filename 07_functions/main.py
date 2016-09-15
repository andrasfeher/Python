def doNothing():
    pass # indicate that the function is empty intentionally

def makeSound():
    print('quack')

def agree():
    return True

def echo(anything):
    return anything + ' ' + anything

# default argument values are calculated when the function is defined
# not when it is run
def menu(wine, entree, dessert = 'pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

# * gathers the list of arguments into tuple
# nothing to do with pointers
def variableNumberOfArguments(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

# ** gathers into dictionary
# again: nothing to do with pointers
def argumentsAsDict(**kwargs):
    print('Keyword arguments:', kwargs)

# docstrings: document the function
def documentedFunction(anything):
    'returns its input argument'
    return anything

# longer documentation
def documentedFunctionWithLongDocumentation(anything):
    '''
    returns its input argument
    second line
    third line
    '''
    return anything

def answer():
    print(42)

def runSomething(func):
    func()

def addArgs(arg1, arg2):
    print(arg1 + arg2)

def runSomethingWithArgs(func, arg1, arg2):
    func(arg1, arg2)

def sumArgs(*args):
    return sum(args)

def runWithPositionalArgs(func, *args):
    return func(*args)

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


# closure: a function that is dynamically generated by another function and
# can change and remember the values of variables that were created outside
# the function
def knights(saying):
    def inner():
        return "We are the knights who say: '%s'" % saying
    return inner()

def editStory(words, func):
    for word in words:
        print(func(word))

# generator: sequence creator object: range()

# decorator: function that takes one function as input and returns another
# function
def documentIt(func):
    def newFunction(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return newFunction

def squareIt(func):
    def newFunction(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return newFunction


# alternative to the manual decorator assingment
@documentIt
@squareIt
def addInts(a, b):
    return a + b


# use the "global" keyword to change variable outside of the function
def changeAndPrintGlobal():
    global animal
    animal = 'wombat'
    print('inside function:', animal)

# locals(): returns a dictionary of the contents of the local namespace
def showLocals():
    animal = 'wombat'
    print('locals:', locals())

doNothing()
makeSound()

if agree():
    print('Agreed!')
else:
    print('That was unexpected')

print(echo('András'))

# positional arguments
print(menu('chardonnay', 'chicken', 'cake'))

# keyword arguments
print(menu(wine = 'chardonnay', entree = 'chicken', dessert = 'cake'))

# mix positional and keyword arguments just positional need to come first
print(menu('chardonnay', dessert = 'cake', entree = 'chicken'))

# using the default
print(menu('chardonnay', entree = 'chicken'))

variableNumberOfArguments('param1', 'param2', 1, 2, 33, 4)

argumentsAsDict(wine='merlot', entree='mutton', dessert='macaroon')

# print the function docstring
# help(documentedFunction)
# help(documentedFunctionWithLongDocumentation)

# just the raw docstring, without the formatting
print(documentedFunction.__doc__)

answer()
runSomething(answer)
runSomethingWithArgs(addArgs, 2, 5)
print(runWithPositionalArgs(sumArgs, 1, 2, 3, 4))
print(outer(4, 7))

print(knights('Duck'))

# lambda function example
stairs = ['thud', 'meow', 'thud', 'hiss']
editStory(stairs, lambda word: word.capitalize() + '!')

# decorator
# print(addInts(3, 4))
# decoratedAddInts = documentIt(addInts)
# decoratedAddInts(2, 4)

# test automatic decorator assingment
addInts(234, 234)

# test global
animal = 'fruitbat'
print(animal)
changeAndPrintGlobal()
print(animal)

# test locals() and globals()
animal = 'fruitbat'
showLocals()
print('globals:', globals())
print(animal)