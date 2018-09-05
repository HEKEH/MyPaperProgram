# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 09:56:02 2018

@author: hk
"""
from Node import Node
class Element:
    def __init__(self, coord1, coord2, component, eid, last_element = None):
        if (last_element):
            self.last_element = last_element
            last_element.next_element = self
            self.node1 = last_element.node2
            self.has_last = True
        else:
            self.last_element = None
            self.node1 = Node(coord1, component)
            self.has_last = False
        self.next_element = None
        
        self.node2 = Node(coord2, component)
        self.node1.next = self.node2
        self.node2.last = self.node1
        
        [self.E, self.A, self.component, self.eid] = [component.E, component.A, component, eid]
        
class CableElement(Element):
    def __init__(self, coord1, coord2, cable, eid, last_element = None):
        super(CableElement,self).__init__(coord1, coord2, cable, eid, last_element) 
        
class BeamElement(Element):
    def __init__(self, coord1, coord2, beam, eid, last_element = None):
        super(BeamElement,self).__init__(coord1, coord2, beam, eid, last_element) 
        self.I = beam.I