'''
from www.practicepython.org
completed on 30.10.2020

Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''
__author__ = 'maxisui'
num = int(input("Please chose a number: "))
div = list(range(1, num + 1))
a = []
for elements in div:
    if num % elements == 0:
        a.append(elements)
print(a)