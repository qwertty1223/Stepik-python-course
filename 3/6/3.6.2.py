import requests
import sys

with open(sys.argv[1], "r", encoding='utf-8') as file, open(sys.argv[2], "w", encoding='utf-8') as out:
	url = file.read().strip()
	response = requests.get(url)
	out.write(str(len(response.text.splitlines())))