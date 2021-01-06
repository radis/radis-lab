# -*- coding: utf-8 -*-
""" Load all all pre-configured databases in ~/.radis to generate cache files """

from radis.misc.utils import get_files_from_regex
from radis.misc.config import getDatabankList, getDatabankEntries

from radis import SpectrumFactory

sf = SpectrumFactory(wavenum_min=50,
                     wavenum_max=10000,
                     isotope='1,2,3')

for dbname in getDatabankList():
    print("Caching", dbname)

    db0 = getDatabankEntries(dbname)

    # Read only one path at a time to generate the cache file. 
    # (prevents Memory errors)
    for path in db0['path']:
        path = get_files_from_regex(path)
        print('...', path)
        db = {k:db0[k] for k in db0.keys() if k not in ['info', 'levelszpe']}
        db['path'] = path
        
        sf.input.molecule=""
        sf.load_databank(**db)
