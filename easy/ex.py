from typing import List

def ex(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        print("i:", i, " nums[i]:", nums[i])

    for i, val in enumerate(nums):
        print("i:", i, " nums[i]:", nums[i])


if __name__ == '__main__':
    ex([3,1,4,1])