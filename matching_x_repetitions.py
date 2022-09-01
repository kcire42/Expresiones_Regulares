<<<<<<< HEAD
Regex_Pattern = r'__________'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

# You have a test string .
# Your task is to write a regex that will match
# S using the following conditions:

# S must be of length equal to 45.
# The first 40 characters should consist of letters
# (both lowercase and uppercase), or of even digits.
# The last 5 characters should consist of odd digits 
# or whitespace characters

4
d
A
=======
x4202v2A22A9a6aaaaaa2G2222m222qwertyYuIo13957
2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
x4202v2A22A9a6aaaaaa2G2222m222qwertyYuIo13957
x4202v2A22A9a6aaaaaa2G2222m222qwertyYuIo13957
^[a-zA-Z02468]{40}[13579\\s]{5}$

^[02468A-Za-z]{40}[13579\s]{5}$
>>>>>>> fdc81e27658b432d7875549ceb0b4b786eff72ee
