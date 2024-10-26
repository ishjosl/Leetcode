class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
                 #ind
         #nums = [1,1,1,3,3,4,3,2,4,2]
                    #ind+1 
        sorted_nums = sorted(nums)
        for ind in range(len(sorted_nums)-1):
            curr =ind
            nxt= ind+1
            if sorted_nums[curr] == sorted_nums[nxt]:
                return True
        return False
        
        #return False if len(nums) == len(set(nums)) else True