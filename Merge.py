import pandas as pd

csv1 = pd.read_csv("data\mycsv1.csv",
                   sep=";",
                   decimal=",")
csv1.head()

csv2 = pd.read_csv("data\mycsv2.csv",
                   sep=";",
                   decimal=",")
csv2.head()

dfMerged = pd.merge(csv1, csv2,
                    how='left',
                    left_on='cod_col_csv1',
                    right_on='cod_col_csv2')
dfMerged.head()

dfMerged.to_csv("data/MergedData.csv",
                sep=';',
                index=False,
                header=True)
