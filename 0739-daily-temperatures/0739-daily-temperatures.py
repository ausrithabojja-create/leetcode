class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0]*len(temperatures)
        stack=[]
        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                pre=stack.pop()
                answer[pre]=i-pre
            stack.append(i)
        return answer
        