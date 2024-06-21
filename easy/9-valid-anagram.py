from typing import List

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    hashmap = [0] * 26
    for i in range(len(s)):
        hashmap[ord(s[i]) - ord('a')] += 1
        hashmap[ord(t[i]) - ord('a')] -= 1
    
    return hashmap == [0] * 26


if __name__ == '__main__':
    print(isAnagram(s = "anagram", t = "nagaram"))
    print(isAnagram(s = "rat", t = "car"))
    print(isAnagram(s = "a", t = "ab"))