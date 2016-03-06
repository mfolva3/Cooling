# MCS Project One by <Maria Folvarska>
"""
This program prompts the user for 4 inputs:
 (1)inside temperature,
 (2)outside temperature,
 (3)the cooling rate, a constant that determines the speed at which the inside temperature decreases,
 (4)time, the time you want to predict the temperature at.
Type of (1), (2) is float. (3) is a float which will be printed in scientific format. (4) is an integer.
The output of the program consists of:
 (1) the temperature inside at the time inputted by the user as according to Newton's Law of Cooling.

1. welcome message,read input and convert
2. confirm the user input using string concatenation
3. calculate the temperature at inputted time
4. print the outcome using string concatenation
 
"""
from math import exp
#welcome message,read input and convert
print('Evaluating Newton\'s Law of cooling ...')
DATA = input('What is the inside temperature ? ')
INSIDE = float(DATA)
DATA = input('What is the outside temperature ? ')
OUTSIDE = float(DATA)
DATA = input('Give the cooling rate : ')
COOLING = float(DATA)
DATA = input('What is the time to predict the temperature ? ')
TIME = int(DATA) 
#confirm the user input using string concatenation
TEMPIN = 'At ' + '%.1f' % INSIDE + ' degrees inside and '
TEMPOUT = '%.1f' % OUTSIDE + ' degrees outside,'
print(TEMPIN + TEMPOUT)
RATE = 'at a cooling rate of ' + '%.3e' % COOLING + ','
print(RATE)
#calculate the temperature at inputted time
temp = OUTSIDE + (INSIDE - OUTSIDE)*exp(-COOLING*TIME)
#print the outcome using string concatenation
print('the temperature at time ' + '%d' % TIME + ' is: ' + '%.1f' % temp +'.')
