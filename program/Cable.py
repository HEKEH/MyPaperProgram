# -*- coding: utf-8 -*-

from Component import Component
from Element import CableElement
class Cable(Component):
    def __init__(self, start, angle, E, A, m, length, elements_num):
        super(Cable, self).__init__(start, angle, E, A, m, length, elements_num)
        self.init_elements(CableElement)
        self.init_nodes()
            
            
            
    def display(self):
        pass



        


