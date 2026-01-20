# nums = [1,4,9,16,25,36,49,64,81,100]

# for val in nums:
#     print(val)

nums = (1,4,9,16,25,36,49,64,81,100)

find = int(input("Enter the number to find: "))
index = 0
for el in nums:
    if (el == find):
        print("Found", index)
    index += 1






