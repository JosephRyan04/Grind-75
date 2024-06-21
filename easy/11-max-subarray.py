from typing import List
'''
Given an integer array nums, find the
subarray
with the largest sum, and return its sum. 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

def maxSubArray(nums: List[int]) -> int:
    cur_max = 0
    ult_max = -10001
    for i in range(len(nums)):
        cur_max = max(nums[i], cur_max + nums[i])
        ult_max = max(ult_max, cur_max)

    return ult_max



if __name__ == '__main__':
    maxSubArray([3,1,4,1])
    maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    maxSubArray([5,4,-1,7,8])