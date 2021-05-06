#!/usr/bin/env python3

import code
import copy

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
    print("\n" + str(g))

    ###########################################################################
    ###################### Kruskal's Minimum Spanning Tree ####################
    ###########################################################################

    # call algorithm
    mst, weight, connections = min_spanning_tree(g)
    print("Found MST with {} nodes and a cost of {} via Kruskal's Algorithm.\n".format(len(mst),weight))

    # starting from "root" of 1, print out the children of each node
    completed = []
    remaining = [1]
    while len(remaining) > 0:
        # check connections of the remaining nodes
        new_nodes = []
        for node in remaining:
            for connection in connections[node]:
                # skip already processed ones
                if connection not in completed:
                    print("\t{} is the 'parent' of {}".format(node, connection))
                    new_nodes.append(connection)

        # switch to the new list
        completed += remaining
        remaining = new_nodes

    ###########################################################################
    ######################### Dijkstra's Shortest Path ########################
    ###########################################################################

    path, cost = shortest_path(g, 3, 19)
    print("\nFound shortest path via Dijkstra's from {}->{}: {}, cost: {}".format(
        3, 19, "->".join([str(p) for p in path]), cost))


    # code.interact(local=locals())

