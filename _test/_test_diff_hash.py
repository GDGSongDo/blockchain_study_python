"""
# comparison of y = hash(diff.X)
# check how would those were changed
"""
print(__doc__)

import hashlib

with open( '__script.txt', 'r', encoding='utf-8') as f:
    x1 = f.read()
    x2 = f.read() + '.'

y1 = hashlib.sha256(x1.encode()).hexdigest()
y2 = hashlib.sha256(x2.encode()).hexdigest()

# print("{:} ({:})\n\n".format(y1 == y2, len(y1)))
print("{:}\n{:}\n".format(y1, y2))
print("{:}\n{:}".format(y1[:4], y2[:4]))
