import sys
import first_lab
import argparse
import doctest

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
x = first_lab.solve_ten(a,b,c,fla)
if (x != None):
    sys.stdout.write(f"x1={x[0]}\nx2={x[1]}")
else: sys.stdout.write(f"complex without -c")
