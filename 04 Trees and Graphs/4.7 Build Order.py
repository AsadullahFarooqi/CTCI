def build_order(p):
    ans = []
    dependencies_hash = {}
    project_hash = {}

    for i in p:
        if not dependencies_hash[i[0]] in dependencies_hash:
            dependencies_hash[i[0]] = []
        if not project_hash[i[1]] in project_hash:
            project_hash[i[1]] = []

        dependencies_hash[i[0]].append(i[1])
        project_hash[i[1]].append(i[0])

# Recursion (#8.10), System Design and Scalability (#9.2, #9.3)
# Sorting and Searching (#10.10), Hard Problems (#17.7, #17.12,
# 17.13, #17.14, #17.17, #17.20, #17.22, #17.25).
    