class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        ans=1
        left=points[0][0]
        right=points[0][1]
    
        print(points)
        for i in range(1,len(points)):
            if points[i][0]>right:
                ans+=1   
                right=points[i][1]
            else:
                left=max(left,points[i][0])
                right=min(right,points[i][1])


        return ans

            