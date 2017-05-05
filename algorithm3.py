# factor_list = []
# prime_list = []

# def factor_finder():
# 	for i in range(1,13196):
# 		if (13195 % i == 0):
# 			factor_list.append(i)

# 	print factor_list


# factor_finder()


def prime_finder():
	n = 600851475143
	i = 2
	while i * i < n:
		while n % i == 0:
			n = n / i
		i = i + 1

	print (n)

prime_finder()