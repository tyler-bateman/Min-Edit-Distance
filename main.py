import sys
from sys import argv
from bt_constants import *

def distance(target, source, insertcost, deletecost, replacecost):
    n = len(target) + 1
    m = len(source) + 1
    # set up dist and initialize values
    dist = [ [0 for j in range(m)] for i in range(n)  ]
    bt = [[0 for j in range(m)] for i in range(n) ]
    for i in range(1, n):
        dist[i][0] = dist[i-1][0] + insertcost
    for j in range(1, m):
        dist[0][j] = dist[0][j-1] + deletecost

    #align source and target strings
    for j in range(1,m):
        for i in range(1,n):
            inscost = insertcost + dist[i-1][j]
            delcost = deletecost + dist[i][j-1]
            if source[j-1] == target[i-1]:
                add = 0
            else:
                add = replacecost
            substcost = add + dist[i-1][j-1]
            dist[i][j] = min(inscost, delcost, substcost)
            if dist[i][j] == substcost:
                bt[i][j] = SUBSTITUTE
            elif dist[i][j] == inscost:
                bt[i][j] = INSERT
            else:
                bt[i][j] = DELETE
    # return min edit distance
    return dist[n-1][m-1]


if __name__ == "__main__":
    if len(argv) > 2:
        print "levenshtein distance = {}".format(distance(argv[1], argv[2], 1, 1, 2))

