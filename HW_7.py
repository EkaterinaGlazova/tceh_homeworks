#1 Прочитать теорию (ссылки в материалах) о работе с файлами в python. 
# И реализовать две функции: write_to_file(data) и read_file_data(). 
# Которые соотвественно: пишут данные в файл и читают данные из файла.

def write_to_file(text):
	file = open("test_py.txt", "w") # from the folder with file or write the path to this file
	file.write(text)
	file.close()

write_to_file("I'm writing to this file")

def read_file_data():
	file = open("test_py.txt", "r") # from the folder with file or write the path to this file
	print(file.read())
	file.close()

if __name__ == '__main__':
	write_to_file("I'm writing to this file")
	read_file_data()

#2 Прочитать теорию о работе с json. Реализовать следующую логику: 
# получать при помощи requests данные сайта https://jsonplaceholder.typicode.com/, 
# выводить в консоль все пары "ключ-значение", сохранять полученный json в файл.

import json
import requests

def get_json():
	r = requests.get('https://jsonplaceholder.typicode.com/')
	headers = r.headers
	for key, value in headers.items():
		print(key, value)

	file = open("file_1.txt", "w")
	file.write(json.dumps(dict(headers)))
	file.close()

if __name__ == '__main__':
	get_json()

#3 Обратиться с странице https://habrahabr.ru/. Получить текст страницы. 
# При помощи регулярных выражений нужно получить все ссылки со страницы на другие

import requests
import re

r = requests.get('https://habrahabr.ru/')
#print(r.content)
result = re.findall(r'(https:\/\/\S*(?="))', str(r.content))
print(result)
