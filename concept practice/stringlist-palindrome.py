wrd = str(input("Please enter a word: "))
rvs=wrd[::-1]
print(rvs)

if(wrd==rvs):
    print("This word is a palindrome")

else:
    print("This word is not a palindrome")