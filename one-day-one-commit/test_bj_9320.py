py = []
ja = []
for i in range(int(input())):
    py.append(input())

for j in range(int(input())):
    ja.append(input())

print("-----------------------------")

for i in range(6561):
    if not py[i] == ja[i]:
        print(i)
        
