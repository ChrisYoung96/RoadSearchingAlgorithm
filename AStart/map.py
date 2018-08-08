from AStart.A_Star_Algorithm import AStarAlgorithm
import numpy as np

map = np.array([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]])

star = AStarAlgorithm(1, 3, 5, 4, 7, 6, map)

star.find_path()

print(star.map)
print(star.path)
print(star.actions)
