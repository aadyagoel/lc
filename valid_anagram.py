class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictionary = {}
        for i in s:
            if i in dictionary:
                dictionary[i] +=1
            else:
                dictionary[i] = 1
        for j in t:
            if j in dictionary:
                dictionary[j] -= 1
            else:
                return False
        for k in dictionary:
            if dictionary[k] != 0:
                return False 
        return True 