from collections import defaultdict
from math import ceil


# getting discount percentage from user
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


# splitting shared meals between diners
prices_and_names = defaultdict(int)
if input("Any shared meals? type 'y' for Yes, any other key for No. \n>> ").lower() == 'y':
    try:
        shared_meal = input("shared meal - write all names, and then the price at the end. \n"
                             "example: itay dan harel 79. press enter to end \n>> ").split()
        names = [x for x in shared_meal if x.isalpha()]
        prices = [x for x in shared_meal if x.isdigit()]
        
total_meal_price = lambda prices: 
        shared_price = ceil(int(shared_meals[-1])/len(names))
        for name in names:
            prices_and_names[name] += shared_price
        print(prices_and_names.items())
    except ValueError:
        print("value error")



prices_before_discount = input("price before discount - name + price: ").split()
for i in range(len(prices_before_discount)):
    if i%2 != 1:
        prices_and_names[prices_before_discount[i]] += int(prices_before_discount[i + 1])

for name, price in prices_and_names.items():
    price_after_discount = price*discount_percentage
    price_with_tip = price_after_discount + price*0.1
    print(f"For {name}: Original price: {price} ==> After discount: {price_after_discount.__round__()}"
          f" ==> With tip: {price_with_tip.__round__()}")

