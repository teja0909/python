a=input()
best=0
c=0
for i in range(1,len(a)):
    if a[i-1]==a[i]:
        c+=1
    else:
        c=0
    if c>best:
        best=c
print(best+1)
