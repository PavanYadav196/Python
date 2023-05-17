# Built-in data types

# Text Type: Str
# Numeric Types: int, float, complex
# Sequence Types:list,tuple,range
# Mapping Type: dict
# Set Type:set frozenset
# Boolean Type:bool
# Binary Types:bytes,bytearray,momoryview
# None Type : None Type

# String
x = 'Hello World!'
# Integer
x = 20
# Float
x = 20.5
# Complex
x = 1j
# List And Tuple
x = ['apple', 'banana', 'cherry']
y = ('apple', 'banana', 'cherry')


#  Control Flow tolls
x = int(input("Please enter integer: "))
# Please enter integr:19
if x < 0:
    x = 0
    print('Negatve changed to zero')
elif x == 0:
    print('x is zero')
elif x == 1:
    print('x is one')
else:
    print('print more')
