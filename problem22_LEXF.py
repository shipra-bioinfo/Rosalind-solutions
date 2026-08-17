from itertools import product
result = list(product(['A', 'B', 'C', 'D', 'E', 'F'], repeat = 3))
#print(result)
for comb in result:
    print("".join(str(base) for base in comb))

