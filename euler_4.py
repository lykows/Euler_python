y = 1

def palindrome(x):
	if x == (x[::-1]):
		return int(x)
	else:
		return 1	

for a in range(999, 100, -1):
	for b in range (999, 100, -1):
		c = str(a * b)
		if int(y) <= palindrome(c):
			y = palindrome(c)	

print(f"Largest Palindrome: {y}")


