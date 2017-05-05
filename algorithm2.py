fib_list = [1, 1]

def sumfinder4mil(f):
	even_list = []
	while f < 4000000:
		f = fib_list[-1] + fib_list[-2]
		fib_list.append(f)
	fib_list.pop()
	print sum(fib_list)






sumfinder4mil(1)