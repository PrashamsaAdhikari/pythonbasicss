name=input("Enter your name: ")
hour=int(input("enter time in hour(in 24-hour format:"))
min=int(input("enter time in minutes: "))

print(f"The time is {hour}:{min}")

if(hour<=5):
    print("Early good morning", name)

elif(hour>5 and hour<12):
    print("Good morning", name)

elif(hour>=12 and hour<16):
    print("Happy Noon", name)

else:
    print("Good Evening", name)
   
