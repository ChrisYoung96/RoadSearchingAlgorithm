#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 19:48
# @Author  : ChrisYoung

from BFS.BFSAlgorithm import BFS
import numpy as np

m = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

if __name__ == "__main__":
    bfs = BFS(0, 0, 3, 2, 7, 4, m)
    if bfs.find_path():
        print(bfs.actions)
