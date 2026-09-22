def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    if len(packages) == 0:
        return []
    
    # Step 1: Build in-degree map and adjacency list
    # Only include packages that are keys in `packages`
    # Dependencies not in packages are ignored
    in_degree = {}
    adj = {}
    
    for pkg in packages:
        in_degree[pkg] = 0
        adj[pkg] = []
    
    for pkg in packages:
        for dep in packages[pkg]:
            if dep in packages:          # ignore unknown packages
                adj[dep].append(pkg)     # dep must come before pkg
                in_degree[pkg] += 1
    
    # Step 2: Collect all packages with in-degree 0 (no dependencies)
    # Use a list as a queue (index-based to avoid pop(0) cost)
    queue = []
    for pkg in packages:
        if in_degree[pkg] == 0:
            queue.append(pkg)
    
    # Step 3: Process the queue
    result = []
    head = 0
    while head < len(queue):
        pkg = queue[head]
        head += 1
        result.append(pkg)
        
        for dependent in adj[pkg]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    # Step 4: If not all packages were processed, there's a cycle
    if len(result) != len(packages):
        return []
    
    return result