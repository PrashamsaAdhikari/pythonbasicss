name= input("What is your name? ")
hour=int(input("Insert the time in hour: "))
minutes=int(input("Insert the time in minutes: "))

if(hour<12):
    print(f"It's {hour} : {minutes} am")

else:
    print(f"It's {hour} : {minutes} pm")


if(hour<12):
    if(hour<=5):
        print("Hello early bird")
    print(f"Good morning {name}")


elif(hour<16):
     print("Good afternoon")

elif(hour<18):
     print("Good evening")

else:

    print("good nighttt")
