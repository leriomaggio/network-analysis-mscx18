import numpy as np

def ecdf(data):
    """Calucalte the ECDF from a distribution of values 
    (i.e. centrality metrics of nodes in a Graph)"""
    return np.sort(data), np.arange(1, len(data)+1) / len(data)
