import itertools 


# itertools.product()
def cartesian_product():

	listA, listB = [tuple(map(int, input().split())) for _ in range(2)]
	print(*itertools.product(listA, listB))


# itertools.permutations()
def permutating_characters():

	string, value = input().split()
	[print("".join(i)) for i in sorted(itertools.permutations(string, int(value)))]


# itertools.combinations()
def char_combinations():
	string, value = input().split()
	string = sorted(list(string))
	for i in range(1, int(value) + 1):
		for u in itertools.combinations(string, i):
			print("".join(u))


# itertools.combinations_with_replacement()
def char_combinations_with_replacmente():

	string, value = input().split()
	string, value = sorted(list(string)), int(value)
	[print("".join(i)) for i in itertools.combinations_with_replacement(string, value)]


# Compress the String!
def compressing_string():

	string = input()
	sliced_string = []

	for content, length in itertools.groupby(string):
		sliced_string.append((sum(1 for _ in length), int(content)))

	[print(i, end=" ") for i in sliced_string]


# Iterables and Iterators
def probability_of_a_letter():

	_ = int(input())
	letters = input().split()
	together = int(input())
	#letters = [(quantity[i], letters[i]) for i in range(len(quantity))]
	occurances = [i for i in itertools.combinations(letters, together)]

	print(round(sum(1 for i in occurances if 'a' in i)/len(occurances), 3))


if __name__ == '__main__':
	# cartesian_product()
	# permutating_characters()
	# char_combinations()
	# char_combinations_with_replacmente()
	# compressing_string()
	probability_of_a_letter()
