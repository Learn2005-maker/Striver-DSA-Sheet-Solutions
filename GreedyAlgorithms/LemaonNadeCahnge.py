

class Solution:
    def lemonadeChange(self, bills):
        fives=0
        tens=0
        for s in range(len(bills)):
            if bills[s]==5:
                fives+=1
            elif bills[s]==10:
                if fives:
                    tens+=1
                    fives-=1
                else:
                    return False
            else:
                if fives and tens:
                    fives-=1
                    tens-=1
                elif fives>=3:
                    fives-=3
                else:
                    return False
        return True
    

s=Solution()

print(s.lemonadeChange(bills=[5,5,5,10,20]))
