# Importing the necessary libraries
from pprint import pprint
from blueprintMap import *
from slpp import slpp as lua
import calculator

# load the blueprint string from the file
with open('blueprint.txt', 'r') as file:
    blueprint_string = file.read()

# convert the blueprint string into a dictionary
blueprint_dict = blueprint_string_to_dict(blueprint_string)

# create a list of entities
bp_entities = blueprint_dict['blueprint']['entities']

# create a list of nodes and edges from the entities
for entity in bp_entities:
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

data = lua.decode(open('data-final-fixes.lua').read())

import_category = [
    "accumulator",
    "ammo-turret",
    "assembling-machine",
    "beacon",
    "boiler",
    "curved-rail",
    "decider-combinator",
    "electric-energy-interface",
    "electric-pole",
    "electric-turret",
    "fluid-turret",
    "furnace",
    "gate",
    "generator",
    "heat-interface",
    "heat-pipe",
    "inserter",
    "lab",
    "lamp",
    "land-mine",
    "linked-belt",
    "loader",
    "logistic-container",
    "mining-drill",
    "offshore-pump",
    "pipe",
    "pipe-to-ground",
    "power-switch",
    "programmable-speaker",
    "pump",
    "radar",
    "rail-chain-signal",
    "rail-signal",
    "reactor",
    "roboport",
    "rocket-silo",
    "solar-panel",
    "splitter",
    "storage-tank",
    "straight-rail",
    "train-stop",
    "transport-belt",
    "underground-belt",
    "wall"
]

placeables = {}


for category in import_category:
    # pprint(data[category])
    for key, value in data[category].items():
        placeables[key] = value

pprint(data)



