import math


# Mod Divmod
def divmoding():
	a, b = int(input()), int(input())
	print(a//b, a%b, divmod(a, b), sep="\n")


# Power - Mod Power
def poweringmod():
	a, b, m = int(input()), int(input()), int(input())
	print(pow(a, b), pow(a, b, m), sep="\n")



if __name__ == '__main__':
	# divmoding()
	poweringmod()
