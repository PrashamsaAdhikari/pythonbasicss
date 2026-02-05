n=int(input("Enter your number: "))
if(n<=1):
    print(F"{n} id not prime number")
else:
    is_prime = True
    for i in range(2, int(n**0.50)+1):
        if n%i==0:
            is_prime=False
            break
if is_prime:
        print(f"{n} is prime")
else:
        print(f"{n} is not prime")



























#     def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# # Example usage
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")   