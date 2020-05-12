import sys
with open(sys.argv[1], "r") as file:
	table = [{'class':int(line.split("\t")[0]), "height":int(line.split("\t")[-1])} for line in file.read().strip('\n').split('\n')]
classes = dict.fromkeys([i for i in range(1, 12)])
for entry in table:
	if not classes[entry['class']]:
		classes[entry['class']] = [0, 0]
	classes[entry['class']][0] += entry['height']
	classes[entry['class']][1] += 1
with open(sys.argv[2], "w") as out:
	for c in classes:
		if not classes[c]:
			out.write(str(c)+' -\n')
		else:
			classes[c] = classes[c][0] / classes[c][1]
			out.write(str(c)+" "+str(classes[c])+'\n')
