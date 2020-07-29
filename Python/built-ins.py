
# Zipped!
def zipping_scores():
	_, subjects = map(int, input().split())
	lists = []

	[lists.append(list(map(float, input().split()))) for _ in range(subjects)]

	zipped = zip(*lists)
	print(*[sum(i)/subjects for i in zipped], sep="\n")


# Input()
def an_user_calculator():

	x, k = map(int, input().split())
	print(eval(input()) == k)


# Python Evaluation
def evaluation():

	eval(input())


# Athlete Sort
def sorting_athlete():

	N, M = map(int, input().split())
	array = [input().split() for _ in range(N)]

	K = int(input())
	array = sorted(array, key = lambda x: x[K])

	[print(*i) for i in array]


# Any of All
def all_palindromic_integers():

	_, values = [input().split() for _ in range(2)]
	print(all([int(i) >= 0 for i in values]) and any([i == i[::-1] for i in values]))


# ginortS
def weird_sort():
	
	this_way_is_better = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
	print(*sorted(input(), key=this_way_is_better.index), sep="")


if __name__ == '__main__':
	# zipping_scores()
	# an_user_calculator()
	# valuation()
	# sorting_athlete()
	# all_palindromic_integers()
	weird_sort()
