nums_file = input('Введите путь к массиву:')
file = open(nums_file, "r")
nums = file.read().split()
for i, item in enumerate(nums):
    nums[i] = int(item)
file.close()

def task4():
    nums.sort()
    print(nums)
    mid = len(nums) // 2
    if len(nums) % 2 == 0:
        res = (nums[mid] + nums[mid-1]) // 2
    else:
        res = nums[mid]

    summ = 0
    for item in nums:
        a = abs(res - item)
        summ += a
    print(summ)

task4()