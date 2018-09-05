# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 12:51:46 2018

@author: hk
"""

class Component:
    def __init__(self, start, angle, E, A, m, length, elements_num):
        self.start = start
        self.angle = angle
        self.E = E
        self.A = A
        self.m = m
        self.length = length
        self.elements_num = elements_num
        self.elements = []
        self.nodes = []
    
    def init_elements(self, ElementClass):#ElementClass是CableElement或者BeamElement
        element_len = self.length / self.elements_num
        last_element = None
        for i in range(self.elements_num):
            coord1 = [element_len * i, 0]
            coord2 = [element_len * (i + 1), 0]
            new_element = ElementClass(coord1, coord2, self, i, last_element)
            self.elements.append(new_element)
            last_element = new_element;
            
    def init_nodes(self):
        for e in self.elements:
            if not e.has_last:
                self.nodes.append(e.node1)
            self.nodes.append(e.node2)
