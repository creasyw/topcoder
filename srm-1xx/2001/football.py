# It looks like a typical DP problem. It sounds like a DP problem. And, it is solved like a DP
# problem. However, there is one bite hidding in the solution. The number of COMBINATIONS. It
# conflicts with the typical DP steps deriving the value from left side (0) to the right side (input
# value). If we simply adding the values up, then 2+3+2 and 2+2+3 would be regarded as two solutions.
# To remove this kind of duplicated solutions, in each value, we have to also remember how many 2s,
# 3s, and 7s in each solution.
#
# As a result, the next question is that "how to distinguish the same combinations with different
# orders"? There are two ways. If we go with the previous thought to /only/ accumulate the sum,
# there must be a way to store each unique solution for the given sum so that one can distinguish
# the duplicated ways of a combination. An easier way is to map the three possbile scores as a 3D
# plane where each point stands for a unique combination of three vectors. So, we only need to find
# the decompositions of all of the vectors within a /given range/, we know how many unique points
# are there for a specific value. That is the function =fetchCombinations_detailed=.
#
# Then, the solution get simpler... there is no need to store any of the value in that 3D cube.
# Because we move the X, Y, Z axis as the numbers of 2-, 3-, and 7- points. It guarantees there is
# no duplicated ways for a combination. Besides, none of the point uses previous values. So, we only
# need to count the points that equals to the given value.



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


f = Football()
assert f.fetchCombinations(2) == 1
assert f.fetchCombinations(4) == 1
assert f.fetchCombinations(34) == 19
assert f.fetchCombinations(47) == 33
assert f.fetchCombinations(1) == 0
print("Everthing is passed")
