import os


PATH = os.getcwd() + '/static/images/'

file_name = PATH + '1.jpg'

data_file = open(file_name, 'rb').read()

print(data_file)