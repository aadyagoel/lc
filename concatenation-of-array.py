class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        twoN = 2*N
        ans = [None]*twoN
        for i in range(N):
            ans[i] = nums[i]
            ans[i+N] = nums[i]
        return ans