class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters1={}
        letters2={}
        for i in s:
            if i in letters1:
                letters1[i]+=1
                continue
            letters1[i]=1
        for i in t:
            if i in letters2:
                letters2[i]+=1
                continue
            letters2[i]=1
        if letters1==letters2:
            return True
        return False