num=int(input("Enter the number:"))
s=0
test=num
while num>0:
    r=num%10
    s=s+r**3
    num=num//10
if test==s:
    print("Armstong number")
else:
    print("Not an armstrong number")
