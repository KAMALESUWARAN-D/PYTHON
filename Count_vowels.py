word=input("Enter the word:")
vowel='aeiouAEIOU'
c=0
for i in range(len(word)):
    if word[i] in vowel:
         c+=1
print("No.of vowels:",c) 
