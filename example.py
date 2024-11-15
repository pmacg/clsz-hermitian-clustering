"""
This file demonstrates how to run the CLSZ algorithm.
"""
import networkx as nx
import clsz.cluster


def main():
    # Construct a graph
    sizes = [100, 100, 100]
    probs = [[0.02, 0.25, 0.02], [0.02, 0.02, 0.25], [0.25, 0.02, 0.02]]
    g = nx.stochastic_block_model(sizes, probs, directed=True)

    # Apply the CLSZ algorithm to find clusters
    labels = clsz.cluster.cluster_networkx(g, len(sizes))
    print(labels)


if __name__ == "__main__":
    main()
