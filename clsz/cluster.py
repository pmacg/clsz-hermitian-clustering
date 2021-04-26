"""
This module contains an implementation of the CLSZ algorithm for clustering directed graphs.
"""
import numpy as np
import scipy as sp
import scipy.sparse.linalg
from sklearn.cluster import KMeans
import math
import networkx as nx


def cluster_hermitian(hermitian_adjacency, k):
    """
    Given a sparse hermitian adjacency matrix, compute the clusters given by the CLSZ algorithm.

    :param hermitian_adjacency: the hermitian adjacency matrix of the graph
    :param k: the number of clusters to look for
    :return: a list of cluster labels assigned to each vertex in the graph.
    """
    eigenvalues, eigenvectors = sp.sparse.linalg.eigsh(hermitian_adjacency, k=int(2 * math.floor(k / 2)))
    input_to_kmeans = np.block([[np.real(eigenvectors), np.imag(eigenvectors)]])
    kmeans = KMeans(n_clusters=k).fit(input_to_kmeans)
    return kmeans.labels_


def cluster_networkx(directed_graph, k):
    """
    Given a directed networkx graph, find k clusters with the CLSZ algorithm.

    :param directed_graph: the graph to be clustered
    :param k: the number of clusters to find
    :return: a list of cluster labels assigned to each vertex in the graph.
    """
    adjacency_matrix = nx.adjacency_matrix(directed_graph)
    hermitian_adjacency = (adjacency_matrix * 1j) - (adjacency_matrix.transpose() * 1j)
    return cluster_hermitian(hermitian_adjacency, k)
