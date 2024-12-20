class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums = [-1,0,1,2,-1,-4], nums[i]+num[j] + num[k] == 0 l, r
        #         i l         r
        res= []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l = i +1
            r= len(nums)-1
            
            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l +=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l +=1 
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res 
                    
        
            
      