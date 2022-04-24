'''arr=[1,3,2,4]
output=[3,4,4,-1]
for 1 next largest value is 3
for 3 next largest value is 4 
for 2 next largest value is 4
for 4 it was last value so -1
'''
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
	for i in x[::-1]:
		if a.top()==-1:
			l.append(-1)
			a.push(i)
		else:
			if a.top()>i:
				l.append(a.top())
				a.push(i)
			else:
				while a.top()<=i:
					a.pop()
				if a.top()==-1:
					l.append(-1)
				else:
					l.append(a.top())
					a.push(i)
	return l[::-1]
arr=[int(i) for i in input().split()]
res=next_largest(arr)
print(res)
