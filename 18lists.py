#list
fruits= ["mango", "pineapple", "pear", "banana"]
fruits[1]="plum"
print(len(fruits))
fruits.append("strawberry")
fruits.insert(3, "strawberry")
fruits.pop(2)
for i in range(len(fruits)): #with index
  print(i,fruits[i])

for fruit in fruits:
  print(fruit)

print(fruits)

#list methods
"""
append()	
insert()	
remove()
pop()	
sort()
reverse()	
count()	
index()


Feature	List	Tuple
Brackets	[]	()
Mutable	✅ Yes	❌ No
Speed	Slower	Faster
Safety	Less	More
"""
