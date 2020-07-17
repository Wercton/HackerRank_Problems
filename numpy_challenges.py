import numpy


def reverse_array():
	l = input().split()
	print(numpy.array(l[::-1], float))


def cube_shape():
	l = "1 2 3 4 5 6 7 8 9".split()
	print(numpy.reshape(numpy.array(l, int), (3, 3)))


def smithing_the_array():
	column, line = map(int, input().split())
	l = [i for i in range(1, (column * line) + 1)]
	np = numpy.array(l)
	np.shape = (column, line)
	print(np.T)
	print(np.flatten())


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


def zeros_and_ones():
	values = tuple(map(int, input().split()))
	print(numpy.zeros(values, dtype=numpy.int))
	print(numpy.ones(values, dtype=numpy.int))


if __name__ == '__main__':
	# reverse_array()
	# cube_shape()
	# smithing_the_array()
	# come_together_array()
	zeros_and_ones()