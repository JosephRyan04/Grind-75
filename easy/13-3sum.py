from typing import List

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets. 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

'''

def threeSum(nums: List[int]) -> List[int]:
    map = {}
    result = []
    for i, val in enumerate(nums):
        map[val] = i

    for key in map:
        target = -key
        for j in range(len(nums)):
            if j == map[key]:
                break
            complement = target - nums[j]
            if complement in map and (j != map[complement]) and (map[key] != map[complement]):
                print(key,nums[j],complement)
                result.append([key,nums[j],complement])
        # map[nums[i]] = i
    print(result)
    return result



if __name__ == '__main__':
    threeSum([-1,0,1,2,-1,-4])