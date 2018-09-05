# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 09:56:58 2018

@author: hk
"""
import numpy as np
class Node:
    def __init__(self, coord, component):
        [self.x, self.y] = coord
        self.u = self.w = 0
        self.vx = self.vy = 0
        self.ax = self.ay = 0
        self.last = None
        self.next = None
        self.component = component
        
    def another_node(self, element):
        if self is element.node1:
            return element.node2
        elif self is element.node2:
            return element.node1
        else:
            return None
        
    def get_coord(self):
        return np.array((self.x + self.u, self.y + self.w))
        
            
