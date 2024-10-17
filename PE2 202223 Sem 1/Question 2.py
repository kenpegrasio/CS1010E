def readmap(filename):
    f = open(filename)
    m = []
    for line in f:
        m.append(list(line.rstrip('\n')))
    return m

def crop_map(filename,minr,maxr,minc,maxc):
    island = readmap(filename)
    nrow, ncol = len(island), len(island[0])
    
    minr, minc = max(0, minr), max(0, minc)
    maxr, maxc = min(nrow, maxr), min(ncol, maxc)
    
    if minr == maxr or minc == maxc:
        return []
    
    ans = []
    for row_idx in range(minr, maxr):
        ans.append("".join(island[row_idx][minc:maxc]))
    return ans
    
def inrange(cur_row, cur_col, maxr, maxc):
    return cur_row >= 0 and cur_row < maxr and cur_col >= 0 and cur_col < maxc

def find_start(island, nrow, ncol, prince):
    for row_idx in range(nrow):
        for col_idx in range(ncol):
            if island[row_idx][col_idx] == prince:
                return (row_idx, col_idx)
    return (-1, -1)

def visit(island, visited, nrow, ncol, start_row, start_col):
    dr = (0, 0, -1, 1)
    dc = (1, -1, 0, 0)
    bfs = [(start_row, start_col)]
    visited.append((start_row, start_col))
    while len(bfs) > 0:
        cur_row = bfs[-1][0]
        cur_col = bfs[-1][1]
        bfs.pop()
        for idx in range(4):
            next_row = cur_row + dr[idx]
            next_col = cur_col + dc[idx]
            if (inrange(next_row, next_col, nrow, ncol)
                and (next_row, next_col) not in visited
                and island[next_row][next_col] == "."):
                visited.append((next_row, next_col))
                bfs.append((next_row, next_col))

def island_area(filename,prince):
    island = readmap(filename)
    nrow = len(island)
    ncol = len(island[0])

    visited = []

    # find start
    start_row, start_col = find_start(island, nrow, ncol, prince)
    if start_row == -1 and start_col == -1:
        return 0

    # visit all connected nodes
    visit(island, visited, nrow, ncol, start_row, start_col)
    
    return len(visited)
            

def prince_map(filename,prince):
    island = readmap(filename)
    nrow = len(island)
    ncol = len(island[0])

    visited = []

    # find start
    start_row, start_col = find_start(island, nrow, ncol, prince)
    if start_row == -1 or start_col == -1:
        return []
    
    # visit all connected nodes
    visit(island, visited, nrow, ncol, start_row, start_col)

    minr, minc, maxr, maxc = nrow, ncol, -1, -1
    for row_idx in range(nrow):
        for col_idx in range(ncol):
            if (row_idx, col_idx) in visited:
                minr = min(minr, row_idx)
                minc = min(minc, col_idx)
                maxr = max(maxr, row_idx)
                maxc = max(maxc, col_idx)
    
    return crop_map(filename, minr, maxr + 1, minc, maxc + 1)