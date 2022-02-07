import sys

array = [0] * 8001
sorted_list = []
n = int(sys.stdin.readline().strip())
for _ in range(n):
    array[int(sys.stdin.readline().strip()) + 4000] += 1

if array.count(max(array)) > 1:
    mean_3 = array.index(max(array), array.index(max(array)) + 1) - 4000
else:
    mean_3 = array.index(max(array)) - 4000

for i in range(len(array)):
    if not array[i]:
        continue
    for _ in range(array[i]):
        sorted_list.append(i - 4000)

mean_2 = sorted_list[(n - 1) // 2]
mean_1 = sum(sorted_list) / n
mean_4 = sorted_list[-1] - sorted_list[0]
print(round(mean_1))
print(mean_2)
print(mean_3)
print(mean_4)
