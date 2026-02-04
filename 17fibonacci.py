n= int(input("Enter the number of terms: "))

a,b=0,1
fib_sum=0

if(n<=0):
    print("0")

elif(n==1):
    print("1")
    
else:
    print("Fibonacci series are: ")
    for i in range(a, n):
        print(a, end=" ")
        fib_sum +=a
        a,b=b,a+b

print("\nfib sum is ", fib_sum)
       