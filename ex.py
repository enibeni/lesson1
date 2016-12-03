import math

print('enter a')
a = int(input())
print('enter b')
b = int(input())
print('enter c')
c = int(input())


def func(a, b, c):			#ax^2+bx+c = 0
	d = b*b - 4*a*c
	x1 = (-b + math.sqrt(d))/2*a
	x2 = (-b - math.sqrt(d))/2*a
	return x1, x2

print(func(a,b,c))




