"""
Petur Nikolov
IX B class No. 23
"""


def find_maze_exits(maze, starting_position):
    all_paths = []

    def find_exits(maze, current_pos, current_path=''):
        if maze[current_pos['row']][current_pos['column']]:
            if 0 < current_pos['row'] < len(maze) - 1 and \
                    0 < current_pos['column'] < len(maze[0]) - 1:
                maze[current_pos['row']][current_pos['column']] = 0

                up_pos = {'row': current_pos['row'] - 1, 'column': current_pos['column']}
                up_path = current_path + 'U-'
                find_exits(maze, up_pos, up_path)

                right_pos = {'row': current_pos['row'], 'column': current_pos['column'] + 1}
                right_path = current_path + 'R-'
                find_exits(maze, right_pos, right_path)

                down_pos = {'row': current_pos['row'] + 1, 'column': current_pos['column']}
                down_path = current_path + 'D-'
                find_exits(maze, down_pos, down_path)

                left_pos = {'row': current_pos['row'], 'column': current_pos['column'] - 1}
                left_path = current_path + 'L-'
                find_exits(maze, left_pos, left_path)

            else:
                all_paths.append(current_path + 'EXIT')

    def find_shortest_path(maze_paths):
        shortest_path = None

        for path in maze_paths:
            if shortest_path is None or len(path) < len(shortest_path):
                shortest_path = path

        return shortest_path

    maze_copy = [row[:] for row in maze]
    find_exits(maze_copy, starting_position)
    fastest_path = find_shortest_path(all_paths)

    return {
        'maze_paths': all_paths,
        'shortest_path': fastest_path,
    }


def main():
    # A basic example (5x5)
    maze = [
        [0, 1, 0, 1, 0],
        [0, 2, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    start = {'row': 1, 'column': 1}

    # A more complex example (10x7)
    maze = [
        [0, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 0, 0],
        [0, 0, 2, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 1, 0],
    ]
    start = {'row': 3, 'column': 2}

    # The most complex example of these three (20x9)
    maze = [
        [1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 0],
        [1, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 1, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0, 2, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 1, 0],
    ]
    start = {'row': 15, 'column': 6}

    result = find_maze_exits(maze, start)

    print("The labyrinth:")
    print(*maze, sep='\n')

    print("\nThe paths out of this maze are: ")
    if result['maze_paths']:
        print(*result['maze_paths'], sep='\n')
    else:
        print(None)

    print("\nThe shortest way out of this maze is '%s'." % result['shortest_path'])


main()
