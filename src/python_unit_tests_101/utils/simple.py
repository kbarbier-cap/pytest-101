from typing import Union

import pandas as pd

def pandas_multiply_column_by_alpha(
    df: pd.DataFrame,
    column_name: str,
    alpha: Union[int, float]
) -> pd.DataFrame:

    return (
        df
        .assign(**{
            column_name: lambda _df:
                _df[column_name] * alpha
        })
    )
