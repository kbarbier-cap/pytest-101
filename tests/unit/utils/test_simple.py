from typing import Union

import pandas as pd

from python_unit_tests_101.utils.simple import (
    pandas_multiply_column_by_alpha
)

def test_simple_function() -> None:
    assert 1 == 1

def test_pandas_multiply_column_by_alpha() -> None:
    df_input = pd.DataFrame([
        (2, 20),
        (1, 10),
        (3, 30),
        (4, 40)
    ], columns=["col1", "col2"])

    df_output = pandas_multiply_column_by_alpha(
        df=df_input,
        column_name="col2",
        alpha=2
    )

    df_expected = pd.DataFrame([
        (2, 40),
        (1, 20),
        (3, 60),
        (4, 80)
    ], columns=["col1", "col2"])

    pd.testing.assert_frame_equal(
        df_output,
        df_expected
    )
