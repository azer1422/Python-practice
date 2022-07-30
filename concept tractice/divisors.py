num= int(input("Enter a number:"))

div= range(1,12)
for d in div:
    if(num%d ==0):
        print("numbers that are divisible are: "+ str(d))