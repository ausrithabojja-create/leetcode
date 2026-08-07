class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        Vowels={"a","e","i","o","u"}
        for i in range(k):
            if s[i] in Vowels:
                count+=1
        max1=count
        for j in range(k,len(s)):
            if s[j-k] in Vowels:
                count-=1
            if s[j] in Vowels:
                count+=1
            max1=max(max1,count)
        return max1


        