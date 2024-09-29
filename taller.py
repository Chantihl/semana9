import pandas as pd
import openpyxl
from tabulate import tabulate
columnas=[0,1]
de=pd.read_excel("ejemplo.xlsx", sheet_name="Hoja1", header=None)
dt=pd.read_excel("taller.xlsx", sheet_name="hoja1", header=None)
#print("Columnas del archivo:", dt.columns)
dt[6] = pd.to_numeric(dt[6], errors='coerce')
#print(dt.dtypes)

#print(tabulate(de))
#print(tabulate(dt))

#primeros_12_registros = dt.head(13)

#print("Primeros 12 nombres y apellidos:")
#print(tabulate(primeros_12_registros, headers=["Nombre", "Apellido"]))

#ultimos_9_registros = dt.tail(10)

#print("ultimos 9 nombres y apellidos: ")
#print(tabulate(ultimos_9_registros, headers=["Nombre", "Apellido"]))

#print("Nombres y apellidos que no presentaron en el día de la fecha: ")
#print(de[(de[2]==0) | (de[3]==0)  | (de[4]==0)])

#print("Nombres y apellidos que no presentaron faltas: ")
#print(de[(de[2]==1) & (de[3]==1)  & (de[4]==1)])


print("Nombres y apellidos de estudiantes que tienen nota mayor a 3: ")
print(tabulate(dt[dt[6] > 3][[0, 1, 6]]))

# Estilos del dataFrame con la libreria tabulate
#print(tabulate(de, headers='keys', tablefmt='grid'))
#print(tabulate(dt, headers='keys', tablefmt='grid'))