"""
    Kleb Dale G. Bayaras
    217095
    ADMU MSCS
    Python 2.7

    BFS + Djikstra
    Djikstra Algo is basically BFS but respecting the weight of the edges;
    thus Djikstra Algo is used for FASTEST PATH ; BFS will be used for SHORTEST PATH
"""
from collections import deque

graph = {}
costs = {}
parents = {}
processed = []


def setup_graph_bfs():
    graph["A"] = ["B", "C", "H"]
    graph["B"] = ["D", "F"]
    graph["C"] = ["E", "G"]
    graph["D"] = []
    graph["E"] = []
    graph["F"] = []
    graph["G"] = []
    graph["H"] = []


def setup_graph_1A():
    graph["A"] = {}
    graph["A"]["B"] = 5
    graph["A"]["C"] = 2

    graph["B"] = {}
    graph["B"]["E"] = 4
    graph["B"]["D"] = 2

    graph["C"] = {}
    graph["C"]["B"] = 8
    graph["C"]["D"] = 7

    graph["D"] = {}
    graph["D"]["F"] = 1

    graph["E"] = {}
    graph["E"]["D"] = 6
    graph["E"]["F"] = 3

    graph["F"] = {}

    costs["A"] = 0
    costs["B"] = float("inf")
    costs["C"] = float("inf")
    costs["D"] = float("inf")
    costs["E"] = float("inf")
    costs["F"] = float("inf")

    parents["A"] = "start"

    return None


def setup_graph_1B():
    graph["A"] = {}
    graph["A"]["B"] = 10

    graph["B"] = {}
    graph["B"]["C"] = 20

    graph["C"] = {}
    graph["C"]["E"] = 30
    graph["C"]["D"] = 1

    graph["D"] = {}
    graph["D"]["B"] = 1

    graph["E"] = {}

    costs["A"] = 0
    costs["B"] = float("inf")
    costs["C"] = float("inf")
    costs["D"] = float("inf")
    costs["E"] = float("inf")

    parents["A"] = "start"

    return None


def bfs_shortest_path(start_node, end_node):
    explored = []
    search_queue = [[start_node]]

    if start_node == end_node:
        return "Same Node"

    while search_queue:
        path = search_queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                search_queue.append(new_path)

                if neighbour == end_node:
                    return new_path
            explored.append(node)


"""
Utility method that goes through costs graph to get the lowest cost node
"""


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    """
    We can use the node as the key which returns the cost from the hash
    """
    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


"""
Get the first lowest cost node.
Take note that the first run of find_lowest_cost_node will result from the root node.
"""


def djikstra_algo():
    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]

        # We can use node as the key to refer to graph to get the neighbors
        neighbors = graph[node]

        # Go through all the neighbors of the node
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]

            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        processed.append(node)

        # Traverse to the next node by determining the next lowest node
        node = find_lowest_cost_node(costs)


def build_fastest_path(end_node):
    fastest_path = [end_node]

    while True:
        x = parents[fastest_path[-1]]

        if x == 'start':
            break
        fastest_path.append(x)

    return fastest_path[::-1]


def is_fastest_also_shortest(list1, list2):
    return True if list1 == list2 else False


def main():
    end_node = raw_input("Please enter desired end node: ")

    # Choose the graph by uncommenting it
    setup_graph_1A()
    # setup_graph_1B()
    djikstra_algo()

    # print("Costs:")
    # for item in costs.items(): print(item)
    # print("Parents:")
    # for item in parents.items(): print(item)

    print("Fastest Path to {}: \n{} with cost of {}".format(end_node, build_fastest_path(end_node), costs[end_node]))
    print("\nShortest Path to {}: \n{}".format(end_node, bfs_shortest_path("A", end_node)))
    print("\nDjikstra and BFS Results same path? {}".format(is_fastest_also_shortest(build_fastest_path(end_node), bfs_shortest_path("A", end_node))))


if __name__ == '__main__':
    main()
