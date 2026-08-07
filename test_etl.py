import pytest

from etl import run_etl


@pytest.fixture
def etl_df():
    return run_etl()

def test_data_not_empty(etl_df):
    assert not etl_df.empty

def test_columns_exists(etl_df):
    assert "Name" in etl_df.columns
    assert "Age" in etl_df.columns
    assert "Age_in_5_years" in etl_df.columns

def test_age_trans(etl_df):
    assert all(etl_df["Age_in_5_years"] ==  etl_df["Age"] + 5)