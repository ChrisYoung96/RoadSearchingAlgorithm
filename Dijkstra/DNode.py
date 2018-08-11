#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 9:31
# @Author  : ChrisYoung

class Node:
    def __init__(self, x, y, parent,cost):
        self.x = x
        self.y = y
        self.parent = parent
        self.cost=cost

    def is_same_node(self,node):
        return node.x==self.x and node.y==self.y

