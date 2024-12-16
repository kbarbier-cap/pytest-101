import logging

import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def df_input_missing_values() -> pd.DataFrame:
    return pd.DataFrame([
        (None, None, 45, 1),
        (1, 10, 10, 1),
        (2, None, -1, 1),
        (None, 40, 67, 2)
    ], columns=["col1", "col2", "col3", "col4"])