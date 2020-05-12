import re, sys

s = open(sys.argv[1], "r").read().strip('\n')
out = open(sys.argv[2], "w")

w = re.findall(r"[\D]+", s)
d = re.findall(r"[\d]+", s)

for i in range(len(w)):
	print(w[i]*int(d[i]), end='', file=out)

out.close()
out = open(sys.argv[2], "r")
text = out.read()
out.close()
out = open(sys.argv[2], "w")
print(text, end='', file=out)
out.close()