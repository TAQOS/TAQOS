###############################################################################
#
#   utils.py - Utilities for quantum instruction compiler
#
#   Authors: Harley Patton
#   Created on: July 12, 2017
#   Last modified: July 18, 2017
#
###############################################################################

import networkx as nx

def build_graph(edges):
    """
    Builds a graph with the given edge list

    :param edges: list of edges
    :return: a graph
    """
    g = nx.Graph()
    for edge in edges:
        g.add_edge(edge[0], edge[1])
    return g
