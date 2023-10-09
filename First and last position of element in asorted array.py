class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        list1=[-1,-1]
        list2=[]
        if target not in nums:
            return list1
        for i in range(len(nums)):
            if target==nums[i]:
                list2.append(i)
        return list2[0],list2[-1]
