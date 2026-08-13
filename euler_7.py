primes = [0, 2]
ind = 10001
i = 1
num = 3
while (len(primes) <= ind) :	
	if (num % primes[i] != 0):
		i += 1		
		if (i >= (len(primes))):
			primes.append(num)
			print(f"I: {i}, Prime: {num}")
			i = 1
	
	else: 
		num += 1
		i = 1
print("10001th prime: ", primes[10001])
