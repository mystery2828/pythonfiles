import time

start = time.time()


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    h = {}
    lis = []
    for i, num in enumerate(nums):

        if num not in h:
            h[num] = 1
        else:
            h[num] += 1

    if 0 in h:
        for i, num in enumerate(nums):

            if num < 0 and abs(num) in nums and [num, 0, abs(num)] not in lis:
                lis.append([num, 0, abs(num)])

    for i, num in enumerate(nums):
        for j in range(len(nums) - 1, -1, -1):
            target = num - i
            if abs(target) in h and 0 in h and [target, 0, abs(target)] not in lis:
                lis.append([target, 0, abs(target)])
            if num + i + nums[j] == 0 and [num, i, nums[j]] not in lis:
                lis.append([num, i, nums[j]])

    return lis


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
print(time.time() - start)
