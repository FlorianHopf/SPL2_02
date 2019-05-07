prime = False
for i in range(2, 1001):
	for j in range(2, i):
		if((i%j == 0) and (i != j)):
			prime = False
			break
		else:
			prime = True
	if(prime):
		print(i)