class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)-1
        i = 0
        sum = target+1 
        while sum !=target:
            sum = numbers[i] + numbers[n]
            if sum > target: 
                n = n-1
            elif sum < target:
                i = i + 1
            elif sum == target:
                return i+1, n+1
            