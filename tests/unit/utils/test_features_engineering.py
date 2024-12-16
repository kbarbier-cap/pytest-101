import pandas as pd

from python_unit_tests_101.utils.features_engineering import df_multiply_col_by_alpha

def test_df_multiply_col_by_alpha():

    df_input = pd.DataFrame([
        [2, 20],
        [5, 16],
    ], columns=["col1", "col2"])

    df_output = df_multiply_col_by_alpha(
        df_input,
        col="col1",
        alpha=2
    )

    df_expected = df_input = pd.DataFrame([
        [4, 20],
        [10, 16],
    ], columns=["col1", "col2"])

    pd.testing.assert_frame_equal(df_output, df_expected)