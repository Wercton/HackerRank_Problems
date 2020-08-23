import calendar
from datetime import datetime

# Calendar Module
def what_day_of_the_week_is():
	dia = datetime.strptime(input(), '%m %d %Y')
	print(calendar.day_name[dia.weekday()].upper())  # weekday devolve um valor de 0-6, day_name dá nome a esse valor


# Time Delta
def absolute_difference_time():
	
	pass


if __name__ == '__main__':
	what_day_of_the_week_is()
