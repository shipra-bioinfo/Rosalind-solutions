from itertools import permutations
result = list(permutations([1,2,3,4,5,6]))
print(len(result))
for perm in result:
    print(" ".join(str(num) for num in perm))
