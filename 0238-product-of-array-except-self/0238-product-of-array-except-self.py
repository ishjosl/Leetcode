class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n  # Initialize output array with 1s
        
        # Calculate left products
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]
        
        # Calculate right products and multiply with left products
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
        
        return output
