n=int(input())

l=map(int,input().split())
s=int((n*(n+1))/2)
print(s-sum(l))
