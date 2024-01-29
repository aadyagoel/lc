class Solution(object):
#neetcode solution although this uses a bit more memory than two
#dk how because both have 1 list and two temp variables
#this one has two for loops 
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        print(answer)
        postfix = 1
        for j in range(len(nums)- 1, -1, -1):
            answer[j]*=postfix
            postfix *= nums[j]
        return answer 