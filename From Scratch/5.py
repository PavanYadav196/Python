#-------------------------------------------------------------
# Lists in Python
# ------------------------------------------------------------

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
# thisList = ["Pavan", "Ravan", "Ravi", "Pankaj"]

# for index, x in enumerate( thisList):
#     print(index, x)

# for value in range(len(thisList)):
#     print(value, thisList[value])


#  Print Using While Loop
# i=0
# while i < len(thisList):
#     print(thisList[i])
#     i=i+1


# Print using list comprehension
# [print(x) for x in thisList]

# fruits = ["Apple", "Banana", "Kiwi", "Mango"]
# newList = [x for x in fruits if 'a' in x]
# newList1 = [x for x in fruits if x != "Mango"]
# print(newList)
# print(newList1)


# for x in fruits:
#     if 'a' in x:
#         newList.append(x)
# print(fruits)
# print(newList)


# Iterables in Python
# thisList=["Pavan","Rajesh","Yadav"]
# newList=[x for x in range(4)]
# print(newList)


# Sorting in Python
# thisList = ["Mango", "Kiwi", "Pineapple", "Banana", "Orange"]
# thisList.sort()
# print(thisList)

# thisNum = [100, 50, 20, 55, 60, 90]
# thisNum.sort()
# print(thisNum)

# # Sorting Descending
# thisList.sort(reverse=True)
# print(thisList)

# -------------------------Copying a List----------------------------
# Copy() Method
thisList=["Pavan","Ravi","Kshitij","Mitesh"]
newList=thisList.copy()
# print(newList)

# thisList = ["Pavan", "Ravi", "Kshitij", "Mitesh"]
# list() Method
# myList = list(thisList)
# print(myList)
for i in range(0,len(thisList)):
    dic1 = {thisList[i]:newList[i]}
    print(dic1)


# -----------------------------------------Joining a List---------------------------------------

# first is to use append() method
# list = ['a', 'b', 'c']
# list1 = [1, 2, 3]

# for x in list1:
#     list.append(x)

# print(list)
# print(list1)

# # or you can use extend method
# list = ['Pavan', 'Rajesh', 'Yadav']
# list2 = [1, 2, 3]
# list.extend(list2)
# print(list)
