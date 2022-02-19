x = int(input())
line = 0 # diagonal
max_n = 0
while x > max_n:
	line += 1
	max_n += line
gap = max_n - x
if line % 2 == 0:
	numer = line - gap
	denom = gap + 1
else:
	numer = gap + 1
	denom = line - gap
print(f'{numer}/{denom}')