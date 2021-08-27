RADIS databases are stored in [~/.radisdb](~/.radisdb) and registered in [~/radis.json](~/radis.json) :

```
ls ~/.radisdb
```

You can view the ~/radis.json content from RADIS with [get_config()](https://radis.readthedocs.io/en/latest/gen_modules/radis.misc.config.html#radis.misc.config.get_config):

```python
from radis import get_config
get_config()
```