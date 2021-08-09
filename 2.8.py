n, k = int(input()), int(input())
lst = []
for i in range(1, n+1): lst.append(i)

def josephus(ls, skip):
	skip -= 1 # pop automatically skips the dead guy
	idx = skip
	while len(ls) > 1:
		ls.pop(idx)
		#print(ls.pop(idx)) # kill prisoner at idx
		#print(ls)
		idx = (idx + skip) % len(ls)
	return(ls[0])

print(josephus(lst, k))
