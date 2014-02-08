multiples = [3, 5]
min = 1
max = 1000

multiplesInRange = []

for i in range(min, max):
	for x in multiples:
		if i % x == 0:
			multiplesInRange.append(i)

print sum(multiplesInRange)