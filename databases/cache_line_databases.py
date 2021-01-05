# -*- coding: utf-8 -*-
""" Load all all pre-configured databases in ~/.radis to generate cache files """

from radis import SpectrumFactory
from radis.misc.config import getDatabankList

sf = SpectrumFactory(wavenum_min = 100, 
                     wavenum_max = 20000,
                    isotope='1,2,3')
for db in getDatabankList():
    sf.input.molecule = None
    sf.load_databank(db)
# Note: for CO2 we're loading the whole database. May need > 2 GB RAM. 