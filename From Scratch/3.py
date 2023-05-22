# ---------------------------------------------
# type conversion
# ----------------------------------------------
# import random
# x = 10
# y = 10.20
# z = 1j

# a = float(x)
# b = int(y)
# c = complex(z)

# print(type(a))
# print(type(b))
# print(type(c))

# print(random.randrange(1, 10))

# String literal // strings are array
# a = "Hello world"
# print(a[1])

# Looping through a string
# for p in "pavan":
#     print(p)

# ---------------------------------------------
# Data Types
# ---------------------------------------------
# Length in python
# def myfunc():
#     a = "hello World"
#     print(len(a))
#     if "hea" in a:
#         print("Yes, he is in hello world")
#     else:
#         print("Not in the list")


# myfunc()


# Slicing String
# c = "Hello World"
# print(c[0: 5])
# slice from start
# print(c[:8])
# slice to the end
# print(c[1:])


# ------------------------------------------------
# Modifying the strings
# ------------------------------------------------
# Modifying the string to lower,upper and in captilized cases
a = " Hello, World "
print(a.lower())

# removing the before and after spaces
# print(a.strip())

# Replacing the strings
print(a.replace("H", "j"))

# spliting the string
print(a.split(","))

# Concating two strings
a = "Hello"
b = " World"
concat = a + b
print(concat)

# formating the string
age = 36
txt = "Hello, This is Pavan Yadav, I'am {} Year Old."
print(txt.format(age))

quantity = 3
item = 10
price = 200

myOrder="I want {} pieces of item {} for {} ruppes"
print(myOrder.format(quantity,item,price))