sent= input()

no_of_words= len(sent.split())
no_of_char = len(sent)
vowels="aeiouAEIOU"
num_vowels=0
for char in sent:
    if char in vowels:
        num_vowels+= 1

print(no_of_char)
print(no_of_words)
print (num_vowels)
