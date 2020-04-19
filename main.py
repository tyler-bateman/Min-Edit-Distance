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
        bt[i][0] = LEFT 
    for j in range(1, m):
        dist[0][j] = dist[0][j-1] + deletecost
        bt[0][j] = DOWN 

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
                bt[i][j] = DIAG 
            elif dist[i][j] == inscost:
                bt[i][j] = LEFT 
            else:
                bt[i][j] = DOWN

    # return min edit distance
    return (dist[n-1][m-1], bt)

def generate_alignment(target, source, bt):
    t_format = ""
    connections = ""
    s_format = ""
    n = len(target) 
    m = len(source)
    while m > 0 or n > 0:
        if bt[n][m] == DIAG:
            t_format = target[n - 1] + " " + t_format
            s_format = source[m - 1] + " " + s_format
            connections = "| " + connections if target[n - 1] == source[m - 1] else "  " + connections
            n -= 1
            m -= 1
        elif bt[n][m] == LEFT:
            t_format = target[n - 1] + " " + t_format
            s_format = "_ " + s_format
            connections = "  " + connections
            n -= 1
        else:
            t_format = "_ " + t_format
            s_format = source[m - 1] + " " + s_format 
            connections = "  " + connections
            m -= 1
    return (t_format, connections, s_format)



if __name__ == "__main__":
    if len(argv) > 2:
        dist_data = distance(argv[1], argv[2], 1, 1, 2) 
        print "levenshtein distance = {}".format(dist_data[0])
        for s in generate_alignment(argv[1], argv[2], dist_data[1]):
            print s
