import urllib2, json, time

def main():
	#response = urllib2.urlopen('http://www.reddit.com/r/Club_Nintendo/comments/2zbh79/looks_like_canadian_accounts_are_now_getting/.json')
	#json_data = response.read()
	json_data = open('data')
	json_tree = json.load(json_data)

	parsed_data = []

	for i, root in enumerate(json_tree[1]['data']['children']):
		#print '%s\n\n' % str(i)
		if root['kind'] == 't3':
			body = 'selftext'
		elif root['kind'] == 't1':
			body = 'body'

		temp = []
		temp.append(root['data']['author'])
		temp.append(root['data'][body])
		temp.append(int(root['data']['created_utc']))

		parsed_data.append(temp)
		#print "%s\t%s\t%s\n" % (root['data']['author'],
		#					  root['data'][body],
		#					  time.strftime('%Y%m%d %H:%M:%S', time.localtime(int(root['data']['created_utc'])))
		#					  )

	parsed_data.sort(key=lambda x: x[2])

	for entry in parsed_data:
		print '%s\t%s\t%s\n' % (time.strftime('%Y%m%d %H:%M:%S', time.localtime(entry[2])), entry[1], entry[0])

if __name__ == '__main__':
	main()