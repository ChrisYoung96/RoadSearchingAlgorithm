#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 9:34
# @Author  : ChrisYoung

from Dijkstra.DijkstraAlgorithm import Dijkstra

import Map_Maker as MapMaker

my_map, width, height = MapMaker.load_map("map1")

if __name__ == "__main__":
    D = Dijkstra(0, 0, 6, 3, width, height, my_map)
    if D.find_path():
        print(D.actions)
