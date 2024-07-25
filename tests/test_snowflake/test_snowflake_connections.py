""" Very Basic Test Suite for Snowflake Connection Objects """
import os
import numpy as np
import pandas as pd
import pytest
from dotenv import load_dotenv
from hxm_refuel.snowflake import (
    snowflake_connect,
    snowflake_sql_engine,
    snowflake_create_or_replace,
    posh_create_or_replace,
    posh_create_or_append,
)

# in order to securely test we need dummy access to Snowflake
# store data in a .env file
load_dotenv()

# pull user details from .env file
TEST_USER_DETAILS = dict(
    user=os.getenv("USER"),
    password="",
    account=os.getenv("ACCOUNT"),
    region=os.getenv("REGION"),
    authenticator="externalbrowser",
    warehouse=os.getenv("WAREHOUSE"),
    database=os.getenv("DATABASE"),
    schema="TEST_SPACE",
)

TEST_TABLE_NAME = "TEST_TABLE_DELETE"


# create a dataframe: test df to load into snowflake
@pytest.fixture
def df():

    # set seed for consistency
    np.random.seed(42)

    # Create the dummy dataframe
    return pd.DataFrame({
        'A': ['text' + str(i) for i in range(10)],
        'B': np.random.rand(10),
        'C': np.random.rand(10),
    })


@pytest.fixture
def conn():
    """ Connection Object: For putting data """
    return snowflake_connect(
        user_details=TEST_USER_DETAILS,
        method='user',
        password=None,
        private_key_file=None,
        raw=True,
    )


@pytest.fixture
def engine():
    """ Engine Object: For pulling data """
    return snowflake_sql_engine(
        user_details=TEST_USER_DETAILS,
        method='user',
        password=None,
        private_key_file=None,
        raw=True,
    )


class TestSnowflakeConnect:
    """ This is basic test suite, with very limited functionality tests"""

    def test_snowflake_create_or_replace(self, df, conn):
        """ Push dummy dataframe to Snowflake Test Table """
        snowflake_create_or_replace(df, conn, TEST_TABLE_NAME)

    def test_snowflake_engine_query(self, df, engine):
        """ Pull dummy table from Snowflake and Test is matches Dummy Dataframe """
        result = pd.read_sql_query(f"SELECT * FROM {TEST_TABLE_NAME}", con=engine)
        pd.testing.assert_frame_equal(df, result, check_index_type=False, check_column_type=False, atol=1e-4)
