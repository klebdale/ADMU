"""
    Kleb Dale G. Bayaras
    217095
    ADMU MSCS
    Python 2.7
    Modifications from Sir Alampay's Djikstra Algo code to show path and cost of fastest path
"""
graph = {}
costs = {}
parents = {}
processed = []


def setup_graph_1A(start_node):
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

    for key in graph.keys():
        costs[key] = float("inf")
        if key == start_node:
            costs[start_node] = 0

    parents[start_node] = "start"

    return None


def setup_graph_1B(start_node):
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

    for key in graph.keys():
        costs[key] = float("inf")
        if key == start_node:
            costs[start_node] = 0

    parents[start_node] = "start"

    return None


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

    try:
        while True:
            x = parents[fastest_path[-1]]

            if x == 'start':
                break
            fastest_path.append(x)

        return fastest_path[::-1]

    except KeyError:
        print("\nThere is no path that connects them")



def main():
    start_node, end_node = raw_input("Please enter desired start and end node (separate with space): ").split()

    # Choose the graph by uncommenting it
    setup_graph_1A(start_node)
    #setup_graph_1B(start_node)
    djikstra_algo()

    print("Costs:")
    for item in costs.items(): print(item)
    print("Parents:")
    for item in parents.items(): print(item)

    print("Fastest Path from {} to {}: \n{} with cost of {}".format(start_node, end_node, build_fastest_path(end_node), costs[end_node]))


if __name__ == '__main__':
    main()
