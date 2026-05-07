from graph import Graph


def main():
    g1 = Graph()

    g1.connect(7,5, is_directed=True)
    g1.connect(7,6, is_directed=True)
    g1.connect(5,4, is_directed=True)
    g1.connect(6,4, is_directed=True)
    g1.connect(5,2, is_directed=True)
    g1.connect(6,3, is_directed=True)
    g1.connect(2,1, is_directed=True)
    g1.connect(3,1, is_directed=True)
    g1.connect(1,0, is_directed=True)

    #g1.print_graph()

    print(f"Topological Sort: {g1.topological_sort()}")




    g2 = Graph()

    g2.connect('a', 'b', 4)
    g2.connect('a', 'h', 8)

    g2.connect('b', 'c', 8)
    g2.connect('b', 'h', 11)

    g2.connect('c', 'd', 7)
    g2.connect('c', 'f', 4)
    g2.connect('c', 'i', 2)

    g2.connect('d', 'e', 9)
    g2.connect('d', 'f', 14)

    g2.connect('e', 'f', 10)
    
    g2.connect('f', 'g', 2)
    g2.connect('g', 'h', 1)
    g2.connect('g', 'i', 6)
    g2.connect('h', 'i', 7)

    g2.set_start('a')

    #g2.print_graph()

    MST = g2.PrimsMST()
    
    print("Minimum Spanning Tree:")
    MST.print_graph()


if __name__ == "__main__":
    main()