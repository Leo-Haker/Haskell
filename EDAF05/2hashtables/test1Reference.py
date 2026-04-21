import sys
from test1 import SeparateChaining
# read words from input, one word per line
# then use a dictionary to count which word is most frequent
# but sometimes try to remove the word
# and then print the most frequent word and if there are multiple
# most frequent take the first one in alphabetical order



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
