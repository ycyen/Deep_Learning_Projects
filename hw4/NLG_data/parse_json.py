import json
from pprint import pprint

with open('valid.json') as data_file:    
    data = json.load(data_file)

inFile = open('valid.en','w')
outFile = open('valid.es','w')

for x in data:
	y = x[0].split('(') 
	y[1] = y[1].strip(')')
	#y[1] = dict(item.split("=") for item in y[1].split(";"))
	y[1] = y[1].split(';')
	y[1] = list(z.split('=') for z in y[1])
	if y[1][0][0] != '':
		inFile.write(y[0]+' ')
		for z in y[1]:
			inFile.write(z[0]+' ')
		inFile.write('\n')
		inFile.write(y[0]+' ')
		for z in y[1]:
			inFile.write(z[0]+' ')
		inFile.write('\n')
	else:
		inFile.write(y[0]+'\n')
		inFile.write(y[0]+'\n')
	for z in y[1]:
		if len(z) >= 2:
			x[1] = x[1].replace(z[1].strip('\''), z[0])
	outFile.write(x[1]+'\n')
	for z in y[1]:
		if len(z) >= 2:
			x[2] = x[2].replace(z[1].strip('\''), z[0])
	outFile.write(x[2]+'\n')
	
