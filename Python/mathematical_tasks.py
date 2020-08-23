import math


# Mod Divmod
def divmoding():
	a, b = int(input()), int(input())
	print(a//b, a%b, divmod(a, b), sep="\n")


# Power - Mod Power
def poweringmod():
	a, b, m = int(input()), int(input()), int(input())
	print(pow(a, b), pow(a, b, m), sep="\n")


# Integers Come In All Sizes
def summing_powered():
	a, b, c, d = [int(input()) for _ in range(4)]
	print((a**b)+(c**d))


if __name__ == '__main__':
	# divmoding()
	# poweringmod()
	summing_powered()
