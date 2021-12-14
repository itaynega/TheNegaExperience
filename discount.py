from collections import defaultdict

prices_and_names = defaultdict(int)
discount_percentage = 1 - int(input("discount percentage: "))/100
if input("Any shared meals? type 'y' for yes. \n>> ").lower() == 'y':
    more = True
    while more:
        shared_meals = input("shared meals - write all name and price at the end. \n"
                             "example: itay dan harel 79. \n>> ").split()
        shared_price = int(shared_meals[-1])
        del(shared_meals[-1])
        for name in shared_meals:
            prices_and_names[name] += round(shared_price/3)
        print(prices_and_names.items())
        more = bool(int(input("are there more shared meals? 1 for y, 0 for no\n>>")))


prices_before_discount = input("price before discount - name + price: ").split()
for i in range(len(prices_before_discount)):
    if i % 2 != 1:
        prices_and_names[prices_before_discount[i]] += int(prices_before_discount[i + 1])

for name, price in prices_and_names.items():
    price_after_discount = price*discount_percentage
    price_with_tip = price_after_discount + price*0.1
    print(f"For {name}: Original price: {price} ==> After discount: {price_after_discount.__round__()}"
          f" ==> With tip: {price_with_tip.__round__()}")


