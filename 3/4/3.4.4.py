import sys

def avg(array):
	return sum(array) / len(array)

file = open(sys.argv[1], "r", encoding='utf-8')
text = file.read()
file.close()

marks = [[int(i) for i in line.split(';')[1:]] for line in text.split()]
vermarks = []
for i in tuple(zip(*marks[::-1])):
	vermarks.append(i)

marks = [[str(avg(line)) for line in marks]]
marks.append([str(avg(line)) for line in vermarks])

out = open(sys.argv[2], "w")

out.write("\n".join(marks[0]))
out.write("\n")
out.write(" ".join(marks[1]))

out.close()