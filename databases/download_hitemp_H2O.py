# -*- coding: utf-8 -*-
"""
Download HITEMP H2O database, parse & cache them, to make sure the example notebooks run fast 
"""

from radis.test.utils import setup_test_line_databases
from radis.io.hitemp import fetch_hitemp

setup_test_line_databases()  # init radis.json etc if needed

for (wmin, wmax) in [(k+50, k+1050) for k in range(0, 30000, 1000)]:
    fetch_hitemp("H2O", isotope='1',                   # only 1 HITEMP file so all isotopes are downloaded anyway
                 load_wavenum_min=wmin, 
                 load_wavenum_max=wmax,   
                 verbose=3)