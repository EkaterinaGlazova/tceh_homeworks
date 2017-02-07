#1 Реализовать класс Person, у которого должно быть два публичных поля: age и name. 
#Также у него должен быть следующий набор методов: know(person), который позволяет добавить другого человека в список знакомых. 
#И метод is_known(person), который возвращает знает ли знакомы ли два человека

class Person(object):
	my_list = []
	
	def __init__(self, age, name):
		self.age = age
		self.name = name

	def know(self, person):
		my_list.append(person)
		print(my_list)
	
	def is_known(self, person):
		if person in my_list:
			print(person, 'is in list')
		else:
			print('you do not know this person')
		

p = Person(15, 'Sasha')
p1 = Person(20, 'Ivan')
my_list = ['Ivan', 'Fedor']

p.know('Sasha')
p1.is_known('Ivan')


#2 Есть класс, который выводит информацию в консоль: `Printer`, у него есть метод: log(*values). 
#Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

class Task2(object):

	def __init__(self):
		print('Printer')

	def log(self, *value):
		return value

class FormattedPrinter(object):

	def __init__(self):
		print('*'*10, '\n', t2.log(3), '\n', '*'*10)

t2 = Task2()
t2.log(3)

f = FormattedPrinter()

#3 Написать класс Animal и Human, сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые). 
#Другие - нет. За что будет отвечать метод is_dangerous(animal)


class Human(object):
	def __init__(self):
		print('This is a human')


class Animal(object):
	def __init__(self, species, danger):
		self.species = species
		self.danger = danger
		print(species, 'is an animal')

	def is_dangerous(self):
		if self.danger == True:
			print(self.species, 'is dangerous animal')
		else:
			print(self.species, 'is not dangerous')

h1 = Human()
a1 = Animal('tiger', True)
a2 = Animal('mouse', False)

a1.is_dangerous()
a2.is_dangerous()
