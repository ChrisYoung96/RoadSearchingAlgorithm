#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ChrisYoung'

from AStart.NodeItem import Node
import numpy as np


# A星路径搜索算法
# 初始化参数：
# s_x,s_y:起点坐标
# e_x,e_y:终点坐标
# width,height:地图的宽和高
# map:地图数据，数据类型为np.array的二维整型数组，暂定0为可走的路，其他数字不可走
class AStarAlgorithm:
    def __init__(self, s_x, s_y, e_x, e_y, width=10, height=10, map=np.zeros((10, 10))):
        self.__s_x = s_x
        self.__s_y = s_y
        self.__e_x = e_x
        self.__e_y = e_y
        self.__width = width
        self.__height = height
        self.__map = map

        self.__open = []
        self.__close = []
        self.path = []  # 路径序列
        self.actions = []  # 动作序列

    # 验证坐标是否合法以及是否可走
    def __is_valid_coordinate(self, x, y):
        if x < 0 or x >= self.__width or y < 0 or y >= self.__height:
            return False
        return self.__map[y, x] == 0

    # 获得当前坐标距离起点的距离G
    def __get_g(self, x1, y1, x2, y2):
        if x1 == x2 or y1 == y2:
            return 1

    # 判断结点是否在close列表中
    def __node_in_close(self, node):
        for item in self.__close:
            if node.x == item.x and node.y == item.y:
                return True
            return False

    # 判断结点是否在open列表中，如果在，返回结点索引
    def __node_in_open(self, node):
        for index, item in enumerate(self.__open):
            if node.x == item.x and node.y == item.y:
                return index
        return -1

    # 探索当前结点四周的结点并将未走过的结点添加到open列表中
    def __extend_round(self, cur_node):
        # 四个方向向量，上下左右
        xs = (0, 0, -1, 1)
        ys = (-1, 1, 0, 0)
        for x, y in zip(xs, ys):
            new_x = x + cur_node.x
            new_y = y + cur_node.y

            if not self.__is_valid_coordinate(new_x, new_y):  # 对当前结点四周的结点，判断是否合法，不合法则舍弃
                continue
            new_G = cur_node.G + self.__get_g(cur_node.x, cur_node.y, new_x, new_y)  # 计算四周结点到起点的距离
            new_node = Node(cur_node, new_x, new_y, new_G)  # 创建结点
            if self.__node_in_close(new_node):  # 如果该结点已经在close列表中，舍弃
                continue
            index = self.__node_in_open(new_node)  # 否则判断该节点是否在open列表中
            if index != -1:  # 如果在
                if self.__open[index].G > new_node.G:  # 若因当前结点导致该节点到起点的距离更短
                    self.__open[index].parent = cur_node  # 更新该节点的父结点
                    self.__open[index].G = new_node.G  # 更新距离
                continue
            self.__open.append(new_node)  # 若未探索且可走，加入open列表

    # 判断是否到终点
    def __is_end(self, node):
        return node.x == self.__e_x and node.y == self.__e_y

    # 采用“曼哈顿距离方法”计算H估计值，并计算F
    def __get_f(self, node):
        return node.G + abs(self.__e_x - node.x) + abs(self.__e_y - node.y)

    # 从当前结点的四周可走结点中选取最优的结点，作为下一步的方向
    def __get_min_node(self):
        min_f_node = None
        min_f = 100000
        min_index = -1
        for index, item in enumerate(self.__open):
            f = self.__get_f(item)
            if f <= min_f:
                min_f_node = item
                min_f = f
                min_index = index
        return min_index, min_f_node

    # 回溯法生成路径
    def __make_path(self, node):
        temp = []
        while node:
            temp.append((node.x, node.y))
            node = node.parent
        for i in range(len(temp) - 1, -1, -1):
            self.path.append(temp[i])

    # 根据路径生成动作序列
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

    # 计算路径并生成动作序列
    def find_path(self):
        if not self.__is_valid_coordinate(self.__s_x, self.__s_y):
            return False
        if not self.__is_valid_coordinate(self.__e_x, self.__e_y):
            return False
        node = Node(None, self.__s_x, self.__s_y, 0)
        while True:
            self.__extend_round(node)
            if not self.__open:
                return False
            index, node = self.__get_min_node()
            if self.__is_end(node):
                self.__make_path(node)
                self.__make_action_sequence()
                return True
            self.__close.append(node)
            del self.__open[index]
