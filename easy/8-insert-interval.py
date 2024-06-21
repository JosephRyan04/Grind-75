from typing import List

'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it. 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    start_time = 0
    end_time = 1
    result = []
    for i, val in enumerate(intervals):
        if newInterval[end_time] < val[start_time]:
            result.append(newInterval)
            return result + intervals[i:]
        elif val[end_time] < newInterval[start_time]:
            result.append(val)
        else:
            newInterval[start_time] = min(newInterval[start_time],val[start_time])
            newInterval[end_time] = max(newInterval[end_time], val[end_time])

    result.append(newInterval)
    return result



if __name__ == '__main__':
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[18,19]))
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[0,1]))
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[11,11]))