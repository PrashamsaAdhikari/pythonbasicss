#map() applies a function to every element in an iterable (like list, tuple).
numbers = [1, 2, 3, 4]

def square(x):
    return x ** 2

result = map(square, numbers)
print(list(result))
 

 #using lambda
numbers = [1, 2, 3, 4]
result = map(lambda x: x**2, numbers)
print(list(result))



#with filter
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))



#with reduce
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)
print(result)

"""
reduce() takes two elements at a time from a list (or iterable), applies a function, and then uses the result with the next element. It keeps going until there’s only one value left.
Think of it as folding a list into a single value.

map() applies a function to every element of a list (or any iterable) and gives you a new collection of results.
Think: “Do something to each item in the list.”

lambda Definition: Creates a small anonymous function in one line, usually for quick use in map, filter, or reduce.
Think: “A tiny function without a name that you can use on the fly.”


filter() Definition: Goes through each element of a list (or iterable), applies a condition, and keeps only the items where the condition is True.
Think: “Sift through the list and keep only the items that pass the test.”
"""