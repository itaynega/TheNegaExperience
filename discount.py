from collections import defaultdict
from math import ceil


# getting discount percentage from user
def get_discount_from_user():
    while True:
        try:
            discount_percentage = int(input("Discount percentage: "))
            if 0 <= discount_percentage < 100:
                break
            else:
                print("error. try again.")
        except ValueError:
            print("error. try again.")
    discount_percentage_multiplier = 1 - discount_percentage / 100
    return discount_percentage_multiplier


def get_meals(dict):
    instructions = "For every meal, write the price and people who shared the meal.\n" \
                   "If meal was individual, write only one name.\n" \
                   "If several meals were shared between same people, write all prices in the same line.\n" \
                   "Examples: \n" \
                   "- itay dan harel 37\n" \
                   "- alon 60 23\n"\
                   "- 40 erez dan 21\n"
    meals = input(f"{instructions}\n>> ").split()
    while 'd' not in meals:
        prices = [int(price) for price in meals if price.isdigit()]
        total_price = sum(prices)
        names = [str(name) for name in meals if name.isalpha()]
        if len(names) == 1:
            # an individual meal
            name = names[0]
            dict[name] += total_price
        elif len(names) > 1:
            # shared meal
            shared_price = ceil(total_price / len(names))
            for one_name in names:
                dict[one_name] += shared_price
        elif len(names) == 0:
            print("ERROR. Please type names: ")
        meals = input(">> ").split()


def total_of(dict):
    total = 0
    for key, value in dict.items():
        total += value
    return total


discount = get_discount_from_user()
receipt = defaultdict(int)
get_meals(receipt)
print(receipt.items())
print("total of -", total_of(receipt))

tip = 0.1
new_receipt = defaultdict(int)
for name, price in receipt.items():
    price_after_discount = ceil(price * discount)
    price_after_discount_and_tip = ceil(price * (discount + tip))
    new_receipt[name] += price_after_discount_and_tip
    print(f"For {name}: Original price: {price} ==> After discount: {price_after_discount}"
          f" ==> With tip: {price_after_discount_and_tip}")
print(new_receipt.items())
print("total of -", total_of(new_receipt), "with tip")
