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
def string_formatting():
	number = 2
	for i in range(1, number+1):
		number8, number16, number2 = str(oct(i)), str(hex(i)), str(bin(i))
		width = (len(str(i)), len(number8), len(number16), len(number2))
		print('{:2d}'.format(i), '{:2s}'.format(number8[2:]), '{:2s}'.format(number16[2:].upper()), '{:2s}'.format(number2[2:]))


def formatting_again():
	number = 17
	largura = len("{0:b}".format(number))
	for i in range(1, number+1):
		print("{0:{largura}d} {0:{largura}o} {0:{largura}X} {0:{largura}b}".format(i, largura=largura))



# Alphabet Rangoli
def alphabet_rangoli():
	pass


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
	formatting_again()