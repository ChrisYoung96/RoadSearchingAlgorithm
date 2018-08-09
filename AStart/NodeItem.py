#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ChrisYoung'


class Node:
    def __init__(self, parent, x, y, G=0):
        self.parent = parent
        self.x = x
        self.y = y
        self.G = G
