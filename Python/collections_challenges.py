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






if __name__ == '__main__':
	shoe_store_total_earn()
