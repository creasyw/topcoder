# This question is hard in a unique way - for most of the cases, the DP question has one or multiple
# degrees of freedoms so that we can abstract them into different axis. The basic assumption is that
# these axis are independent from one another. However, in this case, there are two degrees of
# freedoms while we can move one element from one axis to the other...
#
# Actually, I lie... the capacity is the third degree of freedom.
#
# There are three conditions for each deer. 1) Its antlers are at the edge of the capacity -
# meaning, we cannot switch either of them with another antler. 2) Its antlers are within the
# capacity. 3) They are out of capacity.
#
# +There is no operation for the first case. The third case has to work with the second or third case
# to find a solution (regardless of the "minimum" number of operations).+
#
# Fuck, it is hard! All three cases can be move so that we can have the final result. e.g.,
# [4, 5] and [3, 3] with capacity as 1. The final result is [4, 3] and [5, 3].
#
# 1) we are moving the diffs between the two lists. The capacity is the absolute value of the
# differences between these two lists, but both positive and negative have meanings while we're
# switching the antlers.
#
# 2) Both the diff and the absolute values matter.
#
# Given two lists. Calculate the differences between them. The smallest possible solution equals
# ceil(number of pairs beyond capacity / 2). The largest possible result is N - 1, where N is the
# length of either given list. But the annoying part is that only the number of operations increases
# +monotonically+, but the actual combination of a sub-problem does not guarantee to be a part of the
# solution for the consequent problem for a larger scope -- all paires beyond the capacity are
# subject to change.
#
# It is not a typicla fucking incremental (aka. left-to-right sequential) problem - it is not
# guaranteed that the solution of N pairs is larger than N-1 pairs. The sequence does not matter.
# The residual capacity of a pair or pairs also does not really matter. The essential part is to
# /find the sub problems/ that converts the pairs beyond capacity to within capacity. Finally,
# combining all groups within capacity derives the final result.
#
# 【TCO13 Round 3B 450】AntlerSwapping 首先如果一个集合的鹿经过若干次交换之后可以让所有鹿都平衡，那
# 么一定存在交换次数小于集合大小的方案（相当于找一颗最大的生成森林）。于是就可以状压DP，每一个状态只
# 可能由自己内部交换或者由两个子集合并而来，内部交换的次数可以直接视为集合大小-1，因为更优的值一定可
# 以从子集中合并上来。判断一个集合能不能都平衡只要对角的大小排序即可。


class Group:
    def __init__(self, left, right, capacity):
        self.register = sorted([left, right])
        self.capacity = capacity
        self.balanced = abs(left - right) <= capacity
        if self.balanced:
            self.counter = 0
        else:
            self.counter = -1

    def __repr__(self):
        return "Register: " + str(self.register) + ". Balanced:" + str(self.balanced) + ". Counter:" + str(self.counter)

    @property
    def max(self):
        return self.register[-1]

    @property
    def min(self):
        return self.register[0]

    def merge(self, g2):
        self.register = sorted(self.register + g2.register)
        if self.balanced and g2.balanced:
            self.counter += g2.counter
            return
        for i in range(0, len(self.register), 2):
            if self.register[i + 1] - self.register[i] > self.capacity:
                self.counter = -1
                self.balanced = False
                return
        self.counter = len(self.register) // 2 - 1
        self.balanced = True
        return


class AntlerSwapping:
    def getmin(self, a, b, c):
        register = []
        for i in range(len(a)):
            register.append(Group(a[i], b[i], c))

        if len(register) == 1:
            return register.balanced

        register.sort(key=lambda k: k.min)
        while len(register) > 1:
            first = register[0]
            second = register[1]
            if first.max > second.min:
                first.merge(second)
                register.pop(1)
                print(register)
                continue
            break

        counter = 0
        for group in register:
            if group.counter == -1:
                return -1
            counter += group.counter

        return counter


sol = AntlerSwapping()

#ans = sol.getmin([3,2,2], [3,5,5], 0)
#print(ans, ans == 1)

ans = sol.getmin([4, 2, 6, 4, 8, 5, 2, 3], [3, 4, 5, 2, 8, 5, 7, 6], 1)
print(ans, ans == 2)
