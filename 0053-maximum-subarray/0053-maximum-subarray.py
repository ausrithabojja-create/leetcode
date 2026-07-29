class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        curr_sum=nums[0]
        start=end=temp=0
        for i in range(1,len(nums)):
            if nums[i]>curr_sum+nums[i]:
                curr_sum=nums[i]
                temp=i
            else:
                curr_sum+=nums[i]

            if curr_sum>max_sum:
                max_sum=curr_sum
                start=temp
                end=i
        return max_sum  
     
       
                

        