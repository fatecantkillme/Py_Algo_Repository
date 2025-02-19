class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left=max(weights)
        right=sum(weights)
        while left<right:
            mid=left+(right-left>>1)
            if self.if_ok(weights,days,mid):
                right=mid
            else:
                left=mid+1
        return left
    
    def if_ok(self,weight,days,mid):
        res=1
        cureent=0
        for item in weight:
            cureent+=item
            if cureent >mid:
                res+=1
                cureent=item
        if res<=days:
            return True
        else: 
            return False
        
solution=Solution()
weights=[1,2,3,4,5,6,7,8,9,10]
days=5
print(solution.shipWithinDays(weights,days))