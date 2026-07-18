class Solution:
    def rearrangeArray(self,nums: List[int]) -> List[int]:     
        pos=[]
        neg=[]
        ans=[]
        for num in nums:
            if num<0:
                pos.append(num)
            else:
                neg.append(num)
        for num in range(len(pos)):
            ans.append(neg[num])
            ans.append(pos[num])
        return ans

        