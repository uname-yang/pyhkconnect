import unittest
import sys
sys.path.append("..")

from pyhkconnect.daily_statistics import (
    top10_traded_stocks, top10_traded_stocks_by_date)


class TestDailyStatistics(unittest.TestCase):

    # def test_top10_traded_stocks(self):
    #     data = top10_traded_stocks()
    #     print (data)
    #     # self.assertEqual('foo'.upper(), 'FOO')

    def test_top10_traded_stocks_by_date(self):
        data = top10_traded_stocks_by_date(20181219)
        print(data)
        # self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
