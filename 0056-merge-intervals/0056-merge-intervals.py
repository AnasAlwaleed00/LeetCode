class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        res = [intervals[0]]
        if len(intervals) == 1: return intervals

        
        for i in range(1, len(intervals)):
            if (res[-1][1] >= intervals[i][0]):
                res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])]
            else: res.append(intervals[i])
        return res