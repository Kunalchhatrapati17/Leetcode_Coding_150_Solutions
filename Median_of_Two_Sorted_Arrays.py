class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 1. Ensure the first array is the smaller one to minimize binary search steps
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n1, n2 = len(nums1), len(nums2)
        low, high = 0, n1

        while low <= high:
            # 2. Partition both arrays
            partition1 = (low + high) // 2
            partition2 = (n1 + n2 + 1) // 2 - partition1

            # 3. Handle edge cases with infinity
            l1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            r1 = float('inf') if partition1 == n1 else nums1[partition1]

            l2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            r2 = float('inf') if partition2 == n2 else nums2[partition2]

            # 4. Check if we found the correct partition
            if l1 <= r2 and l2 <= r1:
                # Odd total length
                if (n1 + n2) % 2 != 0:
                    return float(max(l1, l2))
                # Even total length
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            
            elif l1 > r2:
                # We are too far to the right in nums1, move left
                high = partition1 - 1
            else:
                # We are too far to the left in nums1, move right
                low = partition1 + 1

        return 0.0
