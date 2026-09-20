













a = ['.*.', '***', '.*.']



p = [(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)]



_ = "    .*.    "
_ = "    ***    "
_ = "    .*.    "


# for i in a:
#     print(i)
    
    

def constellation_mapper1(stars: list[tuple[int, int]], dim: int) -> list[str]:
    
    seen = []
    for i in stars:
        if i in seen:
            stars.remove(i)
        else:
            seen.append(i)
    
    
    
    return 1


def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    # Build a grid of empty spaces
    grid = [['.' for _ in range(dim)] for _ in range(dim)]
    print(grid)
    for row, col in stars:
        if 0 <= row < dim and 0 <= col < dim:
            grid[row][col] = "*"
    
    return [''.join(row) for row in grid]


print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2), (1, 2)], 3))

def constellation_mapper11(stars: list[tuple[int, int]], dim: int) -> list[str]:
    grid = [['.' * dim] ]
    return grid
print(constellation_mapper11([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2), (1, 2)], 3))

def constellation_mapper12(stars: list[tuple[int, int]], dim: int) -> list[str]:
    star_set = {(r,c) for r,c in stars if 0 <= r < dim and 0 <= c < dim}
    return [''.join('*' if (r,c) in star_set else '.' for c in range(dim)) for r in range(dim)]


print(constellation_mapper12([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2), (1, 2)], 3))