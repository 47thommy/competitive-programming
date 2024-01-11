class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(cards)==len(set(cards)):
            return -1
        left=0
        ans=float('inf')
        check={}
        for end in range(len(cards)):
            if cards[end] in check:
                ans=min(ans,end-check[cards[end]]+1)
                left=check[cards[end]]+1
            check[cards[end]]=end
        return ans