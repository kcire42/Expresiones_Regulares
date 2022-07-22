

import re
Regex_Pattern = r"^[A-Z]{5}\d{4}\w$"	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, input()))).lower())
ABCDS1234Y
ABAB12345Y
avCDS1234Y