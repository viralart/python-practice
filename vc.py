str = input("Enter a string: ")
vowel = 0
consonent = 0
vowel_list = "aeiouAEIOU"
for ch in str :
    if ch.isalpha():
        if ch in vowel_list:
            vowel += 1
        else :
            consonent += 1

print(vowel)
print(consonent)



