import itertools 


# itertools.product()
def cartesian_product():
	listA, listB = [tuple(map(int, input().split())) for _ in range(2)]
	print(*itertools.product(listA, listB))


# itertools.permutations()
def permutating_characters():
	string, value = input().split()
	[print("".join(i)) for i in sorted(itertools.permutations(string, int(value)))]
	#print(sorted(tuples))

if __name__ == '__main__':
	# cartesian_product()
	permutating_characters()
