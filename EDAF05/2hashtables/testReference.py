import sys
from test import SeparateChaining
# read words from input, one word per line
# then use a dictionary to count which word is most frequent
# but sometimes try to remove the word
# and then print the most frequent word and if there are multiple
# most frequent take the first one in alphabetical order

"""
data/sample/1.in
Correct!
data/sample/2.in
Correct!
data/secret/1musl.in
Correct!
data/secret/2pg.in
Correct!
data/secret/3glibc.in
Correct!
data/secret/4linux.in
Correct!
data/secret/5ppc.in
Correct!
data/secret/6big.in
Correct!
data/secret/7huge.in
Correct!

real    0m17.767s
user    0m15.210s
sys     0m0.352s
"""

d = SeparateChaining()

i = 0

for line in sys.stdin:
	word = line.strip()
	is_present = d.exists(word)
	remove_it = i % 16 == 0

	if is_present:
		if remove_it:
			d.remove(word)
		else:
			count = d.get(word)
			d.insert(word, count + 1)
	elif not remove_it:
		d.insert(word, 1)
	i += 1

(count, word) = (0, "")

for w, c in d.items():
	if c > count:
		count = c
		word = w
	elif c == count and w < word:
		word = w

print(word, count)
