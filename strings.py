# Swap case
def swap_case():
	print (''.join([i.lower() if i.isupper() else i.upper() for i in input()]))


# String Split and Join
def translate_to_hifen_language():
	print('-'.join(input().split()))


# What's Your Name?
def call_me_by_this_name():
	print(f"Hello {input()} {input()}! You just delved into python.")


# Mutations
def to_change_a_char():
	word = input()
	place, letter = input().split()
	print(word[:int(place)] + letter + word[int(place)+1:])


# String Validators
def show_me_what_you_have():
	string = input()
	print(any(i.isalnum() for i in string))
	print(any(i.isalpha() for i in string))
	print(any(i.isdigit() for i in string))
	print(any(i.islower() for i in string))
	print(any(i.isupper() for i in string))


# Text Wrap
def wrapping():
	string, width = input(), int(input())
	print(*[_ for _ in textwrap.wrap(string, 10)], sep="\n")


if __name__ == '__main__':
	# swap_case()
	# translate_to_hifen_language()
	# call_me_by_this_name()
	# to_change_a_char()
	# show_me_what_you_have()
	wrapping()
	
