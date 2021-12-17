from collections import defaultdict
from math import ceil


# getting discount percentage from user
def getting_discount_from_user():
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


# splitting shared meals between diners
def get_shared_meals(defaultdict_of_names_and_prices):
    if input("Any shared meals? type 'y' for Yes, any other key for No. \n>> ").lower() == 'y':
        while True:
            shared_meals = input(
                "shared meals - write all names who shared and prices of the meals that were shared, no matter the order. \n"
                "example: 56 itay dan harel 79. press enter to end \n>> ").split()
            names = [x for x in shared_meals if x.isalpha()]
            prices = [int(x) for x in shared_meals if x.isdigit()]
            total_meals_price = sum(prices)
            shared_price = ceil(total_meals_price / len(names))
            for one_name in names:
                defaultdict_of_names_and_prices[one_name] += shared_price
            if input("Any more shared meals? type 'y' for Yes, any other key for No. \n>> ").lower() != 'y':
                break


def get_individual_meal(defaultdict_of_names_and_prices):
    individual_meals = input(
        "individual_meals - write the name of the dinner and all the prices of all the things he ordered. \n"
        "press 'd' and enter to end. \n>> ").split()
    while 'd' not in individual_meals:
        person_price = [int(x) for x in individual_meals if x.isdigit()]
        person_price = sum(person_price)
        person_name_as_list = [x for x in individual_meals if x.isalpha()]
        if len(person_name_as_list) == 1:
            person_name = ''
            for letter in person_name_as_list:
                person_name += letter
            defaultdict_of_names_and_prices[person_name] += person_price
        else:
            print("error. enter only one name.")
        individual_meals = input(">> ").split()


receipt = defaultdict(int)
discount = getting_discount_from_user()
get_shared_meals(receipt)
get_individual_meal(receipt)
print(receipt.items())

new_receipt = receipt
tip = 0.1
for name, price in new_receipt.items():
    new_receipt[name] = price * (discount + tip)
print(new_receipt.items())



'''
prices_before_discount = input("price before discount - name + price: ").split()
for i in range(len(prices_before_discount)):
    if i % 2 != 1:
        prices_and_names[prices_before_discount[i]] += int(prices_before_discount[i + 1])

for name, price in prices_and_names.items():
    price_after_discount = price * discount_percentage
    price_with_tip = price_after_discount + price * 0.1
    print(f"For {name}: Original price: {price} ==> After discount: {price_after_discount.__round__()}"
          f" ==> With tip: {price_with_tip.__round__()}")
'''
