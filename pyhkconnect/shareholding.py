# -*- coding:utf-8 -*-
from __future__ import print_function

import os
import json
from datetime import datetime
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

SH_URL = "http://www.hkexnews.hk/sdw/search/mutualmarket.aspx?t="
SHAREHOLDING_CLS = ['code', 'name', 'shareholding', 'shareholding_percent']


def northbound_shareholding_sh():
    return _get_shareholding('sh')


def northbound_shareholding_sz():
    return _get_shareholding('sz')


def _get_shareholding(exchange):
    try:
        html = _fetch(SH_URL+exchange.lower())
        bsObj = BeautifulSoup(html, "html.parser")
        data = []
        for tr in bsObj.find("table", {"id": "mutualmarket-result"}).find("tbody").findAll("tr"):
            code = tr.find("td", {"class": "col-stock-code"}
                           ).find("div", {"class": "mobile-list-body"}).get_text()
            name = tr.find("td", {"class": "col-stock-name"}
                           ).find("div", {"class": "mobile-list-body"}).get_text()
            shareholding = tr.find("td", {"class": "col-shareholding"}
                                   ).find("div", {"class": "mobile-list-body"}).get_text()
            shareholding_percent = tr.find("td", {"class": "col-shareholding-percent"}
                                           ).find("div", {"class": "mobile-list-body"}).get_text()

            data.append([code, name, shareholding, shareholding_percent])

        df = pd.DataFrame(data, columns=SHAREHOLDING_CLS)
        return df
    except Exception as er:
        print(str(er))


def _fetch(url):
    response = requests.get(url)
    if response.status_code == 404:
        return None
    if response.status_code != 200:
        raise Exception()
    return response.content


# TEST
# print(northbound_shareholding())
