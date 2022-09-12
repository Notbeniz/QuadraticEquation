import math

x = input()

a,b,c = x.split(' ')

delta = ((int(b)**2)-(4*int(a)*int(c)))
if delta >0:
  r1 = (-int(b)+math.sqrt(delta))/(2*int(a))
  r2 = (-int(b)-math.sqrt(delta))/(2*int(a))
  print(f'{r1} {r2}')
if delta==0:
  r = (-int(b))/(2*int(a))
  print(f'{r}')
if delta<0:
   print("Equation Answers is NaN, Because delta is Negative")
