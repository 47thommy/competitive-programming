class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_length=len(cardPoints)-k
        left=0
        right=window_length
        total=sum(cardPoints)
        totalMinimum=sum(cardPoints[left:right])
        currentSum=totalMinimum
        for right in range(right,len(cardPoints)):
            currentSum-=cardPoints[left]
            currentSum+=cardPoints[right]
            left+=1
            totalMinimum=min(totalMinimum,currentSum) 
        ans=total-totalMinimum
        return ans
        