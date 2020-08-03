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
	
	occurances = [i for i in itertools.combinations(letters, together)]

	print(round(sum(1 for i in occurances if 'a' in i)/len(occurances), 3))


# Maximize It
def maximizing_it():

numberOfTimes, M = map(int, input().split())

soManyLists = [list(map(lambda x: int(x) ** 2, input().split()[1:])) for _ in range(numberOfTimes)]
soManyLists = list(map(lambda x: sum(x)%M, list(itertools.product(*soManyLists))))

print(max(soManyLists))



'''
7 867
7 6429964 4173738 9941618 2744666 5392018 5813128 9452095
7 6517823 4135421 6418713 9924958 9370532 7940650 2027017
7 1506500 3460933 1550284 3679489 4538773 5216621 5645660
7 7443563 5181142 8804416 8726696 5358847 7155276 4433125
7 2230555 3920370 7851992 1176871 610460 309961 3921536
7 8518829 8639441 3373630 5036651 5291213 2308694 7477960
7 7178097 249343 9504976 8684596 6226627 1055259 4880436

866
'''


if __name__ == '__main__':
	# cartesian_product()
	# permutating_characters()
	# char_combinations()
	# char_combinations_with_replacmente()
	# compressing_string()
	# probability_of_a_letter()
	maximizing_it()
