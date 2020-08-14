opr = input("enter operation symbol")
num = int(input("enter first number"))
num1 = int(input("enter second number"))

if opr == '+':
	value = num+num1
elif opr == '-':
	value = num-num1
elif opr == '*':
	value = num*num1
elif opr == '/':
	if num1 == 0:
		value =''
		print('not possible with 0')
	else:
		value = num/num1
else:
	print("invalid")
print(value)




