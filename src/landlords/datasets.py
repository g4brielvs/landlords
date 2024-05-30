import pandas as pd
from sodapy import Socrata


def get_from_socrata(identifier: str, *args, **kwargs):
    """
    Retrieves data from the Socrata API for a specified dataset identifier.

    Parameters:
    identifier (str): The identifier of the dataset on Socrata

    Returns:
    pandas.DataFrame: A pandas DataFrame containing the retrieved data from Socrata.
    """
    client = Socrata("data.cityofnewyork.us", None)

    results = client.get(identifier, *args, **kwargs)
    df = pd.DataFrame.from_records(results)

    return df
