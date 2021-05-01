import math

def shortest_path(graph, source, target):
    """ Returns the shortest path from source -> target nodes in the given graph.

    This is a basic implementation of Dijkstra's Algorithm
    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode
    """

    # instantiate queue and first node
    path = {}
    Q = []
    for node in graph.node_list():
        if node != source:
            # queue for minimizing distance
            Q.append((math.inf, node))
            # keep track of the current tentative distance and
            #  neighbor of each node
            path[node] = (math.inf, None)

    # initialize source node
    Q.append((0, source))
    path[source] = (0, None)

    # iterate through queue based on next closest distance
    while len(Q) != 0:
        # sort queue and get next lowest neighbor
        Q.sort()
        dist, node = Q.pop(0)

        # get neighbors and distance to next node
        for neighbor, weight in graph.neighbors(node):
            # find this, if still in our queue
            queue_index = None
            for i,(w,n) in enumerate(Q):
                if n == neighbor:
                    queue_index = i

            if queue_index is None:
                # neighbor not in queue, skip
                continue

            # check if it's shorter to proceed here via 
            #  the current node than our queue's estimate
            alt = dist + weight
            if alt < Q[queue_index][0]:
                # update variables
                path[neighbor] = (alt, node)
                Q[queue_index] = (alt, neighbor)

    # backtrack to get the shortest path and cumulative costs
    traj = []
    current = target
    while True:
        _, parent = path[current]
        traj.append(current)

        # stop condition
        if parent is None:
            break
        current = parent

    # reverse path
    traj.reverse()

    # return path, cost
    return traj, path[target][0]


