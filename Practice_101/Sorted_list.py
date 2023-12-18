"""
Given an array of integer that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2)
are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

"""
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            print(nums[l], nums[r])
            return [l, r]
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1

if __name__ == '__main__':
    nums = [2, 7, 11, 15, 16, 17, 18, 19, 20]
    target = 34
    print(twoSum(nums, target))
