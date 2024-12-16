from pandas import DataFrame as PandasDataFrame

from python_unit_tests_101.utils.features_engineering import df_multiply_col_by_alpha


class PreprocessingPipeline:
    def __init__(self, paramA: int):
        self.paramA = paramA

    @staticmethod
    def remove_duplicates(df: PandasDataFrame) -> PandasDataFrame:
        return (
            df
            .drop_duplicates(subset=[
                "col1",
                "col2"
            ])
        )

    def remove_outliers(self, df: PandasDataFrame) -> PandasDataFrame:
        return (
            df
            .query("(col3 > 0) & (col3 < 100)")
            .query(f"(col4 != {self.paramA})")
        )

    @staticmethod
    def fill_missing_values(df: PandasDataFrame) -> PandasDataFrame:
        return (
            df
            .fillna({
                "col1": 0,
                "col2": 0
            })
        )

    def run(self, df: PandasDataFrame) -> PandasDataFrame:
        df = self.remove_duplicates(df)
        df = self.remove_outliers(df)
        df = self.fill_missing_values(df)

        return df


class FeaturesEngineeringPipeline:
    def __init__(self, paramA: int):
        self.paramA = paramA

    @staticmethod
    def create_lag_features(df: PandasDataFrame):
        return (
            df
            .assign(lag_col1=lambda _df: _df["col1"].shift(1))
            .assign(lag_col2=lambda _df: _df["col2"].shift(3))
            .assign(lag_col3=lambda _df: _df["col3"].shift(-1))
        )


    def create_cross_features(self, df: PandasDataFrame):
        df = df_multiply_col_by_alpha(df, "col1", self.paramA)

        return (
            df
            .assign(cross_col1_col2=lambda _df: _df["col1"] * _df["col2"])
            .assign(cross_col1_col3=lambda _df: _df["col1"] * _df["col3"])
        )


    def run(self, df: PandasDataFrame):
        df = self.create_lag_features(df)
        df = self.create_cross_features(df)

        return df
