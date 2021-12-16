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
        discount_percentage_multiplier = 1 - discount_percentage/100
    return discount_percentage_multiplier


# splitting shared meals between diners
def get_shared_meals(defaultdict_of_names_and_prices):
    if input("Any shared meals? type 'y' for Yes, any other key for No. \n>> ").lower() == 'y':
        while True:
            shared_meals = input("shared meals - write all names who shared and prices of the meals that were shared, no matter the order. \n"
                             "example: 56 itay dan harel 79. press enter to end \n>> ").split()
            names = [x for x in shared_meals if x.isalpha()]
            prices = [int(x) for x in shared_meals if x.isdigit()]
            total_meals_price = 0
            total_meals_price = lambda prices: total_meal_price + x for x in prices
            shared_price = ceil(total_meals_price/len(names))
            for name in names:
                defaultdict_of_names_and_prices[name] += shared_price
            if input("Any more shared meals? type 'y' for Yes, any other key for No. \n>> ").lower() != 'y':
                break
            print(defaultdict_of_names_and_prices.items())
            return defaultdict_of_names_and_prices

 def get_individual_meal(defaultdict_of_names_and_prices):
    individual_meals = input("individual_meals - write the name of the dinner and all the prices of all the things he ordered. \n"
                             "press 'd' and enter to end. \n>> "
    while individual_meals != 'd':
        
        
        
        
prices_before_discount = input("price before discount - name + price: ").split()
for i in range(len(prices_before_discount)):
    if i%2 != 1:
        prices_and_names[prices_before_discount[i]] += int(prices_before_discount[i + 1])

for name, price in prices_and_names.items():
    price_after_discount = price*discount_percentage
    price_with_tip = price_after_discount + price*0.1
    print(f"For {name}: Original price: {price} ==> After discount: {price_after_discount.__round__()}"
          f" ==> With tip: {price_with_tip.__round__()}")

