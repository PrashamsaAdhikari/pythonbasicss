# a=int(input("Enter your time: "))

# if (a<12):
#     print("Good morning")
# elif (a==12):
#     print("noon")
# else:
#     print("good evening")

num=int(input("Enter a number: "))
print("The number is", num)

if(num<0):
  print("The number is negative")

elif(num>0):
  if (num<=10):
    print("The number is between 0 and 10")  
  elif(num>10 and num<=20 ):
    print("number is between 10 ans 20")
  else:
    print("number is greater than 0")


else:
  print("number is 0")

  
