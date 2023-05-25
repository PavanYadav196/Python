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
# x=("Apple","Banana","Kiwi")
# y=list(x)
# y[1]="Mango"
# print(y)


# Add items
# thisTuple=("Apple","Banana","Kiwi")
# y=list(thisTuple)
# y.append("Orange")
# print(y)


# Adding the new tuple into tuple
# thisTuple=("Apple","Banana","Kiwi")
# y=("Orange",)

# thisTuple += y
# print(thisTuple)


# Unpacking the tuples

# (one, two, *three) = fruits
# (one, *two, three) = fruits

# print(one)
# print(two)
# print(three)

# Loop through tuples
# for x in range(len(fruits)):
#   print(fruits[x])


# fruits = ("Apple", "Banana", "Kiwi", "Pineapple", "Guvava", "Mango")
numbers = (1, 2, 3, 4, 5)

# tupleJoin = fruits+numbers
# tupleJoin= numbers * 2
# print(tupleJoin)


# myCount=numbers.count(5)
# print(myCount)

myIndex=numbers.index(3)
txt="The Position variable found is {} "
print(txt.format(myIndex))