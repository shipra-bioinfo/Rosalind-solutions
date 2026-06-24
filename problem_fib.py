data = input('Enter n and k: ')
parts = data.split()
n = int(parts[0])
k = int(parts[1])

a = 1
b = 1

for i in range(n-2):
    new_b = k* a + b
    a = b
    b = new_b
    

print('Answer:', b)    
