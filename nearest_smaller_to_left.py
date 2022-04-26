stack=[]
op=[]
a=[int(i) for i in input().split()]
for i in a:
    if len(stack)==0:op.append(-1)
    else:
        if i>stack[-1]:op.append(stack[-1])
        else:
            while len(stack)>0 and stack[-1]>i:
                stack.pop()
            if len(stack)==0:op.append(-1)
            else:op.append(stack[-1])
    stack.append(i)
print(*op)
