import snap
import TSSImplementation as tss

def set_static_treshold(graph, hash_table, value):
    for v in graph.Nodes():
        hash_table[v.GetId()] = value
    return hash_table


def set_degree_based_treshold(graph, hash_table, degrees):
    for v in graph.Nodes():
        hash_table[v.GetId()] = degrees[v.GetId()]
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
    set_static_treshold(graph, t, 6)

    # Set the treshold for each node based on its degree
    #set_degree_based_treshold(graph, t, degrees)

    s = tss.tss(snap.ConvertGraph(type(graph), graph), t)

    print("Nodi nel seed set: \n")
    for node_id in s:
        print(str(node_id) + " ")

def test():
    graph = snap.LoadEdgeListStr(snap.TUNGraph, "dataset/twitch/test/test.csv", 0, 1)
    degrees = graph.GetDegSeqV()
    for i in range(0, degrees.Len()):
        print("Node %s has degree %s" % (i, degrees[i]))

if __name__ == "__main__":
    exec()
    # test()
