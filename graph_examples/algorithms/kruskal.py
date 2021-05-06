from collections import defaultdict

def min_spanning_tree(graph):
    """ Returns the Minimum Spanning Tree of the given Graph.

    This is a basic implementation of Kruskal's Algorithm
    https://en.wikipedia.org/wiki/Kruskal%27s_algorithm#Pseudocode
    """
    # initialize a dict (edge: weight) to hold our sets
    sets = []
    connections = defaultdict(list)

    # get the list of graph edges (u,v)
    sorted_edges = graph.edge_list()

    # iterate through edges, checking if duplicative or not
    for weight, source, target in sorted_edges:
        # check if either source / target are in our set list
        src_set = None
        tgt_set = None
        for idx, (set_, _) in enumerate(sets):
            if source in set_:
                assert (src_set is None), "Source set already found; duplicate sets!"
                src_set = idx
            if target in set_:
                assert (tgt_set is None), "Target set already found; duplicate sets!"
                tgt_set = idx

        # decide what to do based on findings
        parent = True
        if (src_set is None) and (tgt_set is None):
            # new set
            sets.append((set([source, target]), weight))
        elif src_set is None:
            # target set exists, add source node to it
            s,w = sets[tgt_set]
            sets[tgt_set] = (s.union({source, target}), w + weight)
        elif tgt_set is None:
            # source set exists, add target node to it
            s,w = sets[src_set]
            sets[src_set] = (s.union({source, target}), w + weight)
        elif tgt_set == src_set:
            # both belong to the same set (tree). skip, since
            #  the existing one is already lower cost
            parent = False
        else:
            # join two separate trees
            s1,w1 = sets[src_set]
            s2,w2 = sets[tgt_set]

            # update the source set and remove the target set
            sets[src_set] = (s1.union(s2), w1 + w2)
            sets.pop(tgt_set)

        if (parent):
            connections[source].append(target)
            connections[target].append(source)

    # return the minimum spanning tree and weight
    #  note we return the largest set, since theoretically we
    #  could have been given a disconnected graph
    mst = None
    weight = None
    for tree, w in sets:
        if mst is None or len(mst) < len(tree):
            mst = tree
            weight = w

    return mst, weight, connections

