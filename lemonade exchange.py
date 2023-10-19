#860. Lemonade Change

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dict1={5:0,10:0}
        for i in bills:
            if i==5:
                dict1[5]+=1
            elif i==10 and dict1[5]:
                dict1[10]+=1
                dict1[5]-=1
            elif i==20 and((dict1[5] and dict1[10]) or dict1[5]>=3 ):
                if dict1[5] and dict1[10]:
                    dict1[5]-=1
                    dict1[10]-=1
                else:
                    dict1[5]-=3
            else:
                return False
        return True
