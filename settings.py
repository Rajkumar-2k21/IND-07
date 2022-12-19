SEARCH_KEY = "AIzaSyDCExjb4ovDyDzsB1TrueSyyb0PR3oOXCg"
SEARCH_ID = "d561244460ec743c8"
COUNTRY = "us"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT = 20

import os
if os.path.exists("private.py"):
    from private import *