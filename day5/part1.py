import os

from collections import defaultdict, deque


def topological_sort_subset(constraints, subset):
    # Filter the constraints to only include the subset
    subset = set(subset)
    filtered_constraints = [(a, b) for a, b in constraints if a in subset and b in subset]

    # Build the graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for before, after in filtered_constraints:
        graph[before].append(after)
        in_degree[after] += 1
        if before not in in_degree:
            in_degree[before] = 0

    # Find all nodes in the subset with in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0 and node in subset])
    topological_order = []

    while queue:
        current = queue.popleft()
        topological_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycles in the subset
    if len(topological_order) != len(subset):
        raise ValueError("Graph has a cycle involving the subset; topological sort not possible.")

    return topological_order

rules, groups = open(os.path.dirname(__file__) + '/input.txt', 'r').read().split('\n\n')

constraints = []

total = 0

for rule in rules.split('\n'):
    constraints.append(tuple(map(int, rule.split('|'))))

for group in groups.split('\n'):
    current = list(map(int, group.split(',')))
    valid = True

    if current == topological_sort_subset(constraints, current):
        total += current[len(current) // 2]

print(total)
