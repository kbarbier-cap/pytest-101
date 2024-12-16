import numpy as np
import pandas as pd

from python_unit_tests_101.pipelines import (
    PreprocessingPipeline,
    FeaturesEngineeringPipeline
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

class TestFeaturesEngineeringPipeline:

    @classmethod
    def setup_class(cls):
        """Look at this doc to know how it works
        https://docs.pytest.org/en/6.2.x/xunit_setup.html
        """
        cls.df_input = pd.DataFrame([
            [2, 20, 200],
            [5, 16, 160],
            [10, 45, 450],
        ], columns=["col1", "col2", "col3"])

    def test_create_lag_features(self):
        df_input = self.df_input

        df_output = FeaturesEngineeringPipeline.create_lag_features(df_input)

        df_expected = pd.DataFrame([
            [2, 20, 200, np.NaN, np.NaN, 160],
            [5, 16, 160, 2, np.NaN, 450],
            [10, 45, 450, 5, np.NaN, np.NaN],
        ], columns=["col1", "col2", "col3", "lag_col1", "lag_col2", "lag_col3"])

        pd.testing.assert_frame_equal(df_output, df_expected)

    def test_create_cross_features(self):
        df_input = self.df_input

        df_output = (
            FeaturesEngineeringPipeline(paramA=2)
            .create_cross_features(df_input)
        )

        df_expected = pd.DataFrame([
            [4, 20, 200, 80, 800],
            [10, 16, 160, 160, 1600],
            [20, 45, 450, 900, 9000],
        ], columns=["col1", "col2", "col3", "cross_col1_col2", "cross_col1_col3"])

        pd.testing.assert_frame_equal(df_output, df_expected)