# "Say "Hello, World!" With Python
def print_string(string='Hello, World!'):
	print(string)


# Python If-Else
def weird_number():
	n = int(input())
	if (n % 2 == 0) and (n < 5 or n > 20):
		print("Not Weird")
	else:
		print("Weird")


# Arithmetic Operators
def simple_arithmetic():
	a = int(input())
	b = int(input())
	print('{0}\n{1}\n{2}'.format((a + b), (a - b), (a * b)))


# Python: Division
def simple_division():
	a = int(input())
	b = int(input())
	print(a//b, a/b, sep='\n')


# Loops
def simple_loop():
	n = int(input())
	for i in range(n):
		print(i ** 2)


# Write a function
def leap_year():
	year = int(input())
	print((year % 4 == 0) and (not(year % 100 == 0) or (year % 400 == 0)))


# Print Function
def simple_string():
	n = int(input())
	print(*[str(i) for i in range(1, n+1)], sep='')


if __name__ == '__main__':
	# print_string()
	# weird_number()
	# simple_arithmetic()
	# simple_division()
	# simple_loop()
	# leap_year()
	simple_string()
