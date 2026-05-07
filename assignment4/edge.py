class Edge:
    def __init__(self, source, destination, weight = 1, is_directed = False): # weighted
        self.source = source
        self.destination = destination
        self.weight = weight
        self.is_directed = is_directed
