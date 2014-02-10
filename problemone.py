# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

multiples = [3, 5]
min = 1
max = 1000

multiplesInRange = []

for i in range(min, max):
	for x in multiples:
		if i % x == 0:
			multiplesInRange.append(i)

print sum(multiplesInRange)
