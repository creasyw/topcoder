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
# As a result, it is not a typicla fucking left-to-right sequential solved problem - because the
# sub-problem are not from left to right (or right to left) based on the given lists. The sequences
# do not matter. The essential part is to /find the sub problems/, whose combination is the final
# solution.
#
# 【TCO13 Round 3B 450】AntlerSwapping 首先如果一个集合的鹿经过若干次交换之后可以让所有鹿都平衡，那
# 么一定存在交换次数小于集合大小的方案（相当于找一颗最大的生成森林）。于是就可以状压DP，每一个状态只
# 可能由自己内部交换或者由两个子集合并而来，内部交换的次数可以直接视为集合大小-1，因为更优的值一定可
# 以从子集中合并上来。判断一个集合能不能都平衡只要对角的大小排序即可。

class AntlerSwapping:

    def getmin(a, b, c):
        pass
