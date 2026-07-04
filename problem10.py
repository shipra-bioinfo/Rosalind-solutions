n , m = map(int,input().split())
ages = [1] + [0] * (m-1)
for month in range(2, n + 1):
    newborns = sum(ages[1:])
    ages = [newborns] + ages[:-1]
print(sum(ages))    
