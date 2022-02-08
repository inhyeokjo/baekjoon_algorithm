import sys
input = sys.stdin.readline

max = int(input())
monetary_units = list(map(int, input().strip().split()))
no = False

for i in range(len(monetary_units)-1):
    if monetary_units[i+1]%monetary_units[i] != 0:
        print('No')
        no=True
        break
if not no:
    print('Yes')
