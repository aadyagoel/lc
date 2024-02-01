class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #extract min, find consecutive, add to numbers list, if not go to next min
        if len(nums) == 0:
            return 0
        numbers = []
        index = 0
        while len(nums) > 0:
            minimum = nums[0]
            i = 0
            while i < len(nums):
                if nums[i] < minimum:
                    minimum = nums[i]
            current_sequence = [minimum]
            nums.remove(minimum)
            i += 1
            j = 0
            while j < len(nums):
                if nums[j] == current_sequence[-1] + 1:
                    current_sequence.append(nums[j])
                    nums.remove(nums[j])
                else:
                    j += 1
            numbers.append(current_sequence)
            index +=1 

        longest = max(len(sequence) for sequence in numbers)
        return longest
