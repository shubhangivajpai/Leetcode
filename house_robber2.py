class Solution:
    def rob(self, nums: List[int]) -> int:
        def max_price(nums1):
            n = len(nums1)
            prev1=nums1[0]
            prev2=0
            for i in range(1,n):
                take=nums1[i]
                if i>1:
                    take+=prev2
                not_take=0+prev1
                curr=max(take,not_take)
                prev2=prev1
                prev1=curr
            return prev1
        if len(nums)<=1:
            return nums[0]
        ans1=max_price(nums[1:]) # when the house at first is not included
        ans2=max_price(nums[:-1]) # when house at last is not included
        return max(ans1,ans2)
        
    
