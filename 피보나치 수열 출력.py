nums = [1, 1, 2]

for i in range(47):
    nums.append(nums[-1]+nums[-2])

for i in nums:
    print(i)