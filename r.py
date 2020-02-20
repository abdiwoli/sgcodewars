def interleave(*n):
	n = [i for i in n]
	for i in range(len(n)):
		for h in n:
			if len(n[i])<len(h):
				while len(n[i]) < len(h): n[i] += [None]
	x = [h for i in zip(*n) for h in i]
	
	return x
	