s=0
n=int(input("Enter the number:"))
while n!=0:
    s=s+(n%10)
    n=n//10
print("Sum of digits:",s)
