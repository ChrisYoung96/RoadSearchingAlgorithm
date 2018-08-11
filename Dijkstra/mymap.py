#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 9:34
# @Author  : ChrisYoung

from Dijkstra.DijkstraAlgorithm import Dijkstra
import numpy as np

m = np.array([
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0]
])

if __name__ == "__main__":
    D = Dijkstra(0, 0, 6, 3, 7, 4, m)
    if D.find_path():
        print(D.actions)
