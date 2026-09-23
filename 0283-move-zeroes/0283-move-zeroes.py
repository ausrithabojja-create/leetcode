class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result=0
        for num in nums:
            if num!=0:
                nums[result]=num
                result+=1
        while result<len(nums):
            nums[result]=0
            result+=1
        return nums

        