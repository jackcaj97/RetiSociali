import snap


# noinspection PyUnresolvedReferences
def tss(graph: snap.TUNGraph, t):

    found_node = False
    s = set()

    while graph.GetNodes() != 0:   # Finché non è vuoto il grafo
        found_node = False

        for v in graph.Nodes():     # Scorrere i vertici
            if t[v.GetId()] == 0:
                print("Caso 1: t["+str(v.GetId())+"] = 0")
                for u in v.GetOutEdges():
                    t[u] = t[u] - 1         # Si riduce il threshold dei vicini
                    graph.DelEdge(v.GetId(), u)     # Si rimuovono gli archi con i vicini.
                graph.DelNode(v.GetId())            # Si rimuove il nodo.
                found_node = True
            elif v.GetOutDeg() < t[v.GetId()]:
                print("Caso 2: grado di "+str(v.GetId())+" pari a "+str(v.GetOutDeg())+" e minore di t[" + str(v.GetId()) + "] = " + str(t[v.GetId()]))
                s.add(v.GetId())        # Aggiunto v al seed set
                for u in v.GetOutEdges():   # Rimozione del nodo dal grafo
                    if t[u] > 0:
                        t[u] = t[u] - 1
                    graph.DelEdge(v.GetId(), u)
                graph.DelNode(v.GetId())
                found_node = True

        if not found_node:      # Se non è stato trovato un nodo da rimuovere per il threshold
            temp_max = -1
            node_id = -1
            for v in graph.Nodes():     # Selezione del nodo che massimizza la quantità specificata
                node_value = t[v.GetId()]/(v.GetOutDeg() * (v.GetOutDeg() + 1))
                if node_value > temp_max:
                    temp_max = node_value
                    node_id = v.GetId()

            # Eliminare il nodo che massimizza la quantità
            node = graph.GetNI(node_id)
            for u in node.GetOutEdges():  # Rimozione del nodo dal grafo
                graph.DelEdge(node_id, u)
            graph.DelNode(node_id)
            print("Caso 3: eliminato nodo " + str(node_id))

    return s



'''
g1 = snap.TUNGraph.New()
g1.AddNode(0)
g1.AddNode(1)
g1.AddNode(2)
g1.AddNode(3)
g1.AddEdge(0, 1)
g1.AddEdge(1, 2)
g1.AddEdge(2, 3)

threshold = snap.TIntH()
for v in g1.Nodes():
    threshold[v.GetId()] = 2
    print("threshold di " + str(v.GetId()) + " pari a " + str(threshold[v.GetId()]))

s = tss(snap.ConvertGraph(type(g1), g1), threshold)

for node_id in s:
    print("Nodo: " + str(node_id))
'''