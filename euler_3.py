import math
num = 600851475143
def primes(x):
	i = 2
	while (x % i !=0) and (i <= x):
		i+=1
	print(f"Prime: {i}")
	y = x/i
	return primes(y)
primes(num)

#def palindrome(x):
	#91 * 99 = (90 * 90) + (1 * 90) + (90 * 9) + (1 * 9)
	#		= 	 8100        90          810       9