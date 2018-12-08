# To rephrase the question:
#
# There are two kinds of costs for the type of questions about the distance between strings. One of
# them is a upfront cost - regardless of how many characters are replaced, this cost occur whenever
# there is one consecutive replacements. The other is an incremental cost (1 in this question) - each
# modification occurs one of this cost.
#
# This is a typical question about string distance, with minor modifications.
#
# Assuming the D[i, j] is the optimal cost between two sub-strings A[:i] and B[:j], it is the
# *smallest* value among three cases -
# - If they are different, there are two choices
#   - D[i, j-1] + cost, add the "-" from B.
#   - D[i-1, j] + cost, add the "-" from A.
#   - In either case, the "cost" depends whether it needs to pay the upfront charge.
# - If they are the same, there is /one more/ choice - use the value D[i-1, j-1].
#
# As a reuslt, there are /up to/ three possbile values in each *intermediate* step rather than only
# one /smallest/ result, because the upfront cost might be so high that it is cheaper to extend the
# "-" from a sub-optimal step than starting a new series of "-" from the optimal step.


class Node:
    def __init__(self, a, b, c):
        self.extenda = a
        self.extendb = b
        self.matched = c

    def __repr__(self):
        return str([self.extenda, self.extendb, self.matched])


class Alignment:
    def align(self, a, b, x):
        # The maximum possbile cost - intermittent using "-" for both A and B
        max_value = 2 * x * (len(a) + len(b))

        register = [Node(0, 0, 0)]
        for i in range(len(a)):
            register.append(Node(max_value, x + i + 1, max_value))

        for i, bc in enumerate(b):
            tmp = [Node(x + i + 1, max_value, max_value)]
            for j, ac in enumerate(a):
                if ac == bc:
                    matched = min(register[j].matched, register[j].extenda,
                                  register[j].extendb)
                else:
                    matched = max_value
                prev_a = register[j + 1]
                prev_b = tmp[-1]

                extenda = min(prev_a.extenda + 1, prev_a.extendb + x + 1,
                              prev_a.matched + x + 1)
                extendb = min(prev_b.extendb + 1, prev_b.extenda + x + 1,
                              prev_b.matched + x + 1)
                tmp.append(Node(extenda, extendb, matched))

            register = tmp

        last_item = register[-1]
        return min(last_item.extenda, last_item.extendb, last_item.matched)


a = Alignment()

ans = a.align("ABC", "ACE", 1)
print(ans, ans == 4)

ans = a.align("AA", "B", 1)
print(ans, ans == 5)

# AAABAAAABAA----
# AAA----ABAABAAA
ans = a.align("AAABAAAABAA", "AAAABAABAAA", 10)
print(ans, ans == 28)
