Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())


#la regex busca el patron de la siguiente manera non-espacio en blanco{2},espacio en blanco,non-espacio en blanco{2},espacio en blanco