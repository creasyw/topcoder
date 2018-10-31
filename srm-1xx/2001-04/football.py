# Problem Statement
#
# Create a class called Football. In football, scores are incremented by either
# 2, 3, or 7 points. Given a numerical input (integer between 1 and 75)
# representing a final score, calculate the number of all possible combinations
# of (2, 3, 7) which add up to that score. The output should be the number of
# combinations found. Here are a couple of examples:
#
# input | output | combinations
# 1       0
# 4       1        (2, 2)
# 9       3        (2, 7), (2, 2, 2, 3), (3, 3, 3)
# 11      3        (2, 2, 7), (2, 2, 2, 2, 3), (2, 3, 3, 3)
#
# Here is the method signature (be sure your method is public:
# int fetchCombinations(int input)
#
# We will check to make sure the input to this problem is valid.
#
# Definition
#
# Class:	Football
# Method:	fetchCombinations
# Parameters:	int
# Returns:	int
# Method signature:	int fetchCombinations(int param0)
#
# It looks like a typical DP problem. It sounds like a DP problem. And, it is solved like a DP
# problem. However, there is one bite hidding in the solution. The number of COMBINATIONS. It
# conflicts with the typical DP steps deriving the value from left side (0) to the right side (input
# value). If we simply adding the values up, then 2+3+2 and 2+2+3 would be regarded as two solutions.
# To remove this kind of duplicated solutions, in each value, we have to also remember how many 2s,
# 3s, and 7s in each solution.


class Football:
    def fetchCombinations(self, val):
        counter = 0
        for i in range(val // 7 + 1):
            for j in range(val // 3 + 1):
                for k in range(val // 2 + 1):
                    if 2 * k + 3 * j + 7 * i == val:
                        counter += 1
        return counter

    def fetchCombinations_detailed(self, val):
        register = []
        for i in range(val // 7 + 1):
            plane = []
            for j in range(val // 3 + 1):
                row = []
                for k in range(val // 2 + 1):
                    row.append(2 * k + 3 * j + 7 * i)
                plane.append(row)
            register.append(plane)

        counter = 0
        for i in register:
            for j in i:
                for k in j:
                    if k == val:
                        counter += 1
        return counter

    def dup_fetchCombinations(self, score):

        register = [0] * (score + 1)
        possible_scores = [2, 3, 7]

        for index in range(1, score + 1):

            if index in possible_scores:
                register[index] += 1

            if register[index] == 0:
                continue

            for i in possible_scores:
                if index + i >= score + 1:
                    continue
                register[index + i] += register[index]

        return register[-1]
