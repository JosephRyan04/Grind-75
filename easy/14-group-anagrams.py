from typing import List

'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = []
    answer = []
    map = {}
    for i in range(len(strs)):
        result.append(''.join(sorted(strs[i])))
        if result[i] in map:
            map[result[i]].append(strs[i])
        else:
            map[result[i]] = [strs[i]]

    print(map.values())
    return map.values()



if __name__ == '__main__':
    groupAnagrams(["eat","tea","tan","ate","nat","bat"])