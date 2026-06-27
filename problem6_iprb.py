data = input().split()
k = int(data[0])
m = int(data[1])
n = int(data[2])
total = k + m + n
d = total * (total - 1)
prob = (k*(k-1) + 2*k*m + 2*k*n + 0.75*m*(m-1) + m*n) / d
print(prob)
