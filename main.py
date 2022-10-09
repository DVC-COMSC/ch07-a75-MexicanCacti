
import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if len(num1) > len(num2):
	print ('False')
	sys.exit(0)
# ******************************
# Make your Code
# ******************************

# print ('True') or ('False')
for i in range(len(num2)):
	j = 0
	count = 0
	if num1[j] is num2[i]:
		while j < len(num1) and num1[j] == num2[i] and count < len(num1):
			i += 1
			j += 1
			count += 1
	if count == len(num1):
		break
if count == len(num1):
	print('True')
else:
	print('False')