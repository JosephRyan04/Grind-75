from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    prefix = 1
    postfix = 1
    result = [1] * len(nums)
    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]
    
    for i in range(len(nums) - 1, -1,-1):
        result[i]*= postfix
        postfix *= nums[i]

    print(result)
    return result


if __name__ == '__main__':
    productExceptSelf([3,1,4,1])
    productExceptSelf([1,2,3,4])
    productExceptSelf([-1,1,0,-3,3])