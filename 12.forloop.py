#find multiplication
num= int(input("Enter the number: "))
print(f"The number is {num}")
for i in range(1, 11):
    print(f"{num} * {i} =", num*i)

name = input("Enter your name: ")

for ch in name:
    print(ch)


#find number of vowels and display
word=input("Enter a word: ")
count=0
vowels_found=" "

for ch in word:
    if ch in "AEIOUaeiou":
        count+=1
        vowels_found +=ch + " "

print("Number of vowels: ", count)
print("Vowels are : ", vowels_found)

#three arguments 
for k in range(1, 11, 2):
    print(k)
    

