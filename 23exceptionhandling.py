
try:
    a=int(input("Enter your number: "))
    print(f"Multiplication of {a} is: ") 
    for i in range(1,11):
        print(f"{int(a)}*{i}= {int(a)*i}")
        
except ValueError:
    print("number entered is not integer")  

except IndexError:
    print("Index error")  

except Exception as e:
    print("Invalid!! YOYOYO") 

print("Life goes on babygrulllll")
print("YOYOYO")