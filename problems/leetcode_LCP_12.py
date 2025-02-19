class Solution(object):
    def minTime(self, time, m):
        """
        :type time: List[int]
        :type m: int
        :rtype: int
        """
        if len(time)==m:
            return 0
        left=min(time)
        right=sum(time)-m*min(time)
        while left <right:
            mid=left+(right-left>>1)
            if self.if_ok(time,m,mid):
                right=mid
            else:
                left=mid+1
        return left

    def if_ok(self,time,m,T):
        res=1
        curret_time=0
        max_time=-1
        for item in time:
            max_time=max_time if max_time >item else item
            curret_time+=item
            if curret_time-max_time >T:
                curret_time=item
                max_time=item
                res+=1
        if res<=m:
            return True
        else:
            return False

solution=Solution()
time=[94,92,90,57,6,89,63,15,91,74]
m=6
print(solution.minTime(time,m))