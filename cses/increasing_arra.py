n=int(input())
x=[int(i) for i in input().split()]
c=0
for i in range(1,n):
    if x[i-1]>=x[i]:
        d=x[i-1]-x[i]
        x[i]+=d
        c+=d
print(c)
