# -*- coding: utf-8 -*-
""" Init and add pre-configured databases to RADIS ~/.radis config file in HOME """

from radis.misc.config import (
    addDatabankEntries,
    diffDatabankEntries,
    getDatabankEntries,
    getDatabankList,
)

# Make sure the names correspond to the databases unzipped in postBuild.
RADIS_LAB_DATABASES = {
    "HITEMP2019-CO":
    {
        "info": "HITEMP2019 CO lines with TIPS-2017 for partition functions (equilibrium) and RADIS for rovibrational energies (nonequilibrium) ",
        "path": ["/home/jovyan/databases/HITEMP/05_HITEMP2019_all.par"],
        "format": "hitran",
        "parfuncfmt": "hapi",
        "levelsfmt": "radis",
    },
}

# Add them :
# ... code from :py:func:`~radis.test.utils.setup_test_line_databases`
for dbname, dbentries in RADIS_LAB_DATABASES.items():

    # Get list of databases
    try:
        dbnames = getDatabankList()
    except FileNotFoundError:
        dbnames = []

    # %% Add test databases
    if dbname in dbnames:  # Check entries are correct
        diff = diffDatabankEntries(getDatabankEntries(dbname), dbentries, verbose=False)
        if diff is not None:
            raise ValueError(
                "{0}".format(diff)
                + "\nIn ~/.radis\n----------\n{0}".format(getDatabankEntries(dbname))
                + "\n\nExpected\n---------\n{0}\n\n".format(dbentries)
                + "Test Database {0} doesnt match expected ".format(dbname)
                + "entries for key `{0}`. See comparison above. ".format(diff)
                + "To regenerate test databases just delete the {0} ".format(dbname)
                + "entry in your ~/.radis"
            )

    else:  # add them (create ~/.radis file if doesnt exist yet)
        addDatabankEntries(dbname, dbentries)
