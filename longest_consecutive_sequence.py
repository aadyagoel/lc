class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        answerarray = []

        for i in range(len(nums)):
            if nums[i]-1 in nums:
                continue
            else:
                j = 1
                temp = 1
                array = [nums[i]]
                while True:  
                    if nums[i]+j not in nums:
                        if temp > longest:
                            longest = temp
                            answerarray = array 
                        break

                    elif nums[i]+j in nums:
                        temp += 1
                        array.append(nums[i]+j)
                    j += 1
                    if temp > longest:
                        longest = temp
                        answerarray = array

        return longest 

        