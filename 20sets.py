s={2,4,2,6} #set (set do not contain duplicate items) doesn't maintain order can't use index
s1=[2,4,2,6] #list
s2=(2,4,2,6) #tuple (immutable)
print(s)
print(s1)
print(s2)


harry=set()
print(type(harry))

harry={}
print(type(harry))

for value in s1:
    print(value)


p1={1,2,3,4,5}
p2={2,5,7,8,5}
print(p1.union(p2))
print(p1.intersection(p2))
print(p1.difference(p2))
