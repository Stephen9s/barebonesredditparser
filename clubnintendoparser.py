import urllib2, json, time

# Simple and single use code
# No error checking at this time since it was thrown together quickly for a contest!

def main():
	#response = urllib2.urlopen('http://www.reddit.com/r/subreddit/comments/id0000/thread_name/.json')
	#json_data = response.read()
	json_data = open('data')
	json_tree = json.load(json_data)

	parsed_data = [] # Eventually will hold [[author, body, epochtime]]

	for i, root in enumerate(json_tree[1]['data']['children']):
		
		# Below not necessarily needed since json_tree[0] should contain
		#     the only post that has the key 'selftext'.
		#     json_tree[1:] should have the key 'kind' as 't1' and a key 'body' instead of 'selftext'
		if root['kind'] == 't3':
			body = 'selftext'
		elif root['kind'] == 't1':
			body = 'body'

		temp = []
		temp.append(root['data']['author'])
		temp.append(root['data'][body])
		temp.append(int(root['data']['created_utc']))

		# [author, body, epochtime] added to parsed_data list
		parsed_data.append(temp)

		#print "%s\t%s\t%s\n" % (root['data']['author'],
		#					  root['data'][body],
		#					  time.strftime('%Y%m%d %H:%M:%S', time.localtime(int(root['data']['created_utc'])))
		#					  )

	# Sort by epoch time
	parsed_data.sort(key=lambda x: x[2])

	# Print converted epoch time, body, author
	for entry in parsed_data:
		print '%s\t%s\t%s\n' % (time.strftime('%Y%m%d %H:%M:%S', time.localtime(entry[2])), entry[1], entry[0])

if __name__ == '__main__':
	main()