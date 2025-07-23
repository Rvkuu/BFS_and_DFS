from collections import deque, defaultdict

# Define the bridges (edges) within each region
bridges = {
    "Region 1": [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('F', 'G'), ('H', 'I'), ('I', 'J')]
}

# Build a full graph (adjacency list) from all bridge (edge) definitions
def build_graph(bridges_by_region):
    graph = defaultdict(list)
    for region_edges in bridges_by_region.values():
        for u, v in region_edges:
            graph[u].append(v)
            graph[v].append(u)
    return graph

# Function to perform BFS on a graph starting from a given node
def bfs(graph, start, visited):
    print(f"Starting BFS from node: {start}")

    queue = deque([start])
    component = []

    while queue:
        print(f"Queue: {list(queue)}")
        node = queue.popleft()
        print(f"Visiting node: {node}")
        print(f"Dequeued node: {node}")

        if node not in visited:
            visited.add(node)
            component.append(node)
            print(f"Visited nodes: {component}")
            print(f"Current component: {component}")

            for neighbor in graph[node]:
                print(f"Checking neighbor: {neighbor}")
                if neighbor not in visited:
                    queue.append(neighbor)
                    print(f"Queued neighbor: {neighbor}")
                else:
                    print(f"Neighbor {neighbor} already visited")
        else:
            print(f"Node {node} already visited")

    print(f"Finished BFS for component: {component}")
    return component

#Discover all connected regions (island clusters) using BFS
def discover_regions(graph):
    visited = set()
    regions_discovered = []

    # Iterate through all nodes in the graph even if they are not connected
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)

    for node in sorted(all_nodes): #Optional: sort nodes for consistent output
        if node not in visited:
            print(f"New region discovery starting from: {node}")
            region = bfs(graph, node, visited)
            regions_discovered.append(region)

    return regions_discovered

# Run the discovery and print results
graph = build_graph(bridges)
discovered_regions = discover_regions(graph)

print("\n Discovered Regions:")
for i, region in enumerate(discovered_regions, start=1):
    print(f"Region {i}: {region}")
