import json
from pprint import pprint

with open('train.json') as data_file:    
    data = json.load(data_file)

for x in data:
	y = x[0].split('(') 
	y[1] = y[1].strip(')')
	#y[1] = dict(item.split("=") for item in y[1].split(";"))
	y[1] = y[1].split(';')
	y[1] = list(z.split('=') for z in y[1])
	print(y[1])
