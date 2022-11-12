import sys
import math
import cmath

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = b*b - 4*a*c
try: d = math.sqrt(d)
except: d = cmath.sqrt(d)
x1 = (0-b+d)/(2*a)
x2 = (0-b-d)/(2*a)

sys.stdout.write(f"x1={x1}\nx2={x2}")