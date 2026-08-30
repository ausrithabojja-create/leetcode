class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        max_count = 0
        for rank in ranks:
            max_count = max(max_count, ranks.count(rank))
        if max_count >= 3: 
            return "Three of a Kind"
        if max_count == 2:
            return "Pair"
        return "High Card"

        