#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 14:13
# @Author  : ChrisYoung

class Node:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent

    def is_same_node(self,node):
        return node.x==self.x and node.y==self.y
