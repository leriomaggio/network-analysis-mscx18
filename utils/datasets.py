"""
Python module containing utility functions to load the different 
datasets we will be using during the tutorial.

Most of the dataset have been gathered from the Konect network analysis repository
(http://konect.uni-koblenz.de)

Original version: https://github.com/ericmjl/Network-Analysis-Made-Simple/blob/master/custom/load_data.py
"""

import gzip
import json

import networkx as nx
import pandas as pd
from tqdm import tqdm


def load_seventh_grader_network():
    """
    Load the Seventh Grader Network: http://konect.uni-koblenz.de/networks/moreno_seventh
    
    DESCRIPTION:
    ===========
    This directed network contains proximity ratings between studetns from 29 seventh grade students 
    from a school in Victoria. Among other questions the students were asked to nominate 
    their preferred classmates for three different activities. 
    A node represents a student. An edge between two nodes shows that the left student 
    picked the right student as his answer. 
    The edge weights are between 1 and 3 and show how often the left student chose the right student 
    as his favourite.
    """
    # Read the edge list
    df = pd.read_csv('datasets/moreno_seventh/out.moreno_seventh_seventh',
                     skiprows=2, header=None, sep=' ')
    df.columns = ['student1', 'student2', 'count']

    # Read the node metadata
    meta = pd.read_csv(
        'datasets/moreno_seventh/ent.moreno_seventh_seventh.student.gender',
        header=None)
    meta.index += 1
    meta.columns = ['gender']

    # Construct graph from edge list.
    G = nx.DiGraph()
    for row in df.iterrows():
        G.add_edge(row[1]['student1'], row[1]['student2'],
                   count=row[1]['count'])
    # Add node metadata
    for n in G.nodes():
        G.node[n]['gender'] = meta.ix[n]['gender']
    return G


def load_facebook_network():
    # Read the edge list

    df = pd.read_csv('datasets/ego-facebook/out.ego-facebook',
                     sep=' ', skiprows=2, header=None)
    df = df[[0, 1]]
    df.columns = ['user1', 'user2']

    G = nx.DiGraph()
    for row in df.iterrows():
        G.add_edge(row[1]['user1'], row[1]['user2'])

    return G


def load_sociopatterns_network():
    """
    Load the Infectious Network: http://konect.uni-koblenz.de/networks/sociopatterns-infectious
    
    DESCRIPTION:
    ===========
    This network describes the face-to-face behavior of people during the exhibition 
    INFECTIOUS: STAY AWAY in 2009 
    at the Science Gallery in Dublin. 
    Nodes represent exhibition visitors; edges represent face-to-face contacts 
    that were active for at least 20 seconds. 
    Multiple edges between two nodes are possible and denote multiple contacts. 
    The network contains the data from the day with the most interactions.
    """
    # Read the edge list

    df = pd.read_csv(
        'datasets/sociopatterns-infectious/out.sociopatterns-infectious',
        sep=' ', skiprows=2, header=None)
    df = df[[0, 1, 2]]
    df.columns = ['person1', 'person2', 'weight']

    G = nx.Graph()
    for row in df.iterrows():
        p1 = row[1]['person1']
        p2 = row[1]['person2']
        if G.has_edge(p1, p2):
            G.edges[p1, p2]['weight'] += 1
        else:
            G.add_edge(p1, p2, weight=1)

    for n in sorted(G.nodes()):
        G.node[n]['order'] = float(n)

    return G


def load_physicians_network():
    """
    Load the Physicians Network: http://konect.uni-koblenz.de/networks/moreno_innovation
    
    DESCRIPTION:
    ===========
    This directed network captures innovation spread among 246 physicians in for towns in 
    Illinois, Peoria, Bloomington, Quincy and Galesburg. The data was collected in 1966. 
    A node represents a physician and an edge between two physicians shows that the left 
    physician told that the righ physician is his friend or that he turns 
    to the right physician if he needs advice or is interested in a discussion. 
    There always only exists one edge between two nodes 
    even if more than one of the listed conditions are true.
    """
    
    # Read the edge list
    df = pd.read_csv(
        'datasets/moreno_innovation/out.moreno_innovation_innovation',
        sep=' ', skiprows=2, header=None)
    df = df[[0, 1]]
    df.columns = ['doctor1', 'doctor2']

    G = nx.Graph()
    for row in df.iterrows():
        G.add_edge(row[1]['doctor1'], row[1]['doctor2'])

    return G


def load_propro_network():
    """
    Load the Protein-Protein Interaction Network: http://konect.uni-koblenz.de/networks/moreno_propro
    
    DESCRIPTION:
    ===========
    This undirected network contains protein interactions contained in yeast. 
    Research showed that proteins with a high degree were more important for the surivial 
    of the yeast than others. 
    A node represents a protein and an edge represents a metabolic interaction between two proteins. The network contains loops.
    """
    propro = pd.read_csv('datasets/moreno_propro/out.moreno_propro_propro.txt', 
                         skiprows=2, header=None, delimiter=' ')
    propro.columns = ['prot1_id', 'prot2_id']
    G = nx.Graph()
    G.add_edges_from(zip(propro['prot1_id'], propro['prot2_id']))

    return G


def load_crime_network():
    """
    Load the Crime Network: http://konect.uni-koblenz.de/networks/moreno_crime
    
    DESCRIPTION:
    ===========
    This bipartite network contains persons who appeared in at least one crime case as either a suspect, a victim, 
    a witness or both a suspect and victim at the same time. 
    A left node represents a person and a right node represents a crime. 
    An edge between two nodes shows that the left node was involved in the crime represented by the right node.
    
    """
    df = pd.read_csv('datasets/moreno_crime/out.moreno_crime_crime',
                     sep=' ', skiprows=2, header=None)
    df = df[[0, 1]]
    df.columns = ['personID', 'crimeID']
    df.index += 1

    # Read in the role metadata
    roles = pd.read_csv(
        'datasets/moreno_crime/rel.moreno_crime_crime.person.role',
        header=None)
    roles.columns = ['roles']
    roles.index += 1

    # Add the edge data to the graph.
    G = nx.Graph()
    for r, d in df.join(roles).iterrows():
        pid = 'p{0}'.format(d['personID'])  # pid stands for "Person I.D."
        cid = 'c{0}'.format(d['crimeID'])  # cid stands for "Crime I.D."
        G.add_node(pid, bipartite='person')
        G.add_node(cid, bipartite='crime')
        G.add_edge(pid, cid, role=d['roles'])

    # Read in the gender metadata
    gender = pd.read_csv(
        'datasets/moreno_crime/ent.moreno_crime_crime.person.sex', header=None)
    gender.index += 1
    for n, gender_code in gender.iterrows():
        nodeid = 'p{0}'.format(n)
        G.node[nodeid]['gender'] = gender_code[0]

    return G


def load_university_social_network():
    G = nx.read_edgelist('datasets/moreno_oz/out.moreno_oz_oz',
                         comments='%',
                         delimiter=' ',
                         data=[('rating', int)],
                         create_using=nx.DiGraph(),
                         nodetype=int)
    return G


def load_amazon_reviews():
    # Read raw data.
    data = []
    with gzip.open('datasets/amazon_reviews/reviews_Digital_Music_5.json.gz', 'rt') as f:
        for line in tqdm(f.readlines()):
            # Clean data
            line = line.strip('\n')
            # Parse with JSON
            j = json.loads(line)
            data.append(j)

    # Add nodes
    G = nx.Graph()  # noqa: N806
    for d in tqdm(data):
        G.add_node(d['asin'], bipartite='product')
        G.add_node(d['reviewerID'], bipartite='customer')

    # Add edges
    for d in tqdm(data):
        G.add_edge(d['reviewerID'], d['asin'])

    return G

