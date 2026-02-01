answer= int(input("Enter day (1-7)"))

match answer:
    case 1:
        print(f"you typed day{answer}. The day is Sunday")
    case 2:
        print(f"you typed day{answer}. The day is Monday")
    case 3:
        print(f"you typed day{answer}. The day is Tuesday")
    case 4:
        print(f"you typed day{answer}. The day is Wednesday")
    case 5:
        print(f"you typed day{answer}. The day is Thursday")
    case 6:
        print(f"you typed day{answer}. The day is Friday")
    case 7:
        print(f"you typed day{answer}. The day is Saturday")
    case _:
        print("Invalid: ERROR")
