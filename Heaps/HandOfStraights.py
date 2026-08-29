from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        count=Counter(hand)
        for card in sorted(count):
            while count[card]>0:
                for i in range(groupSize):
                    current=card+i
                    if count[current]==0:
                        return False
                    count[current]-=1
        return True