def fun(n):
	l=[n]
	while(n!=1):
		if n&1==0:
			n=int(n/2)
		else:
			n=n*3+1
		l.append(n)
	print(*l)
n=int(input())
fun(n)
