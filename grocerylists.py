grocery_lists= {
      'mango' : 200 , 
      'pineapple' : 500, 
      'orange' : 600
}
def print_grocery_list(saman):
   for saman, price in saman.items():
        print(f"{saman} : Rs {price}")

print_grocery_list(grocery_lists)

name= input("Enter name: ")
if(name in grocery_lists):
   print(grocery_lists[name])

else:
#add name
  price= input("Enter price: ")
  grocery_lists[name]=price

print_grocery_list(grocery_lists)


