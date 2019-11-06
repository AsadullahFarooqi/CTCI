def bfs(node, node2):
    if node == None:
        return node
    visited = {}

    Q = deque()
    Q.append(node)
    while len(Q):
        node = Q.popleft()
        if node in visited:
            continue
        if node == node2:
            return True

        print(node.val, [x.val for x in node.children])
        visited[node] = True
        
        if len(node.children):
            Q += node.children
    return False