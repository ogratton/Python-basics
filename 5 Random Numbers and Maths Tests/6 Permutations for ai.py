def perm(lst):
	if len(lst) == 0:
		return []
	elif len(lst) == 1:
		return [lst]
	else:
		perms = []
		for i in range(len(lst)):
			x = lst[i]
			xs = lst[:i] + lst[i+1:]
			for p in perm(xs):
				perms.append([x]+p)
		return perms

TOP = []

data = [1,2,3,4,5,6] # see green circles in part c
for p in perm(data):
	if (p.index(1) < p.index(3)): # checks preconditions are met
		if (p.index(3) < p.index(5)):
			if (p.index(2) < p.index(4)):
				if (p.index(4) < p.index(6)):
					TOP.append(p)
					print(p)

print(len(TOP)+2) 
