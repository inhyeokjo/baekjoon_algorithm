a = input().split('-')
for i, sum_list in enumerate(a):
    a[i] = sum(map(int, sum_list.split('+')))
result = 0
for i, element, in enumerate(a):
    if i == 0:
        result += element
    else:
            result -= element

print(result)
