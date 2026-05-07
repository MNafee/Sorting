from edge import Edge
from queue import Queue


class Node:
    def __init__(self, value, edges=None):
        self.value = value
        self.edges = edges if edges is not None else []
        self.indegree = 0
    def connect(self, node, weight = 1, is_directed = False):
        edge = Edge(self, node, weight, is_directed)
        self.edges.append(edge)



class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.is_directed = False
        self.start = None

    def add_node(self, node):
        self.nodes.append(node)

    def get_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None
    
    def set_start(self, value):
        self.start = self.get_node(value)

    def connect(self, value1, value2, weight = 1, is_directed = False):
        n1 = self.get_node(value1)
        n2 = self.get_node(value2)
        node1 =  n1 if n1 else Node(value1)
        node2 = n2 if n2 else Node(value2)
        if n1 is None:
            self.add_node(node1)
        if n2 is None:
            self.add_node(node2)
        
        node1.connect(node2, weight, is_directed)
        edge = Edge(node1, node2, weight, is_directed)
        self.edges.append(edge)
        if not is_directed:
            node2.connect(node1, weight, is_directed)
        else:
            node2.indegree += 1

        self.is_directed = is_directed


    def print_graph(self):
        for node in self.nodes:
            print(f"{node.value}: {[edge.destination.value for edge in node.edges]}")



    def create_graph_from_edges(self, edges):
        values = set()

        for edge in edges:
            if edge.source.value not in values:
                self.add_node(Node(edge.source.value))
                values.add(edge.source.value)
            if edge.destination.value not in values:
                self.add_node(Node(edge.destination.value))
                values.add(edge.destination.value)
            self.get_node(edge.source.value).connect(self.get_node(edge.destination.value), edge.weight, edge.is_directed)
                
            if not edge.is_directed:
                self.get_node(edge.destination.value).connect(self.get_node(edge.source.value), edge.weight, edge.is_directed)
            else:
                self.get_node(edge.destination.value).indegree += 1
        self.is_directed = edges[0].is_directed if edges else False
        self.edges = edges

    def topological_sort(self):
        if not self.is_directed:
            raise Exception("Topological sort is only applicable to directed graphs.")
        queue = Queue()
        sorted_nodes = []
        for node in self.nodes:
            if node.indegree == 0:
                queue.put(node)
        while not queue.empty():
            node = queue.get()
            sorted_nodes.append(node.value)
            for edge in node.edges:
                edge.destination.indegree -= 1
                if edge.destination.indegree == 0:
                    queue.put(edge.destination)
        return sorted_nodes
    

    def PrimsMST(self):
        if self.is_directed:
            raise Exception("Prim's MST is only applicable to undirected graphs.")
        if self.start == None:
            raise Exception("Start node is not set.")
        mst = Graph()
        node_list = [self.start]
        edge_list = []
        added_edges = []
        while True:
            for node in node_list:
                for edge in node.edges:
                    if edge.destination not in node_list and edge not in added_edges:
                        edge_list.append(edge)
            if not edge_list:
                break;
            edge_list.sort(key=lambda edge: edge.weight)
            edge = edge_list.pop(0)
            added_edges.append(edge)
            node_list.append(edge.destination)
            edge_list.clear()

        mst.create_graph_from_edges(added_edges)
        return mst
    

