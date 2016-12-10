import sys
inFile = open('test.tmp','w')
dataFile = open(sys.argv[1],'r')

for x in dataFile:
	y = x.split('(') 
	y[1] = y[1].strip(")\n")
	#y[1] = dict(item.split("=") for item in y[1].split(";"))
	y[1] = y[1].split(';')
	y[1] = list(z.split('=') for z in y[1])
#	print(y)
	if y[1][0][0] != '':
		inFile.write(y[0]+' ')
		for z in y[1]:
			inFile.write(z[0]+' ')
		inFile.write('\n')
	else:
		inFile.write(y[0]+'\n')
