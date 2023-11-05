# Find the winner of the array game
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k==1:
            return max(arr[0],arr[1])
        if k>=len(arr):
            return max(arr)
        curr_win=arr[0]
        win_count=0
        for i in range(1,len(arr)):
            if curr_win>arr[i]:
                win_count+=1
            else:
                 curr_win=arr[i]
                 win_count=1
            if win_count==k:
                return curr_win
        return curr_win
        
