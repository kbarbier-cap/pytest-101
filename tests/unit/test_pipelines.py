import pandas as pd

from python_unit_tests_101.pipelines import (
    PreprocessingPipeline
)


class TestPreprocessingPipeline:

    def test_remove_duplicates(self):
        df_input = pd.DataFrame([
            (1, 20),
            (1, 10),
            (2, 10),
            (2, 10),
            (3, 40)
        ], columns=["col1", "col2"])

        df_output = PreprocessingPipeline.remove_duplicates(
            df=df_input
        ).reset_index(drop=True)

        df_expected = pd.DataFrame([
            (1, 20),
            (1, 10),
            (2, 10),
            (3, 40)
        ], columns=["col1", "col2"])

        pd.testing.assert_frame_equal(df_output, df_expected)

    def test_remove_outliers(self):
        df_input = pd.DataFrame([
            (1, 20, 45, 1),
            (1, 10, 10, 1),
            (2, 10, -1, 1),
            (3, 40, 67, 2)
        ], columns=["col1", "col2", "col3", "col4"])

        df_output = PreprocessingPipeline(paramA=2).remove_outliers(
            df=df_input
        )

        df_expected = pd.DataFrame([
            (1, 20, 45, 1),
            (1, 10, 10, 1)
        ], columns=["col1", "col2", "col3", "col4"])

        pd.testing.assert_frame_equal(df_output, df_expected)

    def test_fill_missing_values(self, df_input_missing_values):
        df_input = df_input_missing_values

        df_output = PreprocessingPipeline.fill_missing_values(
            df=df_input
        )

        df_expected = pd.DataFrame([
            (0, 0, 45, 1),
            (1, 10, 10, 1),
            (2, 0, -1, 1),
            (0, 40, 67, 2)
        ], columns=["col1", "col2", "col3", "col4"])

        pd.testing.assert_frame_equal(
            df_output,
            df_expected,
            check_dtype=False
        )