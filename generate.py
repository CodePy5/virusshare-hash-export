import requests

print('Downloading…')

with open('virushashes.txt', 'w') as virushashes:
	isFirstLine = True

	for id in range(99999):
		url = f'https://virusshare.com/hashfiles/VirusShare_{str(id).zfill(5)}.md5'

		response = requests.get(url, stream=True)
		response.encoding = 'utf-8'
		if response.status_code != 200:
			print("Reached end of files.")
			break
		else:
			for line in response.iter_lines(decode_unicode=True):
				if line.startswith('#'):
					continue
				if isFirstLine:
					isFirstLine = False
				else:
					line = '\n' + line
				virushashes.write(line)
			print(f'Downloaded {url}')

print('Download complete')
