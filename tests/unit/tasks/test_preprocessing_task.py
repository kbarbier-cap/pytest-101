import pandas as pd

from python_unit_tests_101.tasks.preprocessing_task import PreprocessingTask

class MockPreprocessingTask(PreprocessingTask):
    def __init__(self):
        self.conf = {}
        self.conf["table_input"] = "blablabla I'm not testing that"

class TestPreprocessingTask:

    @classmethod
    def setup_class(cls):
        cls.task = MockPreprocessingTask()

    def test_add_source_before_writing(self):
        df_input = pd.DataFrame([
            (1, 20),
            (1, 10),
            (2, 10),
            (2, 10),
            (3, 40)
        ], columns=["col1", "col2"])

        df_output = self.task.add_source_before_writing(df_input)

        assert "source" in df_output.columns
