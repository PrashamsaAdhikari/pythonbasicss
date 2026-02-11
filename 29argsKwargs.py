#*args
nums = [2,5,7,1,9]
print(nums)
print(*nums)


def add_numbers(*args):
    total=0
    for num in args:
        total+=num
    return total
    
print(add_numbers(2,3,4,5,4))    
print(add_numbers(2,4))
print(add_numbers(4))
print(add_numbers(2,3,4,5,4,5,6,7,8))

#**kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Kathmandu")

