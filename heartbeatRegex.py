import re
with open("LogsForRegex.log") as openfileobject:
	for line in openfileobject:
		pattern = '^((?!] heartbeat).)*$'
		result = re.match(pattern, line)
		if result:
			print(line)