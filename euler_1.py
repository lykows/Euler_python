multiples = []
sum = 0
for i in range(1, 1000):
	#print(i)
	if (i % 3 == 0 or i % 5 ==0 ):
		print(i)
		sum += i

print(f"Total: {sum}")
	
