class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        output = []
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        while k > 0:
            highest_value = 0
            highest_key = 0
            for value in d:
                if d[value] > highest_value:
                    highest_value = d[value]
                    highest_key = value
            output.append(highest_key)  
            del d[highest_key]
            k = k - 1
        return output