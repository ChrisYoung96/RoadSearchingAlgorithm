#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 14:47
# @Author  : ChrisYoung
import numpy as np
import queue
from BFS.BNode import Node

INFINIY = 1000000


class BFS:
    def __init__(self, s_x, s_y, e_x, e_y, width=10, height=10, map=np.zeros((10, 10))):
        self.s_x = s_x
        self.s_y = s_y
        self.e_x = e_x
        self.e_y = e_y
        self.width = width
        self.height = height
        self.map = map

        self.visited = []
        self.path = []  # 路径序列
        self.actions = []  # 动作序列

    def __is_valid_coordinate(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return self.map[y, x] == 0

    def __is_visited(self, node):
        if not self.visited:
            for item in self.visited:
                return item.is_same_node(node)
        return False

    def __is_the_end(self, node):
        return self.e_x == node.x and self.e_y == node.y

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

    def find_path(self):
        if not self.__is_valid_coordinate(self.s_x, self.s_y):
            return False
        if not self.__is_valid_coordinate(self.e_x, self.e_y):
            return False
        cur_node = Node(self.s_x, self.s_y, None)
        q = queue.Queue()
        xs = (0, 0, -1, 1)
        ys = (-1, 1, 0, 0)
        q.put(cur_node)
        while not q.empty():
            cur_node = q.get()
            self.visited.append(cur_node)
            if self.__is_the_end(cur_node):
                self.__make_path(cur_node)
                self.__make_action_sequence()
                return True
            for x, y in zip(xs, ys):
                new_x = cur_node.x + x
                new_y = cur_node.y + y
                if not self.__is_valid_coordinate(new_x, new_y):
                    continue
                new_node = Node(new_x, new_y, cur_node)
                q.put(new_node)
        return False
