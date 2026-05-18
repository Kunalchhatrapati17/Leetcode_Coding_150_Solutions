class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # Line 1: Initialize all trackers with nums[0]
        # Same reason as before — array could be all negative
        max_sum  = nums[0]   # best answer for Case 1 (no wrap)
        curr_max = nums[0]   # current running max (Kadane's)
        
        min_sum  = nums[0]   # best answer for Case 2 (min middle)
        curr_min = nums[0]   # current running min (reverse Kadane's)
        
        total = nums[0]      # total sum of entire array
        
        # Line 2: Loop from index 1 (index 0 already used)
        for num in nums[1:]:
            
            # Line 3: SAME as Problem 1 — find max subarray
            curr_max = max(num, curr_max + num)
            max_sum  = max(max_sum, curr_max)
            
            # Line 4: OPPOSITE of Kadane's — find MIN subarray
            # min(num, curr_min + num)
            # Should I extend current min? Or start fresh min?
            curr_min = min(num, curr_min + num)
            min_sum  = min(min_sum, curr_min)
            
            # Line 5: Keep adding to get total sum of array
            total += num
        
        # Line 6: EDGE CASE — all numbers are negative
        # If max_sum < 0, every element is negative
        # total - min_sum would be 0 (empty), which is INVALID
        # So just return the least-negative element
        if max_sum < 0:
            return max_sum
        
        # Line 7: Return best of Case 1 vs Case 2
        # Case 1 = max_sum         (no wrap)
        # Case 2 = total - min_sum (wrap = remove minimum middle)
        return max(max_sum, total - min_sum)
