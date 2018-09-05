# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:21:44 2018

@author: hk
"""

from Component import Component
from Element import BeamElement
class Beam(Component):
    def __init__(self, start, angle, E, A, I, m, length, elements_num):
        super(Beam, self).__init__(start, angle, E, A, m, length, elements_num)
        self.I = I
        self.init_elements(BeamElement)
        self.init_nodes()
            
            
            
    def display(self):
        pass