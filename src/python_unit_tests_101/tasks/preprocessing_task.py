from argparse import ArgumentParser
from typing import Tuple

from loguru import logger
from pandas import DataFrame as PandasDataFrame

from python_unit_tests_101.common import Task
from python_unit_tests_101.pipelines import PreprocessingPipeline

class PreprocessingTask(Task):
    def __init__(self):
        Task.__init__(
            self,
            conf={
                "paramA": 10,
                "table_input": "data/01_raw/data.csv",
                "table_output": "data/02_preprocess/data_preprocessed.csv"
            }
        )

    def read_data(self) -> PandasDataFrame:
        return self.read_table(self.conf["table_input"])

    def add_source_before_writing(self, df: PandasDataFrame) -> PandasDataFrame:
        return (
            df
            .assign(
                source=self.conf["table_input"]
            )
        )

    def write_data(self, df: PandasDataFrame) -> None:
        self.write_table(df, self.conf["table_output"])

    def launch(self):
        logger.info("Launching PreprocessingTask")
        df = self.read_data()

        df = PreprocessingPipeline(
            paramA=self.conf["paramA"]
        ).run(df)

        df = self.add_source_before_writing(df)

        self.write_data(df)
        logger.info("PreprocessingTask finished!")


if __name__ == '__main__':
    task = PreprocessingTask()
    task.launch()