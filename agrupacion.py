import pandas as pd
import openpyxl
from tabulate import tabulate
columnas=[0,3]
dt=pd.read_excel("ejemplo.xlsx", sheet_name="Hoja1", header=None, usecols=columnas)
print(tabulate(dt))
print(dt[dt["28 de julio"]==0])