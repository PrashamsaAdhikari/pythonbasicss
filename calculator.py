#python program to keep adding stream of number inputed by user and stop as soon as user press q on keyboard

sum=0
while(True):
    userInput=input("Enter your price: ")
    if(userInput!='q'):
        sum+=int(userInput)
        print("The total so far is", sum)

    else:
        print("Total sum is", sum)   
        print("Thank you for Shopping with us")
