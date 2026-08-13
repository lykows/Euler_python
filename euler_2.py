fib = [0, 1]
sum = 0
i = 0
while fib[i] < 4000000:
	fib.append(fib[i] + fib[i+1])
	if(fib[i] % 2 == 0):
		sum += fib[i]
	i+=1
print(fib)
print(f"Total: {sum}")