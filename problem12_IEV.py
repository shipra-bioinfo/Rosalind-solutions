counts = list(map(int, input().split()))
probabilitites = [1, 1, 1, 0.75, 0.5, 0]
total = 0

for count , prob in zip(counts, probabilitites):
    total += count * 2 * prob
print(total)    