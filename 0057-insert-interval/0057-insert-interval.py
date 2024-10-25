class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        #intervals = [[1,3],[6,9]] newInterval = [2,5]
        #[...] [.......] [.....] [...]
                #[s....e]
            
        res =[]
        ind = 0
        len_intervals= len(intervals)
        start, end = newInterval[0], newInterval[1]
        
        while ind < len(intervals) and start > intervals[ind][1]:
            res.append(intervals[ind])
            ind +=1
        while ind < len(intervals) and end >= intervals[ind][0]:
            start = min(start, intervals[ind][0])
            end = max(end, intervals[ind][1])
            ind +=1
        res.append([start, end])
        
        while ind < len(intervals):
            res.append(intervals[ind])
            ind +=1
            
        return res