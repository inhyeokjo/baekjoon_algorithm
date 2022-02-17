import operator
import sys
from collections import defaultdict

input = sys.stdin.readline

n, c = map(int, input().split())
message = list(map(int, input().split()))
frequency_dict = defaultdict(int)

for i in message:
    frequency_dict[i] += 1
sorted_message_dict = sorted(frequency_dict.items(), reverse=True, key=operator.itemgetter(1))
result = []
for item, frequency in sorted_message_dict:
    for i in range(frequency):
        result.append(item)
print(' '.join(result))
