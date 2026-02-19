# input are Rent, food groceries water and elcetricity
rsum = 0
while True:
    rent = input("Enter your rent price or 'q' to quit: ")
    if rent != 'q':
        rsum += int(rent)
        print("The total rent so far is", rsum)
    else:
        print("Total rent sum is", rsum)
        break

foodsum = 0
while True:
    food = input("Enter your food price or 'q' to quit: ")
    if food != 'q':
        foodsum += int(food)
        print("The total food sum so far is", foodsum)
    else:
        print("Total food sum is", foodsum)
        break


gsum = 0
while True:
    groceries = input("Enter your groceries price or 'q' to quit: ")
    if groceries != 'q':
        gsum += int(groceries)
        print("The total groceries sum so far is", gsum)
    else:
        print("Total groceries sum is", gsum)
        break

watersum = 0
while True:
    waterE = input("Enter your water & electricity price or 'q' to quit: ")
    if waterE != 'q':
        watersum += int(waterE)
        print("The total water & electricity sum so far is", watersum)
    else:
        print("Total water & electricity sum is", watersum)
        break

def total_expense(rent, food, grocery, water):
    return rent + food + grocery + water

final_total = total_expense(rsum, foodsum, gsum, watersum)
print("The overall total is:", final_total)


def div(a):
    return a/3

final_divided= div(final_total)
print("the money after divided is", final_divided)