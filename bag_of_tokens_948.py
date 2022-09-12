import collections
from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        ans = 0
        tokens.sort()
        queue = collections.deque(tokens)
        while queue and (power >= queue[0] or score):
            # increase score while possible
            while queue and power >= queue[0]:
                score += 1
                power -= queue.popleft()
            ans = max(ans, score)
            # increase power if it makes sense
            if queue and score:
                score -= 1
                power += queue.pop()
        return ans

tokens = [100, 200]
power = 150
print(Solution().bagOfTokensScore(tokens, power))