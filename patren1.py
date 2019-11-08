n=int(input("enter no of rows you want:"))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(end=" ")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
for k in range(1,n):
    for l in range(1,k+1):
        print(end=" ")
    for l in range(1,n+1-k):
        print(l,end="")
    for l in range(n-1-k,0,-1):
        print(l,end="")
    print()