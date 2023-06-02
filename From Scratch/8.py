# ============================================================================
# Dictionary in Python
# ============================================================================

# thisDic = {
#     "Pavan": "Front-End Developer",
#     "Birth": "Badrinath",
#     "Things I Like": "Making Websites and Football",
#     "colors": ["Red", "White", "Black"]
# }

# print(thisDic["Pavan"])

# Length Of Directory
# print(len(thisDic))

# print(thisDic)

# The dict() Contstuctor
# thisDic = dict(name="Pavan Yadav", age=20, Passion="Web Developent")

# Accessing the property
# print(thisDic["name"])

# get
# x= thisDic.get("name")
# print(x)

# get keys
# y= thisDic.keys()
# print(y)

# thisDic["Internship"]="Yes"
# print(thisDic)

# x = thisDic.values()
# print(x)

# Accessing both key and value in python

# for key, value in thisDic.items():
#     print(key, value)
# for key in thisDic:
#   print(key, thisDic[key])

# get items()

# x=thisDic.items()
# print(x)

# Check Wheter ket exists or not
# if "name" in thisDic:
#   print("Yes it exists")


# Update ,change and adding in dictionary
# thisDic["Passion"]="Front-end Developer"
# print(thisDic)

# thisDic.update({"internship":"yes"})
# print(thisDic)


# Removing from dictionary
# poppedValue=thisDic.pop("internship")
# print(thisDic)
# print(poppedValue)

# poppedItem=thisDic.popitem()
# print(thisDic)
# print(poppedItem)

# Clearing dictionary
# thisDic.clear()
# print(thisDic)

# deleting the dictionary
# del thisDic
# print(thisDic)

# thisDic = dict()
# thisDic["Name"] = "Pavan Yadav"
# thisDic["Age"] = 20
# thisDic["Passion"] = "Web-Development"
# thisDic.update({"About": "My Name Is Pavan"})
# print(thisDic)

# for key in thisDic:
#   print(key,thisDic[key])

# Loop through dictionary in python
# for x in thisDic:
#   print(thisDic[x])

# for x in thisDic.values():
#   print(x)

# for x in thisDic.keys():
#   print(x)

# for x, y in thisDic.items():
#     print(x, y)


# myDict = thisDic.copy()
# print(myDict)

# thisDic["Ip Address"]='127.0.0.1'
# print(thisDic)

# print(thisDic)

# myDic=dict(thisDic)
# print(myDic)

# myDic["Age"]=20
# print(myDic)
# print(thisDic)

myFamily = {
    "Child 1": {
        "name": "Pavan Yadav",
        "age": 20
    },
    "Child 2": {
        "name": "Kavan Yadav",
        "age": 20
    },
    "Child 3": {
        "name": "Ravan Yadav",
        "age": 20
    }
}

# print(myFamily["Child 1"]["name"]["age"])
for key in myFamily:
    print(key,myFamily[key])

# values=myFamily.values()
# print(key,values)