from typing import List

'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping. */

Start date: 1/11 2021
end date: 5/17/2021

Start date: 5/17/2021 
End date: 8/6/2021.

Start date: 8/22/2022
End date: 12/16/2022
'''

def meeting_rooms(intervals: List[List[int]]):
    start = 0
    end = 1
    prev = intervals[0]
    result = []
    intervals.sort(key = lambda x: x[start])

    for i, val in enumerate(intervals):
        if prev[end] >= val[start]:
            prev[end] = max(prev[end],val[end])
        else:
            result.append(prev)
            prev = val
            
        

    result.append(prev)
    return result



if __name__ == '__main__':
    print(meeting_rooms([[1,3],[2,6],[8,10],[15,18]]))
    print(meeting_rooms([[1,3],[2,8],[8,10],[15,18]]))
    print(meeting_rooms([[1,4],[4,5]]))
    print(meeting_rooms([[1,3],[2,6],[8,10],[15,18],[18,19]]))
    print(meeting_rooms([[1,3],[8,10],[15,18],[2,6],[18,19]]))
    print(meeting_rooms([[4,5]]))