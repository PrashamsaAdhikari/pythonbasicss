try:
    l=[1,2,3,4,5]
    i=int(input("enter the index: "))
    print(l[i])
except:
    print("error error let's run sad sad")    
finally:
    print("Always executing sexy hahhahahh")

#raising custom error
age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative")

print("Your age is:", age)

 
