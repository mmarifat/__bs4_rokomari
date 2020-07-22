# rokomari-scrap <br/>
This module scraps details from rokomari.com
 
 # Usage:
 It can be used in two ways:<br/>
<h6>MySQL Database</h6>
To store as MySQL database, simply import rokomari.sql into myadmin and run scrapToMysql.py
<h6>Export as CSV</h6>
To export as CSV (utf-8), simply run scrapToCsv.py

# BeautifulSoup Scraping

## Introduction

This python script will scrap data from rokomari.com about books and descriptions.

## Install the dependencies
```bash
pip3 install -r requirements.txt

# or (for python 2)

pip install -r requirements.txt
```

### Start
```bash
# For csv output
python3 scrapToCsv.py
or (for python2)
python scrapToCsv.py

# For sql output
import rokomari.sql then
python3 scrapToMysql.py
or (for python2)
python scrapToMysql.py
```

### About rokomari.com
```bash
See [rokomari.com](https://www.rokomari.com).
```