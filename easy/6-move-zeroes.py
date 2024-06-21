from typing import List


def move2(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            while j < len(nums) - 1:
                nums[j] = nums[j+1]
                nums[j+1] = 0
                j+=1
    return nums

def moveZeroes(nums: List[int]) -> List[int]:
    left = 0
    right  = 0
    for i in range(len(nums)):
        if nums[right] != 0:
            tmp = nums[right]
            nums[right] = 0
            nums[left] = tmp
            left += 1
        right += 1
    
    return nums
    



if __name__ == '__main__':
    print(moveZeroes([0,10,0,1,1,0,2,3,0]))
    print(moveZeroes([0,1]))
    print(moveZeroes([1]))
    print(moveZeroes([0]))