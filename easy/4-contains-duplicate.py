from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    hashmap = {}
    for i in range(len(nums)):
        if nums[i] in hashmap:
            return True
        hashmap[nums[i]] = i

    return False




if __name__ == '__main__':
    print(containsDuplicate([1,2,3,1]))
    print(containsDuplicate([1,2,3,4]))