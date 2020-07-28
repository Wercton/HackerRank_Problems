# Introduction to Sets
def taking_avarage():
	
	numberPlats, heightPlants = int(input()), set(map(int, input().split()))
	print(sum(heightPlants)/len(heightPlants))


# No Idea
def mesuring_happiness():
	
	m, n = map(int, input().split())
	array = list(map(int, input().split()))
	A, B = [set(map(int, input().split())) for i in range(2)]
	happy, sad  = [], []
	[happy.append(i) for i in array if i in A]
	[sad.append(i) for i in array if i in B]
	print(len(happy) - len(sad))


# Symmetric Difference
def symmetric_difference():

	setA = [list(map(int, input().split())) for _ in range(4)]
	setB = set(setA[1]).difference(set(setA[3]))
	setB.update(set(setA[3]).difference(set(setA[1])))
	print(*[i for i in sorted(setA, key=int)], sep="\n")


# Set .add()
def counting_unique_stamps():

	stamps = set()
	[stamps.add(input()) for _ in range(int(input()))]
	print(len(stamps))


# Set .discard(), .remove() & .pop()
def manipulate_your_own_set():

	_, mySet = [set(map(int, input().split())) for _ in range(2)]

	for _ in range(int(input())):
		string = input().split()
		if string[0] != "pop":
			eval("mySet.{0}({1})".format(string[0], string[1]))
		else:
			mySet.pop()

	print(sum(mySet))


# Set .union() Operation
def number_of_individuals():

	englishClass, frenchClass = [input().split() for _ in range(4)][1::2]
	print(len(set(englishClass) | set(frenchClass)))


# Set .intersection() Operation
def intersection_set():

	englishClass, frenchClass = [input().split() for _ in range(4)][1::2]
	print(len(set(englishClass) & set(frenchClass)))


# Set .difference() Operation
def differenciation_set():

	englishClass, frenchClass = [input().split() for _ in range(4)][1::2]
	print(len(set(englishClass) - set(frenchClass)))


# Set .symmetric_difference() Operation
def symmetric_differenciation_set():

	englishClass, frenchClass = [input().split() for _ in range(4)][1::2]
	print(len(set(englishClass) ^ set(frenchClass)))


# Set Mutations
def mutating_your_own_set():

	_, mySet = [set(map(int, input().split())) for _ in range(2)]

	for _ in range(int(input())):
		command = input().split()
		eval("{0}.{1}({2})".format("mySet", command[0], str(set(map(int, input().split())))))

	print(sum(mySet))


# The Captain's Room
def captain_room():

	_ = input()
	all_individuals = input().split()
	setA, setB = set(), set()
	
	for i in all_individuals:
		if i not in setA:
			setA.add(i)
		else:
			setB.add(i)

	print(list(setA ^ setB)[0])


# Check Subset
def is_it_subset():

	for _ in range(int(input())):
		setA, setB = [set(map(int, input().split())) for _ in range(4)][1::2]
		print(len(setA | setB) == len(setB))


def is_it_superset():

	setA = set(map(int, input().split()))
	flag = True
	for _ in range(int(input())):
		if not setA.issuperset(set(map(int, input().split()))):
			flag = False

	print(flag)


if __name__ == '__main__':
	# taking_avarage()
	# mesuring_happiness()
	# symmetric_difference()
	# counting_unique_stamps()
	# manipulate_your_own_set()
	# number_of_individuals()
	# intersection_set()
	# differenciation_set()
	# symmetric_differenciation_set()
	# mutating_your_own_set()
	# captain_room()
	# is_it_subset()
	is_it_superset()

