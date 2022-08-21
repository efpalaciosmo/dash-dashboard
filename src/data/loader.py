import pandas as pd
import numpy as np
from datetime import datetime


class Dataschema:
    AMOUNT = "amount"
    CATEGORY = "category"
    DATE = "date"
    MONTH = "month"
    YEAR = "year"


def load_transaction_data(path: str) -> pd.DataFrame:
    """
    function to load the data with a proper schema
    :param path: string with the location of data to use
    :return: dataframe
    """
    # load the data from a CSV file
    data = pd.read_csv(
        path,
        dtype={
            Dataschema.AMOUNT: np.float64,
            Dataschema.CATEGORY: str
        },
        parse_dates=[Dataschema.DATE]
    )
    data[Dataschema.MONTH] = data[Dataschema.DATE].dt.month.astype(str)
    data[Dataschema.YEAR] = data[Dataschema.DATE].dt.year.astype(str)
    return data


if __name__ == "__main__":
    pass