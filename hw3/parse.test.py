import sys

test_data = sys.argv[1]
test_in = "/data/test/test.seq.in"
df = open(test_in, 'w')

with open(test_data) as f:
	for line in f:
		sentence = [word for word in line.split()]
		df.write(" ".join(sentence[1:len(sentence)-1])+"\n")
