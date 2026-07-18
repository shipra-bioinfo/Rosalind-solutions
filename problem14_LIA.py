import math
k, N = map(int, input().split())
n = 2 ** k
p = 1/4
total_probability = 0
for i in range(N, n+1):
    prob_i = math.comb(n, i) * (p ** i) * ((1-p )** (n - i))
    total_probability += prob_i
print(round(total_probability, 3))
