from collections import deque


class TriesNode:

    def __init__(self, c):
        self.c = c  # c means the character
        self.children = []


def append_childs(n, s):
    print("append_childs", s)
    for i in s:
        n.children.append(TriesNode(i))
        n = n.children[-1]


def found(root, c):
    for child in root.children:
        if child.c == c:
            return True, child
    return False, root


def insert_word(root, s):
    if not len(s):
        return

    i = 0
    while i < len(s):
        t = found(root, s[i])
        if t[0] == False:
            break
        root = t[1]
        i += 1

    if i < len(s):
        append_childs(root, s[i:])


def bfs(root):
    if root == None:
        return root

    Q = deque()
    Q.append(root)
    while len(Q):
        root = Q.popleft()
        print(root.c, [x.c for x in root.children], end=" ")
        if len(root.children):
            Q += root.children
            print()


def main():
    words = ["Many", "asad", "My", "Lie", "A", "M"]
    root = TriesNode("*")
    for w in words:
        insert_word(root, w.lower())

    bfs(root)


if __name__ == '__main__':
    main()
