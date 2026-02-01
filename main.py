"""""
is_member = False
level1 = 100
level2 = 300
discount = 0

price = input("Välkommen, köp något dyrt: ")
price = float(price)
if price > level1:
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
if price >= level2:
    print("Grattis! Du har avancerat till nivå 2 och 25% rabatt.")
    discount = discount + 25

final_price = price * (100 - discount) / 100
print("Efter rabatter blir priset.... " + str(final_price))

"""""

is_member = input("Are you a member? (y/n)")
level1 = 100
level2 = 300
discount = 0

if is_member == "y":
    print("Great! You are aloud to have discounts on your next bye")

    price = float(input("Välkommen, köp något dyrt: "))
    if price >= level2:  # and < level2:
        print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
        discount = discount + 25
        final_price = int(price * (100 - discount) / 100)
        print("Efter rabatter blir priset.... " + str(final_price) + "kr")
    elif price >= level1:
        print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
        discount = discount + 10
        final_price = int(price * (100 - discount) / 100)
        print("Efter rabatter blir priset.... " + str(final_price) + "kr")
    elif price < level1:
        print("Priset blir", price,"kronor")

    #final_price = int(price * (100 - discount) / 100)
    #print("Efter rabatter blir priset.... " + str(final_price) + "kr")
elif is_member == "n":
    print("No discounts for you!")

