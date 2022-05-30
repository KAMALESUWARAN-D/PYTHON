num=int(input("Enter a number:"))
def strong(num):
    s,rem=0,0
    while(num>0):
        rem=num%10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
        s=s+fact
        num=num//10
    return s
number=num
if number==strong(num):
    print(f"The number {number} is strong number")
else:
    print(f"The number {number} is not strong number")
    
    
