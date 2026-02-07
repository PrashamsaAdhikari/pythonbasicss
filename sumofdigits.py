n=int(input("Enter the number: "))
print(f"The number is {n}")

sum=0

while(n>0):
    last_digits=n%10
    sum+=last_digits
    n=n//10

print(f"the total sum is {sum}")
