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

# Set .union() Operation
def number_of_individuals():
	englishClass, frenchClass = [input().split() for _ in range(4)][1::2]
	print(len(set(englishClass) | set(frenchClass)))


if __name__ == '__main__':
	# taking_avarage()
	# mesuring_happiness()
	# symmetric_difference()
	# counting_unique_stamps()
	#
	number_of_individuals()
