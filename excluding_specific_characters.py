Regex_Pattern = r'^[^0-9][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'	# Do not delete 'r'.

from importlib.machinery import BYTECODE_SUFFIXES
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

# tarea 
# cadena de 6 digitos
# 1 que no incluya numero 
# 2 que no tenga vocales en minusculas
# 3 que no tenga bcDF
# 4 que no tenga caracter
# 5 que no tenca vocales en mayusculas
# 6 que no tenga . o , 


# 1ab A.