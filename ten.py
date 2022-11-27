import sys
import math
import cmath
import argparse

def solve_ten(a:int,b:int,c:int,flag:bool) -> tuple:
    d = b*b - 4*a*c
    if not flag:
        try: d = math.sqrt(d)
        except: return None
    else: 
        d = cmath.sqrt(d)
    x1 = (0-b+d)/(2*a)
    x2 = (0-b-d)/(2*a)
    return (x1,x2)

parser = argparse.ArgumentParser(description='eleven')
parser.add_argument('a',type=int,help='Ax*x + b*x + c = y')
parser.add_argument('b',type=int,help='ax*x + B*x + c = y')
parser.add_argument('c',type=int,help='ax*x + b*x + C = y')
parser.add_argument('-c','--complex',action='store_true')
parse_n = parser.parse_args()
a = parse_n.a
b = parse_n.b
c = parse_n.c
fla = parse_n.complex
x = solve_ten(a,b,c,fla)
if (x != None):
    sys.stdout.write(f"x1={x[0]}\nx2={x[1]}")
else: sys.stdout.write(f"complex without -c")
