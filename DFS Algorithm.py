from collections import defaultdict

# Define the bridges (edges) within each region
bridges = {
    "Region 1": [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('F', 'G'), ('H', 'I'), ('I', 'J')]
}

# Build adjacency list graph from the bridge connections
def build_graph(bridges_by_region):
    graph = defaultdict(list)
    for region_edges in bridges_by_region.values():
        for u, v in region_edges:
            graph[u].append(v)
            graph[v].append(u)
    return graph

# DFS traversal function
def dfs(graph, node, visited, component):
    print(f"Visiting node: {node}")
    visited.add(node)
    component.append(node)

    for neighbor in graph[node]:
        print(f"Checking neighbor: {neighbor}")
        if neighbor not in visited:
            print(f"Going deeper into: {neighbor}")
            dfs(graph, neighbor, visited, component)
        else:
            print(f"Already visited: {neighbor}")

# Discover all connected regions (island clusters) using DFS
def discover_regions_dfs(graph):
    visited = set()
    regions_discovered = []

    # Ensure all nodes are included (even if isolated)
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)

    for node in sorted(all_nodes):  # Optional sort for consistent output
        if node not in visited:
            print(f"\nStarting new region discovery from: {node}")
            component = []
            dfs(graph, node, visited, component)
            regions_discovered.append(component)

    return regions_discovered

# Run the discovery process
graph = build_graph(bridges)
discovered_regions = discover_regions_dfs(graph)

# Output results
print("\nDiscovered Regions using DFS:")
for i, region in enumerate(discovered_regions, start=1):
    print(f"  Region {i}: {sorted(region)}")
