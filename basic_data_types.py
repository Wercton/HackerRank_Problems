# List Comprehensions
def simple_list_maker():
	x, y, z, n = (int(input()) for i in range(4))
	print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])


# Find the Runner-Up Score
def runner_up():
	n = int(input())
	runners = list(map(int, input().split()))
	winner = max(runners)
	while winner == max(runners):
		runners.remove(max(runners))
	print(max(runners))


# Nested Lists
def second_lowest():
	studants, scores, name = [], [], []
	for i in range(int(input())):
		name.append(input())
		scores.append(float(input()))
		studants.append([name[i], scores[i]])
	lowest = min(scores)
	while min(scores) == lowest:
		scores.remove(min(scores))
	lowest = min(scores)
	for i in range(len(studants)):
		if studants[i][1] != lowest:
			name.remove(studants[i][0])
	name.sort()
	print(*[i for i in name], sep="\n")



# Finding the percentage
def percentage_grade():
	students = {}
	for _ in range(int(input())):
		name, *line = input().split()
		scores = list(map(float, line))
		students[name] = scores
	media = students[input()]
	print(("{:.2f}".format(sum(media[0:3])/3)))


# Lists
def create_your_own_list():




if __name__ == '__main__':
	percentage_grade()

