import sys

file = open(sys.argv[1], "r")
text = file.read().lower().split()

words = {}
for word in text:
	if word not in words:
		words.update({word:1})
	else:
		words[word] += 1

maxword = ["", 0]
for word, count in words.items():
	if maxword[1] < count:
		maxword = [word, count]


out = open(sys.argv[2], "w")
out.write(f"{maxword[0]} {maxword[1]}")
out.close()