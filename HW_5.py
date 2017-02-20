#1 Написать списковые выражения, которые:
  #a создают список из строк всех нечетных чисел от 1 до 100
  #b создают список из объектов другого списка, кроме итерируемых
  #c создают список из фразы 'The quick brown fox jumps over the lazy dog', 
     #где каждый объект списка - кортеж из: слова в верхнем регистре, слова в случанйном регистре (qUIcK) и длины слова

#a
a1 = [a for a in range(1, 100) if a % 2 ==0]
print(a1)

#b


#c



#2 Написать класс IntToStr, у которого есть одно поле: value. А тип поля - число. Его задачей должно быть реализация возможности сложения чисел и строк. 
#Примеры:
#obj = IntToStr(9.2)
#print(obj + 3)  # 12.2
#print('a' + obj)  # a9.2
#print(obj + 'z')  # 9.2z

class IntToStr(object):
	def __init__(self, value):
		self.value = value

	def __add__(self, other):
		if isinstance(other.value, str):
			print(str(self.value) + other.value)
		elif isinstance(self.value, str):
			print(self.value + str(other.value))
		else:
			print(self.value + other.value)

i = IntToStr(9.2)
a = IntToStr('abc')
n = IntToStr(3)
i.__add__(a)
a.__add__(i)
i.__add__(n)

#3 Написать класс Stack, у которого есть два метода push(value) и pop(). 
#Если мы пытаемся сделать pop из пустого стека, нужно выбрасывать исключение IndexError.

class Stack(object):
	def __init__(self):
		self.value = None
		self.stack = []

	def push(self, value):
		self.stack.append(value)
		print('Stack is', s.stack) 

	def pop(self):
		try:
			print('Pop is', self.stack.pop())
		except IndexError as e:
			print('IndexError', e)
			

s = Stack()

s.push(1)
s.pop()
s.pop()
