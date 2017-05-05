num_collection = []

def sumfinder1000():
	for x in xrange(1,1000):
		if (x % 5 == 0) or (x % 3 == 0):
			num_collection.append(x)
	print num_collection
	print sum(num_collection)

sumfinder1000()