#fstrings
#old
letter="my name is {} and i live in {}"
country="Nepal"
name="darpan"
print(letter.format(name, country))

#new
letter=f"my name is {name} and i live in {country}"
country="Nepal"
name="darpan"
print(letter)


#doc strings
def square(n):
    ''' take number and return '''
    print(n**2)
square(5)   
print(square.__doc__)