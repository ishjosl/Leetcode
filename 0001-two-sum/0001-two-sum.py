class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen= {}
        for ind in range(len(nums)):
            num = nums[ind]
            if target-num in seen:
                return [ind, seen[target - num]]
            seen[num]= ind
        return seen
        
       
        #seen
        #nums = [1,3,2,7,11,15], target = 9 
                    #[2, 3]
            
        
        
            