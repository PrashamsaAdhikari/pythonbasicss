#conditional statement
a=int(input("Enter your age: "))
print("The age is", a)

print(a==18)
print(a>18)
print(a<18)
print(a!=18)
if(a>=18):
    print(f"your age is {a}. so you can drive")

else:
    print("your age is", a, "so you cannot drive")