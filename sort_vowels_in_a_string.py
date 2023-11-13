#
# 'A': 65
# ↓
# 'Z': 90

# 'a': 97
# ↓
# 'z': 122
class Solution:
    def sortVowels(self, s: str) -> str:
        sorted_vowels=sorted([c for c in s if c.lower() in'aeiou'],reverse=True)
        res=[]
        for char in s:
            if char.lower() in 'aeiou':
                res.append(sorted_vowels.pop())
            else:
                res.append(char)
        return ''.join(res) 
