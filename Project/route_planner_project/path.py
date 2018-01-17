def shortest_path(M, start, goal):
    print("shortest path called")

    frontier = dict([(i,[start]) for i in M.roads[start]]) if start!=goal else {start:[]}
    explored = set([start])

    while frontier:
        explore = g_h(M, frontier, goal)
        for i in [i for i in M.roads[explore] if i not in frontier.keys()|explored]:
            frontier[i] = frontier[explore] + [explore]
        frontier = remove_frontier(M, frontier)

        if explore == goal:
            return frontier[explore] + [explore]

        explored.add(explore)
        del frontier[explore]

def heuristic(M, a, b):
    M=M.intersections
    return ((M[a][0]-M[b][0])**2+(M[a][1]-M[b][1])**2)**0.5

def g_h(M, frontier, goal):
    g_h = dict([(path_costs(M, frontier[node] + [node]) + heuristic(M, node, goal), node) for node in frontier])
    return g_h[min(g_h)]

def path_costs(M, path, cost=0):
    M=M.intersections
    for i in range(len(path) - 1):
        cost += ((M[path[i]][0] - M[path[i+1]][0])**2 + (M[path[i]][1] - M[path[i+1]][1])**2)**0.5
    return cost

def remove_frontier(M, frontier):
    delete = []
    nodes = list(frontier.keys())
    for node in nodes:
        for i in [i for i in nodes if i != node]:
            if frontier[i] != frontier[node]:
                if i in M.roads[node]:
                    if path_costs(M, frontier[node]+[node]+[i]) < path_costs(M, frontier[i]+[i]):
                        delete.append(i)
    for i in delete:
        if i in frontier:
            del frontier[i]
    return frontier
