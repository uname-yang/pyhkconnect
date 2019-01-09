# pyhkconnect

香港交易所 沪港通 深港通 数据接口

## Install

```bash
pip install pyhkconnect
```

## Demo

```python
>>> import pyhkconnect as hkc
>>> dp = hkc.northbound_shareholding_sh() # dataframe from pandas
>>> dp
      code                                               name   shareholding shareholding_percent
0    90000  SHANGHAI PUDONG DEVELOPMENT BANK CO., LTD. (A ...    379,430,135                1.35%
1    90004  GUANGZHOU BAIYUN INTERNATIONAL AIRPORT CO.,LTD...    282,353,856               13.64%
2    90006            DONGFENG AUTOMOBILE CO.,LTD (A #600006)      7,461,913                0.37%
3    90007  CHINA WORLD TRADE CENTER COMPANY LTD. (A #600007)     13,202,103                1.31%
4    90008                BEIJING CAPITAL CO.,LTD (A #600008)     63,689,287                1.32%
5    90009  SHANGHAI INTERNATIONAL AIRPORT CO., LTD. (A #6...    316,733,029               28.96%
6    90010  INNER MONGOLIA BAOTOU STEEL UNION CO.,LTD. (A ...    215,362,295                0.67%
7    90011      HUANENG POWER INTERNATIONAL, INC. (A #600011)     42,917,773                0.40%
8    90012       ANHUI EXPRESSWAY COMPANY LIMITED (A #600012)      6,149,168                0.52%
9    90015              HUA XIA BANK CO., LIMITED (A #600015)     83,923,960                0.65%
10   90016     CHINA MINSHENG BANKING CORP., LTD. (A #600016)    594,264,189                1.67%
..     ...                                                ...            ...                  ...
840  93979        JCHX MINING MANAGEMENT CO.,LTD. (A #603979)        191,590                0.03%
841  93986  GIGADEVICE SEMICONDUCTOR(BEIJING) INC (A #603986)        358,240                0.17%
842  93989             HUNAN AIHUA GROUP C0.,LTD. (A #603989)      5,537,526                1.41%
843  93993             CHINA MOLYBDENUM CO., LTD. (A #603993)    133,230,718                0.75%
844  93997       NINGBO JIFENG AUTO PARTS CO.,LTD (A #603997)        100,463                0.01%

[845 rows x 4 columns]
>>>
>>>json_obj=dp.to_json(orient='index') # return json data
```

## APIs

### 获取北上沪港通持股数据

```python
import pyhkconnect as hkc
hkc.statistics_northbound_sh()
```

### 获取北上深港通持股数据

```python
import pyhkconnect as hkc
hkc.statistics_northbound_sz()
```

---

有任何问题请联系我。

![wechat](qrcode.jpg)