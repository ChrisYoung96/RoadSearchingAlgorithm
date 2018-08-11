#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 14:00
# @Author  : ChrisYoung
from GBFS.GNode import Node
import numpy as np


class GBFS:
    def __init__(self, s_x, s_y, e_x, e_y, width=10, height=10, map=np.zeros((10, 10))):
        self.s_x = s_x
        self.s_y = s_y
        self.e_x = e_x
        self.e_y = e_y
        self.width = width
        self.height = height
        self.map = map

        self.open = []
        self.visited = []
        self.path = []  # 路径序列
        self.actions = []  # 动作序列

    def __is_valid_coordinate(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return self.map[y, x] == 0

    def __is_the_end(self, node):
        return self.e_x == node.x and self.e_y == node.y

    def __is_visited(self, node):
        if not self.visited:
            for item in self.visited:
                return item.is_same_node(node)
        return False

    def __is_in_open(self, node):
        if not self.open:
            for index, item in self.open:
                if item.is_same_node(node):
                    return index
        return -1

    def __get_min_node(self):
        min_node = None
        min_dis = 10000
        min_index = -1
        if self.open:
            for index, item in enumerate(self.open):
                if item.distance <= min_dis:
                    min_dis = item.distance
                    min_node = item
                    min_index = index
        return min_index, min_node

    def __make_path(self, node):
        temp = []
        while node:
            temp.append((node.x, node.y))
            node = node.parent
        for i in range(len(temp) - 1, -1, -1):
            self.path.append(temp[i])

    def __make_action_sequence(self):

        if len(self.path) > 1:
            for i in range(len(self.path) - 1):
                x1 = self.path[i][0]
                y1 = self.path[i][1]
                x2 = self.path[i + 1][0]
                y2 = self.path[i + 1][1]
                if x2 - x1 > 0:
                    self.actions.append('right')
                elif x2 - x1 < 0:
                    self.actions.append('left')
                elif y2 - y1 > 0:
                    self.actions.append('down')
                elif y2 - y1 < 0:
                    self.actions.append('up')

    def __heuristic(self, x, y):
        return abs(self.e_x - x) + abs(self.e_y - y)

    def __extend_around(self, cur_node):
        xs = (0, 0, -1, 1)
        ys = (-1, 1, 0, 0)
        for x, y in zip(xs, ys):
            new_x = x + cur_node.x
            new_y = y + cur_node.y
            if not self.__is_valid_coordinate(new_x, new_y):
                continue
            new_distance = cur_node.distance + self.__heuristic(new_x, new_y)
            new_node = Node(new_x, new_y, cur_node, new_distance)
            if self.__is_visited(new_node):
                continue
            idx = self.__is_in_open(new_node)
            if idx != -1:
                continue
            self.open.append(new_node)

    def find_path(self):
        if not self.__is_valid_coordinate(self.s_x, self.s_y):
            return False
        if not self.__is_valid_coordinate(self.e_x, self.e_y):
            return False
        node = Node(self.s_x, self.s_y, None, 0)
        self.visited.append(node)
        while True:
            self.__extend_around(node)
            if not self.open:
                return False
            index, node = self.__get_min_node()
            if self.__is_the_end(node):
                self.__make_path(node)
                self.__make_action_sequence()
                return True
            self.visited.append(node)
            del self.open[index]
