from random import randrange
from collections import deque

class GraphNode:

    def __init__(self, val):
        self.val = val  # c means the character
        self.children = []

class Graph:

    def __init__(self):
        self.nodes = []

def create_graph(G, N, childs):
    if not len(G.nodes):
        G.nodes.append(N)
        # N.children += [GraphNode(x) for x in childs]
        N.children += childs
        return G
    
    for n in G.nodes:
        if n.val == N.val:
            n.children += childs # [GraphNode(x) for x in childs]
    G.nodes += childs
    for c in childs:
        c.children += [N]
    return G.nodes[-1]


def bfs(node):
    if node == None:
        return node
    visited = {}

    Q = deque()
    Q.append(node)
    while len(Q):
        node = Q.popleft()
        if node in visited:
            continue
        print(node.val, [x.val for x in node.children])
        visited[node] = True
        
        if len(node.children):
            Q += node.children


def dfs(node):
    if node == None:
        return node

    visited = {}
    stack = []
    stack.append(node)
    while len(stack):
        node = stack.pop()
        if node in visited:
            continue
        visited[node] = True
        
        print(node.val, [x.val for x in node.children], end=" ")
        if len(node.children):
            stack += node.children
            print()


def print_adjacency_list(G):
    d = {}
    for i in G.nodes:
        print(i.val, " : ", [c.val for c in i.children])


def print_adjacency_matrix(G):
    mat = [[0 for i in range(len(G.nodes))] for j in range(len(G.nodes))]
    d = {n:i for i,n in enumerate(G.nodes)}
    # print([[k,v] for k,v in d.items()])
    # print(d)
    for n in G.nodes:
        row = d[n]
        for c in n.children:
            col = d[c]
            mat[row][col] = 1

    print("\t   ", [n.val for n in G.nodes])
    ith = 0
    for r in mat:
        s = len("\t   ") - len(str(G.nodes[ith].val))
        print([G.nodes[ith].val], " "*s, [c for c in r])
        ith += 1


def main():
    # nums = list({randrange(1,27) for x in range(25)})
    nums = [2, 4, 6, 9, 10, 11, 12, 14, 17, 21, 22, 24, 25, 26]
    print(nums)
    n = GraphNode(27)
    g = Graph()
    g.nodes.append(n)
    l = 0
    while l < len(nums):
        r = l+3
        # print(nums[l:r])
        childs = [GraphNode(e) for e in nums[l:r]]
        n = create_graph(g, n, childs)
        # n = n.children[-1]
        l = r

    # dfs(n)
    bfs(n)
    # print_adjacency_matrix(g)
    # print_adjacency_list(g)

if __name__ == '__main__':
    main()