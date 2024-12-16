from pandas import DataFrame as PandasDataFrame

def df_multiply_col_by_alpha(
    df: PandasDataFrame,
    col: str,
    alpha: int
) -> PandasDataFrame:
    return df.assign(**{
        col: lambda _df: _df[col] * alpha
    })