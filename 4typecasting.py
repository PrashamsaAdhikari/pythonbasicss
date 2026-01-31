#type casting
#explicit conversion

string="4"
integernumber= 3
string_num= int(string)
sum= integernumber + string_num
print("the sum of given numbers is", sum)

print("the sum of given numbers is", integernumber + string_num)

print("the type of stringis", type(string))
print("the type of string_num is", type(string_num))


#implicit conversion
c=3
d=3.5
print(c+d)