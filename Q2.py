# Two groups of employees (managers and developers) are considered. Managers supervise the developers.

# Through this code we can display info of developers, apply for promotion, add and remove developers 
# from the managers' lists, and display the list of developers under the supervision of each manager.

# Parent class
class Employee:
	
	num_of_emps = 0
		
	def __init__(self, first, last, title, department, year, pay):
		self.first = first
		self.last = last
		self.email = first.lower() + '.' + last.lower() + '@lucidmotors.com'
		self.title = title
		self.department = department
		self.year = year
		self.pay = pay
		
		Employee.num_of_emps += 1
	
	# Promotion leads to modification of salary and/or title  
	def apply_promotion(self, raise_percentage, new_title):
		self.pay = int(self.pay * (100. + raise_percentage)/100.)
		self.title = new_title

# Managers class is inherited from the Employee class		
class Managers(Employee):
	def __init__(self, first, last, title, department, year, pay, developers=None):
		# These attributes are the same as the parent class
		super().__init__(first, last, title, department, year, pay)
		
		# list of developers of a manager
		if developers == None:
			self.developers = []
		else:
			self.developers = developers
	
	# Add a new developer to the list of a manager	
	def add_dev(self, dev):
		if dev not in self.developers:
			self.developers.append(dev)
	
	# Remove a developer from the list of a manager			
	def remove_dev(self, dev):
		if dev in self.developers:
			self.developers.remove(dev)
	
	# Display the list of developers of a manager		
	def display_developers(self):
		if self.developers == []:
			print('{} {} is not a supervisor of any developer.'.format(self.first, self.last))
		else:
			print('{} {} is the supervisor of the following developers:'.format(self.first, self.last))
			for dev in self.developers:
				print('{} {}'.format(dev.first, dev.last))
		print('\n')

# Developers class is inherited from the Employee class				
class Developers(Employee):
	
	def __init__(self, first, last, title, department, year, pay, top_skill):
		# These attributes are the same as the parent class
		super().__init__(first, last, title, department, year, pay)
		
		# An extra attribute
		self.top_skill = top_skill
	
	# Display information of a developer
	def display_info(self):
		return '{} {}\n{}\n{}\nEmail: {}\nJoined in {}\nCurrent salary: {}$\nTop skill: {}\n'.format(self.first, self.last, self.title, self.department, self.email, self.year, self.pay, self.top_skill)

# Considering two developers
dev_1 = Developers('Hamid', 'Daryan', 'Junior Data Analyst', 'Hardware Engineering Department', 2022, 90000, 'Analysis')
dev_2 = Developers('Sara', 'Lien', 'Junior Software Developer', 'Hardware Engineering Department', 2021, 100000, 'Programming')

# Displaying info of these developers
print(dev_1.display_info())
print(dev_2.display_info())

# dev_1 has a promotion; his salary has been increased by 5% and his new title is 'Senior Data Analyst'
dev_1.apply_promotion(5, 'Senior Data Analyst')

# Displaying info of dev_1 after the promotion
print(dev_1.display_info())

# Considering two managers
mgr_1 = Managers('Yu', 'Lin', 'Senior Data Scientist', 'Hardware Engineering Department', 2019, 150000, [dev_1])
mgr_2 = Managers('Elizabeth', 'Smith', 'Lead Engineer', 'Hardware Engineering Department', 2018, 160000)

# Add dev_2 to the list of mgr_1
mgr_1.add_dev(dev_2)
# Display the list of developers of mgr_1		
mgr_1.display_developers()

# Remove dev_2 from the list of mgr_1
mgr_1.remove_dev(dev_2)
# Display the list of developers of mgr_1		
mgr_1.display_developers()

# Display the list of developers of mgr_2	
mgr_2.display_developers()

# Print the number of the total employees
print('Number of employees: {}\n'.format(Employee.num_of_emps))