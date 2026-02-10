course={
    "name":"python",
    "learner":"Darpan"
}
#iterating over dictionary
for y in course: #to print each key not values
    print(y)

#access values of dictionary
for y in course: 
    print(course[y])

#accessiing values using value() methods
for y in course.values(): 
    print(y)

#accessing key using key() methods
for y in course.keys(): 
    print(y)

#accessing key using key() and values() methods
for x,y in course.items(): 
    print(x,y)

