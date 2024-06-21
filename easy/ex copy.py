from typing import List

def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    hashmap = {}
    for line in lines:
        pos, word = line.strip().split()
        hashmap[int(pos)] = word
    
    n = 1
    cur_pos = 1
    result = ''

    while n <= len(hashmap):
        cur_pos = (n*(n+1))//2
        if cur_pos in hashmap:
            result += hashmap[cur_pos]
            result += ' '
            n+=1
        else:
            return result
    
    return result
    


if __name__ == '__main__':
    # print(decode("easy/input.txt"))
    print(decode("easy/test.txt"))