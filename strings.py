import string

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

	
# Designer Door Mat
def door_mat():
	n, m = map(int, int().split())
	for i in range(1, n, 2):
		print((".|." * i).center(m, "-"))
	print("WELCOME".center(m, "-"))
	for i in range(n-2, 0, -2):
		print((".|." * i).center(m, "-"))
		j += 3


# Text Alignment
def hacker_rank_logo():
	thickness = int(input())
	c = 'H'
	
	# Top Cone
	for i in range(thickness):
		print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
	
	# Top Pillars
	for i in range(thickness+1):
		print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))	
	
	#Middle Belt
	for i in range((thickness+1)//2):
	    print((c*thickness*5).center(thickness*6))
   	
   	#Bottom Pillars
	for i in range(thickness+1):
		print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

	#Bottom Cone
	for i in range(thickness):
		print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# Capitalize
def capital_letter():
	s = list(input())
	for i in range(len(s)):
		if s[i] == ' ':
			if s[i+1] != ' ':
				s[i+1] = s[i+1].capitalize()
		elif i == 0:
			s[i] = s[i].capitalize()
	print(s)


# String Formatting
def numbers_convention_formatting():
	number = 17
	largura = len("{0:b}".format(number))
	for i in range(1, number+1):
		print("{0:{largura}d} {0:{largura}o} {0:{largura}X} {0:{largura}b}".format(i, largura=largura))


# Alphabet Rangoli
def alphabet_rangoli():
	size = int(input())
	largura = ((size * 2) - 1) + ((size * 2) -2)
	list_alphabet = list(string.ascii_lowercase)

	for i in range(size):
		output_list = ""

		for u in range(i+1):
			output_list += list_alphabet[size-(u+1)]
		size_list = len(output_list)

		if size_list > 1:
			output_string = output_list[:size_list-1] + output_list[size_list-1] + output_list[-2::-1]
		else:
			output_string = output_list[0]
		print('-'.join(output_string).center(largura, "-"))

	for i in range(size - 2, -1, -1):
		output_list = ""

		for u in range(i + 1):
			output_list += list_alphabet[size-(u+1)]

		size_list = len(output_list)
		if size_list > 1:
			output_string = output_list[:size_list-1] + output_list[-1::-1]
		else:
			output_string = output_list[0]
		print('-'.join(output_string).center(largura, "-"))


# The Minion Game
def minion_game():
	string = "BANANA"
	stuartPoint, kevinPoint = 0, 0
	vowel = "AEIOU"

	for i in range(len(string)):
		if string[i] in vowel:
			kevinPoint += len(string) - i 
		else:
			stuartPoint += len(string) - i
			
	if stuartPoint > kevinPoint:
		print("Stuart", stuartPoint)
	elif stuartPoint < kevinPoint:
		print("Kevin", kevinPoint)
	else:
		print("Draw")







if __name__ == '__main__':
	# swap_case()
	# translate_to_hifen_language()
	# call_me_by_this_name()
	# to_change_a_char()
	# show_me_what_you_have()
	# wrapping()
	# door_mat()
	# capital_letter()
	# string_formatting()
	# formatting_again()
	# alphabet_rangoli()
	minion_game()	

