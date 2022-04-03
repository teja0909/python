n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if x>y:
        if x&1:
            n=(x-1)**2+1
            print(n+y-1)
        else:
            n=x**2
            print(n-y+1)
    else:
        if y&1:
            n=y**2
            print(n-x+1)
        else:
            n=(y-1)**2+1
            print(n+x-1)
        
