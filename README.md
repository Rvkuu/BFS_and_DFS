#  Traversal Algorithms: BFS & DFS
### Data Structures and Algorithms Seminar Project  
**Presented by:** Branson and Precious  

---

##  Overview

This project explores graph traversal algorithms—**Breadth-First Search (BFS)** and **Depth-First Search (DFS)**—to help understand the internal structure of graphs and trees.  
We use these algorithms to identify **connected components** in a graph, such as **groups of connected islands**.

---

## Topics Covered

###  What is a Graph?
A graph is an Abstract Data Type (ADT) consisting of:
- **Vertices (nodes)**
- **Edges (connections between nodes)**

###  What is a Tree?
A tree is a **connected** and **acyclic** type of graph.

###  What is an Algorithm?
An algorithm is a **step-by-step procedure** used to solve a problem or accomplish a task.

---

##  BFS: Breadth-First Search

**BFS** is a graph traversal method that explores **all nodes at the current depth level before moving to the next level**.  
It uses a **queue (FIFO)** to track which node to visit next.

###  Pseudocode

```text
BFS(graph, start_node):
    queue = [start_node]
    visited = set(start_node)
    component = {start_node}

    while queue is not empty:
        current = queue.dequeue()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
                component.add(neighbor)

    return component


DFS(graph, node, visited, component):
    visited.add(node)
    component.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited, component)


 Discovering Connected Components
We can use either BFS or DFS to find separate groups of connected nodes:

 BFS Implementation
Discover_Regions_BFS(graph):
    visited = set()
    regions = []

    for node in graph:
        if node not in visited:
            region = BFS(graph, node, visited)
            regions.append(region)

    return regions

 DFS Implementation
Discover_Regions_DFS(graph):
    visited = set()
    regions = []

    for node in graph:
        if node not in visited:
            component = set()
            DFS(graph, node, visited, component)
            regions.append(component)

    return regions
Sample Input & Output
Input (edges):
python
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('C', 'E'), ('F', 'G')]

Output (connected components):
python
[{'A', 'B', 'C', 'D', 'E'}, {'F', 'G'}]


| BFS Applications                      | DFS Applications                          |
| ------------------------------------- | ----------------------------------------- |
| Shortest path in unweighted graphs    | Pathfinding / Maze solving                |
| Web crawlers                          | Cycle detection                           |
| Friend recommendations (social graph) | Topological sorting                       |
| Level-order traversal (trees)         | Finding strongly connected components     |
| Network broadcasting                  | Bridges and articulation points detection |


