class stack():
	def __init__(self):
		self.s=[]
	def top(self):
		if self.s:return self.s[-1]
		else:return -1
	def push(self,x):
		self.s.append(x)
	def pop(self):
		if self.s:return self.s.pop()
		else:return -1
def next_largest(x):
	l=[]
	a=stack()
	for i in x:
		if a.top()==-1:
			l.append(-1)
		else:
			if a.top()>i:
				l.append(a.top())
			else:
				while a.top()!=-1 and a.top()<=i:
					a.pop()
				if a.top()==-1:
					l.append(-1)
				else:
					l.append(a.top())
		a.push(i)
	return l
arr=[int(i) for i in input().split()]
res=next_largest(arr)
print(res)
