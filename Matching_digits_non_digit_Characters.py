Regex_Pattern = r"\d{2}\D\d{2}\D\d{4}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

#con esta regex busco un cadena con la siguiente estructura 06-11-2015
# los cual serian dos numeros,not numero, dos numeros, not numero, cuatro numeros