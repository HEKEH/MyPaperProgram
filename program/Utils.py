# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:47:18 2018

@author: hk
"""
import numpy as np
def coordinate_tranformation(node): #节点,计算用的是np.array
    component = node.component
    angle = component.angle
    reference_point = component.start
    rad = angle / 180 * np.pi
    
    node_ref_coord = node.get_coord()
    
    trans_matrix = np.array([[np.cos(rad), np.sin(rad)],
                             [-np.sin(rad), np.cos(rad)]])
    prime_coord = node_ref_coord.dot(trans_matrix) + np.array(reference_point)
    return prime_coord

def derivation(node):
    coord_this = node.getCoord()
    if node.last:
        coord_last = node.last.getCoord()
        if node.next:
            coord_next = node.next.getCoord()
            #FIXME
            delta_coord = coord_next - coord_last
            return delta_coord[1] / delta_coord[0]
        else:
            coord_last_last = node.last.last.getCoord()
            delta_coord = 3 * coord_this - 4 * coord_last + coord_last_last
            return delta_coord[1] / delta_coord[0]
         
    else:
        coord_next = node.next.getCoord()
        coord_next_next = node.next.next.getCoord()
        delta_coord = 3 * coord_this - 4 * coord_next + coord_next_next
        return delta_coord[1] / delta_coord[0]    
            