#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 19:48
# @Author  : ChrisYoung

from BFS.BFSAlgorithm import BFS
import Map_Maker as MapMaker

my_map, width, height = MapMaker.load_map("map1")

if __name__ == "__main__":
    bfs = BFS(0, 0, 6, 3, width, height, my_map)
    if bfs.find_path():
        print(bfs.actions)
