import re

string = 'Construct a 2 storey detached dwelling'.lower()


expression = r'construct a [\d+] storey'
pattern = re.compile(expression)
match = pattern.match(string)
if match:
    print match.group(0)