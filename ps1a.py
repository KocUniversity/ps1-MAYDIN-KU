n, B = list(map(int, input().strip().split())) # UNCOMMENT THIS
#n, B = 5, 11223344
T = 0


sum = 0
tries = 0

for i in (range(0, n)):
	i += 1
	if i%2 == 1:
		sum += ((3 ** i) + 1) ** (n - i)
		# print(sum)
	else:
		sum += ((2 ** i) + 1) ** (n - i)
		# print(sum)


while tries <= 10000:
	T += 1
	tries += 1
	if (sum * T) > B:
		break

if tries > 10000:
   T = -1

print(T)