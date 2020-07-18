import numpy

# Arrays
def reverse_array():
	l = input().split()
	print(numpy.array(l[::-1], float))


# Shape and Reshape
def cube_shape():
	l = "1 2 3 4 5 6 7 8 9".split()
	print(numpy.reshape(numpy.array(l, int), (3, 3)))


# Transpose and Flatten
def smithing_the_array():
	column, line = map(int, input().split())
	l = [i for i in range(1, (column * line) + 1)]
	np = numpy.array(l)
	np.shape = (column, line)
	print(np.T)
	print(np.flatten())


# Concatenate
def come_together_array():
	line1, line2, column = map(int, input().split())
	l1, l2 = [], []
	for i in range(line1):
		l1.append(input().split())
	for i in range(line2):
		l2.append(input().split())
	np, np2 = numpy.array(l1, int), numpy.array(l2, int)
	np = numpy.concatenate((np, np2))
	np.shape = (line1 + line2, column)
	print(np)


# Zeros and Ones
def zeros_and_ones():
	values = tuple(map(int, input().split()))
	print(numpy.zeros(values, dtype=numpy.int))
	print(numpy.ones(values, dtype=numpy.int))


# Eye and Identity
def identity():
	n, m = map(int, input().split())
	print(numpy.eye(n, m))


# Array Mathematics
def mathrray():
	x, y = map(int, input().split())
	l1, l2 = [], []
	for i in range(x):
		l1.append(list(map(int, input().split())))
	for i in range(x):
		l2.append(list(map(int, input().split())))
	l1 = numpy.array(l1, int)
	l2 = numpy.array(l2, int)
	print(l1 + l2, l1 - l2, l1 * l2, l1 // l2, l1 % l2, l1 ** l2, sep="\n")


# Floor, Ceil and Rint
def floor_rint_ceil():
	np = numpy.array(list(input().split()), float)
	print(numpy.floor(np), numpy.ceil(np), numpy.rint(np), sep="\n")


# Sum and Prod
def sum_prod_array():
	n, m = map(int, input().split())
	np = numpy.array([input().split() for _ in range(n)], int)
	np = numpy.prod(numpy.sum(np, axis=0))
	print(np)


# Min and Max
def max_of_min():
	n, m = map(int, input().split())
	np = numpy.array([input().split() for _ in range(n)], int)
	np = numpy.max(numpy.min(np, axis=1))
	print(np)


if __name__ == '__main__':
	# reverse_array()
	# cube_shape()
	# smithing_the_array()
	# come_together_array()
	# zeros_and_ones()
	# identity()
	# mathrray()
	# floor_rint_ceil()
	# sum_prod_array()
	max_of_min()
