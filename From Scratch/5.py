# Lists

# thisList = ["Apple", "Mango", "Kiwi", "Pineapple", "Apple","Guvava"]
# print(thisList)

# for x in thisList:
#     print(x)

# print(thisList[2:4])
# print(len(thisList))
# print(type(thisList))


# list1 = ["Apple", "Banana", "Kiwi"]
# list2 = [1, 2, 3, 4, 5]
# list3 = [True, False, True]

# for i in list1, list2, list3:
#   print(type(i))


# Append - To Insert from end of list use apped
# list.append("Kavan")
# print(list)

# Insert - To insert value in perticuler position use insert
# list.insert(2, "Savan")
# print(list)

# Extend - To Merge with other list or to append the other list into the current one.
# thisList = ["Ravi", "Sunny", "Pankaj"]
# list.extend(thisList)
# print(list)

# Adding tuples in list
# thisTupple = ("Hello", "World!")
# list.extend(thisTupple)
# print(list)

# Removing the the item from list

# remove() method
# list.remove("World!")
# print(list)

# pop () method - with this you can remove perticuler variable on that position
# list.pop(0)
# print(list)

# del method - delete method can delete specific or can completely delete variables
# del list[6]
# print(list)

# list = ["Pavan", "Ravan"]
# del list

# list=[]
# list.append("Pavan")
# list.append("Ravi")
# print(list)

# clear() method - it will clear the list but not the content
# list.clear()
# print(list)

# Loop through the list
thisList = ["Pavan", "Ravan", "Ravi", "Pankaj"]

for index, x in enumerate( thisList):
    print(index, x)

    # 0 : Pavan
    # 1 : Ravan
