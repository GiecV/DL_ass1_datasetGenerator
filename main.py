# This is a sample Python script.
import random


# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def addPalyndromes(amount):

    palyndromes = []

    for i in range(amount):
        d1,d2,d3 = random.sample(range(1,9),3)
        number = str(d1) + str(d2) + str(d3) + str(d3) + str(d2) + str(d1)
        palyndromes.append(number)

    return palyndromes


def addRandomNumbers(amount):
    numbers = []

    for i in range(amount):
        d1, d2, d3, d4, d5, d6 = random.sample(range(1, 9), 6)
        number = str(d1) + str(d2) + str(d3) + str(d4) + str(d5) + str(d6)
        numbers.append(number)

    return numbers

def isPalyndrome(a):

    while(len(a) < 6):
        return "-1"

    first = 0
    middle = (len(a) - 1) / 2
    last = len(a) - 1

    while(first <= middle):
        if(a[first] == a[last]):
            first+=1
            last-=1
        else:
            return "0"

    return "1"



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    numbers = []
    numbers += addPalyndromes(32)
    numbers += addRandomNumbers(32)
    for n in numbers:
        print(n + ";" + isPalyndrome(n))
