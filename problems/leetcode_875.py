class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        right=sum(piles)
        left=1
        while left<right:
            k=left+(right-left>>1)
            piles_copy=[item for item in piles]
            if self.if_ok(piles_copy,h,k):
                right=k
            else:
                left=k+1
        return left

    def if_ok(self,piles,h,k):
        time_sum=0
        for item in piles:
            time_sum+=(item+k-1)//k
        if time_sum <=h:
            return True
        else:
            return False
    
solution=Solution()
piles=[312884470]
h=312884469
print(solution.minEatingSpeed(piles,h))