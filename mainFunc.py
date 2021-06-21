import snap
import TSSImplementation as tss


def set_static_threshold(graph, hash_table, value):
    for v in graph.Nodes():
        hash_table[v.GetId()] = value
    return hash_table


def set_degree_based_threshold(graph, hash_table, degrees):
    for v in graph.Nodes():
        hash_table[v.GetId()] = degrees[v.GetId()]
    return hash_table


def exec():
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

    # Set the threshold for each node statically
    #for i in range(1, 11):
        # Creates an hash-table used to store the threshold for each node.
        # noinspection PyUnresolvedReferences
    t = snap.TIntH()

    threshold = 1
    set_static_threshold(graph, t, threshold)
    s = tss.tss(snap.ConvertGraph(type(graph), graph), t)

    print("t = " + str(threshold) + " - seed set size = " + str(len(s)))

    # Set the threshold for each node based on its degree
    # set_degree_based_threshold(graph, t, degrees)

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
    exec()
    # test()
