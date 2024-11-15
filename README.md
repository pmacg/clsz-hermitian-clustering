# Hermitian Spectral Clustering

A Python implementation of the CLSZ algorithm for clustering directed graphs.

## Example

There is an example script showing how to use the code in `example.py`. You may first like to install the dependencies with

```
pip install -r requirements.txt
```

and then you can run the example with the following command.

```
python example.py
```

The example script constructs a simple directed graph using the networkx library and applies the CLSZ algorithm to find the
clusters.

## Reference

The primary reference for this algorithm is 

```Cucuringu, M., Li, H., Sun, H. and Zanetti, L., 2020, June. Hermitian matrices for clustering directed graphs: insights and applications. In International Conference on Artificial Intelligence and Statistics (pp. 983-992). PMLR.```

This implementation was developed as part of the experimental results reported in the paper

```Macgregor, P and Sun, H., 2021, Local Algorithms for Finding Densely Connected Clusters. In 38th International Conference on Machine Learning (ICML'21), pages 7268--7278.```

If you find this implementation useful in your work, acknowledgement of both the above papers would be appreciated.
