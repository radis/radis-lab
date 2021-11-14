# -*- coding: utf-8 -*-
"""
Download some molecules from HITRAN data, parse & cache them, to make 
sure the example notebooks run fast.
"""

from radis.io.hitran import fetch_hitran

for molecule, parse_quanta in [('C2H2', False),
                               ('C2H4', False),
                               ('C2H6', False),
                               ('CH4', False),
                               ('CO', True),
                               ('CO2', True),
                               ('H2O', False),
                               ('N2O', False),
                               ('NH3', False),
                               ('NO', False),
                               ('NO2', False)]:
    fetch_hitran(molecule, parse_quanta=parse_quanta)
