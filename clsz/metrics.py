"""Provide methods for computing the cut imbalance metric associated with the CLSZ algorithm."""
import networkx as nx


def networkx_directed_cut_size(graph, set_s, set_t=None):
    """
    Compute the cut size between sets S and T in a directed networkx graph.

    If T is not given, assume it is the complement of S.

    :param graph: The graph as a networkx object
    :param set_s: The vertex set S
    :param set_t: The vertex set T, or None
    :return: The size of cut(S, T)
    """
    edges = nx.edge_boundary(graph, set_s, set_t, data="weight", default=1)
    return sum(weight for u, v, weight in edges)


def networkx_cut_imbalance(graph, vertex_set_l, vertex_set_r):
    """
    Compute the cut imbalance between the sets L and R as specified in CLSZ. This is defined to be

        CI(L, R) = 1/2 * abs[ (w(L, R) - w(R, L)) / (w(L, R) + w(R, L)) ]

    :param graph: the directed networkx graph on which to operate
    :param vertex_set_l: the set L
    :param vertex_set_r: the set R
    :return: the cut imbalance ratio CI(S, T)
    """
    w_s_t = networkx_directed_cut_size(graph, vertex_set_l, vertex_set_r)
    w_t_s = networkx_directed_cut_size(graph, vertex_set_r, vertex_set_l)
    return (1/2) * abs((w_s_t - w_t_s) / (w_s_t + w_t_s))
