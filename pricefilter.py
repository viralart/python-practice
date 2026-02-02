# def removed_dollar(dollar):
    
#     price = float(dollar.replace("$",""))
#     if(price > 20):
#         return price
#     else :
#         return None

# dollar = input()
# result = removed_dollar(dollar)
# print(result)



def clear_price(price):
    return float(price.replace("$",""))


inventory_prices = ["$29.99","$9.99","$15.99","$49.99","$7.99","$10.00"]
expensive_items = []
for p in inventory_prices:
    amount = clear_price(p)

    if amount > 20: 
        expensive_items.append(amount)

print(expensive_items)