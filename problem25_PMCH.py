import sys
import math

lines = sys.stdin.read().split('\n')
sequence = ''
for line in lines:
    if not line.startswith('>'):
        sequence += line

a_count = sequence.count('A')
u_count = sequence.count('U')
g_count = sequence.count('G')
c_count = sequence.count('C')

au_ways = math.factorial(a_count)
cg_ways = math.factorial(c_count)

result = au_ways * cg_ways
print(result)
