# Importing the necessary libraries
from pprint import pprint
from blueprintMap import *
import calculator

# load the blueprint string from the file
with open('blueprint.txt', 'r') as file:
    blueprint_string = file.read()

# convert the blueprint string into a dictionary
blueprint_dict = blueprint_string_to_dict(blueprint_string)

# create a list of entities
entities = blueprint_dict['blueprint']['entities']

# create a list of nodes and edges from the entities
for entity in entities:
    entity_to_nodes_and_edges(entity)

nodes = Node.node_dict.values()
edges = Edge.edge_list

# create a map from the graph
map = Map(nodes, edges)
map_array = map.get_map_array()

# pprint(entities)
#
# pprint(map.get_map_array())
#
# pprint(Node.similar_nodes)
