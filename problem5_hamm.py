S1 = input()
S2 = input()
count = 0
for i in range(len(S1)):
    if S1[i] != S2[i]:
        count = count + 1
print(count)        


