#without argument,without no retrun
def name():
	print("name")
name()

#without argument,with return
def name1():
	print("me")
	return "name1"
name1()

#with argument,without return
def name2(kannur):
	print(kannur+" is my place")
name2('kerala')

#with argument,with return
def name3(keys):
	print(keys+"key")
	return"name3"
name3('enter')


    # 4 types of function in python
# 1.No argument, No return value
def sample():
    print("hello")  
    sample()
# 2.No argument, with return value
def sample1():
    a=10
    b=20
    sum = a + b
    return sum
result = sample1()
print(result)
# 3.with argument, no return value
def sample2(value):
    print("value is: " +str(value))
sample2(123)
# 4.with argument, with return value
def sample3(num1,num2):
    sum = num1 + num2
    return sum
result1 = sample3(12,24)
print(result1)
