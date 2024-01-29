#neetcode solution; mine was a nested for loop and exceeded time limit
#this is such a nice solution, like just 1 multiplication and the rest #divisions; but we're not allowed divisions 
#values before num[i] * values after num[i]
#soln 1
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1]*n
        postfix = [1]*n
        answer = []
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
                postfix[n-1-i] = 1
                continue
            prefix[i] = prefix[i-1]*nums[i-1]
            postfix[n-1-i] = postfix[n-i]*nums[n-i]
        print(postfix)
        print(prefix)
        for j in range(len(nums)):
            ans = prefix[j]*postfix[j]
            answer.append(ans)
        return answer
