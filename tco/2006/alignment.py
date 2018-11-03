# To rephrase the question:
#
# There are two kinds of costs for the type of questions about the distance between strings. One of
# them is a one-time cost - regardless of how many characters are replaced, this cost occur whenever
# there is one consecutive replacements. The other is an incremental cost (1 in this question) - each
# modification occurs one of this cost.
#
# This is a typical question about string distance, with minor modifications.
#
# Say for two specific characters in the two given strings A[i] and B[j]:
# - If they are different, the only choice is to use a "-". The cost increases accordingly.
# - If they are the same, there are two choices. Let them match each other and keep the previous
#   cost. Or defer the match and increase the cost.
#
# Imagine a 2D matrix x with A as columns and B as rows
# To find the minimum value for the spot x[i][j], there are three possibilities:
# - x[i-1][j] --> x[i][j]: extending A for a "-"
# - x[i][j-1] --> x[i][j]: extending B for a "-"
# - x[i-1][j-1] --> x[i][j]: extending A and B each for a "-" if A[j] != B[i]. Otherwise, keep the
#   value of x[i-1][j-1].
#
# The cost of adding a "-" depending on if the previous place is an extension of "-" or a matching.
# To split the tie, extending "-" is preferred since it covers the one-time cost in the value.

class Alignment:

    def align(self, a, b, x):
        register = [(0, x, 0)]
        for i in range(len(a)):
            register.append((x+i+1, x, 0))

        print("")
        print(register)
        for i, cb in enumerate(b):
            current = [(x+i+1, 0, x)]
            for j, ca in enumerate(a):
                if ca == cb:
                    if register[j+1][0] + register[j+1][1] < current[-1][0] + current[-1][2]:
                        spot = (register[j+1][0] + 1 + register[j+1][1], 0, register[j+1][2])
                    else:
                        spot = (current[-1][0] + 1 + current[-1][2], current[-1][1], 0)
                    if register[j][0] < spot[0]:
                        spot = (register[j][0], x, x)
                else:
                    if register[j+1][0] + register[j+1][1] < current[-1][0] + current[-1][2]:
                        spot = (register[j+1][0] + 1 + register[j+1][1], 0, register[j+1][2])
                    else:
                        spot = (current[-1][0] + 1 + current[-1][2], current[-1][1], 0)
                    if register[j][0] + 2*x + 2 <= spot[0]:
                        spot = (register[j][0] + 2*x + 2, 0, 0)
                current.append(spot)
            register = current
            print(register)
        return register[-1][0]

a = Alignment()

ans = a.align("ABC", "ACE", 1)
print(ans, ans == 4)

ans = a.align("AA", "B", 1)
print(ans, ans == 5)

# AAABAAAABAA----
# AAA----ABAABAAA
ans = a.align("AAABAAAABAA", "AAAABAABAAA", 10)
print(ans, ans == 28)
