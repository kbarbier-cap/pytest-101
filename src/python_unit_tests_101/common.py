import pandas as pd


class Task:
    def __init__(self, conf: dict = {}):

        """Imagine some code here to setup connection with your databases,
        with some tools like MlFlow, loading the conf, etc
        """

        self.conf = conf

    def read_table(self, file_path: str, **kwargs) -> pd.DataFrame:
        """Imagine that you're reading a table from a database managed in the cloud
        or in the client's servers
        """
        return pd.read_csv(file_path, **kwargs)

    def write_table(self, df: pd.DataFrame, file_path: str, **kwargs) -> None:
        """Imagine that you're writing a table in a database managed in the cloud
        or in the client's servers
        """

        df.to_csv(file_path, index=False, **kwargs)