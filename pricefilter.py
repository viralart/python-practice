# def removed_dollar(dollar):
    
#     price = float(dollar.replace("$",""))
#     if(price > 20):
#         return price
#     else :
#         return None

# dollar = input()
# result = removed_dollar(dollar)
# print(result)



def removed_dollar(price):
    amount = float(price.replace("$",""))
    for el in price:
        if amount > 20: return amount
        else : return None


inventory_prices = ["$29.99","$9.99","$15.99","$49.99","$7.99","$10.00"]
result = removed_dollar(inventory_prices)
print(result)