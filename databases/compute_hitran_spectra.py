# -*- coding: utf-8 -*-
"""
Compute some spectra using 'hitran' to get HITRAN data, cache it, and make 
sure the example notebooks run fast if users keep the same waverange.
"""

from radis import calc_spectrum

# Used in welcome.ipynb
s = calc_spectrum(1900, 2300,         # cm-1
                  molecule='CO',
                  isotope='1,2,3',
                  pressure=1.01325,   # bar
                  Tgas=700,           # K
                  mole_fraction=0.1,
                  path_length=1,      # cm
                  verbose=False,
                  use_cached=True,
                  databank='fetch'  # download HITRAN
                  )

# Used in examples/compare CO-HITRAN.ipynb
s = calc_spectrum(1300, 2600,         # cm-1
                  molecule='CO',
                  isotope='1,2,3',
                  pressure=1.01325,   # bar
                  Tgas=700,           # K
                  mole_fraction=0.1,
                  path_length=1,      # cm
                  verbose=False,
                  use_cached=True,
                  databank='fetch'  # download HITRAN
                  )

# Used in examples/compare_CO2-HITRAN.ipynb
s = calc_spectrum(2000, 2400,         # cm-1
                  molecule='CO2',
                  isotope='1,2,3',
                  pressure=1.01325,   # bar
                  Tgas=700,           # K
                  mole_fraction=0.1,
                  path_length=1,      # cm
                  verbose=False,
                  use_cached=True,
                  databank='hitran'  # download HITRAN
                  )
