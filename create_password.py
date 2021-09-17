from string import ascii_lowercase, ascii_uppercase, digits
from random import shuffle

LETTER = {'EN': set([x for x in ascii_uppercase if x not in 'OI']),
          'en': set([x for x in ascii_lowercase if x not in 'ol']),
          'dig': set([x for x in digits if x not in '01'])}

def generate_password(length):
	s = ''.join(LETTER['EN'] | LETTER['en'] | LETTER['dig'])
	s = set(s)
	s = list(s)
	check=False
	while check==False:
		shuffle(s)
		t = set(s[:length])
		if len(t & LETTER['EN'])>0 and len(t & LETTER['en'])>0 and len(t & LETTER['dig'])>0:
			s=list(t)
			check=True
	return s

def generate_passwords(count, length):
	return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())

for lst in generate_passwords(n, m):
	print(*lst, sep='')
