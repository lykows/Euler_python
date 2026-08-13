i = 1
n = 1
while i <= 20:
	if n % i == 0:
		i += 1
	else:
		n += 1
		i = 1


print(f"Smallest Multiple: {n}")