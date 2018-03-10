import pandas as pd
import numpy as np

csv_a = input("Enter the full path of the first Budget Data file for your CSV: ")
csv_path_a = str(csv_a)
csv_path_a

bf_a = pd.read_csv(csv_path_a, encoding="utf-8")
bf_a.head()

csv_b = input("Enter the full path of the first Budget Data file for your CSV: ")
csv_path_b = str(csv_b)

bf_b = pd.read_csv(csv_path_b, encoding="utf-8")
bf_b.head()

merge_bd = pd.merge(bf_a, bf_b, on="Date")
merge_bd
