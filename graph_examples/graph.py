# @file: graph.py
# @author: Daniel M. Sahu
# @brief: This class implements and adjacency-list based undirected Graph object.

from graphviz import Graph as GraphvizGraph

class Graph:
    def __init__(self, num_nodes):
        """ Construct an empty undirected Graph of size num_nodes.

        Args:
            num_nodes:  The expected number of vertices.

        """
        self.nodes = {i:[] for i in range(1, num_nodes+1)}

    def edge_list(self):
        """ Returns the current graph as a sorted set of edges.

        Returns:
            edges: Set of tuples: (weight, source, target), where
                    source and target are arbitrary because this
                    is an undirected graph.
        """

        # inefficiently get all (non-duplicate) values
        edges = []
        for s, vals in self.nodes.items():
            for t, w in vals:
                # check if this pair has been processed already
                #  note, not doing any duplication checking for weights
                pair = [s,t]
                pair.sort()
                if tuple(pair) not in [(a,b) for _,a,b in edges]:
                    # new pair, append
                    edges.append((w,*pair))

        # sort and return
        edges.sort()
        return edges

    def node_list(self):
        """ Get a list of all current nodes.
        """
        return list(self.nodes.keys())

    def neighbors(self, node):
        """ Return a list of (neighbor, weight) for all neighbors of the given node.
        """
        return list(self.nodes[node])

    def add_edge(self, source, target, weight):
        """ Add a weighted edge from source -> target with the given weight.
        """
        # sanity checks
        assert (source in self.nodes), "Given unknown source node {}.".format(source)
        assert (target in self.nodes), "Given unknown target node {}.".format(target)

        # add the weighted edge (bidirectionally)
        self._add_edge(source, target, weight)
        self._add_edge(target, source, weight)

    def _add_edge(self, source, target, weight):
        # handle node duplication. It's ok to add a new edge with 
        #  the same weight, but not a different weight
        for t,w in self.nodes[source]:
            # check if the node already exists
            if t == target:
                if w != weight:
                    raise ValueError("Tried to add a new edge when a different weight exists.")
                else:
                    # node exists and is duplicated; don't do anything
                    return

        # if we've gotten this far it's a new node. add it
        self.nodes[source].append((target, weight))

    def _render(self):
        """ Convert to a graphviz version, for use of plotting methods

        A highly inefficient approach, since we basically construct an entirely
        new graph object.
        """
        dot = GraphvizGraph(comment="MyGraph")

        # first initialize the nodes
        for node in self.nodes.keys():
            dot.node(str(node))

        # then add the edges
        for weight, source, target in self.edge_list():
            dot.edge(str(source), str(target), label=str(weight))

        return dot

    def save(self, file_="graph"):
        """ Print current graph to terminal.
        """
        dot = self._render()
        dot.render(file_)
        print("Saved graph to file: {}.pdf".format(file_))


    def __str__(self):
        # convenience magic method wrapper for a pure terminal output
        result = "Adjacency List Graph Representation:"
        for node,list_ in self.nodes.items():
            result = result + "\n\t{}: {}".format(node,list_)
        result += "\n"

        return result

