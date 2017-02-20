#1 Написать декоратор, который отменяет выполнение функции и пишет: ИМЯ_ФУНКЦИИ не будет вызвана

def decorator_no_func(function):
	def inner(*args):
		print(function.__name__, 'will not be called')
	return inner

@decorator_no_func
def f_1(x, y):
	return x + y

f_1(3, 5)


#2 Реализовать декоратор, который измеряет скорость выполнения функций. 
#  Написать три разные функции, задекорировать их и проверить

import time

def decorator_2(func):
	def inner(x, y):
		t = time.clock()
		result = func(x, y)
		print(func.__name__, 'time', time.clock() - t)
		return result
	return inner

@decorator_2
def func_1(x, y):
	return x*y + y*y + x*x

@decorator_2
def func_2(x, y):
    return x + y

@decorator_2
def func_3(x, y):
	return x/y

f1 = func_1(3, 10)

f2 = func_2(3, 10)

f3 = func_3(3, 10)


#3 Написать генероторное выражение, которое включает в себя все четные числа от 0 до 100

list3 = [l for l in range(0, 100) if l % 2 ==0]
print(list3) 

#4 Написать генератор, который возвращает бесконечную последовательность случайных чисел, таких что следующее не меньше прошлого

import random
import sys


def rand_inf():
	a = 0
	while True:
		yield a
		a += random.randint(0, sys.maxsize)
		
task4 = rand_inf()
for index, _ in enumerate(range(15)):
	print(next(task4))


#5 Написать генератор, который принимает на вход дату и на каждый вызов выдает следующий день

import dateitem

def next_day(year, month, day):
	day1 = datetime.date(year, month, day)
	return day1 + datetime.timetable(days = 1)

today = next_day(2017, 2, 10)
print(next(today))
