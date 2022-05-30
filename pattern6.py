def triangle(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print(end=" ")
        for k in range(i,n+1):
            print("*",end=" ")
        print("")
n=5
triangle(n)
