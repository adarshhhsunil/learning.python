class office_details:
	year=2020

	def __init__(self,name,salary,location,experince):
		self.name=name
		self.salary=salary
		self.location=location
		self.experince=experince

	def increment_salary(self):
		self.salary=self.salary+self.salary*(15/100)

	def increment_experince(self):
		self.experince=self.experince+1

	def display(self):
	    print("name :"+self.name)
	    print("salary :"+str(self.salary))
	    print("location :"+self.location)
	    print("experince :"+str(self.experince))


x=office_details('adi',10000,'knr',1)
x.display()

print('\nsalary after one year\n')

x.increment_salary()
x.increment_experince()
office_details.year=office_details.year+1

x.display()




