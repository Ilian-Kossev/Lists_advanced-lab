nums = input().split(', ')
result = []
for index in range(len(nums)):
    if nums[index] % 2 == 0:
        result.append(index)
print(result)
#print([index for index in range(len(nums)) if nums[index] % 2 == 0])

