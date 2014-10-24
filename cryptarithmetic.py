__author__ = 'jasonjkeller'

"""
CIS 471 Artificial Intelligence - Fall 14

cryptarithmetic.py is a Python 2.7 program which
can solve crypt-arithmetic problems of the form:

FOUR (minuend)
-TWO (subtrahend)
----
TWO (difference)
"""

import time
minuend = raw_input('Enter the minuend: ')
subtrahend = raw_input('Enter the subtrahend: ')
difference = raw_input('Enter the difference: ')

# pretty print problem
print "\n", minuend
print "-" + subtrahend
print "------"
print " " + difference + "\n"

num_solutions = 0
# list of characters used in problem
unique_letters = []

# populate list of characters used in problem
for let in minuend:
    if let not in unique_letters:
        unique_letters.append(let)

for let in subtrahend:
    if let not in unique_letters:
        unique_letters.append(let)

for let in difference:
    if let not in unique_letters:
        unique_letters.append(let)

unique_letters.sort()
list_size = len(unique_letters)
start = time.time()

# DEBUG
# print unique_letters
# print "size: " + str(list_size) + "\n"


def get_subt(n):
    """ Method which takes an integer representing a character index in the subtrahend string
        Returns the index location of the retrieved character in the list unique_letters """
    if unique_letters.index(subtrahend[n]) == 0:
        return a
    elif unique_letters.index(subtrahend[n]) == 1:
        return b
    elif unique_letters.index(subtrahend[n]) == 2:
        return c
    elif unique_letters.index(subtrahend[n]) == 3:
        return d
    elif unique_letters.index(subtrahend[n]) == 4:
        return e
    elif unique_letters.index(subtrahend[n]) == 5:
        return f
    elif unique_letters.index(subtrahend[n]) == 6:
        return g
    elif unique_letters.index(subtrahend[n]) == 7:
        return h
    elif unique_letters.index(subtrahend[n]) == 8:
        return i
    elif unique_letters.index(subtrahend[n]) == 9:
        return j


def get_diff(n):
    """ Method which takes an integer representing a character index in the difference string
        Returns the index location of the retrieved character in the list unique_letters """
    if unique_letters.index(difference[n]) == 0:
        return a
    elif unique_letters.index(difference[n]) == 1:
        return b
    elif unique_letters.index(difference[n]) == 2:
        return c
    elif unique_letters.index(difference[n]) == 3:
        return d
    elif unique_letters.index(difference[n]) == 4:
        return e
    elif unique_letters.index(difference[n]) == 5:
        return f
    elif unique_letters.index(difference[n]) == 6:
        return g
    elif unique_letters.index(difference[n]) == 7:
        return h
    elif unique_letters.index(difference[n]) == 8:
        return i
    elif unique_letters.index(difference[n]) == 9:
        return j


def get_minu(n):
    """ Method which takes an integer representing a character index in the minuend string
        Returns the index location of the retrieved character in the list unique_letters """
    if unique_letters.index(minuend[n]) == 0:
        return a
    elif unique_letters.index(minuend[n]) == 1:
        return b
    elif unique_letters.index(minuend[n]) == 2:
        return c
    elif unique_letters.index(minuend[n]) == 3:
        return d
    elif unique_letters.index(minuend[n]) == 4:
        return e
    elif unique_letters.index(minuend[n]) == 5:
        return f
    elif unique_letters.index(minuend[n]) == 6:
        return g
    elif unique_letters.index(minuend[n]) == 7:
        return h
    elif unique_letters.index(minuend[n]) == 8:
        return i
    elif unique_letters.index(minuend[n]) == 9:
        return j


def calc_results():
    """ Method which calculates the number of correct solutions and prints them """
    global num_solutions
    subt = 100*get_subt(0) + 10*get_subt(1) + get_subt(2)
    diff = 100*get_diff(0) + 10*get_diff(1) + get_diff(2)
    minu = 1000*get_minu(0) + 100*get_minu(1) + 10*get_minu(2) + get_minu(3)
    if (subt + diff == minu) and (minu >= 1000):
        print minu, "-", subt, "==", diff
        num_solutions += 1

print "Solutions:"
print "================="

# calculate solutions based on number of unique characters
if list_size == 1:
    for a in range(10):
        calc_results()
elif list_size == 2:
    for a in range(10):
        for b in range(10):
            if len({a, b}) == list_size:
                calc_results()
elif list_size == 3:
    for a in range(10):
        for b in range(10):
            for c in range(10):
                if len({a, b, c}) == list_size:
                    calc_results()
elif list_size == 4:
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if len({a, b, c, d}) == list_size:
                        calc_results()
elif list_size == 5:
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        if len({a, b, c, d, e}) == list_size:
                            calc_results()
elif list_size == 6:
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            if len({a, b, c, d, e, f}) == list_size:
                                calc_results()
elif list_size == 7:
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            for g in range(10):
                                if len({a, b, c, d, e, f, g}) == list_size:
                                    calc_results()
elif list_size == 8:
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            for g in range(10):
                                for h in range(10):
                                    if len({a, b, c, d, e, f, g, h}) == list_size:
                                        calc_results()
elif list_size == 9:
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            for g in range(10):
                                for h in range(10):
                                    for i in range(10):
                                        if len({a, b, c, d, e, f, g, h, i}) == list_size:
                                            calc_results()
elif list_size == 10:
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            for g in range(10):
                                for h in range(10):
                                    for i in range(10):
                                        for j in range(10):
                                            if len({a, b, c, d, e, f, g, h, i, j}) == list_size:
                                                calc_results()

print "================="
end = time.time()
print str(num_solutions) + " solutions found in " + str(end - start) + " seconds."