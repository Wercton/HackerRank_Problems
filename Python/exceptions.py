import re


# Exceptions
def division_error():
	
	for _ in range(int(input())):
		division = input().split()

		try:
			print(int(division[0])//int(division[1]))
		except Exception as e:
			print("Error Code:", e)


# Incorrect Regex
def incorrect_regex():

	for _ in range(int(input())):
		
		try:
			string = input()
			re.compile(string)
			print(True)
		except:
			print(False)


if __name__ == '__main__':
	# division_error()
	incorrect_regex()