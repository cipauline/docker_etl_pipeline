import pandas as pd
import numpy as np


def transform_data(data):

    # querying the dataframe based on the columns we need as well as the state we need (CA - California)
    # since there is the data on all the states in the dataframe

    transformed_data = data.query('STATE == "CA"')[
        [
            "FIRE_YEAR",
            "DISCOVERY_DATE",
            "DISCOVERY_DOY",
            "NWCG_CAUSE_CLASSIFICATION",
            "NWCG_GENERAL_CAUSE",
            "CONT_DATE",
            "CONT_DOY",
            "FIRE_SIZE",
            "FIRE_SIZE_CLASS",
            "OWNER_DESCR",
        ]
    ]

    # getting rid of the nulls (since they cannot be replaced with neighbouring values
    # as well as filled in by me (since nulls are the dates of the wildfires being over))

    transformed_data = transformed_data.dropna()

    # turning date values to datetime type and adding two new columns - month of the wildfire and a season

    transformed_data["DISCOVERY_DATE"] = pd.to_datetime(
        transformed_data["DISCOVERY_DATE"], errors="coerce"
    )
    transformed_data["CONT_DATE"] = pd.to_datetime(
        transformed_data["CONT_DATE"], errors="coerce"
    )

    def to_season(month):
        if month in (1, 2, 12):
            return "Winter"
        elif month in (3, 4, 5):
            return "Spring"
        elif month in (6, 7, 8):
            return "Summer"
        elif month in (9, 10, 11):
            return "Autumn"
        else:
            return np.nan

    transformed_data["MONTH"] = transformed_data["DISCOVERY_DATE"].dt.month
    transformed_data["SEASON"] = transformed_data["MONTH"].apply(to_season)

    transformed_data.columns = transformed_data.columns.str.lower()

    return transformed_data
