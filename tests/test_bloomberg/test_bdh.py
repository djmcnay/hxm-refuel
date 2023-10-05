import pytest
import pandas as pd
from hxm_refuel.bloomberg.bloomberg_api import bdh

# dict of BDH inputs which are standard
# these are selected to minimise the amount of data pulled from Bloomberg
STANDARD_ARGS = dict(
    freq='EOM',
    t0='20191231',
    t1='20200301',
)


class TestBloombergBDH:
    """ Tests for the Bloomberrg BDH functionality """

    def test_testing(self):
        """ Just to confirm testing suite is working"""
        assert 1 == 1

    def test_bdh_dataframe_index_name(self):
        """ Test DataFrame Index Name is 'date'"""
        df = bdh('SPX Index', 'PX_LAST', multi_index=False, **STANDARD_ARGS)
        assert df.index.name == 'date'

    @pytest.mark.parametrize("tickers, fields, solution", [
        ("SPX Index", "PX_LAST", ["SPX Index"]),
        (["SPX Index", "UKX Index"], "PX_LAST", ["SPX Index", "UKX Index"]),
        (["SPX Index"], ["PX_LAST", "PX_VOLUME"], ["PX_LAST", "PX_VOLUME"]),
        (["SPX Index", "UKX Index"], ["PX_LAST", "PX_VOLUME"],
         ["SPX Index | PX_LAST", "SPX Index | PX_VOLUME", "UKX Index | PX_LAST", "UKX Index | PX_VOLUME"]),
        ({"SPX Index": 'SPX', "UKX Index": 'UKX'}, {"PX_LAST": "PX", "PX_VOLUME": "VOL"},
         ["SPX | PX", "SPX | VOL", "UKX | PX", "UKX | VOL"]),
    ])
    def test_bdh_dataframe_columns_multi_index_false(self, tickers, fields, solution):
        """ Tests which check correct column format for a non-multi_index return """
        df = bdh(tickers, fields, multi_index=False, **STANDARD_ARGS)
        assert list(df.columns) == solution, f"result should be {solution}; df.columns={df.columns}"
