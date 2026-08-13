sum1 = 0
sum2 = 0
n = int(input("Enter number: "))
for i in range(1, n+1):
	sum1 += i ** 2
	sum2 += i

sum2 = sum2 ** 2
dif = sum2 - sum1
print(f"Sum squares: {sum1}")
print(f"Square sum: {sum2}")
print(f"Difference: {dif}")

