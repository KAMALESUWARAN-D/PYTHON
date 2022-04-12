l=list(map(int,input("Enter the list:").split()))
s=0
for i in range(0,len(l)-1):
    if l[i]>s:
        s+=l[i]
    else:
        print("The list of elements are not super incresing")
        break
else:
    print("The list of elements are super incresing")

