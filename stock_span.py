values=[int(i) for i in input().split()]
def greater_right(l):
	stack=[]
	op=[]
	for i  in range(0,len(l)):
		if len(stack)==0:
			op.append([-1]*2)
		else:
			if stack[-1][0]>l[i]:
				op.append(stack[-1])
			else:
				while stack and stack[-1][0]<=l[i]:
					stack.pop()
				if len(stack):
					op.append(stack[-1])
				else:
					op.append([-1,i])
		stack.append([l[i],i])
	return op
indexs=greater_right(values)
final=[]
for i in range(len(indexs)):
    final.append(abs(i-indexs[i][1]))
print(final)
