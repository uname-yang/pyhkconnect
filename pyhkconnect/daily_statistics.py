# -*- coding:utf-8 -*-
from __future__ import print_function

import os
import json
from datetime import datetime
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

DAILY_URL = "https://www.hkex.com.hk/eng/csm/DailyStat/data_tab_daily_{{date}}e.js"
# DAILY_SHN_URL = "https://www.hkex.com.hk/Mutual-Market/Stock-Connect/Statistics/Historical-Daily?sc_lang=en#select4=1&select5=0"
# DAILY_SHS_URL = "https://www.hkex.com.hk/Mutual-Market/Stock-Connect/Statistics/Historical-Daily?sc_lang=en#select4=1&select5=1"
# DAILY_SZN_URL = "https://www.hkex.com.hk/Mutual-Market/Stock-Connect/Statistics/Historical-Daily?sc_lang=en#select4=1&select5=2"
# DAILY_SZS_URL = "https://www.hkex.com.hk/Mutual-Market/Stock-Connect/Statistics/Historical-Daily?sc_lang=en#select4=1&select5=3"


def statistics_northbound_sh():
    return 1

def statistics_northbound_sz():
    return 1

def top10_traded_stocks_northbound_sh():
    pass

def top10_traded_stocks_northbound_sz():
    pass


"""
TOP 10 MOST ACTIVELY TRADED STOCKS
"""
def _get_top10_most_actively_traded_stocks(URL):
    try:
        html = _fetch(URL)
        bsObj = BeautifulSoup(html, "html.parser")

        print(bsObj)
        data = []
        for tr in bsObj.find("div", {"id": "tbl__1"}).find("table").find("tbody").findAll("tr"):
            print(tr)
            # code = tr.find("td", {"class": "col-stock-code"}
            #                ).find("div", {"class": "mobile-list-body"}).get_text()
            # name = tr.find("td", {"class": "col-stock-name"}
            #                ).find("div", {"class": "mobile-list-body"}).get_text()
            # shareholding = tr.find("td", {"class": "col-shareholding"}
            #                        ).find("div", {"class": "mobile-list-body"}).get_text()
            # shareholding_percent = tr.find("td", {"class": "col-shareholding-percent"}
            #                                ).find("div", {"class": "mobile-list-body"}).get_text()

            # data.append([code, name, shareholding, shareholding_percent])

        # df = pd.DataFrame(data, columns=SHAREHOLDING_CLS)
        # return df
    except Exception as er:
        print(str(er))


def _fetch(url):
    response = requests.get(url)
    if response.status_code == 404:
        return None
    if response.status_code != 200:
        raise Exception()
    return response.content


print(_get_top10_most_actively_traded_stocks(DAILY_SHN_URL))
