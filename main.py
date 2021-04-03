
n, B = list(map(int, input().strip().split())) # UNCOMMENT THIS
#n, B = 5, 11223344
T = 0

# your code here

######################################################## CORE

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


######################################################## END OF CORE


######################################################## PART A 


while tries <= 10000:
	T += 1
	tries += 1
	if (sum * T) > B:
		break

######################################################## END OF PART A


######################################################## PART B


# minVal = 0
# maxVal = 10000
# preVal = 0
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
# #print(preVal)
# #print(tries)
# T += 1


######################################################## END OF PART B

######################################################## T = -1

if tries > 10000:
   T = -1


# please do not modify the input and print statements
# and make sure that your code does not have any other print statements

print(T) #UNCOMMENT
