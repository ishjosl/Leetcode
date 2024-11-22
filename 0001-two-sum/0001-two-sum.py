class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ind in range(len(nums)):
            num = nums[ind]
            if target - num in seen:
                return [ind, seen[target - num]]
            seen[num]= ind
            
# Add number to dictionary, then loop through to find target - number. If target - num is found then return its index, if it is not found, then add it to the dictionary

# return the ind of current value and the index of value in dict