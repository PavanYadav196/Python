# =============================================================
# Set in Python
# =============================================================

# thisSet = {"Pavan","Pavan", "Ravan", "Kavan",1,True,0,False}
# print(len(thisSet))
# print(thisSet)
# for x in thisSet:
#   print(x)


# Set Items - data types

# set1={"Pavan","Ravan","Kavan"}
# set2={1,2,3,4,5}
# set3={True,False,True}

# print(set1)
# print(set2)
# print(set3)

# set = {"Pavan", "Yadav", 1, 2, False}
# print(type(set))


# Set() constructor
# thisSet = set(("Apple", "Banana", "Kiwi"))
# print(type(thisSet))
# print(thisSet)
# print("Apple" in thisSet)


# Adding and removing set values
# Creating empty set
# thisSet= set()
# thisSet.add("Guvava")
# creating another set
# anotherSet={"Apple","Banana","Kiwi","Pineapple"}
# updating the set
# thisSet.update(anotherSet)

# adding iterable object in python
thisSet={"Apple","Kiwi","Guvava"}
myList=["Pineapple","Banana"]
thisSet.update(myList)
print(thisSet)

# Removing the value in set in python

