# HongXiongMao Refuel

Toolbox for importing data from various financial sources; 
for a personal project so if you are here by accident I highly advise you look elsewhere.


## Bloomberg API
In order to make calls to Bloomberg we must have the `blpapi` installed. 
We then extend the excellent `xbbg` package. 
One complication is the installation of `blpapi` which is a bit of a pain in the backside.

According to the [Bloomberg website](https://www.bloomberg.com/professional/support/api-library/) 
one can install using pip with:

```angular2html
python -m pip install --index-url=https://bcms.bloomberg.com/pip/simple blpapi
```

For Poetry there are 2 steps required: Setting up Bloomberg as a source & then installing.

```angular2html
# set up Bloomberg URL as a source
poetry source add --priority bloomberg https://bcms.bloomberg.com/pip/simple

# poetry add blpapi
poetry add --source bloomberg blpapi 
```

This shows up in the pyproject.toml file like:
```angular2html
blpapi = {version = "^3.21.0", source = "bloomberg"}

[[tool.poetry.source]]
name = "bloomberg"
url = "https://bcms.bloomberg.com/pip/simple"
priority = "supplemental"
```
