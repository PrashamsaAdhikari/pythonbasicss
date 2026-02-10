dic= {
    "pras": "human",
    "Spoon": "object"
}
print(dic["pras"])

#students roll no and name
students={
    "riya": 1,
    "siya": 2,
    "piya": 3,
    "diya": 4,
    "niya": 5,
    "iiya": 6,
    "kiya": 7,
    "ciya": 8,
}
print(students["kiya"])
print(students.get("niya"))

# for key in students.keys():
#     print(students[key])

for key, value in students.items():
    print(value)



'''
Method	What you get	How to use
keys()	key only	students[key]
values()	value only	print(value)
items()	(key, value) tuple	for k, v in items()
'''