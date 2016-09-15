shortList = [1, 2, 3]
position = 5
try:
    shortList[position]
except: # no arguments: catchall for any exception type
    print('Need a position between 0 and', len(shortList)-1, ' but got', position)


# catch IndexError first
# shortList = [1, 2, 3]
# while True:
#     value =  input('Position [q to quit]? ')
#     if value == 'q':
#         break
#     try:
#         position = int(value)
#         print(shortList[position])
#     except IndexError as err:
#         print('Bad index:', position)
#     except Exception as other:
#         print('Something else broke:', other)

# own exception
# class UppercaseException(Exception):
#     pass
#
# words = ['eeenie', 'meenie', 'miny', 'MO']
# for word in words:
#     if word.isupper():
#         raise UppercaseException(word)


# print the exception
class OopsException(BaseException):
    pass

try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)
