import os
import time

directory = r'C:\Users\Dasha\PycharmProjects\untitled2\venv\module_7'


for root, dirs, files in os.walk(directory):

  for file in files:
    filepath = os.path.join(root, file)
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(root)

    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
          f' Родительская директория: {parent_dir}')