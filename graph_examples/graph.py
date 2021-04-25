# @file: graph.py
# @author: Daniel M. Sahu
# @brief: This class implements and adjacency-list based Graph object.

from graphviz import Digraph

class Graph:
    def __init__(self, num_nodes):
        """ Construct an empty Graph of size num_nodes.
        """
        self.nodes = {i:[] for i in range(1, num_nodes+1)}

    def add_edge(self, source, target, weight):
        """ Add a weighted edge from source -> target with the given weight.
        """
        # sanity checks
        assert (source in self.nodes), "Given unknown source node {}.".format(source)
        assert (target in self.nodes), "Given unknown target node {}.".format(target)

        # add the weighted edge
        self.nodes[source].append((target, weight))


    def _render(self):
        """ Convert to a graphviz version, for use of plotting methods

        A highly inefficient approach, since we basically construct an entirely
        new graph object.
        """
        dot = Digraph(comment="My Graph")

        # first initialize the nodes
        for node in self.nodes.keys():
            dot.node(str(node))

        # then add the edges
        for source, targets in self.nodes.items():
            for target, weight in targets:
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
        dot = self._render()
        print(dot.source)

        # return some string, so python doesn't get upset
        return ""

