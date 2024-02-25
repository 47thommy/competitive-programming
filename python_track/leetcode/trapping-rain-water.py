class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxHeight=[0]
        rightMaxHeight=[0]
        maxLeft=height[0]
        maxRight=height[-1]
        for i in range(1,len(height)):
            leftMaxHeight.append(maxLeft)
            maxLeft=max(maxLeft,height[i])
        
        for i in range(len(height)-2,-1,-1):
            rightMaxHeight.append(maxRight)
            maxRight=max(maxRight,height[i])
        rightMaxHeight=rightMaxHeight[::-1]
        ans=0
        for i in range(len(height)):
            val=min(leftMaxHeight[i],rightMaxHeight[i])-height[i]
            if val>0:
                ans+=val
        return ans

