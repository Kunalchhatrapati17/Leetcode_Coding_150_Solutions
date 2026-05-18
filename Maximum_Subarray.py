class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Line 1: Initialize both with nums[0]
        # We can't use 0 because array might be all negative
        max_sum = nums[0]   # stores the best answer found so far
        curr_sum = nums[0]  # stores current running subarray sum
        
        # Line 2: Start loop from index 1 (we already used index 0)
        for num in nums[1:]:
            
            # Line 3: THE CORE DECISION
            # Should I ADD this num to existing subarray?
            # OR start a FRESH subarray from this num?
            # Pick whichever is larger
            curr_sum = max(num, curr_sum + num)
            
            # Line 4: Update global best if current is better
            max_sum = max(max_sum, curr_sum)
        
        # Line 5: Return the best subarray sum found
        return max_sum
        
