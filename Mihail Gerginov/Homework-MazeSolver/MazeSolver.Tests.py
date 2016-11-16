import MazeSolver as m
import unittest
import collections

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

class TestsForAtLeastOnePath(unittest.TestCase):
    def create_normal_maze_assert_if_paths_are_the_same(self):
        maze = []
        maze.append([' ', ' ', ' ', '*', ' ', ' ', ' '])
        maze.append(['*', '*', ' ', '*', ' ', '*', ' '])
        maze.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
        maze.append([' ', '*', '*', '*', '*', '*', ' '])
        maze.append([' ', ' ', ' ', ' ', ' ', ' ', 'e'])
        m.find_at_least_one_path(maze)
        self.assertTrue(compare(m.paths_found, ['RRDDLLDDRRRRRR', 'RRDDRRUURRDDDD']), "The two paths don't match.")


if __name__ == '__main__':
    unittest.main()