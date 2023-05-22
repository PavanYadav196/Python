# =================================================================
# Tuples in Python
# =================================================================

# Tuple is collection which is ordered and unchangeable

# thisTuple=("apple","banana","kiwi")
# print(thisTuple)

# # Tuple Length
# print(len(thisTuple))

# # Creating the tuple with one variable
# thisTuple=("Apple",)
# print(type(thisTuple))

# thisTuple=("Apple")
# print(type(thisTuple))

# thisTuple = ("abc", 123, True, "def", False)
# print(type(thisTuple))

# Accessing the tuple
# print(thisTuple[0])

# Negetive Indexing
# print(thisTuple[-1])

# Specifying the range
# print(thisTuple[2:5])

# By not giving one value in pair either it start from top to bottom bottom to top
# print(thisTuple[0:])

# Checking whether item exist or not
# thisTuple = ("apple", "banana", "pineapple")
# if 'apple' in thisTuple:
#     print("Yes, value found.")
# else:
#     print("Not found.")


# Change Tuple Value
x=("Apple","Banana","Kiwi")
y=list(x)
y[1]="Mango"
print(y)
