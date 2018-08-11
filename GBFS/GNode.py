#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 14:00
# @Author  : ChrisYoung

class Node:
    def __init__(self, x, y, parent, dis):
        self.x = x
        self.y = y
        self.parent = parent
        self.distance = dis

    def is_same_node(self, node):
        return node.x == self.x and node.y == self.y

    def __lt__(self, other):
        return self.distance < other.distance
