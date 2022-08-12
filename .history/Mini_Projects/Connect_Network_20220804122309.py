n = 6
conn = [[0, 1],[0, 2], [0, 3], [1, 2]]
def makeConnected(n, connections):
    if(len(connections) == n-1):
        return -1
    

print(makeConnected(n,conn))

