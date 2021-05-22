import networkx as nx
import regex as re

f = open("inputs/day7.txt", "r").read().split("\n")

# initialise graph
G = nx.DiGraph()
for rule in f:
    outer, inner = rule.split('contain')
    outer = outer[:-5].strip()
    G.add_node(outer)
    if "no other" not in rule:
        for i in inner.strip().split(","):
            inners = re.findall("(\d)(.*)bag[s]?", i)
            for inner_bag in inners:
                G.add_edge(outer, inner_bag[1].strip(), weight=int(inner_bag[0]))

# Part 1
T = nx.algorithms.traversal.bfs_tree(G, "shiny gold", reverse=True)
print(T.number_of_nodes() - 1)


# Part 2
def get_number_of_bags(node):
    ans = 0
    if len(list(G.neighbors(node))) == 0:
        return 1
    for neighbor in G.neighbors(node):
        ans += G.get_edge_data(node, neighbor)['weight'] * (get_number_of_bags(neighbor) + 1)
    return ans


def overcounted_bags(node):
    ans = 0
    if len(list(G.neighbors(node))) == 0:
        return 1
    for neighbor in G.neighbors(node):
        ans += G.get_edge_data(node, neighbor)['weight'] * (overcounted_bags(neighbor))
    return ans


# solving recurrence relation using two recurrences
print(get_number_of_bags("shiny gold") - overcounted_bags("shiny gold"))
