nums = int(input("Enter a number: "))

def facto(nums):
    fact = 1
    for el in range(1,nums+1):
        fact *= el
    return fact

print(facto(nums))






