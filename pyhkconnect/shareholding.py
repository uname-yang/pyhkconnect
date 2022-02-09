# -*- coding:utf-8 -*-
from __future__ import print_function

from datetime import datetime
from urllib import parse

import pandas as pd
import requests
from bs4 import BeautifulSoup

SH_URL = "https://www.hkexnews.hk/sdw/search/mutualmarket.aspx?t="
SHAREHOLDING_CLS = ['code', 'name', 'shareholding', 'shareholding_percent']


def northbound_shareholding_sh(txt_date=None):
    """
    date: '%Y/%m/%d'
    """
    return _get_shareholding('sh', txt_date)


def northbound_shareholding_sz(txt_date=None):
    """
    date: '%Y/%m/%d'
    """
    return _get_shareholding('sz', txt_date)


def _get_shareholding(exchange, txt_date):
    try:
        html = _fetch(SH_URL + exchange.lower(), txt_date)
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


def _fetch(url, txt_date=None):
    today = datetime.today()
    if txt_date is None:
        txt_date = today.strftime('%Y/%m/%d')
    today_str = today.strftime('%Y%m%d')
    payload = {
        '__VIEWSTATE': '/wEPDwUJNjIxMTYzMDAwZGSFj8kdzCLeVLiJkFRvN5rjsPotqw==',
        '__VIEWSTATEGENERATOR': '3C67932C',
        '__EVENTVALIDATION': '/wEdAAdbi0fj+ZSDYaSP61MAVoEdVobCVrNyCM2j+bEk3ygqmn1KZjrCXCJtWs9HrcHg6Q64ro36uTSn/Z2SUlkm9HsG7WOv0RDD9teZWjlyl84iRMtpPncyBi1FXkZsaSW6dwqO1N1XNFmfsMXJasjxX85ju3P1WAPUeweM/r0/uwwyYLgN1B8=',
        'today': today_str,
        'sortBy': 'stockcode',
        'sortDirection': 'asc',
        'alertMsg': '',
        'txtShareholdingDate': txt_date,
        'btnSearch': 'Search'
    }
    payload = parse.urlencode(payload)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 404:
        return None
    if response.status_code != 200:
        raise Exception()
    return response.content


# TEST
# print(northbound_shareholding())
