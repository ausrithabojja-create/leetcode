class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w=0
        max1=0
        for i in range(k):
            w+=nums[i]
        max1=w
        for i in range(k,len(nums)):
            w=w-nums[i-k]+nums[i]
            max1=max(max1,w)
        return max1/k

        # n=len(nums)-k+1
        # max1=0
        # for i in range(n):
        #     sum1=sum(nums[i:k+i])
        #     avg=sum1/k
        #     max1=max(max1,avg)
        # return max1

            
        