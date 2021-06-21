import snap
import TSSImplementation as tss
import random
import math


def set_static_threshold(graph, hash_table, value):
    for v in graph.Nodes():
        hash_table[v.GetId()] = value
    return hash_table


def set_degree_based_threshold(graph, hash_table, proportion):
    for v in graph.Nodes():
        hash_table[v.GetId()] = math.ceil(proportion * v.GetOutDeg())  # e.g. 1/2 * node's degree
    return hash_table


def set_edge_probability(graph, hash_table):
    random.seed(123)
    for edge in graph.Edges():
        tupla = edge.GetId()
        key = str(tupla[0]) + "-" + str(tupla[1])
        hash_table[key] = random.random()
    return hash_table


def deferred_decision(graph, probability_hash_table):
    for edge in graph.Edges():
        number_generated = random.random()
        tupla = edge.GetId()
        key = str(tupla[0]) + "-" + str(tupla[1])
        if number_generated < probability_hash_table[key]:  # If random number generated is less than edge activation probability
            graph.DelEdge(tupla[0], tupla[1])

    return graph


def exe():
    # Load Graph
    # noinspection PyUnresolvedReferences
    graph = snap.LoadEdgeListStr(snap.TUNGraph, "dataset/twitch/ENGB/musae_ENGB_edges.csv", 0, 1)

    # Get the degree of each node by storing them into an hash-table
    # noinspection PyUnresolvedReferences

    '''
    degrees = graph.GetDegSeqV()
    for i in range(0, degrees.Len()):
        print("Node %s has degree %s" % (i, degrees[i]))
    '''

    '''
    # Set the threshold for each node statically
    #for i in range(1, 11):
        # Creates an hash-table used to store the threshold for each node.
        # noinspection PyUnresolvedReferences
    t = snap.TIntH()

    threshold = 6
    set_static_threshold(graph, t, threshold)
    s = tss.tss(snap.ConvertGraph(type(graph), graph), t)

    print("t = " + str(threshold) + " - seed set size = " + str(len(s)))
    '''

    # Set the threshold for each node based on its degree
    t = snap.TIntH()
    proportion = 1/2
    set_degree_based_threshold(graph, t, proportion)

    s = tss.tss(snap.ConvertGraph(type(graph), graph), t)

    print("proportion = " + str(proportion) + " - seed set size = " + str(len(s)))


    '''
    # Probability based deferred decision
    t = snap.TIntH()
    probability = snap.TStrIntH()

    set_edge_probability(graph, probability)

    threshold = 1
    set_static_threshold(graph, t, threshold)
    mean = 0
    for i in range(1, 11):
        s = tss.tss(deferred_decision(snap.ConvertGraph(type(graph), graph), probability), t)
        seed_set_size = len(s)
        mean = mean + seed_set_size
    mean = mean/10
    print("t = " + str(threshold) + " - mean seed set size = " + str(mean))
    '''

    '''
    print("Nodi nel seed set: \n")
    for node_id in s:
        print(str(node_id) + " ")
    '''


def test():
    graph = snap.LoadEdgeListStr(snap.TUNGraph, "dataset/twitch/test/test.csv", 0, 1)
    degrees = graph.GetDegSeqV()
    for i in range(0, degrees.Len()):
        print("Node %s has degree %s" % (i, degrees[i]))


if __name__ == "__main__":
    exe()
    # test()
