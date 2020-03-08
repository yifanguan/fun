'''
Eight Queen Solver
This implementation is purely using backtracking without any herusitic.
Find one solution, print it out, and then stop.
It is easy to adopt to find all solutions.
Non-efficient implementation for easy-understanding.
'''

def backtrack_search(grids, size, neighbors):
    ''' main backtrack search '''
    backtrack(grids, size, 0, neighbors)

def backtrack(grids, size, num, neighbors):
    ''' backtrack to explore solution search states '''
    if num == size: # solution; assignment is complete
        print('Solution found')
        return True
    nexts = select_next_grid(grids, neighbors, size, num)
    for next in nexts:
        grids[next] = 1 # mark a queen occupy this grid
        num += 1
        # print_solution(grids, size)
        found = backtrack(grids, size, num, neighbors)
        if found:
            return found
        # failure
        grids[next] = 0
        num -= 1
    return False

def select_next_grid(grids, neighbors, size, num):
    ''' generate possible positions for next queen on row num '''
    nexts = set(range(size * num, size * (num + 1)))
    for grid in grids:
        if grids[grid] == 1:
            nexts = nexts.difference(neighbors[grid])
    return nexts

def print_solution(grids, size):
    ''' visualize n-queen solution '''
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']
    row = [' '] + alpha[:size]
    row_str = ''.join(row)
    print(row_str)
    for i in range(size):
        row_str = str(i + 1)
        for j in range(size):
            if grids[i * size + j] == 0: # 0 indicate empty
                row_str += '-' # empty
            else: # 1 indicate a queen is placed at this grid
                assert grids[i * size + j] == 1
                row_str += '*' # queen
        print(row_str)

def main():
    ''' main function'''
    size = 8
    # index starting from index 0 to size ** 2 - 1;
    # the top row is the first row
    grids = {} # define each grid as a variable
    for i in range(size):
        for j in range(size):
            grids[i * size + j] = 0 # 0 indicate empty

    # generate neighbors (index) for each grid
    neighbors = {}
    for i in range(size):
        for j in range(size):
            neighbors_for_this_grid = set()
            # same row
            for z in range(size):
                neighbors_for_this_grid.add(i * size + z)
            # same column
            for z in range(size):
                neighbors_for_this_grid.add(z * size + j)
            # same diagonals
            step_go_up_left = min(i, j)
            step_go_up_right = min(i, size - 1 - j)
            step_go_down_left = min(size - 1 - i, j)
            step_go_down_right = min(size - 1 - i, size - 1 - j)

            for z in range(1, step_go_up_left + 1):
                neighbors_for_this_grid.add((i - z) * size + (j - z))

            for z in range(1, step_go_up_right + 1):
                neighbors_for_this_grid.add((i - z) * size + (j + z))

            for z in range(1, step_go_down_left + 1):
                neighbors_for_this_grid.add((i + z) * size + (j - z))

            for z in range(1, step_go_down_right + 1):
                neighbors_for_this_grid.add((i + z) * size + (j + z))

            neighbors[i * size + j] = neighbors_for_this_grid
    backtrack_search(grids, size, neighbors)
    print_solution(grids, size)


if __name__ == '__main__':
    main()
