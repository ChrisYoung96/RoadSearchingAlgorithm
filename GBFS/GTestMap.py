#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 14:39
# @Author  : ChrisYoung
from GBFS.GBFSAlgorithm import GBFS
import Map_Maker as MapMaker

my_map, width, height = MapMaker.load_map("map1")

if __name__ == "__main__":
    D = GBFS(0, 0, 6, 3, width, height, my_map)
    if D.find_path():
        print(D.actions)
