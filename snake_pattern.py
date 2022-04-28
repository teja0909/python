'''
snake pattern 
for n=4
1 2 3 4
8 7 6 5 
9 10 11 12
16 15 14 13

for n=7
1 2 3 4 5 6 7
14 13 12 11 10 9 8 
15 16 17 18 19 20 21
28 27 26 25 24 23 22 
29 30 31 32 33 34 35
42 41 40 39 38 37 36 
43 44 45 46 47 48 49

for n=3
1 2 3
6 5 4 
7 8 9
'''
n=int(input())
for i in range(1,(n*n)+1,n):
    if ((i+n-1)//n)&1:
        j=i
        while(j%n!=0):
            print(j,end=' ')
            j+=1
        print(j)
    else:
        j=i+n-1
        print(j,end=' ')
        j-=1
        while(j%n!=0):
            print(j,end=' ')
            j-=1
        print()
