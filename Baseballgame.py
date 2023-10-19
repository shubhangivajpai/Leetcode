#BASEBALL GAME

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in operations:
            if i=='C':
                res.pop()
            elif i=='D':
                a=int(res[-1])
                res.append(2*a)
            elif i=='+':
                a1=res[-1]
                a2=res[-2]
                res.append(int(a1+a2))
            else:
                res.append(int(i))
        return sum(res)

