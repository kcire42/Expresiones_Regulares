regex_pattern = r"\w{3}[\.]\w{3}[\.]\w{3}[\.]\w{3}"	# Do not delete 'r'.

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())

#lo que hace esta regex es hacer el match de una cadena como la que esta debajo ghc.abc.123.455 si es correcta devuelve un true y un false si no machea
