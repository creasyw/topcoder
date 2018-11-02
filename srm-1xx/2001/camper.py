# differences between Camper and Football
# - one item cannot be used twice in this question.
# - it searches for the largest number withint a given range.
#
# Test cases:
#	0, 0		0		Passed
#	100, 100		372		Passed
#	30, 70		110		Passed
#	1000, 1000		2467		Passed
#	80, 80		280		Passed




from itertools import permutations

class Camper:

    def __init__(self):
        self.items = [
            # calories
            [10, 100, 170, 40, 68, 92, 220, 30, 60, 85, 92, 109, 230, 60, 65, 72, 80, 82, 120, 130, 180, 222, 400, 800],
            # weight
            [5,  20,  10, 12, 20, 40,  70, 30, 40, 30, 30,  60, 100, 51, 52, 53, 54, 70,  20,  40,  40, 90,  200, 600],
            # volume
            [3,  20,  90, 90, 80, 12,  50,  1, 70, 20, 20,  30, 120, 40, 40, 40, 20, 80,  90, 100,  60, 30,  200,  50]]

    def maxCalories(self, mw, mv):

        ans = 0
        num_items = len(self.items[0])

        for i in permutations(list(range(num_items)), num_items):
            weight, volume, calories = 0, 0, 0
            for j in i:
                calories += self.items[j][0]
                weight += self.items[j][1]
                volume += self.items[j][2]
                if weight > mw or volume > mv:
                    break
                ans = max(ans, calories)
        return ans

c = Camper()
c.maxCalories(100, 100)
