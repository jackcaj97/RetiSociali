import snap
import TSSImplementation as tss

def set_static_treshold(hash_table, graph, value):
    for v in graph.Nodes():
        hash_table[v.GetId()] = value
    for key in hash_table:
        hash_table[key] = value
    return hash_table


def set_degree_based_treshold(hash_table, degrees):
    for key in hash_table:
        hash_table[key] = degrees[key]
    return hash_table


def exec():
    # Load Graph
    # noinspection PyUnresolvedReferences
    graph = snap.LoadEdgeListStr(snap.TUNGraph, "dataset/twitch/ENGB/musae_ENGB_edges.csv", 0, 1)

    # Get the degree of each node by storing them into an hash-table
    # noinspection PyUnresolvedReferences
    degrees = graph.GetDegSeqV()
    for i in range(0, degrees.Len()):
        print("Node %s has degree %s" % (i, degrees[i]))

    # Creates an hash-table used to store the treshold for each node.
    # noinspection PyUnresolvedReferences
    t = snap.TIntH()

    # Set the treshold for each node statically
    set_static_treshold(t, graph, 1)

    # Set the treshold for each node based on its degree
    #set_degree_based_treshold(t, degrees)

    s = tss.tss(snap.ConvertGraph(type(graph), graph), t)

if __name__ == "__main__":
    exec()
