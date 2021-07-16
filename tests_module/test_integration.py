from poo_module.src.api.currency_api import DaySummaryAPI
from datetime import datetime

class TestDaySummaryAPI:

    def test_get_data_check_date(self):
        actual = DaySummaryAPI(currency = 'BTC').get_data(datetime(2021, 1, 1)).get('date')
        expected = '2021-01-01'
        assert actual == expected

    def test_get_data(self):
        actual = DaySummaryAPI(currency = 'BTC').get_data(datetime(2021, 1, 1))
        expected = {'date': '2021-01-01', 'opening': 152700.00002, 'closing': 153458.29999999, 'lowest': 151539, 'highest': 153975, 'volume': 12583384.54790148, 'quantity': 82.27265844, 'amount': 4824, 'avg_price': 152947.34346135}
        assert actual == expected