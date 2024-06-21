from typing import List


def majorityElement(nums: List[int]) -> int:
    cur_streak = 0
    cur_num = nums[0]
    for num in nums:

        if cur_streak == 0:
            cur_num = num
            
        if cur_num != num:
            cur_streak -=1
        else:
            cur_streak +=1

    return cur_num


if __name__ == '__main__':
    print(majorityElement([8,8,7,7,7]))
    print(majorityElement([2,2,1,1,1,2,2]))
    print(majorityElement([3,2,3]))