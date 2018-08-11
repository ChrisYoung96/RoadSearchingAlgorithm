#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ChrisYoung'


from AStart.A_Star_Algorithm import AStarAlgorithm
import Map_Maker as MapMaker

my_map,width,height = MapMaker.load_map("map1")


star = AStarAlgorithm(0, 0, 6, 3, width, height, my_map)

if star.find_path():
    print(star.map)
    print(star.path)
    print(star.actions)
