import numpy as np
import json


# create a class for the nodes
class Node:
    # dict for node names and their entity numbers
    node_dict = {}
    similar_nodes = {}

    def __init__(self, name, entity_number, position, **kwargs):
        self.name = name
        self.id = int(entity_number)
        self.position = position
        self.kwargs = kwargs

        # add to the node dict
        if id not in Node.node_dict.keys():
            Node.node_dict[self.id] = self

        # check if the direction is there
        if 'direction' not in self.kwargs:
            self.kwargs['direction'] = 0

        name_direction = self.name + '-' + str(self.kwargs['direction'])
        if name_direction in Node.similar_nodes:
            Node.similar_nodes[name_direction].append(self.id)
        else:
            Node.similar_nodes[name_direction] = [self.id]

        def __repr__(self):
            return self.name + ' ' + str(self.id)   # + ' ' + str(self.position) + ' ' + str(self.kwargs)
        # if name in Node.node_dict:
        #     Node.node_dict[name].append(entity_number)
        # else:
        #     Node.node_dict[name] = [entity_number]

    # function to check if 2 nodes are connected based on position
    def is_connected(self, other):
        # if positions are 1 removed from each other, they are connected
        if abs(self.position['x'] - other.position['x']) + abs(self.position['y'] - other.position['y']) == 1:
            return True
        else:
            return False

    # function to get the neighbours of a node
    @staticmethod
    def get_neighbours(node):
        neighbours = []
        for edge in Edge.edge_list:
            if edge.node1 == node:
                neighbours.append(edge.node2)
            elif edge.node2 == node:
                neighbours.append(edge.node1)
        return neighbours


# create a class for the edges
class Edge:
    edge_list = []

    def __init__(self, node1, node2, **kwargs):
        self.node1 = node1.id
        self.node2 = node2.id
        self.kwargs = kwargs

        # add the edge to the edge list as long as it is not already in there
        if self not in Edge.edge_list:
            Edge.edge_list.append(self)


# create a class for the graph
class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    # logs a node and its neighbours
    @staticmethod
    def log_node_and_neighbours(node):
        print(node.name)
        print(node.position)
        print(node.kwargs)
        neighbours = Node.get_neighbours(node)
        for neighbour in neighbours:
            print(neighbour.name)
            print(neighbour.position)
            print(neighbour.kwargs)

    @property
    def dimensions(self):
        x_min = min([node.position['x'] for node in self.nodes])
        x_max = max([node.position['x'] for node in self.nodes])
        y_min = min([node.position['y'] for node in self.nodes])
        y_max = max([node.position['y'] for node in self.nodes])
        return x_min, x_max, y_min, y_max


# create a class for the map
class Map(Graph):
    def __init__(self, nodes, edges):
        super().__init__(nodes, edges)

    def get_map_array(self):
        # get the dimensions of the graph
        x_min, x_max, y_min, y_max = self.dimensions

        # create a 2d array of the graph
        graph_array = np.zeros((int(x_max - x_min + 1), int(y_max - y_min + 1)))

        # fill the array with the nodes
        for node in self.nodes:
            x = int(node.position['x'] - x_min)
            y = int(node.position['y'] - y_min)
            graph_array[x, y] = node.id

        return graph_array


# function to convert a blueprint string into a dictionary of entities
def blueprint_string_to_dict(blueprint_string):
    # remove the first character from the string
    blueprint_string = blueprint_string[1:]

    # decode the string from base64
    import base64
    blueprint_string = base64.b64decode(blueprint_string)

    # decompress the string from zlib decompress
    import zlib
    blueprint_json = zlib.decompress(blueprint_string)

    # convert the string into a dictionary
    blueprint_dict = json.loads(blueprint_json)

    return blueprint_dict


# function to convert an entity into nodes and edges
def entity_to_nodes_and_edges(entity):
    # create a node for each entity
    node = Node(**entity)
    edges = []

    # create edges between nodes
    for other in node.node_dict.values():
        if node.is_connected(other):
            edge = Edge(node, other)
            edges.append(edge)


    return node, edges

