for i in range(1, 1001):
	for j in range(2, 1001):
		if(i%j > 0 and i != j):
			False
		else:
			break			
	print(i)