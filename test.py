#!/usr/bin/env python3

import code

from graph_examples.graph import Graph

# expected location of file data and key metadata
GRAPH_DATA = "example/graph_info.txt"
NUM_NODES = 20
NULL_WEIGHT = 999

if __name__ == "__main__":

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

    # print graph
    g.save()

    # code.interact(local=locals())

