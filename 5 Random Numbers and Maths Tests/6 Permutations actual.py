def perm(lst):
	if len(lst) == 0:
		return []
	elif len(lst) == 1:
		return [lst]
	else:
		perms = []
		for i in range(len(lst)):
			x = lst[i] #head
			xs = lst[:i] + lst[i+1:] #tail
			for p in perm(xs):
				perms.append([x]+p)
		return perms


data = [1,2,3,4]
for p in perm(data):
        print(p)

