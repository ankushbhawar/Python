myDict = {
    "fast" : "In a Quick Manner",
    "ankush" : "A Coder",
    "marks" : [1,2,3],
    "anotherdict" : {"ankush" : "Developer"},
    1 : 2
}

print(myDict[1])
print(type(myDict.keys()))
print(list(myDict.keys()))
print(myDict.keys())
print(myDict.values())
print(myDict.items())

updateDict = {
    "hello" : "Ankush"
}

myDict.update(updateDict)
print(myDict)

print(myDict.get("ankush2"))
# print(myDict["ankush2"])