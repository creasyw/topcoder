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


def parent(index, register):
    n = register[index].parent
    while register[n].index != register[n].parent:
        n = register[n].parent
    return n

class Node:
    def __init__(self, left, right, capacity, index):
        self.parent = None
        self.index = index
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

    def merge(self, n2):
        if self.parent and parent(n2) == parent(self):
            return
        elif self.parent is None:
            self.parent = self.index

        self.register = sorted(self.register + n2.register)
        n2.parent = self.index
        if self.balanced and n2.balanced:
            self.counter += n2.counter
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
            register.append(Node(a[i], b[i], c, i))

        if len(register) == 1:
            return register.balanced

        distance = []
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                distance.append((abs(a[i] - a[j]) + abs(b[i]-b[j]), i, j))

        distance.sort(key=lambda k: k[0])
        while distance:
            _, i, j = distance.pop(0)
            register[i].merge(register[j])

        node = parent(0, register)
        return register[node].counter


sol = AntlerSwapping()

#ans = sol.getmin([3,2,2], [3,5,5], 0)
#print(ans, ans == 1)

ans = sol.getmin([4, 2, 6, 4, 8, 5, 2, 3], [3, 4, 5, 2, 8, 5, 7, 6], 1)
print(ans, ans == 2)
