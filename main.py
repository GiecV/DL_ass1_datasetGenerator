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
        n = str(random.randint(1, 999999))
        while(len(n) < 6):
            n = '0' + n
        numbers.append(n)
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

def binaryRange(numberOfBits):
    numbers=[]
    for number in range(2**numberOfBits):
        numbers.append('{0:06b}'.format(number))
    return numbers

if __name__ == '__main__':
    numbers = binaryRange(6)
    for n in numbers:
        print(n + ";" + isPalyndrome(n))