class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print(f'Name: {self.lastName}, {self.firstName}')
        print(f'ID: {self.idNumber}')


class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        score = sum(self.scores)/len(self.scores)
        if score < 40:
            return 'T'
        elif score < 55:
            return 'D'
        elif score < 70:
            return 'P'
        elif score < 80:
            return 'A'
        elif score < 90:
            return 'E'
        else:
            return 'O'


if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    scores = list(map(int, input().split()))
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
