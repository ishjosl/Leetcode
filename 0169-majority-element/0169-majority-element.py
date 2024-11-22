class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                element = num
            count +=1 if element == num else -1
            
        return element

    # keeping track og our current element and our current count
      
            