import pandas as pd
from django_pandas import models

import os

BASE_DIR = os.getcwd().replace("apps/algo_apps/load_pandas_df", "")
DATA_DIR = os.path.join(BASE_DIR, "data")
APP_DIR = os.path.join(DATA_DIR, "nutrition")

import warnings

warnings.filterwarnings("ignore")


def read_nutritional_data(
    file_path=f"{APP_DIR}/food_composition_table.csv", view=False
):
    df = pd.read_csv(file_path)

    ds = df[["code", "name", "scie", "lang", "grup", "regn"]]
    for col in df.columns:
        if "_e" in col:
            ds[col.replace("_e", "_min")] = df[col.replace("_e", "")] - df[col]
            ds[col.replace("_e", "_max")] = df[col.replace("_e", "")] + df[col]
    ds.fillna("", inplace=True)
    if view:
        return nutrional_data_view(ds)
    return ds


def nutrional_data_view(ds):
    dq = ds[["code", "name", "scie", "lang", "grup", "regn"]]
    for col1, col2 in zip(ds.columns, ds.columns[1:]):
        if col1.replace("_min", "") == col2.replace("_max", ""):
            dq[col1.replace("_min", "")] = (
                ds[[col1, col2]]
                .round(3)
                .apply(
                    lambda x: str(x[0]) + "-" + str(x[1]) if x[0] != x[1] else x[0],
                    axis=1,
                )
            )
    return dq


def read_columns_mapping(file_path=f"{APP_DIR}/columns_mapping.csv"):
    return pd.read_csv(file_path)


def read_indian_food_database(file_path=f"{APP_DIR}/indian_food.xlsx"):
    return pd.read_excel(file_path).fillna("").applymap(lambda x: str(x).lower())
