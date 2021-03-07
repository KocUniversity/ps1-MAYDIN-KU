
n, B = list(map(int, input().strip().split())) # UNCOMMENT THIS
# n, B = 8, 99887766
T = 0

# your code here

######################################################## CORE

sum = 0

for i in (range(0, n)):
	i += 1
	if i%2 == 1:
		sum += ((3 ** i) + 1) ** (n - i)
		# print(sum)
	else:
		sum += ((2 ** i) + 1) ** (n - i)
		# print(sum)


######################################################## END OF CORE


######################################################## PART A 


while T != 10000:
	T += 1
	if (sum * T) > B:
		# print("found the answer")
		break

if T == 10000:
	# print("couldn't find the answer")


######################################################## END OF PART A


######################################################## PART B


# minVal = 0
# maxVal = 10000
# preVal = 0
# tries = 0
# solution = 0
# while tries < 10000 :
# 	preVal = T
# 	T = (minVal + maxVal) // 2
# 	if (sum * T) > B:
# 		solution = preVal
# 		maxVal = T
# 	else:
# 		minVal = T
# 	tries += 1
# # print(f"The result in {tries} tries is")
# T += 1


######################################################## END OF PART B


# please do not modify the input and print statements
# and make sure that your code does not have any other print statements

print(T) #UNCOMMENT
