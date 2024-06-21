from typing import List

'''
Given an integer array nums, find a
subarray
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer. 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

def maxProduct(nums: List[int]) -> int:
    cur_max = 1
    result = -11
    arr_cur = []
    arr_res = []
    start = 0
    end = 0
    for i in range(len(nums)):
        cur_max = max(nums[i], cur_max*nums[i])
        result = max(result, cur_max)
    print(result)


if __name__ == '__main__':
    maxProduct([3,1,4,1])
    maxProduct([2,3,-2,4])
    maxProduct([-2,3,-2,4])