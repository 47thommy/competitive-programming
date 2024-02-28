from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        
        index = deque(range(len(deck)))
        ans = [None] * len(deck)

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans