class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start = 0
        middle = 0
        end = len(nums) -1
        while middle <= end:
            if nums[middle] == 0:
                nums[start], nums[middle] = nums[middle], nums[start]
                start +=1
                middle +=1   
            elif nums[middle]==1:
                middle +=1
            else:
                nums[end], nums[middle] = nums[middle], nums[end]
                end -=1
                
    # we start with three pointers (start, mid, end): at start, mid = 0
    #move the start and mid pointer if nums[i] == 0, if nums[i] == 1, only move the middle, else: move the end by -1. in 1st and 3rd case, start will always be sway by end, and end will be swapped by middle respecively 