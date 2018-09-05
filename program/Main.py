# -*- coding: utf-8 -*-
from Cable import Cable
from Beam import Beam
global t
t = 0
dt = 0.1
cable_start = [0, 0]
cable_angle = 30
cable_length = 100
cable_E = 2.1 * 10 ** 11
cable_A = 0.5
cable_density = 7.85 * 10 ** 3
cable_m = cable_A * cable_density
cable_section_num = 100

cable = Cable(cable_start, cable_angle, cable_E, cable_A, cable_m, cable_length, cable_section_num)
#beam = Beam(cable_E, cable_A, 1000, cable_m, cable_length, cable_section_num)
#print(cable.elements[0].node2,cable.elements[1].node1)