# Rotate array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n  # to handle the cases where k is larger than n
        nums.reverse()
        print(nums)
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])

    # by seeing this question we can make out that we have to deal with the array from n-k therefore we can reverse the array and reverse the first k elements
