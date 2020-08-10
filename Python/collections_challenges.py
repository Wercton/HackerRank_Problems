import collections


# collections.Counter()
def shoe_store_total_earn():

	_, shoesSize = [collections.Counter(input().split()) for _ in range(2)]
	total_gain = 0

	for _ in range(int(input())):

		size, price = input().split()
		if size in shoesSize:
			if shoesSize[size] > 0:
				total_gain += int(price)
				shoesSize[size] -= 1

	print(total_gain)


# Collections.namedtuple()
def average_students_collections():

	rounds = int(input())
	Student = collections.namedtuple('Student', ' '.join(input().split()))
	students, counter = [], 0

	for i in range(rounds):
		data = input().split()
		students.append(Student(data[0], data[1], data[2], data[3]))
		counter += int(students[i].MARKS)

	print(counter/rounds)


# Collections.OrderedDict()
def ordering_dicts():

	ordinary_dict = collections.OrderedDict()
	
	for _ in range(int(input())):

		products = input().split()
		value = int(products[-1])
		products.pop()
		products = " ".join(products)
		
		if products not in ordinary_dict:
			ordinary_dict[products] = value
		else:
			ordinary_dict[products] += value

	[print(i, ordinary_dict[i]) for i in ordinary_dict]


# Collections.deque()
def your_own_deque():

	deque = collections.deque()

	for _ in range(int(input())):
		command = input().split()
		if len(command) == 2:
			eval("deque.{0}({1})".format(command[0], int(command[1])))
		else:
			eval("deque.{0}()".format(*command))

	print(*deque)



if __name__ == '__main__':
	# shoe_store_total_earn()
	# average_students_collections()
	# ordering_dicts()
	your_own_deque()
