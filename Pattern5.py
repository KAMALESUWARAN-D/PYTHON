def pattern(n):
    for i in range(n,0,-1):
        for j in range(1,i):
            print(end=" ")
        for j in range(i,n+1):
            print("*",end="")
        print(" ")
n=5
pattern(n)
