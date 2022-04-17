"""INPUT X='double nine two triple six five four'
Expected outpput-99222654
"""
def getPhonenumber(s):
	inp=s.split()
	con={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
	mult={'double':2,'triple':3}
	fin=''
	j=1
	for i in inp:
		if i in mult:
			j=mult[i]
			continue
		fin+=con[i]*j
		j=1
	return fin
