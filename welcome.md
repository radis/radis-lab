# Welcome in RADIS-lab !

![](binder/radis_ico_dark.png)

This your online environment to compute spectra and post-process them. 

It comes pre-installed with
- a scientific Python environment
- the latest RADIS version
- pre-configured [`~/databases`](./databases) 

### Get started 

Run and edit an existing notebook such as [compare_with_experiment.ipynb](./compare_with_experiment.ipynb), or start a new one from the Launcher. Each notebook can also be connected to a console for more interactive.  


### Examples 

- [examples/co2-4080-4500nm/](examples/co2-4080-4500nm/co2-4080-4500.ipynb) : CO$_2$ spectrum compared with experiment, with line-of-sight absorption, and instrumental slit function. 


### Useful links 

- [Documentation](https://radis.readthedocs.io/)
- [Discussion on Slack](https://github.com/radis/slack-invite)


### Environment

`RADIS-lab` uses the JupyterLab environment, and is deployed for you on [mybinder.org](http://mybinder.org/). The session will timeout after ~1hr of inactivity. You'll still be able to download your notebooks on timeout. You can also save/restore directly to your browser storage. 

JupyterLab can be improved with extensions. Open the `Extension Manager` on the left.

[mybinder.org](http://mybinder.org/) provides 2 Gb of RAM by default. This is enough for calculations with the HITRAN database but may be limiting for HITEMP. [GESIS.org](https://notebooks.gesis.org/) can host JupyterLab with up to 8 Gb RAM for public users and 32 Gb for registered users. We are also looking for institutions to host RADIS-lab on clusters with large RAM access. 