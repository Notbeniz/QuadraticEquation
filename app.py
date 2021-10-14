import math

x = input()

a,b,c = x.split(' ')

delta = math.sqrt((int(b)**2)-(4*int(a)*int(c)))

r1 = (-int(b)+delta)/(2*int(a))
r2 = (-int(b)-delta)/(2*int(a))

print(f'{r1} {r2}')
