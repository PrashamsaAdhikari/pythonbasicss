#calculate factorial of given number
while(True):
    n=int(input("Enter the number: "))
    print(f"The number is {n}")
    fact=1

    if(n==0):
        print("The factorial of your given number is 1")
    else: 
        for i in range(1, n+1):
                fact*=i

    print(f"The factorial is {fact}")            