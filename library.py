"""Library Management System"""


class Book():
	def __init__(self, name, publishing_date, author, publisher, category):
		self.name = name
		self.publishing_date = publishing_date
		self.author = author
		self.publisher = publisher
		self.category = category
		pass


class LendingPeriod():
	def __init__(self, lending_period=14):
		self.lending_period = lending_period
		pass


class HighestDemand():
	def __init__(self, lending_period=7, high_demand=True):
		self.lending_period = lending_period
		self.high_demand = high_demand
		pass



class Category():
	def __init__(self, category_name):
		self.category_name = category_name
		pass


class Publisher():
	def __init__(self, publisher_name, publisher_location):
		self.publisher_name = publisher_name
		self.publisher_location = publisher_location

	@property
	def describe_publisher(self):
		print(f"Publisher's name: {self.publisher_name}\nLocation: {self.publisher_location}")


class Author():
	def __init__(self, author_name, years_of_life):
		self.author_name = author_name
		self.years_of_life = years_of_life

	@property
	def describe_author(self):
		print(f"{self.author_name} / {self.years_of_life}")

#=====================================================================================

class Student():
	def __init__(self, student_name, student_surname, student_id):
		self.student_name = student_name
		self.student_surname = student_surname
		self.student_id = student_id
		
	@property
	def describe_student(self):
		student_full_name = f"{self.student_name} {self.student_surname}"
		print(f"Student: {student_full_name.title()}\nStudent's id: {self.student_id}")

	def is_allowed(self, allowance=True):
		"""
		Проверить, сколько книг взял студент.
		Если кол-во равно 5, то allowance = False
		"""
		pass

	def asking_to_prolong(self):
		"""
		Студент может попростить продлить время на 7 дней, если книга не из HighestDemadn
		"""
		pass



class Librarian():
	def __init__(self):
		pass

	def librarian_allowence(self):
		"""
		Проверить allowance студента.
		Если allowance = False, то отказать
		"""
		pass
		
	def prolong(self):
		"""
		Проверить, и если возможно продлить время.
		"""
		pass









































# my_book = Book('Dark Tower', 2004, 
# 	author=Author(author_name='Stephen King', years_of_life='1947-Present'), 
# 	publisher=Publisher(publisher_name='AST', publisher_location='Moskow'), 
# 	category=Category(category_name='fantasy'),
# 	)

# print(my_book.publisher.publisher_location)
# my_book.author.describe_author
# my_book.publisher.describe_publisher