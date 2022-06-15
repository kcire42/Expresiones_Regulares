Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

#tenemos una regex que busca el patron 3 word, 1 non-word, 10 word, 1 non-word, 3 word