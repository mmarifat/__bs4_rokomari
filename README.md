# BeautifulSoup Scraping Rokomari

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
<h6>Export as CSV (utf-8)</h6>
python3 scrapToCsv.py
or (for python2)
python scrapToCsv.py

<h6>MySQL Database</h6>
import rokomari.sql into phpMyAdmin then
python3 scrapToMysql.py
or (for python2)
python scrapToMysql.py
```

### About rokomari.com
```bash
See [rokomari.com](https://www.rokomari.com).
```