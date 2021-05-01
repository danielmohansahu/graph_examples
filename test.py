#!/usr/bin/env python3

import code

from graph_examples.graph import Graph
from graph_examples.algorithms.kruskal import min_spanning_tree
from graph_examples.algorithms.dijkstra import shortest_path

# expected location of file data and key metadata
GRAPH_DATA = "example/graph_info.txt"
NUM_NODES = 20
NULL_WEIGHT = 999

if __name__ == "__main__":

    ###########################################################################
    ##################### Problem Setup, Graph Construction ###################
    ###########################################################################

    # load graph data and add to our graph object
    g = Graph(NUM_NODES)
    source, target = 1, 1
    for i, w in enumerate(open(GRAPH_DATA, "r")):
        # format index, weights
        (idx, weight) = (i+1, int(w.strip()))

        # add an edge if this is a valid weight
        if weight != NULL_WEIGHT:
            g.add_edge(source, target, weight)

        # update indices
        target += 1
        if (target > NUM_NODES):
            target = 1
            source += 1

    # print graph to file
    g.save()

    # print out adjacency list representation
    print(g)

    ###########################################################################
    ###################### Kruskal's Minimum Spanning Tree ####################
    ###########################################################################

    # call algorithm
    mst, weight = min_spanning_tree(g)
    print("Found MST with {} nodes and a cost of {}.".format(len(mst),weight))

    print("@TODO, figure out what 'parent' means in this context")


    ###########################################################################
    ######################### Dijkstra's Shortest Path ########################
    ###########################################################################

    path, cost = shortest_path(g, 3, 19)
    print("Found shortest path from {}->{}: {}, cost: {}".format(
        3, 19, "->".join([str(p) for p in path]), cost))


    # code.interact(local=locals())

