# Introduction to Sets
def taking_avarage():
	numberPlats, heightPlants = int(input()), set(map(int, input().split()))
	print(sum(heightPlants)/len(heightPlants))


if __name__ == '__main__':
	taking_avarage()
