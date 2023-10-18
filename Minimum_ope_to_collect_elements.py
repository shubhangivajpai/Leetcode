#2869 leetcode
# Minimum Operations to collect elements
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        set1=set()
        i=len(nums)-1
        while len(set1)<k:
            if nums[i]<=k:
                set1.add(nums[i])
            i-=1
        return len(nums)-i-1
