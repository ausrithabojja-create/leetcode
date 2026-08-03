class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer1=[]
        answer2=[]
        for x in nums1:
            if x not in nums2 and x not in answer1:
                answer1.append(x)
        for x in nums2:
            if x not in nums1 and x not in answer2:
                answer2.append(x)
        return [answer1,answer2]
    
        