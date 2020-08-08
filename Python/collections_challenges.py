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


if __name__ == '__main__':
	# shoe_store_total_earn()
	average_students_collections()
