#!/usr/bin/env python3
import json, sys

j = None

if len(sys.argv) == 1:
    j = json.loads(sys.stdin.read())
else:
    file_name = sys.argv[1]
    with open(file_name) as f:
        j = json.loads(f.read())

nodes = j["nodes"]
arcs = j["arcs"]

print("digraph D {")
for node in nodes:
    print(
        f'  Node{node["node"]} [label=\"{node["node"]} {", ".join(node["info"])}\"]'
    )

for arc in arcs:
    print(f'  Node{arc["from"]} -> Node{arc["to"]} [label=\"{arc["type"]}\"]')
print("}")
