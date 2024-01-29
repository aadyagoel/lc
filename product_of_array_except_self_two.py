class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1]*n
        tempprefix = 1
        temppostfix = 1
        for i in range(len(nums)):
            if i == 0:
                answer[i] = 1
                answer[n-1-i] = 1
                #tempprefix = 1
                #temppostfix = 1
                continue
            tempprefix = tempprefix*nums[i-1]
            temppostfix = temppostfix*nums[n-i]
            answer[i] = answer[i]*tempprefix  
            answer[n-1-i] = answer[n-1-i]*temppostfix
            #answer[i] = answer[i-1]*nums[i-1] * answer[i]
            #answer[n-1-i] = answer[n-i]*nums[n-i] * answer[n-1-i]
        return answer
#just using answer in the same for loop makes prefix values dependent #on that array which are also being changed by postfix