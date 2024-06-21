from typing import List

'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order. 
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''

def sortedSquares(nums: List[int]) -> List[int]:
    result = [0] * len(nums)
    length = len(nums) - 1
    left = 0
    right = length
    for i, val in enumerate(nums):
        if abs(nums[left]) > abs(nums[right]):
            result[length - i] = nums[left]**2
            left += 1
        else:
            result[length - i] = nums[right]**2
            right -= 1

    return result

if __name__ == '__main__':
    print(sortedSquares([-4,-1,0,3,10]))
    print(sortedSquares([-7,-3,2,3,11]))
    print(sortedSquares([-7,-3,2,3,11,12]))
    print(sortedSquares([-7]))
    print(sortedSquares([-7,2]))