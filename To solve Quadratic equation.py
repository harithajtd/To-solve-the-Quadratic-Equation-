# PYTHON PROGRAM TO SOLVE QUADRATIC EQUATION

#The standard form of quadratic equation is:
#ax**2+bx+c=0, where
#a,b,c are real numbers and
#a!=0

''' The solution of this quadratic equation is given by:'''
#(-b+-(b**2-4*a*c)**0.5)/(2*a)

#CODE

print('To solve the quadrartic equation,')

#Solve the quadratic equation ax**@+bx+c=0
#import complex math module

import cmath

a=int(input('Enter "a" value:'))
b=int(input('Enter "b" value:'))
c=int(input('Enter "c" value:'))

#calculate the discriminant
d=(b**2)-(4*a*c)

#find two solutions
solution1=(-b-cmath.sqrt(d))/(2*a)
solution2=(-b+cmath.sqrt(d))/(2*a)

print('The solutions are {0} and {1}'.format(solution1,solution2))

print(solution1)
