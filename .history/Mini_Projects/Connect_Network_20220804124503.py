# https://docs.google.com/document/d/11w0Yf1b0HEKwlMdChv3Z9pBFstcsL5kegR5BHYBt3Ns/edit

n = 3
conn = [[0, 1],[0, 2], [0, 3], [1, 2]]
def makeConnected(n, connections):
    cables_req = range(n)
    if(len(connections) < n-1):
        return -1
    for item in connections:
        print(item)

print(makeConnected(n,conn))

