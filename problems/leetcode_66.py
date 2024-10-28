class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=len(digits)
        for i in range(1,n+1):
            if digits[-i]+1<=9:
                digits[-i]+=1
                return digits
            else:
                digits[-i]=0
        if digits[0]==0:
            digits.insert(0,1)
            return digits
                