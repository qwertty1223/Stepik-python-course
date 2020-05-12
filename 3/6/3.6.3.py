import requests, sys

start = open(sys.argv[1], "r")
end = open(sys.argv[2], "w")
link, filename = start.read().rsplit('/', maxsplit=1)
start.close()
link += '/'
filename = filename.strip('\n')

while filename:
	response = requests.get(link+filename)
	filename = None if response.text.startswith("We") else response.text

end.write(response.text)
end.close()