#1
#Написать функцию, которая выбрасывает одно из трех исключений: ValueError, TypeError или RuntimeError случайным образом. 
#В месте вызова функции обрабатывать все три исключения

import random

def f_error():
    try:
        raise random.choice([ValueError, TypeError, RuntimeError])
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')
    except RuntimeError:
        print('RuntimeError')

#2
#Написать функцию, которая принимает на вход список, если в списке все объекты - int, сортирует его. Иначе выбрасывает ValueError

l0 = [1, 3, 5, 'a', 7]
def f_list_sort(l1):
    list_sort = []
    try:
        for i in l1:
            i = int(i)
            list_sort.append(i)
            list_sort.sort()
        return list.sort
    except ValueError as e:
        print(e)
print(f_list_sort(l0))
    
#3
#Написать функцию, которая принимает словарь, преобразует все ключи словаря к строкам и возвращает новый словарь

dict_0 = {1:2, 'a':3, 'b':'c'}

def f_dict(dict1):
    dict_keys = {}
    for i in dict1.keys():
        value = dict1.get(i)
        i = str(i)
        dict_keys[i] = value
    return dict_keys
print(f_dict(dict_0))

#4
#Написать функцию, которая принимает список чисел и возвращает их произведение

from functools import reduce
f_mult = reduce(lambda x, y: x * y, [1, 3, 5, 7])    
print(f_mult)

#5
#Написать три функции: do_work, handle_success, handle_error. 
#do_work(my_list, success_callback, error_callback) принимает на вход три аргумента: 
#список, функцию для обработки успеха и функцию для обработки ошибки. 
#Ее задача проверить, что все значения в списке идут по-возрастанию. 
#Если все верно: вызываем success_callback, иначе: error_callback. 
#Функция handle_success пишет в консоль информацию об успешном выполнении. Функция handle_error выбрасывает ValueError

def success_callback():
    print('Success')
def error_callback():
    print('Error')
def do_work(my_list, success_callback, error_callback):
    if my_list == sorted(my_list):
        success_callback()
    else:
        error_callback()
print(do_work([1, 3, 5], success_callback, error_callback))


def handle_success():
    print('Выполнено успешно!')
    
def handle_error():
    try:
        raise ValueError
    except ValueError:
        print('ValueError')

